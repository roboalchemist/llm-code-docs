# Associations | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/mtls_certificates/subresources/associations

[API Reference][MTLS Certificates]
# Associations

##### [List mTLS certificate associations]
GET/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}/associations
##### ModelsExpand Collapse
CertificateAsssociation  { service, status } service: optional string
The service using the certificate.
[]status: optional string
Certificate deployment status for the given service.
[][]