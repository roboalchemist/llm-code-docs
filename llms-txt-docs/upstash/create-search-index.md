# Source: https://upstash.com/docs/api-reference/search/create-search-index.md

# Create Search Index

> Creates a new search index with the specified configuration

## OpenAPI

````yaml devops/developer-api/openapi.yml post /search
paths:
  path: /search
  method: post
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    description: Name of the search index
                    example: mySearchIndex
              region:
                allOf:
                  - type: string
                    enum:
                      - eu-west-1
                      - us-central1
                    description: Region of the index
                    example: eu-west-1
              type:
                allOf:
                  - type: string
                    enum:
                      - free
                      - payg
                      - fixed
                    description: >-
                      Index payment type. Currently 'free' and 'payg' are
                      available.
                    example: payg
            required: true
            requiredProperties:
              - name
              - region
              - type
        examples:
          example:
            value:
              name: mySearchIndex
              region: eu-west-1
              type: payg
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
                    format: uuid
                    description: Unique ID of the index
                    example: 99a4c327-31f0-490f-a594-043ade84085a
              name:
                allOf:
                  - type: string
                    description: Name of the search index
                    example: mySearchIndex
              endpoint:
                allOf:
                  - type: string
                    description: The REST endpoint of the index
                    example: glowing-baboon-15797-us1
              type:
                allOf:
                  - type: string
                    description: The payment plan of the index
                    enum:
                      - free
                      - payg
                      - fixed
                    example: payg
              region:
                allOf:
                  - type: string
                    description: The region where the index is currently deployed
                    enum:
                      - eu-west-1
                      - us-central1
                    example: us-central1
              vercel_email:
                allOf:
                  - type: string
                    description: >-
                      The email associated with Vercel integration, if any.
                      Empty string otherwise.
                    example: example@vercel.com
              token:
                allOf:
                  - type: string
                    description: The REST authentication token for the index
                    example: ZXhhbXBsZUB1cHN0YXNoLmNvbTpuYWJlcg==
              read_only_token:
                allOf:
                  - type: string
                    description: >-
                      The REST authentication read only token for the search
                      index
                    example: ZXhhbXBsZUB1cHN0YXNoLmNvbTpuYWJlcg==
              max_vector_count:
                allOf:
                  - type: integer
                    description: Maximum number of vectors allowed in the index
                    example: 2000000
              max_monthly_reranks:
                allOf:
                  - type: integer
                    description: Maximum monthly rerank operations (-1 for unlimited)
                    example: -1
              max_daily_updates:
                allOf:
                  - type: integer
                    description: Maximum daily update operations (-1 for unlimited)
                    example: -1
              max_daily_queries:
                allOf:
                  - type: integer
                    description: Maximum daily query operations (-1 for unlimited)
                    example: -1
              max_monthly_bandwidth:
                allOf:
                  - type: integer
                    description: Maximum monthly bandwidth in bytes (-1 for unlimited)
                    example: -1
              max_writes_per_second:
                allOf:
                  - type: integer
                    description: Maximum write operations per second (rate limit)
                    example: 1000
              max_query_per_second:
                allOf:
                  - type: integer
                    description: Maximum query operations per second (rate limit)
                    example: 1000
              max_reads_per_request:
                allOf:
                  - type: integer
                    description: Maximum number of reads allowed per request
                    example: 100
              max_writes_per_request:
                allOf:
                  - type: integer
                    description: Maximum number of writes allowed per request
                    example: 100
              creation_time:
                allOf:
                  - type: integer
                    format: int64
                    description: Unix timestamp of creation
                    example: 1761200000
              input_enrichment_enabled:
                allOf:
                  - type: boolean
                    description: Whether input enrichment is enabled for this index
                    example: true
              throughput_vector:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Throughput metrics over time
                    example:
                      - x: 2025-10-23 20:54:00.000 +0000 UTC
                        'y': 0
            refIdentifier: '#/components/schemas/SearchIndex'
        examples:
          example:
            value:
              customer_id: example@upstash.com
              id: 99a4c327-31f0-490f-a594-043ade84085a
              name: mySearchIndex
              endpoint: glowing-baboon-15797-us1
              type: payg
              region: us-central1
              vercel_email: example@vercel.com
              token: ZXhhbXBsZUB1cHN0YXNoLmNvbTpuYWJlcg==
              read_only_token: ZXhhbXBsZUB1cHN0YXNoLmNvbTpuYWJlcg==
              max_vector_count: 2000000
              max_monthly_reranks: -1
              max_daily_updates: -1
              max_daily_queries: -1
              max_monthly_bandwidth: -1
              max_writes_per_second: 1000
              max_query_per_second: 1000
              max_reads_per_request: 100
              max_writes_per_request: 100
              creation_time: 1761200000
              input_enrichment_enabled: true
              throughput_vector:
                - x: 2025-10-23 20:54:00.000 +0000 UTC
                  'y': 0
        description: Index created successfully
  deprecated: false
  type: path
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