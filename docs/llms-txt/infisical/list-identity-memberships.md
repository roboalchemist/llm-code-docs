# Source: https://infisical.com/docs/api-reference/endpoints/project-identities-membership/list-identity-memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/organizations/list-identity-memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-identities-v2/list-identity-memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/project-identities-membership/list-identity-memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/organizations/list-identity-memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-identities-v2/list-identity-memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/project-identities-membership/list-identity-memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/organizations/list-identity-memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-identities-v2/list-identity-memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/project-identities-membership/list-identity-memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/organizations/list-identity-memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-identities-v2/list-identity-memberships.md

# List Identity Memberships

> Return project identity memberships

## OpenAPI

````yaml GET /api/v1/projects/{projectId}/identity-memberships
paths:
  path: /api/v1/projects/{projectId}/identity-memberships
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
        projectId:
          schema:
            - type: string
              required: true
              description: The ID of the project to get identity memberships from.
      query:
        offset:
          schema:
            - type: number
              required: false
              description: >-
                The offset to start from. If you enter 10, it will start from
                the 10th identity membership.
              minimum: 0
              default: 0
        limit:
          schema:
            - type: number
              required: false
              description: The number of identity memberships to return.
              maximum: 20000
              minimum: 1
              default: 100
        orderBy:
          schema:
            - type: enum<string>
              enum:
                - name
              required: false
              description: The column to order identity memberships by.
              default: name
        orderDirection:
          schema:
            - type: enum<string>
              enum:
                - asc
                - desc
              required: false
              description: The direction identity memberships will be sorted in.
              default: asc
        search:
          schema:
            - type: string
              required: false
              description: >-
                The text string that identity membership names will be filtered
                by.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              identityMemberships:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                        identityId:
                          type: string
                        createdAt:
                          type: string
                          format: date-time
                        updatedAt:
                          type: string
                          format: date-time
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
                        identity:
                          type: object
                          properties:
                            name:
                              type: string
                            id:
                              type: string
                              format: uuid
                            projectId:
                              type: string
                              nullable: true
                            orgId:
                              type: string
                              format: uuid
                            authMethods:
                              type: array
                              items:
                                type: string
                          required:
                            - name
                            - id
                            - orgId
                            - authMethods
                          additionalProperties: false
                        project:
                          type: object
                          properties:
                            name:
                              type: string
                            id:
                              type: string
                          required:
                            - name
                            - id
                          additionalProperties: false
                      required:
                        - id
                        - identityId
                        - createdAt
                        - updatedAt
                        - roles
                        - identity
                        - project
                      additionalProperties: false
              totalCount:
                allOf:
                  - type: number
            requiredProperties:
              - identityMemberships
              - totalCount
            additionalProperties: false
        examples:
          example:
            value:
              identityMemberships:
                - id: <string>
                  identityId: <string>
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
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
                  identity:
                    name: <string>
                    id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                    projectId: <string>
                    orgId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                    authMethods:
                      - <string>
                  project:
                    name: <string>
                    id: <string>
              totalCount: 123
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