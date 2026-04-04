# Models | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/ai/subresources/models

[API Reference][AI]
# Models

##### [Model Search]
GET/accounts/{account_id}/ai/models/search
##### ModelsExpand Collapse
ModelListResponse = unknown[]
#### ModelsSchema

##### [Get Model Schema]
GET/accounts/{account_id}/ai/models/schema
##### ModelsExpand Collapse
SchemaGetResponse  { input, output } input:  { additionalProperties, description, type } additionalProperties: boolean[]description: string[]type: string[][]output:  { additionalProperties, description, type } additionalProperties: boolean[]description: string[]type: string[][][]