# Source: https://docs.turso.tech/cli/org/create.md

# Source: https://docs.turso.tech/cli/group/tokens/create.md

# Source: https://docs.turso.tech/cli/group/create.md

# Source: https://docs.turso.tech/cli/db/tokens/create.md

# Source: https://docs.turso.tech/cli/db/create.md

# Source: https://docs.turso.tech/api-reference/tokens/create.md

# Source: https://docs.turso.tech/api-reference/organizations/invites/create.md

# Source: https://docs.turso.tech/api-reference/groups/create.md

# Source: https://docs.turso.tech/api-reference/databases/create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Database

> Creates a new database in a group for the organization or user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases' \
    -H 'Authorization: Bearer TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "new-database",
        "group": "default"
    }'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const database = await turso.databases.create("new-database", {
    group: "default",
  });
  ```
</RequestExample>


## OpenAPI

````yaml POST /v1/organizations/{organizationSlug}/databases
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
  /v1/organizations/{organizationSlug}/databases:
    post:
      summary: Create Database
      description: Creates a new database in a group for the organization or user.
      operationId: createDatabase
      parameters:
        - $ref: '#/components/parameters/organizationSlug'
      requestBody:
        description: Database data to create a new database
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateDatabaseInput'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  database:
                    $ref: '#/components/schemas/CreateDatabaseOutput'
                    description: The newly created database
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
                    example: group not found
        '409':
          description: Conflict
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message
                    example: database with name [databaseName] already exists
components:
  parameters:
    organizationSlug:
      in: path
      name: organizationSlug
      required: true
      schema:
        type: string
      description: The slug of the organization or user account.
  schemas:
    CreateDatabaseInput:
      type: object
      properties:
        name:
          type: string
          description: >-
            The name of the new database. Must contain only lowercase letters,
            numbers, dashes. No longer than 64 characters.
        group:
          type: string
          description: >-
            The name of the group where the database should be created. **The
            group must already exist.**
        seed:
          type: object
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
                The name of the existing database when `database` is used as a
                seed type.
              example: my-db
            timestamp:
              type: string
              description: >-
                A formatted [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
                recovery point to create a database from. This must be within
                the last 24 hours, or 30 days on the scaler plan.
              example: '2023-12-20T09:46:08Z'
        size_limit:
          type: string
          description: >-
            The maximum size of the database in bytes. Values with units are
            also accepted, e.g. 1mb, 256mb, 1gb.
      required:
        - name
        - group
    CreateDatabaseOutput:
      type: object
      properties:
        DbId: a0e7e55a-5eb4-49ec-8e29-e946e241d99f
        Hostname: b6d47bb5-e1cb-4e26-b40a-dd263ec0914a
        Name: ba7319ab-30c6-4763-9d34-517e949e55dc

````