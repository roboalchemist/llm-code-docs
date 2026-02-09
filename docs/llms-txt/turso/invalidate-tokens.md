# Source: https://docs.turso.tech/api-reference/groups/invalidate-tokens.md

# Source: https://docs.turso.tech/api-reference/databases/invalidate-tokens.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Invalidate All Database Auth Tokens

> Invalidates all authorization tokens for the specified database.

<Warning>
  A short downtime is required to complete the changes.
</Warning>

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}/auth/rotate' \
  -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const response = await turso.databases.rotateTokens("my-db");
  ```
</RequestExample>


## OpenAPI

````yaml POST /v1/organizations/{organizationSlug}/databases/{databaseName}/auth/rotate
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
  /v1/organizations/{organizationSlug}/databases/{databaseName}/auth/rotate:
    post:
      summary: Invalidate All Database Auth Tokens
      description: Invalidates all authorization tokens for the specified database.
      operationId: invalidateDatabaseTokens
      parameters:
        - $ref: '#/components/parameters/organizationSlug'
        - $ref: '#/components/parameters/databaseName'
      responses:
        '200':
          description: Successful response (No Content)
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