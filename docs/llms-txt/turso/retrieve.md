# Source: https://docs.turso.tech/api-reference/organizations/retrieve.md

# Source: https://docs.turso.tech/api-reference/organizations/members/retrieve.md

# Source: https://docs.turso.tech/api-reference/groups/retrieve.md

# Source: https://docs.turso.tech/api-reference/databases/retrieve.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve Database

> Returns a database belonging to the organization or user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}' \
  -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const database = await turso.databases.retrieve("my-db");
  ```
</RequestExample>


## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/databases/{databaseName}
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
  /v1/organizations/{organizationSlug}/databases/{databaseName}:
    get:
      summary: Retrieve Database
      description: Returns a database belonging to the organization or user.
      operationId: getDatabase
      parameters:
        - $ref: '#/components/parameters/organizationSlug'
        - $ref: '#/components/parameters/databaseName'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  database:
                    $ref: '#/components/schemas/Database'
        '404':
          $ref: '#/components/responses/DatabaseNotFoundResponse'
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
  responses:
    DatabaseNotFoundResponse:
      description: Database not found
      content:
        application/json:
          schema:
            type: object
            properties:
              error:
                type: string
                description: The error message
                example: >-
                  could not find database with name [databaseName]: record not
                  found

````