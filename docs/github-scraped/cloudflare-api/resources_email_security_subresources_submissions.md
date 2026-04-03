# Submissions | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/email_security/subresources/submissions

[API Reference][Email Security]
# Submissions

##### [Get reclassify submissions]
GET/accounts/{account_id}/email-security/submissions
##### ModelsExpand Collapse
SubmissionListResponse  { requested_ts, submission_id, customer_status, 15 more } Deprecatedrequested_ts: string
deprecated as of 2026-04-01, use `requested_at` instead.
formatdate-time[]submission_id: string[]customer_status: optional "escalated" or "reviewed" or "unreviewed"One of the following:"escalated"[]"reviewed"[]"unreviewed"[][]escalated_as: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]escalated_at: optional stringformatdate-time[]escalated_by: optional string[]escalated_submission_id: optional string[]original_disposition: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]original_edf_hash: optional string[]original_postfix_id: optional string[]outcome: optional string[]outcome_disposition: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]requested_at: optional stringformatdate-time[]requested_by: optional string[]requested_disposition: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]status: optional string[]subject: optional string[]type: optional string[][]