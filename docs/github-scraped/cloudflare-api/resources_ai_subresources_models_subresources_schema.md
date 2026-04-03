# Schema | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/ai/subresources/models/subresources/schema

[API Reference][AI][Models]
# Schema

##### [Get Model Schema]
GET/accounts/{account_id}/ai/models/schema
##### ModelsExpand Collapse
SchemaGetResponse  { input, output } input:  { additionalProperties, description, type } additionalProperties: boolean[]description: string[]type: string[][]output:  { additionalProperties, description, type } additionalProperties: boolean[]description: string[]type: string[][][]