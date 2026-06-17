# The Semantic Medallion: Building a Knowledge Graph-Powered Data Catalog

**Author:** [Veronika Heimsbakk](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23veronikaHeimsbakk) — Knowledge Graph Specialist, author of [SHACL for the Practitioner](https://shacl.veronahe.no/), [Data Treehouse](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dataTreehouse)
**Published:** May 14, 2026 · [Modern Data 101](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23modernData101)
**Source:** https://moderndata101.substack.com/p/the-semantic-medallion

Associated files:
- **RDF Turtle KG:** [the-semantic-medallion.ttl](the-semantic-medallion.ttl)
- **HTML Infographic:** [the-semantic-medallion.html](the-semantic-medallion.html)
- **Executable Instance Data:** [semantic-medallion-ontology-instance-data.ttl](semantic-medallion-ontology-instance-data.ttl)

---

## Overview

How you can transform raw data sources into a unified knowledge graph in four lines of Python.

The [Semantic Medallion](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23semanticMedallion) extends the standard [Bronze/Silver/Gold medallion data architecture](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23medallionArchitecture) by transforming the Gold layer into a connected [knowledge graph](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23knowledgeGraph) rather than isolated clean tables. The result is a [data catalog](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dataCatalog) that answers relational questions — *"Show me everything about this record"*, *"Which sources contribute to our customer records?"*, *"Find customers with billing issues who have active contracts"* — rather than serving static table lists.

---

## Core Concepts

### [Semantic Medallion](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23semanticMedallion)

An extension of the medallion data architecture where the Gold layer is transformed into a connected knowledge graph rather than isolated clean tables. Relationships are embedded in the data itself, not in external join logic.

### [IRI Minting](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23iriMinting)

Creating stable, globally unique identifiers (Internationalized Resource Identifiers) for every entity in the Silver layer — replacing database auto-increment IDs and GUIDs with identifiers that work across all systems. This is the biggest implementation challenge and requires upfront governance.

### [Entity Resolution](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23entityResolution)

Using `owl:sameAs` to link entities appearing in CRM, billing, and external registries — providing a unified view of every record across all systems.

### [Data Provenance](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23provenance)

Tracking the origin and lineage of data using [PROV-O](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23provOntology), expressed as queryable RDF triples rather than stored in a separate lineage tool with its own database.

### [Semantic Data Catalog](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23semanticCatalog)

A knowledge graph-powered catalog describing what things mean and how they relate — metadata and data unified in the same graph, with the catalog as part of the knowledge graph rather than a separate system pointing at data.

### [DataFrame-to-RDF Transformation](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23rdfTransformation)

The process of mapping structured DataFrames to RDF triples using [OTTR templates](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23ottrTemplates) and the [maplib](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23maplib) Python library — complete Silver-to-Gold transformation in four lines of Python.

---

## Architecture Layers

The medallion layers are reframed as **semantic enrichment stages**: Bronze (no semantics), Silver (local semantics via identifiers), Gold (global semantics via shared vocabulary) — and, at the apex, the **Platinum Layer** where Linked Data principles manifest a Semantic Web.

### [Bronze Layer — Raw Ingestion](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23bronzeLayer)

Standard raw data ingestion via orchestration tools. Data is ingested in its original format with **no semantic transformation**. Linked to raw source datasets via [DCAT](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dcatVocabulary). Everything starts here — raw, unprocessed, but fully captured.

### [Silver Layer — IRI Minting](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23silverLayer)

In addition to cleaning and typing, this layer focuses on **minting stable IRIs** for every entity — creating join keys that work across all systems. This is the biggest implementation challenge: establishing identifiers that remain consistent as new data sources are added.

### [Gold Layer — Semantic RDF](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23goldLayer)

Silver DataFrames are mapped to a shared ontology using a common vocabulary and published as RDF via four lines of Python. The relationships are **in the data**, not in join logic. A [DCAT Catalog](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dcatCatalog) describes the unified knowledge graph with a [SPARQL endpoint](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23sparqlEndpointService) distribution.

### [Platinum Layer — Semantic Web](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23platinumLayer)

The RDF-based Knowledge Graph is deployed using **Linked Data principles** — leveraging the power of hyperlinks for entity and relationship naming. IRIs are dereferenceable, globally unique identifiers; the knowledge graph becomes a node in the wider Semantic Web. This is the apex of the enrichment pipeline: from raw bytes in Bronze to globally interconnected, web-addressable knowledge in Platinum.

> "And the Platinum Layer is when the RDF based Knowledge Graph is deployed using Linked Data principles i.e., knowledge construction that leverages the power of hyperlinks for entity and relationship naming that manifests a Semantic Web."
>
> — [Kingsley Uyi Idehen](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fkidehen%23this), Founder & CEO of [OpenLink Software](https://www.openlinksw.com/) · [@kidehen](https://x.com/kidehen)

---

## Technologies

| Technology | Description |
|---|---|
| [maplib](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23maplib) | Python library for DataFrame-to-RDF transformation |
| [OTTR Templates](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23ottrTemplates) | Declarative stOTTR syntax mapping columns to ontology properties |
| [DCAT](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dcatVocabulary) | W3C Data Catalog Vocabulary — used by data.gov, European Data Portal |
| [PROV-O](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23provOntology) | W3C Provenance Ontology — data lineage as queryable triples |
| [SPARQL](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23sparqlQueryLanguage) | W3C query language for RDF knowledge graphs |
| [RDF](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23rdfStandard) | W3C Resource Description Framework — subject-predicate-object triples |

---

## Semantic Data Catalog Capabilities

A Semantic Medallion-powered data catalog provides three key capabilities that traditional structural catalogs cannot:

**[Entity Resolution Across Sources](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23entityResolutionCapability)** — Using `owl:sameAs` to unify customer records appearing in CRM, billing, and external registries under one identifier, enabling *"Show me everything we know about this record"* queries.

**[Semantic Search](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23semanticSearchCapability)** — Ontology subclass hierarchies enable search that understands concepts: a query for `ComplianceRelated` entities automatically includes `ComplianceOfficer`, `AuditRecord`, and `RegulatoryFiling` subtypes.

**[Impact Analysis](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23impactAnalysisCapability)** — Tracing graph relationships to find downstream dependencies when schemas change — identifying every dataset, report, and application affected by a modification to a source system.

---

## Industry Context

- [Data Management Industry](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dataManagementVertical): NAICS 518210 — Data Processing, Hosting, and Related Services (~$200B TAM, High automation readiness)
- [Knowledge Graph Consulting](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23knowledgeGraphConsultingVertical): NAICS 541511 — Custom Computer Programming Services (~$80B TAM, High automation readiness)

---

## Building a Semantic Medallion Data Catalog

### [Step 1: Ingest Raw Data into Bronze](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23step1)

Set up orchestration tools to ingest raw data from all source systems into the Bronze layer. Preserve original formats without transformation. Link datasets to sources via DCAT.

### [Step 2: Clean Data and Mint IRIs in Silver](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23step2)

Clean and type the data in the Silver layer. Critically, replace database auto-increment IDs with stable, globally unique IRIs for every entity. Define a consistent IRI naming scheme using your organisation's domain namespace.

### [Step 3: Design the Shared Ontology](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23step3)

Design a shared ontology that maps your business concepts to RDF classes and properties. Start with what is available from existing data models. Use standard vocabularies (DCAT, PROV-O, schema.org) where possible. Iterate and refine as understanding deepens.

### [Step 4: Define OTTR Templates](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23step4)

Create OTTR templates in stOTTR syntax that map your DataFrame columns to ontology properties. Each template defines how a row in your DataFrame becomes a set of RDF triples.

### [Step 5: Transform to RDF with maplib](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23step5)

Use the maplib Python library to apply your OTTR templates to the Silver DataFrames. This transformation produces RDF triples in as few as four lines of Python.

### [Step 6: Publish to Gold as a Knowledge Graph](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23step6)

Write the resulting RDF to the Gold layer — either as Turtle files on a data lake, or directly to a triplestore with a SPARQL endpoint. Register the knowledge graph in a DCAT Catalog with a SPARQL endpoint distribution.

### [Step 7: Query and Validate](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23step7)

Use SPARQL to validate the knowledge graph: run customer 360 queries to verify entity resolution, lineage queries to trace provenance, and cross-system queries to confirm relationships are correctly modelled. Iterate on the ontology and templates based on query results.

---

## SPARQL Query Examples

All four queries below are fully executable against the companion ontology and instance data in [`semantic-medallion-ontology-instance-data.ttl`](semantic-medallion-ontology-instance-data.ttl). The live links run queries against the [URIBurner SPARQL endpoint](https://linkeddata.uriburner.com/sparql); load the instance data first for complete results.

### Query 1: [Customer 360](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23customer360Query)

Retrieve every fact about customer `C-001` from every data source, unified under one identifier.

[▶ Run live query](https://linkeddata.uriburner.com/sparql?query=PREFIX%20%3A%20%3Chttps%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23%3E%0APREFIX%20schema%3A%20%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX%20prov%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fprov%23%3E%0APREFIX%20dcat%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fdcat%23%3E%0ADESCRIBE%20%3AC-001%0AFROM%20%3Chttps%3A%2F%2Flinkeddata.uriburner.com%2FDAV%2Fdemos%2Fdaas%2Fthe-semantic-medallion.ttl%3E&format=text%2Fhtml&timeout=30000)

```sparql
PREFIX : <https://moderndata101.substack.com/p/the-semantic-medallion#>
PREFIX schema: <http://schema.org/>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX dcat: <http://www.w3.org/ns/dcat#>

DESCRIBE :C-001
FROM <https://linkeddata.uriburner.com/DAV/demos/daas/the-semantic-medallion.ttl>
```

**What it returns:** All triples about Acme Corporation (`:C-001`) — name, email, phone, address, revenue, contracts, billing issues, account manager, source systems, and `owl:sameAs` links to CRM and billing representations.

---

### Query 2: [Data Lineage](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23lineageQuery)

Trace which sources contribute to customer records — identifying the provenance path from Gold entities back through Silver to Bronze datasets.

[▶ Run live query](https://linkeddata.uriburner.com/sparql?query=PREFIX%20%3A%20%3Chttps%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23%3E%0APREFIX%20prov%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fprov%23%3E%0APREFIX%20dcat%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fdcat%23%3E%0ASELECT%20%3Fsource%20%3Fdataset%20%3Fdistribution%0AFROM%20%3Chttps%3A%2F%2Flinkeddata.uriburner.com%2FDAV%2Fdemos%2Fdaas%2Fthe-semantic-medallion.ttl%3E%0AWHERE%20%7B%0A%20%20%3AC-001%20prov%3AwasDerivedFrom%20%3Fsource%20.%0A%20%20%3Fsource%20prov%3AhadPrimarySource%20%3Fdataset%20.%0A%20%20%3Fdataset%20dcat%3Adistribution%20%3Fdistribution%20.%0A%7D&format=text%2Fhtml&timeout=30000)

```sparql
PREFIX : <https://moderndata101.substack.com/p/the-semantic-medallion#>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX dcat: <http://www.w3.org/ns/dcat#>

SELECT ?source ?dataset ?distribution
FROM <https://linkeddata.uriburner.com/DAV/demos/daas/the-semantic-medallion.ttl>
WHERE {
  :C-001 prov:wasDerivedFrom ?source .
  ?source prov:hadPrimarySource ?dataset .
  ?dataset dcat:distribution ?distribution .
}
```

**What it returns:** The provenance chain for C-001 — that it is derived from `CRM-Salesforce` and `Billing-Stripe`, each with their Bronze raw datasets and distributions.

---

### Query 3: [Cross-System Relationship](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23crossSystemQuery)

Find all customers with open billing issues who also have active contracts — navigating relationships directly across systems without manual joins or table hunting.

[▶ Run live query](https://linkeddata.uriburner.com/sparql?query=PREFIX%20%3A%20%3Chttps%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23%3E%0APREFIX%20schema%3A%20%3Chttp%3A%2F%2Fschema.org%2F%3E%0ASELECT%20%3Fcustomer%20%3Fname%20%3FbillingIssue%20%3Fcontract%0AFROM%20%3Chttps%3A%2F%2Flinkeddata.uriburner.com%2FDAV%2Fdemos%2Fdaas%2Fthe-semantic-medallion.ttl%3E%0AWHERE%20%7B%0A%20%20%3Fcustomer%20a%20schema%3APerson%20%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20schema%3Aname%20%3Fname%20%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%3AhasBillingIssue%20%3FbillingIssue%20%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%3AhasActiveContract%20%3Fcontract%20.%0A%20%20%3FbillingIssue%20schema%3Astatus%20%22Open%22%20.%0A%20%20%3Fcontract%20schema%3Astatus%20%22Active%22%20.%0A%7D&format=text%2Fhtml&timeout=30000)

```sparql
PREFIX : <https://moderndata101.substack.com/p/the-semantic-medallion#>
PREFIX schema: <http://schema.org/>

SELECT ?customer ?name ?billingIssue ?contract
FROM <https://linkeddata.uriburner.com/DAV/demos/daas/the-semantic-medallion.ttl>
WHERE {
  ?customer a schema:Person ;
            schema:name ?name ;
            :hasBillingIssue ?billingIssue ;
            :hasActiveContract ?contract .
  ?billingIssue schema:status "Open" .
  ?contract schema:status "Active" .
}
```

**What it returns:** Acme Corporation (C-001) and Beta Industries (C-002) — both have open billing issues AND active Gold Support Plan contracts.

---

### Query 4: [Ontology Inspection](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23ontologyQuery)

Inspect the Semantic Medallion ontology — list all defined classes with their labels and descriptions.

[▶ Run live query](https://linkeddata.uriburner.com/sparql?query=PREFIX%20%3A%20%3Chttps%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT%20%3Fclass%20%3Flabel%20%3Fcomment%0AFROM%20%3Chttps%3A%2F%2Flinkeddata.uriburner.com%2FDAV%2Fdemos%2Fdaas%2Fthe-semantic-medallion.ttl%3E%0AWHERE%20%7B%0A%20%20%3Fclass%20a%20rdfs%3AClass%20%3B%0A%20%20%20%20%20%20%20%20%20rdfs%3Alabel%20%3Flabel%20%3B%0A%20%20%20%20%20%20%20%20%20rdfs%3Acomment%20%3Fcomment%20.%0A%20%20FILTER%28STRSTARTS%28STR%28%3Fclass%29%2C%20%22https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23%22%29%29%0A%7D%0AORDER%20BY%20%3Flabel&format=text%2Fhtml&timeout=30000)

```sparql
PREFIX : <https://moderndata101.substack.com/p/the-semantic-medallion#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?class ?label ?comment
FROM <https://linkeddata.uriburner.com/DAV/demos/daas/the-semantic-medallion.ttl>
WHERE {
  ?class a rdfs:Class ;
         rdfs:label ?label ;
         rdfs:comment ?comment .
  FILTER(STRSTARTS(STR(?class), "https://moderndata101.substack.com/p/the-semantic-medallion#"))
}
ORDER BY ?label
```

**What it returns:** All 9 custom classes in the Semantic Medallion ontology — `BronzeLayer`, `DataCatalogConnector`, `DataManagementIndustry`, `GoldLayer`, `Industry`, `KnowledgeGraphConsultingIndustry`, `MedallionLayer`, `SemanticEnrichmentProcess`, `SilverLayer`.

---

## FAQ

### 1. [What is the Semantic Medallion?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q1)

The [Semantic Medallion](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23semanticMedallion) is an extension of the traditional Bronze/Silver/Gold data lakehouse architecture where the [Gold layer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23goldLayer) is transformed into a connected [knowledge graph](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23knowledgeGraph) rather than isolated clean tables. Relationships are embedded in the data itself, not in external join logic, enabling [entity resolution](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23entityResolution), cross-system queries, and semantic search.

### 2. [How does the Bronze layer work?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q2)

The [Bronze layer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23bronzeLayer) handles standard raw data ingestion via orchestration tools. Data is ingested in its original format with no [semantic enrichment](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23semanticEnrichment). [DCAT](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dcatVocabulary) links these raw datasets to their source systems.

### 3. [What is the role of IRI minting in the Silver layer?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q3)

In the [Silver layer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23silverLayer), beyond cleaning and typing data, stable [IRIs](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termIRI) are [minted](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23iriMinting) for every entity. These globally unique identifiers replace database auto-increment IDs and GUIDs, creating join keys that work across all systems rather than being scoped to a single database.

### 4. [How does the Gold layer transform data into a knowledge graph?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q4)

The [Gold layer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23goldLayer) maps Silver DataFrames to a shared ontology using [OTTR templates](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23ottrTemplates) and the [maplib](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23maplib) Python library, then publishes the result as [RDF](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23rdfStandard). Rather than creating separate Parquet/Delta tables requiring manual join logic, the data becomes a connected knowledge graph where relationships are stored as triples — making the data inherently relational.

### 5. [Can the DataFrame-to-RDF transformation really be done in four lines of Python?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q5)

Yes. The article demonstrates the complete Silver-to-Gold [transformation](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23rdfTransformation): (1) load the DataFrame, (2) define an [OTTR template](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23ottrTemplates) mapping columns to ontology properties, (3) apply the template using [maplib](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23maplib), and (4) publish the resulting RDF to the Gold layer. The power comes from declarative templates rather than imperative code.

### 6. [Why use DCAT instead of a custom catalog schema?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q6)

[DCAT](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dcatVocabulary) is a W3C standard used by data.gov, the European Data Portal, and thousands of organisations. It provides: (1) interoperability with existing data catalog ecosystems, (2) rich standardised metadata, (3) a unified graph where the catalog IS part of the knowledge graph — not a separate system, and (4) built-in integration with [PROV-O](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23provOntology) for provenance.

### 7. [How does entity resolution work across data sources?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q7)

[Entity resolution](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23entityResolution) uses `owl:sameAs` assertions to link entities appearing in CRM, billing, and external registries. A customer in both the sales system and the billing system is linked via an `owl:sameAs` triple, creating a unified view. [SPARQL](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23sparqlQueryLanguage) queries then navigate all facts about that customer regardless of which source system contributed them.

### 8. [How does PROV-O enable data lineage?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q8)

[PROV-O](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23provOntology) expresses [data provenance](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23provenance) as RDF triples — recording which entities were derived from which sources, which activities generated them, and which agents were responsible. Instead of storing lineage in a separate tool with its own database, PROV-O provenance triples live in the [knowledge graph](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23knowledgeGraph), making lineage queryable using the same SPARQL endpoint as the data itself.

### 9. [What is the biggest implementation challenge?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q9)

The biggest challenge is not the RDF conversion itself, but establishing stable identifiers ([IRIs](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termIRI)) in the [Silver layer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23silverLayer). This requires upfront design of IRI naming conventions and careful governance to ensure identifiers remain consistent as new data sources are added.

### 10. [How should you approach ontology design?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q10)

Start with the ontology available from your existing data models, then refine it incrementally as you understand cross-system relationships better. Do not aim for a perfect ontology upfront — the knowledge graph can evolve as your understanding deepens.

### 11. [Semantic Gold vs traditional Gold layer?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q11)

A traditional [Gold layer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23goldLayer) consists of separate Parquet or Delta tables requiring manual join logic in SQL or dbt scripts. The [Semantic Gold layer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23semanticCatalog) is RDF where relationships are embedded in the data as triples — eliminating table hunting, manual JOINs, and fragile transformation pipelines. The data becomes inherently connected rather than depending on external join logic.

### 12. [What is the bigger picture of this architecture?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q12)

The medallion layers are reframed as [semantic enrichment](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23semanticEnrichment) stages: [Bronze](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23bronzeLayer) provides no semantics, [Silver](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23silverLayer) provides local semantics through stable identifiers, and [Gold](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23goldLayer) provides global semantics through a shared vocabulary. This transforms the medallion from a storage pattern into a semantic enrichment pipeline.

---

## Glossary

- **[Semantic Medallion](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termSemanticMedallion):** An architecture pattern extending the Bronze/Silver/Gold medallion with knowledge graph semantics — transforming the Gold layer into connected RDF.
- **[IRI](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termIRI):** A globally unique, stable identifier for an entity — replacing database auto-increment IDs with identifiers that work across all systems.
- **[DCAT](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termDCAT):** W3C Data Catalog Vocabulary — describing data catalogs, datasets, distributions, and data services. Used by data.gov and the European Data Portal.
- **[PROV-O](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termPROVO):** W3C Provenance Ontology — representing provenance information as queryable RDF triples within the knowledge graph.
- **[OTTR](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termOTTR):** Reasonable Ontology Templates — a templating language for RDF that maps structured data columns to ontology properties using declarative stOTTR syntax.
- **[maplib](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termMaplib):** A Python library that applies OTTR templates to DataFrames to produce RDF — enabling the complete Silver-to-Gold transformation in as few as four lines of Python.
- **[RDF](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termRDF):** The W3C Resource Description Framework — subject-predicate-object triples forming the foundational data model of the Semantic Gold layer.
- **[SPARQL](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termSPARQL):** The W3C standard query language for RDF knowledge graphs — used to navigate entity relationships, trace lineage, and execute cross-system queries.
- **[Knowledge Graph](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termKnowledgeGraph):** A graph-structured data model where entities are connected by typed relationships — enabling navigation, reasoning, and semantic search across unified data.
- **[Medallion Architecture](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termMedallionArchitecture):** A data lakehouse design pattern with Bronze (raw ingestion), Silver (cleaned and typed with IRIs), and Gold (semantic RDF knowledge graph) layers.

---

## Key Relationships

- [analysis](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23analysis) → `schema:author` → [Veronika Heimsbakk](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23veronikaHeimsbakk)
- [analysis](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23analysis) → `schema:publisher` → [Modern Data 101](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23modernData101)
- [bronzeLayer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23bronzeLayer) → `:hasSemanticEnrichment` → [noSemantics](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23noSemantics)
- [silverLayer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23silverLayer) → `:hasSemanticEnrichment` → [localSemantics](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23localSemantics)
- [goldLayer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23goldLayer) → `:hasSemanticEnrichment` → [globalSemantics](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23globalSemantics)
- [goldLayer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23goldLayer) → `:usesVocabulary` → [DCAT](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dcatVocabulary), [PROV-O](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23provOntology)
- [dcatCatalog](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dcatCatalog) → `dcat:service` → [sparqlEndpointService](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23sparqlEndpointService)
- [entityResolutionCapability](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23entityResolutionCapability) → `:enablesCapability` → [queryEverythingAboutRecord](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23queryEverythingAboutRecord)
- [impactAnalysisCapability](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23impactAnalysisCapability) → `:enablesCapability` → [downstreamDependencyTrace](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23downstreamDependencyTrace)

---

## Related Resources

**[▶ Explore Knowledge Graph using SPARQL](https://linkeddata.uriburner.com/sparql?query=SELECT+DISTINCT+%3Fsubject+%3Ftype+%28SAMPLE%28%3Flabel%29+AS+%3Fname%29%0AFROM+%3Chttps%3A%2F%2Flinkeddata.uriburner.com%2FDAV%2Fdemos%2Fdaas%2Fthe-semantic-medallion.ttl%3E%0AWHERE+%7B%0A++%3Fsubject+a+%3Ftype+.%0A++OPTIONAL+%7B+%3Fsubject+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23label%3E+%3Flabel+%7D%0A%7D%0AGROUP+BY+%3Fsubject+%3Ftype%0AORDER+BY+%3Ftype%0ALIMIT+50&format=text%2Fhtml&timeout=30000)**

- [Source article on Modern Data 101](https://moderndata101.substack.com/p/the-semantic-medallion)
- [RDF Turtle Knowledge Graph](the-semantic-medallion.ttl)
- [Interactive HTML Infographic](the-semantic-medallion.html)
- [Executable Ontology & Instance Data](semantic-medallion-ontology-instance-data.ttl)
- [Author: Veronika Heimsbakk on LinkedIn](https://www.linkedin.com/in/vheimsbakk/)
- [Author's Substack: veronahe](https://veronahe.substack.com/)
- [SHACL for the Practitioner (book)](https://shacl.veronahe.no/)
- [Modern Data 101 Community](https://www.moderndata101.com/)
- [DCAT Vocabulary (W3C)](https://www.w3.org/TR/vocab-dcat-3/)
- [PROV-O Ontology (W3C)](https://www.w3.org/TR/prov-o/)
- [maplib on PyPI](https://pypi.org/project/maplib/)

---

*Generated 2026-05-19 using [kg-generator](https://github.com/OpenLinkSoftware/ai-agent-skills/tree/main/kg-generator) and [rdf-infographic-skill](https://github.com/OpenLinkSoftware/ai-agent-skills/tree/main/rdf-infographic-skill) via Claude Sonnet 4.6 in Cowork mode. Entity links via [URIBurner](https://linkeddata.uriburner.com/) describe service over RDF hash IRIs.*
