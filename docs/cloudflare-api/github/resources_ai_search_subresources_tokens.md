# Tokens | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/ai_search/subresources/tokens

[API Reference][AI Search]
# Tokens

##### [List tokens.]
GET/accounts/{account_id}/ai-search/tokens
##### [Create new tokens.]
POST/accounts/{account_id}/ai-search/tokens
##### [Read tokens.]
GET/accounts/{account_id}/ai-search/tokens/{id}
##### [Update tokens.]
PUT/accounts/{account_id}/ai-search/tokens/{id}
##### [Delete tokens.]
DELETE/accounts/{account_id}/ai-search/tokens/{id}
##### ModelsExpand Collapse
TokenListResponse  { id, cf_api_id, created_at, 6 more } id: stringformatuuid[]cf_api_id: string[]created_at: stringformatdate-time[]modified_at: stringformatdate-time[]name: string[]created_by: optional string[]enabled: optional boolean[]legacy: optional boolean[]modified_by: optional string[][]TokenCreateResponse  { id, cf_api_id, created_at, 6 more } id: stringformatuuid[]cf_api_id: string[]created_at: stringformatdate-time[]modified_at: stringformatdate-time[]name: string[]created_by: optional string[]enabled: optional boolean[]legacy: optional boolean[]modified_by: optional string[][]TokenReadResponse  { id, cf_api_id, created_at, 6 more } id: stringformatuuid[]cf_api_id: string[]created_at: stringformatdate-time[]modified_at: stringformatdate-time[]name: string[]created_by: optional string[]enabled: optional boolean[]legacy: optional boolean[]modified_by: optional string[][]TokenUpdateResponse  { id, cf_api_id, created_at, 6 more } id: stringformatuuid[]cf_api_id: string[]created_at: stringformatdate-time[]modified_at: stringformatdate-time[]name: string[]created_by: optional string[]enabled: optional boolean[]legacy: optional boolean[]modified_by: optional string[][]TokenDeleteResponse  { id, cf_api_id, created_at, 6 more } id: stringformatuuid[]cf_api_id: string[]created_at: stringformatdate-time[]modified_at: stringformatdate-time[]name: string[]created_by: optional string[]enabled: optional boolean[]legacy: optional boolean[]modified_by: optional string[][]