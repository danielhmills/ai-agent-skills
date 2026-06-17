# YouID WebID Verification SPARQL Queries

These SPARQL queries are used to verify a remote WebID profile document. They come from the YouID browser extension's `utils.js` and are adapted for use with the URIBurner SPASQL endpoint or the local `verify_webid.sh` script.

## Prerequisites

- Fetch the WebID URL first (via `curl` or `python3` with `rdflib`)
- Determine the RDF serialization (Turtle, JSON-LD, RDFa, RDF/XML, or HTML with embedded structured data)
- Parse the content into a local RDF graph or send to URIBurner's SPARQL endpoint

## Q1: Load WebID — Find identity name

Retrieves the primary WebID URI and its display name from the profile document.

```sparql
PREFIX foaf:   <http://xmlns.com/foaf/0.1/>
PREFIX schema: <http://schema.org/>
PREFIX rdfs:   <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:    <http://www.w3.org/2002/07/owl#>
PREFIX cert:   <http://www.w3.org/ns/auth/cert#>
PREFIX oplcert:<http://www.openlinksw.com/schemas/cert#>
PREFIX acl:    <http://www.w3.org/ns/auth/acl#>
PREFIX pim:    <http://www.w3.org/ns/pim/space#>
PREFIX ldp:    <http://www.w3.org/ns/ldp#>
PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>
PREFIX as:     <http://www.w3.org/ns/activitystreams#>
PREFIX vcard:  <http://www.w3.org/2006/vcard/ns#>

SELECT * WHERE
{
  {
    { ?url foaf:primaryTopic ?webid . } UNION
    { ?url schema:mainEntity ?webid . } UNION
    { ?url foaf:primaryTopic ?webid_x . ?webid owl:sameAs ?webid_x . } UNION
    { ?url schema:mainEntity ?webid_x . ?webid owl:sameAs ?webid_x . }
  }
  {
    { ?webid schema:name ?schema_name } UNION
    { ?webid foaf:name ?foaf_name } UNION
    { ?webid rdfs:label ?rdfs_name } UNION
    { ?webid skos:prefLabel ?skos_prefLabel } UNION
    { ?webid skos:altLabel ?skos_altLabel } UNION
    { ?url schema:name ?schema_name } UNION
    { ?url foaf:name ?foaf_name } UNION
    { ?url rdfs:label ?rdfs_name } UNION
    { ?url skos:prefLabel ?skos_prefLabel } UNION
    { ?url skos:altLabel ?skos_altLabel }
  }
}
```

### Usage with URIBurner SPASQL Endpoint

```bash
curl -X POST "https://linkeddata.uriburner.com/sparql" \
  -H "Content-Type: application/sparql-query" \
  -H "Accept: application/sparql-results+json" \
  --data-binary @query.sparql
```

## Q2: WebID Details — Delegates, storage, inbox

Retrieves delegation relationships, storage locations, inbox, outbox, know relations, and email addresses.

```sparql
PREFIX foaf:   <http://xmlns.com/foaf/0.1/>
PREFIX schema: <http://schema.org/>
PREFIX rdfs:   <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:    <http://www.w3.org/2002/07/owl#>
PREFIX cert:   <http://www.w3.org/ns/auth/cert#>
PREFIX oplcert:<http://www.openlinksw.com/schemas/cert#>
PREFIX acl:    <http://www.w3.org/ns/auth/acl#>
PREFIX pim:    <http://www.w3.org/ns/pim/space#>
PREFIX ldp:    <http://www.w3.org/ns/ldp#>
PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>
PREFIX as:     <http://www.w3.org/ns/activitystreams#>
PREFIX vcard:  <http://www.w3.org/2006/vcard/ns#>

SELECT * WHERE
{
  { <{webid}> oplcert:hasIdentityDelegate ?delegate . } UNION
  { <{webid}> oplcert:onBehalfOf ?behalfOf . } UNION
  { <{webid}> acl:delegates ?acl_delegates . } UNION
  { <{webid}> pim:storage ?pim_store . } UNION
  { <{webid}> ldp:inbox ?inbox . } UNION
  { <{webid}> as:outbox ?outbox . } UNION
  { <{webid}> foaf:knows ?knows . } UNION
  { <{webid}> foaf:mbox ?foaf_mbox . } UNION
  { <{webid}> vcard:email ?vcard_email . } UNION
  { <{webid}> schema:email ?schema_email . }
}
```

Replace `{webid}` with the user's WebID URI.

## Q3: Load Public Key — Certificate details

Retrieves public key information (algorithm, modulus, exponent) and certificate details (fingerprints).

```sparql
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs:   <http://www.w3.org/2000/01/rdf-schema#>
PREFIX cert:   <http://www.w3.org/ns/auth/cert#>
PREFIX foaf:   <http://xmlns.com/foaf/0.1/>
PREFIX vcard:  <http://www.w3.org/2006/vcard/ns#>
PREFIX schema: <http://schema.org/>
PREFIX owl:    <http://www.w3.org/2002/07/owl#>
PREFIX oplcert:<http://www.openlinksw.com/schemas/cert#>

SELECT * WHERE
{
  {
    {
      { <{webid}> cert:key ?pubkey . } UNION
      { <{webid}> owl:sameAs ?webid_x . ?webid_x cert:key ?pubkey . }
    }
    ?pubkey a ?alg ;
            cert:modulus ?cert_mod ;
            cert:exponent ?cert_exp .
  }
  OPTIONAL { ?pubkey dcterms:created ?key_cr_dt . }
  OPTIONAL { ?pubkey dcterms:title ?key_cr_title . }
  OPTIONAL { ?pubkey rdfs:label ?key_label . }
  OPTIONAL { ?pubkey owl:sameAs ?fp_uri . }
  OPTIONAL {
    <{webid}> oplcert:hasCertificate ?cert .
    ?cert oplcert:fingerprint ?fp ;
          oplcert:fingerprint-digest ?fp_dg .
    OPTIONAL { ?cert oplcert:serial ?ser . }
    OPTIONAL { ?cert oplcert:notBefore ?nb . }
    OPTIONAL { ?cert oplcert:notAfter ?na . }
    OPTIONAL { ?cert oplcert:subject ?subj . }
    OPTIONAL { ?cert oplcert:issuer ?iss . }
  }
}
```

Replace `{webid}` with the user's WebID URI.

## Verification Script Usage

The `scripts/verify_webid.sh` script automates WebID verification. It:

1. Fetches the WebID URL
2. Parses the content with rdflib
3. Executes these queries against the parsed graph
4. Returns structured JSON with all identity details

### Manual URIBurner SPASQL Query

For quick verification of a hosted WebID profile (e.g., one you just uploaded), use the URIBurner SPASQL endpoint:

```
https://linkeddata.uriburner.com/spasqlqb/?permlink_e={url-encoded-json}
```

With the JSON format:
```json
{
  "v":1,
  "url":"/XMLA",
  "dsn":"DSN=Local_Instance",
  "uid":"",
  "pwd":"",
  "path":null,
  "tab":"exec",
  "idx":null,
  "fkey":null,
  "ref":null,
  "exec":{"sql":"SELECT * WHERE { <WEBID_URL> ?p ?o }"}
}
```

## Expected Verification Results

A successful verification produces:

```
Identity: Jane Doe
WebID: https://example.org/people/jane#me

Public Key:
  Algorithm: cert:RSAPublicKey
  Modulus: 00A3B2C1...
  Exponent: 65537

Certificate:
  Fingerprint: A1B2C3D4... (SHA-1)
  Fingerprint: E5F6A7B8... (SHA-256)
  Created: 2026-06-09T00:00:00Z
  Not Before: 2026-06-09T00:00:00Z
  Not After: 2036-06-06T00:00:00Z

Delegates: (none)
Storage: https://id.myopenlink.net/DAV/home/jane/
```
