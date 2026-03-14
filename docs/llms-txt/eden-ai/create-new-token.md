# Source: https://docs.edenai.co/api-reference/user-management/create-new-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Create new Token



## OpenAPI

````yaml openapi/v3-user.json post /user/custom_token/
openapi: 3.0.3
info:
  title: User Management
  version: '2.0'
  description: Your project description
servers:
  - url: https://api.edenai.run/v2
security: []
paths:
  /user/custom_token/:
    post:
      tags:
        - User Management
      summary: Create new Token
      operationId: user_root_create
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CustomTokensCreateRequest'
        required: true
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CustomTokensCreate'
          description: ''
      security:
        - FeatureApiAuth: []
components:
  schemas:
    CustomTokensCreateRequest:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          description: The token name
          maxLength: 200
        token_type:
          $ref: '#/components/schemas/TokenTypeEnum'
        balance:
          type: string
          format: decimal
          pattern: ^-?\d{0,5}(?:\.\d{0,9})?$
          description: >-
            Optional remaining credits balance for this Token, if
            `active_balance` is set to True and the balance reaches 0, this
            token will become unusable
        expire_time:
          type: string
          format: date-time
          nullable: true
        active_balance:
          type: boolean
          description: Weither to use the balance field or not.
      required:
        - name
    CustomTokensCreate:
      type: object
      properties:
        name:
          type: string
          description: The token name
          maxLength: 200
        token_type:
          $ref: '#/components/schemas/TokenTypeEnum'
        balance:
          type: string
          format: decimal
          pattern: ^-?\d{0,5}(?:\.\d{0,9})?$
          description: >-
            Optional remaining credits balance for this Token, if
            `active_balance` is set to True and the balance reaches 0, this
            token will become unusable
        expire_time:
          type: string
          format: date-time
          nullable: true
        active_balance:
          type: boolean
          description: Weither to use the balance field or not.
      required:
        - name
    TokenTypeEnum:
      enum:
        - sandbox_api_token
        - api_token
      type: string
      description: |-
        * `sandbox_api_token` - Sandbox
        * `api_token` - Back
  securitySchemes:
    FeatureApiAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````

Built with [Mintlify](https://mintlify.com).