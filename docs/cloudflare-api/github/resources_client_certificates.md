# Client Certificates | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/client_certificates

[API Reference]
# Client Certificates

##### [List Client Certificates]
GET/zones/{zone_id}/client_certificates
##### [Client Certificate Details]
GET/zones/{zone_id}/client_certificates/{client_certificate_id}
##### [Create Client Certificate]
POST/zones/{zone_id}/client_certificates
##### [Reactivate Client Certificate]
PATCH/zones/{zone_id}/client_certificates/{client_certificate_id}
##### [Revoke Client Certificate]
DELETE/zones/{zone_id}/client_certificates/{client_certificate_id}
##### ModelsExpand Collapse
ClientCertificate  { id, certificate, certificate_authority, 15 more } id: optional string
Identifier.
maxLength32[]certificate: optional string
The Client Certificate PEM
[]certificate_authority: optional  { id, name }
Certificate Authority used to issue the Client Certificate
id: optional string[]name: optional string[][]common_name: optional string
Common Name of the Client Certificate
[]country: optional string
Country, provided by the CSR
[]csr: optional string
The Certificate Signing Request (CSR). Must be newline-encoded.
[]expires_on: optional string
Date that the Client Certificate expires
[]fingerprint_sha256: optional string
Unique identifier of the Client Certificate
[]issued_on: optional string
Date that the Client Certificate was issued by the Certificate Authority
[]location: optional string
Location, provided by the CSR
[]organization: optional string
Organization, provided by the CSR
[]organizational_unit: optional string
Organizational Unit, provided by the CSR
[]serial_number: optional string
The serial number on the created Client Certificate.
[]signature: optional string
The type of hash used for the Client Certificate..
[]ski: optional string
Subject Key Identifier
[]state: optional string
State, provided by the CSR
[]status: optional [Status]
Client Certificates may be active or revoked, and the pending_reactivation or pending_revocation represent in-progress asynchronous transitions
[]validity_days: optional number
The number of days the Client Certificate will be valid after the issued_on date
[][]