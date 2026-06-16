#!/bin/bash
#
# YouID Fingerprint Computer
# Extracts key fingerprints from a PEM certificate and outputs
# NI (Named Information) URI, DI (Document Identifier) URI,
# and SHA-256 / SHA-1 fingerprints in multiple formats.
#
# Usage:
#   ./compute_fingerprints.sh <certificate.pem>
#
# Output: JSON to stdout with all fingerprints
#
set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Usage: $0 <certificate.pem>"
    exit 1
fi

CERT="$1"

if [ ! -f "$CERT" ]; then
    echo "Error: Certificate file not found: $CERT"
    exit 1
fi

# Extract DER-encoded certificate
DER=$(openssl x509 -in "$CERT" -outform DER 2>/dev/null)

# Compute SHA-256 fingerprint (hex, colon-separated)
SHA256_HEX=$(echo "$DER" | openssl dgst -sha256 -hex | sed 's/.*= //')
SHA256_COLON=$(echo "$SHA256_HEX" | sed 's/\(..\)/\1:/g; s/:$//')

# Compute SHA-1 fingerprint (hex, colon-separated)
SHA1_HEX=$(echo "$DER" | openssl dgst -sha1 -hex | sed 's/.*= //')
SHA1_COLON=$(echo "$SHA1_HEX" | sed 's/\(..\)/\1:/g; s/:$//')

# Compute SHA-256 raw bytes for NI/DI URIs
SHA256_RAW=$(echo "$DER" | openssl dgst -sha256 -binary)

# NI URI: base64url of SHA-256 hash
NI_B64=$(echo "$SHA256_RAW" | openssl base64 -e | tr -d '\n' | tr '+/' '-_' | sed 's/=//g')
NI_URI="ni:///sha-256;${NI_B64}"

# DI URI: hex lowercase of SHA-256
DI_HEX=$(echo "$SHA256_RAW" | xxd -p -c 256 | tr -d '\n' | tr '[:upper:]' '[:lower:]')
DI_URI="urn:di:sha-256;${DI_HEX}"

# Get certificate validity dates
NOT_BEFORE=$(openssl x509 -in "$CERT" -noout -startdate -dateopt iso_8601 2>/dev/null | sed 's/notBefore=//' || openssl x509 -in "$CERT" -noout -startdate 2>/dev/null | sed 's/notBefore=//')
NOT_AFTER=$(openssl x509 -in "$CERT" -noout -enddate -dateopt iso_8601 2>/dev/null | sed 's/notEndDate=//' || openssl x509 -in "$CERT" -noout -enddate 2>/dev/null | sed 's/notAfter=//')

# Get subject
SUBJECT=$(openssl x509 -in "$CERT" -noout -subject 2>/dev/null | sed 's/subject=//')

# Get serial
SERIAL=$(openssl x509 -in "$CERT" -noout -serial 2>/dev/null | sed 's/serial=//')

# Get issuer
ISSUER=$(openssl x509 -in "$CERT" -noout -issuer 2>/dev/null | sed 's/issuer=//')

# Output JSON
python3 -c "
import json, sys

result = {
    'sha256_fingerprint': '$SHA256_COLON',
    'sha256_hex': '$SHA256_HEX',
    'sha1_fingerprint': '$SHA1_COLON',
    'sha1_hex': '$SHA1_HEX',
    'ni_uri': '$NI_URI',
    'di_uri': '$DI_URI',
    'subject': '$SUBJECT',
    'issuer': '$ISSUER',
    'serial': '$SERIAL',
    'not_before': '$NOT_BEFORE',
    'not_after': '$NOT_AFTER',
}
json.dump(result, sys.stdout, indent=2)
print()
"
