# Source: https://docs.turso.tech/api-reference/groups/configuration.md

# Source: https://docs.turso.tech/api-reference/databases/configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve Database Configuration

> Retrieve an individual database configuration belonging to the organization or user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X GET 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}/configuration' \
    -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>


## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/databases/{databaseName}/configuration
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
    get:
      summary: Retrieve Database Configuration
      description: >-
        Retrieve an individual database configuration belonging to the
        organization or user.
      operationId: getDatabaseConfiguration
      parameters:
        - $ref: '#/components/parameters/organizationSlug'
        - $ref: '#/components/parameters/databaseName'
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