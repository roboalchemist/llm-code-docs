# Source: https://infisical.com/docs/api-reference/endpoints/project-users/get-by-username.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-users/get-by-username.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get By Username

> Return project user memberships



## OpenAPI

````yaml POST /api/v1/workspace/{workspaceId}/memberships/details
openapi: 3.0.3
info:
  title: Infisical API
  description: List of all available APIs that can be consumed
  version: 0.0.1
servers:
  - url: https://us.infisical.com
    description: Production server (US)
  - url: https://eu.infisical.com
    description: Production server (EU)
  - url: http://localhost:8080
    description: Local server
security: []
paths:
  /api/v1/workspace/{workspaceId}/memberships/details:
    post:
      tags:
        - Project Users
      description: Return project user memberships
      parameters:
        - schema:
            type: string
            minLength: 1
          in: path
          name: workspaceId
          required: true
          description: The ID of the project to get memberships from.
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                username:
                  type: string
                  minLength: 1
                  description: >-
                    The username to get project membership of. Email is the
                    default username.
              required:
                - username
              additionalProperties: false
        required: true
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  membership:
                    type: object
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
                required:
                  - membership
                additionalProperties: false
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 400
                  message:
                    type: string
                  error:
                    type: string
                  details: {}
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '401':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 401
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '403':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 403
                  message:
                    type: string
                  details: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '404':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 404
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '422':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 422
                  message: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - error
                additionalProperties: false
        '500':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 500
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: An access token in Infisical

````