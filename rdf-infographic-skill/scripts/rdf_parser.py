"""Parse RDF documents and extract KG Explorer data + narrative sections."""

from __future__ import annotations
import re
from pathlib import Path
from rdflib import Graph, URIRef, BNode, Literal
from rdflib.namespace import RDF, RDFS, OWL, XSD, Namespace


SCHEMA = Namespace("http://schema.org/")
PROV = Namespace("http://www.w3.org/ns/prov#")
KNOWN_CLASS_URIS = {
    RDF.Property, RDFS.Class, OWL.Class, OWL.NamedIndividual,
    SCHEMA.Person, SCHEMA.Organization, SCHEMA.Article,
    SCHEMA.FAQPage, SCHEMA.Question, SCHEMA.DefinedTermSet,
    SCHEMA.DefinedTerm, SCHEMA.HowTo, SCHEMA.HowToStep,
    SCHEMA.SoftwareApplication, SCHEMA.SoftwareSourceCode,
    SCHEMA.Thing, SCHEMA.CreativeWork,
}


def classify(node_uri: URIRef, g: Graph) -> str:
    """Classify a URIRef node as Class, Property, or Instance."""
    types = set(g.objects(node_uri, RDF.type))
    if not types:
        # Check if it's used as a predicate
        if (None, node_uri, None) in g or (node_uri, RDF.type, RDF.Property) in g:
            return "Property"
        # Check if it's used as a class
        for s, p, o in g:
            if p == RDF.type and o == node_uri:
                return "Class"
        return "Instance"

    for t in types:
        if t in (RDFS.Class, OWL.Class):
            return "Class"
        if t == RDF.Property:
            return "Property"

    for t in types:
        if t in KNOWN_CLASS_URIS:
            return "Instance"

    return "Instance"


def shorten(uri: URIRef, g: Graph) -> str:
    """Try to shorten a URI using namespace prefixes from the graph."""
    for prefix, ns in g.namespaces():
        if str(uri).startswith(str(ns)):
            return f"{prefix}:{str(uri)[len(str(ns)):]}"
    # Last resort: extract local name
    uri_str = str(uri)
    if "#" in uri_str:
        return uri_str.split("#")[-1]
    return uri_str.split("/")[-1] if "/" in uri_str else uri_str


def extract_label(uri: URIRef, g: Graph) -> str:
    """Extract the best label for a URI."""
    for label in g.objects(uri, RDFS.label):
        return str(label)
    for label in g.objects(uri, SCHEMA.name):
        return str(label)
    return shorten(uri, g)


def extract_description(uri: URIRef, g: Graph) -> str:
    """Extract description/comment for a URI."""
    for desc in g.objects(uri, RDFS.comment):
        return str(desc)[:200]
    for desc in g.objects(uri, SCHEMA.description):
        return str(desc)[:200]
    return ""


def build_kgdata(rdf_path: str | Path) -> dict:
    """Build kgData payload from an RDF file.

    Returns: {'nodes': [...], 'links': [...]}
    """
    g = Graph()
    g.parse(str(rdf_path))

    nodes_map: dict[str, dict] = {}
    links: list[dict] = []
    seen_predicates: set[str] = set()

    for s, p, o in g:
        if isinstance(s, BNode) or isinstance(o, BNode) and isinstance(p, URIRef):
            continue

        pred_short = shorten(p, g) if isinstance(p, URIRef) else str(p)
        seen_predicates.add(pred_short)

        subj_id = str(s) if isinstance(s, URIRef) else f"_:{s}"
        obj_id = str(o) if isinstance(o, URIRef) else f"_:{o}"

        # Add subject node
        if subj_id not in nodes_map and isinstance(s, URIRef):
            nodes_map[subj_id] = {
                "id": subj_id,
                "group": classify(s, g),
                "label": extract_label(s, g),
                "desc": extract_description(s, g),
                "iri": str(s),
            }

        # Add object node
        if obj_id not in nodes_map and isinstance(o, URIRef):
            nodes_map[obj_id] = {
                "id": obj_id,
                "group": classify(o, g),
                "label": extract_label(o, g),
                "desc": extract_description(o, g),
                "iri": str(o),
            }

        # Add link
        if isinstance(p, URIRef) and isinstance(s, (URIRef, BNode)) and isinstance(o, (URIRef, BNode)):
            link = {
                "source": subj_id,
                "target": obj_id,
                "predicate": pred_short,
                "label": pred_short,
            }
            links.append(link)

    nodes = list(nodes_map.values())

    # Orphan check
    incident_ids: set[str] = set()
    for link in links:
        incident_ids.add(link["source"] if isinstance(link["source"], str) else link["source"])
        incident_ids.add(link["target"] if isinstance(link["target"], str) else link["target"])
    orphans = [n for n in nodes if n["id"] not in incident_ids]
    if orphans:
        orphan_ids = [n["id"] for n in orphans]
        print(f"Warning: {len(orphans)} orphan nodes found: {orphan_ids}")

    return {
        "nodes": nodes,
        "links": links,
    }


def extract_narrative(rdf_path: str | Path, base_iri: str) -> dict:
    """Extract narrative sections (FAQ, glossary, HowTo, People, Orgs) from RDF."""
    g = Graph()
    g.parse(str(rdf_path))

    result = {
        "faq": [],
        "glossary": [],
        "howto": [],
        "people": [],
        "organizations": [],
    }

    # FAQ
    for faq in g.subjects(RDF.type, SCHEMA.FAQPage):
        for q_item in g.objects(faq, SCHEMA.hasPart):
            q_text = extract_label(q_item, g) if isinstance(q_item, URIRef) else str(q_item)
            a_iri = None
            for a_item in g.objects(q_item, SCHEMA.acceptedAnswer):
                a_iri = a_item
                break
            a_text = ""
            for txt in g.objects(a_item, SCHEMA.text):
                a_text = str(txt)
                break
            for txt in g.objects(a_item, RDFS.comment):
                if not a_text:
                    a_text = str(txt)
                break
            if q_text and a_text:
                result["faq"].append({
                    "question": q_text,
                    "answer": a_text,
                    "iri": str(q_item) if isinstance(q_item, URIRef) else "",
                })

    # Fallback: look for Question nodes directly
    if not result["faq"]:
        for q in g.subjects(RDF.type, SCHEMA.Question):
            q_text = extract_label(q, g) or ""
            for a in g.objects(q, SCHEMA.acceptedAnswer):
                a_text = ""
                for txt in g.objects(a, SCHEMA.text):
                    a_text = str(txt)
                    break
                if q_text and a_text:
                    result["faq"].append({
                        "question": q_text,
                        "answer": a_text,
                        "iri": str(q) if isinstance(q, URIRef) else "",
                    })

    # Glossary
    for term_set in g.subjects(RDF.type, SCHEMA.DefinedTermSet):
        for term in g.objects(term_set, SCHEMA.hasPart):
            term_text = extract_label(term, g) if isinstance(term, URIRef) else str(term)
            term_desc = extract_description(term, g) if isinstance(term, URIRef) else ""
            if term_text and term_desc:
                result["glossary"].append({
                    "term": term_text,
                    "definition": term_desc,
                    "iri": str(term) if isinstance(term, URIRef) else "",
                })

    # Fallback glossary: DefinedTerm nodes
    if not result["glossary"]:
        for term in g.subjects(RDF.type, SCHEMA.DefinedTerm):
            term_text = extract_label(term, g) or ""
            desc = extract_description(term, g) or ""
            if term_text:
                result["glossary"].append({
                    "term": term_text,
                    "definition": desc,
                    "iri": str(term) if isinstance(term, URIRef) else "",
                })

    # HowTo
    for howto in g.subjects(RDF.type, SCHEMA.HowTo):
        for step in g.objects(howto, SCHEMA.step):
            step_text = extract_label(step, g) if isinstance(step, URIRef) else str(step)
            step_desc = extract_description(step, g) if isinstance(step, URIRef) else ""
            if step_text:
                result["howto"].append({
                    "step": step_text,
                    "description": step_desc,
                    "iri": str(step) if isinstance(step, URIRef) else "",
                })

    # People
    for person in g.subjects(RDF.type, SCHEMA.Person):
        name = extract_label(person, g)
        if name:
            desc = extract_description(person, g)
            result["people"].append({
                "name": name,
                "description": desc,
                "iri": str(person) if isinstance(person, URIRef) else "",
            })

    # Organizations
    for org in g.subjects(RDF.type, SCHEMA.Organization):
        name = extract_label(org, g)
        if name:
            desc = extract_description(org, g)
            result["organizations"].append({
                "name": name,
                "description": desc,
                "iri": str(org) if isinstance(org, URIRef) else "",
            })

    return result


def get_base_iri(rdf_path: str | Path) -> str:
    """Extract the base IRI from an RDF file if available."""
    g = Graph()
    g.parse(str(rdf_path))
    for s in set(g.subjects()):
        if isinstance(s, URIRef):
            uri = str(s)
            if "#" in uri:
                return uri.split("#")[0] + "#"
            return uri.rsplit("/", 1)[0] + "/"
    return "https://linkedin.com/pulse/"


def get_entity_count(rdf_path: str | Path) -> int:
    """Return the number of triples in the RDF file."""
    g = Graph()
    g.parse(str(rdf_path))
    return len(g)


def validate_orphans(kgdata: dict) -> list[str]:
    """Return list of orphan node IDs (nodes with no incident links)."""
    incident: set[str] = set()
    for link in kgdata["links"]:
        src = link["source"] if isinstance(link["source"], str) else link["source"]["id"]
        tgt = link["target"] if isinstance(link["target"], str) else link["target"]["id"]
        incident.add(src)
        incident.add(tgt)
    orphans = [n["id"] for n in kgdata["nodes"] if n["id"] not in incident]
    return orphans
