# Release | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/release

[API Reference][Email Security][Investigate]
# Release

##### [Release messages from quarantine]
POST/accounts/{account_id}/email-security/investigate/release
##### ModelsExpand Collapse
ReleaseBulkResponse  { id, postfix_id, delivered, 2 more } id: string[]postfix_id: string
The identifier of the message.
[]delivered: optional array of string[]failed: optional array of string[]undelivered: optional array of string[][]