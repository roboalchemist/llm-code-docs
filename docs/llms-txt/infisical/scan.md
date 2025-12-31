# Source: https://infisical.com/docs/cli/commands/scan.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/gitlab/scan.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/github/scan.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/bitbucket/scan.md

# Source: https://infisical.com/docs/cli/commands/scan.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/gitlab/scan.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/github/scan.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/bitbucket/scan.md

# Source: https://infisical.com/docs/cli/commands/scan.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/gitlab/scan.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/github/scan.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/bitbucket/scan.md

# Source: https://infisical.com/docs/cli/commands/scan.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/gitlab/scan.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/github/scan.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/bitbucket/scan.md

# Scan

> Trigger a scan for the specified Bitbucket Data Source.

## OpenAPI

````yaml POST /api/v2/secret-scanning/data-sources/bitbucket/{dataSourceId}/scan
paths:
  path: /api/v2/secret-scanning/data-sources/bitbucket/{dataSourceId}/scan
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
        dataSourceId:
          schema:
            - type: string
              required: true
              description: The ID of the Bitbucket Data Source to trigger a scan for.
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
              dataSource:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      externalId:
                        type: string
                        nullable: true
                      name:
                        type: string
                      description:
                        type: string
                        nullable: true
                      encryptedCredentials:
                        nullable: true
                      isAutoScanEnabled:
                        type: boolean
                        default: true
                        nullable: true
                      projectId:
                        type: string
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                      isDisconnected:
                        type: boolean
                        default: false
                      type:
                        type: string
                        enum:
                          - bitbucket
                      connectionId:
                        type: string
                        format: uuid
                      connection:
                        type: object
                        properties:
                          app:
                            type: string
                            enum:
                              - bitbucket
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
                      config:
                        type: object
                        properties:
                          workspaceSlug:
                            type: string
                            minLength: 1
                            maxLength: 128
                            description: The workspace to scan.
                          includeRepos:
                            type: array
                            items:
                              type: string
                              minLength: 1
                              maxLength: 256
                            minItems: 1
                            maxItems: 100
                            default:
                              - '*'
                            description: >-
                              The repositories to include when scanning.
                              Defaults to all repositories (["*"]).
                        required:
                          - workspaceSlug
                        additionalProperties: false
                    required:
                      - id
                      - name
                      - projectId
                      - createdAt
                      - updatedAt
                      - type
                      - connectionId
                      - connection
                      - config
                    additionalProperties: false
                    title: Bitbucket
            requiredProperties:
              - dataSource
            additionalProperties: false
        examples:
          example:
            value:
              dataSource:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                externalId: <string>
                name: <string>
                description: <string>
                encryptedCredentials: <any>
                isAutoScanEnabled: true
                projectId: <string>
                createdAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
                isDisconnected: false
                type: bitbucket
                connectionId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                connection:
                  app: bitbucket
                  name: <string>
                  id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                config:
                  workspaceSlug: <string>
                  includeRepos:
                    - '*'
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