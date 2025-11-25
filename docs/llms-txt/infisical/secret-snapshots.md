# Source: https://infisical.com/docs/api-reference/endpoints/projects/secret-snapshots.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/projects/secret-snapshots.md

# Source: https://infisical.com/docs/api-reference/endpoints/projects/secret-snapshots.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/projects/secret-snapshots.md

# Get Snapshots

> Return project secret snapshots ids

## OpenAPI

````yaml GET /api/v1/workspace/{workspaceId}/secret-snapshots
paths:
  path: /api/v1/workspace/{workspaceId}/secret-snapshots
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
              description: The ID of the project to get snapshots from.
      query:
        environment:
          schema:
            - type: string
              required: true
              description: The environment to get snapshots from.
        path:
          schema:
            - type: string
              required: false
              description: The secret path to get snapshots from.
              default: /
        offset:
          schema:
            - type: number
              required: false
              description: >-
                The offset to start from. If you enter 10, it will start from
                the 10th snapshot.
              default: 0
        limit:
          schema:
            - type: number
              required: false
              description: The number of snapshots to return.
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
              secretSnapshots:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          format: uuid
                        envId:
                          type: string
                          format: uuid
                        folderId:
                          type: string
                          format: uuid
                        parentFolderId:
                          type: string
                          format: uuid
                          nullable: true
                        createdAt:
                          type: string
                          format: date-time
                        updatedAt:
                          type: string
                          format: date-time
                      required:
                        - id
                        - envId
                        - folderId
                        - createdAt
                        - updatedAt
                      additionalProperties: false
            requiredProperties:
              - secretSnapshots
            additionalProperties: false
        examples:
          example:
            value:
              secretSnapshots:
                - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  envId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  folderId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  parentFolderId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
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