# Source: https://infisical.com/docs/api-reference/endpoints/universal-auth/get-client-secret-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Client Secret By ID

> Get Universal Auth Client Secret for machine identity



## OpenAPI

````yaml GET /api/v1/auth/universal-auth/identities/{identityId}/client-secrets/{clientSecretId}
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
  /api/v1/auth/universal-auth/identities/{identityId}/client-secrets/{clientSecretId}:
    get:
      tags:
        - Universal Auth
      description: Get Universal Auth Client Secret for machine identity
      operationId: getUniversalAuthClientSecret
      parameters:
        - schema:
            type: string
          in: path
          name: identityId
          required: true
          description: The ID of the machine identity to get the client secret from.
        - schema:
            type: string
          in: path
          name: clientSecretId
          required: true
          description: The ID of the client secret to get details.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  clientSecretData:
                    type: object
                    properties:
                      id:
                        type: string
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                      description:
                        type: string
                      clientSecretPrefix:
                        type: string
                      clientSecretNumUses:
                        type: number
                        default: 0
                      clientSecretNumUsesLimit:
                        type: number
                        default: 0
                      clientSecretTTL:
                        type: number
                        default: 0
                      identityUAId:
                        type: string
                        format: uuid
                      isClientSecretRevoked:
                        type: boolean
                        default: false
                    required:
                      - id
                      - createdAt
                      - updatedAt
                      - description
                      - clientSecretPrefix
                      - identityUAId
                    additionalProperties: false
                required:
                  - clientSecretData
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