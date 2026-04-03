# Trace | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/trace

[API Reference][Email Security][Investigate]
# Trace

##### [Get email trace]
GET/accounts/{account_id}/email-security/investigate/{postfix_id}/trace
##### ModelsExpand Collapse
TraceGetResponse  { inbound, outbound } inbound:  { lines, pending } lines: optional array of  { lineno, message, ts } lineno: numberformatint64[]message: string[]ts: stringformatdate-time[][]pending: optional boolean[][]outbound:  { lines, pending } lines: optional array of  { lineno, message, ts } lineno: numberformatint64[]message: string[]ts: stringformatdate-time[][]pending: optional boolean[][][]