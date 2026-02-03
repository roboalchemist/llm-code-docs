# Source: https://docs.pinecone.io/reference/api/2025-10/data-plane/update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a vector

> Update a vector in a namespace. If a value is included, it will overwrite the previous value. If a `set_metadata` is included, the values of the fields specified in it will be added or overwrite the previous value.

For guidance and examples, see [Update data](https://docs.pinecone.io/guides/manage-data/update-data).

<RequestExample>
  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/vectors/update" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
          "id": "id-3",
          "values": [4.0, 2.0],
          "setMetadata": {"type": "comedy"},
          "namespace": "example-namespace"
        }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {}
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_data_2025-10.oas.yaml post /vectors/update
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
  /vectors/update:
    post:
      tags:
        - Vector Operations
      summary: Update a vector
      description: >-
        Update a vector in a namespace. If a value is included, it will
        overwrite the previous value. If a `set_metadata` is included, the
        values of the fields specified in it will be added or overwrite the
        previous value.


        For guidance and examples, see [Update
        data](https://docs.pinecone.io/guides/manage-data/update-data).
      operationId: updateVector
      parameters:
        - in: header
          name: X-Pinecone-Api-Version
          description: Required date-based version header
          required: true
          schema:
            default: 2025-10
            type: string
          style: simple
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateRequest'
        required: true
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateResponse'
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
    UpdateRequest:
      description: The request for the `update` operation.
      type: object
      properties:
        id:
          example: example-vector-1
          description: Vector's unique id.
          type: string
          minLength: 1
          maxLength: 512
        values:
          example:
            - 0.1
            - 0.2
            - 0.3
            - 0.4
            - 0.5
            - 0.6
            - 0.7
            - 0.8
          description: Vector data.
          type: array
          items:
            type: number
            format: float
          minLength: 1
          maxLength: 20000
        sparseValues:
          $ref: '#/components/schemas/SparseValues'
        setMetadata:
          example:
            genre: documentary
            year: 2019
          description: Metadata to set for the vector.
          type: object
        namespace:
          example: example-namespace
          description: The namespace containing the vector to update.
          type: string
        filter:
          example:
            genre:
              $in:
                - comedy
                - documentary
                - drama
            year:
              $eq: 2019
          description: >-
            A metadata filter expression. When updating metadata across records
            in a namespace,  the update is applied to all records that match the
            filter.  See [Understanding
            metadata](https://docs.pinecone.io/guides/index-data/indexing-overview#metadata).
          type: object
        dryRun:
          example: false
          description: >-
            If `true`, return the number of records that match the `filter`, but
            do not execute the update.  Default is `false`.
          default: false
          type: boolean
    UpdateResponse:
      description: The response for the `update` operation.
      type: object
      properties:
        matchedRecords:
          example: 42
          description: >-
            The number of records that matched the filter (if a filter was
            provided).
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
    SparseValues:
      description: >-
        Vector sparse data. Represented as a list of indices and a list of 
        corresponded values, which must be with the same length.
      type: object
      properties:
        indices:
          example:
            - 1
            - 312
            - 822
            - 14
            - 980
          description: The indices of the sparse data.
          type: array
          required:
            - indices
          items:
            type: integer
            format: int64
          minLength: 1
          maxLength: 1000
        values:
          example:
            - 0.1
            - 0.2
            - 0.3
            - 0.4
            - 0.5
          description: >-
            The corresponding values of the sparse data, which must be with the
            same length as the indices.
          type: array
          required:
            - values
          items:
            type: number
            format: float
          minLength: 1
          maxLength: 1000
      required:
        - indices
        - values
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