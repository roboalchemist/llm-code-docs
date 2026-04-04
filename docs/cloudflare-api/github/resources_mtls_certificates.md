# MTLS Certificates | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/mtls_certificates

[API Reference]
# MTLS Certificates

##### [List mTLS certificates]
GET/accounts/{account_id}/mtls_certificates
##### [Get mTLS certificate]
GET/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}
##### [Upload mTLS certificate]
POST/accounts/{account_id}/mtls_certificates
##### [Delete mTLS certificate]
DELETE/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}
##### ModelsExpand Collapse
MTLSCertificate  { id, ca, certificates, 6 more } id: optional string
Identifier.
maxLength32[]ca: optional boolean
Indicates whether the certificate is a CA or leaf certificate.
[]certificates: optional string
The uploaded root CA certificate.
[]expires_on: optional string
When the certificate expires.
formatdate-time[]issuer: optional string
The certificate authority that issued the certificate.
[]name: optional string
Optional unique name for the certificate. Only used for human readability.
[]serial_number: optional string
The certificate serial number.
[]signature: optional string
The type of hash used for the certificate.
[]uploaded_on: optional string
This is the time the certificate was uploaded.
formatdate-time[][]MTLSCertificateCreateResponse  { id, ca, certificates, 7 more } id: optional string
Identifier.
maxLength32[]ca: optional boolean
Indicates whether the certificate is a CA or leaf certificate.
[]certificates: optional string
The uploaded root CA certificate.
[]expires_on: optional string
When the certificate expires.
formatdate-time[]issuer: optional string
The certificate authority that issued the certificate.
[]name: optional string
Optional unique name for the certificate. Only used for human readability.
[]serial_number: optional string
The certificate serial number.
[]signature: optional string
The type of hash used for the certificate.
[]updated_at: optional string
This is the time the certificate was updated.
formatdate-time[]uploaded_on: optional string
This is the time the certificate was uploaded.
formatdate-time[][]
#### MTLS CertificatesAssociations

##### [List mTLS certificate associations]
GET/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}/associations
##### ModelsExpand Collapse
CertificateAsssociation  { service, status } service: optional string
The service using the certificate.
[]status: optional string
Certificate deployment status for the given service.
[][]