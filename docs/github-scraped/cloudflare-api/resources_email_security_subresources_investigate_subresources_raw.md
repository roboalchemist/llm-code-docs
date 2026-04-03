# Raw | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/raw

[API Reference][Email Security][Investigate]
# Raw

##### [Get raw email content]
GET/accounts/{account_id}/email-security/investigate/{postfix_id}/raw
##### ModelsExpand Collapse
RawGetResponse  { raw } raw: string
A UTF-8 encoded eml file of the email.
[][]