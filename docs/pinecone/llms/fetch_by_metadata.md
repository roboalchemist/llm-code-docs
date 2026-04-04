# Source: https://docs.pinecone.io/reference/api/2025-10/data-plane/fetch_by_metadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Fetch vectors by metadata

> Look up and return vectors by metadata filter from a single namespace. The returned vectors include the vector data and/or metadata.
For guidance and examples, see [Fetch data](https://docs.pinecone.io/guides/manage-data/fetch-data).

<RequestExample>
  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X POST "https://$INDEX_HOST/vectors/fetch_by_metadata" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
      "namespace": "__default__",
      "filter": {"genre": {"$eq": "Action/Adventure"}},
      "limit": 2
    }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "vectors": {
      "0": {
        "id": "0",
        "values": [
          0.0234527588, 0.0291595459 ...
        ],
        "metadata": {
          "box-office": 2923706026,
          "genre": "Action/Adventure",
          "summary": "On the alien world of Pandora, paraplegic Marine Jake Sully uses an avatar to walk again and becomes torn between his mission and protecting the planet's indigenous Na'vi people. The film stars Sam Worthington, Zoe Saldana, and Sigourney Weaver.",
          "title": "Avatar",
          "year": 2009
        }
      },
      "1": {
        "id": "1",
        "values": [
          0.0397644043, 0.013053894, ...
        ],
        "metadata": {
          "box-office": 2799439100,
          "genre": "Action/Adventure",
          "summary": "In the aftermath of Thanos wiping out half of the universe, the remaining Avengers assemble once more to undo the chaos, leading to a time-traveling adventure. Stars Robert Downey Jr., Chris Evans, and Scarlett Johansson.",
          "title": "Avengers: Endgame",
          "year": 2019
        }
      }
    },
    "namespace": "__default__",
    "usage": {
      "readUnits": 1
    },
    "pagination": {
      "next": "Tm90aGluZyB0byBzZWUgaGVyZQo="
    }
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_data_2025-10.oas.yaml post /vectors/fetch_by_metadata
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
  /vectors/fetch_by_metadata:
    post:
      tags:
        - Vector Operations
      summary: Fetch vectors by metadata
      description: >-
        Look up and return vectors by metadata filter from a single namespace.
        The returned vectors include the vector data and/or metadata.

        For guidance and examples, see [Fetch
        data](https://docs.pinecone.io/guides/manage-data/fetch-data).
      operationId: fetch_vectors_by_metadata
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
              $ref: '#/components/schemas/FetchByMetadataRequest'
        required: true
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FetchByMetadataResponse'
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
    FetchByMetadataRequest:
      description: The request for the `fetch_by_metadata` operation.
      type: object
      properties:
        namespace:
          example: example-namespace
          description: The namespace to fetch vectors from.
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
            Metadata filter expression to select vectors. See [Understanding
            metadata](https://docs.pinecone.io/guides/index-data/indexing-overview#metadata).
          type: object
        limit:
          example: 12
          description: Max number of vectors to return.
          default: 100
          type: integer
          format: int64
          minimum: 1
        paginationToken:
          example: Tm90aGluZyB0byBzZWUgaGVyZQo=
          description: Pagination token to continue a previous listing operation.
          type: string
    FetchByMetadataResponse:
      example:
        namespace: example-namespace
        pagination:
          next: Tm90aGluZyB0byBzZWUgaGVyZQo=
        usage:
          readUnits: 5
        vectors:
          id-1:
            id: id-1
            metadata:
              genre: documentary
              year: 2019
            values:
              - 1
              - 1.5
          id-2:
            id: id-2
            metadata:
              genre: comedy
              year: 2019
            values:
              - 2
              - 1
      description: The response for the `fetch_by_metadata` operation.
      type: object
      properties:
        vectors:
          description: >-
            The fetched vectors, in the form of a map between the fetched ids
            and the fetched vectors
          type: object
          additionalProperties:
            $ref: '#/components/schemas/Vector'
        namespace:
          example: example-namespace
          description: The namespace of the vectors.
          default: ''
          type: string
        usage:
          $ref: '#/components/schemas/Usage'
        pagination:
          $ref: '#/components/schemas/Pagination'
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
    Usage:
      type: object
      properties:
        readUnits:
          example: 5
          description: The number of read units consumed by this operation.
          type: integer
          format: int64
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