# Source: https://checklyhq.com/docs/api-reference/analytics/icmp-monitors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# ICMP monitors

> Fetch detailed availability metrics and aggregated or non-aggregated ICMP Monitor metrics across custom time ranges. For example, you can get the p99 and p95 of latency metrics together with the packet loss percentage for any time range.
**Rate-limiting is applied to this endpoint, you can send 30 requests / 60 seconds at most.**



## OpenAPI

````yaml get /v1/analytics/icmp/{id}
openapi: 3.0.0
info:
  title: Checkly Public API
  version: v1
  description: >-
    These are the docs for the newly released Checkly Public API. If you have
    any questions, please do not hesitate to get in touch with us.
servers:
  - url: https://api.checklyhq.com
security:
  - Bearer: []
tags: []
paths:
  /v1/analytics/icmp/{id}:
    get:
      tags:
        - Analytics
      summary: ICMP monitors
      description: >-
        Fetch detailed availability metrics and aggregated or non-aggregated
        ICMP Monitor metrics across custom time ranges. For example, you can get
        the p99 and p95 of latency metrics together with the packet loss
        percentage for any time range.

        **Rate-limiting is applied to this endpoint, you can send 30 requests /
        60 seconds at most.**
      operationId: getV1AnalyticsIcmpId
      parameters:
        - name: x-checkly-account
          in: header
          schema:
            type: string
            description: >-
              Your Checkly account ID, you can find it at
              https://app.checklyhq.com/settings/account/general
            x-format:
              guid: true
          description: >-
            Your Checkly account ID, you can find it at
            https://app.checklyhq.com/settings/account/general
        - name: id
          in: path
          schema:
            type: string
            x-format:
              guid: true
          required: true
        - name: from
          in: query
          schema:
            type: string
            format: date
            description: >-
              Custom start time of reporting window in unix timestamp format.
              Setting a custom "from" timestamp overrides the use of any
              "quickRange".
          description: >-
            Custom start time of reporting window in unix timestamp format.
            Setting a custom "from" timestamp overrides the use of any
            "quickRange".
        - name: to
          in: query
          schema:
            type: string
            format: date
            description: >-
              Custom end time of reporting window in unix timestamp format.
              Setting a custom "to" timestamp overrides the use of any
              "quickRange".
          description: >-
            Custom end time of reporting window in unix timestamp format.
            Setting a custom "to" timestamp overrides the use of any
            "quickRange".
        - name: quickRange
          in: query
          schema:
            type: string
            description: >-
              Preset reporting windows are used for quickly generating report on
              commonly used windows. Can be overridden by using a custom "to"
              and "from" timestamp.
            default: last24Hours
            enum:
              - last24Hours
              - last7Days
              - last30Days
              - thisWeek
              - thisMonth
              - lastWeek
              - lastMonth
          description: >-
            Preset reporting windows are used for quickly generating report on
            commonly used windows. Can be overridden by using a custom "to" and
            "from" timestamp.
        - name: aggregationInterval
          in: query
          schema:
            type: number
            description: >-
              The time interval to use for aggregating metrics in minutes. For
              example, five minutes is 5, 24 hours is 1440.
            example: 1440
            minimum: 1
            maximum: 43200
          description: >-
            The time interval to use for aggregating metrics in minutes. For
            example, five minutes is 5, 24 hours is 1440.
        - name: filterByStatus
          in: query
          schema:
            type: array
            description: >-
              Filter based on whether a check result was either failing or
              passing
            example:
              - failure
            x-constraint:
              single: true
            items:
              type: string
              enum:
                - success
                - failure
          description: Filter based on whether a check result was either failing or passing
          style: form
          explode: true
        - name: groupBy
          in: query
          schema:
            type: string
            description: >-
              Determines how the series data is grouped. Note that grouped
              queries are a bit more expensive and might take longer.
            enum:
              - runLocation
          description: >-
            Determines how the series data is grouped. Note that grouped queries
            are a bit more expensive and might take longer.
        - name: metrics
          in: query
          schema:
            type: array
            description: >-
              Available metrics for ICMP Monitors. You can pass multiple metrics
              as a comma separated string.
            x-constraint:
              single: true
            items:
              type: string
              enum:
                - packetLoss
                - latencyMin
                - latencyMax
                - latencyAvg
                - latencyStdDev
                - availability
                - retries
                - packetLoss_avg
                - packetLoss_max
                - packetLoss_median
                - packetLoss_min
                - packetLoss_p50
                - packetLoss_p90
                - packetLoss_p95
                - packetLoss_p99
                - packetLoss_stddev
                - packetLoss_sum
                - latencyMin_avg
                - latencyMin_max
                - latencyMin_median
                - latencyMin_min
                - latencyMin_p50
                - latencyMin_p90
                - latencyMin_p95
                - latencyMin_p99
                - latencyMin_stddev
                - latencyMin_sum
                - latencyMax_avg
                - latencyMax_max
                - latencyMax_median
                - latencyMax_min
                - latencyMax_p50
                - latencyMax_p90
                - latencyMax_p95
                - latencyMax_p99
                - latencyMax_stddev
                - latencyMax_sum
                - latencyAvg_avg
                - latencyAvg_max
                - latencyAvg_median
                - latencyAvg_min
                - latencyAvg_p50
                - latencyAvg_p90
                - latencyAvg_p95
                - latencyAvg_p99
                - latencyAvg_stddev
                - latencyAvg_sum
                - latencyStdDev_avg
                - latencyStdDev_max
                - latencyStdDev_median
                - latencyStdDev_min
                - latencyStdDev_p50
                - latencyStdDev_p90
                - latencyStdDev_p95
                - latencyStdDev_p99
                - latencyStdDev_stddev
                - latencyStdDev_sum
          description: >-
            Available metrics for ICMP Monitors. You can pass multiple metrics
            as a comma separated string.
          style: form
          explode: true
          required: true
        - name: limit
          in: query
          schema:
            type: integer
            description: Limit the number of results
            default: 10
            minimum: 1
            maximum: 100
          description: Limit the number of results
        - name: page
          in: query
          schema:
            type: number
            description: Page number
            default: 1
            x-constraint:
              sign: positive
          description: Page number
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Model25'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UnauthorizedError'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ForbiddenError'
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TooManyRequestsError'
components:
  schemas:
    Model25:
      type: object
      properties:
        checkId:
          type: string
          x-format:
            guid: true
        name:
          type: string
        checkType:
          $ref: '#/components/schemas/Model24'
        activated:
          type: boolean
        muted:
          type: boolean
        frequency:
          type: number
        from:
          type: string
          format: date
        to:
          type: string
          format: date
        tags:
          $ref: '#/components/schemas/tags'
        series:
          $ref: '#/components/schemas/series'
        pagination:
          $ref: '#/components/schemas/pagination'
        metadata:
          type: object
          properties:
            string:
              $ref: '#/components/schemas/string'
    UnauthorizedError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 401
        error:
          $ref: '#/components/schemas/error'
        message:
          type: string
          example: Bad Token
        attributes:
          $ref: '#/components/schemas/attributes'
      required:
        - statusCode
        - error
    ForbiddenError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 403
        error:
          $ref: '#/components/schemas/Model1'
        message:
          type: string
          example: Forbidden
      required:
        - statusCode
        - error
    TooManyRequestsError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 429
        error:
          $ref: '#/components/schemas/Model2'
        message:
          type: string
          example: Too Many Requests
        attributes:
          $ref: '#/components/schemas/attributes'
      required:
        - statusCode
        - error
    Model24:
      type: string
      enum:
        - AGENTIC
        - API
        - BROWSER
        - HEARTBEAT
        - ICMP
        - MULTI_STEP
        - TCP
        - PLAYWRIGHT
        - URL
        - DNS
    tags:
      type: array
      items:
        type: string
    series:
      type: array
      items:
        type: string
    pagination:
      type: object
      properties:
        page:
          type: number
        limit:
          type: number
    string:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    error:
      type: string
      enum:
        - Unauthorized
    attributes:
      type: object
    Model1:
      type: string
      enum:
        - Forbidden
    Model2:
      type: string
      enum:
        - Too Many Requests
    unit:
      type: string
      enum:
        - milliseconds
        - score
        - count
        - percentage
    aggregation:
      type: string
      enum:
        - avg
        - max
        - median
        - min
        - p50
        - p90
        - p95
        - p99
        - stddev
        - sum
  securitySchemes:
    Bearer:
      type: http
      scheme: bearer
      bearerFormat: Bearer
      description: >-
        The Checkly Public API uses API keys to authenticate requests. You can
        get the API Key
        [here](https://app.checklyhq.com/settings/user/api-keys). Your API key
        is like a password:  keep it secure!

        Authentication to the API is performed using the Bearer auth method in
        the Authorization header and using the account ID.

        For example, set **Authorization** header while using cURL: `curl -H
        "Authorization: Bearer [apiKey]" "X-Checkly-Account: [accountId]"` 

````

Built with [Mintlify](https://mintlify.com).