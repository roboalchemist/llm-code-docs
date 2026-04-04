# Source: https://checklyhq.com/docs/api-reference/analytics/browser-checks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Browser checks

> Fetch detailed availability metrics and aggregated or non-aggregated Browser Check metrics across custom time ranges.  For example, you can get the average amount of console errors, the p99 of your FCP and the standard deviation of your TTFB for the second page in your Browser check with one API call.
**Rate-limiting is applied to this endpoint, you can send 30 requests / 60 seconds at most.**



## OpenAPI

````yaml get /v1/analytics/browser-checks/{id}
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
  /v1/analytics/browser-checks/{id}:
    get:
      tags:
        - Analytics
      summary: Browser checks
      description: >-
        Fetch detailed availability metrics and aggregated or non-aggregated
        Browser Check metrics across custom time ranges.  For example, you can
        get the average amount of console errors, the p99 of your FCP and the
        standard deviation of your TTFB for the second page in your Browser
        check with one API call.

        **Rate-limiting is applied to this endpoint, you can send 30 requests /
        60 seconds at most.**
      operationId: getV1AnalyticsBrowserchecksId
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
              - pageIndex
          description: >-
            Determines how the series data is grouped. Note that grouped queries
            are a bit more expensive and might take longer.
        - name: metrics
          in: query
          schema:
            type: array
            description: >-
              Available metrics for Browser Checks. You can pass multiple
              metrics as a comma separated string.
            x-constraint:
              single: true
            items:
              type: string
              enum:
                - responseTime
                - TTFB
                - FCP
                - LCP
                - CLS
                - TBT
                - consoleErrors
                - networkErrors
                - userScriptErrors
                - documentErrors
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
                - TTFB_avg
                - TTFB_max
                - TTFB_median
                - TTFB_min
                - TTFB_p50
                - TTFB_p90
                - TTFB_p95
                - TTFB_p99
                - TTFB_stddev
                - TTFB_sum
                - FCP_avg
                - FCP_max
                - FCP_median
                - FCP_min
                - FCP_p50
                - FCP_p90
                - FCP_p95
                - FCP_p99
                - FCP_stddev
                - FCP_sum
                - LCP_avg
                - LCP_max
                - LCP_median
                - LCP_min
                - LCP_p50
                - LCP_p90
                - LCP_p95
                - LCP_p99
                - LCP_stddev
                - LCP_sum
                - CLS_avg
                - CLS_max
                - CLS_median
                - CLS_min
                - CLS_p50
                - CLS_p90
                - CLS_p95
                - CLS_p99
                - CLS_stddev
                - CLS_sum
                - TBT_avg
                - TBT_max
                - TBT_median
                - TBT_min
                - TBT_p50
                - TBT_p90
                - TBT_p95
                - TBT_p99
                - TBT_stddev
                - TBT_sum
                - consoleErrors_avg
                - consoleErrors_max
                - consoleErrors_median
                - consoleErrors_min
                - consoleErrors_p50
                - consoleErrors_p90
                - consoleErrors_p95
                - consoleErrors_p99
                - consoleErrors_stddev
                - consoleErrors_sum
                - networkErrors_avg
                - networkErrors_max
                - networkErrors_median
                - networkErrors_min
                - networkErrors_p50
                - networkErrors_p90
                - networkErrors_p95
                - networkErrors_p99
                - networkErrors_stddev
                - networkErrors_sum
                - userScriptErrors_avg
                - userScriptErrors_max
                - userScriptErrors_median
                - userScriptErrors_min
                - userScriptErrors_p50
                - userScriptErrors_p90
                - userScriptErrors_p95
                - userScriptErrors_p99
                - userScriptErrors_stddev
                - userScriptErrors_sum
                - documentErrors_avg
                - documentErrors_max
                - documentErrors_median
                - documentErrors_min
                - documentErrors_p50
                - documentErrors_p90
                - documentErrors_p95
                - documentErrors_p99
                - documentErrors_stddev
                - documentErrors_sum
          description: >-
            Available metrics for Browser Checks. You can pass multiple metrics
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
          description: Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Model13'
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
    Model13:
      type: object
      properties:
        checkId:
          type: string
          x-format:
            guid: true
        name:
          type: string
        checkType:
          $ref: '#/components/schemas/Model11'
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
          $ref: '#/components/schemas/Model12'
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
    Model11:
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
    Model12:
      type: object
      properties:
        responseTime:
          $ref: '#/components/schemas/responseTime'
        TTFB:
          $ref: '#/components/schemas/TTFB'
        FCP:
          $ref: '#/components/schemas/FCP'
        LCP:
          $ref: '#/components/schemas/LCP'
        CLS:
          $ref: '#/components/schemas/CLS'
        TBT:
          $ref: '#/components/schemas/TBT'
        consoleErrors:
          $ref: '#/components/schemas/consoleErrors'
        networkErrors:
          $ref: '#/components/schemas/networkErrors'
        userScriptErrors:
          $ref: '#/components/schemas/userScriptErrors'
        documentErrors:
          $ref: '#/components/schemas/documentErrors'
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
        TTFB_avg:
          $ref: '#/components/schemas/TTFB_avg'
        TTFB_max:
          $ref: '#/components/schemas/TTFB_max'
        TTFB_median:
          $ref: '#/components/schemas/TTFB_median'
        TTFB_min:
          $ref: '#/components/schemas/TTFB_min'
        TTFB_p50:
          $ref: '#/components/schemas/TTFB_p50'
        TTFB_p90:
          $ref: '#/components/schemas/TTFB_p90'
        TTFB_p95:
          $ref: '#/components/schemas/TTFB_p95'
        TTFB_p99:
          $ref: '#/components/schemas/TTFB_p99'
        TTFB_stddev:
          $ref: '#/components/schemas/TTFB_stddev'
        TTFB_sum:
          $ref: '#/components/schemas/TTFB_sum'
        FCP_avg:
          $ref: '#/components/schemas/FCP_avg'
        FCP_max:
          $ref: '#/components/schemas/FCP_max'
        FCP_median:
          $ref: '#/components/schemas/FCP_median'
        FCP_min:
          $ref: '#/components/schemas/FCP_min'
        FCP_p50:
          $ref: '#/components/schemas/FCP_p50'
        FCP_p90:
          $ref: '#/components/schemas/FCP_p90'
        FCP_p95:
          $ref: '#/components/schemas/FCP_p95'
        FCP_p99:
          $ref: '#/components/schemas/FCP_p99'
        FCP_stddev:
          $ref: '#/components/schemas/FCP_stddev'
        FCP_sum:
          $ref: '#/components/schemas/FCP_sum'
        LCP_avg:
          $ref: '#/components/schemas/LCP_avg'
        LCP_max:
          $ref: '#/components/schemas/LCP_max'
        LCP_median:
          $ref: '#/components/schemas/LCP_median'
        LCP_min:
          $ref: '#/components/schemas/LCP_min'
        LCP_p50:
          $ref: '#/components/schemas/LCP_p50'
        LCP_p90:
          $ref: '#/components/schemas/LCP_p90'
        LCP_p95:
          $ref: '#/components/schemas/LCP_p95'
        LCP_p99:
          $ref: '#/components/schemas/LCP_p99'
        LCP_stddev:
          $ref: '#/components/schemas/LCP_stddev'
        LCP_sum:
          $ref: '#/components/schemas/LCP_sum'
        CLS_avg:
          $ref: '#/components/schemas/CLS_avg'
        CLS_max:
          $ref: '#/components/schemas/CLS_max'
        CLS_median:
          $ref: '#/components/schemas/CLS_median'
        CLS_min:
          $ref: '#/components/schemas/CLS_min'
        CLS_p50:
          $ref: '#/components/schemas/CLS_p50'
        CLS_p90:
          $ref: '#/components/schemas/CLS_p90'
        CLS_p95:
          $ref: '#/components/schemas/CLS_p95'
        CLS_p99:
          $ref: '#/components/schemas/CLS_p99'
        CLS_stddev:
          $ref: '#/components/schemas/CLS_stddev'
        CLS_sum:
          $ref: '#/components/schemas/CLS_sum'
        TBT_avg:
          $ref: '#/components/schemas/TBT_avg'
        TBT_max:
          $ref: '#/components/schemas/TBT_max'
        TBT_median:
          $ref: '#/components/schemas/TBT_median'
        TBT_min:
          $ref: '#/components/schemas/TBT_min'
        TBT_p50:
          $ref: '#/components/schemas/TBT_p50'
        TBT_p90:
          $ref: '#/components/schemas/TBT_p90'
        TBT_p95:
          $ref: '#/components/schemas/TBT_p95'
        TBT_p99:
          $ref: '#/components/schemas/TBT_p99'
        TBT_stddev:
          $ref: '#/components/schemas/TBT_stddev'
        TBT_sum:
          $ref: '#/components/schemas/TBT_sum'
        consoleErrors_avg:
          $ref: '#/components/schemas/consoleErrors_avg'
        consoleErrors_max:
          $ref: '#/components/schemas/consoleErrors_max'
        consoleErrors_median:
          $ref: '#/components/schemas/consoleErrors_median'
        consoleErrors_min:
          $ref: '#/components/schemas/consoleErrors_min'
        consoleErrors_p50:
          $ref: '#/components/schemas/consoleErrors_p50'
        consoleErrors_p90:
          $ref: '#/components/schemas/consoleErrors_p90'
        consoleErrors_p95:
          $ref: '#/components/schemas/consoleErrors_p95'
        consoleErrors_p99:
          $ref: '#/components/schemas/consoleErrors_p99'
        consoleErrors_stddev:
          $ref: '#/components/schemas/consoleErrors_stddev'
        consoleErrors_sum:
          $ref: '#/components/schemas/consoleErrors_sum'
        networkErrors_avg:
          $ref: '#/components/schemas/networkErrors_avg'
        networkErrors_max:
          $ref: '#/components/schemas/networkErrors_max'
        networkErrors_median:
          $ref: '#/components/schemas/networkErrors_median'
        networkErrors_min:
          $ref: '#/components/schemas/networkErrors_min'
        networkErrors_p50:
          $ref: '#/components/schemas/networkErrors_p50'
        networkErrors_p90:
          $ref: '#/components/schemas/networkErrors_p90'
        networkErrors_p95:
          $ref: '#/components/schemas/networkErrors_p95'
        networkErrors_p99:
          $ref: '#/components/schemas/networkErrors_p99'
        networkErrors_stddev:
          $ref: '#/components/schemas/networkErrors_stddev'
        networkErrors_sum:
          $ref: '#/components/schemas/networkErrors_sum'
        userScriptErrors_avg:
          $ref: '#/components/schemas/userScriptErrors_avg'
        userScriptErrors_max:
          $ref: '#/components/schemas/userScriptErrors_max'
        userScriptErrors_median:
          $ref: '#/components/schemas/userScriptErrors_median'
        userScriptErrors_min:
          $ref: '#/components/schemas/userScriptErrors_min'
        userScriptErrors_p50:
          $ref: '#/components/schemas/userScriptErrors_p50'
        userScriptErrors_p90:
          $ref: '#/components/schemas/userScriptErrors_p90'
        userScriptErrors_p95:
          $ref: '#/components/schemas/userScriptErrors_p95'
        userScriptErrors_p99:
          $ref: '#/components/schemas/userScriptErrors_p99'
        userScriptErrors_stddev:
          $ref: '#/components/schemas/userScriptErrors_stddev'
        userScriptErrors_sum:
          $ref: '#/components/schemas/userScriptErrors_sum'
        documentErrors_avg:
          $ref: '#/components/schemas/documentErrors_avg'
        documentErrors_max:
          $ref: '#/components/schemas/documentErrors_max'
        documentErrors_median:
          $ref: '#/components/schemas/documentErrors_median'
        documentErrors_min:
          $ref: '#/components/schemas/documentErrors_min'
        documentErrors_p50:
          $ref: '#/components/schemas/documentErrors_p50'
        documentErrors_p90:
          $ref: '#/components/schemas/documentErrors_p90'
        documentErrors_p95:
          $ref: '#/components/schemas/documentErrors_p95'
        documentErrors_p99:
          $ref: '#/components/schemas/documentErrors_p99'
        documentErrors_stddev:
          $ref: '#/components/schemas/documentErrors_stddev'
        documentErrors_sum:
          $ref: '#/components/schemas/documentErrors_sum'
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
    TTFB:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    FCP:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    LCP:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    CLS:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TBT:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    consoleErrors:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    networkErrors:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    userScriptErrors:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    documentErrors:
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
    TTFB_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TTFB_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TTFB_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TTFB_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TTFB_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TTFB_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TTFB_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TTFB_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TTFB_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TTFB_sum:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    FCP_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    FCP_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    FCP_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    FCP_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    FCP_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    FCP_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    FCP_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    FCP_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    FCP_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    FCP_sum:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    LCP_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    LCP_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    LCP_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    LCP_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    LCP_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    LCP_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    LCP_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    LCP_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    LCP_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    LCP_sum:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    CLS_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    CLS_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    CLS_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    CLS_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    CLS_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    CLS_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    CLS_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    CLS_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    CLS_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    CLS_sum:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TBT_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TBT_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TBT_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TBT_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TBT_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TBT_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TBT_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TBT_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TBT_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    TBT_sum:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    consoleErrors_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    consoleErrors_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    consoleErrors_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    consoleErrors_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    consoleErrors_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    consoleErrors_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    consoleErrors_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    consoleErrors_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    consoleErrors_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    consoleErrors_sum:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    networkErrors_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    networkErrors_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    networkErrors_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    networkErrors_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    networkErrors_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    networkErrors_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    networkErrors_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    networkErrors_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    networkErrors_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    networkErrors_sum:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    userScriptErrors_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    userScriptErrors_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    userScriptErrors_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    userScriptErrors_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    userScriptErrors_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    userScriptErrors_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    userScriptErrors_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    userScriptErrors_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    userScriptErrors_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    userScriptErrors_sum:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    documentErrors_avg:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    documentErrors_max:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    documentErrors_median:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    documentErrors_min:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    documentErrors_p50:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    documentErrors_p90:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    documentErrors_p95:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    documentErrors_p99:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    documentErrors_stddev:
      type: object
      properties:
        unit:
          $ref: '#/components/schemas/unit'
        label:
          type: string
        aggregation:
          $ref: '#/components/schemas/aggregation'
    documentErrors_sum:
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