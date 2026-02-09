# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/windows-local-account/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/unix-linux-local-account/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/redis-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/postgres-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/oracledb-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/okta-client-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mysql-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mssql-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mongodb-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/ldap-password/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/databricks-service-principal-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/azure-client-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/aws-iam-user-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/auth0-client-secret/rotate-secrets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Rotate Secrets

> Rotate the generated credentials for the specified Auth0 Client Secret Rotation.



## OpenAPI

````yaml POST /api/v2/secret-rotations/auth0-client-secret/{rotationId}/rotate-secrets
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
  /api/v2/secret-rotations/auth0-client-secret/{rotationId}/rotate-secrets:
    post:
      tags:
        - Secret Rotations
      description: >-
        Rotate the generated credentials for the specified Auth0 Client Secret
        Rotation.
      operationId: rotateAuth0ClientSecretRotation
      parameters:
        - schema:
            type: string
            format: uuid
          in: path
          name: rotationId
          required: true
          description: >-
            The ID of the Auth0 Client Secret Rotation to rotate generated
            credentials for.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  secretRotation:
                    type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      name:
                        type: string
                      description:
                        type: string
                        nullable: true
                      isAutoRotationEnabled:
                        type: boolean
                        default: true
                      activeIndex:
                        type: number
                        default: 0
                      folderId:
                        type: string
                        format: uuid
                      connectionId:
                        type: string
                        format: uuid
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                      rotationInterval:
                        type: number
                      rotationStatus:
                        type: string
                      lastRotationAttemptedAt:
                        type: string
                        format: date-time
                      lastRotatedAt:
                        type: string
                        format: date-time
                      lastRotationJobId:
                        type: string
                        nullable: true
                      nextRotationAt:
                        type: string
                        format: date-time
                        nullable: true
                      isLastRotationManual:
                        type: boolean
                        default: true
                      connection:
                        type: object
                        properties:
                          app:
                            type: string
                            enum:
                              - auth0
                          name:
                            type: string
                          id:
                            type: string
                            format: uuid
                        required:
                          - app
                          - name
                          - id
                        additionalProperties: false
                      environment:
                        type: object
                        properties:
                          slug:
                            type: string
                          name:
                            type: string
                          id:
                            type: string
                            format: uuid
                        required:
                          - slug
                          - name
                          - id
                        additionalProperties: false
                      projectId:
                        type: string
                      folder:
                        type: object
                        properties:
                          id:
                            type: string
                          path:
                            type: string
                        required:
                          - id
                          - path
                        additionalProperties: false
                      rotateAtUtc:
                        type: object
                        properties:
                          hours:
                            type: number
                            minimum: 0
                            maximum: 23
                          minutes:
                            type: number
                            minimum: 0
                            maximum: 59
                        required:
                          - hours
                          - minutes
                        additionalProperties: false
                      lastRotationMessage:
                        type: string
                        nullable: true
                      type:
                        type: string
                        enum:
                          - auth0-client-secret
                      parameters:
                        type: object
                        properties:
                          clientId:
                            type: string
                            minLength: 1
                            description: >-
                              The client ID of the Auth0 Application to rotate
                              the client secret for.
                        required:
                          - clientId
                        additionalProperties: false
                      secretsMapping:
                        type: object
                        properties:
                          clientId:
                            type: string
                            minLength: 1
                            description: >-
                              The name of the secret that the client ID will be
                              mapped to.
                          clientSecret:
                            type: string
                            minLength: 1
                            description: >-
                              The name of the secret that the rotated client
                              secret will be mapped to.
                        required:
                          - clientId
                          - clientSecret
                        additionalProperties: false
                    required:
                      - id
                      - name
                      - folderId
                      - connectionId
                      - createdAt
                      - updatedAt
                      - rotationInterval
                      - rotationStatus
                      - lastRotationAttemptedAt
                      - lastRotatedAt
                      - connection
                      - environment
                      - projectId
                      - folder
                      - rotateAtUtc
                      - type
                      - parameters
                      - secretsMapping
                    additionalProperties: false
                required:
                  - secretRotation
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