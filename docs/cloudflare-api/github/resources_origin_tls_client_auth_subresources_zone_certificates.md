# Zone Certificates | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/zone_certificates

[API Reference][Origin TLS Client Auth]
# Zone Certificates

##### [List Certificates]
GET/zones/{zone_id}/origin_tls_client_auth
##### [Get Certificate Details]
GET/zones/{zone_id}/origin_tls_client_auth/{certificate_id}
##### [Upload Certificate]
POST/zones/{zone_id}/origin_tls_client_auth
##### [Delete Certificate]
DELETE/zones/{zone_id}/origin_tls_client_auth/{certificate_id}
##### ModelsExpand Collapse
ZoneAuthenticatedOriginPull  { id, certificate, expires_on, 4 more } id: optional string
Identifier.
maxLength32[]certificate: optional string
The zone’s leaf certificate.
[]expires_on: optional string
When the certificate from the authority expires.
formatdate-time[]issuer: optional string
The certificate authority that issued the certificate.
[]signature: optional string
The type of hash used for the certificate.
[]status: optional "initializing" or "pending_deployment" or "pending_deletion" or 4 more
Status of the certificate activation.
One of the following:"initializing"[]"pending_deployment"[]"pending_deletion"[]"active"[]"deleted"[]"deployment_timed_out"[]"deletion_timed_out"[][]uploaded_on: optional string
This is the time the certificate was uploaded.
formatdate-time[][]ZoneCertificateListResponse = [ZoneAuthenticatedOriginPull] { id, certificate, expires_on, 4 more } id: optional string
Identifier.
maxLength32[]certificate: optional string
The zone’s leaf certificate.
[]enabled: optional boolean
Indicates whether zone-level authenticated origin pulls is enabled.
[]private_key: optional string
The zone’s private key.
[][]ZoneCertificateGetResponse = [ZoneAuthenticatedOriginPull] { id, certificate, expires_on, 4 more } id: optional string
Identifier.
maxLength32[]certificate: optional string
The zone’s leaf certificate.
[]enabled: optional boolean
Indicates whether zone-level authenticated origin pulls is enabled.
[]private_key: optional string
The zone’s private key.
[][]ZoneCertificateCreateResponse = [ZoneAuthenticatedOriginPull] { id, certificate, expires_on, 4 more } id: optional string
Identifier.
maxLength32[]certificate: optional string
The zone’s leaf certificate.
[]enabled: optional boolean
Indicates whether zone-level authenticated origin pulls is enabled.
[]private_key: optional string
The zone’s private key.
[][]ZoneCertificateDeleteResponse = [ZoneAuthenticatedOriginPull] { id, certificate, expires_on, 4 more } id: optional string
Identifier.
maxLength32[]certificate: optional string
The zone’s leaf certificate.
[]enabled: optional boolean
Indicates whether zone-level authenticated origin pulls is enabled.
[]private_key: optional string
The zone’s private key.
[][]