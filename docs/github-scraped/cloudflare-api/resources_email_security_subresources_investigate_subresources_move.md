# Move | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/move

[API Reference][Email Security][Investigate]
# Move

##### [Move a message]
POST/accounts/{account_id}/email-security/investigate/{postfix_id}/move
##### [Move multiple messages]
POST/accounts/{account_id}/email-security/investigate/move
##### ModelsExpand Collapse
MoveCreateResponse  { completed_timestamp, item_count, success, 6 more } Deprecatedcompleted_timestamp: string
Deprecated, use `completed_at` instead
formatdate-time[]Deprecateditem_count: numberformatint32[]success: boolean[]completed_at: optional stringformatdate-time[]destination: optional string[]message_id: optional string[]operation: optional string[]recipient: optional string[]status: optional string[][]MoveBulkResponse  { completed_timestamp, item_count, success, 6 more } Deprecatedcompleted_timestamp: string
Deprecated, use `completed_at` instead
formatdate-time[]Deprecateditem_count: numberformatint32[]success: boolean[]completed_at: optional stringformatdate-time[]destination: optional string[]message_id: optional string[]operation: optional string[]recipient: optional string[]status: optional string[][]