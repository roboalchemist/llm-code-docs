# Finetunes | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/ai/subresources/finetunes

[API Reference][AI]
# Finetunes

##### [List Finetunes]
GET/accounts/{account_id}/ai/finetunes
##### [Create a new Finetune]
POST/accounts/{account_id}/ai/finetunes
##### ModelsExpand Collapse
FinetuneListResponse  { id, created_at, model, 3 more } id: stringformatuuid[]created_at: stringformatdate-time[]model: string[]modified_at: stringformatdate-time[]name: string[]description: optional string[][]FinetuneCreateResponse  { id, created_at, model, 4 more } id: stringformatuuid[]created_at: stringformatdate-time[]model: string[]modified_at: stringformatdate-time[]name: string[]public: boolean[]description: optional string[][]
#### FinetunesAssets

##### [Upload a Finetune Asset]
POST/accounts/{account_id}/ai/finetunes/{finetune_id}/finetune-assets
##### ModelsExpand Collapse
AssetCreateResponse  { success } success: boolean[][]
#### FinetunesPublic

##### [List Public Finetunes]
GET/accounts/{account_id}/ai/finetunes/public
##### ModelsExpand Collapse
PublicListResponse  { id, created_at, model, 4 more } id: stringformatuuid[]created_at: stringformatdate-time[]model: string[]modified_at: stringformatdate-time[]name: string[]public: boolean[]description: optional string[][]