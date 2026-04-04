# Source: https://checklyhq.com/docs/api-reference/accounts/fetch-user-accounts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get details for all accounts

> List account details based on supplied API key.



## OpenAPI

````yaml get /v1/accounts
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
  /v1/accounts:
    get:
      tags:
        - Accounts
      summary: Fetch user accounts
      description: List account details based on supplied API key.
      operationId: getV1Accounts
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
                $ref: '#/components/schemas/AccountList'
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
    AccountList:
      type: array
      items:
        $ref: '#/components/schemas/Account'
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
    Account:
      type: object
      properties:
        id:
          type: string
          description: Checkly account ID.
          example: d43967ee-81db-4e0b-a18c-06be5c995288
          x-format:
            guid: true
        name:
          type: string
          description: The name of the account.
          example: Checkly
        runtimeId:
          type: string
          description: The account default runtime ID.
          example: '2022.10'
        plan:
          type: string
          description: The account plan type.
          example: team
        planDisplayName:
          type: string
          description: The human-readable display name of the account plan.
          example: Team
        addons:
          $ref: '#/components/schemas/addons'
        settings:
          $ref: '#/components/schemas/settings'
        alertSettings:
          $ref: '#/components/schemas/alertSettings'
      required:
        - id
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
    addons:
      type: object
      description: The add-ons available to the account.
      properties:
        communicate:
          $ref: '#/components/schemas/AddonTier'
        resolve:
          $ref: '#/components/schemas/AddonTier'
    settings:
      type: object
      description: The settings of the account.
    alertSettings:
      type: object
      description: The alert settings of the account.
    AddonTier:
      type: object
      properties:
        tier:
          $ref: '#/components/schemas/tier'
        tierDisplayName:
          type: string
          description: The human-readable display name of the add-on tier.
          example: Communicate Starter
    tier:
      type: string
      description: The add-on tier.
      example: starter
      enum:
        - hobby
        - starter
        - team
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