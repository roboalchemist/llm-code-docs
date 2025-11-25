# Source: https://docs.turso.tech/api-reference/organizations/invites/delete.md

# Source: https://docs.turso.tech/api-reference/groups/delete.md

# Source: https://docs.turso.tech/api-reference/databases/delete.md

# Source: https://docs.turso.tech/api-reference/organizations/invites/delete.md

# Source: https://docs.turso.tech/api-reference/groups/delete.md

# Source: https://docs.turso.tech/api-reference/databases/delete.md

# Delete Database

> Delete a database belonging to the organization or user.

## OpenAPI

````yaml DELETE /v1/organizations/{organizationSlug}/databases/{databaseName}
paths:
  path: /v1/organizations/{organizationSlug}/databases/{databaseName}
  method: delete
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
      application/json:
        schemaArray:
          - type: object
            properties:
              database:
                allOf:
                  - type: string
                    description: The name of the database that was deleted.
                    example: my-db
        examples:
          example:
            value:
              database: my-db
        description: Successful response
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