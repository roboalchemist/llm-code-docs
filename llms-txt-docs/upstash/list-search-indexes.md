# Source: https://upstash.com/docs/api-reference/search/list-search-indexes.md

# List Search Indexes

> Returns a list of all search indices belonging to the authenticated user.

## OpenAPI

````yaml devops/developer-api/openapi.yml get /search
paths:
  path: /search
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/SearchIndex'
        examples:
          example:
            value:
              - customer_id: example@upstash.com
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
        description: Successfully retrieved list of search indices.
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
    SearchIndex:
      type: object
      properties:
        customer_id:
          type: string
          description: The associated ID of the owner of the index
          example: example@upstash.com
        id:
          type: string
          format: uuid
          description: Unique ID of the index
          example: 99a4c327-31f0-490f-a594-043ade84085a
        name:
          type: string
          description: Name of the search index
          example: mySearchIndex
        endpoint:
          type: string
          description: The REST endpoint of the index
          example: glowing-baboon-15797-us1
        type:
          type: string
          description: The payment plan of the index
          enum:
            - free
            - payg
            - fixed
          example: payg
        region:
          type: string
          description: The region where the index is currently deployed
          enum:
            - eu-west-1
            - us-central1
          example: us-central1
        vercel_email:
          type: string
          description: >-
            The email associated with Vercel integration, if any. Empty string
            otherwise.
          example: example@vercel.com
        token:
          type: string
          description: The REST authentication token for the index
          example: ZXhhbXBsZUB1cHN0YXNoLmNvbTpuYWJlcg==
        read_only_token:
          type: string
          description: The REST authentication read only token for the search index
          example: ZXhhbXBsZUB1cHN0YXNoLmNvbTpuYWJlcg==
        max_vector_count:
          type: integer
          description: Maximum number of vectors allowed in the index
          example: 2000000
        max_monthly_reranks:
          type: integer
          description: Maximum monthly rerank operations (-1 for unlimited)
          example: -1
        max_daily_updates:
          type: integer
          description: Maximum daily update operations (-1 for unlimited)
          example: -1
        max_daily_queries:
          type: integer
          description: Maximum daily query operations (-1 for unlimited)
          example: -1
        max_monthly_bandwidth:
          type: integer
          description: Maximum monthly bandwidth in bytes (-1 for unlimited)
          example: -1
        max_writes_per_second:
          type: integer
          description: Maximum write operations per second (rate limit)
          example: 1000
        max_query_per_second:
          type: integer
          description: Maximum query operations per second (rate limit)
          example: 1000
        max_reads_per_request:
          type: integer
          description: Maximum number of reads allowed per request
          example: 100
        max_writes_per_request:
          type: integer
          description: Maximum number of writes allowed per request
          example: 100
        creation_time:
          type: integer
          format: int64
          description: Unix timestamp of creation
          example: 1761200000
        input_enrichment_enabled:
          type: boolean
          description: Whether input enrichment is enabled for this index
          example: true
        throughput_vector:
          type: array
          items:
            $ref: '#/components/schemas/TimeSeriesData'
          description: Throughput metrics over time
          example:
            - x: 2025-10-23 20:54:00.000 +0000 UTC
              'y': 0

````