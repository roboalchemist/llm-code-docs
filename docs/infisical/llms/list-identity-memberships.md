# Source: https://infisical.com/docs/api-reference/endpoints/project-identities-membership/list-identity-memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/organizations/list-identity-memberships.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-identities-v2/list-identity-memberships.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Identity Memberships

> Return project identity memberships



## OpenAPI

````yaml GET /api/v1/projects/{projectId}/identity-memberships
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
  /api/v1/projects/{projectId}/identity-memberships:
    get:
      tags:
        - Project Identities
      description: Return project identity memberships
      parameters:
        - schema:
            type: number
            minimum: 0
            default: 0
          in: query
          name: offset
          required: false
          description: >-
            The offset to start from. If you enter 10, it will start from the
            10th identity membership.
        - schema:
            type: number
            minimum: 1
            maximum: 20000
            default: 100
          in: query
          name: limit
          required: false
          description: The number of identity memberships to return.
        - schema:
            type: string
            enum:
              - name
            default: name
          in: query
          name: orderBy
          required: false
          description: The column to order identity memberships by.
        - schema:
            type: string
            enum:
              - asc
              - desc
            default: asc
          in: query
          name: orderDirection
          required: false
          description: The direction identity memberships will be sorted in.
        - schema:
            type: string
          in: query
          name: search
          required: false
          description: The text string that identity membership names will be filtered by.
        - schema:
            type: string
          in: path
          name: projectId
          required: true
          description: The ID of the project to get identity memberships from.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  identityMemberships:
                    type: array
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
                    type: number
                required:
                  - identityMemberships
                  - totalCount
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