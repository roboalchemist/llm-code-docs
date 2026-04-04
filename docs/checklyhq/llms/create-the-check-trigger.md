# Source: https://checklyhq.com/docs/api-reference/triggers/create-the-check-trigger.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create the check trigger

> **[DEPRECATED]** This endpoint will be removed soon. Please use the [Checkly CLI](https://www.checklyhq.com/docs/cli) to test and trigger checks. Creates the check trigger



## OpenAPI

````yaml post /v1/triggers/checks/{checkId}
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
  /v1/triggers/checks/{checkId}:
    post:
      tags:
        - Triggers
      summary: Create the check trigger
      description: >-
        **[DEPRECATED]** This endpoint will be removed soon. Please use the
        [Checkly CLI](https://www.checklyhq.com/docs/cli) to test and trigger
        checks. Creates the check trigger
      operationId: postV1TriggersChecksCheckid
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
        - name: checkId
          in: path
          schema:
            type: string
            x-format:
              guid: true
          required: true
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CheckTrigger'
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
      deprecated: true
components:
  schemas:
    CheckTrigger:
      type: object
      properties:
        id:
          type: number
          example: 1
        token:
          type: string
          example: h7QMmh8c0hYw
        created_at:
          type: string
          format: date
        called_at:
          type: string
          format: date
          nullable: true
        updated_at:
          type: string
          format: date
          nullable: true
        checkId:
          type: string
          example: a13a7875-ec45-4780-b39f-675ec288cfe1
      required:
        - id
        - token
        - created_at
        - checkId
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