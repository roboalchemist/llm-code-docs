# Source: https://checklyhq.com/docs/api-reference/analytics/tcp-checks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# TCP monitors

> Fetch detailed availability metrics and aggregated or non-aggregated TCP Check metrics across custom time ranges. For example, you can get the p99 and p95 of all the check phases of your TCP check together with the availability percentage for any time range.
**Rate-limiting is applied to this endpoint, you can send 30 requests / 60 seconds at most.**



## OpenAPI

````yaml get /v1/analytics/tcp-checks/{id}
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
  /v1/analytics/tcp-checks/{id}:
    get:
      tags:
        - Analytics
      summary: TCP checks
      description: >-
        Fetch detailed availability metrics and aggregated or non-aggregated TCP
        Check metrics across custom time ranges. For example, you can get the
        p99 and p95 of all the check phases of your TCP check together with the
        availability percentage for any time range.

        **Rate-limiting is applied to this endpoint, you can send 30 requests /
        60 seconds at most.**
      operationId: getV1AnalyticsTcpchecksId
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
              Available metrics for TCP Checks. You can pass multiple metrics as
              a comma separated string.
            x-constraint:
              single: true
            items:
              type: string
              enum:
                - total
                - dns
                - connection
                - data
                - availability
                - retries
                - total_avg
                - total_max
                - total_median
                - total_min
                - total_p50
                - total_p90
                - total_p95
                - total_p99
                - total_stddev
                - total_sum
                - dns_avg
                - dns_max
                - dns_median
                - dns_min
                - dns_p50
                - dns_p90
                - dns_p95
                - dns_p99
                - dns_stddev
                - dns_sum
                - connection_avg
                - connection_max
                - connection_median
                - connection_min
                - connection_p50
                - connection_p90
                - connection_p95
                - connection_p99
                - connection_stddev
                - connection_sum
                - data_avg
                - data_max
                - data_median
                - data_min
                - data_p50
                - data_p90
                - data_p95
                - data_p99
                - data_stddev
                - data_sum
          description: >-
            Available metrics for TCP Checks. You can pass multiple metrics as a
            comma separated string.
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
          description: Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Model35'
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
    Model35:
      type: object
      properties:
        checkId:
          type: string
          x-format:
            guid: true
        name:
          type: string
        checkType:
          $ref: '#/components/schemas/Model33'
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
          $ref: '#/components/schemas/Model34'
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
    Model33:
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
    Model34:
      type: object
      properties:
        total:
          $ref: '#/components/schemas/total'
        dns:
          $ref: '#/components/schemas/dns'
        connection:
          $ref: '#/components/schemas/connection'
        data:
          $ref: '#/components/schemas/data'
        availability:
          $ref: '#/components/schemas/availability'
        retries:
          $ref: '#/components/schemas/retries'
        total_avg:
          $ref: '#/components/schemas/total_avg'
        total_max:
          $ref: '#/components/schemas/total_max'
        total_median:
          $ref: '#/components/schemas/total_median'
        total_min:
          $ref: '#/components/schemas/total_min'
        total_p50:
          $ref: '#/components/schemas/total_p50'
        total_p90:
          $ref: '#/components/schemas/total_p90'
        total_p95:
          $ref: '#/components/schemas/total_p95'
        total_p99:
          $ref: '#/components/schemas/total_p99'
        total_stddev:
          $ref: '#/components/schemas/total_stddev'
        total_sum:
          $ref: '#/components/schemas/total_sum'
        dns_avg:
          $ref: '#/components/schemas/dns_avg'
        dns_max:
          $ref: '#/components/schemas/dns_max'
        dns_median:
          $ref: '#/components/schemas/dns_median'
        dns_min:
          $ref: '#/components/schemas/dns_min'
        dns_p50:
          $ref: '#/components/schemas/dns_p50'
        dns_p90:
          $ref: '#/components/schemas/dns_p90'
        dns_p95:
          $ref: '#/components/schemas/dns_p95'
        dns_p99:
          $ref: '#/components/schemas/dns_p99'
        dns_stddev:
          $ref: '#/components/schemas/dns_stddev'
        dns_sum:
          $ref: '#/components/schemas/dns_sum'
        connection_avg:
          $ref: '#/components/schemas/connection_avg'
        connection_max:
          $ref: '#/components/schemas/connection_max'
        connection_median:
          $ref: '#/components/schemas/connection_median'
        connection_min:
          $ref: '#/components/schemas/connection_min'
        connection_p50:
          $ref: '#/components/schemas/connection_p50'
        connection_p90:
          $ref: '#/components/schemas/connection_p90'
        connection_p95:
          $ref: '#/components/schemas/connection_p95'
        connection_p99:
          $ref: '#/components/schemas/connection_p99'
        connection_stddev:
          $ref: '#/components/schemas/connection_stddev'
        connection_sum:
          $ref: '#/components/schemas/connection_sum'
        data_avg:
          $ref: '#/components/schemas/data_avg'
        data_max:
          $ref: '#/components/schemas/data_max'
        data_median:
          $ref: '#/components/schemas/data_median'
        data_min:
          $ref: '#/components/schemas/data_min'
        data_p50:
          $ref: '#/components/schemas/data_p50'
        data_p90:
          $ref: '#/components/schemas/data_p90'
        data_p95:
          $ref: '#/components/schemas/data_p95'
        data_p99:
          $ref: '#/components/schemas/data_p99'
        data_stddev:
          $ref: '#/components/schemas/data_stddev'
        data_sum:
          $ref: '#/components/schemas/data_sum'
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
    total:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    dns:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    connection:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    data:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    availability:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    retries:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    total_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    total_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    total_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    total_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    total_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    total_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    total_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    total_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    total_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    total_sum:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    dns_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    dns_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    dns_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    dns_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    dns_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    dns_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    dns_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    dns_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    dns_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    dns_sum:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    connection_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    connection_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    connection_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    connection_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    connection_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    connection_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    connection_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    connection_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    connection_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    connection_sum:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    data_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    data_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    data_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    data_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    data_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    data_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    data_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    data_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    data_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    data_sum:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
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