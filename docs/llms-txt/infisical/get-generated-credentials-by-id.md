# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/redis-credentials/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/postgres-credentials/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/oracledb-credentials/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/okta-client-secret/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mysql-credentials/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mssql-credentials/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/ldap-password/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/azure-client-secret/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/aws-iam-user-secret/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/auth0-client-secret/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/redis-credentials/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/postgres-credentials/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/oracledb-credentials/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/okta-client-secret/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mysql-credentials/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mssql-credentials/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/ldap-password/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/azure-client-secret/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/aws-iam-user-secret/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/auth0-client-secret/get-generated-credentials-by-id.md

# Get Credentials by ID

> Get the generated credentials for the specified Auth0 Client Secret Rotation.

## OpenAPI

````yaml GET /api/v2/secret-rotations/auth0-client-secret/{rotationId}/generated-credentials
paths:
  path: >-
    /api/v2/secret-rotations/auth0-client-secret/{rotationId}/generated-credentials
  method: get
  servers:
    - url: https://us.infisical.com
      description: Production server (US)
    - url: https://eu.infisical.com
      description: Production server (EU)
    - url: http://localhost:8080
      description: Local server
  request:
    security: []
    parameters:
      path:
        rotationId:
          schema:
            - type: string
              required: true
              description: >-
                The ID of the Auth0 Client Secret Rotation to retrieve the
                generated credentials for.
              format: uuid
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              generatedCredentials:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        clientId:
                          type: string
                        clientSecret:
                          type: string
                      required:
                        - clientId
                        - clientSecret
                      additionalProperties: false
                    minItems: 1
                    maxItems: 2
              activeIndex:
                allOf:
                  - type: number
              rotationId:
                allOf:
                  - type: string
                    format: uuid
              type:
                allOf:
                  - type: string
                    enum:
                      - auth0-client-secret
            requiredProperties:
              - generatedCredentials
              - activeIndex
              - rotationId
              - type
            additionalProperties: false
        examples:
          example:
            value:
              generatedCredentials:
                - clientId: <string>
                  clientSecret: <string>
              activeIndex: 123
              rotationId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              type: auth0-client-secret
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