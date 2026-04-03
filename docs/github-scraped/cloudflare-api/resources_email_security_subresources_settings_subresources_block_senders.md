# Block Senders | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/block_senders

[API Reference][Email Security][Settings]
# Block Senders

##### [List blocked email senders]
GET/accounts/{account_id}/email-security/settings/block_senders
##### [Get a blocked email sender]
GET/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}
##### [Create a blocked email sender]
POST/accounts/{account_id}/email-security/settings/block_senders
##### [Update a blocked email sender]
PATCH/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}
##### [Delete a blocked email sender]
DELETE/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}
##### ModelsExpand Collapse
BlockSenderListResponse  { id, created_at, is_regex, 4 more } id: number
The unique identifier for the allow policy.
formatint32[]created_at: stringformatdate-time[]is_regex: boolean[]last_modified: stringformatdate-time[]pattern: stringmaxLength1024minLength1[]pattern_type: "EMAIL" or "DOMAIN" or "IP" or "UNKNOWN"One of the following:"EMAIL"[]"DOMAIN"[]"IP"[]"UNKNOWN"[][]comments: optional stringmaxLength1024[][]BlockSenderGetResponse  { id, created_at, is_regex, 4 more } id: number
The unique identifier for the allow policy.
formatint32[]created_at: stringformatdate-time[]is_regex: boolean[]last_modified: stringformatdate-time[]pattern: stringmaxLength1024minLength1[]pattern_type: "EMAIL" or "DOMAIN" or "IP" or "UNKNOWN"One of the following:"EMAIL"[]"DOMAIN"[]"IP"[]"UNKNOWN"[][]comments: optional stringmaxLength1024[][]BlockSenderCreateResponse  { id, created_at, is_regex, 4 more } id: number
The unique identifier for the allow policy.
formatint32[]created_at: stringformatdate-time[]is_regex: boolean[]last_modified: stringformatdate-time[]pattern: stringmaxLength1024minLength1[]pattern_type: "EMAIL" or "DOMAIN" or "IP" or "UNKNOWN"One of the following:"EMAIL"[]"DOMAIN"[]"IP"[]"UNKNOWN"[][]comments: optional stringmaxLength1024[][]BlockSenderEditResponse  { id, created_at, is_regex, 4 more } id: number
The unique identifier for the allow policy.
formatint32[]created_at: stringformatdate-time[]is_regex: boolean[]last_modified: stringformatdate-time[]pattern: stringmaxLength1024minLength1[]pattern_type: "EMAIL" or "DOMAIN" or "IP" or "UNKNOWN"One of the following:"EMAIL"[]"DOMAIN"[]"IP"[]"UNKNOWN"[][]comments: optional stringmaxLength1024[][]BlockSenderDeleteResponse  { id } id: number
The unique identifier for the allow policy.
formatint32[][]