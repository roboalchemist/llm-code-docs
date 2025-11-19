# Source: https://docs.turso.tech/api-reference/organizations/retrieve.md

# Source: https://docs.turso.tech/api-reference/organizations/members/retrieve.md

# Source: https://docs.turso.tech/api-reference/groups/retrieve.md

# Source: https://docs.turso.tech/api-reference/databases/retrieve.md

# Retrieve Database

> Returns a database belonging to the organization or user.

## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/databases/{databaseName}
paths:
  path: /v1/organizations/{organizationSlug}/databases/{databaseName}
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
              database:
                allOf:
                  - $ref: '#/components/schemas/Database'
        examples:
          example:
            value:
              database:
                Name: my-db
                DbId: 0eb771dd-6906-11ee-8553-eaa7715aeaf2
                Hostname: '[databaseName]-[organizationSlug].turso.io'
                block_reads: false
                block_writes: false
                regions:
                  - lhr
                  - bos
                  - nrt
                primaryRegion: lhr
                group: default
                delete_protection: false
                parent:
                  id: <string>
                  name: <string>
                  branched_at: '2025-04-15T13:14:34.468213117Z'
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
  schemas:
    Database:
      type: object
      properties:
        Name:
          type: string
          description: The database name, **unique** across your organization.
          example: my-db
        DbId:
          type: string
          description: The database universal unique identifier (UUID).
          example: 0eb771dd-6906-11ee-8553-eaa7715aeaf2
        Hostname:
          type: string
          description: The DNS hostname used for client libSQL and HTTP connections.
          example: '[databaseName]-[organizationSlug].turso.io'
        block_reads:
          type: boolean
          description: The current status for blocked reads.
          example: false
        block_writes:
          type: boolean
          description: The current status for blocked writes.
          example: false
        regions:
          type: array
          items:
            type: string
          description: A list of regions for the group the database belongs to.
          example:
            - lhr
            - bos
            - nrt
          deprecated: true
        primaryRegion:
          type: string
          description: The primary region location code the group the database belongs to.
          example: lhr
        group:
          type: string
          description: The name of the group the database belongs to.
          example: default
        delete_protection:
          type: boolean
          description: >-
            The current status for delete protection. If enabled, the database
            cannot be deleted.
          example: false
        parent:
          type: object
          nullable: true
          properties:
            id:
              type: string
              description: The parent database identifier.
            name:
              type: string
              description: The name of the parent database.
            branched_at:
              type: string
              format: date-time
              description: The timestamp when the database was branched from the parent.
              example: '2025-04-15T13:14:34.468213117Z'

````