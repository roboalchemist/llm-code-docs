# Source: https://infisical.com/docs/api-reference/endpoints/project-identities-membership/update-identity-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-identities-v2/update-identity-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/project-identities-membership/update-identity-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-identities-v2/update-identity-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/project-identities-membership/update-identity-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-identities-v2/update-identity-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/project-identities-membership/update-identity-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-identities-v2/update-identity-membership.md

# Update Identity Membership

> Update project identity memberships

## OpenAPI

````yaml PATCH /api/v1/projects/{projectId}/identity-memberships/{identityId}
paths:
  path: /api/v1/projects/{projectId}/identity-memberships/{identityId}
  method: patch
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
              description: The ID of the project to update the identity membership for.
        identityId:
          schema:
            - type: string
              required: true
              description: The ID of the machine identity to update the membership for.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              roles:
                allOf:
                  - type: array
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
                                Expiry time for temporary access. In relative
                                mode it could be 1s, 2m ,3h, etc.
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
            required: true
            requiredProperties:
              - roles
            additionalProperties: false
        examples:
          example:
            value:
              roles:
                - role: <string>
                  isTemporary: false
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              roles:
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
            requiredProperties:
              - roles
            additionalProperties: false
        examples:
          example:
            value:
              roles:
                - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  role: <string>
                  projectMembershipId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  customRoleId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  isTemporary: false
                  temporaryMode: <string>
                  temporaryRange: <string>
                  temporaryAccessStartTime: '2023-11-07T05:31:56Z'
                  temporaryAccessEndTime: '2023-11-07T05:31:56Z'
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
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