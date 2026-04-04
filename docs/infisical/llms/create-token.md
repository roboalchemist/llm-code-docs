# Source: https://infisical.com/docs/api-reference/endpoints/token-auth/create-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Token

> Create token for machine identity with Token Auth



## OpenAPI

````yaml POST /api/v1/auth/token-auth/identities/{identityId}/tokens
openapi: 3.0.3
info:
  title: Infisical API
  description: List of all available APIs that can be consumed
  version: 0.0.1
servers:
  - url: https://us.infisical.com
    description: Production server (US)
  - url: https://eu.infisical.com
    description: Production server (EU)
  - url: http://localhost:8080
    description: Local server
security: []
paths:
  /api/v1/auth/token-auth/identities/{identityId}/tokens:
    post:
      tags:
        - Token Auth
      description: Create token for machine identity with Token Auth
      operationId: createTokenAuthToken
      parameters:
        - schema:
            type: string
          in: path
          name: identityId
          required: true
          description: The ID of the machine identity to create the token for.
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: The name of the token to create.
                organizationSlug:
                  type: string
                  minLength: 1
                  maxLength: 64
                  description: The sub organization name to scope the token to.
              additionalProperties: false
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  accessToken:
                    type: string
                  expiresIn:
                    type: number
                  accessTokenMaxTTL:
                    type: number
                  tokenType:
                    type: string
                    enum:
                      - Bearer
                  tokenData:
                    type: object
                    properties:
                      id:
                        type: string
                      accessTokenTTL:
                        type: number
                        default: 2592000
                      accessTokenMaxTTL:
                        type: number
                        default: 2592000
                      accessTokenNumUses:
                        type: number
                        default: 0
                      accessTokenNumUsesLimit:
                        type: number
                        default: 0
                      accessTokenLastUsedAt:
                        type: string
                        format: date-time
                        nullable: true
                      accessTokenLastRenewedAt:
                        type: string
                        format: date-time
                        nullable: true
                      isAccessTokenRevoked:
                        type: boolean
                        default: false
                      identityUAClientSecretId:
                        type: string
                        nullable: true
                      identityId:
                        type: string
                        format: uuid
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                      name:
                        type: string
                        nullable: true
                      authMethod:
                        type: string
                      accessTokenPeriod:
                        type: number
                        default: 0
                      subOrganizationId:
                        type: string
                        format: uuid
                        nullable: true
                    required:
                      - id
                      - identityId
                      - createdAt
                      - updatedAt
                      - authMethod
                    additionalProperties: false
                required:
                  - accessToken
                  - expiresIn
                  - accessTokenMaxTTL
                  - tokenType
                  - tokenData
                additionalProperties: false
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 400
                  message:
                    type: string
                  error:
                    type: string
                  details: {}
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '401':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 401
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '403':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 403
                  message:
                    type: string
                  details: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '404':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 404
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '422':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 422
                  message: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - error
                additionalProperties: false
        '500':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 500
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: An access token in Infisical

````