# Source: https://upstash.com/docs/devops/developer-api/vector/get_index.md

# Get Index

> This endpoint returns the data associated to a index.

## OpenAPI

````yaml devops/developer-api/openapi.yml get /vector/index/{id}
paths:
  path: /vector/index/{id}
  method: get
  servers:
    - url: https://api.upstash.com/v2
  request:
    security:
      - title: basicAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: basic
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: The unique ID of the index to fetch
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              customer_id:
                allOf:
                  - type: string
                    description: The associated ID of the owner of the index
                    example: example@upstash.com
              id:
                allOf:
                  - type: string
                    description: Unique ID of the index
                    example: 0639864f-ece6-429c-8118-86a287b0e808
              name:
                allOf:
                  - type: string
                    description: The name of the index
                    example: myindex
              similarity_function:
                allOf:
                  - type: string
                    description: >-
                      Similarity function that's used to calculate the distance
                      between two vectors
                    enum:
                      - COSINE
                      - EUCLIDEAN
                      - DOT_PRODUCT
                    example: COSINE
              dimension_count:
                allOf:
                  - type: number
                    description: The amount of values in a single vector
                    example: 384
              embedding_model:
                allOf:
                  - type: string
                    description: >-
                      The predefined embedding model to vectorize your plain
                      text
                    enum:
                      - BGE_SMALL_EN_V1_5
                      - BGE_BASE_EN_V1_5
                      - BGE_LARGE_EN_V1_5
                      - BGE_M3
                      - BERT_BASE_UNCASED
                      - UAE_LARGE_V1
                      - ALL_MINILM_L6_V2
                      - MXBAI_EMBED_LARGE_V1
                      - BM25
                    example: BGE_SMALL_EN_V1_5
              sparse_embedding_model:
                allOf:
                  - type: string
                    description: The sparse embedding model to be used for indexes
                    enum:
                      - BM25
                      - BGE_M3
                    example: BM25
              endpoint:
                allOf:
                  - type: string
                    description: The REST endpoint of the index
                    example: glowing-baboon-15797-us1
              token:
                allOf:
                  - type: string
                    description: The REST authentication token for the index
                    example: >-
                      QkZGAsWp2tdW0tdC0zNzM1LWV1MkFkNQzB1ExUb3hOekF0TVRJbFpMDNLVSm1GZw==
              read_only_token:
                allOf:
                  - type: string
                    description: The REST authentication read only token for the index
                    example: >-
                      QkZGRk1heGSKC0MtdRlZC0zNzM1LWTj3pAV0Wm1aZ01p05qY3RNR0U0TkRtRt2s9azJU
              type:
                allOf:
                  - type: string
                    description: The payment plan of the index
                    enum:
                      - free
                      - payg
                      - fixed
                    example: fixed
              region:
                allOf:
                  - type: string
                    description: The region where the index is currently deployed
                    enum:
                      - eu-west-1
                      - us-east-1
                      - us-central-1
                    example: us-east-1
              max_vector_count:
                allOf:
                  - type: number
                    description: The number of maximum that your index can contain
                    example: 5210000
              max_daily_updates:
                allOf:
                  - type: number
                    description: >-
                      The number of maximum update operations you can perform in
                      a day. Only upsert operations are included in update
                      count.
                    example: 1000000
              max_daily_queries:
                allOf:
                  - type: number
                    description: >-
                      The number of maximum query operations you can perform in
                      a day. Only query operations are included in query count.
                    example: 1000000
              max_monthly_bandwidth:
                allOf:
                  - type: number
                    description: >-
                      The maximum amount of monthly bandwidth for the index.
                      Unit is bytes. -1 if the limit is unlimited.
                    example: -1
              max_writes_per_second:
                allOf:
                  - type: number
                    description: >-
                      The number of maximum write operations you can perform per
                      second. Only upsert operations are included in write
                      count.
                    example: 1000
              max_query_per_second:
                allOf:
                  - type: number
                    description: >-
                      The number of maximum query operations you can perform per
                      second. Only query operations are included in query count.
                    example: 1000
              max_reads_per_request:
                allOf:
                  - type: number
                    description: >-
                      The number of maximum vectors in a read operation. Query
                      and fetch operations are included in read operations.
                    example: 1000
              max_writes_per_request:
                allOf:
                  - type: number
                    description: >-
                      The number of maximum vectors in a write operation. Only
                      upsert operations are included in write operations.
                    example: 1000
              max_total_metadata_size:
                allOf:
                  - type: number
                    description: >-
                      The amount of maximum size for the total metadata sizes in
                      your index.
                    example: 53687091200
              reserved_price:
                allOf:
                  - type: number
                    description: >-
                      Monthly pricing of your index. Only available for fixed
                      and pro plans.
                    example: 60
              creation_time:
                allOf:
                  - type: number
                    description: >-
                      The creation time of the vector index in UTC as unix
                      timestamp.
                    example: 1753207106
              index_type:
                allOf:
                  - type: string
                    description: The type of the vector index
                    enum:
                      - DENSE
                      - SPARSE
                      - HYBRID
                    example: DENSE
              throughput_vector:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Throughput data for the vector index over time
                    example:
                      - x: 2025-09-04 14:55:00.000 +0000 UTC
                        'y': 0
                      - x: 2025-09-04 14:56:00.000 +0000 UTC
                        'y': 0
            refIdentifier: '#/components/schemas/VectorIndex'
        examples:
          example:
            value:
              customer_id: example@upstash.com
              id: 0639864f-ece6-429c-8118-86a287b0e808
              name: myindex
              similarity_function: COSINE
              dimension_count: 384
              embedding_model: BGE_SMALL_EN_V1_5
              sparse_embedding_model: BM25
              endpoint: glowing-baboon-15797-us1
              token: >-
                QkZGAsWp2tdW0tdC0zNzM1LWV1MkFkNQzB1ExUb3hOekF0TVRJbFpMDNLVSm1GZw==
              read_only_token: >-
                QkZGRk1heGSKC0MtdRlZC0zNzM1LWTj3pAV0Wm1aZ01p05qY3RNR0U0TkRtRt2s9azJU
              type: fixed
              region: us-east-1
              max_vector_count: 5210000
              max_daily_updates: 1000000
              max_daily_queries: 1000000
              max_monthly_bandwidth: -1
              max_writes_per_second: 1000
              max_query_per_second: 1000
              max_reads_per_request: 1000
              max_writes_per_request: 1000
              max_total_metadata_size: 53687091200
              reserved_price: 60
              creation_time: 1753207106
              index_type: DENSE
              throughput_vector:
                - x: 2025-09-04 14:55:00.000 +0000 UTC
                  'y': 0
                - x: 2025-09-04 14:56:00.000 +0000 UTC
                  'y': 0
        description: Index retrieved successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/vector/get_index
components:
  schemas:
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

````