# Source: https://checklyhq.com/docs/api-reference/check-status/list-all-check-statuses.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all check statuses

> Shows the current status information for all checks in your account. The check status records are continuously updated as new check results come in.



## OpenAPI

````yaml get /v1/check-statuses
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
  /v1/check-statuses:
    get:
      tags:
        - Check status
      summary: List all check statuses
      description: >-
        Shows the current status information for all checks in your account. The
        check status records are continuously updated as new check results come
        in.
      operationId: getV1Checkstatuses
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
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CheckStatusList'
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
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotFoundError'
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TooManyRequestsError'
components:
  schemas:
    CheckStatusList:
      type: array
      items:
        $ref: '#/components/schemas/CheckStatus'
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
    NotFoundError:
      type: object
      properties:
        statusCode:
          type: number
          enum:
            - 404
        error:
          $ref: '#/components/schemas/Model3'
        message:
          type: string
          example: Not Found
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
    CheckStatus:
      type: object
      nullable: true
      properties:
        name:
          type: string
          description: The name of the check.
          example: API Check
        checkId:
          type: string
          description: The ID of check this status belongs to.
          example: 1008ca04-d3ca-41fa-b477-9e99b761dbb4
        hasFailures:
          type: boolean
          description: >-
            Describes if this check is currently failing. If any of the
            assertions for an API checkfail this value is true. If a browser
            check fails for whatever reason, this is true.
          example: false
        hasErrors:
          type: boolean
          description: >-
            Describes if due to some error outside of normal operation this
            check is failing. This should be extremely rare and only when there
            is an error in the Checkly backend.
          example: false
        isDegraded:
          type: boolean
          description: >-
            A check is degraded if it is over the degradation limit set by the
            "degradedResponseTime" field on the check. Applies only to API
            checks.
          example: true
        longestRun:
          type: number
          description: The longest ever recorded response time for this check.
          example: 10
          nullable: true
        shortestRun:
          type: number
          description: The shortest ever recorded response time for this check.
          example: 5
          nullable: true
        lastRunLocation:
          type: string
          description: What location this check was last run at.
          example: us-east-1
          nullable: true
        lastCheckRunId:
          type: string
          description: The unique incrementing ID for each check run.
          example: f10d711f-cd16-4303-91ce-741c92586b4a
          nullable: true
        sslDaysRemaining:
          type: number
          description: How many days remain till the current SSL certificate expires.
          example: 3
          nullable: true
        created_at:
          type: string
          format: date
        updated_at:
          type: string
          format: date-time
          nullable: true
      required:
        - name
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
    Model3:
      type: string
      enum:
        - Not Found
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