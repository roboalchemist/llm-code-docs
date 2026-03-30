# Source: https://checklyhq.com/docs/api-reference/reporting/generates-a-report-with-aggregate-statistics-for-checks-and-check-groups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Generates a report with aggregate statistics for checks and check groups.

> Generates a report with aggregated statistics for all checks or a filtered set of checks over a specified time window.



## OpenAPI

````yaml get /v1/reporting
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
  /v1/reporting:
    get:
      tags:
        - Reporting
      summary: >-
        Generates a report with aggregate statistics for checks and check
        groups.
      description: >-
        Generates a report with aggregated statistics for all checks or a
        filtered set of checks over a specified time window.
      operationId: getV1Reporting
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
            default: last24Hrs
            enum:
              - last24Hrs
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
        - name: filterByTags
          in: query
          schema:
            type: array
            description: Use tags to filter the checks you want to see in your report.
            example:
              - production
            x-constraint:
              single: true
            items:
              type: string
          description: Use tags to filter the checks you want to see in your report.
          style: form
          explode: true
        - name: deactivated
          in: query
          schema:
            type: boolean
            description: >-
              Filter checks by activated status. When set to true, only
              deactivated checks are returned. When set to false, only activated
              checks are returned. When omitted, all checks are returned.
            default: null
            nullable: true
          description: >-
            Filter checks by activated status. When set to true, only
            deactivated checks are returned. When set to false, only activated
            checks are returned. When omitted, all checks are returned.
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ReportingList'
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
    ReportingList:
      type: array
      items:
        $ref: '#/components/schemas/Reporting'
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
    Reporting:
      type: object
      properties:
        name:
          type: string
          description: Check name.
          example: API Check
        checkId:
          type: string
          description: Check ID.
          example: d2881e09-411b-4c8d-84b8-fe05fbca80b6
        checkType:
          type: string
          description: Check type.
          example: API
        deactivated:
          type: boolean
          description: Check deactivated.
          default: false
        tags:
          $ref: '#/components/schemas/ReportingTagList'
        aggregate:
          $ref: '#/components/schemas/ReportingAggregate'
      required:
        - name
        - checkId
        - checkType
        - deactivated
        - tags
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
    ReportingTagList:
      type: array
      description: Check tags.
      example:
        - production
      items:
        type: string
    ReportingAggregate:
      type: object
      properties:
        successRatio:
          type: number
          description: >-
            Success ratio of the check over selected date range. Percentage is
            in decimal form.
          example: 50
          minimum: 0
        avg:
          type: number
          description: >-
            Average response time of the check over selected date range in
            milliseconds.
          example: 100
          minimum: 0
        p95:
          type: number
          description: >-
            P95 response time of the check over selected date range in
            milliseconds.
          example: 200
          minimum: 0
        p99:
          type: number
          description: >-
            P99 response time of the check over selected date range in
            milliseconds.
          example: 100
          minimum: 0
      required:
        - successRatio
        - avg
        - p95
        - p99
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