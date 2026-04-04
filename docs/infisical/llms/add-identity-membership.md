# Source: https://infisical.com/docs/api-reference/endpoints/project-identities-membership/add-identity-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-identities-v2/add-identity-membership.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Identity Membership

> Create project identity membership



## OpenAPI

````yaml POST /api/v1/projects/{projectId}/identity-memberships/{identityId}
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
  /api/v1/projects/{projectId}/identity-memberships/{identityId}:
    post:
      tags:
        - Project Identities
      description: Create project identity membership
      parameters:
        - schema:
            type: string
          in: path
          name: projectId
          required: true
        - schema:
            type: string
          in: path
          name: identityId
          required: true
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                role:
                  type: string
                  default: no-access
                roles:
                  type: array
                  items:
                    anyOf:
                      - type: object
                        properties:
                          role:
                            type: string
                            description: >-
                              The role slug to assign to the newly created
                              identity project membership.
                          isTemporary:
                            type: boolean
                            enum:
                              - false
                            default: false
                            description: >-
                              The role slug to assign to the newly created
                              identity project membership.
                        required:
                          - role
                        additionalProperties: false
                      - type: object
                        properties:
                          role:
                            type: string
                            description: >-
                              The role slug to assign to the newly created
                              identity project membership.
                          isTemporary:
                            type: boolean
                            enum:
                              - true
                            description: >-
                              The role slug to assign to the newly created
                              identity project membership.
                          temporaryMode:
                            type: string
                            enum:
                              - relative
                            description: >-
                              The role slug to assign to the newly created
                              identity project membership.
                          temporaryRange:
                            type: string
                            description: >-
                              The role slug to assign to the newly created
                              identity project membership.
                          temporaryAccessStartTime:
                            type: string
                            format: date-time
                            description: >-
                              The role slug to assign to the newly created
                              identity project membership.
                        required:
                          - role
                          - isTemporary
                          - temporaryMode
                          - temporaryRange
                          - temporaryAccessStartTime
                        additionalProperties: false
                  description: >-
                    A list of role slugs to assign to the newly created identity
                    project membership.
              additionalProperties: false
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  identityMembership:
                    type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      projectId:
                        type: string
                      identityId:
                        type: string
                        format: uuid
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                    required:
                      - id
                      - projectId
                      - identityId
                      - createdAt
                      - updatedAt
                    additionalProperties: false
                required:
                  - identityMembership
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