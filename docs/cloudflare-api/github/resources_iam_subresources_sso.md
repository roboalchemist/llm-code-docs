# SSO | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/iam/subresources/sso

[API Reference][IAM]
# SSO

##### [Get all SSO connectors]
GET/accounts/{account_id}/sso_connectors
##### [Get single SSO connector]
GET/accounts/{account_id}/sso_connectors/{sso_connector_id}
##### [Initialize new SSO connector]
POST/accounts/{account_id}/sso_connectors
##### [Update SSO connector state]
PATCH/accounts/{account_id}/sso_connectors/{sso_connector_id}
##### [Delete SSO connector]
DELETE/accounts/{account_id}/sso_connectors/{sso_connector_id}
##### [Begin SSO connector verification]
POST/accounts/{account_id}/sso_connectors/{sso_connector_id}/begin_verification
##### ModelsExpand Collapse
SSOListResponse  { id, created_on, email_domain, 4 more } id: optional string
SSO Connector identifier tag.
maxLength32minLength32[]created_on: optional string
Timestamp for the creation of the SSO connector
formatdate-time[]email_domain: optional string[]enabled: optional boolean[]updated_on: optional string
Timestamp for the last update of the SSO connector
formatdate-time[]use_fedramp_language: optional boolean
Controls the display of FedRAMP language to the user during SSO login
[]verification: optional  { code, status } code: optional string
DNS verification code. Add this entire string to the DNS TXT record of the email domain to validate ownership.
[]status: optional "awaiting" or "pending" or "failed" or "verified"
The status of the verification code from the verification process.
One of the following:"awaiting"[]"pending"[]"failed"[]"verified"[][][][]SSOGetResponse  { id, created_on, email_domain, 4 more } id: optional string
SSO Connector identifier tag.
maxLength32minLength32[]created_on: optional string
Timestamp for the creation of the SSO connector
formatdate-time[]email_domain: optional string[]enabled: optional boolean[]updated_on: optional string
Timestamp for the last update of the SSO connector
formatdate-time[]use_fedramp_language: optional boolean
Controls the display of FedRAMP language to the user during SSO login
[]verification: optional  { code, status } code: optional string
DNS verification code. Add this entire string to the DNS TXT record of the email domain to validate ownership.
[]status: optional "awaiting" or "pending" or "failed" or "verified"
The status of the verification code from the verification process.
One of the following:"awaiting"[]"pending"[]"failed"[]"verified"[][][][]SSOCreateResponse  { id, created_on, email_domain, 4 more } id: optional string
SSO Connector identifier tag.
maxLength32minLength32[]created_on: optional string
Timestamp for the creation of the SSO connector
formatdate-time[]email_domain: optional string[]enabled: optional boolean[]updated_on: optional string
Timestamp for the last update of the SSO connector
formatdate-time[]use_fedramp_language: optional boolean
Controls the display of FedRAMP language to the user during SSO login
[]verification: optional  { code, status } code: optional string
DNS verification code. Add this entire string to the DNS TXT record of the email domain to validate ownership.
[]status: optional "awaiting" or "pending" or "failed" or "verified"
The status of the verification code from the verification process.
One of the following:"awaiting"[]"pending"[]"failed"[]"verified"[][][][]SSOUpdateResponse  { id, created_on, email_domain, 4 more } id: optional string
SSO Connector identifier tag.
maxLength32minLength32[]created_on: optional string
Timestamp for the creation of the SSO connector
formatdate-time[]email_domain: optional string[]enabled: optional boolean[]updated_on: optional string
Timestamp for the last update of the SSO connector
formatdate-time[]use_fedramp_language: optional boolean
Controls the display of FedRAMP language to the user during SSO login
[]verification: optional  { code, status } code: optional string
DNS verification code. Add this entire string to the DNS TXT record of the email domain to validate ownership.
[]status: optional "awaiting" or "pending" or "failed" or "verified"
The status of the verification code from the verification process.
One of the following:"awaiting"[]"pending"[]"failed"[]"verified"[][][][]SSODeleteResponse  { id } id: string
Identifier
maxLength32minLength32[][]SSOBeginVerificationResponse  { errors, messages, success } errors: array of  { code, message, documentation_url, source } code: numberminimum1000[]message: string[]documentation_url: optional string[]source: optional  { pointer } pointer: optional string[][][]messages: array of  { code, message, documentation_url, source } code: numberminimum1000[]message: string[]documentation_url: optional string[]source: optional  { pointer } pointer: optional string[][][]success: true
Whether the API call was successful.
[][]