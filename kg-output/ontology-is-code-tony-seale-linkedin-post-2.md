# Ontology as Source Code — Edition 2

**Author:** [Tony Seale](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23tonySeale) — Knowledge Graph Engineer
**Source:** https://www.linkedin.com/posts/tonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54
**Published:** May 21, 2026
**Engagement:** 400 reactions, 45 comments, 14 contributors
**RDF Resolver:** [Turtle](ontology-is-code-tony-seale-linkedin-post-2.ttl)
**Source HTML:** [ontology-is-code-tony-seale-linkedin-post-2.html](ontology-is-code-tony-seale-linkedin-post-2.html)

---

## Overview

[Tony Seale](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23tonySeale) asks: "Did you start building your ontology as a set of rows in a custom database table?" He argues this instinct is understandable but misguided. [Ontologies are logic and formal axioms](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23ontologyAsCode), not tables. They should be treated as source code — compiled, version-controlled, and governed with engineering discipline. Closing line: **"Your ontology is source code for your meaning."**

This Edition 2 knowledge graph captures the full 45-comment discussion with 14 distinct contributor threads, featuring [Kingsley Uyi Idehen](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23kingsleyIdehen)'s anchor insight on how LLMs and the Semantic Web stack form a natural ecosystem for ontology management.

---

## The Three Pillars

### [Compile — Not Just Parse](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23pillarCompile)
A build should break on contradictions or unexpected entailments. An absent entailment is a test failure, not a curiosity discovered six months later in production. Jacob Friedman notes OWL is based on Description Logic — leverage its formal semantics for normalization checks.

### [Live in Plain Text](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23pillarPlainText)
Ontologies should live in plain text — enabling diffs, branches, blame, and pull requests. You want LLMs to read, navigate, and edit the source directly, exactly the way it works with a codebase.

### [Governed Like Code](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23pillarGovernance)
Standard engineering discipline — version control, code review, and CI/CD pipelines applied to meaning itself.

---

## Featured Insight: LLMs + Semantic Web — A Natural Ecosystem

**[Kingsley Uyi Idehen](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23kingsleyIdehen):** Agreed. Ontology management is a classic files-and-filesystem interaction pattern. RDF-Turtle is very much human-readable shorthand but lacked tooling support. Today the Semantic Web stack gels naturally with LLMs and AI Agents. Ask an AI Agent to express worldviews in whatever notation you prefer, save to a file, and copy to a folder bound to a backend RDF DBMS. LLM-powered Agents with Skills make this process a zillion times easier. I will use this post to demonstrate how I've used this approach to create the demo showcases at [linkeddata.uriburner.com/DAV/demos/daas/](https://linkeddata.uriburner.com/DAV/demos/daas/).

---

## Comments (14 Contributors)

**[Kingsley Uyi Idehen](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23kingsleyIdehen)** — Founder & CEO, OpenLink Software (Featured):
Agreed. Ontology management is a classic files-and-filesystem interaction pattern. RDF-Turtle is very much human-readable shorthand but lacked tooling support. Today the Semantic Web stack gels naturally with LLMs and AI Agents. Ask an AI Agent to express worldviews in whatever notation you prefer, save to a file, and copy to a folder bound to a backend RDF DBMS. LLM-powered Agents with Skills make this process a zillion times easier. I will use this post to demonstrate how I've used this approach to create the demo showcases at [linkeddata.uriburner.com/DAV/demos/daas/](https://linkeddata.uriburner.com/DAV/demos/daas/).

**[Veronika Heimsbakk](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23veronikaHeimsbakk)** — Knowledge Graph Specialist (14 reactions):
Hear, hear! Getting ontology from tables into code is easy with four lines of Python.

**Jacob Friedman** — Semantic Reasoning Specialist:
References conceptual graphs, Harold Boley, and RuleML. Notes OWL is based on Description Logic and asks: "Can anyone point us to a standards body with a certifiable normalization of Description Logic for OWL?" Links to W3C OWL2 Direct Semantics.

**Robert Sanderson** — Linked Art Contributor:
Linked Art's compile pipeline processes RDFS+OWL into a Python class library. Engineers write familiar code like `r = Person(id="Rob"); r.name = "Rob"` instead of raw triple adds. Ontology is code — and transpiles to other code that makes it more developer friendly.

**Gabor Csepregi** — Knowledge Graph Practitioner:
Can't remember the last time I had ontology and knowledge graph related content properly explained.

**Harish Iyer** — Product-Strategy Thinker:
The gap between engineering, design and product is narrowing. Ontology should no longer be a layer but the language of the company. Context switching will be replaced by context expansion. Who owns the ontology guardian role?

**Joseph Macdonald** — TODAG Advocate:
WhenTTT, not only IFTTT. Temporal Objective-Directed Acyclic Graphs (TODAG) as a hypergraph approach for treating ontologies as revenue-generating assets.

**Mark O'Donovan** — Data Practitioner:
Started as an idea in my head, then a note in a notebook, then an Excel table, then a SQL table — now looking at GraphDB. A personal journey toward ontology maturity.

**Kyle Tobin** — Pydantic Ontology Advocate:
Do your ontology in Pydantic so entities are executable — they don't just describe their own behavior. They conduct it too! Ontology should be reflected in application architecture, not smeared across four duplicative components.

**[Honorio J. Padrón III](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23honorioPadron)** — Creator, CLEARED Platform:
Operational ontologies describe what exists. Decision ontologies describe what the enterprise does — who owns each decision, what triggers it, what action it generates. An operational ontology makes data legible. A decision ontology makes the enterprise executable. The decision ontology is source code for your will to act.

**Stepan Karandin** — Information Theorist:
Ontology is information. Databases or code are just data formats. The relational model is the worst kind of normalization for ontology. Mathematically, ontology could be described as a graph.

**Edward Henry** — AI Practitioner:
The biggest illusion in AI is the gap. We are trying to address upstream problems downstream, trying to turn LLM slop into something real with great ideas like ontology-as-code.

**Olivier Rey**:
I would rather say: an ontology is a hypergraph. Code is not a graph but a tree.

**Thomas Smith** — Database Theorist:
Relational databases only index binary trees — two dimensions only. The correct approach uses triples to define three dimensions of a graph. SQL gets choked up with circular references.

---

## Adopting Ontology as Code

1. **[Extract from Tables](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23step1)** — Four lines of Python (maplib + OTTR templates).
2. **[Store in Plain Text](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23step2)** — Turtle for readability, JSON-LD for tooling.
3. **[Set Up Compilation](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23step3)** — Build step for logical consistency with Description Logic normalization.
4. **[Version Control](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23step4)** — Git for diffs, branches, PRs.
5. **[LLM Editing](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23step5)** — AI Agents read, navigate, edit source files.
6. **[Bind to RDF DBMS](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23step6)** — Folder transparently bound to quad store.
7. **[Define Decision Ownership](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23step7)** — Who owns each decision, what triggers it, what action. Consider Pydantic executability, transpilation, and TODAG temporal patterns.

---

## FAQ

### 1. Why should ontologies be treated as source code?
Because ontologies express formal logic and axioms — not database rows. They should compile, live in plain text for version control, and be governed with engineering discipline. Tony Seale: "Your ontology is source code for your meaning."

### 2. What does "compile, not just parse" mean?
A build should break on contradictions or unexpected entailments. An absent entailment is a test failure, not a curiosity discovered six months later in production. This catches logical errors at build time rather than in production.

### 3. Why plain text for ontologies?
Plain text enables diffs, branches, blame, and pull requests — standard software engineering tooling. It also allows LLMs to read, navigate, and edit the source directly, exactly like working with a codebase.

### 4. How do LLMs change ontology management?
Kingsley Idehen (anchor commentary): The Semantic Web stack gels naturally with LLMs and AI Agents. Users can ask an AI Agent to express worldviews in any notation, save to a file, and copy to a folder bound to a backend RDF DBMS. LLM-powered Agents with Skills make this "a zillion times easier." The demo showcases at [linkeddata.uriburner.com/DAV/demos/daas/](https://linkeddata.uriburner.com/DAV/demos/daas/) are live examples of this filesystem-to-quad-store pipeline.

### 5. What is a decision ontology?
Honorio J. Padrón III distinguishes operational ontologies (what exists) from decision ontologies (who owns each decision, what triggers it, what action it generates). An operational ontology makes data legible; a decision ontology makes the enterprise executable. The decision ontology is "source code for your will to act." His CLEARED platform operationalizes this distinction.

### 6. What is McOntology?
A term coined by Tony Seale for commoditized, fast-food approaches to ontology — treating ontologies as mass-produced rather than carefully engineered artifacts. It is the antithesis of the ontology-as-code philosophy.

### 7. How does the Semantic Web stack relate to ontology-as-code?
RDF-Turtle is human-readable shorthand for triples. JSON-LD has more tooling support. Combined with LLMs, the stack now provides both readability and tooling — bridging the historical gap. Files in a DAV folder bound to Virtuoso automatically become part of a live quad store.

### 8. What's wrong with putting ontologies in database tables?
Tony Seale: You wouldn't write application code in a database table. Thomas Smith adds: relational databases index binary trees — two dimensions only. Ontologies need triples for three dimensions. Stepan Karandin: the relational model is the worst kind of normalization for ontology.

### 9. How do you bridge tables to ontology code?
Veronika Heimsbakk: Getting ontology from tables into code is straightforward — four lines of Python using tools like maplib and OTTR templates to map structured data to ontology properties.

### 10. Can ontologies be executable?
Kyle Tobin argues for Pydantic-defined ontologies where entities are executable — "they don't just describe their own behavior. They conduct it too!" Robert Sanderson demonstrates with Linked Art's transpilation from RDFS+OWL into Python class libraries. Both embed ontology into application architecture.

### 11. Who owns the ontology in an organization?
Harish Iyer frames this as one of the most consequential product decisions a company will make. The ontology guardian role sits at the intersection of engineering, design, and product — a decision owner who maintains the language of the company.

### 12. What is the upstream/downstream gap in AI?
Edward Henry warns the biggest illusion is trying to address upstream problems downstream — turning LLM slop into something real. Ontology-as-code addresses this by formalizing meaning at the source. Joseph Macdonald extends this with TODAG temporal patterns for revenue-generating ontologies.

---

## Glossary

- **[Ontology as Code](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23termOntologyAsCode)**: Treating ontologies as source code with compilation, version control, and engineering governance.
- **[Compile](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23termCompile)**: Build step checking logical consistency — contradictions should break the build.
- **[Plain Text](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23termPlainText)**: Storage format enabling diffs, branches, and LLM navigation.
- **[Governance](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23termGovernance)**: Engineering discipline — version control, code review, CI/CD for meaning.
- **[RDF-Turtle](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23termRDFTurtle)**: Human-readable RDF notation — preferred for LLM-mediated ontology creation.
- **[LLM](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23termLLM)**: Large Language Model — AI systems that read, navigate, and edit ontology source files.
- **[Decision Ontology](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23termDecisionOntology)**: Ontology describing who owns each decision, what triggers it, what action it generates.
- **[Semantic Web Stack](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23termSemanticWeb)**: W3C stack — RDF, SPARQL, OWL, JSON-LD — now gelling with LLMs.
- **[Knowledge Graph](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23termKnowledgeGraph)**: Graph-structured data model — the runtime instantiation of ontologies.
- **[McOntology](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23termMcOntology)**: Commoditized, fast-food ontology — mass-produced rather than engineered.
- **[Pydantic-Executable Ontology](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23termPydanticOntology)**: Kyle Tobin's approach — entities that conduct their own behavior.
- **[TODAG](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Ftonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54%23termTODAG)**: Temporal Objective-Directed Acyclic Graph — WhenTTT patterns for revenue-generating ontologies.

---

## Industry Context

NAICS 541511 — Custom Computer Programming Services. Knowledge Engineering vertical with ~$80B labor TAM and high automation readiness via LLM + Semantic Web integration.

---

## Knowledge Graph Statistics

| Metric | Count |
|--------|-------|
| Contributors | 14 |
| RDF Triples | 450+ |
| FAQ Entries | 12 |
| Glossary Terms | 12 |
| Adoption Steps | 7 |
| Ontology Pillars | 3 |
| Defined Terms | 7 |
| Ontology Classes | 3 |
| Custom Properties | 3 |

---

## Related Resources

- [Source post on LinkedIn](https://www.linkedin.com/posts/tonyseale_did-you-start-building-your-ontology-as-a-share-7463353332565356545-jY54)
- [RDF Turtle KG](ontology-is-code-tony-seale-linkedin-post-2.ttl) (450+ triples)
- [HTML Infographic](ontology-is-code-tony-seale-linkedin-post-2.html)
- [The Knowledge Graph Guys](https://lnkd.in/eMQwyBpj)
- [URIBurner Demo Showcases](https://linkeddata.uriburner.com/DAV/demos/daas/)
- [Veronika Heimsbakk's Python Extraction Post](https://substack.com/@veronahe/p-183770493)

---

*Generated 2026-05-22 using [kg-generator](https://github.com/OpenLinkSoftware/ai-agent-skills/tree/main/kg-generator) and [rdf-infographic-skill](https://github.com/OpenLinkSoftware/ai-agent-skills/tree/main/rdf-infographic-skill) via Claude Opus 4.7 on Claude Code. Entity links via [URIBurner](https://linkeddata.uriburner.com/). Edition 2 — Enhanced with 14 comment threads and Kingsley Idehen's featured insight.*
