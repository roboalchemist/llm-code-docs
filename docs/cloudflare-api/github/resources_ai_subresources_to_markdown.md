# To Markdown | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/ai/subresources/to_markdown

[API Reference][AI]
# To Markdown

##### [Convert Files into Markdown]
POST/accounts/{account_id}/ai/tomarkdown
##### [Get all converted formats supported]
GET/accounts/{account_id}/ai/tomarkdown/supported
##### ModelsExpand Collapse
ToMarkdownTransformResponse  { data, format, mimeType, 2 more } data: string[]format: string[]mimeType: string[]name: string[]tokens: string[][]ToMarkdownSupportedResponse  { extension, mimeType } extension: string[]mimeType: string[][]