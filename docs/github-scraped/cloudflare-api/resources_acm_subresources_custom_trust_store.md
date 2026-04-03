# Custom Trust Store | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/acm/subresources/custom_trust_store

[API Reference][ACM]
# Custom Trust Store

##### [List Custom Origin Trust Store Details]
GET/zones/{zone_id}/acm/custom_trust_store
##### [Upload Custom Origin Trust Store]
POST/zones/{zone_id}/acm/custom_trust_store
##### [Custom Origin Trust Store Details]
GET/zones/{zone_id}/acm/custom_trust_store/{custom_origin_trust_store_id}
##### [Delete Custom Origin Trust Store]
DELETE/zones/{zone_id}/acm/custom_trust_store/{custom_origin_trust_store_id}
##### ModelsExpand Collapse
CustomTrustStore  { id, certificate, expires_on, 5 more } id: string
Identifier.
maxLength32[]certificate: string
The zone’s SSL certificate or certificate and the intermediate(s).
[]expires_on: string
When the certificate expires.
formatdate-time[]issuer: string
The certificate authority that issued the certificate.
[]signature: string
The type of hash used for the certificate.
[]status: "initializing" or "pending_deployment" or "active" or 3 more
Status of the zone’s custom SSL.
One of the following:"initializing"[]"pending_deployment"[]"active"[]"pending_deletion"[]"deleted"[]"expired"[][]updated_at: string
When the certificate was last modified.
formatdate-time[]uploaded_on: string
When the certificate was uploaded to Cloudflare.
formatdate-time[][]CustomTrustStoreDeleteResponse  { id } id: optional string
Identifier.
maxLength32[][]