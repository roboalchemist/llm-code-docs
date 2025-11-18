# Source: https://upstash.com/docs/devops/developer-api/redis/get_database_stats.md

# Get Database Stats

> This endpoint gets detailed stats of a database.

## OpenAPI

````yaml devops/developer-api/openapi.yml get /redis/stats/{id}
paths:
  path: /redis/stats/{id}
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
              description: The ID of the database
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
              monitor_count:
                allOf:
                  - $ref: '#/components/schemas/TimeSeriesData'
                    description: Monitor count
              daily_net_commands:
                allOf:
                  - type: integer
                    description: Total number of commands executed today
                    example: 7
              daily_read_requests:
                allOf:
                  - type: integer
                    description: Total number of read requests executed today
                    example: 7
              daily_write_requests:
                allOf:
                  - type: integer
                    description: Total number of write requests executed today
                    example: 0
              connection_count:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Connection count over time
                    example:
                      - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                        'y': 0
              keyspace:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Total number of keys in the database over time
                    example:
                      - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                        'y': 0
              throughput:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Throughput on database connections over time
                    example:
                      - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                        'y': 0
              diskusage:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Disk usage over time
                    example:
                      - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                        'y': 0
              latencymean:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Average latency over time
                    example:
                      - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                        'y': 0
              latency_99:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: 99th percentile latency over time
                    example:
                      - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                        'y': 0
              read_latency_mean:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Average read latency over time
                    example:
                      - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                        'y': 0
              read_latency_99:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: 99th percentile read latency over time
                    example:
                      - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                        'y': 0
              write_latency_mean:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Average write latency over time
                    example:
                      - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                        'y': 0
              write_latency_99:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: 99th percentile write latency over time
                    example:
                      - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                        'y': 0
              hits:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Cache hits over time
                    example:
                      - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                        'y': 0
              misses:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Cache misses over time
                    example:
                      - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                        'y': 0
              read:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Read requests over time
                    example:
                      - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                        'y': 0
              write:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Write requests over time
                    example:
                      - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                        'y': 0
              dailyrequests:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Daily requests over time
                    example:
                      - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                        'y': 0
                      - x: 2025-09-04 15:12:52.76649148 +0000 UTC
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
              dailybilling:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Daily billing amounts over time
                    example:
                      - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                        'y': 0
                      - x: 2025-09-04 15:12:52.76649148 +0000 UTC
                        'y': 1.333
              dailybandwidth:
                allOf:
                  - type: integer
                    description: Total daily bandwidth usage in bytes
                    example: 50444740913
              bandwidths:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Bandwidth usage over time
                    example:
                      - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                        'y': 0
                      - x: 2025-09-04 15:12:52.76649148 +0000 UTC
                        'y': 7
              total_monthly_bandwidth:
                allOf:
                  - type: integer
                    description: Total bandwidth used in current month (bytes)
                    example: 7
              total_monthly_requests:
                allOf:
                  - type: integer
                    description: Total requests in current month
                    example: 7
              total_monthly_read_requests:
                allOf:
                  - type: integer
                    description: Total read requests in current month
                    example: 7
              total_monthly_write_requests:
                allOf:
                  - type: integer
                    description: Total write requests in current month
                    example: 0
              total_monthly_script_requests:
                allOf:
                  - type: integer
                    description: Total script requests in current month
                    example: 0
              queue_optimized:
                allOf:
                  - type: boolean
                    description: Whether queue optimization is enabled for the database
                    example: false
              total_monthly_storage:
                allOf:
                  - type: integer
                    description: Total storage used in current month (bytes)
                    example: 0
              current_storage:
                allOf:
                  - type: integer
                    description: Current storage used (bytes)
                    example: 0
              total_monthly_billing:
                allOf:
                  - type: number
                    format: float
                    description: Total cost in current month
                    example: 222.33902763855485
              command_counts:
                allOf:
                  - type: array
                    description: Command-specific counts over time
                    items:
                      $ref: '#/components/schemas/CommandCount'
                    example:
                      - metric_identifier: EXISTS
                        data_points:
                          - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                            'y': 0
            refIdentifier: '#/components/schemas/DatabaseStats'
        examples:
          example:
            value:
              monitor_count:
                x: 2023-05-22 10:59:23.426 +0000 UTC
                'y': 320
              daily_net_commands: 7
              daily_read_requests: 7
              daily_write_requests: 0
              connection_count:
                - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                  'y': 0
              keyspace:
                - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                  'y': 0
              throughput:
                - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                  'y': 0
              diskusage:
                - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                  'y': 0
              latencymean:
                - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                  'y': 0
              latency_99:
                - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                  'y': 0
              read_latency_mean:
                - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                  'y': 0
              read_latency_99:
                - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                  'y': 0
              write_latency_mean:
                - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                  'y': 0
              write_latency_99:
                - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                  'y': 0
              hits:
                - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                  'y': 0
              misses:
                - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                  'y': 0
              read:
                - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                  'y': 0
              write:
                - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                  'y': 0
              dailyrequests:
                - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                  'y': 0
                - x: 2025-09-04 15:12:52.76649148 +0000 UTC
                  'y': 7
              days:
                - Sunday
                - Monday
                - Tuesday
                - Wednesday
                - Thursday
              dailybilling:
                - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                  'y': 0
                - x: 2025-09-04 15:12:52.76649148 +0000 UTC
                  'y': 1.333
              dailybandwidth: 50444740913
              bandwidths:
                - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                  'y': 0
                - x: 2025-09-04 15:12:52.76649148 +0000 UTC
                  'y': 7
              total_monthly_bandwidth: 7
              total_monthly_requests: 7
              total_monthly_read_requests: 7
              total_monthly_write_requests: 0
              total_monthly_script_requests: 0
              queue_optimized: false
              total_monthly_storage: 0
              current_storage: 0
              total_monthly_billing: 222.33902763855485
              command_counts:
                - metric_identifier: EXISTS
                  data_points:
                    - x: 2025-08-31 15:12:52.799480932 +0000 UTC
                      'y': 0
        description: Database stats retrieved successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/redis/get_database_stats
components:
  schemas:
    CommandCount:
      type: object
      properties:
        metric_identifier:
          type: string
          description: Command name or metric identifier
          example: EXISTS
        data_points:
          type: array
          items:
            $ref: '#/components/schemas/TimeSeriesData'
          description: Data points for the given command
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