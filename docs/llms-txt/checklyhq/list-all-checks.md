# Source: https://checklyhq.com/docs/api-reference/checks/list-all-checks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all checks

> Lists all current checks in your account.



## OpenAPI

````yaml get /v1/checks
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
  /v1/checks:
    get:
      tags:
        - Checks
      summary: List all checks
      description: Lists all current checks in your account.
      operationId: getV1Checks
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
        - name: apiCheckUrlFilterPattern
          in: query
          schema:
            type: string
            description: >-
              Filters the results by a string contained in the URL of an API
              check, for instance a domain like "www.myapp.com". Only returns
              API checks.
            minLength: 1
          description: >-
            Filters the results by a string contained in the URL of an API
            check, for instance a domain like "www.myapp.com". Only returns API
            checks.
        - name: tag
          in: query
          schema:
            type: array
            description: >-
              Filters checks by tags. Returns checks that have at least one of
              the specified tags.
            x-constraint:
              single: true
            items:
              type: string
          description: >-
            Filters checks by tags. Returns checks that have at least one of the
            specified tags.
          style: form
          explode: true
        - name: checkType
          in: query
          schema:
            type: string
            description: >-
              Filters checks by type. Returns checks that match the specified
              type.
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
          description: >-
            Filters checks by type. Returns checks that match the specified
            type.
        - name: search
          in: query
          schema:
            type: string
            description: Filters checks by name using a case-insensitive partial match.
          description: Filters checks by name using a case-insensitive partial match.
        - name: status
          in: query
          schema:
            type: string
            description: Filters checks by current status.
            enum:
              - passing
              - failing
              - degraded
          description: Filters checks by current status.
        - name: applyGroupSettings
          in: query
          schema:
            type: boolean
            description: >-
              Checks that belong to a group are returned with group settings
              applied.
            default: false
          description: >-
            Checks that belong to a group are returned with group settings
            applied.
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CheckList'
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
    CheckList:
      type: array
      items:
        $ref: '#/components/schemas/Check'
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
    Check:
      type: object
      properties:
        id:
          type: string
        checkType:
          $ref: '#/components/schemas/checkType'
      required:
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
    checkType:
      type: string
      description: The type of the check.
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