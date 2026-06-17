"""
Build RDF Knowledge Graph: Databricks Tables → Virtual Knowledge Graph with Virtuoso
Source: https://community.openlinksw.com/t/from-databricks-tables-to-a-virtual-knowledge-graph-with-virtuoso/6293

Script-Assisted KG generation — deterministic RDF construction via rdflib.
"""
import rdflib
from rdflib import RDF, RDFS, OWL, XSD, Literal, URIRef, BNode
from rdflib.namespace import NamespaceManager
from datetime import date

# ── Namespaces ────────────────────────────────────────────────────────────────
SOURCE = "https://community.openlinksw.com/t/from-databricks-tables-to-a-virtual-knowledge-graph-with-virtuoso/6293"
BASE  = SOURCE + "#"

SCHEMA  = rdflib.Namespace("http://schema.org/")
SKOS    = rdflib.Namespace("http://www.w3.org/2004/02/skos/core#")
PROV    = rdflib.Namespace("http://www.w3.org/ns/prov#")
DBO     = rdflib.Namespace("http://dbpedia.org/ontology/")
DBR     = rdflib.Namespace("http://dbpedia.org/resource/")
WD      = rdflib.Namespace("http://www.wikidata.org/entity/")
FOAF    = rdflib.Namespace("http://xmlns.com/foaf/0.1/")
DCTERMS = rdflib.Namespace("http://purl.org/dc/terms/")

g = rdflib.Graph()
g.bind("", BASE)
g.bind("schema", SCHEMA)
g.bind("skos", SKOS)
g.bind("prov", PROV)
g.bind("owl", OWL)
g.bind("dbo", DBO)
g.bind("dbr", DBR)
g.bind("wd", WD)
g.bind("foaf", FOAF)
g.bind("dcterms", DCTERMS)

NS = rdflib.Namespace(BASE)
TODAY = str(date.today())  # 2026-06-16

# ── Self-describing document entity ───────────────────────────────────────────
doc = URIRef(BASE.rstrip("#"))
g.add((doc, RDF.type, SCHEMA.CreativeWork))
g.add((doc, SCHEMA.name, Literal("Databricks-Virtuoso Virtual Knowledge Graph — RDF Knowledge Graph", lang="en")))
g.add((doc, SCHEMA.description, Literal("Comprehensive RDF knowledge graph covering the value proposition of generating AI Agent-friendly Knowledge Graphs from Databricks-hosted data using Virtuoso, R2RML, SPARQL, and Linked Data principles.", lang="en")))
g.add((doc, SCHEMA.dateCreated, Literal(TODAY, datatype=XSD.date)))
g.add((doc, SCHEMA.dateModified, Literal(TODAY, datatype=XSD.date)))

# ── Lightweight Ontology ──────────────────────────────────────────────────────
g.add((NS.ontology, RDF.type, OWL.Ontology))
g.add((NS.ontology, SCHEMA.name, Literal("Databricks-Virtuoso Knowledge Graph Ontology", lang="en")))
g.add((NS.ontology, SCHEMA.description, Literal("Lightweight ontology for modelling the Databricks-to-Virtuoso virtual knowledge graph pipeline: ODBC attachment, R2RML mapping, SPARQL querying, Linked Data entity dereferencing, and AI Agent consumption patterns.", lang="en")))
g.add((NS.ontology, SCHEMA.identifier, Literal(SOURCE)))
g.add((NS.ontology, RDFS.label, Literal("Databricks-Virtuoso KG Ontology", lang="en")))

# Custom classes
for cls_id, cls_label, cls_comment in [
    ("VirtualKnowledgeGraph", "Virtual Knowledge Graph", "A knowledge graph constructed over existing relational data without physical data movement, using virtual database attachment and R2RML declarative mappings."),
    ("DataPlatform", "Data Platform", "A cloud or on-premises platform hosting structured data (warehouses, lakes, lakehouses)."),
    ("GraphReasoningCapability", "Graph Reasoning Capability", "The ability to traverse relationships and discover patterns across connected data using ontology-defined semantics rather than implicit foreign keys."),
    ("SemanticEnrichment", "Semantic Enrichment", "The process of augmenting relational data with ontology-defined classes, properties, and inferred relationships to produce a knowledge graph."),
    ("VirtualDatabaseAttachment", "Virtual Database Attachment", "Connecting to a remote database via ODBC/JDBC without copying data — tables appear in the local catalog as virtual references."),
    ("R2RMLMapping", "R2RML Mapping", "A W3C R2RML declarative mapping that defines how relational tables and columns map to RDF classes and properties."),
    ("QuadMapGeneration", "Quad Map Generation", "The conversion of R2RML mappings into Virtuoso's internal Quad Map format for efficient SPARQL-to-SQL translation."),
    ("LinkedDataEntityNavigation", "Linked Data Entity Navigation", "The ability to dereference entity URIs via HTTP content negotiation, receiving HTML for browsers or RDF for machines."),
]:
    c = NS[cls_id]
    g.add((c, RDF.type, RDFS.Class))
    g.add((c, RDFS.label, Literal(cls_label, lang="en")))
    g.add((c, RDFS.comment, Literal(cls_comment, lang="en")))
    g.add((c, RDFS.isDefinedBy, NS.ontology))

# Custom properties
for prop_id, prop_label, prop_comment, prop_domain in [
    ("usesDataPlatform", "uses data platform", "The data platform whose tables are being virtualized into the knowledge graph.", NS.VirtualKnowledgeGraph),
    ("implementsStandard", "implements standard", "A W3C or industry standard employed in the solution.", NS.VirtualKnowledgeGraph),
    ("requiresComponent", "requires component", "A software component or driver required for the pipeline.", NS.VirtualKnowledgeGraph),
    ("producesArtifact", "produces artifact", "An artifact (named graph, entity URI, SPARQL result) produced by the pipeline.", NS.VirtualKnowledgeGraph),
    ("enablesCapability", "enables capability", "A capability unlocked by the virtual knowledge graph approach.", NS.VirtualKnowledgeGraph),
    ("mapsTo", "maps to", "The RDF class or property a relational construct maps to.", NS.R2RMLMapping),
]:
    p = NS[prop_id]
    g.add((p, RDF.type, RDF.Property))
    g.add((p, RDFS.label, Literal(prop_label, lang="en")))
    g.add((p, RDFS.comment, Literal(prop_comment, lang="en")))
    g.add((p, RDFS.domain, prop_domain))
    g.add((p, RDFS.isDefinedBy, NS.ontology))

# ── Main Analysis Article ─────────────────────────────────────────────────────
article = NS.analysis
g.add((article, RDF.type, SCHEMA.CreativeWork))
g.add((article, RDF.type, SCHEMA.TechArticle))
g.add((article, SCHEMA.name, Literal("From Databricks Tables to a Virtual Knowledge Graph with Virtuoso", lang="en")))
g.add((article, SCHEMA.headline, Literal("From Databricks Tables to a Virtual Knowledge Graph with Virtuoso", lang="en")))
g.add((article, SCHEMA.abstract, Literal("A step-by-step guide demonstrating how to unlock machine-computable entity relationships across existing Databricks data without migration, duplication, or platform lock-in — using RDF, SPARQL, R2RML, and Virtuoso's Virtual Database to create an AI Agent-friendly Knowledge Graph deployed on the Semantic Web.", lang="en")))
g.add((article, SCHEMA.articleBody, Literal("Modern AI and analytics need graph reasoning capabilities — the ability to traverse relationships and discover patterns across connected data — but most enterprise data sits in relational warehouses where relationships rely on implicit foreign keys. This guide shows how to bridge that gap using open W3C standards: RDF for entity relationships, SPARQL for graph querying, and R2RML for exposing relational data as graphs. Hyperlinks (IRIs) serve as globally unique identifiers enabling disparate systems to be connected and reasoned over as a whole. The result is a Knowledge Graph that extends beyond the boundaries of any single database, platform, or application.", lang="en")))
g.add((article, SCHEMA.url, Literal(SOURCE)))
g.add((article, SCHEMA.datePublished, Literal("2026-06-09", datatype=XSD.date)))
g.add((article, SCHEMA.dateModified, Literal(TODAY, datatype=XSD.date)))
g.add((article, SCHEMA.inLanguage, Literal("en")))
g.add((article, SCHEMA.about, NS.virtualKnowledgeGraphConcept))
g.add((article, SCHEMA.about, NS.databricksPlatform))
g.add((article, SCHEMA.about, NS.virtuosoPlatform))
g.add((article, SCHEMA.about, DBR["Semantic_Web"]))
g.add((article, SCHEMA.about, DBR["Knowledge_graph"]))

# ── Author ────────────────────────────────────────────────────────────────────
author = URIRef("https://github.com/danielhmills#this")
g.add((author, RDF.type, SCHEMA.Person))
g.add((author, SCHEMA.name, Literal("danielhm", lang="en")))
g.add((author, SCHEMA.alternateName, Literal("danielhmills", lang="en")))
g.add((author, SCHEMA.url, Literal("https://github.com/danielhmills")))
g.add((author, SCHEMA.identifier, Literal("https://github.com/danielhmills")))
g.add((article, SCHEMA.author, author))

# ── Organizations ─────────────────────────────────────────────────────────────
# OpenLink Software
openlink = DBR.OpenLink_Software
g.add((openlink, RDF.type, SCHEMA.Organization))
g.add((openlink, SCHEMA.name, Literal("OpenLink Software", lang="en")))
g.add((openlink, SCHEMA.url, Literal("https://www.openlinksw.com/")))
g.add((openlink, SCHEMA.description, Literal("Creator of Virtuoso Universal Server, URIBurner, and enterprise knowledge graph infrastructure.", lang="en")))
g.add((openlink, OWL.sameAs, WD.Q7096326))
g.add((article, SCHEMA.mentions, openlink))
g.add((NS.virtuosoPlatform, SCHEMA.manufacturer, openlink))

# Databricks
databricks_org = DBR.Databricks
g.add((databricks_org, RDF.type, SCHEMA.Organization))
g.add((databricks_org, SCHEMA.name, Literal("Databricks", lang="en")))
g.add((databricks_org, SCHEMA.url, Literal("https://www.databricks.com/")))
g.add((databricks_org, SCHEMA.description, Literal("Cloud data platform provider offering data lakehouse architecture combining data lakes and data warehouses.", lang="en")))
g.add((databricks_org, OWL.sameAs, WD.Q52014331))
g.add((article, SCHEMA.mentions, databricks_org))

# ── Software Applications ─────────────────────────────────────────────────────
# Virtuoso
virtuoso = NS.virtuosoPlatform
g.add((virtuoso, RDF.type, SCHEMA.SoftwareApplication))
g.add((virtuoso, SCHEMA.name, Literal("Virtuoso Universal Server", lang="en")))
g.add((virtuoso, SCHEMA.alternateName, Literal("OpenLink Virtuoso", lang="en")))
g.add((virtuoso, SCHEMA.url, Literal("https://virtuoso.openlinksw.com/")))
g.add((virtuoso, SCHEMA.description, Literal("A secure, high-performance, cross-platform relational and graph database server with virtual database, SPARQL, RDF, SQL, and R2RML support.", lang="en")))
g.add((virtuoso, OWL.sameAs, DBR.Virtuoso_Universal_Server))
g.add((virtuoso, SCHEMA.applicationCategory, Literal("Database Management System", lang="en")))
g.add((virtuoso, SCHEMA.applicationCategory, Literal("Knowledge Graph Platform", lang="en")))
g.add((virtuoso, SCHEMA.applicationCategory, Literal("SPARQL Endpoint", lang="en")))

# Databricks Spark ODBC Driver
odbc_driver = NS.databricksOdbcDriver
g.add((odbc_driver, RDF.type, SCHEMA.SoftwareApplication))
g.add((odbc_driver, SCHEMA.name, Literal("Databricks ODBC Driver", lang="en")))
g.add((odbc_driver, SCHEMA.url, Literal("https://www.databricks.com/spark/odbc-driver-download")))
g.add((odbc_driver, SCHEMA.description, Literal("ODBC driver enabling SQL connectivity between Virtuoso and Databricks SQL warehouses for virtual database attachment.", lang="en")))
g.add((odbc_driver, SCHEMA.applicationCategory, Literal("Database Driver", lang="en")))

# SPARQLWorks
sparqlworks = NS.sparqlworks
g.add((sparqlworks, RDF.type, SCHEMA.SoftwareApplication))
g.add((sparqlworks, SCHEMA.name, Literal("SPARQLWorks", lang="en")))
g.add((sparqlworks, SCHEMA.url, Literal("https://github.com/danielhmills/sparqlworks/")))
g.add((sparqlworks, SCHEMA.description, Literal("A SPARQL query visualisation tool that renders CONSTRUCT query results as interactive node-link diagrams for exploring knowledge graph relationships.", lang="en")))
g.add((sparqlworks, SCHEMA.applicationCategory, Literal("Graph Visualization", lang="en")))

# kg-generator skill
kg_skill = URIRef("https://github.com/OpenLinkSoftware/ai-agent-skills/tree/main/kg-generator#this")
g.add((kg_skill, RDF.type, SCHEMA.SoftwareApplication))
g.add((kg_skill, RDF.type, PROV.SoftwareAgent))
g.add((kg_skill, SCHEMA.name, Literal("kg-generator skill", lang="en")))
g.add((kg_skill, SCHEMA.url, Literal("https://github.com/OpenLinkSoftware/ai-agent-skills/tree/main/kg-generator")))
g.add((kg_skill, SCHEMA.description, Literal("Knowledge graph generation skill for AI agents — transforms documents and web content into structured RDF.", lang="en")))
g.add((article, PROV.wasGeneratedBy, kg_skill))

# ── Standards ─────────────────────────────────────────────────────────────────
standards = [
    (NS.stdRDF, "RDF", DBR["Resource_Description_Framework"],
     "Resource Description Framework — W3C standard for representing entity relationships as subject-predicate-object triples."),
    (NS.stdSPARQL, "SPARQL", DBR.SPARQL,
     "SPARQL Protocol and RDF Query Language — W3C standard for querying and manipulating RDF graphs."),
    (NS.stdR2RML, "R2RML", NS["stdR2RML-ext"],
     "RDB to RDF Mapping Language — W3C recommendation for exposing relational data as RDF graphs using declarative mappings."),
    (NS.stdODBC, "ODBC", DBR["Open_Database_Connectivity"],
     "Open Database Connectivity — standard API for accessing database management systems."),
    (NS.stdLinkedData, "Linked Data", DBR["Linked_data"],
     "A method of publishing structured data using HTTP URIs and RDF so that it can be interlinked and become more useful through semantic queries."),
]
for iri, name, ext_iri, desc in standards:
    g.add((iri, RDF.type, SCHEMA.DefinedTerm))
    g.add((iri, SCHEMA.name, Literal(name, lang="en")))
    g.add((iri, SCHEMA.description, Literal(desc, lang="en")))
    g.add((iri, RDFS.seeAlso, ext_iri))

# ── Core Concepts ─────────────────────────────────────────────────────────────
concepts = [
    (NS.virtualKnowledgeGraphConcept, "Virtual Knowledge Graph",
     "A knowledge graph constructed over existing relational data without physical data movement — using virtual database attachment to expose tables, R2RML to define semantic mappings, and SPARQL for graph querying. The data stays in Databricks; the semantics are layered on top via Virtuoso."),
    (NS.graphReasoningConcept, "Graph Reasoning",
     "The ability to traverse relationships and discover patterns across connected data using ontology-defined semantics rather than implicit foreign keys. In the bakehouse example, foreign keys become navigable hyperlinks connecting Transaction→Franchise→City through named relationships."),
    (NS.semanticEnrichmentConcept, "Semantic Enrichment",
     "The process of augmenting relational data with ontology-defined classes (e.g., :Transaction, :Franchise), properties (e.g., :franchise, :totalPrice), and inferred relationships to produce a machine-readable knowledge graph. R2RML mappings are the declarative bridge between SQL schemas and RDF vocabularies."),
    (NS.zeroDataMovementConcept, "Zero Data Movement",
     "A defining characteristic of the virtual knowledge graph approach — Databricks tables are attached via ODBC as virtual references, not copied. SPARQL queries are translated to SQL and executed remotely against the Databricks warehouse at query time."),
    (NS.looselyCoupledSemanticLayer, "Loosely Coupled Semantic Layer",
     "A semantic enrichment layer that sits atop existing data platforms without tight coupling — replacing ETL-driven data copying with standards-based virtualization. The knowledge graph is an overlay, not a replacement or another silo."),
    (NS.hyperlinkBasedEntityIdentity, "Hyperlink-Based Entity Identity",
     "The use of IRIs (Internationalized Resource Identifiers) as globally unique, dereferenceable entity identifiers — enabling entities from different systems (Databricks tables, external reference data, other knowledge graphs) to be linked and reasoned over as a single connected graph."),
    (NS.aiAgentFriendlyKG, "AI Agent-Friendly Knowledge Graph",
     "A knowledge graph designed for consumption by AI agents — featuring dereferenceable entity URIs, machine-readable RDF representations, SPARQL endpoints for structured querying, and navigable entity relationships. The Databricks-Virtuoso pipeline produces such a graph: an AI agent can follow entity links, execute SPARQL queries, and retrieve structured context without custom API integration."),
    (NS.contentNegotiationConcept, "Content Negotiation",
     "An HTTP mechanism where the server inspects the client's Accept header to determine the response format — returning an HTML description page for browsers and RDF (Turtle, JSON-LD, RDF/XML) for semantic agents and RDF clients."),
]
for iri, name, desc in concepts:
    g.add((iri, RDF.type, SKOS.Concept))
    g.add((iri, SCHEMA.name, Literal(name, lang="en")))
    g.add((iri, SCHEMA.description, Literal(desc, lang="en")))

# ── Key Services ──────────────────────────────────────────────────────────────
# URIBurner SPARQL endpoint
uriburner_sparql = NS.uriburnerSparqlEndpoint
g.add((uriburner_sparql, RDF.type, SCHEMA.WebAPI))
g.add((uriburner_sparql, SCHEMA.name, Literal("URIBurner SPARQL Endpoint", lang="en")))
g.add((uriburner_sparql, SCHEMA.url, Literal("https://linkeddata.uriburner.com/sparql")))
g.add((uriburner_sparql, SCHEMA.description, Literal("Public SPARQL endpoint for querying knowledge graphs hosted in Virtuoso-backed URIBurner.", lang="en")))

# Demo SPARQL endpoint (demo.openlinksw.com)
demo_endpoint = NS.demoSparqlEndpoint
g.add((demo_endpoint, RDF.type, SCHEMA.WebAPI))
g.add((demo_endpoint, SCHEMA.name, Literal("OpenLink Demo SPARQL Endpoint", lang="en")))
g.add((demo_endpoint, SCHEMA.url, Literal("https://demo.openlinksw.com/sparql")))
g.add((demo_endpoint, SCHEMA.description, Literal("Demo SPARQL endpoint hosting the bakehouse virtual knowledge graph for live query testing.", lang="en")))

# ── Named Graphs ──────────────────────────────────────────────────────────────
named_graphs = [
    (NS.graphR2RML, "urn:databricks:bakehouse:r2rml", "R2RML mapping graph — defines the SQL-to-RDF mapping rules for the bakehouse schema."),
    (NS.graphOntology, "http://www.databricks.com/bakehouse#", "Ontology graph — defines the bakehouse vocabulary: classes (Transaction, Franchise, Customer) and properties (franchise, totalPrice, city)."),
    (NS.graphInstance, "https://linkeddata.uriburner.com/DAV/demos/daas/databricks-virtuoso-kg-deepseek_v4pro-1.ttl", "Instance data graph — the runtime virtual knowledge graph containing entity triples generated by applying R2RML mappings to the live Databricks tables."),
]
for iri, uri, desc in named_graphs:
    g.add((iri, RDF.type, SCHEMA.DataFeed))
    g.add((iri, SCHEMA.name, Literal(uri, lang="en")))
    g.add((iri, SCHEMA.description, Literal(desc, lang="en")))
    g.add((iri, SCHEMA.identifier, Literal(uri)))

# ── Databricks bakehouse dataset entities ─────────────────────────────────────
# Sample dataset tables
tables = [
    (NS.tableCustomers, "sales_customers", "Customer records with names, contact details, and loyalty status."),
    (NS.tableFranchises, "sales_franchises", "Franchise locations with city, country, and coordinate data."),
    (NS.tableTransactions, "sales_transactions", "Transaction records linking customers to franchises with line items and pricing."),
    (NS.tableSuppliers, "sales_suppliers", "Supplier records for ingredients and materials."),
    (NS.tableReviews, "sales_reviews", "Customer reviews and ratings for franchises."),
]
for iri, name, desc in tables:
    g.add((iri, RDF.type, SCHEMA.Dataset))
    g.add((iri, RDF.type, NS["DataPlatform"]))  # actually these are tables, but modeled as sub-datasets
    g.add((iri, SCHEMA.name, Literal(name, lang="en")))
    g.add((iri, SCHEMA.description, Literal(desc, lang="en")))

# Bakehouse sample data — overall
g.add((NS.bakehouseDataset, RDF.type, SCHEMA.Dataset))
g.add((NS.bakehouseDataset, SCHEMA.name, Literal("samples.bakehouse", lang="en")))
g.add((NS.bakehouseDataset, SCHEMA.description, Literal("A fictional bakery chain dataset provided by Databricks as a public sample — includes customers, franchises, suppliers, transactions, and reviews tables.", lang="en")))
g.add((NS.bakehouseDataset, SCHEMA.hasPart, NS.tableCustomers))
g.add((NS.bakehouseDataset, SCHEMA.hasPart, NS.tableFranchises))
g.add((NS.bakehouseDataset, SCHEMA.hasPart, NS.tableTransactions))
g.add((NS.bakehouseDataset, SCHEMA.hasPart, NS.tableSuppliers))
g.add((NS.bakehouseDataset, SCHEMA.hasPart, NS.tableReviews))

# ── GitHub Repository ─────────────────────────────────────────────────────────
repo = NS.demoRepo
g.add((repo, RDF.type, SCHEMA.SoftwareSourceCode))
g.add((repo, SCHEMA.name, Literal("databricks-sample-kg", lang="en")))
g.add((repo, SCHEMA.url, Literal("https://github.com/danielhmills/databricks-sample-kg")))
g.add((repo, SCHEMA.description, Literal("Companion repository containing ODBC configuration templates, R2RML mappings, ontology, and setup scripts for the Databricks-to-Virtuoso virtual knowledge graph pipeline.", lang="en")))
g.add((repo, SCHEMA.codeRepository, Literal("https://github.com/danielhmills/databricks-sample-kg")))

# ── Capabilities enabled ──────────────────────────────────────────────────────
capabilities = [
    (NS.capGraphReasoning, "Graph reasoning on existing data",
     "SPARQL queries over Databricks tables without data movement — SQL is generated and executed at query time against the live Databricks warehouse."),
    (NS.capStandardsInterop, "Standards-based interoperability",
     "W3C standards (RDF, SPARQL, R2RML) prevent vendor lock-in — the knowledge graph is portable and queryable by any standards-compliant SPARQL client or AI agent."),
    (NS.capZeroMovement, "Zero data movement",
     "Virtuoso's Virtual Database attaches Databricks tables via ODBC as virtual references — no ETL, no duplication, no stale copies."),
    (NS.capSemanticEnrichment, "Semantic enrichment",
     "R2RML mappings add ontology-defined classes, properties, and inferred relationships — transforming implicit foreign keys into navigable semantic links."),
    (NS.capProductionGrade, "Production-grade infrastructure",
     "ACID compliance through the underlying Databricks warehouse, federated SPARQL for cross-graph queries, and Virtuoso's proven SPARQL-to-SQL query federation."),
    (NS.capLinkedDataNavigation, "Linked Data entity navigation",
     "Every entity (customer, franchise, transaction) receives a dereferenceable HTTP URI with content negotiation — browsers see HTML descriptions, AI agents retrieve machine-readable RDF."),
]
for iri, name, desc in capabilities:
    g.add((iri, RDF.type, SCHEMA.ActionAccessSpecification))
    g.add((iri, SCHEMA.name, Literal(name, lang="en")))
    g.add((iri, SCHEMA.description, Literal(desc, lang="en")))

# ── HowTo ─────────────────────────────────────────────────────────────────────
howto = NS.howtoSection
g.add((howto, RDF.type, SCHEMA.HowTo))
g.add((howto, SCHEMA.name, Literal("How to Build a Virtual Knowledge Graph from Databricks Tables using Virtuoso", lang="en")))
g.add((howto, SCHEMA.description, Literal("Seven-step guide to creating an AI Agent-friendly knowledge graph from Databricks-hosted data without migration, duplication, or platform lock-in.", lang="en")))
g.add((howto, SCHEMA.isPartOf, article))
g.add((article, SCHEMA.hasPart, howto))

steps = [
    (NS.step1, 1, "Create the ODBC DSN",
     "Configure a Databricks ODBC Data Source Name (DSN) — install the Databricks ODBC Driver, obtain workspace Host/HTTP Path/Personal Access Token, and populate odbcinst.ini and odbc.ini with the driver and connection details."),
    (NS.step2, 2, "Register the DSN in Virtuoso",
     "Access the External Data Sources Manager in Virtuoso Conductor at /conductor/vdb_conn_dsn.vspx to register the databricks_odbc DSN for use by Virtuoso's Virtual Database engine."),
    (NS.step3, 3, "Connect to the Data Source",
     "Find databricks_odbc in the External Data Sources list, click Connect, supply the username (token) and password (personal access token), and establish the ODBC connection from Virtuoso to the Databricks SQL warehouse."),
    (NS.step4, 4, "Clone the Demo Repository",
     "Clone the companion GitHub repository containing ODBC templates, R2RML mapping files, ontology, and setup scripts: git clone https://github.com/danielhmills/databricks-sample-kg.git."),
    (NS.step5, 5, "Run the Quick Setup Script",
     "Execute quick_setup.sql via isql — this script attaches each Databricks table (ATTACH TABLE ... FROM 'databricks_odbc'), grants SPARQL_SELECT privileges, loads the R2RML mapping and ontology via SPARQL LOAD, generates quad maps via R2RML_MAKE_QM_FROM_G, and configures URL rewrite rules for Linked Data content negotiation."),
    (NS.step6, 6, "Test the Attached Tables",
     "Verify the virtual attachment by running a SQL SELECT query against the virtual tables (e.g., SELECT TOP 10 * FROM databricks.bakehouse.sales_customers) via isql or the Conductor iSQL UI."),
    (NS.step7, 7, "Verify the Knowledge Graph with SPARQL",
     "Run SPARQL queries against the virtual knowledge graph — test entity type discovery (SELECT * FROM <...> WHERE { ?s a ?o }), cross-table joins (Revenue by Franchise), and CONSTRUCT queries for graph visualization in SPARQLWorks. Confirm dereferenceable entity URIs respond to both browsers and RDF clients via content negotiation."),
]
for iri, pos, name, text in steps:
    g.add((iri, RDF.type, SCHEMA.HowToStep))
    g.add((iri, SCHEMA.position, Literal(pos, datatype=XSD.integer)))
    g.add((iri, SCHEMA.name, Literal(name, lang="en")))
    g.add((iri, SCHEMA.text, Literal(text, lang="en")))
    g.add((iri, SCHEMA.isPartOf, howto))
    g.add((howto, SCHEMA.step, iri))

# ── SPARQL Query Examples ─────────────────────────────────────────────────────
sparql_queries = [
    (NS.sparqlEntityTypes, "Entity Type Discovery",
     "SPARQL SELECT rdf:type FROM <https://linkeddata.uriburner.com/DAV/demos/daas/databricks-virtuoso-kg-deepseek_v4pro-1.ttl> WHERE { ?s a ?o } LIMIT 10",
     "SELECT *\nFROM <https://linkeddata.uriburner.com/DAV/demos/daas/databricks-virtuoso-kg-deepseek_v4pro-1.ttl>\nWHERE\n{\n  ?s a ?o\n}\nLIMIT 10",
     "text/x-html+tr",
     "http://demo.openlinksw.com/sparql?default-graph-uri=&qtxt=SELECT+*%0D%0AFROM+%3Chttp%3A%2F%2Fdemo.openlinksw.com%2Fdatabricks-bakehouse-r2rml%23%3E%0D%0AWHERE%0D%0A%7B%0D%0A++%3Fs+a+%3Fo%0D%0A%7D%0D%0ALIMIT+10"),

    (NS.sparqlRevenueByFranchise, "Revenue by Franchise (Cross-Table SPARQL Join)",
     "SPARQL SELECT with SUM aggregation joining Transaction and Franchise tables via the :franchise property, grouped by franchise and city.",
     "PREFIX : <http://www.databricks.com/bakehouse#>\n\nSELECT\n?franchise\n?franchiseCity\nSUM(?totalPrice) as ?revenue\nFROM <https://linkeddata.uriburner.com/DAV/demos/daas/databricks-virtuoso-kg-deepseek_v4pro-1.ttl>\nWHERE\n{\n  ?transaction a :Transaction;\n   :franchise ?franchise;\n   :totalPrice ?totalPrice.\n\n  ?franchise :city ?franchiseCity.\n}\nGROUP BY ?franchise ?franchiseCity\nORDER BY DESC(?revenue)\nLIMIT 10",
     "text/x-html+tr",
     "https://demo.openlinksw.com/sparql?default-graph-uri=&qtxt=PREFIX+%3A+%3Chttp%3A%2F%2Fwww.databricks.com%2Fbakehouse%23%3E%0A%0ASELECT%0A%3Ffranchise%0A%3FfranchiseCity%0ASUM(%3FtotalPrice)+as+%3Frevenue%0AFROM+%3Chttp%3A%2F%2Fdemo.openlinksw.com%2Fdatabricks-bakehouse-r2rml%23%3E%0AWHERE%0A%7B%0A++%3Ftransaction+a+%3ATransaction%3B%0A+++%3Afranchise+%3Ffranchise%3B%0A+++%3AtotalPrice+%3FtotalPrice.%0A%0A++%3Ffranchise+%3Acity+%3FfranchiseCity.%0A%7D%0AGROUP+BY+%3Ffranchise+%3FfranchiseCity%0AORDER+BY+DESC(%3Frevenue)%0ALIMIT+10"),

    (NS.sparqlConstructVisualization, "CONSTRUCT for Graph Visualization (SPARQLWorks)",
     "SPARQL CONSTRUCT extracting the Transaction-Franchise-City subgraph for interactive node-link visualization in SPARQLWorks.",
     "PREFIX : <http://www.databricks.com/bakehouse#>\n\nCONSTRUCT\n{\n  ?transaction a :Transaction;\n   :franchise ?franchise;\n   :totalPrice ?totalPrice.\n\n  ?franchise :city ?franchiseCity.\n}\nWHERE\n{\n  GRAPH <https://linkeddata.uriburner.com/DAV/demos/daas/databricks-virtuoso-kg-deepseek_v4pro-1.ttl>\n  {\n    ?transaction a :Transaction;\n     :franchise ?franchise;\n     :totalPrice ?totalPrice.\n\n    ?franchise :city ?franchiseCity.\n  }\n}\nLIMIT 100",
     "text/x-html-nice-turtle",
     "https://demo.openlinksw.com/sparql?default-graph-uri=&query=PREFIX+%3A+%3Chttp%3A%2F%2Fwww.databricks.com%2Fbakehouse%23%3E%0A%0ACONSTRUCT%0A%7B%0A++%3Ftransaction+a+%3ATransaction%3B%0A+++%3Afranchise+%3Ffranchise%3B%0A+++%3AtotalPrice+%3FtotalPrice.%0A%0A++%3Ffranchise+%3Acity+%3FfranchiseCity.%0A%7D%0AWHERE%0A%7B%0A++GRAPH+%3Chttp%3A%2F%2Fdemo.openlinksw.com%2Fdatabricks-bakehouse-r2rml%23%3E%0A++%7B%0A++++%3Ftransaction+a+%3ATransaction%3B%0A+++++%3Afranchise+%3Ffranchise%3B%0A+++++%3AtotalPrice+%3FtotalPrice.%0A%0A++++%3Ffranchise+%3Acity+%3FfranchiseCity.%0A++%7D%0A%7D%0ALIMIT+100"),

    # ── Dashboard Analytics Queries ──────────────────────────────────────────

    (NS.sparqlRevenueByCity, "Dashboard: Revenue by City (Geographic Distribution)",
     "Geographic revenue breakdown — aggregates totalPrice by franchise city for a regional performance dashboard.",
     "PREFIX : <http://www.databricks.com/bakehouse#>\n\nSELECT\n?city\n(COUNT(DISTINCT ?transaction) AS ?orderCount)\n(SUM(?totalPrice) AS ?revenue)\n(ROUND(AVG(?totalPrice)) AS ?avgOrderValue)\nFROM <https://linkeddata.uriburner.com/DAV/demos/daas/databricks-virtuoso-kg-deepseek_v4pro-1.ttl>\nWHERE {\n  ?transaction a :Transaction;\n   :franchise ?franchise;\n   :totalPrice ?totalPrice.\n  ?franchise :city ?city.\n}\nGROUP BY ?city\nORDER BY DESC(?revenue)",
     "text/x-html+tr",
     "https://demo.openlinksw.com/sparql?default-graph-uri=&query=PREFIX+%3A+%3Chttp%3A%2F%2Fwww.databricks.com%2Fbakehouse%23%3E%0ASELECT%0A%3Fcity%0A(COUNT(DISTINCT+%3Ftransaction)+AS+%3ForderCount)%0A(SUM(%3FtotalPrice)+AS+%3Frevenue)%0A(ROUND(AVG(%3FtotalPrice))+AS+%3FavgOrderValue)%0AFROM+%3Chttp%3A%2F%2Fdemo.openlinksw.com%2Fdatabricks-bakehouse-r2rml%23%3E%0AWHERE+%7B%0A++%3Ftransaction+a+%3ATransaction%3B%0A+++%3Afranchise+%3Ffranchise%3B%0A+++%3AtotalPrice+%3FtotalPrice.%0A++%3Ffranchise+%3Acity+%3Fcity.%0A%7D%0AGROUP+BY+%3Fcity%0AORDER+BY+DESC(%3Frevenue)&format=text%2Fx-html%2Btr&timeout=0&debug=on&run=+Run+Query+"),

    (NS.sparqlTopCustomers, "Dashboard: Top 10 Customers by Total Spend",
     "Customer value analysis — ranks customers by total spend across all their transactions for a CRM dashboard.",
     "PREFIX : <http://www.databricks.com/bakehouse#>\n\nSELECT\n?customerName\n(COUNT(DISTINCT ?transaction) AS ?purchaseCount)\n(SUM(?totalPrice) AS ?lifetimeValue)\n(ROUND(SUM(?totalPrice)/COUNT(DISTINCT ?transaction)) AS ?avgPurchaseValue)\nFROM <https://linkeddata.uriburner.com/DAV/demos/daas/databricks-virtuoso-kg-deepseek_v4pro-1.ttl>\nWHERE {\n  ?transaction a :Transaction;\n   :customer ?customer;\n   :totalPrice ?totalPrice.\n  ?customer :customerName ?customerName.\n}\nGROUP BY ?customerName\nORDER BY DESC(?lifetimeValue)\nLIMIT 10",
     "text/x-html+tr",
     "https://demo.openlinksw.com/sparql?default-graph-uri=&query=PREFIX+%3A+%3Chttp%3A%2F%2Fwww.databricks.com%2Fbakehouse%23%3E%0ASELECT%0A%3FcustomerName%0A(COUNT(DISTINCT+%3Ftransaction)+AS+%3FpurchaseCount)%0A(SUM(%3FtotalPrice)+AS+%3FlifetimeValue)%0A(ROUND(SUM(%3FtotalPrice)%2FCOUNT(DISTINCT+%3Ftransaction))+AS+%3FavgPurchaseValue)%0AFROM+%3Chttp%3A%2F%2Fdemo.openlinksw.com%2Fdatabricks-bakehouse-r2rml%23%3E%0AWHERE+%7B%0A++%3Ftransaction+a+%3ATransaction%3B%0A+++%3Acustomer+%3Fcustomer%3B%0A+++%3AtotalPrice+%3FtotalPrice.%0A++%3Fcustomer+%3AcustomerName+%3FcustomerName.%0A%7D%0AGROUP+BY+%3FcustomerName%0AORDER+BY+DESC(%3FlifetimeValue)%0ALIMIT+10&format=text%2Fx-html%2Btr&timeout=0&debug=on&run=+Run+Query+"),

    (NS.sparqlTopRatedFranchises, "Dashboard: Top Rated Franchises (Customer Satisfaction)",
     "Customer satisfaction metrics — averages review ratings per franchise for a quality monitoring dashboard.",
     "PREFIX : <http://www.databricks.com/bakehouse#>\n\nSELECT\n?franchiseName\n?city\n(COUNT(?review) AS ?reviewCount)\n(ROUND(AVG(?rating))*10/10 AS ?avgRating)\nFROM <https://linkeddata.uriburner.com/DAV/demos/daas/databricks-virtuoso-kg-deepseek_v4pro-1.ttl>\nWHERE {\n  ?review a :Review;\n   :franchise ?franchise;\n   :rating ?rating.\n  ?franchise :city ?city.\n  OPTIONAL { ?franchise :franchiseName ?franchiseName. }\n}\nGROUP BY ?franchiseName ?city\nHAVING (COUNT(?review) >= 3)\nORDER BY DESC(?avgRating)\nLIMIT 10",
     "text/x-html+tr",
     "https://demo.openlinksw.com/sparql?default-graph-uri=&query=PREFIX+%3A+%3Chttp%3A%2F%2Fwww.databricks.com%2Fbakehouse%23%3E%0ASELECT%0A%3FfranchiseName%0A%3Fcity%0A(COUNT(%3Freview)+AS+%3FreviewCount)%0A(ROUND(AVG(%3Frating))*10%2F10+AS+%3FavgRating)%0AFROM+%3Chttp%3A%2F%2Fdemo.openlinksw.com%2Fdatabricks-bakehouse-r2rml%23%3E%0AWHERE+%7B%0A++%3Freview+a+%3AReview%3B%0A+++%3Afranchise+%3Ffranchise%3B%0A+++%3Arating+%3Frating.%0A++%3Ffranchise+%3Acity+%3Fcity.%0A++OPTIONAL+%7B+%3Ffranchise+%3AfranchiseName+%3FfranchiseName.+%7D%0A%7D%0AGROUP+BY+%3FfranchiseName+%3Fcity%0AHAVING+(COUNT(%3Freview)+%3E%3D+3)%0AORDER+BY+DESC(%3FavgRating)%0ALIMIT+10&format=text%2Fx-html%2Btr&timeout=0&debug=on&run=+Run+Query+"),

    (NS.sparqlSupplierProductFlow, "Dashboard: Supplier-Ingredient-Franchise Product Flow",
     "Supply chain visibility — traces supplier ingredients to the franchises that use them for a supply chain dashboard.",
     "PREFIX : <http://www.databricks.com/bakehouse#>\n\nSELECT\n?supplierName\n?ingredientName\n(COUNT(DISTINCT ?franchise) AS ?franchisesServed)\nFROM <https://linkeddata.uriburner.com/DAV/demos/daas/databricks-virtuoso-kg-deepseek_v4pro-1.ttl>\nWHERE {\n  ?supply a :SupplyContract;\n   :supplier ?supplier;\n   :ingredient ?ingredient;\n   :franchise ?franchise.\n  ?supplier :supplierName ?supplierName.\n  ?ingredient :ingredientName ?ingredientName.\n}\nGROUP BY ?supplierName ?ingredientName\nORDER BY DESC(?franchisesServed)\nLIMIT 15",
     "text/x-html+tr",
     "https://demo.openlinksw.com/sparql?default-graph-uri=&query=PREFIX+%3A+%3Chttp%3A%2F%2Fwww.databricks.com%2Fbakehouse%23%3E%0ASELECT%0A%3FsupplierName%0A%3FingredientName%0A(COUNT(DISTINCT+%3Ffranchise)+AS+%3FfranchisesServed)%0AFROM+%3Chttp%3A%2F%2Fdemo.openlinksw.com%2Fdatabricks-bakehouse-r2rml%23%3E%0AWHERE+%7B%0A++%3Fsupply+a+%3ASupplyContract%3B%0A+++%3Asupplier+%3Fsupplier%3B%0A+++%3Aingredient+%3Fingredient%3B%0A+++%3Afranchise+%3Ffranchise.%0A++%3Fsupplier+%3AsupplierName+%3FsupplierName.%0A++%3Fingredient+%3AingredientName+%3FingredientName.%0A%7D%0AGROUP+BY+%3FsupplierName+%3FingredientName%0AORDER+BY+DESC(%3FfranchisesServed)%0ALIMIT+15&format=text%2Fx-html%2Btr&timeout=0&debug=on&run=+Run+Query+"),

    (NS.sparqlOrderSizeDistribution, "Dashboard: Order Size Distribution (Revenue Segmentation)",
     "Revenue segmentation analysis — buckets transactions by value range for a financial performance dashboard.",
     "PREFIX : <http://www.databricks.com/bakehouse#>\n\nSELECT\n?orderSizeBucket\n(COUNT(?transaction) AS ?transactionCount)\n(SUM(?totalPrice) AS ?totalRevenue)\n(ROUND(AVG(?totalPrice)) AS ?avgValue)\nFROM <https://linkeddata.uriburner.com/DAV/demos/daas/databricks-virtuoso-kg-deepseek_v4pro-1.ttl>\nWHERE {\n  ?transaction a :Transaction;\n   :totalPrice ?totalPrice.\n  BIND(\n    IF(?totalPrice < 10, \"Small (<$10)\",\n    IF(?totalPrice < 30, \"Medium ($10-$30)\",\n    IF(?totalPrice < 60, \"Large ($30-$60)\",\n    \"Enterprise (>$60)\")))\n    AS ?orderSizeBucket)\n}\nGROUP BY ?orderSizeBucket\nORDER BY DESC(?totalRevenue)",
     "text/x-html+tr",
     "https://demo.openlinksw.com/sparql?default-graph-uri=&query=PREFIX+%3A+%3Chttp%3A%2F%2Fwww.databricks.com%2Fbakehouse%23%3E%0ASELECT%0A%3ForderSizeBucket%0A(COUNT(%3Ftransaction)+AS+%3FtransactionCount)%0A(SUM(%3FtotalPrice)+AS+%3FtotalRevenue)%0A(ROUND(AVG(%3FtotalPrice))+AS+%3FavgValue)%0AFROM+%3Chttp%3A%2F%2Fdemo.openlinksw.com%2Fdatabricks-bakehouse-r2rml%23%3E%0AWHERE+%7B%0A++%3Ftransaction+a+%3ATransaction%3B%0A+++%3AtotalPrice+%3FtotalPrice.%0A++BIND(%0A++++IF(%3FtotalPrice+%3C+10%2C+%22Small+(%3C%2410)%22%2C%0A++++IF(%3FtotalPrice+%3C+30%2C+%22Medium+(%2410-%2430)%22%2C%0A++++IF(%3FtotalPrice+%3C+60%2C+%22Large+(%2430-%2460)%22%2C%0A++++%22Enterprise+(%3E%2460)%22)))%0A++++AS+%3ForderSizeBucket)%0A%7D%0AGROUP+BY+%3ForderSizeBucket%0AORDER+BY+DESC(%3FtotalRevenue)&format=text%2Fx-html%2Btr&timeout=0&debug=on&run=+Run+Query+"),
]
for iri, name, desc, query_text, result_fmt, live_url in sparql_queries:
    # ── GRAPH-scoping transform (contract: GRAPH <iri>, not FROM <iri>) ──────
    DAV = 'https://linkeddata.uriburner.com/DAV/demos/daas/databricks-virtuoso-kg-deepseek_v4pro-1.ttl'
    q = query_text
    if f'FROM <{DAV}>' in q and 'GRAPH <' not in q:
        # Remove FROM <DAV> and wrap WHERE body in GRAPH <DAV> { ... }
        import re
        # Replace FROM <DAV> with a blank line to preserve clause separation
        q = re.sub(rf'\n?FROM\s+<{re.escape(DAV)}>\s*', '\n', q)
        q = re.sub(r'\n{3,}', '\n\n', q)  # collapse excessive blank lines
        # Find WHERE { or WHERE\n{ — the opening of the WHERE clause
        m = re.search(r'WHERE\s*\{', q)
        if m:
            idx = m.start()
            open_pos = m.end() - 1  # position of {
            # Find matching closing brace
            depth = 0
            close_idx = None
            for i in range(open_pos, len(q)):
                if q[i] == '{': depth += 1
                elif q[i] == '}': depth -= 1
                if depth == 0:
                    close_idx = i
                    break
            if close_idx:
                body = q[open_pos+1:close_idx]
                body_indented = '\n'.join('  ' + line for line in body.split('\n'))
                q = q[:idx] + f'WHERE {{\n  GRAPH <{DAV}> {{\n{body_indented}\n  }}\n}}' + q[close_idx+1:]
    query_text = q
    # ──────────────────────────────────────────────────────────────────────────
    g.add((iri, RDF.type, SCHEMA.SoftwareSourceCode))
    g.add((iri, SCHEMA.name, Literal(name, lang="en")))
    g.add((iri, SCHEMA.description, Literal(desc, lang="en")))
    g.add((iri, SCHEMA.text, Literal(query_text, lang="en")))
    g.add((iri, SCHEMA.programmingLanguage, Literal("SPARQL")))
    g.add((iri, SCHEMA.codeSampleType, Literal(result_fmt)))
    g.add((iri, SCHEMA.target, demo_endpoint))
    # Potential action for live query execution
    action = NS[f"action{iri.split('#')[-1]}"]
    g.add((action, RDF.type, SCHEMA.SearchAction))
    g.add((action, SCHEMA.target, Literal(live_url)))
    g.add((iri, SCHEMA.potentialAction, action))

# ── SQL Setup Script ──────────────────────────────────────────────────────────
g.add((NS.quickSetupScript, RDF.type, SCHEMA.SoftwareSourceCode))
g.add((NS.quickSetupScript, SCHEMA.name, Literal("quick_setup.sql", lang="en")))
g.add((NS.quickSetupScript, SCHEMA.description, Literal("SQL script that attaches Databricks tables to Virtuoso's local catalog, grants SPARQL access, loads R2RML mappings and ontology, generates quad maps, and configures URL rewrite rules for Linked Data.", lang="en")))
g.add((NS.quickSetupScript, SCHEMA.programmingLanguage, Literal("SQL")))
g.add((NS.quickSetupScript, SCHEMA.codeRepository, repo))

# ── Entity Sections ───────────────────────────────────────────────────────────
# Concepts section
g.add((NS.conceptsSection, RDF.type, SCHEMA.CreativeWork))
g.add((NS.conceptsSection, SCHEMA.name, Literal("Key Concepts", lang="en")))
g.add((NS.conceptsSection, SCHEMA.isPartOf, article))
g.add((article, SCHEMA.hasPart, NS.conceptsSection))
for iri, _, _ in concepts:
    g.add((NS.conceptsSection, SCHEMA.hasPart, iri))

# Capabilities section
g.add((NS.capabilitiesSection, RDF.type, SCHEMA.CreativeWork))
g.add((NS.capabilitiesSection, SCHEMA.name, Literal("Capabilities Enabled", lang="en")))
g.add((NS.capabilitiesSection, SCHEMA.isPartOf, article))
g.add((article, SCHEMA.hasPart, NS.capabilitiesSection))

# Standards section
g.add((NS.standardsSection, RDF.type, SCHEMA.CreativeWork))
g.add((NS.standardsSection, SCHEMA.name, Literal("W3C Standards", lang="en")))
g.add((NS.standardsSection, SCHEMA.isPartOf, article))
g.add((article, SCHEMA.hasPart, NS.standardsSection))

# Software section
g.add((NS.softwareSection, RDF.type, SCHEMA.CreativeWork))
g.add((NS.softwareSection, SCHEMA.name, Literal("Software Stack", lang="en")))
g.add((NS.softwareSection, SCHEMA.isPartOf, article))
g.add((article, SCHEMA.hasPart, NS.softwareSection))

# Dataset section
g.add((NS.datasetSection, RDF.type, SCHEMA.CreativeWork))
g.add((NS.datasetSection, SCHEMA.name, Literal("Bakehouse Sample Dataset", lang="en")))
g.add((NS.datasetSection, SCHEMA.isPartOf, article))
g.add((article, SCHEMA.hasPart, NS.datasetSection))

# ── FAQ ────────────────────────────────────────────────────────────────────────
faq = NS.faqSection
g.add((faq, RDF.type, SCHEMA.FAQPage))
g.add((faq, SCHEMA.name, Literal("Databricks-Virtuoso Virtual Knowledge Graph FAQ", lang="en")))
g.add((faq, SCHEMA.isPartOf, article))
g.add((article, SCHEMA.hasPart, faq))

faq_items = [
    (NS.q1, NS.a1,
     "What is a Virtual Knowledge Graph?",
     "A Virtual Knowledge Graph (VKG) is a semantic layer constructed over existing relational data without physical data movement. It uses virtual database attachment (ODBC/JDBC) to connect to source systems, R2RML mappings to declare how tables and columns map to RDF classes and properties, and SPARQL-to-SQL query translation to execute graph queries against the live relational data at query time. The data stays in place; the semantics are layered on top."),
    (NS.q2, NS.a2,
     "Why use Virtuoso with Databricks instead of Databricks' built-in graph features?",
     "Databricks provides graph capabilities within its platform, but Virtuoso adds: (1) standards-based interoperability via W3C RDF/SPARQL/R2RML — no vendor lock-in; (2) Linked Data entity URIs enabling cross-system entity navigation; (3) federated SPARQL across multiple data sources; (4) AI Agent-friendly machine-readable RDF with content negotiation; and (5) a loosely coupled architecture where the knowledge graph is an overlay, not yet another silo."),
    (NS.q3, NS.a3,
     "Does data get copied from Databricks to Virtuoso?",
     "No. The virtual knowledge graph approach achieves zero data movement. Databricks tables are attached via ODBC as virtual references — they appear in Virtuoso's local catalog but no data is copied. SPARQL queries are translated to SQL at query time and executed remotely against the live Databricks SQL warehouse. This means the knowledge graph always reflects current data without ETL pipelines or stale copies."),
    (NS.q4, NS.a4,
     "What is R2RML and why is it important?",
     "R2RML (RDB to RDF Mapping Language) is a W3C recommendation that defines how relational database tables, columns, and foreign keys map to RDF classes, properties, and relationships. It provides a declarative, standards-based bridge between the SQL world and the semantic graph world — no custom code needed. The mapping is a Turtle file that can be version-controlled, reviewed, and reused across projects."),
    (NS.q5, NS.a5,
     "How do AI agents consume this knowledge graph?",
     "AI agents consume the virtual knowledge graph through three standard interfaces: (1) SPARQL endpoint — structured graph queries returning typed results with entity IRIs; (2) Linked Data entity URIs — dereferenceable HTTP URIs that return RDF (Turtle, JSON-LD, RDF/XML) when requested with the appropriate Accept header; (3) HTML entity descriptions — human-readable pages with navigable hyperlinks for agentic browsing. No custom API, SDK, or platform-specific integration is required — any standards-compliant SPARQL client or HTTP agent can interact with the graph."),
    (NS.q6, NS.a6,
     "What are Quad Maps in Virtuoso?",
     "Quad Maps are Virtuoso's internal representation of R2RML mappings — they define how SPARQL graph patterns translate to SQL queries against virtual tables. The R2RML_MAKE_QM_FROM_G function converts declarative R2RML Turtle mappings into optimized Quad Maps that Virtuoso's SPARQL engine uses at query time. This is what makes SPARQL queries executable against remote relational tables without data movement."),
    (NS.q7, NS.a7,
     "What is content negotiation and why does it matter for AI agents?",
     "Content negotiation is an HTTP mechanism where the server inspects the client's Accept header to determine the response format. For the bakehouse knowledge graph: browsers requesting text/html receive a human-readable HTML description page with navigable links; AI agents and RDF clients requesting application/ld+json or text/turtle receive machine-readable RDF. This single-URI, multi-format approach means the same entity identifier works for both human exploration and automated agent consumption — a cornerstone of Linked Data and the Semantic Web."),
    (NS.q8, NS.a8,
     "Is this approach suitable for real-time or high-frequency workloads?",
     "The virtual knowledge graph approach using ODBC attachment is best suited for batch reasoning, GraphRAG over reference data, or exploratory graph analytics. For millisecond-latency graph traversals or high-frequency transactional writes, a native graph store may be more appropriate. However, for the majority of enterprise AI agent use cases — where agents need to discover entity relationships, traverse connections, and retrieve structured context — the performance characteristics are more than adequate."),
    (NS.q9, NS.a9,
     "What Databricks components are required?",
     "You need: (1) a Databricks SQL warehouse (Serverless, Pro, or Classic) to provide the ODBC endpoint; (2) the Databricks ODBC Driver installed on the Virtuoso host; (3) a Personal Access Token for authentication; and (4) the workspace Host and HTTP Path for the SQL warehouse. The public samples.bakehouse dataset provides the example tables — your own Databricks catalogs and schemas work the same way."),
    (NS.q10, NS.a10,
     "How does this compare to traditional ETL-based knowledge graph construction?",
     "Traditional ETL-based approaches: extract data from source, transform to RDF, load into a triplestore — creating a copy that must be kept in sync. The virtual approach: no extraction, no transformation pipeline, no load step, no stale copies. R2RML mappings define the semantic model declaratively; SPARQL queries execute against live data. Changes in Databricks tables are immediately visible in SPARQL results. The trade-off is query latency versus data freshness — the virtual approach prioritizes freshness and simplicity over raw graph traversal speed."),
    (NS.q11, NS.a11,
     "Can I use this approach with data sources other than Databricks?",
     "Yes. Virtuoso's Virtual Database supports any ODBC or JDBC data source — PostgreSQL, MySQL, Oracle, SQL Server, Snowflake, BigQuery, and many others. The same pattern applies: attach tables via ODBC, define R2RML mappings, load the ontology, generate quad maps, and query via SPARQL. The knowledge graph becomes a unified semantic layer spanning multiple heterogeneous data platforms."),
    (NS.q12, NS.a12,
     "What skills or expertise are needed to implement this?",
     "SQL knowledge for table attachment and testing; basic understanding of RDF and SPARQL for query writing; familiarity with R2RML for mapping design (the Turtle syntax is straightforward for anyone comfortable with data modelling); and Virtuoso administration basics (Conductor UI or isql command-line). The companion GitHub repository provides templates and working examples — most practitioners can have a working virtual knowledge graph running within an hour."),
]
for q_iri, a_iri, q_text, a_text in faq_items:
    g.add((q_iri, RDF.type, SCHEMA.Question))
    g.add((q_iri, SCHEMA.name, Literal(q_text, lang="en")))
    g.add((q_iri, SCHEMA.text, Literal(q_text, lang="en")))
    g.add((q_iri, SCHEMA.isPartOf, faq))
    g.add((faq, SCHEMA.mainEntity, q_iri))

    g.add((a_iri, RDF.type, SCHEMA.Answer))
    g.add((a_iri, SCHEMA.name, Literal(f"Answer: {q_text[:60]}...", lang="en")))
    g.add((a_iri, SCHEMA.text, Literal(a_text, lang="en")))
    g.add((q_iri, SCHEMA.acceptedAnswer, a_iri))

# ── Glossary ──────────────────────────────────────────────────────────────────
glossary = NS.glossarySection
g.add((glossary, RDF.type, SCHEMA.DefinedTermSet))
g.add((glossary, SKOS.type, SKOS.ConceptScheme))
g.add((glossary, SCHEMA.name, Literal("Databricks-Virtuoso Knowledge Graph Glossary", lang="en")))
g.add((glossary, SCHEMA.isPartOf, article))
g.add((article, SCHEMA.hasPart, glossary))

glossary_terms = [
    (NS.termVirtualKnowledgeGraph, "Virtual Knowledge Graph (VKG)",
     "A knowledge graph constructed over existing relational data without physical data movement — using virtual database attachment to expose tables, R2RML to define semantic mappings, and SPARQL for graph querying."),
    (NS.termR2RML, "R2RML (RDB to RDF Mapping Language)",
     "A W3C recommendation that declaratively defines how relational database tables, columns, primary keys, and foreign keys map to RDF classes, properties, and object relationships."),
    (NS.termQuadMap, "Quad Map",
     "Virtuoso's internal compiled representation of R2RML mapping rules — the SPARQL engine uses quad maps at query time to translate SPARQL graph patterns into SQL queries against virtual tables."),
    (NS.termVirtualDatabase, "Virtual Database (VDB)",
     "Virtuoso's capability to attach remote tables from ODBC/JDBC data sources — tables appear in the local catalog as virtual references without copying data."),
    (NS.termSPARQL, "SPARQL",
     "SPARQL Protocol and RDF Query Language — the W3C standard query language for RDF graphs. In the virtual knowledge graph, SPARQL queries are translated to SQL and executed against the live Databricks warehouse."),
    (NS.termLinkedData, "Linked Data",
     "A method of publishing structured data on the web using HTTP URIs, RDF, and content negotiation — enabling entities to be interlinked across systems and consumed by both humans and machines."),
    (NS.termContentNegotiation, "Content Negotiation",
     "An HTTP mechanism where a server returns different representations of the same resource based on the client's Accept header — HTML for browsers, RDF for semantic agents."),
    (NS.termOntology, "Ontology",
     "A formal vocabulary defining classes, properties, and relationships within a domain. The bakehouse ontology defines Transaction, Franchise, Customer classes and franchise, totalPrice, city properties."),
    (NS.termODBC, "ODBC (Open Database Connectivity)",
     "A standard API for accessing database management systems — used by Virtuoso to connect to Databricks SQL warehouses for virtual table attachment."),
    (NS.termAIKGAgent, "AI Agent-Friendly Knowledge Graph",
     "A knowledge graph designed for AI agent consumption — featuring dereferenceable entity URIs, machine-readable RDF, SPARQL endpoints, and navigable entity relationships without custom API integration."),
    (NS.termEntityURI, "Entity URI",
     "A globally unique, dereferenceable HTTP identifier for a knowledge graph entity (e.g., http://demo.openlinksw.com/databricks/bakehouse/franchise-3000046#this). When dereferenced, returns either human-readable HTML or machine-readable RDF depending on the client."),
    (NS.termSemanticWeb, "Semantic Web",
     "An extension of the World Wide Web where data is given well-defined meaning through standards like RDF, SPARQL, and OWL — enabling machines and AI agents to reason about interconnected data across system boundaries."),
]
for iri, name, definition in glossary_terms:
    g.add((iri, RDF.type, SCHEMA.DefinedTerm))
    g.add((iri, SCHEMA.name, Literal(name, lang="en")))
    g.add((iri, SCHEMA.description, Literal(definition, lang="en")))
    g.add((glossary, SCHEMA.hasDefinedTerm, iri))

# ── relatedLink ───────────────────────────────────────────────────────────────
related_links = [
    ("https://github.com/danielhmills/databricks-sample-kg", "Companion GitHub Repository"),
    ("https://github.com/danielhmills/databricks-sample-kg/blob/main/README.md", "Full README"),
    ("https://github.com/danielhmills/databricks-sample-kg/blob/main/bakehouse/r2rml.ttl", "R2RML Mappings (Turtle)"),
    ("https://github.com/danielhmills/databricks-sample-kg/blob/main/bakehouse/ontology.ttl", "Bakehouse Ontology (Turtle)"),
    ("https://github.com/danielhmills/sparqlworks/", "SPARQLWorks Visualizer"),
    ("https://www.databricks.com/spark/odbc-driver-download", "Databricks ODBC Driver Download"),
    ("https://docs.databricks.com/integrations/bi/jdbc-odbc-bi.html", "Databricks ODBC/JDBC Documentation"),
    ("http://docs.openlinksw.com/virtuoso/rdb2rdfviewsrdb2rdf/", "Virtuoso R2RML Documentation"),
    ("https://virtuoso.openlinksw.com/", "OpenLink Virtuoso Homepage"),
    ("https://linkeddata.uriburner.com/sparql", "URIBurner SPARQL Endpoint"),
    ("http://demo.openlinksw.com/sparql", "OpenLink Demo SPARQL Endpoint"),
    ("https://www.w3.org/TR/r2rml/", "W3C R2RML Specification"),
    ("https://www.w3.org/TR/sparql11-query/", "W3C SPARQL 1.1 Query Language"),
    ("https://www.w3.org/RDF/", "W3C RDF Standard"),
]
for url, label in related_links:
    g.add((article, SCHEMA.relatedLink, Literal(url)))
    link_entity = NS[f"link{url.split('/')[-1].replace('.','_')[:40]}"]
    g.add((link_entity, RDF.type, SCHEMA.WebSite))
    g.add((link_entity, SCHEMA.name, Literal(label, lang="en")))
    g.add((link_entity, SCHEMA.url, Literal(url)))
    g.add((article, SCHEMA.relatedLink, link_entity))

# ── Serialize ─────────────────────────────────────────────────────────────────
output_dir = "kg-output/databricks-virtuoso-kg"
slug = "databricks-virtuoso-kg-deepseek_v4pro-1"

# Turtle
ttl_path = f"{output_dir}/{slug}.ttl"
g.serialize(destination=ttl_path, format="turtle")
print(f"✓ Turtle written: {ttl_path}")

# JSON-LD
jsonld_path = f"{output_dir}/{slug}.jsonld"
g.serialize(destination=jsonld_path, format="json-ld", indent=2)
print(f"✓ JSON-LD written: {jsonld_path}")

# Stats
print(f"\nTriples: {len(g)}")
print(f"FAQ: {len(faq_items)} Q&A pairs")
print(f"Glossary: {len(glossary_terms)} terms")
print(f"HowTo: {len(steps)} steps")
print(f"SPARQL queries: {len(sparql_queries)}")
print(f"Concepts: {len(concepts)}")
print(f"Capabilities: {len(capabilities)}")
print(f"Standards: {len(standards)}")
