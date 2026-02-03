# Source: https://docs.turso.tech/api-reference/groups/update-configuration.md

# Source: https://docs.turso.tech/api-reference/databases/update-configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Database Configuration

> Update a database configuration belonging to the organization or user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X PATCH 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}/configuration' \
    -H 'Authorization: Bearer TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{
        "size_limit": "500mb",
        "delete_protection": true,
        "block_reads": false,
        "block_writes": false
    }'
  ```
</RequestExample>


## OpenAPI

````yaml PATCH /v1/organizations/{organizationSlug}/databases/{databaseName}/configuration
openapi: 3.0.1
info:
  title: Turso Platform API
  description: API description here
  license:
    name: MIT
  version: 0.1.0
servers:
  - url: https://api.turso.tech
    description: Turso's Platform API
security: []
paths:
  /v1/organizations/{organizationSlug}/databases/{databaseName}/configuration:
    patch:
      summary: Update Database Configuration
      description: Update a database configuration belonging to the organization or user.
      operationId: updateDatabaseConfiguration
      parameters:
        - $ref: '#/components/parameters/organizationSlug'
        - $ref: '#/components/parameters/databaseName'
      requestBody:
        description: The configuration to be applied to the chosen database.
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DatabaseConfigurationInput'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DatabaseConfigurationResponse'
components:
  parameters:
    organizationSlug:
      in: path
      name: organizationSlug
      required: true
      schema:
        type: string
      description: The slug of the organization or user account.
    databaseName:
      name: databaseName
      in: path
      required: true
      schema:
        type: string
      description: The name of the database.
  schemas:
    DatabaseConfigurationInput:
      type: object
      properties:
        size_limit:
          type: string
          description: >-
            The maximum size of the database in bytes. Values with units are
            also accepted, e.g. 1mb, 256mb, 1gb.
        allow_attach:
          type: boolean
          description: Allow or disallow attaching databases to the current database.
          deprecated: true
        block_reads:
          type: boolean
          description: Block all database reads.
          example: false
        block_writes:
          type: boolean
          description: Block all database writes.
          example: false
        delete_protection:
          type: boolean
          description: Prevent the database from being deleted.
          example: true
    DatabaseConfigurationResponse:
      type: object
      properties:
        size_limit:
          type: string
          description: >-
            The maximum size of the database in bytes. Values with units are
            also accepted, e.g. 1mb, 256mb, 1gb.
          example: '10000'
        allow_attach:
          type: boolean
          description: Allow or disallow attaching databases to the current database.
          example: true
          deprecated: true
        block_reads:
          type: boolean
          description: The current status for blocked reads.
          example: false
        block_writes:
          type: boolean
          description: The current status for blocked writes.
          example: false
        delete_protection:
          type: boolean
          description: Prevent the database from being deleted.
          example: true

````