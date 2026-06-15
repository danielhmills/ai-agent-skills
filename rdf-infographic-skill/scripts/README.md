# RDF Infographic Generator

Generate self-contained HTML infographics with a D3.js Knowledge Graph Explorer from RDF documents.

## Quick Start

```bash
python3 generate_infographic.py \
  --ttl input.ttl \
  --output output.html \
  --title "My Article Title" \
  --source-url "https://example.com/article"
```

## Requirements

- Python 3.10+
- rdflib
- Jinja2 (optional; falls back to `string.Template`)

Install: `pip install rdflib Jinja2`

## CLI Reference

| Flag | Required | Description |
|------|----------|-------------|
| `--ttl` | Yes | Input RDF file (Turtle, JSON-LD, NTriples) |
| `--output` / `-o` | Yes | Output HTML file path |
| `--title` | No | Page title (default: derived from RDF) |
| `--description` | No | Meta description |
| `--tagline` | No | Hero section tagline |
| `--hero-tagline` | No | Hero metadata line (author, source) |
| `--meta-html` | No | Custom hero meta HTML |
| `--source-url` | No | Source URL for attribution |
| `--source-label` | No | Display label for source URL |
| `--resolver-pattern` | No | Resolver URL pattern (default: URIBurner) |

## Architecture

```
generate_infographic.py  →  rdf_parser.py   (kgData + narrative extraction)
                          →  html_assembler.py (template injection + validation)
                          →  templates/
                               ├── base_template.html  (Jinja2 shell)
                               ├── kg_explorer.js       (canonical D3.js module)
                               └── styles.css           (canonical design system)
```

## What It Extracts

- **Nodes + Links**: All URIRefs from triples → force-directed graph
- **FAQ**: `schema:FAQPage` / `schema:Question` annotations → accordion
- **Glossary**: `schema:DefinedTermSet` / `schema:DefinedTerm` → grid
- **HowTo**: `schema:HowTo` + `schema:HowToStep` → numbered list
- **People**: `schema:Person` → cards
- **Organizations**: `schema:Organization` → cards
- **SPARQL**: Auto-generated query recipes

## Validation

On every run, the generator runs `validate-harness-contract.py` against the output.
The gate blocks delivery if any harness contract check fails.
