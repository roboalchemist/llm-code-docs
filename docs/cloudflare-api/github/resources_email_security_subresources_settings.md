# Settings | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/email_security/subresources/settings

[API Reference][Email Security]
# Settings

#### SettingsAllow Policies

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
#### SettingsBlock Senders

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
#### SettingsDomains

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
#### SettingsImpersonation Registry

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
#### SettingsTrusted Domains

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