# Origin CA Certificates | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/origin_ca_certificates

[API Reference]
# Origin CA Certificates

##### [List Certificates]
GET/certificates
##### [Get Certificate]
GET/certificates/{certificate_id}
##### [Create Certificate]
POST/certificates
##### [Revoke Certificate]
DELETE/certificates/{certificate_id}
##### ModelsExpand Collapse
OriginCACertificate  { csr, hostnames, request_type, 4 more } csr: string
The Certificate Signing Request (CSR). Must be newline-encoded.
[]hostnames: array of string
Array of hostnames or wildcard names bound to the certificate.
Hostnames must be fully qualified domain names (FQDNs) belonging to zones on your account (e.g., `example.com` or `sub.example.com`). Wildcards are supported only as a `*.` prefix for a single level (e.g., `*.example.com`). Double wildcards (`*.*.example.com`) and interior wildcards (`foo.*.example.com`) are not allowed. The wildcard suffix must be a multi-label domain (`*.example.com` is valid, but `*.com` is not). Unicode/IDN hostnames are accepted and automatically converted to punycode.
[]request_type: [CertificateRequestType]
Signature type desired on certificate (“origin-rsa” (rsa), “origin-ecc” (ecdsa), or “keyless-certificate” (for Keyless SSL servers).
[]requested_validity: [RequestValidity]
The number of days for which the certificate should be valid.
[]id: optional string
Identifier.
maxLength32[]certificate: optional string
The Origin CA certificate. Will be newline-encoded.
[]expires_on: optional string
When the certificate will expire.
[][]OriginCACertificateDeleteResponse  { id, revoked_at } id: optional string
Identifier.
maxLength32[]revoked_at: optional string
When the certificate was revoked.
formatdate-time[][]