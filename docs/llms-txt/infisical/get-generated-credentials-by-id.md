# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/windows-local-account/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/unix-linux-local-account/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/redis-credentials/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/postgres-credentials/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/oracledb-credentials/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/okta-client-secret/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mysql-credentials/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mssql-credentials/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mongodb-credentials/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/ldap-password/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/databricks-service-principal-secret/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/azure-client-secret/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/aws-iam-user-secret/get-generated-credentials-by-id.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/auth0-client-secret/get-generated-credentials-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Credentials by ID

> Get the generated credentials for the specified Auth0 Client Secret Rotation.



## OpenAPI

````yaml GET /api/v2/secret-rotations/auth0-client-secret/{rotationId}/generated-credentials
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
  /api/v2/secret-rotations/auth0-client-secret/{rotationId}/generated-credentials:
    get:
      tags:
        - Secret Rotations
      description: >-
        Get the generated credentials for the specified Auth0 Client Secret
        Rotation.
      operationId: getAuth0ClientSecretRotationGeneratedCredentials
      parameters:
        - schema:
            type: string
            format: uuid
          in: path
          name: rotationId
          required: true
          description: >-
            The ID of the Auth0 Client Secret Rotation to retrieve the generated
            credentials for.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  generatedCredentials:
                    type: array
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
                    type: number
                  rotationId:
                    type: string
                    format: uuid
                  type:
                    type: string
                    enum:
                      - auth0-client-secret
                required:
                  - generatedCredentials
                  - activeIndex
                  - rotationId
                  - type
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

````