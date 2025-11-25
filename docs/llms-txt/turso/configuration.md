# Source: https://docs.turso.tech/api-reference/groups/configuration.md

# Source: https://docs.turso.tech/api-reference/databases/configuration.md

# Source: https://docs.turso.tech/api-reference/groups/configuration.md

# Source: https://docs.turso.tech/api-reference/databases/configuration.md

# Retrieve Database Configuration

> Retrieve an individual database configuration belonging to the organization or user.

## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/databases/{databaseName}/configuration
paths:
  path: /v1/organizations/{organizationSlug}/databases/{databaseName}/configuration
  method: get
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
              size_limit:
                allOf:
                  - type: string
                    description: >-
                      The maximum size of the database in bytes. Values with
                      units are also accepted, e.g. 1mb, 256mb, 1gb.
                    example: '10000'
              allow_attach:
                allOf:
                  - type: boolean
                    description: >-
                      Allow or disallow attaching databases to the current
                      database.
                    example: true
                    deprecated: true
              block_reads:
                allOf:
                  - type: boolean
                    description: The current status for blocked reads.
                    example: false
              block_writes:
                allOf:
                  - type: boolean
                    description: The current status for blocked writes.
                    example: false
              delete_protection:
                allOf:
                  - type: boolean
                    description: Prevent the database from being deleted.
                    example: true
            refIdentifier: '#/components/schemas/DatabaseConfigurationResponse'
        examples:
          example:
            value:
              size_limit: '10000'
              allow_attach: true
              block_reads: false
              block_writes: false
              delete_protection: true
        description: Successful response
  deprecated: false
  type: path
components:
  schemas: {}

````