# Source: https://docs.pinecone.io/reference/api/2025-10/data-plane/list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List vector IDs

> List the IDs of vectors in a single namespace of a serverless index. An optional prefix can be passed to limit the results to IDs with a common prefix.

Returns up to 100 IDs at a time by default in sorted order (bitwise "C" collation). If the `limit` parameter is set, `list` returns up to that number of IDs instead. Whenever there are additional IDs to return, the response also includes a `pagination_token` that you can use to get the next batch of IDs. When the response does not include a `pagination_token`, there are no more IDs to return.

For guidance and examples, see [List record IDs](https://docs.pinecone.io/guides/manage-data/list-record-ids).

**Note:** `list` is supported only for serverless indexes.

<RequestExample>
  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/vectors/list?namespace=example-namespace&prefix=doc1#&limit=3" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "vectors": [
      { "id": "doc1#chunk1" },
      { "id": "doc1#chunk2" },
      { "id": "doc1#chunk3" }
    ],
    "pagination": {
      "next": "c2Vjb25kY2FsbA=="
    },
    "namespace": "example-namespace",
    "usage": {
      "readUnits": 1
    }
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_data_2025-10.oas.yaml get /vectors/list
openapi: 3.0.3
info:
  title: Pinecone Data Plane API
  description: >-
    Pinecone is a vector database that makes it easy to search and retrieve
    billions of high-dimensional vectors.
  contact:
    name: Pinecone Support
    url: https://support.pinecone.io
    email: support@pinecone.io
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0
  version: 2025-10
servers:
  - url: https://{index_host}
    variables:
      index_host:
        default: unknown
        description: host of the index
security:
  - ApiKeyAuth: []
tags:
  - name: Vector Operations
  - name: Bulk Operations
  - name: Namespace Operations
externalDocs:
  description: More Pinecone.io API docs
  url: https://docs.pinecone.io/introduction
paths:
  /vectors/list:
    get:
      tags:
        - Vector Operations
      summary: List vector IDs
      description: >-
        List the IDs of vectors in a single namespace of a serverless index. An
        optional prefix can be passed to limit the results to IDs with a common
        prefix.


        Returns up to 100 IDs at a time by default in sorted order (bitwise "C"
        collation). If the `limit` parameter is set, `list` returns up to that
        number of IDs instead. Whenever there are additional IDs to return, the
        response also includes a `pagination_token` that you can use to get the
        next batch of IDs. When the response does not include a
        `pagination_token`, there are no more IDs to return.


        For guidance and examples, see [List record
        IDs](https://docs.pinecone.io/guides/manage-data/list-record-ids).


        **Note:** `list` is supported only for serverless indexes.
      operationId: listVectors
      parameters:
        - in: header
          name: X-Pinecone-Api-Version
          description: Required date-based version header
          required: true
          schema:
            default: 2025-10
            type: string
          style: simple
        - in: query
          name: prefix
          description: The vector IDs to fetch. Does not accept values containing spaces.
          schema:
            type: string
          style: form
        - in: query
          name: limit
          description: Max number of IDs to return per page.
          schema:
            default: 100
            type: integer
            format: int64
          style: form
        - in: query
          name: paginationToken
          description: Pagination token to continue a previous listing operation.
          schema:
            type: string
          style: form
        - in: query
          name: namespace
          description: >-
            The namespace to list vectors from. If not provided, the default
            namespace is used.
          schema:
            type: string
          style: form
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListResponse'
        '400':
          description: Bad request. The request body included invalid request parameters.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/rpcStatus'
        4XX:
          description: An unexpected error response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/rpcStatus'
        5XX:
          description: An unexpected error response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/rpcStatus'
components:
  schemas:
    ListResponse:
      description: The response for the `list` operation.
      type: object
      properties:
        vectors:
          example:
            - id: document1#abb
            - id: document1#abc
          title: A list of ids
          type: array
          items:
            $ref: '#/components/schemas/ListItem'
        pagination:
          $ref: '#/components/schemas/Pagination'
        namespace:
          example: example-namespace
          description: The namespace of the vectors.
          type: string
        usage:
          $ref: '#/components/schemas/Usage'
    rpcStatus:
      type: object
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string
        details:
          type: array
          items:
            $ref: '#/components/schemas/protobufAny'
    ListItem:
      type: object
      properties:
        id:
          example: document1#abb
          type: string
    Pagination:
      type: object
      properties:
        next:
          example: Tm90aGluZyB0byBzZWUgaGVyZQo=
          type: string
    Usage:
      type: object
      properties:
        readUnits:
          example: 5
          description: The number of read units consumed by this operation.
          type: integer
          format: int64
    protobufAny:
      type: object
      properties:
        typeUrl:
          type: string
        value:
          type: string
          format: byte
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: >-
        An API Key is required to call Pinecone APIs. Get yours from the
        [console](https://app.pinecone.io/).

````