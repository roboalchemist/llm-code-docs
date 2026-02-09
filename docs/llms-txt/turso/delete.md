# Source: https://docs.turso.tech/api-reference/organizations/invites/delete.md

# Source: https://docs.turso.tech/api-reference/groups/delete.md

# Source: https://docs.turso.tech/api-reference/databases/delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Database

> Delete a database belonging to the organization or user.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X DELETE 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}' \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const database = await turso.databases.delete("my-db");
  ```
</RequestExample>


## OpenAPI

````yaml DELETE /v1/organizations/{organizationSlug}/databases/{databaseName}
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
    delete:
      summary: Delete Database
      description: Delete a database belonging to the organization or user.
      operationId: deleteDatabase
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
                    type: string
                    description: The name of the database that was deleted.
                    example: my-db
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