# Source: https://infisical.com/docs/api-reference/endpoints/identity-specific-privilege/v2/find-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/identity-specific-privilege/v1/find-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/identity-specific-privilege/v2/find-by-slug.md

# Source: https://infisical.com/docs/api-reference/endpoints/identity-specific-privilege/v1/find-by-slug.md

# Find By Slug

> Retrieve details of a specific privilege by privilege slug.

## OpenAPI

````yaml GET /api/v1/additional-privilege/identity/{privilegeSlug}
paths:
  path: /api/v1/additional-privilege/identity/{privilegeSlug}
  method: get
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
        privilegeSlug:
          schema:
            - type: string
              required: true
              description: The slug of the privilege.
              minLength: 1
      query:
        identityId:
          schema:
            - type: string
              required: true
              description: The ID of the machine identity to list.
              minLength: 1
        projectSlug:
          schema:
            - type: string
              required: true
              description: The slug of the project of the identity in.
              minLength: 1
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              privilege:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      slug:
                        type: string
                      projectMembershipId:
                        type: string
                        format: uuid
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
                      permissions:
                        type: array
                        items:
                          type: object
                          properties:
                            subject:
                              anyOf:
                                - type: string
                                  minLength: 1
                                - type: array
                                  items:
                                    type: string
                            action:
                              anyOf:
                                - type: string
                                  minLength: 1
                                - type: array
                                  items:
                                    type: string
                            conditions: {}
                            inverted:
                              type: boolean
                          required:
                            - action
                          additionalProperties: false
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                    required:
                      - id
                      - slug
                      - projectMembershipId
                      - permissions
                      - createdAt
                      - updatedAt
                    additionalProperties: false
            requiredProperties:
              - privilege
            additionalProperties: false
        examples:
          example:
            value:
              privilege:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                slug: <string>
                projectMembershipId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                isTemporary: false
                temporaryMode: <string>
                temporaryRange: <string>
                temporaryAccessStartTime: '2023-11-07T05:31:56Z'
                temporaryAccessEndTime: '2023-11-07T05:31:56Z'
                permissions:
                  - subject: <string>
                    action: <string>
                    conditions: <any>
                    inverted: true
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