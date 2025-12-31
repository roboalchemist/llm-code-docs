# Source: https://www.activepieces.com/docs/endpoints/users/list.md

# Source: https://www.activepieces.com/docs/endpoints/user-invitations/list.md

# Source: https://www.activepieces.com/docs/endpoints/templates/list.md

# Source: https://www.activepieces.com/docs/endpoints/projects/list.md

# Source: https://www.activepieces.com/docs/endpoints/project-members/list.md

# Source: https://www.activepieces.com/docs/endpoints/global-connections/list.md

# Source: https://www.activepieces.com/docs/endpoints/folders/list.md

# Source: https://www.activepieces.com/docs/endpoints/flows/list.md

# Source: https://www.activepieces.com/docs/endpoints/flow-runs/list.md

# Source: https://www.activepieces.com/docs/endpoints/connections/list.md

# Source: https://www.activepieces.com/docs/endpoints/users/list.md

# Source: https://www.activepieces.com/docs/endpoints/user-invitations/list.md

# Source: https://www.activepieces.com/docs/endpoints/templates/list.md

# Source: https://www.activepieces.com/docs/endpoints/projects/list.md

# Source: https://www.activepieces.com/docs/endpoints/project-members/list.md

# Source: https://www.activepieces.com/docs/endpoints/global-connections/list.md

# Source: https://www.activepieces.com/docs/endpoints/folders/list.md

# Source: https://www.activepieces.com/docs/endpoints/flows/list.md

# Source: https://www.activepieces.com/docs/endpoints/flow-runs/list.md

# Source: https://www.activepieces.com/docs/endpoints/connections/list.md

# Source: https://www.activepieces.com/docs/endpoints/users/list.md

# Source: https://www.activepieces.com/docs/endpoints/user-invitations/list.md

# Source: https://www.activepieces.com/docs/endpoints/projects/list.md

# Source: https://www.activepieces.com/docs/endpoints/project-members/list.md

# Source: https://www.activepieces.com/docs/endpoints/mcp-servers/list.md

# Source: https://www.activepieces.com/docs/endpoints/global-connections/list.md

# Source: https://www.activepieces.com/docs/endpoints/folders/list.md

# Source: https://www.activepieces.com/docs/endpoints/flows/list.md

# Source: https://www.activepieces.com/docs/endpoints/flow-templates/list.md

# Source: https://www.activepieces.com/docs/endpoints/flow-runs/list.md

# Source: https://www.activepieces.com/docs/endpoints/connections/list.md

# List Connections

> List app connections

## OpenAPI

````yaml GET /v1/app-connections
paths:
  path: /v1/app-connections
  method: get
  servers:
    - url: https://cloud.activepieces.com/api
      description: Production Server
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Use your api key generated from the admin console
          cookie: {}
    parameters:
      path: {}
      query:
        cursor:
          schema:
            - type: string
              required: false
        projectId:
          schema:
            - type: string
              required: true
        scope:
          schema:
            - type: enum<string>
              enum:
                - PROJECT
              required: false
            - type: enum<string>
              enum:
                - PLATFORM
              required: false
        pieceName:
          schema:
            - type: string
              required: false
        displayName:
          schema:
            - type: string
              required: false
        status:
          schema:
            - type: array
              items:
                allOf:
                  - anyOf:
                      - type: string
                        enum:
                          - ACTIVE
                      - type: string
                        enum:
                          - MISSING
                      - type: string
                        enum:
                          - ERROR
              required: false
        limit:
          schema:
            - type: number
              required: false
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: array
                    items:
                      description: App connection is a connection to an external app.
                      type: object
                      properties:
                        id:
                          type: string
                        created:
                          type: string
                        updated:
                          type: string
                        externalId:
                          type: string
                        displayName:
                          type: string
                        type:
                          anyOf:
                            - type: string
                              enum:
                                - OAUTH2
                            - type: string
                              enum:
                                - PLATFORM_OAUTH2
                            - type: string
                              enum:
                                - CLOUD_OAUTH2
                            - type: string
                              enum:
                                - SECRET_TEXT
                            - type: string
                              enum:
                                - BASIC_AUTH
                            - type: string
                              enum:
                                - CUSTOM_AUTH
                            - type: string
                              enum:
                                - NO_AUTH
                        pieceName:
                          type: string
                        projectIds:
                          type: array
                          items:
                            pattern: ^[0-9a-zA-Z]{21}$
                            type: string
                        platformId:
                          type: string
                          nullable: true
                        scope:
                          anyOf:
                            - type: string
                              enum:
                                - PROJECT
                            - type: string
                              enum:
                                - PLATFORM
                        status:
                          anyOf:
                            - type: string
                              enum:
                                - ACTIVE
                            - type: string
                              enum:
                                - MISSING
                            - type: string
                              enum:
                                - ERROR
                        ownerId:
                          type: string
                          nullable: true
                        owner:
                          type: object
                          properties:
                            id:
                              type: string
                            email:
                              type: string
                            firstName:
                              type: string
                            status:
                              anyOf:
                                - type: string
                                  enum:
                                    - ACTIVE
                                - type: string
                                  enum:
                                    - INACTIVE
                            externalId:
                              type: string
                              nullable: true
                            lastChangelogDismissed:
                              type: string
                              nullable: true
                            platformId:
                              type: string
                              nullable: true
                            platformRole:
                              anyOf:
                                - type: string
                                  enum:
                                    - ADMIN
                                - type: string
                                  enum:
                                    - MEMBER
                                - type: string
                                  enum:
                                    - OPERATOR
                            lastName:
                              type: string
                            created:
                              type: string
                            updated:
                              type: string
                          required:
                            - id
                            - email
                            - firstName
                            - status
                            - platformRole
                            - lastName
                            - created
                            - updated
                          nullable: true
                        metadata:
                          type: object
                          nullable: true
                          additionalProperties: {}
                        flowIds:
                          type: array
                          items:
                            pattern: ^[0-9a-zA-Z]{21}$
                            type: string
                          nullable: true
                      required:
                        - id
                        - created
                        - updated
                        - externalId
                        - displayName
                        - type
                        - pieceName
                        - projectIds
                        - scope
                        - status
              next:
                allOf:
                  - description: Cursor to the next page
                    type: string
                    nullable: true
              previous:
                allOf:
                  - description: Cursor to the previous page
                    type: string
                    nullable: true
            requiredProperties:
              - data
        examples:
          example:
            value:
              data:
                - id: <string>
                  created: <string>
                  updated: <string>
                  externalId: <string>
                  displayName: <string>
                  type: OAUTH2
                  pieceName: <string>
                  projectIds:
                    - <string>
                  platformId: <string>
                  scope: PROJECT
                  status: ACTIVE
                  ownerId: <string>
                  owner:
                    id: <string>
                    email: <string>
                    firstName: <string>
                    status: ACTIVE
                    externalId: <string>
                    lastChangelogDismissed: <string>
                    platformId: <string>
                    platformRole: ADMIN
                    lastName: <string>
                    created: <string>
                    updated: <string>
                  metadata: {}
                  flowIds:
                    - <string>
              next: <string>
              previous: <string>
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````