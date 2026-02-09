# Source: https://infisical.com/docs/api-reference/endpoints/project-users/update-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/organizations/update-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-users/update-membership.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update User Membership

> Update project user membership



## OpenAPI

````yaml PATCH /api/v1/workspace/{workspaceId}/memberships/{membershipId}
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
  /api/v1/workspace/{workspaceId}/memberships/{membershipId}:
    patch:
      tags:
        - Project Users
      description: Update project user membership
      parameters:
        - schema:
            type: string
          in: path
          name: workspaceId
          required: true
          description: The ID of the project to update the membership for.
        - schema:
            type: string
          in: path
          name: membershipId
          required: true
          description: The ID of the membership to update.
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                roles:
                  type: array
                  items:
                    anyOf:
                      - type: object
                        properties:
                          role:
                            type: string
                          isTemporary:
                            type: boolean
                            enum:
                              - false
                            default: false
                        required:
                          - role
                        additionalProperties: false
                      - type: object
                        properties:
                          role:
                            type: string
                          isTemporary:
                            type: boolean
                            enum:
                              - true
                          temporaryMode:
                            type: string
                            enum:
                              - relative
                          temporaryRange:
                            type: string
                          temporaryAccessStartTime:
                            type: string
                            format: date-time
                        required:
                          - role
                          - isTemporary
                          - temporaryMode
                          - temporaryRange
                          - temporaryAccessStartTime
                        additionalProperties: false
                  minItems: 1
                  description: A list of roles to update the membership to.
              required:
                - roles
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
                  roles:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          format: uuid
                        role:
                          type: string
                        projectMembershipId:
                          type: string
                          format: uuid
                        customRoleId:
                          type: string
                          format: uuid
                          nullable: true
                        isTemporary:
                          type: boolean
                          default: false
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
                        createdAt:
                          type: string
                          format: date-time
                        updatedAt:
                          type: string
                          format: date-time
                      required:
                        - id
                        - role
                        - projectMembershipId
                        - createdAt
                        - updatedAt
                      additionalProperties: false
                required:
                  - roles
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