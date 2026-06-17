# RDF 1.2 Primer — Knowledge Graph Relationships

**Document:** [rdf12-primer-minimax_m2.5free.ttl](rdf12-primer-minimax_m2.5free.ttl) (Turtle RDF)
**HTML Companion:** [rdf12-primer-minimax_m2.5free-infographic.html](rdf12-primer-minimax_m2.5free-infographic.html)
**Source:** [W3C RDF 1.2 Primer](https://www.w3.org/TR/rdf12-primer/)

---

## Overview

This document provides a comprehensive view of the relationships within the RDF 1.2 Primer Knowledge Graph. All entities are linked using the URIBurner resolver: `https://linkeddata.uriburner.com/describe/?uri={URL-encoded-IRI}`

---

## Core Entities

| Entity | Type | Description |
|--------|------|-------------|
| [RDF 1.2 Primer](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F) | schema:TechArticle | W3C Group Note providing basic RDF knowledge |
| [Pierre-Antoine Champin](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23champin) | schema:Person | Editor of the RDF 1.2 Primer |
| [Niklas Lindström](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23lindstrom) | schema:Person | Editor of the RDF 1.2 Primer |
| [W3C](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2F) | schema:Organization | Publisher |
| [kg-generator skill](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23kg-generator-skill) | schema:SoftwareApplication | Tool that generated this KG |

---

## Relationships

### Document → Sections

- **RDF 1.2 Primer** [schema:hasPart](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FhasPart) → [Introduction Section](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23section-Introduction)
- **RDF 1.2 Primer** [schema:hasPart](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FhasPart) → [Data Model Section](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23section-data-model)
- **RDF 1.2 Primer** [schema:hasPart](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FhasPart) → [Vocabularies Section](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23section-vocabulary)
- **RDF 1.2 Primer** [schema:hasPart](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FhasPart) → [Graph Syntax Section](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23section-graph-syntax)
- **RDF 1.2 Primer** [schema:hasPart](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FhasPart) → [FAQ Section](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23faqSection)
- **RDF 1.2 Primer** [schema:hasPart](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FhasPart) → [Glossary Section](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23glossarySection)
- **RDF 1.2 Primer** [schema:hasPart](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FhasPart) → [HowTo Section](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23howtoSection)

### Document → Authors & Publishers

- **RDF 1.2 Primer** [schema:author](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2Fauthor) → [Pierre-Antoine Champin](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23champin)
- **RDF 1.2 Primer** [schema:author](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2Fauthor) → [Niklas Lindström](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23lindstrom)
- **RDF 1.2 Primer** [schema:publisher](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2Fpublisher) → [W3C](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2F)
- **RDF 1.2 Primer** [prov:wasGeneratedBy](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fwww.w3.org%2Fns%2Fprov%23wasGeneratedBy) → [kg-generator skill](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23kg-generator-skill)

### Document → External References (owl:sameAs)

- **RDF 1.2 Primer** [schema:about](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2Fabout) → [DBpedia: Resource Description Framework](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fdbpedia.org%2Fresource%2FResource_Description_Framework)
- **RDF 1.2 Primer** [owl:sameAs](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23sameAs) → [DBpedia: RDF](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fdbpedia.org%2Fresource%2FResource_Description_Framework)
- **RDF 1.2 Primer** [owl:sameAs](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23sameAs) → [Wikidata: Q8762](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fwww.wikidata.org%2Fentity%2FQ8762)

### FAQ Relationships

- **FAQ Section** [rdf:type](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23type) → [schema:FAQPage](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FFAQPage)
- **FAQ Section** [schema:mainEntity](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FmainEntity) → [Q1: What is RDF?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q1)
- **FAQ Section** [schema:mainEntity](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FmainEntity) → [Q2: What is an RDF triple?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q2)
- **FAQ Section** [schema:mainEntity](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FmainEntity) → [Q3: What is an IRI?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q3)
- **FAQ Section** [schema:mainEntity](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FmainEntity) → [Q4: What is a literal in RDF?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q4)
- **FAQ Section** [schema:mainEntity](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FmainEntity) → [Q5: What is a blank node in RDF?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q5)
- **FAQ Section** [schema:mainEntity](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FmainEntity) → [Q6: What is an RDF graph?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q6)
- **FAQ Section** [schema:mainEntity](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FmainEntity) → [Q7: What is RDF Schema?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q7)
- **FAQ Section** [schema:mainEntity](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FmainEntity) → [Q8: What is Turtle syntax?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q8)
- **FAQ Section** [schema:mainEntity](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FmainEntity) → [Q9: What is JSON-LD?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q9)
- **FAQ Section** [schema:mainEntity](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FmainEntity) → [Q10: What is Linked Data?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q10)
- **FAQ Section** [schema:mainEntity](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FmainEntity) → [Q11: What are triple terms in RDF 1.2?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q11)
- **FAQ Section** [schema:mainEntity](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FmainEntity) → [Q12: What is an RDF dataset?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q12)

### Question → Answer Relationships

- [Q1: What is RDF?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q1) [schema:acceptedAnswer](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FacceptedAnswer) → [A1](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23a1)
- [Q2: What is an RDF triple?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q2) [schema:acceptedAnswer](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FacceptedAnswer) → [A2](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23a2)
- [Q3: What is an IRI?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q3) [schema:acceptedAnswer](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FacceptedAnswer) → [A3](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23a3)
- [Q4: What is a literal in RDF?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q4) [schema:acceptedAnswer](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FacceptedAnswer) → [A4](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23a4)
- [Q5: What is a blank node in RDF?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q5) [schema:acceptedAnswer](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FacceptedAnswer) → [A5](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23a5)
- [Q6: What is an RDF graph?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q6) [schema:acceptedAnswer](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FacceptedAnswer) → [A6](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23a6)
- [Q7: What is RDF Schema?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q7) [schema:acceptedAnswer](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FacceptedAnswer) → [A7](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23a7)
- [Q8: What is Turtle syntax?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q8) [schema:acceptedAnswer](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FacceptedAnswer) → [A8](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23a8)
- [Q9: What is JSON-LD?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q9) [schema:acceptedAnswer](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FacceptedAnswer) → [A9](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23a9)
- [Q10: What is Linked Data?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q10) [schema:acceptedAnswer](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FacceptedAnswer) → [A10](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23a10)
- [Q11: What are triple terms in RDF 1.2?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q11) [schema:acceptedAnswer](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FacceptedAnswer) → [A11](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23a11)
- [Q12: What is an RDF dataset?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q12) [schema:acceptedAnswer](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FacceptedAnswer) → [A12](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23a12)

### Glossary Relationships

- **Glossary Section** [rdf:type](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23type) → [schema:DefinedTermSet](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FDefinedTermSet)
- **Glossary Section** [schema:hasDefinedTerm](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FhasDefinedTerm) → [RDF](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23term-rdf)
- **Glossary Section** [schema:hasDefinedTerm](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FhasDefinedTerm) → [RDF Triple](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23term-triple)
- **Glossary Section** [schema:hasDefinedTerm](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FhasDefinedTerm) → [IRI](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23term-iri)
- **Glossary Section** [schema:hasDefinedTerm](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FhasDefinedTerm) → [Literal](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23term-literal)
- **Glossary Section** [schema:hasDefinedTerm](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FhasDefinedTerm) → [Blank Node](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23term-blank-node)
- **Glossary Section** [schema:hasDefinedTerm](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FhasDefinedTerm) → [RDF Graph](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23term-graph)
- **Glossary Section** [schema:hasDefinedTerm](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FhasDefinedTerm) → [RDF Vocabulary](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23term-vocabulary)
- **Glossary Section** [schema:hasDefinedTerm](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FhasDefinedTerm) → [RDF Schema](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23term-rdfs)
- **Glossary Section** [schema:hasDefinedTerm](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FhasDefinedTerm) → [RDF Dataset](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23term-dataset)
- **Glossary Section** [schema:hasDefinedTerm](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FhasDefinedTerm) → [Turtle](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23term-turtle)

### HowTo Relationships

- **HowTo Section** [rdf:type](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23type) → [schema:HowTo](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2FHowTo)
- **HowTo Section** [schema:step](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2Fstep) → [Step 1: Identify the Subject](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23step1)
- **HowTo Section** [schema:step](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2Fstep) → [Step 2: Choose the Predicate](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23step2)
- **HowTo Section** [schema:step](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2Fstep) → [Step 3: Determine the Object](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23step3)
- **HowTo Section** [schema:step](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2Fstep) → [Step 4: Format as a Triple](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23step4)
- **HowTo Section** [schema:step](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2Fstep) → [Step 5: Serialize or Store](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23step5)

### FAQ → DBpedia Cross-References

- [Q1: What is RDF?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q1) [schema:about](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2Fabout) → [DBpedia: Resource Description Framework](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fdbpedia.org%2Fresource%2FResource_Description_Framework)
- [Q10: What is Linked Data?](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23q10) [schema:about](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2Fabout) → [DBpedia: Linked_Data](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fdbpedia.org%2Fresource%2FLinked_Data)

### Glossary → DBpedia Cross-References

- [RDF](https://linkeddata.uriburner.com/describe/?uri=https%3A%2F%2Fwww.w3.org%2FTR%2Frdf12-primer%2F%23term-rdf) [schema:about](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fschema.org%2Fabout) → [DBpedia: Resource_Description_Framework](https://linkeddata.uriburner.com/describe/?uri=http%3A%2F%2Fdbpedia.org%2Fresource%2FResource_Description_Framework)

---

## Related Resources

- [Turtle Knowledge Graph](rdf12-primer-minimax_m2.5free.ttl)
- [HTML Infographic](rdf12-primer-infographic.html)
- [W3C RDF 1.2 Primer (Original)](https://www.w3.org/TR/rdf12-primer/)
- [URIBurner SPARQL Endpoint](https://linkeddata.uriburner.com/sparql)

---

*Generated by: kg-generator skill | Rendered by: rdf-infographic-skill | Model: minimax_m2.5free*