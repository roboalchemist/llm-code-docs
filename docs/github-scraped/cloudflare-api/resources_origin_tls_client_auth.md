# Origin TLS Client Auth | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/origin_tls_client_auth

[API Reference]
# Origin TLS Client Auth

##### [List Certificates]
DeprecatedGET/zones/{zone_id}/origin_tls_client_auth
##### [Get Certificate Details]
DeprecatedGET/zones/{zone_id}/origin_tls_client_auth/{certificate_id}
##### [Upload Certificate]
DeprecatedPOST/zones/{zone_id}/origin_tls_client_auth
##### [Delete Certificate]
DeprecatedDELETE/zones/{zone_id}/origin_tls_client_auth/{certificate_id}
##### ModelsExpand Collapse
OriginTLSClientAuthListResponse = [ZoneAuthenticatedOriginPull] { id, certificate, expires_on, 4 more } id: optional string
Identifier.
maxLength32[]certificate: optional string
The zone’s leaf certificate.
[]enabled: optional boolean
Indicates whether zone-level authenticated origin pulls is enabled.
[]private_key: optional string
The zone’s private key.
[][]OriginTLSClientAuthGetResponse = [ZoneAuthenticatedOriginPull] { id, certificate, expires_on, 4 more } id: optional string
Identifier.
maxLength32[]certificate: optional string
The zone’s leaf certificate.
[]enabled: optional boolean
Indicates whether zone-level authenticated origin pulls is enabled.
[]private_key: optional string
The zone’s private key.
[][]OriginTLSClientAuthCreateResponse = [ZoneAuthenticatedOriginPull] { id, certificate, expires_on, 4 more } id: optional string
Identifier.
maxLength32[]certificate: optional string
The zone’s leaf certificate.
[]enabled: optional boolean
Indicates whether zone-level authenticated origin pulls is enabled.
[]private_key: optional string
The zone’s private key.
[][]OriginTLSClientAuthDeleteResponse = [ZoneAuthenticatedOriginPull] { id, certificate, expires_on, 4 more } id: optional string
Identifier.
maxLength32[]certificate: optional string
The zone’s leaf certificate.
[]enabled: optional boolean
Indicates whether zone-level authenticated origin pulls is enabled.
[]private_key: optional string
The zone’s private key.
[][]
#### Origin TLS Client AuthZone Certificates

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
#### Origin TLS Client AuthHostnames

##### [Get the Hostname Status for Client Authentication]
GET/zones/{zone_id}/origin_tls_client_auth/hostnames/{hostname}
##### [Enable or Disable a Hostname for Client Authentication]
PUT/zones/{zone_id}/origin_tls_client_auth/hostnames
##### ModelsExpand Collapse
AuthenticatedOriginPull  { cert_id, cert_status, cert_updated_at, 11 more } cert_id: optional string
Identifier.
maxLength32[]cert_status: optional "initializing" or "pending_deployment" or "pending_deletion" or 4 more
Status of the certificate or the association.
One of the following:"initializing"[]"pending_deployment"[]"pending_deletion"[]"active"[]"deleted"[]"deployment_timed_out"[]"deletion_timed_out"[][]cert_updated_at: optional string
The time when the certificate was updated.
formatdate-time[]cert_uploaded_on: optional string
The time when the certificate was uploaded.
formatdate-time[]certificate: optional string
The hostname certificate.
[]created_at: optional string
The time when the certificate was created.
formatdate-time[]enabled: optional boolean
Indicates whether hostname-level authenticated origin pulls is enabled. A null value voids the association.
[]expires_on: optional string
The date when the certificate expires.
formatdate-time[]hostname: optional string
The hostname on the origin for which the client certificate uploaded will be used.
maxLength255[]issuer: optional string
The certificate authority that issued the certificate.
[]serial_number: optional string
The serial number on the uploaded certificate.
[]signature: optional string
The type of hash used for the certificate.
[]status: optional "initializing" or "pending_deployment" or "pending_deletion" or 4 more
Status of the certificate or the association.
One of the following:"initializing"[]"pending_deployment"[]"pending_deletion"[]"active"[]"deleted"[]"deployment_timed_out"[]"deletion_timed_out"[][]updated_at: optional string
The time when the certificate was updated.
formatdate-time[][]HostnameUpdateResponse = [AuthenticatedOriginPull] { cert_id, cert_status, cert_updated_at, 11 more } id: optional string
Identifier.
maxLength32[]cert_id: optional string
Identifier.
maxLength32[]certificate: optional string
The hostname certificate.
[]enabled: optional boolean
Indicates whether hostname-level authenticated origin pulls is enabled. A null value voids the association.
[]hostname: optional string
The hostname on the origin for which the client certificate uploaded will be used.
maxLength255[]private_key: optional string
The hostname certificate’s private key.
[][]
#### Origin TLS Client AuthHostname Certificates

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
#### Origin TLS Client AuthSettings

##### [Get Enablement Setting for Zone]
GET/zones/{zone_id}/origin_tls_client_auth/settings
##### [Set Enablement for Zone]
PUT/zones/{zone_id}/origin_tls_client_auth/settings
##### ModelsExpand Collapse
SettingGetResponse  { enabled } enabled: optional boolean
Indicates whether zone-level authenticated origin pulls is enabled.
[][]SettingUpdateResponse  { enabled } enabled: optional boolean
Indicates whether zone-level authenticated origin pulls is enabled.
[][]