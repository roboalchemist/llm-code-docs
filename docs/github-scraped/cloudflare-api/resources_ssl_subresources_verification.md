# Verification | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/ssl/subresources/verification

[API Reference][SSL]
# Verification

##### [SSL Verification Details]
GET/zones/{zone_id}/ssl/verification
##### [Edit SSL Certificate Pack Validation Method]
PATCH/zones/{zone_id}/ssl/verification/{certificate_pack_id}
##### ModelsExpand Collapse
Verification  { certificate_status, brand_check, cert_pack_uuid, 5 more } certificate_status: "initializing" or "authorizing" or "active" or 4 more
Current status of certificate.
One of the following:"initializing"[]"authorizing"[]"active"[]"expired"[]"issuing"[]"timing_out"[]"pending_deployment"[][]brand_check: optional boolean
Certificate Authority is manually reviewing the order.
[]cert_pack_uuid: optional string
Certificate Pack UUID.
[]signature: optional "ECDSAWithSHA256" or "SHA1WithRSA" or "SHA256WithRSA"
Certificate’s signature algorithm.
One of the following:"ECDSAWithSHA256"[]"SHA1WithRSA"[]"SHA256WithRSA"[][]validation_method: optional [ValidationMethod]
Validation method in use for a certificate pack order.
[]verification_info: optional  { record_name, record_target }
Certificate’s required verification information.
record_name: optional "record_name" or "http_url" or "cname" or "txt_name"
Name of CNAME record.
formathostnameOne of the following:"record_name"[]"http_url"[]"cname"[]"txt_name"[][]record_target: optional "record_value" or "http_body" or "cname_target" or "txt_value"
Target of CNAME record.
formathostnameOne of the following:"record_value"[]"http_body"[]"cname_target"[]"txt_value"[][][]verification_status: optional boolean
Status of the required verification information, omitted if verification status is unknown.
[]verification_type: optional "cname" or "meta tag"
Method of verification.
One of the following:"cname"[]"meta tag"[][][]VerificationGetResponse = array of [Verification] { certificate_status, brand_check, cert_pack_uuid, 5 more } certificate_status: "initializing" or "authorizing" or "active" or 4 more
Current status of certificate.
One of the following:"initializing"[]"authorizing"[]"active"[]"expired"[]"issuing"[]"timing_out"[]"pending_deployment"[][]brand_check: optional boolean
Certificate Authority is manually reviewing the order.
[]cert_pack_uuid: optional string
Certificate Pack UUID.
[]signature: optional "ECDSAWithSHA256" or "SHA1WithRSA" or "SHA256WithRSA"
Certificate’s signature algorithm.
One of the following:"ECDSAWithSHA256"[]"SHA1WithRSA"[]"SHA256WithRSA"[][]validation_method: optional [ValidationMethod]
Validation method in use for a certificate pack order.
[]verification_info: optional  { record_name, record_target }
Certificate’s required verification information.
record_name: optional "record_name" or "http_url" or "cname" or "txt_name"
Name of CNAME record.
formathostnameOne of the following:"record_name"[]"http_url"[]"cname"[]"txt_name"[][]record_target: optional "record_value" or "http_body" or "cname_target" or "txt_value"
Target of CNAME record.
formathostnameOne of the following:"record_value"[]"http_body"[]"cname_target"[]"txt_value"[][][]verification_status: optional boolean
Status of the required verification information, omitted if verification status is unknown.
[]verification_type: optional "cname" or "meta tag"
Method of verification.
One of the following:"cname"[]"meta tag"[][][]VerificationEditResponse  { status, validation_method } status: optional string
Result status.
[]validation_method: optional "http" or "cname" or "txt" or "email"
Desired validation method.
One of the following:"http"[]"cname"[]"txt"[]"email"[][][]