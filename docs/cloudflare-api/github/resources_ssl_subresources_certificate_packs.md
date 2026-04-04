# Certificate Packs | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs

[API Reference][SSL]
# Certificate Packs

##### [List Certificate Packs]
GET/zones/{zone_id}/ssl/certificate_packs
##### [Get Certificate Pack]
GET/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}
##### [Order Advanced Certificate Manager Certificate Pack]
POST/zones/{zone_id}/ssl/certificate_packs/order
##### [Restart Validation or Update Advanced Certificate Manager Certificate Pack]
PATCH/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}
##### [Delete Advanced Certificate Manager Certificate Pack]
DELETE/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}
##### ModelsExpand Collapse
Host = string[]RequestValidity = 7 or 30 or 90 or 4 more
The number of days for which the certificate should be valid.
One of the following:7[]30[]90[]365[]730[]1095[]5475[][]Status = "initializing" or "pending_validation" or "deleted" or 18 more
Status of certificate pack.
One of the following:"initializing"[]"pending_validation"[]"deleted"[]"pending_issuance"[]"pending_deployment"[]"pending_deletion"[]"pending_expiration"[]"expired"[]"active"[]"initializing_timed_out"[]"validation_timed_out"[]"issuance_timed_out"[]"deployment_timed_out"[]"deletion_timed_out"[]"pending_cleanup"[]"staging_deployment"[]"staging_active"[]"deactivating"[]"inactive"[]"backup_issued"[]"holding_deployment"[][]ValidationMethod = "http" or "cname" or "txt"
Validation method in use for a certificate pack order.
One of the following:"http"[]"cname"[]"txt"[][]CertificatePackListResponse  { id, certificates, hosts, 10 more }
A certificate pack with all its properties.
id: string
Identifier.
maxLength32[]certificates: array of  { id, hosts, status, 9 more }
Array of certificates in this pack.
id: string
Certificate identifier.
[]hosts: array of string
Hostnames covered by this certificate.
[]status: string
Certificate status.
[]bundle_method: optional string
Certificate bundle method.
[]expires_on: optional string
When the certificate from the authority expires.
formatdate-time[]geo_restrictions: optional  { label }
Specify the region where your private key can be held locally.
label: optional "us" or "eu" or "highest_security"One of the following:"us"[]"eu"[]"highest_security"[][][]issuer: optional string
The certificate authority that issued the certificate.
[]modified_on: optional string
When the certificate was last modified.
formatdate-time[]priority: optional number
The order/priority in which the certificate will be used.
[]signature: optional string
The type of hash used for the certificate.
[]uploaded_on: optional string
When the certificate was uploaded to Cloudflare.
formatdate-time[]zone_id: optional string
Identifier.
maxLength32[][]hosts: array of [Host]
Comma separated list of valid host names for the certificate packs. Must contain the zone apex, may not contain more than 50 hosts, and may not be empty.
[]status: [Status]
Status of certificate pack.
[]type: "mh_custom" or "managed_hostname" or "sni_custom" or 5 more
Type of certificate pack.
One of the following:"mh_custom"[]"managed_hostname"[]"sni_custom"[]"universal"[]"advanced"[]"total_tls"[]"keyless"[]"legacy_custom"[][]certificate_authority: optional "google" or "lets_encrypt" or "ssl_com"
Certificate Authority selected for the order.  For information on any certificate authority specific details or restrictions [see this page for more details.]
One of the following:"google"[]"lets_encrypt"[]"ssl_com"[][]cloudflare_branding: optional boolean
Whether or not to add Cloudflare Branding for the order.  This will add a subdomain of sni.cloudflaressl.com as the Common Name if set to true.
[]dcv_delegation_records: optional array of  { cname, cname_target, emails, 5 more }
DCV Delegation records for domain validation.
cname: optional string
The CNAME record hostname for DCV delegation.
[]cname_target: optional string
The CNAME record target value for DCV delegation.
[]emails: optional array of string
The set of email addresses that the certificate authority (CA) will use to complete domain validation.
[]http_body: optional string
The content that the certificate authority (CA) will expect to find at the http_url during the domain validation.
[]http_url: optional string
The url that will be checked during domain validation.
[]status: optional string
Status of the validation record.
[]txt_name: optional string
The hostname that the certificate authority (CA) will check for a TXT record during domain validation .
[]txt_value: optional string
The TXT record that the certificate authority (CA) will check during domain validation.
[][]primary_certificate: optional string
Identifier of the primary certificate in a pack.
[]validation_errors: optional array of  { message }
Domain validation errors that have been received by the certificate authority (CA).
message: optional string
A domain validation error.
[][]validation_method: optional "txt" or "http" or "email"
Validation Method selected for the order.
One of the following:"txt"[]"http"[]"email"[][]validation_records: optional array of  { cname, cname_target, emails, 5 more }
Certificates’ validation records.
cname: optional string
The CNAME record hostname for DCV delegation.
[]cname_target: optional string
The CNAME record target value for DCV delegation.
[]emails: optional array of string
The set of email addresses that the certificate authority (CA) will use to complete domain validation.
[]http_body: optional string
The content that the certificate authority (CA) will expect to find at the http_url during the domain validation.
[]http_url: optional string
The url that will be checked during domain validation.
[]status: optional string
Status of the validation record.
[]txt_name: optional string
The hostname that the certificate authority (CA) will check for a TXT record during domain validation .
[]txt_value: optional string
The TXT record that the certificate authority (CA) will check during domain validation.
[][]validity_days: optional 14 or 30 or 90 or 365
Validity Days selected for the order.
One of the following:14[]30[]90[]365[][][]CertificatePackGetResponse  { id, certificates, hosts, 10 more }
A certificate pack with all its properties.
id: string
Identifier.
maxLength32[]certificates: array of  { id, hosts, status, 9 more }
Array of certificates in this pack.
id: string
Certificate identifier.
[]hosts: array of string
Hostnames covered by this certificate.
[]status: string
Certificate status.
[]bundle_method: optional string
Certificate bundle method.
[]expires_on: optional string
When the certificate from the authority expires.
formatdate-time[]geo_restrictions: optional  { label }
Specify the region where your private key can be held locally.
label: optional "us" or "eu" or "highest_security"One of the following:"us"[]"eu"[]"highest_security"[][][]issuer: optional string
The certificate authority that issued the certificate.
[]modified_on: optional string
When the certificate was last modified.
formatdate-time[]priority: optional number
The order/priority in which the certificate will be used.
[]signature: optional string
The type of hash used for the certificate.
[]uploaded_on: optional string
When the certificate was uploaded to Cloudflare.
formatdate-time[]zone_id: optional string
Identifier.
maxLength32[][]hosts: array of [Host]
Comma separated list of valid host names for the certificate packs. Must contain the zone apex, may not contain more than 50 hosts, and may not be empty.
[]status: [Status]
Status of certificate pack.
[]type: "mh_custom" or "managed_hostname" or "sni_custom" or 5 more
Type of certificate pack.
One of the following:"mh_custom"[]"managed_hostname"[]"sni_custom"[]"universal"[]"advanced"[]"total_tls"[]"keyless"[]"legacy_custom"[][]certificate_authority: optional "google" or "lets_encrypt" or "ssl_com"
Certificate Authority selected for the order.  For information on any certificate authority specific details or restrictions [see this page for more details.]
One of the following:"google"[]"lets_encrypt"[]"ssl_com"[][]cloudflare_branding: optional boolean
Whether or not to add Cloudflare Branding for the order.  This will add a subdomain of sni.cloudflaressl.com as the Common Name if set to true.
[]dcv_delegation_records: optional array of  { cname, cname_target, emails, 5 more }
DCV Delegation records for domain validation.
cname: optional string
The CNAME record hostname for DCV delegation.
[]cname_target: optional string
The CNAME record target value for DCV delegation.
[]emails: optional array of string
The set of email addresses that the certificate authority (CA) will use to complete domain validation.
[]http_body: optional string
The content that the certificate authority (CA) will expect to find at the http_url during the domain validation.
[]http_url: optional string
The url that will be checked during domain validation.
[]status: optional string
Status of the validation record.
[]txt_name: optional string
The hostname that the certificate authority (CA) will check for a TXT record during domain validation .
[]txt_value: optional string
The TXT record that the certificate authority (CA) will check during domain validation.
[][]primary_certificate: optional string
Identifier of the primary certificate in a pack.
[]validation_errors: optional array of  { message }
Domain validation errors that have been received by the certificate authority (CA).
message: optional string
A domain validation error.
[][]validation_method: optional "txt" or "http" or "email"
Validation Method selected for the order.
One of the following:"txt"[]"http"[]"email"[][]validation_records: optional array of  { cname, cname_target, emails, 5 more }
Certificates’ validation records.
cname: optional string
The CNAME record hostname for DCV delegation.
[]cname_target: optional string
The CNAME record target value for DCV delegation.
[]emails: optional array of string
The set of email addresses that the certificate authority (CA) will use to complete domain validation.
[]http_body: optional string
The content that the certificate authority (CA) will expect to find at the http_url during the domain validation.
[]http_url: optional string
The url that will be checked during domain validation.
[]status: optional string
Status of the validation record.
[]txt_name: optional string
The hostname that the certificate authority (CA) will check for a TXT record during domain validation .
[]txt_value: optional string
The TXT record that the certificate authority (CA) will check during domain validation.
[][]validity_days: optional 14 or 30 or 90 or 365
Validity Days selected for the order.
One of the following:14[]30[]90[]365[][][]CertificatePackCreateResponse  { id, certificates, hosts, 10 more }
A certificate pack with all its properties.
id: string
Identifier.
maxLength32[]certificates: array of  { id, hosts, status, 9 more }
Array of certificates in this pack.
id: string
Certificate identifier.
[]hosts: array of string
Hostnames covered by this certificate.
[]status: string
Certificate status.
[]bundle_method: optional string
Certificate bundle method.
[]expires_on: optional string
When the certificate from the authority expires.
formatdate-time[]geo_restrictions: optional  { label }
Specify the region where your private key can be held locally.
label: optional "us" or "eu" or "highest_security"One of the following:"us"[]"eu"[]"highest_security"[][][]issuer: optional string
The certificate authority that issued the certificate.
[]modified_on: optional string
When the certificate was last modified.
formatdate-time[]priority: optional number
The order/priority in which the certificate will be used.
[]signature: optional string
The type of hash used for the certificate.
[]uploaded_on: optional string
When the certificate was uploaded to Cloudflare.
formatdate-time[]zone_id: optional string
Identifier.
maxLength32[][]hosts: array of [Host]
Comma separated list of valid host names for the certificate packs. Must contain the zone apex, may not contain more than 50 hosts, and may not be empty.
[]status: [Status]
Status of certificate pack.
[]type: "mh_custom" or "managed_hostname" or "sni_custom" or 5 more
Type of certificate pack.
One of the following:"mh_custom"[]"managed_hostname"[]"sni_custom"[]"universal"[]"advanced"[]"total_tls"[]"keyless"[]"legacy_custom"[][]certificate_authority: optional "google" or "lets_encrypt" or "ssl_com"
Certificate Authority selected for the order.  For information on any certificate authority specific details or restrictions [see this page for more details.]
One of the following:"google"[]"lets_encrypt"[]"ssl_com"[][]cloudflare_branding: optional boolean
Whether or not to add Cloudflare Branding for the order.  This will add a subdomain of sni.cloudflaressl.com as the Common Name if set to true.
[]dcv_delegation_records: optional array of  { cname, cname_target, emails, 5 more }
DCV Delegation records for domain validation.
cname: optional string
The CNAME record hostname for DCV delegation.
[]cname_target: optional string
The CNAME record target value for DCV delegation.
[]emails: optional array of string
The set of email addresses that the certificate authority (CA) will use to complete domain validation.
[]http_body: optional string
The content that the certificate authority (CA) will expect to find at the http_url during the domain validation.
[]http_url: optional string
The url that will be checked during domain validation.
[]status: optional string
Status of the validation record.
[]txt_name: optional string
The hostname that the certificate authority (CA) will check for a TXT record during domain validation .
[]txt_value: optional string
The TXT record that the certificate authority (CA) will check during domain validation.
[][]primary_certificate: optional string
Identifier of the primary certificate in a pack.
[]validation_errors: optional array of  { message }
Domain validation errors that have been received by the certificate authority (CA).
message: optional string
A domain validation error.
[][]validation_method: optional "txt" or "http" or "email"
Validation Method selected for the order.
One of the following:"txt"[]"http"[]"email"[][]validation_records: optional array of  { cname, cname_target, emails, 5 more }
Certificates’ validation records.
cname: optional string
The CNAME record hostname for DCV delegation.
[]cname_target: optional string
The CNAME record target value for DCV delegation.
[]emails: optional array of string
The set of email addresses that the certificate authority (CA) will use to complete domain validation.
[]http_body: optional string
The content that the certificate authority (CA) will expect to find at the http_url during the domain validation.
[]http_url: optional string
The url that will be checked during domain validation.
[]status: optional string
Status of the validation record.
[]txt_name: optional string
The hostname that the certificate authority (CA) will check for a TXT record during domain validation .
[]txt_value: optional string
The TXT record that the certificate authority (CA) will check during domain validation.
[][]validity_days: optional 14 or 30 or 90 or 365
Validity Days selected for the order.
One of the following:14[]30[]90[]365[][][]CertificatePackEditResponse  { id, certificates, hosts, 10 more }
A certificate pack with all its properties.
id: string
Identifier.
maxLength32[]certificates: array of  { id, hosts, status, 9 more }
Array of certificates in this pack.
id: string
Certificate identifier.
[]hosts: array of string
Hostnames covered by this certificate.
[]status: string
Certificate status.
[]bundle_method: optional string
Certificate bundle method.
[]expires_on: optional string
When the certificate from the authority expires.
formatdate-time[]geo_restrictions: optional  { label }
Specify the region where your private key can be held locally.
label: optional "us" or "eu" or "highest_security"One of the following:"us"[]"eu"[]"highest_security"[][][]issuer: optional string
The certificate authority that issued the certificate.
[]modified_on: optional string
When the certificate was last modified.
formatdate-time[]priority: optional number
The order/priority in which the certificate will be used.
[]signature: optional string
The type of hash used for the certificate.
[]uploaded_on: optional string
When the certificate was uploaded to Cloudflare.
formatdate-time[]zone_id: optional string
Identifier.
maxLength32[][]hosts: array of [Host]
Comma separated list of valid host names for the certificate packs. Must contain the zone apex, may not contain more than 50 hosts, and may not be empty.
[]status: [Status]
Status of certificate pack.
[]type: "mh_custom" or "managed_hostname" or "sni_custom" or 5 more
Type of certificate pack.
One of the following:"mh_custom"[]"managed_hostname"[]"sni_custom"[]"universal"[]"advanced"[]"total_tls"[]"keyless"[]"legacy_custom"[][]certificate_authority: optional "google" or "lets_encrypt" or "ssl_com"
Certificate Authority selected for the order.  For information on any certificate authority specific details or restrictions [see this page for more details.]
One of the following:"google"[]"lets_encrypt"[]"ssl_com"[][]cloudflare_branding: optional boolean
Whether or not to add Cloudflare Branding for the order.  This will add a subdomain of sni.cloudflaressl.com as the Common Name if set to true.
[]dcv_delegation_records: optional array of  { cname, cname_target, emails, 5 more }
DCV Delegation records for domain validation.
cname: optional string
The CNAME record hostname for DCV delegation.
[]cname_target: optional string
The CNAME record target value for DCV delegation.
[]emails: optional array of string
The set of email addresses that the certificate authority (CA) will use to complete domain validation.
[]http_body: optional string
The content that the certificate authority (CA) will expect to find at the http_url during the domain validation.
[]http_url: optional string
The url that will be checked during domain validation.
[]status: optional string
Status of the validation record.
[]txt_name: optional string
The hostname that the certificate authority (CA) will check for a TXT record during domain validation .
[]txt_value: optional string
The TXT record that the certificate authority (CA) will check during domain validation.
[][]primary_certificate: optional string
Identifier of the primary certificate in a pack.
[]validation_errors: optional array of  { message }
Domain validation errors that have been received by the certificate authority (CA).
message: optional string
A domain validation error.
[][]validation_method: optional "txt" or "http" or "email"
Validation Method selected for the order.
One of the following:"txt"[]"http"[]"email"[][]validation_records: optional array of  { cname, cname_target, emails, 5 more }
Certificates’ validation records.
cname: optional string
The CNAME record hostname for DCV delegation.
[]cname_target: optional string
The CNAME record target value for DCV delegation.
[]emails: optional array of string
The set of email addresses that the certificate authority (CA) will use to complete domain validation.
[]http_body: optional string
The content that the certificate authority (CA) will expect to find at the http_url during the domain validation.
[]http_url: optional string
The url that will be checked during domain validation.
[]status: optional string
Status of the validation record.
[]txt_name: optional string
The hostname that the certificate authority (CA) will check for a TXT record during domain validation .
[]txt_value: optional string
The TXT record that the certificate authority (CA) will check during domain validation.
[][]validity_days: optional 14 or 30 or 90 or 365
Validity Days selected for the order.
One of the following:14[]30[]90[]365[][][]CertificatePackDeleteResponse  { id } id: optional string
Identifier.
maxLength32[][]
#### Certificate PacksQuota

##### [Get Certificate Pack Quotas]
GET/zones/{zone_id}/ssl/certificate_packs/quota
##### ModelsExpand Collapse
QuotaGetResponse  { advanced } advanced: optional  { allocated, used } allocated: optional number
Quantity Allocated.
[]used: optional number
Quantity Used.
[][][]