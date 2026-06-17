# The Semantic Medallion: Building a Knowledge Graph-Powered Data Catalog

**Author:** [Veronika Heimsbakk](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23veronikaHeimsbakk) — Knowledge Graph Specialist, author of [SHACL for the Practitioner](https://shacl.veronahe.no/)
**Published:** May 14, 2026 on [Modern Data 101](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23modernData101)
**Source:** https://moderndata101.substack.com/p/the-semantic-medallion
**RDF Resolver:** https://moderndata101.substack.com/p/the-semantic-medallion

Associated RDF: [semantic-medallion-deepseek_v4pro-1.ttl](semantic-medallion-deepseek_v4pro-1.ttl)
Source HTML: [semantic-medallion-deepseek_v4pro-1.html](semantic-medallion-deepseek_v4pro-1.html)

---

## Overview

How you can transform raw data sources into a unified knowledge graph in four lines of Python. The [Semantic Medallion](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23semanticMedallion) extends the standard [Bronze/Silver/Gold medallion data architecture](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23medallionArchitecture) by transforming the Gold layer into a connected knowledge graph rather than isolated clean tables. The result is a [data catalog that answers relational questions](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dataCatalog) — "Show me everything about this record", "Which sources contribute to our customer records?", "Find customers with billing issues who have active contracts" — rather than serving static table lists.

---

## Core Concepts

### [Semantic Medallion](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23semanticMedallion)
An extension of the medallion data architecture where the Gold layer is transformed into a connected knowledge graph rather than isolated clean tables. Relationships are embedded in the data itself, not in external join logic.

### [IRI Minting](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23iriMinting)
Creating stable, globally unique identifiers (Internationalized Resource Identifiers) for every entity in the Silver layer — replacing database auto-increment IDs and GUIDs with identifiers that work across all systems.

### [Entity Resolution](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23entityResolution)
Using `owl:sameAs` to link entities appearing in CRM, billing, and external registries — providing a unified view of every record across all systems.

### [Data Provenance](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23provenance)
Tracking the origin and lineage of data using [PROV-O](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23provOntology), expressed as queryable RDF triples rather than stored in a separate lineage tool with its own database.

### [Semantic Data Catalog](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dataCatalog)
A knowledge graph-powered catalog describing what things mean and how they relate — metadata and data unified in the same graph, with the catalog as part of the knowledge graph rather than a separate system pointing at data.

### [DataFrame-to-RDF Transformation](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23rdfTransformation)
The process of mapping structured DataFrames to RDF triples using [OTTR templates](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23ottrTemplates) and the [maplib](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23maplib) Python library — complete Silver-to-Gold transformation in four lines of Python.

---

## Architecture Layers

The medallion layers are reframed as semantic enrichment stages: Bronze (no semantics), Silver (local semantics via identifiers), Gold (global semantics via shared vocabulary).

### [Bronze Layer — Raw Ingestion](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23bronzeLayer)

Standard raw data ingestion via orchestration tools. Data is ingested in its original format with **no semantic transformation**. Linked to raw source datasets via [DCAT](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dcatVocabulary). This is where everything starts — raw, unprocessed, but fully captured.

### [Silver Layer — IRI Minting](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23silverLayer)

In addition to cleaning and typing, this layer focuses on **minting stable IRIs** for every entity — creating join keys that work across all systems. This is the biggest implementation challenge: establishing identifiers that remain consistent as new data sources are added.

### [Gold Layer — Semantic RDF](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23goldLayer)

Silver DataFrames are mapped to a shared ontology using a common vocabulary and published as RDF via four lines of Python. The relationships are **in the data**, not in join logic. A [DCAT Catalog](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dcatCatalog) describes the unified knowledge graph with a [SPARQL endpoint](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23sparqlEndpointService) distribution.

---

## Technologies

| Technology | Description |
|------------|-------------|
| [maplib](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23maplib) | Python library for DataFrame-to-RDF transformation |
| [OTTR Templates](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23ottrTemplates) | Declarative stOTTR syntax mapping columns to ontology properties |
| [DCAT](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dcatVocabulary) | W3C Data Catalog Vocabulary — used by data.gov, European Data Portal |
| [PROV-O](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23provOntology) | W3C Provenance Ontology — data lineage as queryable triples |
| [SPARQL](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23sparqlQueryLanguage) | W3C query language for RDF knowledge graphs |
| [RDF](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23rdfStandard) | W3C Resource Description Framework — subject-predicate-object triples |

---

## Industry Context

- [Data Management Industry](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dataManagementVertical): NAICS 518210 — Data Processing, Hosting, and Related Services (~$200B TAM)
- [Knowledge Graph Consulting](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23knowledgeGraphConsultingVertical): NAICS 541511 — Custom Computer Programming Services (~$80B TAM)

---

## Building a Semantic Medallion Data Catalog

### [Step 1: Ingest Raw Data into Bronze](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23step1)
Set up orchestration tools to ingest raw data from all source systems into the Bronze layer. Preserve original formats without transformation. Link datasets to sources via DCAT.

### [Step 2: Clean Data and Mint IRIs in Silver](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23step2)
Clean and type the data in the Silver layer. Critically, replace database auto-increment IDs with stable, globally unique IRIs for every entity. Define a consistent IRI naming scheme using your organization's domain namespace.

### [Step 3: Design the Shared Ontology](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23step3)
Design a shared ontology that maps your business concepts to RDF classes and properties. Start with what is available from existing data models. Use standard vocabularies (DCAT, PROV-O, schema.org) where possible. Iterate and refine as understanding deepens.

### [Step 4: Define OTTR Templates](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23step4)
Create OTTR templates in stOTTR syntax that map your DataFrame columns to ontology properties. Each template defines how a row in your DataFrame becomes a set of RDF triples.

### [Step 5: Transform to RDF with maplib](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23step5)
Use the maplib Python library to apply your OTTR templates to the Silver DataFrames. This transformation produces RDF triples in as few as four lines of Python.

### [Step 6: Publish to Gold as a Knowledge Graph](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23step6)
Write the resulting RDF to the Gold layer — either as Turtle files on a data lake, or directly to a triplestore with a SPARQL endpoint. Register the knowledge graph in a DCAT Catalog with a SPARQL endpoint distribution.

### [Step 7: Query and Validate](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23step7)
Use SPARQL to validate the knowledge graph: run customer 360 queries to verify entity resolution, lineage queries to trace provenance, and cross-system queries to confirm relationships are correctly modeled.

---

## SPARQL Query Examples

The article describes three SPARQL queries. These reconstructed versions run against the companion [ontology and instance data](semantic-medallion-ontology-instance-data.ttl).

### Query 1: Customer 360

Retrieve every fact about customer `C-001` from every data source, unified under one identifier.

[▶ Run live query](https://linkeddata.uriburner.com/sparql?default-graph-uri=&query=PREFIX+%3A+%3Chttp%3A%2F%2Fexample.org%2Fontology%23%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+prov%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fprov%23%3E%0APREFIX+dcat%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fdcat%2F%3E%0ADESCRIBE+%3AC-001&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

```sparql
PREFIX : <http://example.org/ontology#>
PREFIX schema: <http://schema.org/>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX dcat: <http://www.w3.org/ns/dcat/>

DESCRIBE :C-001
```

### Query 2: Data Lineage

Trace which sources contribute to customer records — identifying the provenance path from Gold entities back through Silver to Bronze datasets.

[▶ Run live query](https://linkeddata.uriburner.com/sparql?default-graph-uri=&query=PREFIX+%3A+%3Chttp%3A%2F%2Fexample.org%2Fontology%23%3E%0APREFIX+prov%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fprov%23%3E%0APREFIX+dcat%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fdcat%2F%3E%0ASELECT+%3Fsource+%3Fdataset+%3Fdistribution%0AWHERE+%7B%0A++%3AC-001+prov%3AwasDerivedFrom+%3Fsource+.%0A++%3Fsource+prov%3AhadPrimarySource+%3Fdataset+.%0A++%3Fdataset+dcat%3Adistribution+%3Fdistribution+.%0A%7D&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

```sparql
PREFIX : <http://example.org/ontology#>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX dcat: <http://www.w3.org/ns/dcat/>

SELECT ?source ?dataset ?distribution
WHERE {
  :C-001 prov:wasDerivedFrom ?source .
  ?source prov:hadPrimarySource ?dataset .
  ?dataset dcat:distribution ?distribution .
}
```

### Query 3: Cross-System Relationship

Find customers with billing issues who have active contracts — navigating relationships directly across systems without manual joins or table hunting.

[▶ Run live query](https://linkeddata.uriburner.com/sparql?default-graph-uri=&query=PREFIX+%3A+%3Chttp%3A%2F%2Fexample.org%2Fontology%23%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Fcustomer+%3Fname+%3FbillingIssue+%3Fcontract%0AWHERE+%7B%0A++%3Fcustomer+a+schema%3APerson+%3B%0A++++++++++++schema%3Aname+%3Fname+%3B%0A++++++++++++%3AhasBillingIssue+%3FbillingIssue+%3B%0A++++++++++++%3AhasActiveContract+%3Fcontract+.%0A++%3FbillingIssue+schema%3Astatus+%22Open%22+.%0A++%3Fcontract+schema%3Astatus+%22Active%22+.%0A%7D&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

```sparql
PREFIX : <http://example.org/ontology#>
PREFIX schema: <http://schema.org/>

SELECT ?customer ?name ?billingIssue ?contract
WHERE {
  ?customer a schema:Person ;
            schema:name ?name ;
            :hasBillingIssue ?billingIssue ;
            :hasActiveContract ?contract .
  ?billingIssue schema:status "Open" .
  ?contract schema:status "Active" .
}
```

### Query 4: Ontology Inspection

Inspect the Semantic Medallion ontology — list all defined classes with their labels and descriptions.

[▶ Run live query](https://linkeddata.uriburner.com/sparql?default-graph-uri=&query=PREFIX+%3A+%3Chttps%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fclass+%3Flabel+%3Fcomment%0AWHERE+%7B%0A++%3Fclass+a+rdfs%3AClass+%3B%0A++++++++++rdfs%3Alabel+%3Flabel+%3B%0A++++++++++rdfs%3Acomment+%3Fcomment+.%0A%7D&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

```sparql
PREFIX : <https://moderndata101.substack.com/p/the-semantic-medallion#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?class ?label ?comment
WHERE {
  ?class a rdfs:Class ;
         rdfs:label ?label ;
         rdfs:comment ?comment .
}
```

### Explore Knowledge Graph using SPARQL

Query the full KG by entity type:
- **RDF Turtle:** `GRAPH <https://linkeddata.uriburner.com/DAV/demos/daas/semantic-medallion-deepseek_v4pro-1.ttl>`
- **JSON-LD:** `GRAPH <https://linkeddata.uriburner.com/DAV/demos/daas/semantic-medallion-deepseek_v4pro-1.jsonld>`

---

## FAQ

### 1. [What is the Semantic Medallion?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q1)
The Semantic Medallion is an extension of the traditional Bronze/Silver/Gold data lakehouse architecture where the Gold layer is transformed into a connected knowledge graph rather than isolated clean tables. Relationships are embedded in the data itself, not in external join logic, enabling entity resolution, cross-system queries, and semantic search.

### 2. [How does the Bronze layer work?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q2)
The Bronze layer handles standard raw data ingestion via orchestration tools. Data is ingested in its original format with no semantic transformation. DCAT links these raw datasets to their source systems.

### 3. [What is the role of IRI minting in the Silver layer?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q3)
In the Silver layer, beyond cleaning and typing data, stable IRIs are minted for every entity. These globally unique identifiers replace database auto-increment IDs and GUIDs, creating join keys that work across all systems rather than being scoped to a single database.

### 4. [How does the Gold layer transform data into a knowledge graph?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q4)
The Gold layer maps Silver DataFrames to a shared ontology using OTTR templates and the maplib Python library, then publishes the result as RDF. Rather than creating separate Parquet/Delta tables requiring manual join logic, the data becomes a connected knowledge graph where relationships are stored as triples — subject-predicate-object statements — making the data inherently relational.

### 5. [Can the transformation be done in four lines of Python?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q5)
Yes. The article demonstrates the complete Silver-to-Gold transformation: (1) load the DataFrame, (2) define an OTTR template mapping columns to ontology properties, (3) apply the template using maplib, and (4) publish the resulting RDF to the Gold layer. The power comes from declarative templates rather than imperative code.

### 6. [Why use DCAT instead of a custom catalog schema?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q6)
DCAT (Data Catalog Vocabulary) is a W3C standard used by data.gov, the European Data Portal, and thousands of organizations. It provides: (1) interoperability with existing data catalog ecosystems, (2) rich standardized metadata for publishers, themes, formats, and lineage, (3) a unified graph where the catalog IS part of the knowledge graph, not a separate system, and (4) built-in integration with PROV-O for provenance.

### 7. [How does entity resolution work across data sources?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q7)
Entity resolution uses `owl:sameAs` assertions to link entities appearing in CRM, billing, and external registries. For example, a customer appearing in both the sales system and the billing system is linked via an `owl:sameAs` triple, creating a unified view. SPARQL queries can then navigate all facts about that customer regardless of which source system contributed them.

### 8. [How does PROV-O enable data lineage?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q8)
PROV-O (Provenance Ontology) expresses data lineage as RDF triples — recording which entities were derived from which sources, which activities generated them, and which agents were responsible. Instead of storing lineage in a separate tool with its own database, PROV-O provenance triples live IN the knowledge graph, making lineage queryable using the same SPARQL endpoint as the data itself.

### 9. [What is the biggest implementation challenge?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q9)
The biggest challenge is not the RDF conversion itself, but establishing stable identifiers (IRIs) in the Silver layer. This requires upfront design of IRI naming conventions and careful governance to ensure identifiers remain consistent as new data sources are added.

### 10. [How should you approach ontology design?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q10)
Start with the ontology that is available from your existing data models, then refine it incrementally as you understand cross-system relationships better. Do not aim for a perfect ontology upfront — the knowledge graph can evolve as your understanding deepens.

### 11. [Semantic Gold vs traditional Gold layer?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q11)
A traditional Gold layer consists of separate Parquet or Delta tables that require manual join logic in SQL or dbt scripts to connect related records. The Semantic Gold layer is RDF where relationships are embedded in the data as triples — eliminating table hunting, manual JOINs, and fragile transformation pipelines. The data becomes inherently connected rather than depending on external join logic.

### 12. [What is the bigger picture of this architecture?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q12)
The medallion layers are reframed as semantic enrichment stages: Bronze provides no semantics (raw data), Silver provides local semantics through stable identifiers (entities become referable across systems), and Gold provides global semantics through a shared vocabulary (entities are connected via typed relationships in a knowledge graph). This transforms the medallion from a storage pattern into a semantic enrichment pipeline.

---

## Glossary

- **[Semantic Medallion](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termSemanticMedallion):** An architecture pattern extending the Bronze/Silver/Gold medallion with knowledge graph semantics — transforming the Gold layer into connected RDF.
- **[IRI](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termIRI):** A globally unique, stable identifier for an entity — replacing database auto-increment IDs with identifiers that work across all systems.
- **[DCAT](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termDCAT):** A W3C standard vocabulary for describing data catalogs, datasets, distributions, and data services — used by data.gov and the European Data Portal.
- **[PROV-O](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termPROVO):** A W3C standard ontology for representing provenance information — enabling data lineage as queryable RDF triples within the knowledge graph.
- **[OTTR](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termOTTR):** A templating language for RDF that maps structured data columns to ontology properties using declarative stOTTR syntax — enabling concise DataFrame-to-RDF transformations.
- **[maplib](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termMaplib):** A Python library that applies OTTR templates to DataFrames to produce RDF — enabling the complete Silver-to-Gold transformation in as few as four lines of Python.
- **[RDF](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termRDF):** The W3C standard for representing linked data as subject-predicate-object triples — the foundational data model of the Semantic Gold layer.
- **[SPARQL](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termSPARQL):** The W3C standard query language for RDF knowledge graphs — used to navigate entity relationships, trace lineage, and execute cross-system queries in the Semantic Gold layer.
- **[Knowledge Graph](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termKnowledgeGraph):** A graph-structured data model where entities are connected by typed relationships — enabling navigation, reasoning, and semantic search across unified data.
- **[Medallion Architecture](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termMedallionArchitecture):** A data lakehouse design pattern with three layers: Bronze (raw ingestion), Silver (cleaned and typed with IRIs), and Gold (semantic RDF knowledge graph).

---

## Key Relationships

- [analysis](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23analysis) → [schema:author](http://schema.org/author) → [veronikaHeimsbakk](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23veronikaHeimsbakk)
- [analysis](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23analysis) → [schema:publisher](http://schema.org/publisher) → [modernData101](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23modernData101)
- [analysis](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23analysis) → [schema:hasPart](http://schema.org/hasPart) → [faqSection](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23faqSection)
- [analysis](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23analysis) → [schema:hasPart](http://schema.org/hasPart) → [glossarySection](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23glossarySection)
- [analysis](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23analysis) → [schema:hasPart](http://schema.org/hasPart) → [howtoSection](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23howtoSection)
- [bronzeLayer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23bronzeLayer) → [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) → [BronzeLayer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23BronzeLayer)
- [silverLayer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23silverLayer) → [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) → [SilverLayer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23SilverLayer)
- [goldLayer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23goldLayer) → [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) → [GoldLayer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23GoldLayer)
- [goldLayer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23goldLayer) → [usesVocabulary](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23usesVocabulary) → [dcatVocabulary](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dcatVocabulary)
- [goldLayer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23goldLayer) → [usesVocabulary](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23usesVocabulary) → [provOntology](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23provOntology)
- [dcatCatalog](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dcatCatalog) → [dcat:service](http://www.w3.org/ns/dcat#service) → [sparqlEndpointService](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23sparqlEndpointService)

---

## Related Resources

- [Source article on Modern Data 101](https://moderndata101.substack.com/p/the-semantic-medallion)
- [RDF Turtle Knowledge Graph](semantic-medallion-deepseek_v4pro-1.ttl) (788 triples)
- [JSON-LD Knowledge Graph](semantic-medallion-deepseek_v4pro-1.jsonld)
- [HTML Infographic](semantic-medallion-deepseek_v4pro-1.html)
- [Ontology & Instance Data for SPARQL](semantic-medallion-ontology-instance-data.ttl)
- [Author: Veronika Heimsbakk on LinkedIn](https://www.linkedin.com/in/vheimsbakk/)
- [SHACL for the Practitioner (book)](https://shacl.veronahe.no/)
- [Modern Data 101 Community](https://www.moderndata101.com/)
- [Veronika's Substack](https://veronahe.substack.com/)

---

*Generated 2026-05-18 using [kg-generator](https://github.com/OpenLinkSoftware/ai-agent-skills/tree/main/kg-generator) and [rdf-infographic-skill](https://github.com/OpenLinkSoftware/ai-agent-skills/tree/main/rdf-infographic-skill) via DeepSeek V4 Pro on Claude Code. Entity links via [URIBurner](https://linkeddata.uriburner.com/) describe service over RDF hash IRIs.*