# Custom Certificates | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/custom_certificates

[API Reference]
# Custom Certificates

##### [List SSL Configurations]
GET/zones/{zone_id}/custom_certificates
##### [SSL Configuration Details]
GET/zones/{zone_id}/custom_certificates/{custom_certificate_id}
##### [Create SSL Configuration]
POST/zones/{zone_id}/custom_certificates
##### [Edit SSL Configuration]
PATCH/zones/{zone_id}/custom_certificates/{custom_certificate_id}
##### [Delete SSL Configuration]
DELETE/zones/{zone_id}/custom_certificates/{custom_certificate_id}
##### ModelsExpand Collapse
CustomCertificate  { id, zone_id, bundle_method, 12 more } id: string
Identifier.
maxLength32[]zone_id: string
Identifier.
maxLength32[]bundle_method: optional [BundleMethod]
A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it.
[]custom_csr_id: optional string
The identifier for the Custom CSR that was used.
[]expires_on: optional string
When the certificate from the authority expires.
formatdate-time[]geo_restrictions: optional [GeoRestrictions] { label }
Specify the region where your private key can be held locally for optimal TLS performance. HTTPS connections to any excluded data center will still be fully encrypted, but will incur some latency while Keyless SSL is used to complete the handshake with the nearest allowed data center. Options allow distribution to only to U.S. data centers, only to E.U. data centers, or only to highest security data centers. Default distribution is to all Cloudflare datacenters, for optimal performance.
[]hosts: optional array of string[]issuer: optional string
The certificate authority that issued the certificate.
[]keyless_server: optional [KeylessCertificate] { id, created_on, enabled, 7 more } []modified_on: optional string
When the certificate was last modified.
formatdate-time[]policy_restrictions: optional string
The policy restrictions returned by the API. This field is returned in responses
when a policy has been set. The API accepts the “policy” field in requests but
returns this field as “policy_restrictions” in responses.

Specifies the region(s) where your private key can be held locally for optimal
TLS performance. Format is a boolean expression, for example:
“(country: US) or (region: EU)”
[]priority: optional number
The order/priority in which the certificate will be used in a request. The higher priority will break ties across overlapping ‘legacy_custom’ certificates, but ‘legacy_custom’ certificates will always supercede ‘sni_custom’ certificates.
[]signature: optional string
The type of hash used for the certificate.
[]status: optional "active" or "expired" or "deleted" or 2 more
Status of the zone’s custom SSL.
One of the following:"active"[]"expired"[]"deleted"[]"pending"[]"initializing"[][]uploaded_on: optional string
When the certificate was uploaded to Cloudflare.
formatdate-time[][]GeoRestrictions  { label }
Specify the region where your private key can be held locally for optimal TLS performance. HTTPS connections to any excluded data center will still be fully encrypted, but will incur some latency while Keyless SSL is used to complete the handshake with the nearest allowed data center. Options allow distribution to only to U.S. data centers, only to E.U. data centers, or only to highest security data centers. Default distribution is to all Cloudflare datacenters, for optimal performance.
label: optional "us" or "eu" or "highest_security"One of the following:"us"[]"eu"[]"highest_security"[][][]Status = "active" or "pending_reactivation" or "pending_revocation" or "revoked"
Client Certificates may be active or revoked, and the pending_reactivation or pending_revocation represent in-progress asynchronous transitions
One of the following:"active"[]"pending_reactivation"[]"pending_revocation"[]"revoked"[][]CustomCertificateDeleteResponse  { id } id: optional string
Identifier.
maxLength32[][]
#### Custom CertificatesPrioritize

##### [Re-prioritize SSL Certificates]
PUT/zones/{zone_id}/custom_certificates/prioritize