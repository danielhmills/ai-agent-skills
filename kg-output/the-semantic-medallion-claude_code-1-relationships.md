# The Semantic Medallion: Building a Knowledge Graph-Powered Data Catalog

**Author:** [Veronika Heimsbakk](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23veronikaHeimsbakk) — Knowledge Graph Specialist at [Data Treehouse](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dataTreehouse)
**Published:** May 14, 2026 on [Modern Data 101](https://moderndata101.substack.com/p/the-semantic-medallion)
**RDF Resolver:** [URIBurner](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion)
**Companion Files:** [HTML Infographic](the-semantic-medallion-claude_code-1-infographic.html) · [RDF Turtle](the-semantic-medallion-claude_code-1.ttl) · [JSON-LD](the-semantic-medallion-claude_code-1.jsonld)

---

## Overview

The Semantic Medallion proposes augmenting the traditional Bronze→Silver→Gold medallion data architecture by making the Gold layer an RDF knowledge graph instead of clean tabular data. The W3C Data Catalog Vocabulary (DCAT) is then used to weave catalog metadata into the same graph, creating a self-describing, knowledge graph-powered data catalog where metadata and customer facts coexist in a single queryable SPARQL endpoint.

---

## The Three Medallion Layers

The [Semantic Medallion Ontology](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23semanticMedallionOntology) defines the core architecture:

### [Bronze Layer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23bronzeLayer)

- **Semantic enrichment:** None
- **Order:** 1
- **Purpose:** Harvest raw data from source systems (CRM, ERP, billing, support). No transformations applied. Data is stored as-is with original formats and timestamps.
- **Transforms to:** [Silver Layer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23silverLayer)

### [Silver Layer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23silverLayer)

- **Semantic enrichment:** Local
- **Order:** 2
- **Purpose:** Mint stable globally unique IRIs for every entity. This is the critical step — raw records become identifiable, linkable resources. Without stable IRIs, cross-system linking requires fragile key matching.
- **IRI Minting:** Yes
- **Transforms to:** [Gold Layer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23goldLayer)

### [Gold Layer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23goldLayer)

- **Semantic enrichment:** Global
- **Order:** 3
- **Purpose:** Map DataFrames to RDF via a shared ontology using OTTR templates and maplib. Global semantics enable cross-system entity resolution, semantic search, and impact analysis through SPARQL.

---

## Technology Stack

| Tool | Description |
|------|-------------|
| [maplib](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23maplib) | Python library for DataFrame-to-RDF transformation. Single `maplib.map()` call replaces hundreds of lines of code. |
| [OTTR Templates](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23ottrTemplates) | Template-based ontology mapping framework using stOTTR syntax for declarative column-to-RDF mapping. |
| [DCAT](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23dcatCatalog) | W3C Data Catalog Vocabulary — standard RDF vocabulary for describing catalogs, datasets, and data services. |
| [PROV-O](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23provO) | W3C Provenance Ontology for tracking data lineage from source systems to Gold-layer entities. |
| [SHACL](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23shacl) | Shapes Constraint Language for validating RDF graph quality and enforcing data rules. |
| [IRI Minting](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23iriMinting) | Process of assigning stable globally unique identifiers to every entity at the Silver layer. |

---

## SPARQL Query Examples

All queries target the [URIBurner SPARQL Endpoint](https://linkeddata.uriburner.com/sparql) and are backed by sample instance data (3 customers, 4 data sources, 3 contracts, 2 billing issues) in the [Semantic Medallion knowledge graph](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23sparqlQuerySection).

### Query 1: All Facts About Customer C-001

**Description:** Retrieve every property-value pair for a single customer — the simplest entry point into the catalog. Equivalent to "show me everything we know about Acme Corporation."

**Entity:** [sparqlQuery1](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23sparqlQuery1)

```sparql
PREFIX : <https://moderndata101.substack.com/p/the-semantic-medallion#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX prov: <http://www.w3.org/ns/prov#>

SELECT ?property ?value WHERE {
  :C-001 ?property ?value .
  OPTIONAL { ?value rdfs:label ?label }
}
ORDER BY ?property
```

[▶ Run Live Query](https://linkeddata.uriburner.com/sparql?default-graph-uri=&query=PREFIX%20%3A%20%3Chttps%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20prov%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fprov%23%3E%0ASELECT%20%3Fproperty%20%3Fvalue%20WHERE%20%7B%0A%20%20GRAPH%20%3Chttps%3A%2F%2Flinkeddata.uriburner.com%2FDAV%2Fdemos%2Fdaas%2Fthe-semantic-medallion-claude_code-1.ttl%3E%20%7B%0A%20%20%20%20%3AC-001%20%3Fproperty%20%3Fvalue%20.%0A%20%20%20%20OPTIONAL%20%7B%20%3Fvalue%20rdfs%3Alabel%20%3Flabel%20%7D%0A%20%20%7D%0A%7D%0AORDER%20BY%20%3Fproperty&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

---

### Query 2: Contributing Data Sources for Customer C-001

**Description:** Trace the provenance chain — list all source systems (SalesForce CRM, SAP ERP, Stripe Billing) that contributed records for Acme Corporation using PROV-O `wasDerivedFrom`.

**Entity:** [sparqlQuery2](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23sparqlQuery2)

```sparql
PREFIX : <https://moderndata101.substack.com/p/the-semantic-medallion#>
PREFIX prov: <http://www.w3.org/ns/prov#>

SELECT ?source ?sourceName ?sourceType WHERE {
  :C-001 prov:wasDerivedFrom ?source .
  ?source a :DataSource ;
    :sourceName ?sourceName ;
    :sourceType ?sourceType .
}
ORDER BY ?sourceName
```

[▶ Run Live Query](https://linkeddata.uriburner.com/sparql?default-graph-uri=&query=PREFIX%20%3A%20%3Chttps%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23%3E%0APREFIX%20prov%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fprov%23%3E%0ASELECT%20%3Fsource%20%3FsourceName%20%3FsourceType%20WHERE%20%7B%0A%20%20GRAPH%20%3Chttps%3A%2F%2Flinkeddata.uriburner.com%2FDAV%2Fdemos%2Fdaas%2Fthe-semantic-medallion-claude_code-1.ttl%3E%20%7B%0A%20%20%20%20%3AC-001%20prov%3AwasDerivedFrom%20%3Fsource%20.%0A%20%20%20%20%3Fsource%20a%20%3ADataSource%20%3B%0A%20%20%20%20%20%20%3AsourceName%20%3FsourceName%20%3B%0A%20%20%20%20%20%20%3AsourceType%20%3FsourceType%20.%0A%20%20%7D%0A%7D%0AORDER%20BY%20%3FsourceName&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

---

### Query 3: Customers with Billing Issues AND Active Contracts

**Description:** Cross-domain pattern detection — find all customers who have both an open billing issue and an active contract. This query spans billing, contract, and customer domains — a pattern that would require complex joins across siloed SQL databases but is natural in a knowledge graph.

**Entity:** [sparqlQuery3](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23sparqlQuery3)

```sparql
PREFIX : <https://moderndata101.substack.com/p/the-semantic-medallion#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?customer ?name ?issueDescription ?contractStatus WHERE {
  ?customer a :Customer ;
    :hasName ?name ;
    :hasBillingIssue ?issue ;
    :hasContract ?contract .
  ?issue a :BillingIssue ;
    :issueDescription ?issueDescription .
  ?contract a :Contract ;
    :contractStatus "Active" .
}
ORDER BY ?name
```

[▶ Run Live Query](https://linkeddata.uriburner.com/sparql?default-graph-uri=&query=PREFIX%20%3A%20%3Chttps%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT%20%3Fcustomer%20%3Fname%20%3FissueDescription%20%3FcontractStatus%20WHERE%20%7B%0A%20%20GRAPH%20%3Chttps%3A%2F%2Flinkeddata.uriburner.com%2FDAV%2Fdemos%2Fdaas%2Fthe-semantic-medallion-claude_code-1.ttl%3E%20%7B%0A%20%20%20%20%3Fcustomer%20a%20%3ACustomer%20%3B%0A%20%20%20%20%20%20%3AhasName%20%3Fname%20%3B%0A%20%20%20%20%20%20%3AhasBillingIssue%20%3Fissue%20%3B%0A%20%20%20%20%20%20%3AhasContract%20%3Fcontract%20.%0A%20%20%20%20%3Fissue%20a%20%3ABillingIssue%20%3B%0A%20%20%20%20%20%20%3AissueDescription%20%3FissueDescription%20.%0A%20%20%20%20%3Fcontract%20a%20%3AContract%20%3B%0A%20%20%20%20%20%20%3AcontractStatus%20%22Active%22%20.%0A%20%20%7D%0A%7D%0AORDER%20BY%20%3Fname&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

---

## Sample Instance Data

The following sample data makes all SPARQL queries executable:

### Customers

| Entity | Name | Email | Contract | Billing Issue |
|--------|------|-------|----------|---------------|
| [C-001](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23C-001) | Acme Corporation | contact@acmecorp.example | Enterprise Plan (Active) | Duplicate charge on March invoice |
| [C-002](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23C-002) | Beta Industries | info@betaindustries.example | Standard Plan (Active) | None |
| [C-003](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23C-003) | Gamma Solutions | support@gammasolutions.example | Premium Plan (Active) | Incorrect plan tier applied |

### Data Sources

| Entity | Name | Type |
|--------|------|------|
| [srcCRM](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23srcCRM) | SalesForce CRM | CRM |
| [srcERP](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23srcERP) | SAP ERP | ERP |
| [srcBilling](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23srcBilling) | Stripe Billing | Billing |
| [srcSupport](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23srcSupport) | Zendesk Support | Support |

---

## Relationships

Entity relationships organized from the central [Semantic Medallion Analysis](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23analysis) outward:

### Architecture Relationships

- [Bronze Layer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23bronzeLayer) —[rdf:type](https://linkeddata.uriburner.com/describe/?url=http%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23type)→ [BronzeLayer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23BronzeLayer)
- [Bronze Layer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23bronzeLayer) —[:transformsTo](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23transformsTo)→ [Silver Layer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23silverLayer)
- [Silver Layer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23silverLayer) —[:transformsTo](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23transformsTo)→ [Gold Layer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23goldLayer)
- Each Layer —[rdfs:isDefinedBy](https://linkeddata.uriburner.com/describe/?url=http%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23isDefinedBy)→ [Semantic Medallion Ontology](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23semanticMedallionOntology)

### Customer Domain Relationships

- [C-001 (Acme Corp)](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23C-001) —[:hasContract](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23hasContract)→ [contractC001](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23contractC001)
- [C-001 (Acme Corp)](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23C-001) —[:hasBillingIssue](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23hasBillingIssue)→ [billingIssueC001](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23billingIssueC001)
- [C-001 (Acme Corp)](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23C-001) —[prov:wasDerivedFrom](https://linkeddata.uriburner.com/describe/?url=http%3A%2F%2Fwww.w3.org%2Fns%2Fprov%23wasDerivedFrom)→ [srcCRM](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23srcCRM), [srcERP](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23srcERP), [srcBilling](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23srcBilling)
- [C-002 (Beta Ind)](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23C-002) —[prov:wasDerivedFrom](https://linkeddata.uriburner.com/describe/?url=http%3A%2F%2Fwww.w3.org%2Fns%2Fprov%23wasDerivedFrom)→ [srcCRM](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23srcCRM), [srcSupport](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23srcSupport)
- [C-003 (Gamma Sol)](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23C-003) —[prov:wasDerivedFrom](https://linkeddata.uriburner.com/describe/?url=http%3A%2F%2Fwww.w3.org%2Fns%2Fprov%23wasDerivedFrom)→ [srcCRM](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23srcCRM), [srcBilling](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23srcBilling), [srcSupport](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23srcSupport)

### Query-to-Data Relationships

- [Query 1 (Customer Facts)](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23sparqlQuery1) —[schema:target](https://linkeddata.uriburner.com/describe/?url=http%3A%2F%2Fschema.org%2Ftarget)→ [C-001](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23C-001)
- [Query 3 (Billing+Active)](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23sparqlQuery3) —[schema:target](https://linkeddata.uriburner.com/describe/?url=http%3A%2F%2Fschema.org%2Ftarget)→ [Customer](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23Customer)

### Provenance

- [Analysis](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23analysis) —[prov:wasGeneratedBy](https://linkeddata.uriburner.com/describe/?url=http%3A%2F%2Fwww.w3.org%2Fns%2Fprov%23wasGeneratedBy)→ [kg-generator skill](https://github.com/OpenLinkSoftware/ai-agent-skills/tree/main/kg-generator)

---

## FAQ

- **[What is the Semantic Medallion?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q1)** — An augmentation of the traditional medallion architecture where the Gold layer becomes an RDF knowledge graph instead of clean tabular data, with DCAT catalog metadata woven into the same graph.

- **[How does the Bronze layer differ from traditional medallion Bronze?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q2)** — It functions identically — raw data harvest without transformation. The difference emerges at Silver where IRIs are minted.

- **[What is IRI minting and why is it important?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q3)** — Assigning stable globally unique identifiers to every entity. Without stable IRIs, linking customer records across CRM, ERP, and billing would require fragile key matching.

- **[What role do OTTR templates play?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q4)** — Declarative templates mapping DataFrame columns to RDF ontology classes and properties. A single template transforms millions of Silver-layer rows consistently.

- **[How does maplib simplify the DataFrame-to-RDF transformation?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q5)** — Reduces hundreds of lines of triple-construction code to four lines: `maplib.map(dataframe, template, result_container)`.

- **[What is DCAT and why is it used?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q6)** — W3C standard for describing catalogs in RDF. Catalog metadata and instance data coexist in the same graph, making the catalog self-describing.

- **[How does PROV-O enhance the catalog?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q7)** — Tracks data lineage. Answers "Which CRM and billing records contributed to this customer view?"

- **[What kinds of queries does the knowledge graph catalog enable?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q8)** — Entity lookup, provenance tracing, and cross-domain pattern detection (billing issues + active contracts).

- **[How does the Semantic Medallion handle entity resolution?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q9)** — Through IRI alignment at the Silver layer. Records from different sources referring to the same entity link to the same IRI.

- **[What is SHACL and how does it fit?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q10)** — W3C standard for validating RDF graphs. Enforces data quality rules at the Gold layer.

- **[What are the key lessons?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q11)** — Start IRIs early. Design ontologies iteratively. Each layer adds meaning — none → local → global semantics.

- **[How does this compare to a traditional data catalog?](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23q12)** — Traditional catalogs describe where data lives; a knowledge graph catalog captures how data connects across systems.

---

## Glossary

- **[Medallion Architecture](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termMedallionArchitecture)** — Data architecture pattern: Bronze (raw), Silver (cleaned), Gold (analytics-ready). Semantic variant redefines Gold as an RDF knowledge graph.

- **[IRI Minting](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termIRIMinting)** — Assigning stable globally unique identifiers to entities, enabling cross-system linking.

- **[OTTR](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termOTTR)** — Reasonable Ontology Templates — declarative framework for mapping structured data to RDF.

- **[maplib](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termMaplib)** — Python library for DataFrame-to-RDF transformation using OTTR templates.

- **[DCAT](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termDCAT)** — W3C Data Catalog Vocabulary — standard RDF vocabulary for describing data catalogs.

- **[PROV-O](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termPROVO)** — W3C Provenance Ontology for tracking data lineage.

- **[SHACL](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termSHACL)** — Shapes Constraint Language — validates RDF graphs against shape conditions.

- **[Knowledge Graph](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termKnowledgeGraph)** — Graph-structured data with typed relationships, enabling semantic querying beyond relational databases.

- **[SPARQL](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termSPARQL)** — W3C standard query language for RDF knowledge graphs.

- **[Semantic Enrichment](https://linkeddata.uriburner.com/describe/?url=https%3A%2F%2Fmoderndata101.substack.com%2Fp%2Fthe-semantic-medallion%23termSemanticEnrichment)** — Progressive addition of meaning: none (Bronze) → local (Silver) → global (Gold).

---

## How-To: Build a Semantic Medallion Pipeline

1. **Harvest Raw Data into the Bronze Layer** — Ingest raw data from all source systems (CRM, ERP, billing, support). Apply no transformations.

2. **Mint Stable IRIs at the Silver Layer** — Create stable globally unique IRIs for every entity using a consistent pattern. This is the most critical step.

3. **Design a Shared Ontology** — Define core classes (Customer, Contract, DataSource) and properties. Start minimal and expand iteratively.

4. **Author OTTR Templates** — Write stOTTR templates mapping DataFrame columns to your ontology. Define how each row becomes RDF.

5. **Transform to RDF with maplib** — Call `maplib.map(dataframe, template, result_container)`. Validate output RDF syntax.

6. **Weave in DCAT and PROV-O Metadata** — Describe each layer as a DCAT Dataset. Add provenance links to source systems.

7. **Query and Validate** — Load into a SPARQL triplestore. Apply SHACL shapes. Query the catalog for entity lookup, provenance, and cross-domain patterns.

---

## Related Resources

- [Original Source Article](https://moderndata101.substack.com/p/the-semantic-medallion)
- [HTML Infographic Companion](the-semantic-medallion-claude_code-1-infographic.html)
- [RDF Turtle Knowledge Graph](the-semantic-medallion-claude_code-1.ttl)
- [JSON-LD Knowledge Graph](the-semantic-medallion-claude_code-1.jsonld)
- [URIBurner SPARQL Endpoint](https://linkeddata.uriburner.com/sparql)
- [Explore Knowledge Graph via SPARQL](https://linkeddata.uriburner.com/sparql?query=PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT%0A%20%20%20%20%3Ftype%0A%20%20%20%20%28SAMPLE%28%3Fs%29%20AS%20%3FsampleEntity%29%0A%20%20%20%20%28SAMPLE%28%3Flabel%29%20AS%20%3FsampleLabel%29%0A%20%20%20%20%28COUNT%28%3Fs%29%20AS%20%3FentityCount%29%0AWHERE%20%7B%0A%20%20%20%20GRAPH%20%3Chttps%3A%2F%2Flinkeddata.uriburner.com%2FDAV%2Fdemos%2Fdaas%2Fthe-semantic-medallion-claude_code-1.ttl%3E%20%7B%0A%20%20%20%20%20%20%20%20%3Fs%20rdf%3Atype%20%3Ftype%20.%0A%20%20%20%20%20%20%20%20OPTIONAL%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Fs%20rdfs%3Alabel%20%3Flabel%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%7D%0AGROUP%20BY%20%3Ftype%0AORDER%20BY%20DESC%28%3FentityCount%29&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

---

*Generated by Claude Code (deepseek-v4-pro) using [kg-generator](https://github.com/OpenLinkSoftware/ai-agent-skills/tree/main/kg-generator) and [rdf-infographic-skill](https://github.com/OpenLinkSoftware/ai-agent-skills/tree/main/rdf-infographic-skill) · 2026-05-18*
