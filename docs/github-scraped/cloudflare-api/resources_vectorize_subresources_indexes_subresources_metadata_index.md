# Metadata Index | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes/subresources/metadata_index

[API Reference][Vectorize][Indexes]
# Metadata Index

##### [List Metadata Indexes]
GET/accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/list
##### [Create Metadata Index]
POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/create
##### [Delete Metadata Index]
POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/delete
##### ModelsExpand Collapse
MetadataIndexListResponse  { metadataIndexes } metadataIndexes: optional array of  { indexType, propertyName }
Array of indexed metadata properties.
indexType: optional "string" or "number" or "boolean"
Specifies the type of indexed metadata property.
One of the following:"string"[]"number"[]"boolean"[][]propertyName: optional string
Specifies the indexed metadata property.
[][][]MetadataIndexCreateResponse  { mutationId } mutationId: optional string
The unique identifier for the async mutation operation containing the changeset.
maxLength36[][]MetadataIndexDeleteResponse  { mutationId } mutationId: optional string
The unique identifier for the async mutation operation containing the changeset.
maxLength36[][]