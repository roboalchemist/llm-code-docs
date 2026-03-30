# Source: https://checklyhq.com/docs/api-reference/private-locations/get-private-location-health-metrics-from-a-window-of-time.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get private location health metrics from a window of time.

> Get private location health metrics from a window of time.
**Rate-limiting is applied to this endpoint, you can send 300 requests per day at most.**



## OpenAPI

````yaml get /v1/private-locations/{id}/metrics
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
  /v1/private-locations/{id}/metrics:
    get:
      tags:
        - Private locations
      summary: Get private location health metrics from a window of time.
      description: >-
        Get private location health metrics from a window of time.

        **Rate-limiting is applied to this endpoint, you can send 300 requests
        per day at most.**
      operationId: getV1PrivatelocationsIdMetrics
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
              Select metrics beginning with this UNIX timestamp. Must be less
              than 15 days ago.
          description: >-
            Select metrics beginning with this UNIX timestamp. Must be less than
            15 days ago.
          required: true
        - name: to
          in: query
          schema:
            type: string
            format: date
            description: Select metrics up to this UNIX timestamp.
          description: Select metrics up to this UNIX timestamp.
          required: true
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/privateLocationsMetricsHistoryResponseSchema
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
    privateLocationsMetricsHistoryResponseSchema:
      type: object
      properties:
        timestamps:
          $ref: '#/components/schemas/timestamps'
        queueSize:
          $ref: '#/components/schemas/queueSize'
        oldestScheduledCheckRun:
          $ref: '#/components/schemas/oldestScheduledCheckRun'
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
    timestamps:
      type: array
      items:
        type: string
        format: date-time
    queueSize:
      type: array
      items:
        type: number
    oldestScheduledCheckRun:
      type: array
      items:
        type: number
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