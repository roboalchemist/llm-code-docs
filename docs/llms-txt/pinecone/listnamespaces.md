# Source: https://docs.pinecone.io/reference/api/2025-10/data-plane/listnamespaces.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List namespaces

> List all namespaces in a serverless index.

Up to 100 namespaces are returned at a time by default, in sorted order (bitwise “C” collation). If the `limit` parameter is set, up to that number of namespaces are returned instead. Whenever there are additional namespaces to return, the response also includes a `pagination_token` that you can use to get the next batch of namespaces. When the response does not include a `pagination_token`, there are no more namespaces to return.

For guidance and examples, see [Manage namespaces](https://docs.pinecone.io/guides/manage-data/manage-namespaces).

**Note:** This operation is not supported for pod-based indexes.

<RequestExample>
  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/namespaces" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2025-10"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "namespaces": [
      {
        "name": "example-namespace",
        "record_count": 20000
      },
      {
        "name": "example-namespace2",
        "record_count": 10500
      },
      ...
    ],
    "pagination": {
      "next": "Tm90aGluZyB0byBzZWUgaGVyZQo="
    }
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_data_2025-10.oas.yaml get /namespaces
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
  /namespaces:
    get:
      tags:
        - Namespace Operations
      summary: List namespaces
      description: >-
        List all namespaces in a serverless index.


        Up to 100 namespaces are returned at a time by default, in sorted order
        (bitwise “C” collation). If the `limit` parameter is set, up to that
        number of namespaces are returned instead. Whenever there are additional
        namespaces to return, the response also includes a `pagination_token`
        that you can use to get the next batch of namespaces. When the response
        does not include a `pagination_token`, there are no more namespaces to
        return.


        For guidance and examples, see [Manage
        namespaces](https://docs.pinecone.io/guides/manage-data/manage-namespaces).


        **Note:** This operation is not supported for pod-based indexes.
      operationId: listNamespacesOperation
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
          name: limit
          description: Max number namespaces to return per page.
          schema:
            type: integer
            format: int32
          example: 10
          style: form
        - in: query
          name: paginationToken
          description: Pagination token to continue a previous listing operation.
          schema:
            type: string
          style: form
        - in: query
          name: prefix
          description: >-
            Prefix of the namespaces to list. Acts as a filter to return only
            namespaces that start with this prefix.
          schema:
            type: string
          example: prefixExample
          style: form
      responses:
        '200':
          description: A successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListNamespacesResponse'
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
    ListNamespacesResponse:
      type: object
      properties:
        namespaces:
          description: The list of namespaces belonging to this index.
          type: array
          items:
            $ref: '#/components/schemas/NamespaceDescription'
        pagination:
          $ref: '#/components/schemas/Pagination'
        total_count:
          example: 25
          description: The total number of namespaces in the index matching the prefix
          type: integer
          format: int32
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
    NamespaceDescription:
      description: A description of a namespace, including the name and record count.
      type: object
      properties:
        name:
          example: example-namespace
          description: The name of the namespace.
          type: string
        record_count:
          example: 20000
          description: The total amount of records within the namespace.
          type: integer
          format: int64
        schema:
          example:
            fields:
              description:
                filterable: true
              genre:
                filterable: true
              year:
                filterable: true
          description: >-
            Schema for the behavior of Pinecone's internal metadata index. By
            default, all metadata is indexed; when `schema` is present, only
            fields which are present in the `fields` object with a `filterable:
            true` are indexed. Note that `filterable: false` is not currently
            supported.
          type: object
          properties:
            fields:
              description: >-
                A map of metadata field names to their configuration. The field
                name must be a valid metadata field name. The field name must be
                unique.
              type: object
              additionalProperties:
                type: object
                properties:
                  filterable:
                    description: >-
                      Whether the field is filterable. If true, the field is
                      indexed and can be used in filters. Only true values are
                      allowed.
                    type: boolean
          required:
            - fields
        indexed_fields:
          description: A list of all indexed metatadata fields in the namespace
          type: object
          properties:
            fields:
              type: array
              items:
                type: string
              example:
                - genre
                - year
                - author
    Pagination:
      type: object
      properties:
        next:
          example: Tm90aGluZyB0byBzZWUgaGVyZQo=
          type: string
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