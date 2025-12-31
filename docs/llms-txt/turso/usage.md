# Source: https://docs.turso.tech/sync/usage.md

# Source: https://docs.turso.tech/api-reference/organizations/usage.md

# Source: https://docs.turso.tech/api-reference/databases/usage.md

# Source: https://docs.turso.tech/sync/usage.md

# Source: https://docs.turso.tech/api-reference/organizations/usage.md

# Source: https://docs.turso.tech/api-reference/databases/usage.md

# Source: https://docs.turso.tech/api-reference/organizations/usage.md

# Source: https://docs.turso.tech/api-reference/databases/usage.md

# Source: https://docs.turso.tech/api-reference/organizations/usage.md

# Source: https://docs.turso.tech/api-reference/databases/usage.md

# Retrieve Database Usage

> Fetch activity usage for a database in a given time period.

## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/databases/{databaseName}/usage
paths:
  path: /v1/organizations/{organizationSlug}/databases/{databaseName}/usage
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
      query:
        from:
          schema:
            - type: string
              description: >-
                The datetime to retrieve usage **from** in [ISO
                8601](https://en.wikipedia.org/wiki/ISO_8601) format. Defaults
                to the current calendar month if not provided. Example:
                `2023-01-01T00:00:00Z`
              format: date-time
        to:
          schema:
            - type: string
              description: >-
                The datetime to retrieve usage **to** in [ISO
                8601](https://en.wikipedia.org/wiki/ISO_8601) format. Defaults
                to the current calendar month if not provided. Example:
                `2023-02-01T00:00:00Z`
              format: date-time
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
                  - type: object
                    description: >-
                      The database usage object, containg the total and
                      individual instance usage for rows read and written, as
                      well as the total storage size (in bytes).
                    $ref: '#/components/schemas/DatabaseUsageOutput'
        examples:
          example:
            value:
              database:
                uuid: 0eb771dd-6906-11ee-8553-eaa7715aeaf2
                instances:
                  - uuid: cd831986-94e5-11ee-a6fe-7a52e1f7759a
                    usage:
                      rows_read: 0
                      rows_written: 0
                      storage_bytes: 4096
                      bytes_synced: 0
                  - uuid: 0be90471-6906-11ee-8553-eaa7715aeaf2
                    usage:
                      rows_read: 0
                      rows_written: 0
                      storage_bytes: 4096
                      bytes_synced: 0
                total:
                  rows_read: 0
                  rows_written: 0
                  storage_bytes: 8192
                  bytes_synced: 0
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
                    example: >-
                      invalid from parameter: parsing time "2023-12-12T00:00:00"
                      as "2006-01-02T15:04:05Z07:00": cannot parse "" as
                      "Z07:00"
        examples:
          example:
            value:
              error: >-
                invalid from parameter: parsing time "2023-12-12T00:00:00" as
                "2006-01-02T15:04:05Z07:00": cannot parse "" as "Z07:00"
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
  schemas:
    DatabaseUsageOutput:
      type: object
      properties:
        uuid:
          $ref: '#/components/schemas/Database/properties/DbId'
        instances:
          type: array
          description: The usage objects for instances of the current database.
          items:
            type: object
            properties:
              uuid:
                type: string
                description: The instance universal unique identifier (UUID).
                example: cd831986-94e5-11ee-a6fe-7a52e1f7759a
              usage:
                description: The usage for the current database instance.
                $ref: '#/components/schemas/DatabaseUsageObject'
          example:
            - uuid: cd831986-94e5-11ee-a6fe-7a52e1f7759a
              usage:
                rows_read: 0
                rows_written: 0
                storage_bytes: 4096
                bytes_synced: 0
            - uuid: 0be90471-6906-11ee-8553-eaa7715aeaf2
              usage:
                rows_read: 0
                rows_written: 0
                storage_bytes: 4096
                bytes_synced: 0
        total:
          description: The total usage for the database.
          $ref: '#/components/schemas/DatabaseUsageObject'
          example:
            rows_read: 0
            rows_written: 0
            storage_bytes: 8192
            bytes_synced: 0
    DatabaseUsageObject:
      type: object
      properties:
        rows_read:
          type: integer
          example: 0
          description: The total rows read in the time period.
        rows_written:
          type: integer
          example: 0
          description: The total rows written in the time period.
        storage_bytes:
          type: integer
          example: 0
          description: The total storage used.
        bytes_synced:
          type: integer
          example: 0
          description: The total bytes synced.

````