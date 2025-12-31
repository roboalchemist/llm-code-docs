# Source: https://infisical.com/docs/api-reference/endpoints/project-users/get-by-username.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-users/get-by-username.md

# Source: https://infisical.com/docs/api-reference/endpoints/project-users/get-by-username.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-users/get-by-username.md

# Source: https://infisical.com/docs/api-reference/endpoints/project-users/get-by-username.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-users/get-by-username.md

# Source: https://infisical.com/docs/api-reference/endpoints/project-users/get-by-username.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-users/get-by-username.md

# Get By Username

> Return project user memberships

## OpenAPI

````yaml POST /api/v1/workspace/{workspaceId}/memberships/details
paths:
  path: /api/v1/workspace/{workspaceId}/memberships/details
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
        workspaceId:
          schema:
            - type: string
              required: true
              description: The ID of the project to get memberships from.
              minLength: 1
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              username:
                allOf:
                  - type: string
                    minLength: 1
                    description: >-
                      The username to get project membership of. Email is the
                      default username.
            required: true
            requiredProperties:
              - username
            additionalProperties: false
        examples:
          example:
            value:
              username: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              membership:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      userId:
                        type: string
                        format: uuid
                      projectId:
                        type: string
                      user:
                        type: object
                        properties:
                          email:
                            type: string
                            nullable: true
                          firstName:
                            type: string
                            nullable: true
                          lastName:
                            type: string
                            nullable: true
                          id:
                            type: string
                            format: uuid
                          publicKey:
                            type: string
                            nullable: true
                        required:
                          - id
                        additionalProperties: false
                      roles:
                        type: array
                        items:
                          type: object
                          properties:
                            id:
                              type: string
                            role:
                              type: string
                            customRoleId:
                              type: string
                              nullable: true
                            customRoleName:
                              type: string
                              nullable: true
                            customRoleSlug:
                              type: string
                              nullable: true
                            isTemporary:
                              type: boolean
                            temporaryMode:
                              type: string
                              nullable: true
                            temporaryRange:
                              type: string
                              nullable: true
                            temporaryAccessStartTime:
                              type: string
                              format: date-time
                              nullable: true
                            temporaryAccessEndTime:
                              type: string
                              format: date-time
                              nullable: true
                          required:
                            - id
                            - role
                            - isTemporary
                          additionalProperties: false
                    required:
                      - id
                      - userId
                      - projectId
                      - user
                      - roles
                    additionalProperties: false
            requiredProperties:
              - membership
            additionalProperties: false
        examples:
          example:
            value:
              membership:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                userId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                projectId: <string>
                user:
                  email: <string>
                  firstName: <string>
                  lastName: <string>
                  id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  publicKey: <string>
                roles:
                  - id: <string>
                    role: <string>
                    customRoleId: <string>
                    customRoleName: <string>
                    customRoleSlug: <string>
                    isTemporary: true
                    temporaryMode: <string>
                    temporaryRange: <string>
                    temporaryAccessStartTime: '2023-11-07T05:31:56Z'
                    temporaryAccessEndTime: '2023-11-07T05:31:56Z'
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