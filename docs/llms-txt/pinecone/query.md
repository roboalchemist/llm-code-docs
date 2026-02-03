# Source: https://docs.pinecone.io/reference/api/2025-10/data-plane/query.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Search with a vector

> Search a namespace using a query vector. It retrieves the ids of the most similar items in a namespace, along with their similarity scores.

For guidance, examples, and limits, see [Search](https://docs.pinecone.io/guides/search/search-overview).

<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/query" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
      "namespace": "example-namespace",
      "vector": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
      "filter": {"genre": {"$eq": "documentary"}},
      "topK": 3,
      "includeValues": true
    }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "matches":[
      {
        "id": "vec3",
        "score": 0,
        "values": [0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3]
      },
      {
        "id": "vec2",
        "score": 0.0800000429,
        "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
      },
      {
        "id": "vec4",
        "score": 0.0799999237,
        "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]
      }
    ],
    "namespace": "example-namespace",
    "usage": {"read_units": 6}
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_data_2025-10.oas.yaml post /query
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
  /query:
    post:
      tags:
        - Vector Operations
      summary: Search with a vector
      description: >-
        Search a namespace using a query vector. It retrieves the ids of the
        most similar items in a namespace, along with their similarity scores.


        For guidance, examples, and limits, see
        [Search](https://docs.pinecone.io/guides/search/search-overview).
      operationId: queryVectors
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
              $ref: '#/components/schemas/QueryRequest'
        required: true
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QueryResponse'
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
    QueryRequest:
      description: The request for the `query` operation.
      type: object
      properties:
        namespace:
          example: example-namespace
          description: The namespace to query.
          type: string
        topK:
          example: 10
          description: The number of results to return for each query.
          type: integer
          minimum: 1
          maximum: 10000
          required:
            - top_k
          format: int64
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
            The filter to apply. You can use vector metadata to limit your
            search. See [Understanding
            metadata](https://docs.pinecone.io/guides/index-data/indexing-overview#metadata).
          type: object
        includeValues:
          example: true
          description: >-
            Indicates whether vector values are included in the response. For
            on-demand indexes, setting this to `true` may increase latency,
            especially with higher `topK` values, because vector values are
            retrieved from object storage. Unless you need vector values, set
            this to `false` for better performance.
          default: false
          type: boolean
        includeMetadata:
          example: true
          description: >-
            Indicates whether metadata is included in the response as well as
            the ids.
          default: false
          type: boolean
        queries:
          deprecated: true
          description: DEPRECATED. Use `vector` or `id` instead.
          type: array
          items:
            $ref: '#/components/schemas/QueryVector'
          minLength: 1
          maxLength: 10
        vector:
          example:
            - 0.1
            - 0.2
            - 0.3
            - 0.4
            - 0.5
            - 0.6
            - 0.7
            - 0.8
          description: >-
            The query vector. This should be the same length as the dimension of
            the index being queried. Each `query` request can contain only one
            of the parameters `id` or `vector`.
          type: array
          items:
            type: number
            format: float
          minLength: 1
          maxLength: 20000
        sparseVector:
          $ref: '#/components/schemas/SparseValues'
        id:
          example: example-vector-1
          description: >-
            The unique ID of the vector to be used as a query vector. Each
            request  can contain either the `vector` or `id` parameter.
          type: string
          maxLength: 512
      required:
        - topK
    QueryResponse:
      description: >-
        The response for the `query` operation. These are the matches found for
        a particular query vector. The matches are ordered from most similar to
        least similar.
      type: object
      properties:
        results:
          deprecated: true
          description: >-
            DEPRECATED. The results of each query. The order is the same as
            `QueryRequest.queries`.
          type: array
          items:
            $ref: '#/components/schemas/SingleQueryResults'
        matches:
          description: The matches for the vectors.
          type: array
          items:
            $ref: '#/components/schemas/ScoredVector'
        namespace:
          description: The namespace for the vectors.
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
    QueryVector:
      deprecated: true
      description: A single query vector within a `QueryRequest`.
      type: object
      properties:
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
          description: >-
            The query vector values. This should be the same length as the
            dimension of the index being queried.
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
        topK:
          example: 10
          description: >-
            An override for the number of results to return for this query
            vector.
          type: integer
          format: int64
          minimum: 1
          maximum: 10000
        namespace:
          example: example-namespace
          description: An override the namespace to search.
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
            An override for the metadata filter to apply. This replaces the
            request-level filter.
          type: object
      required:
        - values
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
    SingleQueryResults:
      title: The query results for a single `QueryVector`
      type: object
      properties:
        matches:
          description: The matches for the vectors.
          type: array
          items:
            $ref: '#/components/schemas/ScoredVector'
        namespace:
          example: example-namespace
          description: The namespace for the vectors.
          type: string
    ScoredVector:
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
        score:
          example: 0.08
          description: >-
            This is a measure of similarity between this vector and the query
            vector.  The higher the score, the more they are similar.
          type: number
          format: float
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
          description: This is the vector data, if it is requested.
          type: array
          items:
            type: number
            format: float
        sparseValues:
          $ref: '#/components/schemas/SparseValues'
        metadata:
          example:
            genre: documentary
            year: 2019
          description: This is the metadata, if it is requested.
          type: object
      required:
        - id
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