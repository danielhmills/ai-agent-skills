#!/bin/bash
#
# YouID Delegation Generator
# Generates:
#   1. SPARQL UPDATE patch for delegator's profile
#   2. declarativeNetRequest rule JSON for Chrome extension header injection
#   3. Deployment summary with curl examples
#
# Usage:
#   ./generate_delegation.sh -d <delegator-webid> -e <delegate-webid> -r <role> [-o <output-dir>]
#
# Role: identify | inform | consult | authority
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
YOUID_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

DELEGATOR=""
DELEGATE=""
ROLE=""
OUT_DIR="$(pwd)/delegation-output"

while getopts "d:e:r:o:h" opt; do
    case $opt in
        d) DELEGATOR="$OPTARG" ;;
        e) DELEGATE="$OPTARG" ;;
        r) ROLE="$OPTARG" ;;
        o) OUT_DIR="$OPTARG" ;;
        h) echo "Usage: $0 -d <delegator-webid> -e <delegate-webid> -r <role> [-o <output-dir>]"
           echo ""
           echo "Required:"
           echo "  -d  Delegator WebID/NetID (the entity granting authority)"
           echo "  -e  Delegate WebID/NetID (the entity acting on-behalf-of)"
           echo "  -r  Delegation role: identify | inform | consult | authority"
           echo ""
           echo "Optional:"
           echo "  -o  Output directory (default: ./delegation-output)"
           echo ""
           echo "Role definitions:"
           echo "  identify   - Delegate may identify as the delegator for identification purposes"
           echo "  inform     - Delegate may be informed on behalf of the delegator"
           echo "  consult    - Delegate may be consulted on behalf of the delegator"
           echo "  authority  - Delegate has full authority to act on behalf of the delegator"
           exit 0 ;;
        *) echo "Unknown option -$opt"; exit 1 ;;
    esac
done

if [ -z "$DELEGATOR" ] || [ -z "$DELEGATE" ] || [ -z "$ROLE" ]; then
    echo "Error: -d (delegator), -e (delegate), and -r (role) are required"
    echo "Usage: $0 -d <delegator> -e <delegate> -r <role>"
    exit 1
fi

case "$ROLE" in
    identify|inform|consult|authority) ;;
    *) echo "Error: role must be one of: identify, inform, consult, authority"; exit 1 ;;
esac

mkdir -p "$OUT_DIR"
ROLE_UPPER="$(echo "$ROLE" | tr '[:lower:]' '[:upper:]')"

echo "=== Generating Delegation Bundle ==="
echo "  Delegator: $DELEGATOR"
echo "  Delegate:  $DELEGATE"
echo "  Role:      $ROLE"

# Step 1: Generate SPARQL UPDATE patch
echo "=== Step 1: SPARQL UPDATE Patch ==="
SPARQL_FILE="$OUT_DIR/delegation.sparql"

cat > "$SPARQL_FILE" <<SPARQL
# YouID Delegation — SPARQL UPDATE Patch
# Generated: $(date -u)
# Delegator: <${DELEGATOR}>
# Delegate:  <${DELEGATE}>
# Role:      ${ROLE}
#
# Deploy: curl -X POST <sparql-endpoint> \\
#             -H 'Content-Type: application/sparql-update' \\
#             -u <username>:<password> \\
#             --data-binary @'${SPARQL_FILE}'

PREFIX foaf:     <http://xmlns.com/foaf/0.1/>
PREFIX oplcert:  <http://www.openlinksw.com/schemas/cert#>
PREFIX schema:   <http://schema.org/>
PREFIX xsd:      <http://www.w3.org/2001/XMLSchema#>

INSERT DATA {
  # Delegation role: ${ROLE}
  <${DELEGATOR}>
      a foaf:Agent ;
      a schema:Person ;
      schema:additionalType "Delegator" ;
      schema:description "Delegates ${ROLE_UPPER} role to <${DELEGATE}>"^^xsd:string ;
      oplcert:hasIdentityDelegate <${DELEGATE}> .

  # Delegate acts on behalf of delegator
  <${DELEGATE}>
      a foaf:Agent ;
      schema:additionalType "Delegate" ;
      schema:description "Assigned ${ROLE_UPPER} role for <${DELEGATOR}>"^^xsd:string ;
      oplcert:onBehalfOf <${DELEGATOR}> .
}
SPARQL
echo "  → ${SPARQL_FILE}"

# Step 2: Generate declarativeNetRequest rule JSON
echo "=== Step 2: declarativeNetRequest Rule ==="
RULE_FILE="$OUT_DIR/delegation-rule.json"

cat > "$RULE_FILE" <<JSON
{
  "id": 1,
  "priority": 1,
  "condition": {
    "urlFilter": "*",
    "resourceTypes": ["xmlhttprequest"]
  },
  "action": {
    "type": "modifyHeaders",
    "requestHeaders": [
      {
        "header": "On-Behalf-Of",
        "operation": "set",
        "value": "${DELEGATE}"
      }
    ]
  }
}
JSON
echo "  → ${RULE_FILE}"

# Step 3: Generate deployment summary
echo "=== Step 3: Deployment Summary ==="
SUMMARY_FILE="$OUT_DIR/delegation-summary.json"

cat > "$SUMMARY_FILE" <<JSON
{
  "delegator": "${DELEGATOR}",
  "delegate": "${DELEGATE}",
  "role": "${ROLE}",
  "generated": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "files": {
    "sparql_patch": "delegation.sparql",
    "dnr_rule": "delegation-rule.json"
  },
  "deployment": {
    "method": "SPARQL UPDATE via HTTP POST",
    "content_type": "application/sparql-update",
    "auth_options": [
      "Basic (username:password)",
      "Digest",
      "Bearer token",
      "WebID-OIDC DPoP"
    ],
    "curl_example": "curl -X POST <endpoint> -H 'Content-Type: application/sparql-update' -u <user>:<pass> --data-binary @delegation.sparql",
    "endpoint_note": "Use the SPARQL endpoint of the delegator's identity provider (e.g., https://linkeddata.uriburner.com/SPARQL)"
  }
}
JSON
echo "  → ${SUMMARY_FILE}"

echo ""
echo "=== Delegation Bundle Generated ==="
echo "  Output: ${OUT_DIR}/"
ls -la "$OUT_DIR/"
echo ""
echo "=== Next Steps ==="
echo "  1. Review delegation.sparql — verify the triples are correct"
echo "  2. Deploy the SPARQL UPDATE to the delegator's profile store:"
echo "     curl -X POST <sparql-endpoint> \\"
echo "       -H 'Content-Type: application/sparql-update' \\"
echo "       -u <username>:<password> \\"
echo "       --data-binary @'${SPARQL_FILE}'"
echo "  3. Install delegation-rule.json in the delegate's browser"
echo "     (Chrome extension → declarativeNetRequest rules)"
echo "  4. Verify: query the delegator's WebID for oplcert:hasIdentityDelegate triples"
