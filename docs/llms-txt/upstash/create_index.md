# Source: https://upstash.com/docs/devops/developer-api/vector/create_index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Index

> This endpoint creates an index.



## OpenAPI

````yaml devops/developer-api/openapi.yml post /vector/index
openapi: 3.0.4
info:
  title: Developer API - Upstash
  description: >-
    This is a documentation to specify Developer API endpoints based on the
    OpenAPI 3.0 specification.
  contact:
    name: Support Team
    email: support@upstash.com
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0.html
  version: 1.0.0
servers:
  - url: https://api.upstash.com/v2
security: []
tags:
  - name: redis
    description: Manage redis databases.
    externalDocs:
      description: Find out more
      url: https://upstash.com/docs/devops/developer-api/introduction
  - name: teams
    description: Manage teams and team members.
    externalDocs:
      description: Find out more
      url: https://upstash.com/docs/devops/developer-api/introduction
  - name: vector
    description: Manage vector indices.
    externalDocs:
      description: Find out more
      url: https://upstash.com/docs/devops/developer-api/introduction
  - name: search
    description: Manage search indices.
    externalDocs:
      description: Find out more
      url: https://upstash.com/docs/devops/developer-api/introduction
  - name: qstash
    description: Manage QStash.
    externalDocs:
      description: Find out more
      url: https://upstash.com/docs/devops/developer-api/introduction
externalDocs:
  description: Find out more about Upstash
  url: https://upstash.com/
paths:
  /vector/index:
    post:
      tags:
        - vector
      summary: Create Index
      description: This endpoint creates an index.
      operationId: createIndex
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateIndexRequest'
      responses:
        '200':
          description: Index created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VectorIndex'
      security:
        - basicAuth: []
components:
  schemas:
    CreateIndexRequest:
      type: object
      properties:
        name:
          type: string
          description: Name of the index
          example: myindex
        region:
          type: string
          description: Region of the database
          enum:
            - eu-west-1
            - us-east-1
            - us-central1
          example: us-east-1
        similarity_function:
          type: string
          description: >-
            Similarity function that's used to calculate the distance between
            two vectors
          enum:
            - COSINE
            - EUCLIDEAN
            - DOT_PRODUCT
          example: COSINE
        dimension_count:
          type: number
          description: The amount of values in a single vector
          example: 1024
        type:
          type: string
          description: The payment plan of your index
          enum:
            - payg
            - fixed
            - paid
          example: payg
        embedding_model:
          type: string
          description: The embedding model to use for the index
          enum:
            - BGE_SMALL_EN_V1_5
            - BGE_BASE_EN_V1_5
            - BGE_LARGE_EN_V1_5
            - BGE_M3
          example: BGE_M3
        index_type:
          type: string
          description: The type of the vector index
          enum:
            - DENSE
            - SPARSE
            - HYBRID
          example: HYBRID
        sparse_embedding_model:
          type: string
          description: The sparse embedding model to be used for indexes
          enum:
            - BM25
            - BGE_M3
          example: BM25
      required:
        - name
        - region
        - similarity_function
        - dimension_count
    VectorIndex:
      type: object
      properties:
        customer_id:
          type: string
          description: The associated ID of the owner of the index
          example: example@upstash.com
        id:
          type: string
          description: Unique ID of the index
          example: 0639864f-ece6-429c-8118-86a287b0e808
        name:
          type: string
          description: The name of the index
          example: myindex
        similarity_function:
          type: string
          description: >-
            Similarity function that's used to calculate the distance between
            two vectors
          enum:
            - COSINE
            - EUCLIDEAN
            - DOT_PRODUCT
          example: COSINE
        dimension_count:
          type: number
          description: The amount of values in a single vector
          example: 384
        embedding_model:
          type: string
          description: The predefined embedding model to vectorize your plain text
          enum:
            - BGE_SMALL_EN_V1_5
            - BGE_BASE_EN_V1_5
            - BGE_LARGE_EN_V1_5
            - BGE_M3
          example: BGE_SMALL_EN_V1_5
        sparse_embedding_model:
          type: string
          description: The sparse embedding model to be used for indexes
          enum:
            - BM25
            - BGE_M3
          example: BM25
        endpoint:
          type: string
          description: The REST endpoint of the index
          example: glowing-baboon-15797-us1
        token:
          type: string
          description: The REST authentication token for the index
          example: QkZGAsWp2tdW0tdC0zNzM1LWV1MkFkNQzB1ExUb3hOekF0TVRJbFpMDNLVSm1GZw==
        read_only_token:
          type: string
          description: The REST authentication read only token for the index
          example: QkZGRk1heGSKC0MtdRlZC0zNzM1LWTj3pAV0Wm1aZ01p05qY3RNR0U0TkRtRt2s9azJU
        type:
          type: string
          description: The payment plan of the index
          enum:
            - free
            - payg
            - fixed
          example: fixed
        region:
          type: string
          description: The region where the index is currently deployed
          enum:
            - eu-west-1
            - us-east-1
            - us-central1
          example: us-east-1
        max_vector_count:
          type: number
          description: The number of maximum that your index can contain
          example: 5210000
        max_daily_updates:
          type: number
          description: >-
            The number of maximum update operations you can perform in a day.
            Only upsert operations are included in update count.
          example: 1000000
        max_daily_queries:
          type: number
          description: >-
            The number of maximum query operations you can perform in a day.
            Only query operations are included in query count.
          example: 1000000
        max_monthly_bandwidth:
          type: number
          description: >-
            The maximum amount of monthly bandwidth for the index. Unit is
            bytes. -1 if the limit is unlimited.
          example: -1
        max_writes_per_second:
          type: number
          description: >-
            The number of maximum write operations you can perform per second.
            Only upsert operations are included in write count.
          example: 1000
        max_query_per_second:
          type: number
          description: >-
            The number of maximum query operations you can perform per second.
            Only query operations are included in query count.
          example: 1000
        max_reads_per_request:
          type: number
          description: >-
            The number of maximum vectors in a read operation. Query and fetch
            operations are included in read operations.
          example: 1000
        max_writes_per_request:
          type: number
          description: >-
            The number of maximum vectors in a write operation. Only upsert
            operations are included in write operations.
          example: 1000
        max_total_metadata_size:
          type: number
          description: >-
            The amount of maximum size for the total metadata sizes in your
            index.
          example: 53687091200
        reserved_price:
          type: number
          description: >-
            Monthly pricing of your index. Only available for fixed and pro
            plans.
          example: 60
        creation_time:
          type: number
          description: The creation time of the vector index in UTC as unix timestamp.
          example: 1753207106
        index_type:
          type: string
          description: The type of the vector index
          enum:
            - DENSE
            - SPARSE
            - HYBRID
          example: DENSE
        throughput_vector:
          type: array
          items:
            $ref: '#/components/schemas/TimeSeriesData'
          description: Throughput data for the vector index over time
          example:
            - x: 2025-09-04 14:55:00.000 +0000 UTC
              'y': 0
            - x: 2025-09-04 14:56:00.000 +0000 UTC
              'y': 0
      xml:
        name: vectorIndex
    TimeSeriesData:
      type: object
      properties:
        x:
          type: string
          description: Timestamp when measurement was taken
          example: 2023-05-22 10:59:23.426 +0000 UTC
        'y':
          type: number
          description: The measured value
          example: 320
      required:
        - x
        - 'y'
  securitySchemes:
    basicAuth:
      type: http
      scheme: basic

````