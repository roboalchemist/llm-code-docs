# Source: https://docs.edenai.co/api-reference/user-management/update-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Token



## OpenAPI

````yaml openapi/v3-user.json patch /user/custom_token/{name}/
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
    patch:
      tags:
        - User Management
      summary: Update Token
      operationId: user_root_partial_update
      parameters:
        - in: path
          name: name
          schema:
            type: string
          required: true
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchedCustomTokenUpdateRequest'
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CustomTokenUpdate'
          description: ''
      security:
        - FeatureApiAuth: []
components:
  schemas:
    PatchedCustomTokenUpdateRequest:
      type: object
      properties:
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
        expire_time:
          type: string
          format: date-time
          nullable: true
        active_balance:
          type: boolean
          description: Weither to use the balance field or not.
    CustomTokenUpdate:
      type: object
      properties:
        name:
          type: string
          readOnly: true
          description: The token name
        token_type:
          allOf:
            - $ref: '#/components/schemas/TokenTypeEnum'
          readOnly: true
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
        expire_time:
          type: string
          format: date-time
          nullable: true
        active_balance:
          type: boolean
          description: Weither to use the balance field or not.
      required:
        - name
        - token_type
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