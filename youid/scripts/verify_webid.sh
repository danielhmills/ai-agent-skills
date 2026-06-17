#!/bin/bash
#
# YouID WebID Verifier
# Fetches a WebID profile document and verifies its identity claims
# using SPARQL queries against the parsed RDF graph.
#
# Usage:
#   ./verify_webid.sh <webid_url>
#
# Requirements: python3, curl, rdflib
#
set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Usage: $0 <webid_url>"
    exit 1
fi

WEBID="$1"
OUT_DIR="${2:-./youid-verify-output}"
mkdir -p "$OUT_DIR"

echo "Fetching WebID: $WEBID"
echo ""

# Fetch the WebID profile
CURL_OUT="$OUT_DIR/response"
HTTP_CODE=$(curl -s -o "$CURL_OUT" -w "%{http_code}" -L "$WEBID")

echo "HTTP Status: $HTTP_CODE"
if [ "$HTTP_CODE" -ne 200 ]; then
    echo "Error: Failed to fetch WebID profile (HTTP $HTTP_CODE)"
    exit 1
fi

# Detect content type
CONTENT_TYPE=$(curl -s -I -L "$WEBID" | grep -i content-type | head -1 | sed 's/.*: //' | tr -d '\r\n')
echo "Content-Type: $CONTENT_TYPE"
echo ""

# Verify using Python/rdflib
python3 << 'PYEOF'
import json, sys, os

webid = os.environ.get('WEBID', '')
curl_out = os.environ.get('CURL_OUT', '')
out_dir = os.environ.get('OUT_DIR', '')

try:
    import rdflib
except ImportError:
    print("rdflib not available. Install with: pip3 install rdflib")
    sys.exit(1)

from rdflib import Graph, URIRef

g = Graph()
try:
    with open(curl_out, 'rb') as f:
        content = f.read()
    # Try to parse as RDF (various formats)
    formats_to_try = ['turtle', 'xml', 'json-ld', 'n3', 'n-triples', 'rdfa']
    parsed = False
    for fmt in formats_to_try:
        try:
            g.parse(data=content, format=fmt)
            parsed = True
            break
        except:
            pass
    if not parsed:
        # Try as HTML with RDFa/embedded triples
        try:
            g.parse(data=content, format='rdfa')
            parsed = True
        except:
            pass
    if not parsed:
        print(f"Could not parse content as any known RDF format")
        sys.exit(1)
except Exception as e:
    print(f"Parse error: {e}")
    sys.exit(1)

print(f"Parsed {len(g)} triples from {webid}")
print("")

# SPARQL queries adapted from utils.js
QUERY_LOAD = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX schema: <http://schema.org/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX cert: <http://www.w3.org/ns/auth/cert#>
PREFIX oplcert: <http://www.openlinksw.com/schemas/cert#>

SELECT ?webid ?name ?type WHERE
{
  {
    { ?url foaf:primaryTopic ?webid . } UNION
    { ?url schema:mainEntity ?webid . }
  }
  ?webid ?nameProp ?name .
  VALUES ?nameProp { foaf:name schema:name rdfs:label }
  OPTIONAL { ?webid a ?type }
}
"""

QUERY_DETAILS = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX schema: <http://schema.org/>
PREFIX cert: <http://www.w3.org/ns/auth/cert#>
PREFIX oplcert: <http://www.openlinksw.com/schemas/cert#>
PREFIX acl: <http://www.w3.org/ns/auth/acl#>
PREFIX pim: <http://www.w3.org/ns/pim/space#>
PREFIX ldp: <http://www.w3.org/ns/ldp#>
PREFIX as: <http://www.w3.org/ns/activitystreams#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?property ?value WHERE
{
  { <{webid}> ?property ?value }
  FILTER(?property IN (
    foaf:mbox, schema:email, foaf:knows, pim:storage,
    ldp:inbox, as:outbox, acl:delegates,
    oplcert:hasIdentityDelegate, oplcert:onBehalfOf,
    owl:sameAs, schema:sameAs, cert:key,
    oplcert:hasCertificate
  ))
}
"""

QUERY_PUBKEY = """
PREFIX cert: <http://www.w3.org/ns/auth/cert#>
PREFIX oplcert: <http://www.openlinksw.com/schemas/cert#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?pubkey ?modulus ?exponent ?alg ?label WHERE
{
  <{webid}> cert:key ?pubkey .
  ?pubkey a ?alg ;
          cert:modulus ?modulus ;
          cert:exponent ?exponent .
  OPTIONAL { ?pubkey rdfs:label ?label }
}
"""


def safe_val(v):
    if v is None:
        return ""
    return str(v)

# Try each URI in the graph as the WebID
webid_uri = URIRef(webid)
webids_found = []

# Check if webid_uri itself has triples
if len(list(g.triples((webid_uri, None, None)))) > 0:
    webids_found.append(webid_uri)

# Try finding through the document
for s, p, o in g:
    if p in [rdflib.FOAF.primaryTopic, rdflib.RDFS.label, rdflib.FOAF.name]:
        if p == rdflib.FOAF.primaryTopic:
            if o not in webids_found:
                webids_found.append(o)

for curr_webid in webids_found:
    w_str = str(curr_webid)
    print(f"=== Identity: {w_str} ===")
    print("")

    # Get name
    for s, p, o in g.triples((curr_webid, None, None)):
        if p in [rdflib.FOAF.name, rdflib.SDO.name, rdflib.RDFS.label]:
            print(f"  Name: {o}")
    print("")

    # Public keys
    has_keys = False
    for s, p, o in g.triples((curr_webid, rdflib.URIRef('http://www.w3.org/ns/auth/cert#key'), None)):
        has_keys = True
        key_uri = str(o)
        print(f"  Public Key: {key_uri}")
        for ks, kp, ko in g.triples((URIRef(key_uri), None, None)):
            prop = str(kp).split('/')[-1].split('#')[-1]
            val = str(ko)[:80]
            if 'modulus' in prop.lower() or 'exponent' in prop.lower():
                print(f"    {prop}: {val[:40]}...")
            elif 'label' in prop.lower():
                print(f"    Label: {val}")
        print("")

    # Certificates
    for s, p, o in g.triples((curr_webid, rdflib.URIRef('http://www.openlinksw.com/schemas/cert#hasCertificate'), None)):
        cert_uri = str(o)
        print(f"  Certificate: {cert_uri}")
        for cs, cp, co in g.triples((URIRef(cert_uri), None, None)):
            prop = str(cp).split('/')[-1].split('#')[-1]
            val = str(co)[:80]
            if prop in ['fingerprint', 'serial', 'subject', 'notBefore', 'notAfter']:
                print(f"    {prop}: {val}")
            elif 'fingerprint' in prop:
                print(f"    {prop}: {val[:40]}...")
        print("")

    # Delegates
    for s, p, o in g.triples((curr_webid, rdflib.URIRef('http://www.openlinksw.com/schemas/cert#hasIdentityDelegate'), None)):
        print(f"  Delegate: {o}")
    for s, p, o in g.triples((curr_webid, rdflib.URIRef('http://www.openlinksw.com/schemas/cert#onBehalfOf'), None)):
        print(f"  On-Behalf-Of: {o}")

    # Storage, inbox
    for s, p, o in g.triples((curr_webid, rdflib.URIRef('http://www.w3.org/ns/pim/space#storage'), None)):
        print(f"  Storage: {o}")
    for s, p, o in g.triples((curr_webid, rdflib.URIRef('http://www.w3.org/ns/ldp#inbox'), None)):
        print(f"  Inbox: {o}")

    # sameAs
    same_as_count = 0
    for s, p, o in g.triples((curr_webid, rdflib.OWL.sameAs, None)):
        if same_as_count == 0:
            print("  owl:sameAs:")
        same_as_count += 1
        print(f"    {o}")
    if same_as_count == 0:
        for s, p, o in g.triples((curr_webid, rdflib.SDO.sameAs, None)):
            if same_as_count == 0:
                print("  schema:sameAs:")
            same_as_count += 1
            print(f"    {o}")

    print("")

if not webids_found:
    print("No primary WebID identity found in the profile.")
    print("Raw triples in the document:")
    for s, p, o in g:
        print(f"  {s} {p} {o}")

print("")
print(f"Total triples parsed: {len(g)}")
print("Verification complete.")
PYEOF
