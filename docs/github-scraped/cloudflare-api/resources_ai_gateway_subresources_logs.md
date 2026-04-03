# Logs | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs

[API Reference][AI Gateway]
# Logs

##### [List Gateway Logs]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs
##### [Get Gateway Log Detail]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}
##### [Patch Gateway Log]
PATCH/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}
##### [Delete Gateway Logs]
DELETE/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs
##### [Get Gateway Log Request]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}/request
##### [Get Gateway Log Response]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}/response
##### ModelsExpand Collapse
LogListResponse  { id, cached, created_at, 16 more } id: string[]cached: boolean[]created_at: stringformatdate-time[]duration: number[]model: string[]path: string[]provider: string[]success: boolean[]tokens_in: number[]tokens_out: number[]cost: optional number[]custom_cost: optional boolean[]metadata: optional string[]model_type: optional string[]request_content_type: optional string[]request_type: optional string[]response_content_type: optional string[]status_code: optional number[]step: optional number[][]LogGetResponse  { id, cached, created_at, 22 more } id: string[]cached: boolean[]created_at: stringformatdate-time[]duration: number[]model: string[]path: string[]provider: string[]success: boolean[]tokens_in: number[]tokens_out: number[]cost: optional number[]custom_cost: optional boolean[]metadata: optional string[]model_type: optional string[]request_content_type: optional string[]request_head: optional string[]request_head_complete: optional boolean[]request_size: optional number[]request_type: optional string[]response_content_type: optional string[]response_head: optional string[]response_head_complete: optional boolean[]response_size: optional number[]status_code: optional number[]step: optional number[][]LogEditResponse = unknown[]LogDeleteResponse  { success } success: boolean[][]LogRequestResponse = unknown[]LogResponseResponse = unknown[]