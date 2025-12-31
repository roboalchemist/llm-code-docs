# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/redis-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/postgres-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/oracledb-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/okta-client-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mysql-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mssql-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mongodb-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/ldap-password/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/azure-client-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/aws-iam-user-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/auth0-client-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/redis-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/postgres-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/oracledb-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/okta-client-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mysql-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mssql-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mongodb-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/ldap-password/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/azure-client-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/aws-iam-user-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/auth0-client-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/redis-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/postgres-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/oracledb-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/okta-client-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mysql-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mssql-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/ldap-password/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/azure-client-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/aws-iam-user-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/auth0-client-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/redis-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/postgres-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/oracledb-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/okta-client-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mysql-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/mssql-credentials/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/ldap-password/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/azure-client-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/aws-iam-user-secret/rotate-secrets.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-rotations/auth0-client-secret/rotate-secrets.md

# Rotate Secrets

> Rotate the generated credentials for the specified Auth0 Client Secret Rotation.

## OpenAPI

````yaml POST /api/v2/secret-rotations/auth0-client-secret/{rotationId}/rotate-secrets
paths:
  path: /api/v2/secret-rotations/auth0-client-secret/{rotationId}/rotate-secrets
  method: post
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
                The ID of the Auth0 Client Secret Rotation to rotate generated
                credentials for.
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
              secretRotation:
                allOf:
                  - type: object
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
            requiredProperties:
              - secretRotation
            additionalProperties: false
        examples:
          example:
            value:
              secretRotation:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                name: <string>
                description: <string>
                isAutoRotationEnabled: true
                activeIndex: 0
                folderId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                connectionId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                createdAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
                rotationInterval: 123
                rotationStatus: <string>
                lastRotationAttemptedAt: '2023-11-07T05:31:56Z'
                lastRotatedAt: '2023-11-07T05:31:56Z'
                lastRotationJobId: <string>
                nextRotationAt: '2023-11-07T05:31:56Z'
                isLastRotationManual: true
                connection:
                  app: auth0
                  name: <string>
                  id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                environment:
                  slug: <string>
                  name: <string>
                  id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                projectId: <string>
                folder:
                  id: <string>
                  path: <string>
                rotateAtUtc:
                  hours: 11.5
                  minutes: 29.5
                lastRotationMessage: <string>
                type: auth0-client-secret
                parameters:
                  clientId: <string>
                secretsMapping:
                  clientId: <string>
                  clientSecret: <string>
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