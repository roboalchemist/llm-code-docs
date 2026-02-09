# Source: https://upstash.com/docs/api-reference/qstash/get-qstash-stats.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get QStash Stats

> Retrieves detailed usage statistics for the QStash account including 
daily requests, billing, bandwidth, and workflow metrics over time.




## OpenAPI

````yaml devops/developer-api/openapi.yml get /qstash/stats
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
  /qstash/stats:
    get:
      tags:
        - qstash
      summary: Get QStash Stats
      description: |
        Retrieves detailed usage statistics for the QStash account including 
        daily requests, billing, bandwidth, and workflow metrics over time.
      operationId: getQStashStats
      parameters:
        - name: period
          in: query
          required: false
          schema:
            type: string
            enum:
              - 1h
              - 3h
              - 12h
              - 1d
              - 3d
              - 7d
              - 30d
            default: 1h
          description: >
            Time period for statistics aggregation. Each period returns 60
            datapoints 

            with intervals adjusted to the period length. 


            Exceptionally for 30 days, it returns 240 datapoints with 3-hour
            intervals for increased granularity.
          example: 3h
      responses:
        '200':
          description: Successful response with usage statistics
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QStashStats'
      security:
        - basicAuth: []
components:
  schemas:
    QStashStats:
      type: object
      properties:
        days:
          type: array
          items:
            type: string
          description: >
            Array of day names for the measurement period, typically
            representing all days in the current month.

            This includes both past and future dates within the current month,
            so the array covers the entire month regardless of the current day.

            Future days are included to align with other daily metrics arrays,
            allowing for consistent indexing.
          example:
            - Wednesday
            - Thursday
            - Friday
            - Saturday
            - Sunday
            - Monday
            - Tuesday
        daily_requests:
          type: array
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
          type: array
          items:
            $ref: '#/components/schemas/TimeSeriesData'
          description: Daily billing amounts over time
          example:
            - x: 2025-10-01 11:33:05.585757103 +0000 UTC
              'y': 0
        daily_bandwidths:
          type: array
          items:
            $ref: '#/components/schemas/TimeSeriesData'
          description: Daily bandwidth usage over time
          example:
            - x: 2025-10-01 11:33:05.585757103 +0000 UTC
              'y': 0
        daily_used:
          type: array
          items:
            $ref: '#/components/schemas/TimeSeriesData'
          description: >
            Request counts for the requested time period

            If 1h is specified, it shows 60 data points for every 1 minute
            within the last 1 hour.
          example:
            - x: 2025-10-01 11:33:05.585757103 +0000 UTC
              'y': 0
        daily_used_workflow:
          type: array
          items:
            $ref: '#/components/schemas/TimeSeriesData'
          description: >
            Workflow usage metrics for the requested time period

            If 1h is specified, it shows 60 data points for every 1 minute
            within the last 1 hour.
          example:
            - x: 2025-10-01 11:33:05.585757103 +0000 UTC
              'y': 0
        daily_qstash_messages:
          type: array
          items:
            $ref: '#/components/schemas/TimeSeriesWithId'
          description: >
            QStash message counts broken down by metric identifier for the
            requested time period.

            If 1h is specified, it shows 60 data points for every 1 minute
            within the last 1 hour.
          example:
            - id: delivered
              data_points:
                - x: 2023-05-22 10:59:23.426 +0000 UTC
                  'y': 320
                - x: 2023-05-22 11:00:23.426 +0000 UTC
                  'y': 450
        daily_workflow_messages:
          type: array
          items:
            $ref: '#/components/schemas/TimeSeriesWithId'
          description: >
            Workflow metrics broken down by metric identifier for the requested
            time period.

            If 1h is specified, it shows 60 data points for every 1 minute
            within the last 1 hour.
          example:
            - id: canceled
              data_points:
                - x: 2023-05-22 10:59:23.426 +0000 UTC
                  'y': 320
                - x: 2023-05-22 11:00:23.426 +0000 UTC
                  'y': 450
        dlq_message_count:
          type: integer
          description: Current number of messages in the dead letter queue
          example: 0
        daily_bandwidth_used:
          type: array
          items:
            $ref: '#/components/schemas/TimeSeriesData'
          description: >
            Bandwidth usage for the requested time period

            If 1h is specified, it shows 60 data points for every 1 minute
            within the last 1 hour.
          example:
            - x: 2025-10-01 11:33:05.585757103 +0000 UTC
              'y': 0
        total_monthly_billing:
          type: number
          format: float
          description: Total billing amount for the current month
          example: 5.806
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
  securitySchemes:
    basicAuth:
      type: http
      scheme: basic

````