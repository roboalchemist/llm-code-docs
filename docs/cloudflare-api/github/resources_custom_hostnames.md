# Custom Hostnames | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/custom_hostnames

[API Reference]
# Custom Hostnames

##### [List Custom Hostnames]
GET/zones/{zone_id}/custom_hostnames
##### [Custom Hostname Details]
GET/zones/{zone_id}/custom_hostnames/{custom_hostname_id}
##### [Create Custom Hostname]
POST/zones/{zone_id}/custom_hostnames
##### [Edit Custom Hostname]
PATCH/zones/{zone_id}/custom_hostnames/{custom_hostname_id}
##### [Delete Custom Hostname (and any issued SSL certificates)]
DELETE/zones/{zone_id}/custom_hostnames/{custom_hostname_id}
##### ModelsExpand Collapse
BundleMethod = "ubiquitous" or "optimal" or "force"
A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it.
One of the following:"ubiquitous"[]"optimal"[]"force"[][]CustomHostname  { id, hostname, created_at, 8 more } id: string
Identifier.
maxLength32[]hostname: string
The custom hostname that will point to your hostname via CNAME.
maxLength255[]created_at: optional string
This is the time the hostname was created.
formatdate-time[]custom_metadata: optional map[string]
Unique key/value metadata for this hostname. These are per-hostname (customer) settings.
[]custom_origin_server: optional string
a valid hostname that’s been added to your DNS zone as an A, AAAA, or CNAME record.
[]custom_origin_sni: optional string
A hostname that will be sent to your custom origin server as SNI for TLS handshake. This can be a valid subdomain of the zone or custom origin server name or the string ‘:request_host_header:’ which will cause the host header in the request to be used as SNI. Not configurable with default/fallback origin server.
[]ownership_verification: optional  { name, type, value }
This is a record which can be placed to activate a hostname.
name: optional string
DNS Name for record.
[]type: optional "txt"
DNS Record type.
[]value: optional string
Content for the record.
[][]ownership_verification_http: optional  { http_body, http_url }
This presents the token to be served by the given http url to activate a hostname.
http_body: optional string
Token to be served.
[]http_url: optional string
The HTTP URL that will be checked during custom hostname verification and where the customer should host the token.
[][]ssl: optional  { id, bundle_method, certificate_authority, 17 more } id: optional string
Custom hostname SSL identifier tag.
maxLength36minLength36[]bundle_method: optional [BundleMethod]
A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it.
[]certificate_authority: optional [CertificateCA]
The Certificate Authority that will issue the certificate
[]custom_certificate: optional string
If a custom uploaded certificate is used.
[]custom_csr_id: optional string
The identifier for the Custom CSR that was used.
[]custom_key: optional string
The key for a custom uploaded certificate.
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
[][]expires_on: optional string
The time the custom certificate expires on.
formatdate-time[]hosts: optional array of string
A list of Hostnames on a custom uploaded certificate.
[]issuer: optional string
The issuer on a custom uploaded certificate.
[]method: optional [DCVMethod]
Domain control validation (DCV) method used for this hostname.
[]serial_number: optional string
The serial number on a custom uploaded certificate.
[]settings: optional  { ciphers, early_hints, http2, 2 more } ciphers: optional array of string
An allowlist of ciphers for TLS termination. These ciphers must be in the BoringSSL format.
[]early_hints: optional "on" or "off"
Whether or not Early Hints is enabled.
One of the following:"on"[]"off"[][]http2: optional "on" or "off"
Whether or not HTTP2 is enabled.
One of the following:"on"[]"off"[][]min_tls_version: optional "1.0" or "1.1" or "1.2" or "1.3"
The minimum TLS version supported.
One of the following:"1.0"[]"1.1"[]"1.2"[]"1.3"[][]tls_1_3: optional "on" or "off"
Whether or not TLS 1.3 is enabled.
One of the following:"on"[]"off"[][][]signature: optional string
The signature on a custom uploaded certificate.
[]status: optional "initializing" or "pending_validation" or "deleted" or 18 more
Status of the hostname’s SSL certificates.
One of the following:"initializing"[]"pending_validation"[]"deleted"[]"pending_issuance"[]"pending_deployment"[]"pending_deletion"[]"pending_expiration"[]"expired"[]"active"[]"initializing_timed_out"[]"validation_timed_out"[]"issuance_timed_out"[]"deployment_timed_out"[]"deletion_timed_out"[]"pending_cleanup"[]"staging_deployment"[]"staging_active"[]"deactivating"[]"inactive"[]"backup_issued"[]"holding_deployment"[][]type: optional [DomainValidationType]
Level of validation to be used for this hostname. Domain validation (dv) must be used.
[]uploaded_on: optional string
The time the custom certificate was uploaded.
formatdate-time[]validation_errors: optional array of  { message }
Domain validation errors that have been received by the certificate authority (CA).
message: optional string
A domain validation error.
[][]validation_records: optional array of  { cname, cname_target, emails, 5 more } cname: optional string
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
[][]wildcard: optional boolean
Indicates whether the certificate covers a wildcard.
[][]status: optional "active" or "pending" or "active_redeploying" or 13 more
Status of the hostname’s activation.
One of the following:"active"[]"pending"[]"active_redeploying"[]"moved"[]"pending_deletion"[]"deleted"[]"pending_blocked"[]"pending_migration"[]"pending_provisioned"[]"test_pending"[]"test_active"[]"test_active_apex"[]"test_blocked"[]"test_failed"[]"provisioned"[]"blocked"[][]verification_errors: optional array of string
These are errors that were encountered while trying to activate a hostname.
[][]DCVMethod = "http" or "txt" or "email"
Domain control validation (DCV) method used for this hostname.
One of the following:"http"[]"txt"[]"email"[][]DomainValidationType = "dv"
Level of validation to be used for this hostname. Domain validation (dv) must be used.
[]CustomHostnameListResponse  { id, hostname, created_at, 8 more } id: string
Identifier.
maxLength32[]hostname: string
The custom hostname that will point to your hostname via CNAME.
maxLength255[]created_at: optional string
This is the time the hostname was created.
formatdate-time[]custom_metadata: optional map[string]
Unique key/value metadata for this hostname. These are per-hostname (customer) settings.
[]custom_origin_server: optional string
a valid hostname that’s been added to your DNS zone as an A, AAAA, or CNAME record.
[]custom_origin_sni: optional string
A hostname that will be sent to your custom origin server as SNI for TLS handshake. This can be a valid subdomain of the zone or custom origin server name or the string ‘:request_host_header:’ which will cause the host header in the request to be used as SNI. Not configurable with default/fallback origin server.
[]ownership_verification: optional  { name, type, value }
This is a record which can be placed to activate a hostname.
name: optional string
DNS Name for record.
[]type: optional "txt"
DNS Record type.
[]value: optional string
Content for the record.
[][]ownership_verification_http: optional  { http_body, http_url }
This presents the token to be served by the given http url to activate a hostname.
http_body: optional string
Token to be served.
[]http_url: optional string
The HTTP URL that will be checked during custom hostname verification and where the customer should host the token.
[][]ssl: optional  { id, bundle_method, certificate_authority, 17 more } id: optional string
Custom hostname SSL identifier tag.
maxLength36minLength36[]bundle_method: optional [BundleMethod]
A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it.
[]certificate_authority: optional [CertificateCA]
The Certificate Authority that will issue the certificate
[]custom_certificate: optional string
If a custom uploaded certificate is used.
[]custom_csr_id: optional string
The identifier for the Custom CSR that was used.
[]custom_key: optional string
The key for a custom uploaded certificate.
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
[][]expires_on: optional string
The time the custom certificate expires on.
formatdate-time[]hosts: optional array of string
A list of Hostnames on a custom uploaded certificate.
[]issuer: optional string
The issuer on a custom uploaded certificate.
[]method: optional [DCVMethod]
Domain control validation (DCV) method used for this hostname.
[]serial_number: optional string
The serial number on a custom uploaded certificate.
[]settings: optional  { ciphers, early_hints, http2, 2 more } ciphers: optional array of string
An allowlist of ciphers for TLS termination. These ciphers must be in the BoringSSL format.
[]early_hints: optional "on" or "off"
Whether or not Early Hints is enabled.
One of the following:"on"[]"off"[][]http2: optional "on" or "off"
Whether or not HTTP2 is enabled.
One of the following:"on"[]"off"[][]min_tls_version: optional "1.0" or "1.1" or "1.2" or "1.3"
The minimum TLS version supported.
One of the following:"1.0"[]"1.1"[]"1.2"[]"1.3"[][]tls_1_3: optional "on" or "off"
Whether or not TLS 1.3 is enabled.
One of the following:"on"[]"off"[][][]signature: optional string
The signature on a custom uploaded certificate.
[]status: optional "initializing" or "pending_validation" or "deleted" or 18 more
Status of the hostname’s SSL certificates.
One of the following:"initializing"[]"pending_validation"[]"deleted"[]"pending_issuance"[]"pending_deployment"[]"pending_deletion"[]"pending_expiration"[]"expired"[]"active"[]"initializing_timed_out"[]"validation_timed_out"[]"issuance_timed_out"[]"deployment_timed_out"[]"deletion_timed_out"[]"pending_cleanup"[]"staging_deployment"[]"staging_active"[]"deactivating"[]"inactive"[]"backup_issued"[]"holding_deployment"[][]type: optional [DomainValidationType]
Level of validation to be used for this hostname. Domain validation (dv) must be used.
[]uploaded_on: optional string
The time the custom certificate was uploaded.
formatdate-time[]validation_errors: optional array of  { message }
Domain validation errors that have been received by the certificate authority (CA).
message: optional string
A domain validation error.
[][]validation_records: optional array of  { cname, cname_target, emails, 5 more } cname: optional string
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
[][]wildcard: optional boolean
Indicates whether the certificate covers a wildcard.
[][]status: optional "active" or "pending" or "active_redeploying" or 13 more
Status of the hostname’s activation.
One of the following:"active"[]"pending"[]"active_redeploying"[]"moved"[]"pending_deletion"[]"deleted"[]"pending_blocked"[]"pending_migration"[]"pending_provisioned"[]"test_pending"[]"test_active"[]"test_active_apex"[]"test_blocked"[]"test_failed"[]"provisioned"[]"blocked"[][]verification_errors: optional array of string
These are errors that were encountered while trying to activate a hostname.
[][]CustomHostnameGetResponse  { id, hostname, created_at, 8 more } id: string
Identifier.
maxLength32[]hostname: string
The custom hostname that will point to your hostname via CNAME.
maxLength255[]created_at: optional string
This is the time the hostname was created.
formatdate-time[]custom_metadata: optional map[string]
Unique key/value metadata for this hostname. These are per-hostname (customer) settings.
[]custom_origin_server: optional string
a valid hostname that’s been added to your DNS zone as an A, AAAA, or CNAME record.
[]custom_origin_sni: optional string
A hostname that will be sent to your custom origin server as SNI for TLS handshake. This can be a valid subdomain of the zone or custom origin server name or the string ‘:request_host_header:’ which will cause the host header in the request to be used as SNI. Not configurable with default/fallback origin server.
[]ownership_verification: optional  { name, type, value }
This is a record which can be placed to activate a hostname.
name: optional string
DNS Name for record.
[]type: optional "txt"
DNS Record type.
[]value: optional string
Content for the record.
[][]ownership_verification_http: optional  { http_body, http_url }
This presents the token to be served by the given http url to activate a hostname.
http_body: optional string
Token to be served.
[]http_url: optional string
The HTTP URL that will be checked during custom hostname verification and where the customer should host the token.
[][]ssl: optional  { id, bundle_method, certificate_authority, 17 more } id: optional string
Custom hostname SSL identifier tag.
maxLength36minLength36[]bundle_method: optional [BundleMethod]
A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it.
[]certificate_authority: optional [CertificateCA]
The Certificate Authority that will issue the certificate
[]custom_certificate: optional string
If a custom uploaded certificate is used.
[]custom_csr_id: optional string
The identifier for the Custom CSR that was used.
[]custom_key: optional string
The key for a custom uploaded certificate.
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
[][]expires_on: optional string
The time the custom certificate expires on.
formatdate-time[]hosts: optional array of string
A list of Hostnames on a custom uploaded certificate.
[]issuer: optional string
The issuer on a custom uploaded certificate.
[]method: optional [DCVMethod]
Domain control validation (DCV) method used for this hostname.
[]serial_number: optional string
The serial number on a custom uploaded certificate.
[]settings: optional  { ciphers, early_hints, http2, 2 more } ciphers: optional array of string
An allowlist of ciphers for TLS termination. These ciphers must be in the BoringSSL format.
[]early_hints: optional "on" or "off"
Whether or not Early Hints is enabled.
One of the following:"on"[]"off"[][]http2: optional "on" or "off"
Whether or not HTTP2 is enabled.
One of the following:"on"[]"off"[][]min_tls_version: optional "1.0" or "1.1" or "1.2" or "1.3"
The minimum TLS version supported.
One of the following:"1.0"[]"1.1"[]"1.2"[]"1.3"[][]tls_1_3: optional "on" or "off"
Whether or not TLS 1.3 is enabled.
One of the following:"on"[]"off"[][][]signature: optional string
The signature on a custom uploaded certificate.
[]status: optional "initializing" or "pending_validation" or "deleted" or 18 more
Status of the hostname’s SSL certificates.
One of the following:"initializing"[]"pending_validation"[]"deleted"[]"pending_issuance"[]"pending_deployment"[]"pending_deletion"[]"pending_expiration"[]"expired"[]"active"[]"initializing_timed_out"[]"validation_timed_out"[]"issuance_timed_out"[]"deployment_timed_out"[]"deletion_timed_out"[]"pending_cleanup"[]"staging_deployment"[]"staging_active"[]"deactivating"[]"inactive"[]"backup_issued"[]"holding_deployment"[][]type: optional [DomainValidationType]
Level of validation to be used for this hostname. Domain validation (dv) must be used.
[]uploaded_on: optional string
The time the custom certificate was uploaded.
formatdate-time[]validation_errors: optional array of  { message }
Domain validation errors that have been received by the certificate authority (CA).
message: optional string
A domain validation error.
[][]validation_records: optional array of  { cname, cname_target, emails, 5 more } cname: optional string
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
[][]wildcard: optional boolean
Indicates whether the certificate covers a wildcard.
[][]status: optional "active" or "pending" or "active_redeploying" or 13 more
Status of the hostname’s activation.
One of the following:"active"[]"pending"[]"active_redeploying"[]"moved"[]"pending_deletion"[]"deleted"[]"pending_blocked"[]"pending_migration"[]"pending_provisioned"[]"test_pending"[]"test_active"[]"test_active_apex"[]"test_blocked"[]"test_failed"[]"provisioned"[]"blocked"[][]verification_errors: optional array of string
These are errors that were encountered while trying to activate a hostname.
[][]CustomHostnameCreateResponse  { id, hostname, created_at, 8 more } id: string
Identifier.
maxLength32[]hostname: string
The custom hostname that will point to your hostname via CNAME.
maxLength255[]created_at: optional string
This is the time the hostname was created.
formatdate-time[]custom_metadata: optional map[string]
Unique key/value metadata for this hostname. These are per-hostname (customer) settings.
[]custom_origin_server: optional string
a valid hostname that’s been added to your DNS zone as an A, AAAA, or CNAME record.
[]custom_origin_sni: optional string
A hostname that will be sent to your custom origin server as SNI for TLS handshake. This can be a valid subdomain of the zone or custom origin server name or the string ‘:request_host_header:’ which will cause the host header in the request to be used as SNI. Not configurable with default/fallback origin server.
[]ownership_verification: optional  { name, type, value }
This is a record which can be placed to activate a hostname.
name: optional string
DNS Name for record.
[]type: optional "txt"
DNS Record type.
[]value: optional string
Content for the record.
[][]ownership_verification_http: optional  { http_body, http_url }
This presents the token to be served by the given http url to activate a hostname.
http_body: optional string
Token to be served.
[]http_url: optional string
The HTTP URL that will be checked during custom hostname verification and where the customer should host the token.
[][]ssl: optional  { id, bundle_method, certificate_authority, 17 more } id: optional string
Custom hostname SSL identifier tag.
maxLength36minLength36[]bundle_method: optional [BundleMethod]
A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it.
[]certificate_authority: optional [CertificateCA]
The Certificate Authority that will issue the certificate
[]custom_certificate: optional string
If a custom uploaded certificate is used.
[]custom_csr_id: optional string
The identifier for the Custom CSR that was used.
[]custom_key: optional string
The key for a custom uploaded certificate.
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
[][]expires_on: optional string
The time the custom certificate expires on.
formatdate-time[]hosts: optional array of string
A list of Hostnames on a custom uploaded certificate.
[]issuer: optional string
The issuer on a custom uploaded certificate.
[]method: optional [DCVMethod]
Domain control validation (DCV) method used for this hostname.
[]serial_number: optional string
The serial number on a custom uploaded certificate.
[]settings: optional  { ciphers, early_hints, http2, 2 more } ciphers: optional array of string
An allowlist of ciphers for TLS termination. These ciphers must be in the BoringSSL format.
[]early_hints: optional "on" or "off"
Whether or not Early Hints is enabled.
One of the following:"on"[]"off"[][]http2: optional "on" or "off"
Whether or not HTTP2 is enabled.
One of the following:"on"[]"off"[][]min_tls_version: optional "1.0" or "1.1" or "1.2" or "1.3"
The minimum TLS version supported.
One of the following:"1.0"[]"1.1"[]"1.2"[]"1.3"[][]tls_1_3: optional "on" or "off"
Whether or not TLS 1.3 is enabled.
One of the following:"on"[]"off"[][][]signature: optional string
The signature on a custom uploaded certificate.
[]status: optional "initializing" or "pending_validation" or "deleted" or 18 more
Status of the hostname’s SSL certificates.
One of the following:"initializing"[]"pending_validation"[]"deleted"[]"pending_issuance"[]"pending_deployment"[]"pending_deletion"[]"pending_expiration"[]"expired"[]"active"[]"initializing_timed_out"[]"validation_timed_out"[]"issuance_timed_out"[]"deployment_timed_out"[]"deletion_timed_out"[]"pending_cleanup"[]"staging_deployment"[]"staging_active"[]"deactivating"[]"inactive"[]"backup_issued"[]"holding_deployment"[][]type: optional [DomainValidationType]
Level of validation to be used for this hostname. Domain validation (dv) must be used.
[]uploaded_on: optional string
The time the custom certificate was uploaded.
formatdate-time[]validation_errors: optional array of  { message }
Domain validation errors that have been received by the certificate authority (CA).
message: optional string
A domain validation error.
[][]validation_records: optional array of  { cname, cname_target, emails, 5 more } cname: optional string
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
[][]wildcard: optional boolean
Indicates whether the certificate covers a wildcard.
[][]status: optional "active" or "pending" or "active_redeploying" or 13 more
Status of the hostname’s activation.
One of the following:"active"[]"pending"[]"active_redeploying"[]"moved"[]"pending_deletion"[]"deleted"[]"pending_blocked"[]"pending_migration"[]"pending_provisioned"[]"test_pending"[]"test_active"[]"test_active_apex"[]"test_blocked"[]"test_failed"[]"provisioned"[]"blocked"[][]verification_errors: optional array of string
These are errors that were encountered while trying to activate a hostname.
[][]CustomHostnameEditResponse  { id, hostname, created_at, 8 more } id: string
Identifier.
maxLength32[]hostname: string
The custom hostname that will point to your hostname via CNAME.
maxLength255[]created_at: optional string
This is the time the hostname was created.
formatdate-time[]custom_metadata: optional map[string]
Unique key/value metadata for this hostname. These are per-hostname (customer) settings.
[]custom_origin_server: optional string
a valid hostname that’s been added to your DNS zone as an A, AAAA, or CNAME record.
[]custom_origin_sni: optional string
A hostname that will be sent to your custom origin server as SNI for TLS handshake. This can be a valid subdomain of the zone or custom origin server name or the string ‘:request_host_header:’ which will cause the host header in the request to be used as SNI. Not configurable with default/fallback origin server.
[]ownership_verification: optional  { name, type, value }
This is a record which can be placed to activate a hostname.
name: optional string
DNS Name for record.
[]type: optional "txt"
DNS Record type.
[]value: optional string
Content for the record.
[][]ownership_verification_http: optional  { http_body, http_url }
This presents the token to be served by the given http url to activate a hostname.
http_body: optional string
Token to be served.
[]http_url: optional string
The HTTP URL that will be checked during custom hostname verification and where the customer should host the token.
[][]ssl: optional  { id, bundle_method, certificate_authority, 17 more } id: optional string
Custom hostname SSL identifier tag.
maxLength36minLength36[]bundle_method: optional [BundleMethod]
A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it.
[]certificate_authority: optional [CertificateCA]
The Certificate Authority that will issue the certificate
[]custom_certificate: optional string
If a custom uploaded certificate is used.
[]custom_csr_id: optional string
The identifier for the Custom CSR that was used.
[]custom_key: optional string
The key for a custom uploaded certificate.
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
[][]expires_on: optional string
The time the custom certificate expires on.
formatdate-time[]hosts: optional array of string
A list of Hostnames on a custom uploaded certificate.
[]issuer: optional string
The issuer on a custom uploaded certificate.
[]method: optional [DCVMethod]
Domain control validation (DCV) method used for this hostname.
[]serial_number: optional string
The serial number on a custom uploaded certificate.
[]settings: optional  { ciphers, early_hints, http2, 2 more } ciphers: optional array of string
An allowlist of ciphers for TLS termination. These ciphers must be in the BoringSSL format.
[]early_hints: optional "on" or "off"
Whether or not Early Hints is enabled.
One of the following:"on"[]"off"[][]http2: optional "on" or "off"
Whether or not HTTP2 is enabled.
One of the following:"on"[]"off"[][]min_tls_version: optional "1.0" or "1.1" or "1.2" or "1.3"
The minimum TLS version supported.
One of the following:"1.0"[]"1.1"[]"1.2"[]"1.3"[][]tls_1_3: optional "on" or "off"
Whether or not TLS 1.3 is enabled.
One of the following:"on"[]"off"[][][]signature: optional string
The signature on a custom uploaded certificate.
[]status: optional "initializing" or "pending_validation" or "deleted" or 18 more
Status of the hostname’s SSL certificates.
One of the following:"initializing"[]"pending_validation"[]"deleted"[]"pending_issuance"[]"pending_deployment"[]"pending_deletion"[]"pending_expiration"[]"expired"[]"active"[]"initializing_timed_out"[]"validation_timed_out"[]"issuance_timed_out"[]"deployment_timed_out"[]"deletion_timed_out"[]"pending_cleanup"[]"staging_deployment"[]"staging_active"[]"deactivating"[]"inactive"[]"backup_issued"[]"holding_deployment"[][]type: optional [DomainValidationType]
Level of validation to be used for this hostname. Domain validation (dv) must be used.
[]uploaded_on: optional string
The time the custom certificate was uploaded.
formatdate-time[]validation_errors: optional array of  { message }
Domain validation errors that have been received by the certificate authority (CA).
message: optional string
A domain validation error.
[][]validation_records: optional array of  { cname, cname_target, emails, 5 more } cname: optional string
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
[][]wildcard: optional boolean
Indicates whether the certificate covers a wildcard.
[][]status: optional "active" or "pending" or "active_redeploying" or 13 more
Status of the hostname’s activation.
One of the following:"active"[]"pending"[]"active_redeploying"[]"moved"[]"pending_deletion"[]"deleted"[]"pending_blocked"[]"pending_migration"[]"pending_provisioned"[]"test_pending"[]"test_active"[]"test_active_apex"[]"test_blocked"[]"test_failed"[]"provisioned"[]"blocked"[][]verification_errors: optional array of string
These are errors that were encountered while trying to activate a hostname.
[][]CustomHostnameDeleteResponse  { id } id: optional string
Identifier.
maxLength32[][]
#### Custom HostnamesFallback Origin

##### [Get Fallback Origin for Custom Hostnames]
GET/zones/{zone_id}/custom_hostnames/fallback_origin
##### [Update Fallback Origin for Custom Hostnames]
PUT/zones/{zone_id}/custom_hostnames/fallback_origin
##### [Delete Fallback Origin for Custom Hostnames]
DELETE/zones/{zone_id}/custom_hostnames/fallback_origin
##### ModelsExpand Collapse
FallbackOriginGetResponse  { created_at, errors, origin, 2 more } created_at: optional string
This is the time the fallback origin was created.
formatdate-time[]errors: optional array of string
These are errors that were encountered while trying to activate a fallback origin.
[]origin: optional string
Your origin hostname that requests to your custom hostnames will be sent to.
maxLength255[]status: optional "initializing" or "pending_deployment" or "pending_deletion" or 3 more
Status of the fallback origin’s activation.
One of the following:"initializing"[]"pending_deployment"[]"pending_deletion"[]"active"[]"deployment_timed_out"[]"deletion_timed_out"[][]updated_at: optional string
This is the time the fallback origin was updated.
formatdate-time[][]FallbackOriginUpdateResponse  { created_at, errors, origin, 2 more } created_at: optional string
This is the time the fallback origin was created.
formatdate-time[]errors: optional array of string
These are errors that were encountered while trying to activate a fallback origin.
[]origin: optional string
Your origin hostname that requests to your custom hostnames will be sent to.
maxLength255[]status: optional "initializing" or "pending_deployment" or "pending_deletion" or 3 more
Status of the fallback origin’s activation.
One of the following:"initializing"[]"pending_deployment"[]"pending_deletion"[]"active"[]"deployment_timed_out"[]"deletion_timed_out"[][]updated_at: optional string
This is the time the fallback origin was updated.
formatdate-time[][]FallbackOriginDeleteResponse  { created_at, errors, origin, 2 more } created_at: optional string
This is the time the fallback origin was created.
formatdate-time[]errors: optional array of string
These are errors that were encountered while trying to activate a fallback origin.
[]origin: optional string
Your origin hostname that requests to your custom hostnames will be sent to.
maxLength255[]status: optional "initializing" or "pending_deployment" or "pending_deletion" or 3 more
Status of the fallback origin’s activation.
One of the following:"initializing"[]"pending_deployment"[]"pending_deletion"[]"active"[]"deployment_timed_out"[]"deletion_timed_out"[][]updated_at: optional string
This is the time the fallback origin was updated.
formatdate-time[][]
#### Custom HostnamesCertificate Pack

#### Custom HostnamesCertificate PackCertificates

##### [Replace Custom Certificate and Custom Key In Custom Hostname]
PUT/zones/{zone_id}/custom_hostnames/{custom_hostname_id}/certificate_pack/{certificate_pack_id}/certificates/{certificate_id}
##### [Delete Single Certificate And Key For Custom Hostname]
DELETE/zones/{zone_id}/custom_hostnames/{custom_hostname_id}/certificate_pack/{certificate_pack_id}/certificates/{certificate_id}
##### ModelsExpand Collapse
CertificateUpdateResponse  { id, hostname, created_at, 8 more } id: string
Identifier.
maxLength32[]hostname: string
The custom hostname that will point to your hostname via CNAME.
maxLength255[]created_at: optional string
This is the time the hostname was created.
formatdate-time[]custom_metadata: optional map[string]
Unique key/value metadata for this hostname. These are per-hostname (customer) settings.
[]custom_origin_server: optional string
a valid hostname that’s been added to your DNS zone as an A, AAAA, or CNAME record.
[]custom_origin_sni: optional string
A hostname that will be sent to your custom origin server as SNI for TLS handshake. This can be a valid subdomain of the zone or custom origin server name or the string ‘:request_host_header:’ which will cause the host header in the request to be used as SNI. Not configurable with default/fallback origin server.
[]ownership_verification: optional  { name, type, value }
This is a record which can be placed to activate a hostname.
name: optional string
DNS Name for record.
[]type: optional "txt"
DNS Record type.
[]value: optional string
Content for the record.
[][]ownership_verification_http: optional  { http_body, http_url }
This presents the token to be served by the given http url to activate a hostname.
http_body: optional string
Token to be served.
[]http_url: optional string
The HTTP URL that will be checked during custom hostname verification and where the customer should host the token.
[][]ssl: optional  { id, bundle_method, certificate_authority, 17 more } id: optional string
Custom hostname SSL identifier tag.
maxLength36minLength36[]bundle_method: optional [BundleMethod]
A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it.
[]certificate_authority: optional [CertificateCA]
The Certificate Authority that will issue the certificate
[]custom_certificate: optional string
If a custom uploaded certificate is used.
[]custom_csr_id: optional string
The identifier for the Custom CSR that was used.
[]custom_key: optional string
The key for a custom uploaded certificate.
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
[][]expires_on: optional string
The time the custom certificate expires on.
formatdate-time[]hosts: optional array of string
A list of Hostnames on a custom uploaded certificate.
[]issuer: optional string
The issuer on a custom uploaded certificate.
[]method: optional [DCVMethod]
Domain control validation (DCV) method used for this hostname.
[]serial_number: optional string
The serial number on a custom uploaded certificate.
[]settings: optional  { ciphers, early_hints, http2, 2 more } ciphers: optional array of string
An allowlist of ciphers for TLS termination. These ciphers must be in the BoringSSL format.
[]early_hints: optional "on" or "off"
Whether or not Early Hints is enabled.
One of the following:"on"[]"off"[][]http2: optional "on" or "off"
Whether or not HTTP2 is enabled.
One of the following:"on"[]"off"[][]min_tls_version: optional "1.0" or "1.1" or "1.2" or "1.3"
The minimum TLS version supported.
One of the following:"1.0"[]"1.1"[]"1.2"[]"1.3"[][]tls_1_3: optional "on" or "off"
Whether or not TLS 1.3 is enabled.
One of the following:"on"[]"off"[][][]signature: optional string
The signature on a custom uploaded certificate.
[]status: optional "initializing" or "pending_validation" or "deleted" or 18 more
Status of the hostname’s SSL certificates.
One of the following:"initializing"[]"pending_validation"[]"deleted"[]"pending_issuance"[]"pending_deployment"[]"pending_deletion"[]"pending_expiration"[]"expired"[]"active"[]"initializing_timed_out"[]"validation_timed_out"[]"issuance_timed_out"[]"deployment_timed_out"[]"deletion_timed_out"[]"pending_cleanup"[]"staging_deployment"[]"staging_active"[]"deactivating"[]"inactive"[]"backup_issued"[]"holding_deployment"[][]type: optional [DomainValidationType]
Level of validation to be used for this hostname. Domain validation (dv) must be used.
[]uploaded_on: optional string
The time the custom certificate was uploaded.
formatdate-time[]validation_errors: optional array of  { message }
Domain validation errors that have been received by the certificate authority (CA).
message: optional string
A domain validation error.
[][]validation_records: optional array of  { cname, cname_target, emails, 5 more } cname: optional string
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
[][]wildcard: optional boolean
Indicates whether the certificate covers a wildcard.
[][]status: optional "active" or "pending" or "active_redeploying" or 13 more
Status of the hostname’s activation.
One of the following:"active"[]"pending"[]"active_redeploying"[]"moved"[]"pending_deletion"[]"deleted"[]"pending_blocked"[]"pending_migration"[]"pending_provisioned"[]"test_pending"[]"test_active"[]"test_active_apex"[]"test_blocked"[]"test_failed"[]"provisioned"[]"blocked"[][]verification_errors: optional array of string
These are errors that were encountered while trying to activate a hostname.
[][]CertificateDeleteResponse  { id } id: optional string
Identifier.
maxLength32[][]