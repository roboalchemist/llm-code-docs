# Source: https://checklyhq.com/docs/api-reference/analytics/url-monitors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# URL monitors

> Fetch detailed availability metrics and aggregated or non-aggregated API Check metrics across custom time ranges. For example, you can get the p99 and p95 of all the DNS phases of your API check together with the availability percentage for any time range.
**Rate-limiting is applied to this endpoint, you can send 30 requests / 60 seconds at most.**



## OpenAPI

````yaml get /v1/analytics/url-monitors/{id}
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
  /v1/analytics/url-monitors/{id}:
    get:
      tags:
        - Analytics
      summary: URL Monitors
      description: >-
        Fetch detailed availability metrics and aggregated or non-aggregated API
        Check metrics across custom time ranges. For example, you can get the
        p99 and p95 of all the DNS phases of your API check together with the
        availability percentage for any time range.

        **Rate-limiting is applied to this endpoint, you can send 30 requests /
        60 seconds at most.**
      operationId: getV1AnalyticsUrlmonitorsId
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
              - statusCode
          description: >-
            Determines how the series data is grouped. Note that grouped queries
            are a bit more expensive and might take longer.
        - name: metrics
          in: query
          schema:
            type: array
            description: >-
              Available metrics for API Checks. You can pass multiple metrics as
              a comma separated string.
            x-constraint:
              single: true
            items:
              type: string
              enum:
                - responseTime
                - wait
                - dns
                - tcp
                - firstByte
                - download
                - availability
                - retries
                - responseTime_avg
                - responseTime_max
                - responseTime_median
                - responseTime_min
                - responseTime_p50
                - responseTime_p90
                - responseTime_p95
                - responseTime_p99
                - responseTime_stddev
                - responseTime_sum
                - wait_avg
                - wait_max
                - wait_median
                - wait_min
                - wait_p50
                - wait_p90
                - wait_p95
                - wait_p99
                - wait_stddev
                - wait_sum
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
                - tcp_avg
                - tcp_max
                - tcp_median
                - tcp_min
                - tcp_p50
                - tcp_p90
                - tcp_p95
                - tcp_p99
                - tcp_stddev
                - tcp_sum
                - firstByte_avg
                - firstByte_max
                - firstByte_median
                - firstByte_min
                - firstByte_p50
                - firstByte_p90
                - firstByte_p95
                - firstByte_p99
                - firstByte_stddev
                - firstByte_sum
                - download_avg
                - download_max
                - download_median
                - download_min
                - download_p50
                - download_p90
                - download_p95
                - download_p99
                - download_stddev
                - download_sum
          description: >-
            Available metrics for API Checks. You can pass multiple metrics as a
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
                $ref: '#/components/schemas/Model37'
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
    Model37:
      type: object
      properties:
        checkId:
          type: string
          x-format:
            guid: true
        name:
          type: string
        checkType:
          $ref: '#/components/schemas/Model36'
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
          $ref: '#/components/schemas/metadata'
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
    Model36:
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
    metadata:
      type: object
      properties:
        responseTime:
          $ref: '#/components/schemas/responseTime'
        wait:
          $ref: '#/components/schemas/wait'
        dns:
          $ref: '#/components/schemas/dns'
        tcp:
          $ref: '#/components/schemas/tcp'
        firstByte:
          $ref: '#/components/schemas/firstByte'
        download:
          $ref: '#/components/schemas/download'
        availability:
          $ref: '#/components/schemas/availability'
        retries:
          $ref: '#/components/schemas/retries'
        responseTime_avg:
          $ref: '#/components/schemas/responseTime_avg'
        responseTime_max:
          $ref: '#/components/schemas/responseTime_max'
        responseTime_median:
          $ref: '#/components/schemas/responseTime_median'
        responseTime_min:
          $ref: '#/components/schemas/responseTime_min'
        responseTime_p50:
          $ref: '#/components/schemas/responseTime_p50'
        responseTime_p90:
          $ref: '#/components/schemas/responseTime_p90'
        responseTime_p95:
          $ref: '#/components/schemas/responseTime_p95'
        responseTime_p99:
          $ref: '#/components/schemas/responseTime_p99'
        responseTime_stddev:
          $ref: '#/components/schemas/responseTime_stddev'
        responseTime_sum:
          $ref: '#/components/schemas/responseTime_sum'
        wait_avg:
          $ref: '#/components/schemas/wait_avg'
        wait_max:
          $ref: '#/components/schemas/wait_max'
        wait_median:
          $ref: '#/components/schemas/wait_median'
        wait_min:
          $ref: '#/components/schemas/wait_min'
        wait_p50:
          $ref: '#/components/schemas/wait_p50'
        wait_p90:
          $ref: '#/components/schemas/wait_p90'
        wait_p95:
          $ref: '#/components/schemas/wait_p95'
        wait_p99:
          $ref: '#/components/schemas/wait_p99'
        wait_stddev:
          $ref: '#/components/schemas/wait_stddev'
        wait_sum:
          $ref: '#/components/schemas/wait_sum'
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
        tcp_avg:
          $ref: '#/components/schemas/tcp_avg'
        tcp_max:
          $ref: '#/components/schemas/tcp_max'
        tcp_median:
          $ref: '#/components/schemas/tcp_median'
        tcp_min:
          $ref: '#/components/schemas/tcp_min'
        tcp_p50:
          $ref: '#/components/schemas/tcp_p50'
        tcp_p90:
          $ref: '#/components/schemas/tcp_p90'
        tcp_p95:
          $ref: '#/components/schemas/tcp_p95'
        tcp_p99:
          $ref: '#/components/schemas/tcp_p99'
        tcp_stddev:
          $ref: '#/components/schemas/tcp_stddev'
        tcp_sum:
          $ref: '#/components/schemas/tcp_sum'
        firstByte_avg:
          $ref: '#/components/schemas/firstByte_avg'
        firstByte_max:
          $ref: '#/components/schemas/firstByte_max'
        firstByte_median:
          $ref: '#/components/schemas/firstByte_median'
        firstByte_min:
          $ref: '#/components/schemas/firstByte_min'
        firstByte_p50:
          $ref: '#/components/schemas/firstByte_p50'
        firstByte_p90:
          $ref: '#/components/schemas/firstByte_p90'
        firstByte_p95:
          $ref: '#/components/schemas/firstByte_p95'
        firstByte_p99:
          $ref: '#/components/schemas/firstByte_p99'
        firstByte_stddev:
          $ref: '#/components/schemas/firstByte_stddev'
        firstByte_sum:
          $ref: '#/components/schemas/firstByte_sum'
        download_avg:
          $ref: '#/components/schemas/download_avg'
        download_max:
          $ref: '#/components/schemas/download_max'
        download_median:
          $ref: '#/components/schemas/download_median'
        download_min:
          $ref: '#/components/schemas/download_min'
        download_p50:
          $ref: '#/components/schemas/download_p50'
        download_p90:
          $ref: '#/components/schemas/download_p90'
        download_p95:
          $ref: '#/components/schemas/download_p95'
        download_p99:
          $ref: '#/components/schemas/download_p99'
        download_stddev:
          $ref: '#/components/schemas/download_stddev'
        download_sum:
          $ref: '#/components/schemas/download_sum'
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
    responseTime:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    wait:
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
    tcp:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    firstByte:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    download:
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
    responseTime_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    responseTime_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    responseTime_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    responseTime_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    responseTime_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    responseTime_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    responseTime_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    responseTime_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    responseTime_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    responseTime_sum:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    wait_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    wait_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    wait_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    wait_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    wait_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    wait_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    wait_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    wait_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    wait_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    wait_sum:
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
    tcp_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    tcp_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    tcp_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    tcp_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    tcp_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    tcp_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    tcp_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    tcp_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    tcp_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    tcp_sum:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    firstByte_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    firstByte_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    firstByte_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    firstByte_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    firstByte_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    firstByte_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    firstByte_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    firstByte_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    firstByte_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    firstByte_sum:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    download_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    download_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    download_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    download_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    download_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    download_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    download_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    download_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    download_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    download_sum:
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