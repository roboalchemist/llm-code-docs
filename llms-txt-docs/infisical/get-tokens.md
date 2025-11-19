# Source: https://infisical.com/docs/api-reference/endpoints/token-auth/get-tokens.md

# Get Tokens

> Get tokens for machine identity with Token Auth

## OpenAPI

````yaml GET /api/v1/auth/token-auth/identities/{identityId}/tokens
paths:
  path: /api/v1/auth/token-auth/identities/{identityId}/tokens
  method: get
  servers:
    - url: https://us.infisical.com
      description: Production server (US)
    - url: https://eu.infisical.com
      description: Production server (EU)
    - url: http://localhost:8080
      description: Local server
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: An access token in Infisical
          cookie: {}
    parameters:
      path:
        identityId:
          schema:
            - type: string
              required: true
              description: The ID of the machine identity to list token metadata for.
      query:
        offset:
          schema:
            - type: number
              required: false
              description: >-
                The offset to start from. If you enter 10, it will start from
                the 10th token.
              maximum: 100
              minimum: 0
              default: 0
        limit:
          schema:
            - type: number
              required: false
              description: The number of tokens to return.
              maximum: 100
              minimum: 1
              default: 20
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              tokens:
                allOf:
                  - type: array
                    items:
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
                      required:
                        - id
                        - identityId
                        - createdAt
                        - updatedAt
                        - authMethod
                      additionalProperties: false
            requiredProperties:
              - tokens
            additionalProperties: false
        examples:
          example:
            value:
              tokens:
                - id: <string>
                  accessTokenTTL: 2592000
                  accessTokenMaxTTL: 2592000
                  accessTokenNumUses: 0
                  accessTokenNumUsesLimit: 0
                  accessTokenLastUsedAt: '2023-11-07T05:31:56Z'
                  accessTokenLastRenewedAt: '2023-11-07T05:31:56Z'
                  isAccessTokenRevoked: false
                  identityUAClientSecretId: <string>
                  identityId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
                  name: <string>
                  authMethod: <string>
                  accessTokenPeriod: 0
        description: Default Response
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 400
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 400
              message: <string>
              error: <string>
        description: Default Response
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 401
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 401
              message: <string>
              error: <string>
        description: Default Response
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 403
              message:
                allOf:
                  - type: string
              details:
                allOf:
                  - {}
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 403
              message: <string>
              details: <any>
              error: <string>
        description: Default Response
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 404
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 404
              message: <string>
              error: <string>
        description: Default Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 422
              message:
                allOf:
                  - {}
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 422
              message: <any>
              error: <string>
        description: Default Response
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              reqId:
                allOf:
                  - type: string
              statusCode:
                allOf:
                  - type: number
                    enum:
                      - 500
              message:
                allOf:
                  - type: string
              error:
                allOf:
                  - type: string
            requiredProperties:
              - reqId
              - statusCode
              - message
              - error
            additionalProperties: false
        examples:
          example:
            value:
              reqId: <string>
              statusCode: 500
              message: <string>
              error: <string>
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````