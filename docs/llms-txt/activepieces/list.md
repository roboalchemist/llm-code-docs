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

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Connections

> List app connections



## OpenAPI

````yaml GET /v1/app-connections
openapi: 3.0.3
info:
  title: Activepieces Documentation
  version: 0.0.0
servers:
  - url: https://cloud.activepieces.com/api
    description: Production Server
security: []
externalDocs:
  url: https://www.activepieces.com/docs
  description: Find more info here
paths:
  /v1/app-connections:
    get:
      tags:
        - app-connections
      description: List app connections
      parameters:
        - schema:
            type: string
          in: query
          name: cursor
          required: false
        - schema:
            type: string
          in: query
          name: projectId
          required: true
        - schema:
            anyOf:
              - type: string
                enum:
                  - PROJECT
              - type: string
                enum:
                  - PLATFORM
          in: query
          name: scope
          required: false
        - schema:
            type: string
          in: query
          name: pieceName
          required: false
        - schema:
            type: string
          in: query
          name: displayName
          required: false
        - schema:
            type: array
            items:
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
          in: query
          name: status
          required: false
        - schema:
            type: number
          in: query
          name: limit
          required: false
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
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
                            lastActiveDate:
                              type: string
                              nullable: true
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
                        pieceVersion:
                          type: string
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
                        - pieceVersion
                  next:
                    description: Cursor to the next page
                    type: string
                    nullable: true
                  previous:
                    description: Cursor to the previous page
                    type: string
                    nullable: true
                required:
                  - data
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: http
      description: Use your api key generated from the admin console
      scheme: bearer

````