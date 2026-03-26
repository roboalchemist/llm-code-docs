# Source: https://checklyhq.com/docs/api-reference/analytics/get-analytics-summary-for-multiple-checks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get analytics summary for multiple checks

> Returns availability, response times, and latency metrics for the given checks. Response shape is polymorphic per check type: fields are present only when the metric applies to that type. A null value means no data in the requested time range; an absent field means the metric does not apply to that check type.
Currently only `quickRange` is supported for time filtering. Arbitrary `from`/`to` date ranges are not yet supported but may be added in a future release.
**Rate-limiting is applied to this endpoint, you can send 30 requests / 60 seconds at most.**



## OpenAPI

````yaml post /v1/analytics/checks
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
  /v1/analytics/checks:
    post:
      tags:
        - Analytics
      summary: Get analytics summary for multiple checks
      description: >-
        Returns availability, response times, and latency metrics for the given
        checks. Response shape is polymorphic per check type: fields are present
        only when the metric applies to that type. A null value means no data in
        the requested time range; an absent field means the metric does not
        apply to that check type.

        Currently only `quickRange` is supported for time filtering. Arbitrary
        `from`/`to` date ranges are not yet supported but may be added in a
        future release.

        **Rate-limiting is applied to this endpoint, you can send 30 requests /
        60 seconds at most.**
      operationId: postV1AnalyticsChecks
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
        - name: quickRange
          in: query
          schema:
            type: string
            description: Time range for analytics.
            default: last24Hours
            enum:
              - last24Hours
              - last7Days
              - thisWeek
              - lastWeek
              - lastMonth
          description: Time range for analytics.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Model14'
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Model17'
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
    Model14:
      type: object
      properties:
        checkIds:
          $ref: '#/components/schemas/checkIds'
      required:
        - checkIds
    Model17:
      type: array
      items:
        $ref: '#/components/schemas/Model16'
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
    checkIds:
      type: array
      description: Array of check IDs to fetch analytics for.
      minItems: 1
      maxItems: 100
      items:
        type: string
        x-format:
          guid:
            version: uuidv4
    Model16:
      type: object
      properties:
        checkId:
          type: string
          x-format:
            guid:
              version: uuidv4
        checkType:
          $ref: '#/components/schemas/Model15'
        availability:
          type: number
          nullable: true
        responseTime_avg:
          type: number
          nullable: true
        responseTime_p50:
          type: number
          nullable: true
        responseTime_p95:
          type: number
          nullable: true
        responseTime_p99:
          type: number
          nullable: true
        latency_avg:
          type: number
          nullable: true
        latency_p50:
          type: number
          nullable: true
        latency_p95:
          type: number
          nullable: true
        latency_p99:
          type: number
          nullable: true
        packetLoss_avg:
          type: number
          nullable: true
        packetLoss_p95:
          type: number
          nullable: true
        packetLoss_p99:
          type: number
          nullable: true
      required:
        - checkId
        - checkType
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
    Model15:
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