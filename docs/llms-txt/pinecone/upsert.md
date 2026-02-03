# Source: https://docs.pinecone.io/reference/api/2025-10/data-plane/upsert.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Upsert vectors

> Upsert vectors into a namespace. If a new value is upserted for an existing vector ID, it will overwrite the previous value.

For guidance, examples, and limits, see [Upsert data](https://docs.pinecone.io/guides/index-data/upsert-data).

<Tip>
  To control costs when ingesting large datasets (10,000,000+ records), use [import](/guides/index-data/import-data) instead of upsert.
</Tip>

<RequestExample>
  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/vectors/upsert" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
      "vectors": [
        {
          "id": "vec1",
          "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
          "metadata": {"genre": "comedy", "year": 2020}
        },
        {
          "id": "vec2",
          "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
          "metadata": {"genre": "documentary", "year": 2019}
        }
      ],
      "namespace": "example-namespace"
    }'
  ```
</RequestExample>

<ResponseExample />

```
```


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_data_2025-10.oas.yaml post /vectors/upsert
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
  /vectors/upsert:
    post:
      tags:
        - Vector Operations
      summary: Upsert vectors
      description: >-
        Upsert vectors into a namespace. If a new value is upserted for an
        existing vector ID, it will overwrite the previous value.


        For guidance, examples, and limits, see [Upsert
        data](https://docs.pinecone.io/guides/index-data/upsert-data).
      operationId: upsertVectors
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
              $ref: '#/components/schemas/UpsertRequest'
        required: true
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpsertResponse'
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
    UpsertRequest:
      description: The request for the `upsert` operation.
      type: object
      properties:
        vectors:
          description: >-
            An array containing the vectors to upsert. Recommended batch limit
            is up to 1000 vectors.
          type: array
          items:
            $ref: '#/components/schemas/Vector'
          minLength: 1
          maxLength: 1000
        namespace:
          example: example-namespace
          description: The namespace where you upsert vectors.
          type: string
      required:
        - vectors
    UpsertResponse:
      description: The response for the `upsert` operation.
      type: object
      properties:
        upsertedCount:
          example: 2
          description: The number of vectors upserted.
          type: integer
          format: int64
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
    Vector:
      type: object
      properties:
        id:
          example: example-vector-1
          description: This is the vector's unique id.
          type: string
          required:
            - id
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
          description: This is the vector data included in the request.
          type: array
          required:
            - values
          items:
            type: number
            format: float
          minLength: 1
          maxLength: 20000
        sparseValues:
          $ref: '#/components/schemas/SparseValues'
        metadata:
          example:
            genre: documentary
            year: 2019
          description: This is the metadata included in the request.
          type: object
      required:
        - id
    protobufAny:
      type: object
      properties:
        typeUrl:
          type: string
        value:
          type: string
          format: byte
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
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: >-
        An API Key is required to call Pinecone APIs. Get yours from the
        [console](https://app.pinecone.io/).

````