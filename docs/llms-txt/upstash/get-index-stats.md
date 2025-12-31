# Source: https://upstash.com/docs/api-reference/vector/get-index-stats.md

# Source: https://upstash.com/docs/api-reference/search/get-index-stats.md

# Source: https://upstash.com/docs/api-reference/vector/get-index-stats.md

# Source: https://upstash.com/docs/api-reference/search/get-index-stats.md

# Source: https://upstash.com/docs/api-reference/vector/get-index-stats.md

# Source: https://upstash.com/docs/api-reference/search/get-index-stats.md

# Source: https://upstash.com/docs/api-reference/vector/get-index-stats.md

# Source: https://upstash.com/docs/api-reference/search/get-index-stats.md

# Source: https://upstash.com/docs/api-reference/vector/get-index-stats.md

# Source: https://upstash.com/docs/api-reference/search/get-index-stats.md

# Source: https://upstash.com/docs/api-reference/vector/get-index-stats.md

# Source: https://upstash.com/docs/api-reference/search/get-index-stats.md

# Source: https://upstash.com/docs/api-reference/vector/get-index-stats.md

# Get Index Stats

> Retrieves statistics and metrics for a specific vector index

## OpenAPI

````yaml devops/developer-api/openapi.yml get /vector/index/{id}/stats
paths:
  path: /vector/index/{id}/stats
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
              description: The ID of the vector index
      query:
        period:
          schema:
            - type: enum<string>
              enum:
                - 1h
                - 3h
                - 12h
                - 1d
                - 3d
                - 7d
                - 30d
              required: false
              description: >
                Time period for statistics aggregation. Each period returns 60
                datapoints 

                with intervals adjusted to the period length. 


                Exceptionally for 30 days, it returns 240 datapoints with 3-hour
                intervals for increased granularity.
              default: 1h
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              pending_index_count:
                allOf:
                  - type: integer
                    description: Number of pending index operations
                    example: 1
              current_vector_count:
                allOf:
                  - type: integer
                    description: Current number of vectors in the index
                    example: 1000
              daily_query_count:
                allOf:
                  - type: integer
                    description: Total number of query operations executed today
                    example: 100
              daily_update_count:
                allOf:
                  - type: integer
                    description: Total number of update operations executed today
                    example: 10
              monthly_query_count:
                allOf:
                  - type: integer
                    description: Total query operations in current month
                    example: 1000
              monthly_update_count:
                allOf:
                  - type: integer
                    description: Total update operations in current month
                    example: 1000
              monthly_bandwidth_usage:
                allOf:
                  - type: integer
                    description: Total bandwidth used in current month (bytes)
                    example: 7000
              storage_usage:
                allOf:
                  - type: integer
                    description: Current storage used (bytes)
                    example: 7000
              monthly_cost:
                allOf:
                  - type: number
                    format: float
                    description: Total cost in current month
                    example: 0.5
              daily_update_requests:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Daily update requests over time
                    example:
                      - x: 2025-10-19 18:33:05.244068975 +0000 UTC
                        'y': 1
              daily_query_requests:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Daily query requests over time
                    example:
                      - x: 2025-10-19 18:33:05.244068975 +0000 UTC
                        'y': 7
              daily_bandwidths:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Daily bandwidth usage over time
                    example:
                      - x: 2025-10-19 18:33:05.244068975 +0000 UTC
                        'y': 7
              days:
                allOf:
                  - type: array
                    items:
                      type: string
                    description: Days of the week for measurement
                    example:
                      - Sunday
                      - Monday
                      - Tuesday
                      - Wednesday
                      - Thursday
              query_throughput:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Query throughput over time
                    example:
                      - x: 2025-10-23 17:34:00.000 +0000 UTC
                        'y': 7
              update_throughput:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Update throughput over time
                    example:
                      - x: 2025-10-23 17:34:00.000 +0000 UTC
                        'y': 7
              query_latency_mean:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Average query latency over time
                    example:
                      - x: 2025-10-23 17:34:00.000 +0000 UTC
                        'y': 0
              query_latency_99:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: 99th percentile query latency over time
                    example:
                      - x: 2025-10-23 17:34:00.000 +0000 UTC
                        'y': 0
              update_latency_mean:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Average update latency over time
                    example:
                      - x: 2025-10-23 17:34:00.000 +0000 UTC
                        'y': 0
              update_latency_99:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: 99th percentile update latency over time
                    example:
                      - x: 2025-10-23 17:34:00.000 +0000 UTC
                        'y': 0
              embeds_latency_mean:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Average embedding latency over time
                    example:
                      - x: 2025-10-23 17:34:00.000 +0000 UTC
                        'y': 0
              embeds_latency_99:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: 99th percentile embedding latency over time
                    example:
                      - x: 2025-10-23 17:34:00.000 +0000 UTC
                        'y': 0
              vector_count:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Vector count over time
                    example:
                      - x: 2025-10-23 17:35:00.000 +0000 UTC
                        'y': 2
              data_size:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Data size over time
                    example:
                      - x: 2025-10-23 17:35:00.000 +0000 UTC
                        'y': 76
              daily_rerank_count:
                allOf:
                  - type: integer
                    description: Total number of rerank operations executed today
                    example: 0
              monthly_rerank_count:
                allOf:
                  - type: integer
                    description: Total rerank operations in current month
                    example: 10
              daily_rerank_requests:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Daily rerank requests over time
                    example:
                      - x: 2025-10-19 18:33:05.244068975 +0000 UTC
                        'y': 1
              rerank_latency_mean:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Average rerank latency over time
                    example:
                      - x: 2025-10-23 17:34:00.000 +0000 UTC
                        'y': 0
              rerank_latency_99:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: 99th percentile rerank latency over time
                    example:
                      - x: 2025-10-23 17:34:00.000 +0000 UTC
                        'y': 0
            refIdentifier: '#/components/schemas/VectorStats'
        examples:
          example:
            value:
              pending_index_count: 1
              current_vector_count: 1000
              daily_query_count: 100
              daily_update_count: 10
              monthly_query_count: 1000
              monthly_update_count: 1000
              monthly_bandwidth_usage: 7000
              storage_usage: 7000
              monthly_cost: 0.5
              daily_update_requests:
                - x: 2025-10-19 18:33:05.244068975 +0000 UTC
                  'y': 1
              daily_query_requests:
                - x: 2025-10-19 18:33:05.244068975 +0000 UTC
                  'y': 7
              daily_bandwidths:
                - x: 2025-10-19 18:33:05.244068975 +0000 UTC
                  'y': 7
              days:
                - Sunday
                - Monday
                - Tuesday
                - Wednesday
                - Thursday
              query_throughput:
                - x: 2025-10-23 17:34:00.000 +0000 UTC
                  'y': 7
              update_throughput:
                - x: 2025-10-23 17:34:00.000 +0000 UTC
                  'y': 7
              query_latency_mean:
                - x: 2025-10-23 17:34:00.000 +0000 UTC
                  'y': 0
              query_latency_99:
                - x: 2025-10-23 17:34:00.000 +0000 UTC
                  'y': 0
              update_latency_mean:
                - x: 2025-10-23 17:34:00.000 +0000 UTC
                  'y': 0
              update_latency_99:
                - x: 2025-10-23 17:34:00.000 +0000 UTC
                  'y': 0
              embeds_latency_mean:
                - x: 2025-10-23 17:34:00.000 +0000 UTC
                  'y': 0
              embeds_latency_99:
                - x: 2025-10-23 17:34:00.000 +0000 UTC
                  'y': 0
              vector_count:
                - x: 2025-10-23 17:35:00.000 +0000 UTC
                  'y': 2
              data_size:
                - x: 2025-10-23 17:35:00.000 +0000 UTC
                  'y': 76
              daily_rerank_count: 0
              monthly_rerank_count: 10
              daily_rerank_requests:
                - x: 2025-10-19 18:33:05.244068975 +0000 UTC
                  'y': 1
              rerank_latency_mean:
                - x: 2025-10-23 17:34:00.000 +0000 UTC
                  'y': 0
              rerank_latency_99:
                - x: 2025-10-23 17:34:00.000 +0000 UTC
                  'y': 0
        description: Statistics for the specified vector index retrieved successfully
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