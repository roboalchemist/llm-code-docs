# Allow Policies | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/allow_policies

[API Reference][Email Security][Settings]
# Allow Policies

##### [List email allow policies]
GET/accounts/{account_id}/email-security/settings/allow_policies
##### [Get an email allow policy]
GET/accounts/{account_id}/email-security/settings/allow_policies/{policy_id}
##### [Create an email allow policy]
POST/accounts/{account_id}/email-security/settings/allow_policies
##### [Update an email allow policy]
PATCH/accounts/{account_id}/email-security/settings/allow_policies/{policy_id}
##### [Delete an email allow policy]
DELETE/accounts/{account_id}/email-security/settings/allow_policies/{policy_id}
##### ModelsExpand Collapse
AllowPolicyListResponse  { id, created_at, is_acceptable_sender, 11 more } id: number
The unique identifier for the allow policy.
formatint32[]created_at: stringformatdate-time[]is_acceptable_sender: boolean
Messages from this sender will be exempted from Spam, Spoof and Bulk dispositions.
Note: This will not exempt messages with Malicious or Suspicious dispositions.
[]is_exempt_recipient: boolean
Messages to this recipient will bypass all detections.
[]is_regex: boolean[]is_trusted_sender: boolean
Messages from this sender will bypass all detections and link following.
[]last_modified: stringformatdate-time[]pattern: stringmaxLength1024minLength1[]pattern_type: "EMAIL" or "DOMAIN" or "IP" or "UNKNOWN"One of the following:"EMAIL"[]"DOMAIN"[]"IP"[]"UNKNOWN"[][]verify_sender: boolean
Enforce DMARC, SPF or DKIM authentication.
When on, Email Security only honors policies that pass authentication.
[]comments: optional stringmaxLength1024[]Deprecatedis_recipient: optional boolean[]Deprecatedis_sender: optional boolean[]Deprecatedis_spoof: optional boolean[][]AllowPolicyGetResponse  { id, created_at, is_acceptable_sender, 11 more } id: number
The unique identifier for the allow policy.
formatint32[]created_at: stringformatdate-time[]is_acceptable_sender: boolean
Messages from this sender will be exempted from Spam, Spoof and Bulk dispositions.
Note: This will not exempt messages with Malicious or Suspicious dispositions.
[]is_exempt_recipient: boolean
Messages to this recipient will bypass all detections.
[]is_regex: boolean[]is_trusted_sender: boolean
Messages from this sender will bypass all detections and link following.
[]last_modified: stringformatdate-time[]pattern: stringmaxLength1024minLength1[]pattern_type: "EMAIL" or "DOMAIN" or "IP" or "UNKNOWN"One of the following:"EMAIL"[]"DOMAIN"[]"IP"[]"UNKNOWN"[][]verify_sender: boolean
Enforce DMARC, SPF or DKIM authentication.
When on, Email Security only honors policies that pass authentication.
[]comments: optional stringmaxLength1024[]Deprecatedis_recipient: optional boolean[]Deprecatedis_sender: optional boolean[]Deprecatedis_spoof: optional boolean[][]AllowPolicyCreateResponse  { id, created_at, is_acceptable_sender, 11 more } id: number
The unique identifier for the allow policy.
formatint32[]created_at: stringformatdate-time[]is_acceptable_sender: boolean
Messages from this sender will be exempted from Spam, Spoof and Bulk dispositions.
Note: This will not exempt messages with Malicious or Suspicious dispositions.
[]is_exempt_recipient: boolean
Messages to this recipient will bypass all detections.
[]is_regex: boolean[]is_trusted_sender: boolean
Messages from this sender will bypass all detections and link following.
[]last_modified: stringformatdate-time[]pattern: stringmaxLength1024minLength1[]pattern_type: "EMAIL" or "DOMAIN" or "IP" or "UNKNOWN"One of the following:"EMAIL"[]"DOMAIN"[]"IP"[]"UNKNOWN"[][]verify_sender: boolean
Enforce DMARC, SPF or DKIM authentication.
When on, Email Security only honors policies that pass authentication.
[]comments: optional stringmaxLength1024[]Deprecatedis_recipient: optional boolean[]Deprecatedis_sender: optional boolean[]Deprecatedis_spoof: optional boolean[][]AllowPolicyEditResponse  { id, created_at, is_acceptable_sender, 11 more } id: number
The unique identifier for the allow policy.
formatint32[]created_at: stringformatdate-time[]is_acceptable_sender: boolean
Messages from this sender will be exempted from Spam, Spoof and Bulk dispositions.
Note: This will not exempt messages with Malicious or Suspicious dispositions.
[]is_exempt_recipient: boolean
Messages to this recipient will bypass all detections.
[]is_regex: boolean[]is_trusted_sender: boolean
Messages from this sender will bypass all detections and link following.
[]last_modified: stringformatdate-time[]pattern: stringmaxLength1024minLength1[]pattern_type: "EMAIL" or "DOMAIN" or "IP" or "UNKNOWN"One of the following:"EMAIL"[]"DOMAIN"[]"IP"[]"UNKNOWN"[][]verify_sender: boolean
Enforce DMARC, SPF or DKIM authentication.
When on, Email Security only honors policies that pass authentication.
[]comments: optional stringmaxLength1024[]Deprecatedis_recipient: optional boolean[]Deprecatedis_sender: optional boolean[]Deprecatedis_spoof: optional boolean[][]AllowPolicyDeleteResponse  { id } id: number
The unique identifier for the allow policy.
formatint32[][]