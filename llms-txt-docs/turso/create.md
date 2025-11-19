# Source: https://docs.turso.tech/cli/org/create.md

# Source: https://docs.turso.tech/cli/group/tokens/create.md

# Source: https://docs.turso.tech/cli/group/create.md

# Source: https://docs.turso.tech/cli/db/tokens/create.md

# Source: https://docs.turso.tech/cli/db/create.md

# Source: https://docs.turso.tech/api-reference/tokens/create.md

# Source: https://docs.turso.tech/api-reference/organizations/invites/create.md

# Source: https://docs.turso.tech/api-reference/groups/create.md

# Source: https://docs.turso.tech/api-reference/databases/create.md

# Create Database

> Creates a new database in a group for the organization or user.

## OpenAPI

````yaml POST /v1/organizations/{organizationSlug}/databases
paths:
  path: /v1/organizations/{organizationSlug}/databases
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    description: >-
                      The name of the new database. Must contain only lowercase
                      letters, numbers, dashes. No longer than 64 characters.
              group:
                allOf:
                  - type: string
                    description: >-
                      The name of the group where the database should be
                      created. **The group must already exist.**
              seed:
                allOf:
                  - type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - database
                          - database_upload
                        description: The type of seed to be used to create a new database.
                        example: database
                      name:
                        type: string
                        description: >-
                          The name of the existing database when `database` is
                          used as a seed type.
                        example: my-db
                      timestamp:
                        type: string
                        description: >-
                          A formatted [ISO
                          8601](https://en.wikipedia.org/wiki/ISO_8601) recovery
                          point to create a database from. This must be within
                          the last 24 hours, or 30 days on the scaler plan.
                        example: '2023-12-20T09:46:08Z'
              size_limit:
                allOf:
                  - type: string
                    description: >-
                      The maximum size of the database in bytes. Values with
                      units are also accepted, e.g. 1mb, 256mb, 1gb.
            required: true
            refIdentifier: '#/components/schemas/CreateDatabaseInput'
            requiredProperties:
              - name
              - group
        examples:
          example:
            value:
              name: <string>
              group: <string>
              seed:
                type: database
                name: my-db
                timestamp: '2023-12-20T09:46:08Z'
              size_limit: <string>
        description: Database data to create a new database
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              database:
                allOf:
                  - $ref: '#/components/schemas/CreateDatabaseOutput'
                    description: The newly created database
        examples:
          example:
            value:
              database:
                DbId: 0eb771dd-6906-11ee-8553-eaa7715aeaf2
                Hostname: '[databaseName]-[organizationSlug].turso.io'
                Name: my-db
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
                    example: group not found
        examples:
          example:
            value:
              error: group not found
        description: Bad Request
    '409':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message
                    example: database with name [databaseName] already exists
        examples:
          example:
            value:
              error: database with name [databaseName] already exists
        description: Conflict
  deprecated: false
  type: path
components:
  schemas:
    CreateDatabaseOutput:
      type: object
      properties:
        DbId:
          $ref: '#/components/schemas/Database/properties/DbId'
        Hostname:
          $ref: '#/components/schemas/Database/properties/Hostname'
        Name:
          $ref: '#/components/schemas/Database/properties/Name'

````