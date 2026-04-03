# Impersonation Registry | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/impersonation_registry

[API Reference][Email Security][Settings]
# Impersonation Registry

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