# Source: https://docs.turso.tech/api-reference/groups/invalidate-tokens.md

# Source: https://docs.turso.tech/api-reference/databases/invalidate-tokens.md

# Source: https://docs.turso.tech/api-reference/groups/invalidate-tokens.md

# Source: https://docs.turso.tech/api-reference/databases/invalidate-tokens.md

# Invalidate All Database Auth Tokens

> Invalidates all authorization tokens for the specified database.

## OpenAPI

````yaml POST /v1/organizations/{organizationSlug}/databases/{databaseName}/auth/rotate
paths:
  path: /v1/organizations/{organizationSlug}/databases/{databaseName}/auth/rotate
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
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Successful response (No Content)
        examples: {}
        description: Successful response (No Content)
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