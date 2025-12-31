# Source: https://infisical.com/docs/api-reference/endpoints/project-identities-membership/add-identity-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-identities-v2/add-identity-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/project-identities-membership/add-identity-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-identities-v2/add-identity-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/project-identities-membership/add-identity-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-identities-v2/add-identity-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/project-identities-membership/add-identity-membership.md

# Source: https://infisical.com/docs/api-reference/endpoints/deprecated/project-identities-v2/add-identity-membership.md

# Create Identity Membership

> Create project identity membership

## OpenAPI

````yaml POST /api/v1/projects/{projectId}/identity-memberships/{identityId}
paths:
  path: /api/v1/projects/{projectId}/identity-memberships/{identityId}
  method: post
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
        identityId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              role:
                allOf:
                  - type: string
                    default: no-access
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
                      A list of role slugs to assign to the newly created
                      identity project membership.
            additionalProperties: false
        examples:
          example:
            value:
              role: no-access
              roles:
                - role: <string>
                  isTemporary: false
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              identityMembership:
                allOf:
                  - type: object
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
            requiredProperties:
              - identityMembership
            additionalProperties: false
        examples:
          example:
            value:
              identityMembership:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                projectId: <string>
                identityId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
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