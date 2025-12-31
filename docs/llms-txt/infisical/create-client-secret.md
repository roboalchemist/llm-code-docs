# Source: https://infisical.com/docs/api-reference/endpoints/universal-auth/create-client-secret.md

# Create Client Secret

> Create Universal Auth Client Secret for machine identity

## OpenAPI

````yaml POST /api/v1/auth/universal-auth/identities/{identityId}/client-secrets
paths:
  path: /api/v1/auth/universal-auth/identities/{identityId}/client-secrets
  method: post
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
              description: The ID of the machine identity to create a client secret for.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              description:
                allOf:
                  - type: string
                    default: ''
                    description: The description of the client secret.
              numUsesLimit:
                allOf:
                  - type: number
                    minimum: 0
                    default: 0
                    description: >-
                      The maximum number of times that the client secret can be
                      used; a value of 0 implies infinite number of uses.
              ttl:
                allOf:
                  - type: number
                    minimum: 0
                    maximum: 315360000
                    default: 0
                    description: The lifetime for the client secret in seconds.
            additionalProperties: false
        examples:
          example:
            value:
              description: ''
              numUsesLimit: 0
              ttl: 0
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              clientSecret:
                allOf:
                  - type: string
              clientSecretData:
                allOf:
                  - type: object
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
            requiredProperties:
              - clientSecret
              - clientSecretData
            additionalProperties: false
        examples:
          example:
            value:
              clientSecret: <string>
              clientSecretData:
                id: <string>
                createdAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
                description: <string>
                clientSecretPrefix: <string>
                clientSecretNumUses: 0
                clientSecretNumUsesLimit: 0
                clientSecretTTL: 0
                identityUAId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                isClientSecretRevoked: false
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