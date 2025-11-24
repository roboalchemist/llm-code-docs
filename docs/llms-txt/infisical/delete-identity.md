# Source: https://infisical.com/docs/api-reference/endpoints/project-identities/delete-identity.md

# Delete Identity

> Delete an identity from a project

## OpenAPI

````yaml DELETE /api/v1/projects/{projectId}/identities/{identityId}
paths:
  path: /api/v1/projects/{projectId}/identities/{identityId}
  method: delete
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
        projectId:
          schema:
            - type: string
              required: true
              description: The ID of the project
        identityId:
          schema:
            - type: string
              required: true
              description: The ID of the machine identity to delete.
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
              identity:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      name:
                        type: string
                      orgId:
                        type: string
                        format: uuid
                      projectId:
                        type: string
                        nullable: true
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                      hasDeleteProtection:
                        type: boolean
                        default: false
                      activeLockoutAuthMethods:
                        type: array
                        items:
                          type: string
                      authMethods:
                        type: array
                        items:
                          type: string
                      metadata:
                        type: array
                        items:
                          type: object
                          properties:
                            key:
                              type: string
                            value:
                              type: string
                            id:
                              type: string
                          required:
                            - key
                            - value
                            - id
                          additionalProperties: false
                    required:
                      - id
                      - name
                      - orgId
                      - createdAt
                      - updatedAt
                    additionalProperties: false
            requiredProperties:
              - identity
            additionalProperties: false
        examples:
          example:
            value:
              identity:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                name: <string>
                orgId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                projectId: <string>
                createdAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
                hasDeleteProtection: false
                activeLockoutAuthMethods:
                  - <string>
                authMethods:
                  - <string>
                metadata:
                  - key: <string>
                    value: <string>
                    id: <string>
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