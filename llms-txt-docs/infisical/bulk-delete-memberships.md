# Source: https://infisical.com/docs/api-reference/endpoints/organizations/bulk-delete-memberships.md

# Bulk Delete User Memberships

> Bulk delete organization user memberships

## OpenAPI

````yaml DELETE /api/v2/organizations/{organizationId}/memberships
paths:
  path: /api/v2/organizations/{organizationId}/memberships
  method: delete
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
        organizationId:
          schema:
            - type: string
              required: true
              description: The ID of the organization to delete the memberships from.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              membershipIds:
                allOf:
                  - type: array
                    items:
                      type: string
                    description: The IDs of the memberships to delete.
            required: true
            requiredProperties:
              - membershipIds
            additionalProperties: false
        examples:
          example:
            value:
              membershipIds:
                - <string>
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
            requiredProperties:
              - memberships
            additionalProperties: false
        examples:
          example:
            value:
              memberships:
                - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  role: <string>
                  status: invited
                  inviteEmail: <string>
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
                  userId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  orgId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  roleId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  projectFavorites:
                    - <string>
                  isActive: true
                  lastInvitedAt: '2023-11-07T05:31:56Z'
                  lastLoginAuthMethod: <string>
                  lastLoginTime: '2023-11-07T05:31:56Z'
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