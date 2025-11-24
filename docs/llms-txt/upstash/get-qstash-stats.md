# Source: https://upstash.com/docs/api-reference/qstash/get-qstash-stats.md

# Get QStash Stats

> Retrieves detailed usage statistics for the QStash account including 
daily requests, billing, bandwidth, and workflow metrics over time.


## OpenAPI

````yaml devops/developer-api/openapi.yml get /qstash/stats
paths:
  path: /qstash/stats
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
              days:
                allOf:
                  - type: array
                    items:
                      type: string
                    description: >
                      Array of day names for the measurement period, typically
                      representing all days in the current month.

                      This includes both past and future dates within the
                      current month, so the array covers the entire month
                      regardless of the current day.

                      Future days are included to align with other daily metrics
                      arrays, allowing for consistent indexing.
                    example:
                      - Wednesday
                      - Thursday
                      - Friday
                      - Saturday
                      - Sunday
                      - Monday
                      - Tuesday
              daily_requests:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        x:
                          type: string
                          description: Timestamp in UTC format
                          example: 2025-10-01 11:33:05.585757103 +0000 UTC
                        'y':
                          type: number
                          description: Total request count for this day
                          example: 0
                        workflow_message:
                          type: integer
                          description: Number of workflow messages for this day
                          example: 0
                        workflow_run:
                          type: integer
                          description: Number of workflow runs for this day
                          example: 0
                    description: Daily request metrics including workflow breakdowns
                    example:
                      - x: 2025-10-01 11:33:05.585757103 +0000 UTC
                        'y': 0
                        workflow_message: 0
                        workflow_run: 0
              daily_billings:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Daily billing amounts over time
                    example:
                      - x: 2025-10-01 11:33:05.585757103 +0000 UTC
                        'y': 0
              daily_bandwidths:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: Daily bandwidth usage over time
                    example:
                      - x: 2025-10-01 11:33:05.585757103 +0000 UTC
                        'y': 0
              daily_used:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: >
                      Request counts for the requested time period

                      If 1h is specified, it shows 60 data points for every 1
                      minute within the last 1 hour.
                    example:
                      - x: 2025-10-01 11:33:05.585757103 +0000 UTC
                        'y': 0
              daily_used_workflow:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: >
                      Workflow usage metrics for the requested time period

                      If 1h is specified, it shows 60 data points for every 1
                      minute within the last 1 hour.
                    example:
                      - x: 2025-10-01 11:33:05.585757103 +0000 UTC
                        'y': 0
              daily_qstash_messages:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesWithId'
                    description: >
                      QStash message counts broken down by metric identifier for
                      the requested time period.

                      If 1h is specified, it shows 60 data points for every 1
                      minute within the last 1 hour.
                    example:
                      - id: delivered
                        data_points:
                          - x: 2023-05-22 10:59:23.426 +0000 UTC
                            'y': 320
                          - x: 2023-05-22 11:00:23.426 +0000 UTC
                            'y': 450
              daily_workflow_messages:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesWithId'
                    description: >
                      Workflow metrics broken down by metric identifier for the
                      requested time period.

                      If 1h is specified, it shows 60 data points for every 1
                      minute within the last 1 hour.
                    example:
                      - id: canceled
                        data_points:
                          - x: 2023-05-22 10:59:23.426 +0000 UTC
                            'y': 320
                          - x: 2023-05-22 11:00:23.426 +0000 UTC
                            'y': 450
              dlq_message_count:
                allOf:
                  - type: integer
                    description: Current number of messages in the dead letter queue
                    example: 0
              daily_bandwidth_used:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/TimeSeriesData'
                    description: >
                      Bandwidth usage for the requested time period

                      If 1h is specified, it shows 60 data points for every 1
                      minute within the last 1 hour.
                    example:
                      - x: 2025-10-01 11:33:05.585757103 +0000 UTC
                        'y': 0
              total_monthly_billing:
                allOf:
                  - type: number
                    format: float
                    description: Total billing amount for the current month
                    example: 5.806
            refIdentifier: '#/components/schemas/QStashStats'
        examples:
          example:
            value:
              days:
                - Wednesday
                - Thursday
                - Friday
                - Saturday
                - Sunday
                - Monday
                - Tuesday
              daily_requests:
                - x: 2025-10-01 11:33:05.585757103 +0000 UTC
                  'y': 0
                  workflow_message: 0
                  workflow_run: 0
              daily_billings:
                - x: 2025-10-01 11:33:05.585757103 +0000 UTC
                  'y': 0
              daily_bandwidths:
                - x: 2025-10-01 11:33:05.585757103 +0000 UTC
                  'y': 0
              daily_used:
                - x: 2025-10-01 11:33:05.585757103 +0000 UTC
                  'y': 0
              daily_used_workflow:
                - x: 2025-10-01 11:33:05.585757103 +0000 UTC
                  'y': 0
              daily_qstash_messages:
                - id: delivered
                  data_points:
                    - x: 2023-05-22 10:59:23.426 +0000 UTC
                      'y': 320
                    - x: 2023-05-22 11:00:23.426 +0000 UTC
                      'y': 450
              daily_workflow_messages:
                - id: canceled
                  data_points:
                    - x: 2023-05-22 10:59:23.426 +0000 UTC
                      'y': 320
                    - x: 2023-05-22 11:00:23.426 +0000 UTC
                      'y': 450
              dlq_message_count: 0
              daily_bandwidth_used:
                - x: 2025-10-01 11:33:05.585757103 +0000 UTC
                  'y': 0
              total_monthly_billing: 5.806
        description: Successful response with usage statistics
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
    TimeSeriesWithId:
      type: object
      properties:
        id:
          type: string
          description: Identifier for the time series data
          example: example_id
        data_points:
          type: array
          items:
            $ref: '#/components/schemas/TimeSeriesData'
          description: Data points for the time series
          example:
            - x: 2023-05-22 10:59:23.426 +0000 UTC
              'y': 320
            - x: 2023-05-22 11:00:23.426 +0000 UTC
              'y': 450

````