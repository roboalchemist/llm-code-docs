# Source: https://infisical.com/docs/api-reference/endpoints/organizations/delete-membership.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete User Membership

> Delete organization user memberships



## OpenAPI

````yaml DELETE /api/v2/organizations/{organizationId}/memberships/{membershipId}
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
  /api/v2/organizations/{organizationId}/memberships/{membershipId}:
    delete:
      tags:
        - Organizations
      description: Delete organization user memberships
      operationId: deleteOrgMembership
      parameters:
        - schema:
            type: string
          in: path
          name: organizationId
          required: true
          description: The ID of the organization to delete the membership from.
        - schema:
            type: string
          in: path
          name: membershipId
          required: true
          description: The ID of the membership to delete.
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
                      role:
                        type: string
                      status:
                        type: string
                        default: invited
                      inviteEmail:
                        type: string
                        nullable: true
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                      userId:
                        type: string
                        format: uuid
                        nullable: true
                      orgId:
                        type: string
                        format: uuid
                      roleId:
                        type: string
                        format: uuid
                        nullable: true
                      projectFavorites:
                        type: array
                        items:
                          type: string
                        nullable: true
                      isActive:
                        type: boolean
                        default: true
                      lastInvitedAt:
                        type: string
                        format: date-time
                        nullable: true
                      lastLoginAuthMethod:
                        type: string
                        nullable: true
                      lastLoginTime:
                        type: string
                        format: date-time
                        nullable: true
                    required:
                      - id
                      - role
                      - createdAt
                      - updatedAt
                      - orgId
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