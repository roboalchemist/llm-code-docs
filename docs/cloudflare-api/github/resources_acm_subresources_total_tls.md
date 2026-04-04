# Total TLS | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/acm/subresources/total_tls

[API Reference][ACM]
# Total TLS

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