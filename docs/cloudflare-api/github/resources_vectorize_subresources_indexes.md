# Indexes | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/vectorize/subresources/indexes

[API Reference][Vectorize]
# Indexes

##### [List Vectorize Indexes]
GET/accounts/{account_id}/vectorize/v2/indexes
##### [Get Vectorize Index]
GET/accounts/{account_id}/vectorize/v2/indexes/{index_name}
##### [Create Vectorize Index]
POST/accounts/{account_id}/vectorize/v2/indexes
##### [Delete Vectorize Index]
DELETE/accounts/{account_id}/vectorize/v2/indexes/{index_name}
##### [Insert Vectors]
POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/insert
##### [Query Vectors]
POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/query
##### [Upsert Vectors]
POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/upsert
##### [Delete Vectors By Identifier]
POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/delete_by_ids
##### [Get Vectors By Identifier]
POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/get_by_ids
##### [Get Vectorize Index Info]
GET/accounts/{account_id}/vectorize/v2/indexes/{index_name}/info
##### [List Vectors]
GET/accounts/{account_id}/vectorize/v2/indexes/{index_name}/list
##### ModelsExpand Collapse
CreateIndex  { config, created_on, description, 2 more } config: optional [IndexDimensionConfiguration] { dimensions, metric } []created_on: optional string
Specifies the timestamp the resource was created as an ISO8601 string.
formatdate-time[]description: optional string
Specifies the description of the index.
[]modified_on: optional string
Specifies the timestamp the resource was modified as an ISO8601 string.
formatdate-time[]name: optional string[][]IndexDeleteVectorsByID  { count, ids } count: optional number
The count of the vectors successfully deleted.
[]ids: optional array of string
Array of vector identifiers of the vectors that were successfully processed for deletion.
[][]IndexDimensionConfiguration  { dimensions, metric } dimensions: number
Specifies the number of dimensions for the index
maximum1536minimum1[]metric: "cosine" or "euclidean" or "dot-product"
Specifies the type of metric to use calculating distance.
One of the following:"cosine"[]"euclidean"[]"dot-product"[][][]IndexInsert  { count, ids } count: optional number
Specifies the count of the vectors successfully inserted.
[]ids: optional array of string
Array of vector identifiers of the vectors successfully inserted.
[][]IndexQuery  { count, matches } count: optional number
Specifies the count of vectors returned by the search
[]matches: optional array of  { id, metadata, score, values }
Array of vectors matched by the search
id: optional string
Identifier for a Vector
maxLength64[]metadata: optional unknown[]score: optional number
The score of the vector according to the index’s distance metric
[]values: optional array of number[][][]IndexUpsert  { count, ids } count: optional number
Specifies the count of the vectors successfully inserted.
[]ids: optional array of string
Array of vector identifiers of the vectors successfully inserted.
[][]IndexDeleteResponse = unknown or stringOne of the following:unknown[]string[][]IndexInsertResponse  { mutationId } mutationId: optional string
The unique identifier for the async mutation operation containing the changeset.
maxLength36[][]IndexQueryResponse  { count, matches } count: optional number
Specifies the count of vectors returned by the search
[]matches: optional array of  { id, metadata, namespace, 2 more }
Array of vectors matched by the search
id: optional string
Identifier for a Vector
maxLength64[]metadata: optional unknown[]namespace: optional string[]score: optional number
The score of the vector according to the index’s distance metric
[]values: optional array of number[][][]IndexUpsertResponse  { mutationId } mutationId: optional string
The unique identifier for the async mutation operation containing the changeset.
maxLength36[][]IndexDeleteByIDsResponse  { mutationId } mutationId: optional string
The unique identifier for the async mutation operation containing the changeset.
maxLength36[][]IndexGetByIDsResponse = unknown
Array of vectors with matching ids.
[]IndexInfoResponse  { dimensions, processedUpToDatetime, processedUpToMutation, vectorCount } dimensions: optional number
Specifies the number of dimensions for the index
maximum1536minimum1[]processedUpToDatetime: optional string
Specifies the timestamp the last mutation batch was processed as an ISO8601 string.
formatdate-time[]processedUpToMutation: optional string
The unique identifier for the async mutation operation containing the changeset.
maxLength36[]vectorCount: optional number
Specifies the number of vectors present in the index
[][]IndexListVectorsResponse  { count, isTruncated, totalCount, 3 more } count: number
Number of vectors returned in this response
[]isTruncated: boolean
Whether there are more vectors available beyond this response
[]totalCount: number
Total number of vectors in the index
[]vectors: array of  { id }
Array of vector items
id: string
Identifier for a Vector
maxLength64[][]cursorExpirationTimestamp: optional string
When the cursor expires as an ISO8601 string
formatdate-time[]nextCursor: optional string
Cursor for the next page of results
[][]
#### IndexesMetadata Index

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