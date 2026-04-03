# Preview | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/preview

[API Reference][Email Security][Investigate]
# Preview

##### [Get email preview]
GET/accounts/{account_id}/email-security/investigate/{postfix_id}/preview
##### [Preview for non-detection messages]
POST/accounts/{account_id}/email-security/investigate/preview
##### ModelsExpand Collapse
PreviewGetResponse  { screenshot } screenshot: string
A base64 encoded PNG image of the email.
[][]PreviewCreateResponse  { screenshot } screenshot: string
A base64 encoded PNG image of the email.
[][]