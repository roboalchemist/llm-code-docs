# Source: https://infisical.com/docs/api-reference/endpoints/integrations/list-project-integrations.md

# List Project Integrations

> List integrations for a project.

## OpenAPI

````yaml GET /api/v1/workspace/{workspaceId}/integrations
paths:
  path: /api/v1/workspace/{workspaceId}/integrations
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
        workspaceId:
          schema:
            - type: string
              required: true
              description: The ID of the project to list integrations for.
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
              integrations:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          format: uuid
                        isActive:
                          type: boolean
                        url:
                          type: string
                          nullable: true
                        app:
                          type: string
                          nullable: true
                        appId:
                          type: string
                          nullable: true
                        targetEnvironment:
                          type: string
                          nullable: true
                        targetEnvironmentId:
                          type: string
                          nullable: true
                        targetService:
                          type: string
                          nullable: true
                        targetServiceId:
                          type: string
                          nullable: true
                        owner:
                          type: string
                          nullable: true
                        path:
                          type: string
                          nullable: true
                        region:
                          type: string
                          nullable: true
                        scope:
                          type: string
                          nullable: true
                        integration:
                          type: string
                        metadata:
                          nullable: true
                        integrationAuthId:
                          type: string
                          format: uuid
                        envId:
                          type: string
                          format: uuid
                        secretPath:
                          type: string
                          default: /
                        createdAt:
                          type: string
                          format: date-time
                        updatedAt:
                          type: string
                          format: date-time
                        lastUsed:
                          type: string
                          format: date-time
                          nullable: true
                        isSynced:
                          type: boolean
                          nullable: true
                        syncMessage:
                          type: string
                          nullable: true
                        lastSyncJobId:
                          type: string
                          nullable: true
                        environment:
                          type: object
                          properties:
                            id:
                              type: string
                            name:
                              type: string
                            slug:
                              type: string
                          required:
                            - id
                            - name
                            - slug
                          additionalProperties: false
                      required:
                        - id
                        - isActive
                        - integration
                        - integrationAuthId
                        - envId
                        - createdAt
                        - updatedAt
                        - environment
                      additionalProperties: false
            requiredProperties:
              - integrations
            additionalProperties: false
        examples:
          example:
            value:
              integrations:
                - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  isActive: true
                  url: <string>
                  app: <string>
                  appId: <string>
                  targetEnvironment: <string>
                  targetEnvironmentId: <string>
                  targetService: <string>
                  targetServiceId: <string>
                  owner: <string>
                  path: <string>
                  region: <string>
                  scope: <string>
                  integration: <string>
                  metadata: <any>
                  integrationAuthId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  envId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  secretPath: /
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
                  lastUsed: '2023-11-07T05:31:56Z'
                  isSynced: true
                  syncMessage: <string>
                  lastSyncJobId: <string>
                  environment:
                    id: <string>
                    name: <string>
                    slug: <string>
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