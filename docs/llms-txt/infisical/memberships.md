# Source: https://infisical.com/docs/api-reference/endpoints/project-users/memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/organizations/memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-users/memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/project-users/memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/organizations/memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-users/memberships.md

# Get User Memberships

> Return project user memberships

## OpenAPI

````yaml GET /api/v1/workspace/{workspaceId}/memberships
paths:
  path: /api/v1/workspace/{workspaceId}/memberships
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
              description: The ID of the project to get memberships from.
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
              memberships:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          format: uuid
                        createdAt:
                          type: string
                          format: date-time
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
                            username:
                              type: string
                            publicKey:
                              type: string
                              nullable: true
                          required:
                            - id
                            - username
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
                        - createdAt
                        - userId
                        - projectId
                        - user
                        - roles
                      additionalProperties: false
            requiredProperties:
              - memberships
            additionalProperties: false
        examples:
          example:
            value:
              memberships:
                - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  createdAt: '2023-11-07T05:31:56Z'
                  userId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  projectId: <string>
                  user:
                    email: <string>
                    firstName: <string>
                    lastName: <string>
                    id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                    username: <string>
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