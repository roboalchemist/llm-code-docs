# Reports | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/email_security/subresources/phishguard/subresources/reports

[API Reference][Email Security][Phishguard]
# Reports

##### [Get `PhishGuard` reports]
GET/accounts/{account_id}/email-security/phishguard/reports
##### ModelsExpand Collapse
ReportListResponse  { id, content, created_at, 7 more } id: numberformatint32[]content: string[]created_at: stringformatdate-time[]disposition: "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]fields:  { to, ts, from, postfix_id } to: array of string[]ts: stringformatdate-time[]from: optional string[]postfix_id: optional string[][]priority: string[]title: string[]ts: stringformatdate-time[]updated_at: stringformatdate-time[]tags: optional array of  { category, value } category: string[]value: string[][][]