# Source: https://docs.edenai.co/api-reference/user-management/retrieve-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve Token



## OpenAPI

````yaml openapi/v3-user.json get /user/custom_token/{name}/
openapi: 3.0.3
info:
  title: User Management
  version: '2.0'
  description: Your project description
servers:
  - url: https://api.edenai.run/v2
security: []
paths:
  /user/custom_token/{name}/:
    get:
      tags:
        - User Management
      summary: Retrieve Token
      operationId: user_root_retrieve
      parameters:
        - in: path
          name: name
          schema:
            type: string
          required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CustomTokensList'
          description: ''
      security:
        - FeatureApiAuth: []
components:
  schemas:
    CustomTokensList:
      type: object
      properties:
        name:
          type: string
          description: The token name
          maxLength: 200
        token:
          type: string
          nullable: true
          maxLength: 2000
        token_type:
          $ref: '#/components/schemas/TokenTypeEnum'
        balance:
          type: number
          format: double
          maximum: 100000
          minimum: -100000
          exclusiveMaximum: true
          exclusiveMinimum: true
          description: >-
            Optional remaining credits balance for this Token, if
            `active_balance` is set to True and the balance reaches 0, this
            token will become unusable
        active_balance:
          type: boolean
          description: Weither to use the balance field or not.
        expire_time:
          type: string
          format: date-time
          nullable: true
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