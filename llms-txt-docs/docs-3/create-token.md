# Source: https://docs.turso.tech/api-reference/groups/create-token.md

# Source: https://docs.turso.tech/api-reference/databases/create-token.md

# Generate Database Auth Token

> Generates an authorization token for the specified database.

## OpenAPI

````yaml POST /v1/organizations/{organizationSlug}/databases/{databaseName}/auth/tokens
paths:
  path: /v1/organizations/{organizationSlug}/databases/{databaseName}/auth/tokens
  method: post
  servers:
    - url: https://api.turso.tech
      description: Turso's Platform API
  request:
    security: []
    parameters:
      path:
        organizationSlug:
          schema:
            - type: string
              required: true
              description: The slug of the organization or user account.
        databaseName:
          schema:
            - type: string
              required: true
              description: The name of the database.
      query:
        expiration:
          schema:
            - type: string
              description: Expiration time for the token (e.g., 2w1d30m).
              default: never
        authorization:
          schema:
            - type: enum<string>
              enum:
                - full-access
                - read-only
              description: Authorization level for the token (full-access or read-only).
              default: full-access
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              permissions:
                allOf:
                  - type: object
                    description: The permissions for the token.
                    properties:
                      read_attach:
                        type: object
                        description: Read `ATTACH` permission for the token.
                        properties:
                          databases:
                            type: array
                            items:
                              type: string
            required: false
            refIdentifier: '#/components/schemas/CreateTokenInput'
        examples:
          example:
            value:
              permissions:
                read_attach:
                  databases:
                    - <string>
        description: Additional context such as claims required for the token.
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              jwt:
                allOf:
                  - type: string
                    description: The generated authorization token (JWT).
        examples:
          example:
            value:
              jwt: <string>
        description: Successful response
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message
                    example: Invalid expiration format
        examples:
          example:
            value:
              error: Invalid expiration format
        description: Bad Request
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message
                    example: >-
                      could not find database with name [databaseName]: record
                      not found
        examples:
          example:
            value:
              error: >-
                could not find database with name [databaseName]: record not
                found
        description: Database not found
  deprecated: false
  type: path
components:
  schemas: {}

````