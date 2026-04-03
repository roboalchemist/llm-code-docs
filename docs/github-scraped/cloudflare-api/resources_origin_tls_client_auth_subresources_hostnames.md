# Hostnames | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostnames

[API Reference][Origin TLS Client Auth]
# Hostnames

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