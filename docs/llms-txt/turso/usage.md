# Source: https://docs.turso.tech/sync/usage.md

# Source: https://docs.turso.tech/api-reference/organizations/usage.md

# Source: https://docs.turso.tech/api-reference/databases/usage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve Database Usage

> Fetch activity usage for a database in a given time period.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X GET 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}/usage?from=2023-01-01T00:00:00Z&to=2023-02-01T00:00:00Z' \
  -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const usageStatsWithDate = await turso.databases.usage("my-db");

  const usageStatsWithDate = await turso.databases.usage("my-db", {
    from: new Date("2023-01-01"),
    to: new Date("2023-02-01"),
  });

  const usageStatsWithString = await turso.databases.usage("my-db", {
    from: "2023-01-01T00:00:00Z",
    to: "2023-02-01T00:00:00Z",
  });
  ```
</RequestExample>


## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/databases/{databaseName}/usage
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
  /v1/organizations/{organizationSlug}/databases/{databaseName}/usage:
    get:
      summary: Retrieve Database Usage
      description: Fetch activity usage for a database in a given time period.
      operationId: getDatabaseUsage
      parameters:
        - $ref: '#/components/parameters/organizationSlug'
        - $ref: '#/components/parameters/databaseName'
        - name: from
          in: query
          schema:
            type: string
            format: date-time
          description: >-
            The datetime to retrieve usage **from** in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format. Defaults to
            the current calendar month if not provided. Example:
            `2023-01-01T00:00:00Z`
        - name: to
          in: query
          schema:
            type: string
            format: date-time
          description: >-
            The datetime to retrieve usage **to** in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format. Defaults to
            the current calendar month if not provided. Example:
            `2023-02-01T00:00:00Z`
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  database:
                    $ref: '#/components/schemas/DatabaseUsageOutput'
                    type: object
                    description: >-
                      The database usage object, containg the total and
                      individual instance usage for rows read and written, as
                      well as the total storage size (in bytes).
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message
                    example: >-
                      invalid from parameter: parsing time "2023-12-12T00:00:00"
                      as "2006-01-02T15:04:05Z07:00": cannot parse "" as
                      "Z07:00"
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
    DatabaseUsageOutput:
      type: object
      properties:
        uuid: cfde0676-8e08-493d-b2c2-f7ee775a8591
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
                $ref: '#/components/schemas/DatabaseUsageObject'
                description: The usage for the current database instance.
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
          $ref: '#/components/schemas/DatabaseUsageObject'
          description: The total usage for the database.
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