# ACM | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/acm

[API Reference]
# ACM

#### ACMTotal TLS

##### [Total TLS Settings Details]
GET/zones/{zone_id}/acm/total_tls
##### [Enable or Disable Total TLS]
POST/zones/{zone_id}/acm/total_tls
##### [Enable or Disable Total TLS]
POST/zones/{zone_id}/acm/total_tls
##### ModelsExpand Collapse
CertificateAuthority = "google" or "lets_encrypt" or "ssl_com"
The Certificate Authority that Total TLS certificates will be issued through.
One of the following:"google"[]"lets_encrypt"[]"ssl_com"[][]TotalTLSGetResponse  { certificate_authority, enabled, validity_period } certificate_authority: optional [CertificateAuthority]
The Certificate Authority that Total TLS certificates will be issued through.
[]enabled: optional boolean
If enabled, Total TLS will order a hostname specific TLS certificate for any proxied A, AAAA, or CNAME record in your zone.
[]validity_period: optional 90
The validity period in days for the certificates ordered via Total TLS.
[][]TotalTLSUpdateResponse  { certificate_authority, enabled, validity_period } certificate_authority: optional [CertificateAuthority]
The Certificate Authority that Total TLS certificates will be issued through.
[]enabled: optional boolean
If enabled, Total TLS will order a hostname specific TLS certificate for any proxied A, AAAA, or CNAME record in your zone.
[]validity_period: optional 90
The validity period in days for the certificates ordered via Total TLS.
[][]TotalTLSEditResponse  { certificate_authority, enabled, validity_period } certificate_authority: optional [CertificateAuthority]
The Certificate Authority that Total TLS certificates will be issued through.
[]enabled: optional boolean
If enabled, Total TLS will order a hostname specific TLS certificate for any proxied A, AAAA, or CNAME record in your zone.
[]validity_period: optional 90
The validity period in days for the certificates ordered via Total TLS.
[][]
#### ACMCustom Trust Store

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