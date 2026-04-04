# Trusted Domains | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/trusted_domains

[API Reference][Email Security][Settings]
# Trusted Domains

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