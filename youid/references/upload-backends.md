# YouID Upload Backend Reference

This reference documents how to upload generated identity documents to various storage backends using curl. Each backend supports PUT requests for file upload.

## Prerequisites

- All generated files exist in the output directory
- Destination URL is known (with write access)
- Authentication credentials are available (password, token, or certificate)

## Backend: OpenLink WebDAV

The primary backend for YouID identity documents. Uses HTTP Basic authentication over HTTPS.

### Upload a Single File

```bash
curl -T "{local_file}" \
  -H "Content-Type: {mime_type}" \
  -u "{username}:{password}" \
  "{base_url}/{filename}"
```

### Upload All Identity Files (Batch)

```bash
BASE_URL="https://id.myopenlink.net/DAV/home/{username}/youid/"
AUTH="{username}:{password}"

# RDF documents
curl -T "profile.ttl"        -H "Content-Type: text/turtle"                -u "$AUTH" "${BASE_URL}profile.ttl"
curl -T "profile.jsonld"     -H "Content-Type: application/ld+json"        -u "$AUTH" "${BASE_URL}profile.jsonld"
curl -T "profile_rdfa.html"  -H "Content-Type: text/html"                  -u "$AUTH" "${BASE_URL}profile_rdfa.html"
curl -T "certificate.ttl"    -H "Content-Type: text/turtle"                -u "$AUTH" "${BASE_URL}certificate.ttl"
curl -T "certificate.jsonld" -H "Content-Type: application/ld+json"        -u "$AUTH" "${BASE_URL}certificate.jsonld"
curl -T "certificate.rdfa.html" -H "Content-Type: text/html"               -u "$AUTH" "${BASE_URL}certificate.rdfa.html"
curl -T "public_key.ttl"     -H "Content-Type: text/turtle"                -u "$AUTH" "${BASE_URL}public_key.ttl"
curl -T "public_key.jsonld"  -H "Content-Type: application/ld+json"        -u "$AUTH" "${BASE_URL}public_key.jsonld"
curl -T "public_key.rdfa.html" -H "Content-Type: text/html"                -u "$AUTH" "${BASE_URL}public_key.rdfa.html"

# Identity card
curl -T "index.html"         -H "Content-Type: text/html"                  -u "$AUTH" "${BASE_URL}index.html"
curl -T "vcard.vcf"          -H "Content-Type: text/vcard"                 -u "$AUTH" "${BASE_URL}vcard.vcf"

# CSS & assets
curl -T "style.css"          -H "Content-Type: text/css"                   -u "$AUTH" "${BASE_URL}style.css"

# Certificate files
curl -T "cert.pem"           -H "Content-Type: application/x-pem-file"     -u "$AUTH" "${BASE_URL}cert.pem"
curl -T "cert.crt"           -H "Content-Type: application/x-x509-ca-cert" -u "$AUTH" "${BASE_URL}cert.crt"
curl -T "cert.p12"           -H "Content-Type: application/x-pkcs12"       -u "$AUTH" "${BASE_URL}cert.p12"
```

### Create Directory (PROPPATCH)

If the target directory does not exist, create it first:

```bash
curl -X PROPPATCH \
  -H "Content-Type: text/xml" \
  -u "$AUTH" \
  -d '<?xml version="1.0" encoding="utf-8"?>
       <D:mkcol xmlns:D="DAV:">
         <D:set>
           <D:prop>
             <D:resourcetype><D:collection/></D:resourcetype>
           </D:prop>
         </D:set>
       </D:mkcol>' \
  "https://id.myopenlink.net/DAV/home/{username}/youid/"
```

### Verify Upload

```bash
curl -I -u "$AUTH" "${BASE_URL}profile.ttl"
# Check HTTP 200 response
```

## Backend: OpenLink LDP

Uses LDP (Linked Data Platform) containers. Files are created as LDP-RS (RDF Source) or LDP-NR (Non-RDF Source).

```bash
# Create an LDP container
curl -X POST \
  -H "Content-Type: text/turtle" \
  -H "Link: <http://www.w3.org/ns/ldp#BasicContainer>; rel=\"type\"" \
  -H "Slug: youid" \
  -u "{username}:{password}" \
  --data-binary @profile.ttl \
  "https://linkeddata.uriburner.com/DAV/LDP/home/{username}/"

# Upload a resource to the container
curl -X PUT \
  -H "Content-Type: text/turtle" \
  -u "{username}:{password}" \
  --data-binary @profile.ttl \
  "https://linkeddata.uriburner.com/DAV/LDP/home/{username}/youid/profile.ttl"
```

## Backend: WebDAV over HTTPS (Generic)

Generic WebDAV for any WebDAV-enabled server.

```bash
curl -T "profile.ttl" \
  -H "Content-Type: text/turtle" \
  -u "{username}:{password}" \
  "https://{webdav-server}/{path}/profile.ttl"
```

## Backend: AWS S3

Requires the `aws` CLI with configured credentials.

```bash
aws s3 cp profile.ttl s3://{bucket}/youid/profile.ttl --content-type "text/turtle"
aws s3 cp profile.jsonld s3://{bucket}/youid/profile.jsonld --content-type "application/ld+json"
aws s3 cp profile_rdfa.html s3://{bucket}/youid/profile_rdfa.html --content-type "text/html"
aws s3 cp index.html s3://{bucket}/youid/index.html --content-type "text/html"
aws s3 cp cert.pem s3://{bucket}/youid/cert.pem --content-type "application/x-pem-file"
```

Set bucket policy to allow public read access for identity card display.

## Backend: Azure Blob Storage

Requires `azcopy` or `curl` with SAS token.

```bash
azcopy copy "profile.ttl" "https://{account}.blob.core.windows.net/{container}/youid/profile.ttl?{sas-token}"
```

Or with curl:

```bash
curl -X PUT \
  -H "x-ms-blob-type: BlockBlob" \
  -H "Content-Type: text/turtle" \
  --data-binary @profile.ttl \
  "https://{account}.blob.core.windows.net/{container}/youid/profile.ttl?{sas-token}"
```

## Backend: Solid POD (WebID-OIDC)

Solid POD uploads require OIDC authentication, which is not available via direct curl. Use the YouID browser extension for Solid POD uploads.

## MIME Type Reference

| File Extension | MIME Type | Notes |
|---------------|-----------|-------|
| `.ttl` | `text/turtle` | Turtle RDF |
| `.jsonld` | `application/ld+json` | JSON-LD |
| `.html` | `text/html` | HTML (RDFa or identity card) |
| `.vcf` | `text/vcard` | vCard |
| `.css` | `text/css` | Stylesheet |
| `.js` | `text/javascript` | JavaScript |
| `.png` | `image/png` | PNG image |
| `.jpg`, `.jpeg` | `image/jpeg` | JPEG image |
| `.pem` | `application/x-pem-file` | PEM certificate |
| `.crt` | `application/x-x509-ca-cert` | DER certificate |
| `.p12` | `application/x-pkcs12` | PKCS#12 bundle |
| `.zip` | `application/zip` | Manual download bundle |
