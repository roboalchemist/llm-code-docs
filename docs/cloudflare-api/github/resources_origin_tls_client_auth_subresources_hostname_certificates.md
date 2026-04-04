# Hostname Certificates | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostname_certificates

[API Reference][Origin TLS Client Auth]
# Hostname Certificates

##### [List Certificates]
GET/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates
##### [Get the Hostname Client Certificate]
GET/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}
##### [Upload a Hostname Client Certificate]
POST/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates
##### [Delete Hostname Client Certificate]
DELETE/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}
##### ModelsExpand Collapse
Certificate  { id, certificate, expires_on, 5 more } id: optional string
Identifier.
maxLength32[]certificate: optional string
The hostname certificate.
[]expires_on: optional string
The date when the certificate expires.
formatdate-time[]issuer: optional string
The certificate authority that issued the certificate.
[]serial_number: optional string
The serial number on the uploaded certificate.
[]signature: optional string
The type of hash used for the certificate.
[]status: optional "initializing" or "pending_deployment" or "pending_deletion" or 4 more
Status of the certificate or the association.
One of the following:"initializing"[]"pending_deployment"[]"pending_deletion"[]"active"[]"deleted"[]"deployment_timed_out"[]"deletion_timed_out"[][]uploaded_on: optional string
The time when the certificate was uploaded.
formatdate-time[][]HostnameCertificateListResponse  { id, certificate, expires_on, 5 more } id: optional string
Identifier.
maxLength32[]certificate: optional string
The hostname certificate.
[]expires_on: optional string
The date when the certificate expires.
formatdate-time[]issuer: optional string
The certificate authority that issued the certificate.
[]serial_number: optional string
The serial number on the uploaded certificate.
[]signature: optional string
The type of hash used for the certificate.
[]status: optional "initializing" or "pending_deployment" or "pending_deletion" or 4 more
Status of the certificate or the association.
One of the following:"initializing"[]"pending_deployment"[]"pending_deletion"[]"active"[]"deleted"[]"deployment_timed_out"[]"deletion_timed_out"[][]uploaded_on: optional string
The time when the certificate was uploaded.
formatdate-time[][]HostnameCertificateGetResponse  { id, certificate, expires_on, 5 more } id: optional string
Identifier.
maxLength32[]certificate: optional string
The hostname certificate.
[]expires_on: optional string
The date when the certificate expires.
formatdate-time[]issuer: optional string
The certificate authority that issued the certificate.
[]serial_number: optional string
The serial number on the uploaded certificate.
[]signature: optional string
The type of hash used for the certificate.
[]status: optional "initializing" or "pending_deployment" or "pending_deletion" or 4 more
Status of the certificate or the association.
One of the following:"initializing"[]"pending_deployment"[]"pending_deletion"[]"active"[]"deleted"[]"deployment_timed_out"[]"deletion_timed_out"[][]uploaded_on: optional string
The time when the certificate was uploaded.
formatdate-time[][]HostnameCertificateCreateResponse  { id, certificate, expires_on, 5 more } id: optional string
Identifier.
maxLength32[]certificate: optional string
The hostname certificate.
[]expires_on: optional string
The date when the certificate expires.
formatdate-time[]issuer: optional string
The certificate authority that issued the certificate.
[]serial_number: optional string
The serial number on the uploaded certificate.
[]signature: optional string
The type of hash used for the certificate.
[]status: optional "initializing" or "pending_deployment" or "pending_deletion" or 4 more
Status of the certificate or the association.
One of the following:"initializing"[]"pending_deployment"[]"pending_deletion"[]"active"[]"deleted"[]"deployment_timed_out"[]"deletion_timed_out"[][]uploaded_on: optional string
The time when the certificate was uploaded.
formatdate-time[][]HostnameCertificateDeleteResponse  { id, certificate, expires_on, 5 more } id: optional string
Identifier.
maxLength32[]certificate: optional string
The hostname certificate.
[]expires_on: optional string
The date when the certificate expires.
formatdate-time[]issuer: optional string
The certificate authority that issued the certificate.
[]serial_number: optional string
The serial number on the uploaded certificate.
[]signature: optional string
The type of hash used for the certificate.
[]status: optional "initializing" or "pending_deployment" or "pending_deletion" or 4 more
Status of the certificate or the association.
One of the following:"initializing"[]"pending_deployment"[]"pending_deletion"[]"active"[]"deleted"[]"deployment_timed_out"[]"deletion_timed_out"[][]uploaded_on: optional string
The time when the certificate was uploaded.
formatdate-time[][]