# Evaluations | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/ai_gateway/subresources/evaluations

[API Reference][AI Gateway]
# Evaluations

##### [List Evaluations]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations
##### [Fetch a Evaluation]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations/{id}
##### [Create a new Evaluation]
POST/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations
##### [Delete a Evaluation]
DELETE/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations/{id}
##### ModelsExpand Collapse
EvaluationListResponse  { id, created_at, datasets, 6 more } id: string[]created_at: stringformatdate-time[]datasets: array of  { id, account_id, account_tag, 6 more } id: string[]account_id: string[]account_tag: string[]created_at: stringformatdate-time[]enable: boolean[]filters: array of  { key, operator, value } key: "created_at" or "request_content_type" or "response_content_type" or 10 moreOne of the following:"created_at"[]"request_content_type"[]"response_content_type"[]"success"[]"cached"[]"provider"[]"model"[]"cost"[]"tokens"[]"tokens_in"[]"tokens_out"[]"duration"[]"feedback"[][]operator: "eq" or "contains" or "lt" or "gt"One of the following:"eq"[]"contains"[]"lt"[]"gt"[][]value: array of string or number or booleanOne of the following:string[]number[]boolean[][][]gateway_id: string
gateway id
maxLength64minLength1[]modified_at: stringformatdate-time[]name: string[][]gateway_id: string
gateway id
maxLength64minLength1[]modified_at: stringformatdate-time[]name: string[]processed: boolean[]results: array of  { id, created_at, evaluation_id, 6 more } id: string[]created_at: stringformatdate-time[]evaluation_id: string[]evaluation_type_id: string[]modified_at: stringformatdate-time[]result: string[]status: number[]status_description: string[]total_logs: number[][]total_logs: number[][]EvaluationGetResponse  { id, created_at, datasets, 6 more } id: string[]created_at: stringformatdate-time[]datasets: array of  { id, account_id, account_tag, 6 more } id: string[]account_id: string[]account_tag: string[]created_at: stringformatdate-time[]enable: boolean[]filters: array of  { key, operator, value } key: "created_at" or "request_content_type" or "response_content_type" or 10 moreOne of the following:"created_at"[]"request_content_type"[]"response_content_type"[]"success"[]"cached"[]"provider"[]"model"[]"cost"[]"tokens"[]"tokens_in"[]"tokens_out"[]"duration"[]"feedback"[][]operator: "eq" or "contains" or "lt" or "gt"One of the following:"eq"[]"contains"[]"lt"[]"gt"[][]value: array of string or number or booleanOne of the following:string[]number[]boolean[][][]gateway_id: string
gateway id
maxLength64minLength1[]modified_at: stringformatdate-time[]name: string[][]gateway_id: string
gateway id
maxLength64minLength1[]modified_at: stringformatdate-time[]name: string[]processed: boolean[]results: array of  { id, created_at, evaluation_id, 6 more } id: string[]created_at: stringformatdate-time[]evaluation_id: string[]evaluation_type_id: string[]modified_at: stringformatdate-time[]result: string[]status: number[]status_description: string[]total_logs: number[][]total_logs: number[][]EvaluationCreateResponse  { id, created_at, datasets, 6 more } id: string[]created_at: stringformatdate-time[]datasets: array of  { id, account_id, account_tag, 6 more } id: string[]account_id: string[]account_tag: string[]created_at: stringformatdate-time[]enable: boolean[]filters: array of  { key, operator, value } key: "created_at" or "request_content_type" or "response_content_type" or 10 moreOne of the following:"created_at"[]"request_content_type"[]"response_content_type"[]"success"[]"cached"[]"provider"[]"model"[]"cost"[]"tokens"[]"tokens_in"[]"tokens_out"[]"duration"[]"feedback"[][]operator: "eq" or "contains" or "lt" or "gt"One of the following:"eq"[]"contains"[]"lt"[]"gt"[][]value: array of string or number or booleanOne of the following:string[]number[]boolean[][][]gateway_id: string
gateway id
maxLength64minLength1[]modified_at: stringformatdate-time[]name: string[][]gateway_id: string
gateway id
maxLength64minLength1[]modified_at: stringformatdate-time[]name: string[]processed: boolean[]results: array of  { id, created_at, evaluation_id, 6 more } id: string[]created_at: stringformatdate-time[]evaluation_id: string[]evaluation_type_id: string[]modified_at: stringformatdate-time[]result: string[]status: number[]status_description: string[]total_logs: number[][]total_logs: number[][]EvaluationDeleteResponse  { id, created_at, datasets, 6 more } id: string[]created_at: stringformatdate-time[]datasets: array of  { id, account_id, account_tag, 6 more } id: string[]account_id: string[]account_tag: string[]created_at: stringformatdate-time[]enable: boolean[]filters: array of  { key, operator, value } key: "created_at" or "request_content_type" or "response_content_type" or 10 moreOne of the following:"created_at"[]"request_content_type"[]"response_content_type"[]"success"[]"cached"[]"provider"[]"model"[]"cost"[]"tokens"[]"tokens_in"[]"tokens_out"[]"duration"[]"feedback"[][]operator: "eq" or "contains" or "lt" or "gt"One of the following:"eq"[]"contains"[]"lt"[]"gt"[][]value: array of string or number or booleanOne of the following:string[]number[]boolean[][][]gateway_id: string
gateway id
maxLength64minLength1[]modified_at: stringformatdate-time[]name: string[][]gateway_id: string
gateway id
maxLength64minLength1[]modified_at: stringformatdate-time[]name: string[]processed: boolean[]results: array of  { id, created_at, evaluation_id, 6 more } id: string[]created_at: stringformatdate-time[]evaluation_id: string[]evaluation_type_id: string[]modified_at: stringformatdate-time[]result: string[]status: number[]status_description: string[]total_logs: number[][]total_logs: number[][]