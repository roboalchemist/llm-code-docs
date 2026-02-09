# Source: https://infisical.com/docs/api-reference/endpoints/project-identities-membership/update-identity-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-identities-v2/update-identity-membership.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Identity Membership

> Update project identity memberships



## OpenAPI

````yaml PATCH /api/v1/projects/{projectId}/identity-memberships/{identityId}
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
    patch:
      tags:
        - Project Identities
      description: Update project identity memberships
      parameters:
        - schema:
            type: string
          in: path
          name: projectId
          required: true
          description: The ID of the project to update the identity membership for.
        - schema:
            type: string
          in: path
          name: identityId
          required: true
          description: The ID of the machine identity to update the membership for.
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
                            description: >-
                              The role slug to assign to the newly created
                              identity project membership.
                          isTemporary:
                            type: boolean
                            enum:
                              - false
                            default: false
                            description: >-
                              Whether the assigned role is temporary. If
                              isTemporary is set true, must provide
                              temporaryMode, temporaryRange and
                              temporaryAccessStartTime.
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
                              Whether the assigned role is temporary. If
                              isTemporary is set true, must provide
                              temporaryMode, temporaryRange and
                              temporaryAccessStartTime.
                          temporaryMode:
                            type: string
                            enum:
                              - relative
                            description: Type of temporary expiry.
                          temporaryRange:
                            type: string
                            description: >-
                              Expiry time for temporary access. In relative mode
                              it could be 1s, 2m ,3h, etc.
                          temporaryAccessStartTime:
                            type: string
                            format: date-time
                            description: Time to which the temporary access starts.
                        required:
                          - role
                          - isTemporary
                          - temporaryMode
                          - temporaryRange
                          - temporaryAccessStartTime
                        additionalProperties: false
                  minItems: 1
                  description: >-
                    A list of role slugs to assign to the identity project
                    membership.
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