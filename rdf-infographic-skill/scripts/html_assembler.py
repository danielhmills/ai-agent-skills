"""Assemble RDF data into a self-contained HTML infographic."""

from __future__ import annotations
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from html import escape
from urllib.parse import quote

try:
    from jinja2 import Environment, FileSystemLoader, Template
    HAS_JINJA = True
except ImportError:
    HAS_JINJA = False
    from string import Template as StrTemplate

from rdf_parser import build_kgdata, extract_narrative, get_base_iri, validate_orphans


HERE = Path(__file__).parent
TEMPLATES_DIR = HERE / "templates"
VALIDATOR = HERE / "validate-harness-contract.py"


def load_asset(name: str) -> str:
    path = TEMPLATES_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"Missing template asset: {path}")
    return path.read_text(encoding="utf-8")


def make_resolver_link(iri: str, resolver_pattern: str = "https://linkeddata.uriburner.com/describe/?url=") -> str:
    return resolver_pattern + quote(iri, safe="")


def make_section_html(section_id: str, title: str, inner_html: str) -> str:
    return (
        f'<section class="section section-alt" id="{section_id}">'
        f'<h2>{title}<a class="headline-anchor" href="#{section_id}" aria-label="Link to this section">¶</a></h2>'
        f'{inner_html}'
        f'</section>'
    )


def render_narrative(rdf_path: str | Path, base_iri: str, resolver_pattern: str) -> tuple[str, list[dict]]:
    """Extract and render narrative sections from RDF annotations."""
    narrative = extract_narrative(rdf_path, base_iri)
    nav_links = [
        {"href": "#hero", "label": "Overview"},
    ]
    html_parts = []
    sections = []

    has_faq = len(narrative["faq"]) > 0
    has_glossary = len(narrative["glossary"]) > 0
    has_howto = len(narrative["howto"]) > 0
    has_people = len(narrative["people"]) > 0
    has_orgs = len(narrative["organizations"]) > 0

    if has_people:
        items_html = ""
        for p in narrative["people"]:
            iri = p["iri"]
            name = escape(p["name"])
            desc = escape(p["description"]) if p["description"] else ""
            items_html += (
                f'<div class="card">'
                f'<h3><a href="{make_resolver_link(iri, resolver_pattern)}" target="_blank" rel="noopener noreferrer">{name}</a></h3>'
                f'<p>{desc}</p></div>'
            )
        html_parts.append(render_narrative_section("people", "People", f'<div class="cards-grid">{items_html}</div>'))
        nav_links.append({"href": "#people", "label": "People"})
        sections.append("people")

    if has_orgs:
        items_html = ""
        for o in narrative["organizations"]:
            iri = o["iri"]
            name = escape(o["name"])
            desc = escape(o["description"]) if o["description"] else ""
            items_html += (
                f'<div class="card">'
                f'<h3><a href="{make_resolver_link(iri, resolver_pattern)}" target="_blank" rel="noopener noreferrer">{name}</a></h3>'
                f'<p>{desc}</p></div>'
            )
        html_parts.append(render_narrative_section("organizations", "Organizations", f'<div class="cards-grid">{items_html}</div>'))
        nav_links.append({"href": "#organizations", "label": "Organizations"})
        sections.append("organizations")

    if has_faq:
        items_html = '<div class="faq-list">'
        for faq in narrative["faq"]:
            iri = faq["iri"]
            q = escape(faq["question"])
            a = escape(faq["answer"])
            link_open = f'<a href="{make_resolver_link(iri, resolver_pattern)}" target="_blank" rel="noopener noreferrer">' if iri else ""
            link_close = "</a>" if iri else ""
            items_html += (
                f'<div class="faq-item anim-fade">'
                f'<div class="faq-question">{link_open}{q}{link_close}<span class="faq-chevron">▼</span></div>'
                f'<div class="faq-answer"><p>{a}</p></div>'
                f'</div>'
            )
        items_html += "</div>"
        html_parts.append(render_narrative_section("faq", "Frequently Asked Questions", items_html))
        nav_links.append({"href": "#faq", "label": "FAQ"})
        sections.append("faq")

    if has_glossary:
        items_html = '<div class="glossary-grid">'
        for g in narrative["glossary"]:
            iri = g["iri"]
            term = escape(g["term"])
            defn = escape(g["definition"])
            link_open = f'<a href="{make_resolver_link(iri, resolver_pattern)}" target="_blank" rel="noopener noreferrer">' if iri else ""
            link_close = "</a>" if iri else ""
            items_html += (
                f'<div class="glossary-term">'
                f'<h4>{link_open}{term}{link_close}</h4>'
                f'<p>{defn}</p></div>'
            )
        items_html += "</div>"
        html_parts.append(render_narrative_section("glossary", "Glossary of Terms", items_html))
        nav_links.append({"href": "#glossary", "label": "Glossary"})
        sections.append("glossary")

    if has_howto:
        items_html = '<div class="howto-list">'
        for i, step in enumerate(narrative["howto"], 1):
            iri = step["iri"]
            s = escape(step["step"])
            desc = escape(step["description"]) if step["description"] else ""
            link_open = f'<a href="{make_resolver_link(iri, resolver_pattern)}" target="_blank" rel="noopener noreferrer">' if iri else ""
            link_close = "</a>" if iri else ""
            items_html += (
                f'<div class="howto-step anim-fade">'
                f'<div class="howto-num">{i}</div>'
                f'<div class="howto-content">'
                f'<h4>{link_open}{s}{link_close}</h4>'
                f'<p>{desc}</p></div></div>'
            )
        items_html += "</div>"
        html_parts.append(render_narrative_section("howto", "How-To Guide", items_html))
        nav_links.append({"href": "#howto", "label": "HowTo"})
        sections.append("howto")

    nav_links.extend([
        {"href": "#kg-explorer", "label": "KG Explorer"},
        {"href": "#sparql-explorer", "label": "SPARQL"},
        {"href": "#footer", "label": "Footer"},
    ])

    return "\n".join(html_parts), nav_links, sections


def render_narrative_section(section_id: str, title: str, inner_html: str) -> str:
    return make_section_html(section_id, title, inner_html)


def render_jsonld(title: str, description: str, base_iri: str, rdf_rel_path: str) -> str:
    ld = {
        "@context": {
            "@vocab": "http://schema.org/",
            "@language": "en",
        },
        "@type": "Article",
        "@id": base_iri,
        "headline": title,
        "description": description,
        "mainEntity": {
            "@type": "CreativeWork",
            "@id": base_iri,
        },
        "sameAs": rdf_rel_path,
    }
    return json.dumps(ld, indent=2)


def build_sparql_recipes(base_iri: str) -> list[dict]:
    return [
        {
            "label": "All triples (sample)",
            "query": f"SELECT ?s ?p ?o\nWHERE {{ ?s ?p ?o }}\nLIMIT 25",
        },
        {
            "label": "Entity types summary",
            "query": f"SELECT ?type (COUNT(?s) AS ?count)\nWHERE {{ ?s a ?type }}\nGROUP BY ?type\nORDER BY DESC(?count)",
        },
        {
            "label": "Named graph triples",
            "query": f"SELECT ?s ?p ?o\nFROM <{base_iri}>\nWHERE {{ ?s ?p ?o }}\nLIMIT 25",
        },
    ]


def assemble_html(
    rdf_path: str | Path,
    output_path: str | Path,
    title: str = "",
    description: str = "",
    source_url: str = "",
    source_label: str = "",
    resolver_pattern: str = "https://linkeddata.uriburner.com/describe/?url=",
    tagline: str = "",
    hero_tagline: str = "",
    meta_html: str = "",
) -> bool:
    """Assemble a complete HTML infographic from an RDF file.

    Returns True on success, False on failure.
    """
    rdf_path = Path(rdf_path)
    output_path = Path(output_path)
    stem = rdf_path.stem

    # Resolve base IRI
    base_iri = get_base_iri(rdf_path)

    if not title:
        title = f"Knowledge Graph Infographic — {stem}"
    if not description:
        description = f"Interactive infographic generated from {rdf_path.name}"

    # Compute relative path for RDF link from output
    rdf_rel = os.path.relpath(str(rdf_path.resolve()), start=str(output_path.parent.resolve()))
    rdf_filename = rdf_path.name

    # Build kgData
    print("Parsing RDF...")
    kgdata = build_kgdata(rdf_path)
    print(f"  Nodes: {len(kgdata['nodes'])}, Links: {len(kgdata['links'])}")

    # Validate orphans
    orphans = validate_orphans(kgdata)
    if orphans:
        print(f"  Warning: {len(orphans)} orphan nodes — {orphans}")
    else:
        print("  Zero orphan nodes")

    # Render narrative
    print("Extracting narrative...")
    narrative_html, nav_links, sections = render_narrative(rdf_path, base_iri, resolver_pattern)
    print(f"  Sections: {', '.join(sections)}")

    # Build JSON-LD
    jsonld_content = render_jsonld(title, description, base_iri, rdf_rel)

    # Build SPARQL recipes
    sparql_recipes = build_sparql_recipes(base_iri)
    default_sparql = sparql_recipes[0]["query"]

    # Load assets
    css_content = load_asset("styles.css")
    kg_explorer_js = load_asset("kg_explorer.js")

    # Serialize kgData
    kgdata_json = json.dumps(kgdata, separators=(",", ":"))

    # Template context
    context = {
        "title": title,
        "description": description,
        "tagline": tagline,
        "hero_tagline": hero_tagline,
        "meta_html": meta_html,
        "rdf_rel_path": rdf_rel,
        "rdf_filename": rdf_filename,
        "output_filename": output_path.name,
        "base_iri": base_iri,
        "css_content": css_content,
        "jsonld_content": jsonld_content,
        "kgdata_json": kgdata_json,
        "kg_explorer_js": kg_explorer_js,
        "nav_links": nav_links,
        "narrative_html": narrative_html,
        "sparql_recipes": sparql_recipes,
        "default_sparql": default_sparql,
        "source_url": source_url,
        "source_label": source_label,
    }

    # Render template
    print("Assembling HTML...")
    if HAS_JINJA:
        env = Environment(
            loader=FileSystemLoader(str(TEMPLATES_DIR)),
            autoescape=False,
        )
        template = env.get_template("base_template.html")
        html = template.render(**context)
    else:
        # Fallback to string.Template
        template_str = load_asset("base_template.html")
        # Convert Jinja2 syntax to $var syntax
        template_str = re.sub(r"\{\{ (\w+) \}\}", r"$\1", template_str)
        template_str = re.sub(r"\{% for (\w+) in (\w+) %\}(.*?)\{% endfor %\}", r"<!-- loop: \1 in \2 -->\3<!-- end loop -->", template_str, flags=re.S)
        template_str = re.sub(r"\{% if (.*?) %\}(.*?)\{% endif %\}", r"\2", template_str, flags=re.S)
        template = StrTemplate(template_str)
        html = template.safe_substitute(**{k: str(v) for k, v in context.items()})

    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    print(f"Written: {output_path} ({output_path.stat().st_size / 1024:.1f} KB)")

    # Validate
    if VALIDATOR.exists():
        print("Running harness contract validation...")
        cmd = [sys.executable, str(VALIDATOR), str(output_path), "--ttl", str(rdf_path)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("  PASS")
            return True
        else:
            print("  FAIL")
            print("  " + result.stdout.replace("\n", "\n  "))
            return False
    else:
        print(f"  Validator not found at {VALIDATOR}")
        return True
