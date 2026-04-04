# Datasets | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/ai_gateway/subresources/datasets

[API Reference][AI Gateway]
# Datasets

##### [List Datasets]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets
##### [Fetch a Dataset]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets/{id}
##### [Create a new Dataset]
POST/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets
##### [Update a Dataset]
PUT/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets/{id}
##### [Delete a Dataset]
DELETE/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets/{id}
##### ModelsExpand Collapse
DatasetListResponse  { id, created_at, enable, 4 more } id: string[]created_at: stringformatdate-time[]enable: boolean[]filters: array of  { key, operator, value } key: "created_at" or "request_content_type" or "response_content_type" or 10 moreOne of the following:"created_at"[]"request_content_type"[]"response_content_type"[]"success"[]"cached"[]"provider"[]"model"[]"cost"[]"tokens"[]"tokens_in"[]"tokens_out"[]"duration"[]"feedback"[][]operator: "eq" or "contains" or "lt" or "gt"One of the following:"eq"[]"contains"[]"lt"[]"gt"[][]value: array of string or number or booleanOne of the following:string[]number[]boolean[][][]gateway_id: string
gateway id
maxLength64minLength1[]modified_at: stringformatdate-time[]name: string[][]DatasetGetResponse  { id, created_at, enable, 4 more } id: string[]created_at: stringformatdate-time[]enable: boolean[]filters: array of  { key, operator, value } key: "created_at" or "request_content_type" or "response_content_type" or 10 moreOne of the following:"created_at"[]"request_content_type"[]"response_content_type"[]"success"[]"cached"[]"provider"[]"model"[]"cost"[]"tokens"[]"tokens_in"[]"tokens_out"[]"duration"[]"feedback"[][]operator: "eq" or "contains" or "lt" or "gt"One of the following:"eq"[]"contains"[]"lt"[]"gt"[][]value: array of string or number or booleanOne of the following:string[]number[]boolean[][][]gateway_id: string
gateway id
maxLength64minLength1[]modified_at: stringformatdate-time[]name: string[][]DatasetCreateResponse  { id, created_at, enable, 4 more } id: string[]created_at: stringformatdate-time[]enable: boolean[]filters: array of  { key, operator, value } key: "created_at" or "request_content_type" or "response_content_type" or 10 moreOne of the following:"created_at"[]"request_content_type"[]"response_content_type"[]"success"[]"cached"[]"provider"[]"model"[]"cost"[]"tokens"[]"tokens_in"[]"tokens_out"[]"duration"[]"feedback"[][]operator: "eq" or "contains" or "lt" or "gt"One of the following:"eq"[]"contains"[]"lt"[]"gt"[][]value: array of string or number or booleanOne of the following:string[]number[]boolean[][][]gateway_id: string
gateway id
maxLength64minLength1[]modified_at: stringformatdate-time[]name: string[][]DatasetUpdateResponse  { id, created_at, enable, 4 more } id: string[]created_at: stringformatdate-time[]enable: boolean[]filters: array of  { key, operator, value } key: "created_at" or "request_content_type" or "response_content_type" or 10 moreOne of the following:"created_at"[]"request_content_type"[]"response_content_type"[]"success"[]"cached"[]"provider"[]"model"[]"cost"[]"tokens"[]"tokens_in"[]"tokens_out"[]"duration"[]"feedback"[][]operator: "eq" or "contains" or "lt" or "gt"One of the following:"eq"[]"contains"[]"lt"[]"gt"[][]value: array of string or number or booleanOne of the following:string[]number[]boolean[][][]gateway_id: string
gateway id
maxLength64minLength1[]modified_at: stringformatdate-time[]name: string[][]DatasetDeleteResponse  { id, created_at, enable, 4 more } id: string[]created_at: stringformatdate-time[]enable: boolean[]filters: array of  { key, operator, value } key: "created_at" or "request_content_type" or "response_content_type" or 10 moreOne of the following:"created_at"[]"request_content_type"[]"response_content_type"[]"success"[]"cached"[]"provider"[]"model"[]"cost"[]"tokens"[]"tokens_in"[]"tokens_out"[]"duration"[]"feedback"[][]operator: "eq" or "contains" or "lt" or "gt"One of the following:"eq"[]"contains"[]"lt"[]"gt"[][]value: array of string or number or booleanOne of the following:string[]number[]boolean[][][]gateway_id: string
gateway id
maxLength64minLength1[]modified_at: stringformatdate-time[]name: string[][]