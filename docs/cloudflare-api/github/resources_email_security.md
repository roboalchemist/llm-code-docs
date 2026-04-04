# Email Security | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/email_security

[API Reference]
# Email Security

#### Email SecurityInvestigate

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
#### Email SecurityInvestigateDetections

##### [Get message detection details]
GET/accounts/{account_id}/email-security/investigate/{postfix_id}/detections
##### ModelsExpand Collapse
DetectionGetResponse  { action, attachments, headers, 5 more } action: string[]attachments: array of  { size, content_type, detection, 2 more } size: numberminimum0[]content_type: optional string[]detection: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]encrypted: optional boolean[]name: optional string[][]headers: array of  { name, value } name: string[]value: string[][]links: array of  { href, text } href: string[]text: optional string[][]sender_info:  { as_name, as_number, geo, 2 more } as_name: optional string
The name of the autonomous system.
[]as_number: optional number
The number of the autonomous system.
formatint64[]geo: optional string[]ip: optional string[]pld: optional string[][]threat_categories: array of  { id, description, name } id: numberformatint64[]description: optional string[]name: optional string[][]validation:  { comment, dkim, dmarc, spf } comment: optional string[]dkim: optional "pass" or "neutral" or "fail" or 2 moreOne of the following:"pass"[]"neutral"[]"fail"[]"error"[]"none"[][]dmarc: optional "pass" or "neutral" or "fail" or 2 moreOne of the following:"pass"[]"neutral"[]"fail"[]"error"[]"none"[][]spf: optional "pass" or "neutral" or "fail" or 2 moreOne of the following:"pass"[]"neutral"[]"fail"[]"error"[]"none"[][][]final_disposition: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][][]
#### Email SecurityInvestigatePreview

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
#### Email SecurityInvestigateRaw

##### [Get raw email content]
GET/accounts/{account_id}/email-security/investigate/{postfix_id}/raw
##### ModelsExpand Collapse
RawGetResponse  { raw } raw: string
A UTF-8 encoded eml file of the email.
[][]
#### Email SecurityInvestigateTrace

##### [Get email trace]
GET/accounts/{account_id}/email-security/investigate/{postfix_id}/trace
##### ModelsExpand Collapse
TraceGetResponse  { inbound, outbound } inbound:  { lines, pending } lines: optional array of  { lineno, message, ts } lineno: numberformatint64[]message: string[]ts: stringformatdate-time[][]pending: optional boolean[][]outbound:  { lines, pending } lines: optional array of  { lineno, message, ts } lineno: numberformatint64[]message: string[]ts: stringformatdate-time[][]pending: optional boolean[][][]
#### Email SecurityInvestigateMove

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
#### Email SecurityInvestigateReclassify

##### [Change email classification]
POST/accounts/{account_id}/email-security/investigate/{postfix_id}/reclassify
##### ModelsExpand Collapse
ReclassifyCreateResponse = unknown[]
#### Email SecurityInvestigateRelease

##### [Release messages from quarantine]
POST/accounts/{account_id}/email-security/investigate/release
##### ModelsExpand Collapse
ReleaseBulkResponse  { id, postfix_id, delivered, 2 more } id: string[]postfix_id: string
The identifier of the message.
[]delivered: optional array of string[]failed: optional array of string[]undelivered: optional array of string[][]
#### Email SecurityPhishguard

#### Email SecurityPhishguardReports

##### [Get `PhishGuard` reports]
GET/accounts/{account_id}/email-security/phishguard/reports
##### ModelsExpand Collapse
ReportListResponse  { id, content, created_at, 7 more } id: numberformatint32[]content: string[]created_at: stringformatdate-time[]disposition: "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]fields:  { to, ts, from, postfix_id } to: array of string[]ts: stringformatdate-time[]from: optional string[]postfix_id: optional string[][]priority: string[]title: string[]ts: stringformatdate-time[]updated_at: stringformatdate-time[]tags: optional array of  { category, value } category: string[]value: string[][][]
#### Email SecuritySettings

#### Email SecuritySettingsAllow Policies

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
#### Email SecuritySettingsBlock Senders

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
#### Email SecuritySettingsDomains

##### [List protected email domains]
GET/accounts/{account_id}/email-security/settings/domains
##### [Get an email domain]
GET/accounts/{account_id}/email-security/settings/domains/{domain_id}
##### [Update an email domain]
PATCH/accounts/{account_id}/email-security/settings/domains/{domain_id}
##### [Unprotect an email domain]
DELETE/accounts/{account_id}/email-security/settings/domains/{domain_id}
##### [Unprotect multiple email domains]
DELETE/accounts/{account_id}/email-security/settings/domains
##### ModelsExpand Collapse
DomainListResponse  { id, allowed_delivery_modes, created_at, 17 more } id: number
The unique identifier for the domain.
formatint32[]allowed_delivery_modes: array of "DIRECT" or "BCC" or "JOURNAL" or 2 moreOne of the following:"DIRECT"[]"BCC"[]"JOURNAL"[]"API"[]"RETRO_SCAN"[][]created_at: stringformatdate-time[]domain: string[]drop_dispositions: array of "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]ip_restrictions: array of string[]last_modified: stringformatdate-time[]lookback_hops: numberformatint32[]regions: array of "GLOBAL" or "AU" or "DE" or 2 moreOne of the following:"GLOBAL"[]"AU"[]"DE"[]"IN"[]"US"[][]transport: string[]authorization: optional  { authorized, timestamp, status_message } authorized: boolean[]timestamp: stringformatdate-time[]status_message: optional string[][]dmarc_status: optional "none" or "good" or "invalid"One of the following:"none"[]"good"[]"invalid"[][]emails_processed: optional  { timestamp, total_emails_processed, total_emails_processed_previous } timestamp: stringformatdate-time[]total_emails_processed: numberformatint32minimum0[]total_emails_processed_previous: numberformatint32minimum0[][]folder: optional "AllItems" or "Inbox"One of the following:"AllItems"[]"Inbox"[][]inbox_provider: optional "Microsoft" or "Google"One of the following:"Microsoft"[]"Google"[][]integration_id: optional stringformatuuid[]o365_tenant_id: optional string[]require_tls_inbound: optional boolean[]require_tls_outbound: optional boolean[]spf_status: optional "none" or "good" or "neutral" or 2 moreOne of the following:"none"[]"good"[]"neutral"[]"open"[]"invalid"[][][]DomainGetResponse  { id, allowed_delivery_modes, created_at, 17 more } id: number
The unique identifier for the domain.
formatint32[]allowed_delivery_modes: array of "DIRECT" or "BCC" or "JOURNAL" or 2 moreOne of the following:"DIRECT"[]"BCC"[]"JOURNAL"[]"API"[]"RETRO_SCAN"[][]created_at: stringformatdate-time[]domain: string[]drop_dispositions: array of "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]ip_restrictions: array of string[]last_modified: stringformatdate-time[]lookback_hops: numberformatint32[]regions: array of "GLOBAL" or "AU" or "DE" or 2 moreOne of the following:"GLOBAL"[]"AU"[]"DE"[]"IN"[]"US"[][]transport: string[]authorization: optional  { authorized, timestamp, status_message } authorized: boolean[]timestamp: stringformatdate-time[]status_message: optional string[][]dmarc_status: optional "none" or "good" or "invalid"One of the following:"none"[]"good"[]"invalid"[][]emails_processed: optional  { timestamp, total_emails_processed, total_emails_processed_previous } timestamp: stringformatdate-time[]total_emails_processed: numberformatint32minimum0[]total_emails_processed_previous: numberformatint32minimum0[][]folder: optional "AllItems" or "Inbox"One of the following:"AllItems"[]"Inbox"[][]inbox_provider: optional "Microsoft" or "Google"One of the following:"Microsoft"[]"Google"[][]integration_id: optional stringformatuuid[]o365_tenant_id: optional string[]require_tls_inbound: optional boolean[]require_tls_outbound: optional boolean[]spf_status: optional "none" or "good" or "neutral" or 2 moreOne of the following:"none"[]"good"[]"neutral"[]"open"[]"invalid"[][][]DomainEditResponse  { id, allowed_delivery_modes, created_at, 17 more } id: number
The unique identifier for the domain.
formatint32[]allowed_delivery_modes: array of "DIRECT" or "BCC" or "JOURNAL" or 2 moreOne of the following:"DIRECT"[]"BCC"[]"JOURNAL"[]"API"[]"RETRO_SCAN"[][]created_at: stringformatdate-time[]domain: string[]drop_dispositions: array of "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]ip_restrictions: array of string[]last_modified: stringformatdate-time[]lookback_hops: numberformatint32[]regions: array of "GLOBAL" or "AU" or "DE" or 2 moreOne of the following:"GLOBAL"[]"AU"[]"DE"[]"IN"[]"US"[][]transport: string[]authorization: optional  { authorized, timestamp, status_message } authorized: boolean[]timestamp: stringformatdate-time[]status_message: optional string[][]dmarc_status: optional "none" or "good" or "invalid"One of the following:"none"[]"good"[]"invalid"[][]emails_processed: optional  { timestamp, total_emails_processed, total_emails_processed_previous } timestamp: stringformatdate-time[]total_emails_processed: numberformatint32minimum0[]total_emails_processed_previous: numberformatint32minimum0[][]folder: optional "AllItems" or "Inbox"One of the following:"AllItems"[]"Inbox"[][]inbox_provider: optional "Microsoft" or "Google"One of the following:"Microsoft"[]"Google"[][]integration_id: optional stringformatuuid[]o365_tenant_id: optional string[]require_tls_inbound: optional boolean[]require_tls_outbound: optional boolean[]spf_status: optional "none" or "good" or "neutral" or 2 moreOne of the following:"none"[]"good"[]"neutral"[]"open"[]"invalid"[][][]DomainDeleteResponse  { id } id: number
The unique identifier for the domain.
formatint32[][]DomainBulkDeleteResponse  { id } id: number
The unique identifier for the domain.
formatint32[][]
#### Email SecuritySettingsImpersonation Registry

##### [List entries in impersonation registry]
GET/accounts/{account_id}/email-security/settings/impersonation_registry
##### [Get an entry in impersonation registry]
GET/accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}
##### [Create an entry in impersonation registry]
POST/accounts/{account_id}/email-security/settings/impersonation_registry
##### [Update an entry in impersonation registry]
PATCH/accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}
##### [Delete an entry from impersonation registry]
DELETE/accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}
##### ModelsExpand Collapse
ImpersonationRegistryListResponse  { id, created_at, email, 8 more } id: numberformatint32[]created_at: stringformatdate-time[]email: string[]is_email_regex: boolean[]last_modified: stringformatdate-time[]name: stringmaxLength1024[]comments: optional string[]directory_id: optional numberformatint64[]directory_node_id: optional numberformatint64[]Deprecatedexternal_directory_node_id: optional string[]provenance: optional string[][]ImpersonationRegistryGetResponse  { id, created_at, email, 8 more } id: numberformatint32[]created_at: stringformatdate-time[]email: string[]is_email_regex: boolean[]last_modified: stringformatdate-time[]name: stringmaxLength1024[]comments: optional string[]directory_id: optional numberformatint64[]directory_node_id: optional numberformatint64[]Deprecatedexternal_directory_node_id: optional string[]provenance: optional string[][]ImpersonationRegistryCreateResponse  { id, created_at, email, 8 more } id: numberformatint32[]created_at: stringformatdate-time[]email: string[]is_email_regex: boolean[]last_modified: stringformatdate-time[]name: stringmaxLength1024[]comments: optional string[]directory_id: optional numberformatint64[]directory_node_id: optional numberformatint64[]Deprecatedexternal_directory_node_id: optional string[]provenance: optional string[][]ImpersonationRegistryEditResponse  { id, created_at, email, 8 more } id: numberformatint32[]created_at: stringformatdate-time[]email: string[]is_email_regex: boolean[]last_modified: stringformatdate-time[]name: stringmaxLength1024[]comments: optional string[]directory_id: optional numberformatint64[]directory_node_id: optional numberformatint64[]Deprecatedexternal_directory_node_id: optional string[]provenance: optional string[][]ImpersonationRegistryDeleteResponse  { id } id: numberformatint32[][]
#### Email SecuritySettingsTrusted Domains

##### [List trusted email domains]
GET/accounts/{account_id}/email-security/settings/trusted_domains
##### [Get a trusted email domain]
GET/accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}
##### [Create a trusted email domain]
POST/accounts/{account_id}/email-security/settings/trusted_domains
##### [Update a trusted email domain]
PATCH/accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}
##### [Delete a trusted email domain]
DELETE/accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}
##### ModelsExpand Collapse
TrustedDomainListResponse  { id, created_at, is_recent, 5 more } id: number
The unique identifier for the trusted domain.
formatint32[]created_at: stringformatdate-time[]is_recent: boolean
Select to prevent recently registered domains from triggering a
Suspicious or Malicious disposition.
[]is_regex: boolean[]is_similarity: boolean
Select for partner or other approved domains that have similar
spelling to your connected domains. Prevents listed domains from
triggering a Spoof disposition.
[]last_modified: stringformatdate-time[]pattern: stringmaxLength1024minLength1[]comments: optional stringmaxLength1024[][]TrustedDomainGetResponse  { id, created_at, is_recent, 5 more } id: number
The unique identifier for the trusted domain.
formatint32[]created_at: stringformatdate-time[]is_recent: boolean
Select to prevent recently registered domains from triggering a
Suspicious or Malicious disposition.
[]is_regex: boolean[]is_similarity: boolean
Select for partner or other approved domains that have similar
spelling to your connected domains. Prevents listed domains from
triggering a Spoof disposition.
[]last_modified: stringformatdate-time[]pattern: stringmaxLength1024minLength1[]comments: optional stringmaxLength1024[][]TrustedDomainCreateResponse =  { id, created_at, is_recent, 5 more }  or array of  { id, created_at, is_recent, 5 more } One of the following:EmailSecurityTrustedDomain  { id, created_at, is_recent, 5 more } id: number
The unique identifier for the trusted domain.
formatint32[]created_at: stringformatdate-time[]is_recent: boolean
Select to prevent recently registered domains from triggering a
Suspicious or Malicious disposition.
[]is_regex: boolean[]is_similarity: boolean
Select for partner or other approved domains that have similar
spelling to your connected domains. Prevents listed domains from
triggering a Spoof disposition.
[]last_modified: stringformatdate-time[]pattern: stringmaxLength1024minLength1[]comments: optional stringmaxLength1024[][]array of  { id, created_at, is_recent, 5 more } id: number
The unique identifier for the trusted domain.
formatint32[]created_at: stringformatdate-time[]is_recent: boolean
Select to prevent recently registered domains from triggering a
Suspicious or Malicious disposition.
[]is_regex: boolean[]is_similarity: boolean
Select for partner or other approved domains that have similar
spelling to your connected domains. Prevents listed domains from
triggering a Spoof disposition.
[]last_modified: stringformatdate-time[]pattern: stringmaxLength1024minLength1[]comments: optional stringmaxLength1024[][][]TrustedDomainEditResponse  { id, created_at, is_recent, 5 more } id: number
The unique identifier for the trusted domain.
formatint32[]created_at: stringformatdate-time[]is_recent: boolean
Select to prevent recently registered domains from triggering a
Suspicious or Malicious disposition.
[]is_regex: boolean[]is_similarity: boolean
Select for partner or other approved domains that have similar
spelling to your connected domains. Prevents listed domains from
triggering a Spoof disposition.
[]last_modified: stringformatdate-time[]pattern: stringmaxLength1024minLength1[]comments: optional stringmaxLength1024[][]TrustedDomainDeleteResponse  { id } id: number
The unique identifier for the trusted domain.
formatint32[][]
#### Email SecuritySubmissions

##### [Get reclassify submissions]
GET/accounts/{account_id}/email-security/submissions
##### ModelsExpand Collapse
SubmissionListResponse  { requested_ts, submission_id, customer_status, 15 more } Deprecatedrequested_ts: string
deprecated as of 2026-04-01, use `requested_at` instead.
formatdate-time[]submission_id: string[]customer_status: optional "escalated" or "reviewed" or "unreviewed"One of the following:"escalated"[]"reviewed"[]"unreviewed"[][]escalated_as: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]escalated_at: optional stringformatdate-time[]escalated_by: optional string[]escalated_submission_id: optional string[]original_disposition: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]original_edf_hash: optional string[]original_postfix_id: optional string[]outcome: optional string[]outcome_disposition: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]requested_at: optional stringformatdate-time[]requested_by: optional string[]requested_disposition: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]status: optional string[]subject: optional string[]type: optional string[][]