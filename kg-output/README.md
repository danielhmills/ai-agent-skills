# AI Incident Database - February-April 2026 Roundup Knowledge Graph

## Overview

This directory contains the RDF knowledge graph generated from the AI Incident Database blog post covering incidents from February, March, and April 2026.

**Source URL:** https://incidentdatabase.ai/blog/incident-report-2026-february-march-april/

**Generated:** 2026-05-07

## Files

| File | Description |
|------|-------------|
| `incident-report-2026-feb-apr-1.ttl` | Turtle RDF knowledge graph |
| `incident-report-2026-feb-apr.html` | HTML with embedded JSON-LD metadata |
| `README.md` | This documentation |

## Knowledge Graph Contents

The JSON-LD contains 100 entities including:

### Main Article
- Title: "AI Incident Roundup – February, March, and April 2026"
- Author: Daniel Atherton
- Publisher: AI Incident Database (AIID)
- Date: 2026-05-05
- 109 new incident IDs (1362-1470)

### Harm Categories (14 sections)
1. Synthetic Media Scams and Consumer Fraud (22 IDs)
2. Political/Geopolitical Misinformation (16 IDs)
3. Privacy, Identity, Voice/Likeness Misuse (12 IDs)
4. Synthetic Sexual Abuse (11 IDs)
5. Legal/Policy/Journalism Credibility Failures (10 IDs)
6. Chatbots and AI Companions (9 IDs)
7. Public-Sector/Policing Failures (7 IDs)
8. Physical-World Autonomy/Robotics (7 IDs)
9. Agentic/Operational Software Failures (7 IDs)
10. Cybersecurity/Adversarial AI (5 IDs)
11. Gambling/Profiling Exploitation (3 IDs)

### Structured Data
- **FAQ Page**: 12 questions and answers
- **Defined Term Set**: 12 glossary terms (deepfake, synthetic media, AI incident, etc.)
- **HowTo**: 6 steps for navigating the AI Incident Database
- **Ontology**: Custom ontology for AI incident reporting

### Key Entities
- **Products**: ChatGPT, Claude Code, Cursor AI, Google Gemini, Meta AI, Baidu Apollo Go
- **Organizations**: OpenAI, Anthropic, Google, Meta, Amazon
- **Publications**: The Guardian, Ars Technica

## Compliance

The knowledge graph passes all 12 compliance checks:
- ✅ schema: namespace uses http://schema.org/
- ✅ FAQ wrapped in schema:FAQPage
- ✅ Glossary terms wrapped in schema:DefinedTermSet
- ✅ Main article has schema:hasPart linking to all sections
- ✅ DBpedia/Wikipedia IRIs fully expanded
- ✅ No file: scheme IRIs
- ✅ owl:sameAs used for DBpedia cross-references
- ✅ @base set to source URL
- ✅ Ontology has proper metadata
- ✅ No blank nodes for schema:Answer
- ✅ Inverse relationships explicit
- ✅ prov:wasGeneratedBy links to skill

## Skills Used

- **kg-generator**: Generated RDF from source URL
- **rdf-infographic-skill**: (Optional) Generate HTML visualization

## Usage

### View the Knowledge Graph
Open `incident-report-2026-feb-apr-1.jsonld` in any RDF viewer or editor.

### Upload to SPARQL Endpoint
```bash
# Upload to Virtuoso
curl -X POST -H "Content-Type: application/ld+json" \
  --data-binary @incident-report-2026-feb-apr-1.jsonld \
  http://localhost:8890/sparql-graph-crud?graph=urn:aiid:incidents:2026-q1
```

### Generate HTML Infographic
Use the rdf-infographic-skill to generate an interactive HTML visualization:
```bash
python3 rdf-parser.py incident-report-2026-feb-apr-1.jsonld --format json-ld
```

## Schema.org Types Used

- TechArticle (main article)
- FAQPage
- DefinedTermSet
- HowTo
- Person (author)
- Organization (publisher)
- SoftwareApplication (AI systems)
- Product (robots, vehicles)
- Question/Answer pairs
- ArticleSection (harm categories)
- rdf:Ontology (custom ontology)

## Related Links

- AI Incident Database: https://incidentdatabase.ai/
- Source Article: https://incidentdatabase.ai/blog/incident-report-2026-february-march-april/
- kg-generator skill: https://github.com/OpenLinkSoftware/ai-agent-skills/tree/main/kg-generator