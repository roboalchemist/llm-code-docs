# Investigate | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/email_security/subresources/investigate

[API Reference][Email Security]
# Investigate

##### [Search email messages]
GET/accounts/{account_id}/email-security/investigate
##### [Get message details]
GET/accounts/{account_id}/email-security/investigate/{postfix_id}
##### ModelsExpand Collapse
InvestigateListResponse  { id, action_log, client_recipients, 28 more } id: string[]action_log: unknown[]client_recipients: array of string[]detection_reasons: array of string[]is_phish_submission: boolean[]is_quarantined: boolean[]postfix_id: string
The identifier of the message.
[]properties:  { allowlisted_pattern, allowlisted_pattern_type, blocklisted_message, 2 more } allowlisted_pattern: optional string[]allowlisted_pattern_type: optional "quarantine_release" or "acceptable_sender" or "allowed_sender" or 5 moreOne of the following:"quarantine_release"[]"acceptable_sender"[]"allowed_sender"[]"allowed_recipient"[]"domain_similarity"[]"domain_recency"[]"managed_acceptable_sender"[]"outbound_ndr"[][]blocklisted_message: optional boolean[]blocklisted_pattern: optional string[]whitelisted_pattern_type: optional "quarantine_release" or "acceptable_sender" or "allowed_sender" or 5 moreOne of the following:"quarantine_release"[]"acceptable_sender"[]"allowed_sender"[]"allowed_recipient"[]"domain_similarity"[]"domain_recency"[]"managed_acceptable_sender"[]"outbound_ndr"[][][]Deprecatedts: string
Deprecated, use `scanned_at` instead
[]alert_id: optional string[]delivery_mode: optional "DIRECT" or "BCC" or "JOURNAL" or 8 moreOne of the following:"DIRECT"[]"BCC"[]"JOURNAL"[]"REVIEW_SUBMISSION"[]"DMARC_UNVERIFIED"[]"DMARC_FAILURE_REPORT"[]"DMARC_AGGREGATE_REPORT"[]"THREAT_INTEL_SUBMISSION"[]"SIMULATION_SUBMISSION"[]"API"[]"RETRO_SCAN"[][]edf_hash: optional string[]envelope_from: optional string[]envelope_to: optional array of string[]final_disposition: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]findings: optional array of  { attachment, detail, detection, 6 more } attachment: optional string[]detail: optional string[]detection: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]field: optional string[]name: optional string[]portion: optional string[]reason: optional string[]score: optional numberformatdouble[]value: optional string[][]from: optional string[]from_name: optional string[]htmltext_structure_hash: optional string[]message_id: optional string[]post_delivery_operations: optional array of "PREVIEW" or "QUARANTINE_RELEASE" or "SUBMISSION" or "MOVE"One of the following:"PREVIEW"[]"QUARANTINE_RELEASE"[]"SUBMISSION"[]"MOVE"[][]postfix_id_outbound: optional string[]replyto: optional string[]scanned_at: optional stringformatdate-time[]sent_at: optional stringformatdate-time[]Deprecatedsent_date: optional string
Deprecated, use `sent_at` instead
[]subject: optional string[]threat_categories: optional array of string[]to: optional array of string[]to_name: optional array of string[]validation: optional  { comment, dkim, dmarc, spf } comment: optional string[]dkim: optional "pass" or "neutral" or "fail" or 2 moreOne of the following:"pass"[]"neutral"[]"fail"[]"error"[]"none"[][]dmarc: optional "pass" or "neutral" or "fail" or 2 moreOne of the following:"pass"[]"neutral"[]"fail"[]"error"[]"none"[][]spf: optional "pass" or "neutral" or "fail" or 2 moreOne of the following:"pass"[]"neutral"[]"fail"[]"error"[]"none"[][][][]InvestigateGetResponse  { id, action_log, client_recipients, 28 more } id: string[]action_log: unknown[]client_recipients: array of string[]detection_reasons: array of string[]is_phish_submission: boolean[]is_quarantined: boolean[]postfix_id: string
The identifier of the message.
[]properties:  { allowlisted_pattern, allowlisted_pattern_type, blocklisted_message, 2 more } allowlisted_pattern: optional string[]allowlisted_pattern_type: optional "quarantine_release" or "acceptable_sender" or "allowed_sender" or 5 moreOne of the following:"quarantine_release"[]"acceptable_sender"[]"allowed_sender"[]"allowed_recipient"[]"domain_similarity"[]"domain_recency"[]"managed_acceptable_sender"[]"outbound_ndr"[][]blocklisted_message: optional boolean[]blocklisted_pattern: optional string[]whitelisted_pattern_type: optional "quarantine_release" or "acceptable_sender" or "allowed_sender" or 5 moreOne of the following:"quarantine_release"[]"acceptable_sender"[]"allowed_sender"[]"allowed_recipient"[]"domain_similarity"[]"domain_recency"[]"managed_acceptable_sender"[]"outbound_ndr"[][][]Deprecatedts: string
Deprecated, use `scanned_at` instead
[]alert_id: optional string[]delivery_mode: optional "DIRECT" or "BCC" or "JOURNAL" or 8 moreOne of the following:"DIRECT"[]"BCC"[]"JOURNAL"[]"REVIEW_SUBMISSION"[]"DMARC_UNVERIFIED"[]"DMARC_FAILURE_REPORT"[]"DMARC_AGGREGATE_REPORT"[]"THREAT_INTEL_SUBMISSION"[]"SIMULATION_SUBMISSION"[]"API"[]"RETRO_SCAN"[][]edf_hash: optional string[]envelope_from: optional string[]envelope_to: optional array of string[]final_disposition: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]findings: optional array of  { attachment, detail, detection, 6 more } attachment: optional string[]detail: optional string[]detection: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]field: optional string[]name: optional string[]portion: optional string[]reason: optional string[]score: optional numberformatdouble[]value: optional string[][]from: optional string[]from_name: optional string[]htmltext_structure_hash: optional string[]message_id: optional string[]post_delivery_operations: optional array of "PREVIEW" or "QUARANTINE_RELEASE" or "SUBMISSION" or "MOVE"One of the following:"PREVIEW"[]"QUARANTINE_RELEASE"[]"SUBMISSION"[]"MOVE"[][]postfix_id_outbound: optional string[]replyto: optional string[]scanned_at: optional stringformatdate-time[]sent_at: optional stringformatdate-time[]Deprecatedsent_date: optional string
Deprecated, use `sent_at` instead
[]subject: optional string[]threat_categories: optional array of string[]to: optional array of string[]to_name: optional array of string[]validation: optional  { comment, dkim, dmarc, spf } comment: optional string[]dkim: optional "pass" or "neutral" or "fail" or 2 moreOne of the following:"pass"[]"neutral"[]"fail"[]"error"[]"none"[][]dmarc: optional "pass" or "neutral" or "fail" or 2 moreOne of the following:"pass"[]"neutral"[]"fail"[]"error"[]"none"[][]spf: optional "pass" or "neutral" or "fail" or 2 moreOne of the following:"pass"[]"neutral"[]"fail"[]"error"[]"none"[][][][]
#### InvestigateDetections

##### [Get message detection details]
GET/accounts/{account_id}/email-security/investigate/{postfix_id}/detections
##### ModelsExpand Collapse
DetectionGetResponse  { action, attachments, headers, 5 more } action: string[]attachments: array of  { size, content_type, detection, 2 more } size: numberminimum0[]content_type: optional string[]detection: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]encrypted: optional boolean[]name: optional string[][]headers: array of  { name, value } name: string[]value: string[][]links: array of  { href, text } href: string[]text: optional string[][]sender_info:  { as_name, as_number, geo, 2 more } as_name: optional string
The name of the autonomous system.
[]as_number: optional number
The number of the autonomous system.
formatint64[]geo: optional string[]ip: optional string[]pld: optional string[][]threat_categories: array of  { id, description, name } id: numberformatint64[]description: optional string[]name: optional string[][]validation:  { comment, dkim, dmarc, spf } comment: optional string[]dkim: optional "pass" or "neutral" or "fail" or 2 moreOne of the following:"pass"[]"neutral"[]"fail"[]"error"[]"none"[][]dmarc: optional "pass" or "neutral" or "fail" or 2 moreOne of the following:"pass"[]"neutral"[]"fail"[]"error"[]"none"[][]spf: optional "pass" or "neutral" or "fail" or 2 moreOne of the following:"pass"[]"neutral"[]"fail"[]"error"[]"none"[][][]final_disposition: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][][]
#### InvestigatePreview

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
#### InvestigateRaw

##### [Get raw email content]
GET/accounts/{account_id}/email-security/investigate/{postfix_id}/raw
##### ModelsExpand Collapse
RawGetResponse  { raw } raw: string
A UTF-8 encoded eml file of the email.
[][]
#### InvestigateTrace

##### [Get email trace]
GET/accounts/{account_id}/email-security/investigate/{postfix_id}/trace
##### ModelsExpand Collapse
TraceGetResponse  { inbound, outbound } inbound:  { lines, pending } lines: optional array of  { lineno, message, ts } lineno: numberformatint64[]message: string[]ts: stringformatdate-time[][]pending: optional boolean[][]outbound:  { lines, pending } lines: optional array of  { lineno, message, ts } lineno: numberformatint64[]message: string[]ts: stringformatdate-time[][]pending: optional boolean[][][]
#### InvestigateMove

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
#### InvestigateReclassify

##### [Change email classification]
POST/accounts/{account_id}/email-security/investigate/{postfix_id}/reclassify
##### ModelsExpand Collapse
ReclassifyCreateResponse = unknown[]
#### InvestigateRelease

##### [Release messages from quarantine]
POST/accounts/{account_id}/email-security/investigate/release
##### ModelsExpand Collapse
ReleaseBulkResponse  { id, postfix_id, delivered, 2 more } id: string[]postfix_id: string
The identifier of the message.
[]delivered: optional array of string[]failed: optional array of string[]undelivered: optional array of string[][]