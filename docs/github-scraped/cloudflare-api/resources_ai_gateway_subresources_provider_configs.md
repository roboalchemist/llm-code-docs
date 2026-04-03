# Provider Configs | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/ai_gateway/subresources/provider_configs

[API Reference][AI Gateway]
# Provider Configs

##### [List Provider Configs]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/provider_configs
##### [Create a new Provider Configs]
POST/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/provider_configs
##### ModelsExpand Collapse
ProviderConfigListResponse  { id, alias, default_config, 7 more } id: string[]alias: string[]default_config: boolean[]gateway_id: string
gateway id
maxLength64minLength1[]modified_at: stringformatdate-time[]provider_slug: string[]secret_id: string[]secret_preview: string[]rate_limit: optional number[]rate_limit_period: optional number[][]ProviderConfigCreateResponse  { id, alias, default_config, 7 more } id: string[]alias: string[]default_config: boolean[]gateway_id: string
gateway id
maxLength64minLength1[]modified_at: stringformatdate-time[]provider_slug: string[]secret_id: string[]secret_preview: string[]rate_limit: optional number[]rate_limit_period: optional number[][]