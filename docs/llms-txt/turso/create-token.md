# Source: https://docs.turso.tech/api-reference/groups/create-token.md

# Source: https://docs.turso.tech/api-reference/databases/create-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate Database Auth Token

> Generates an authorization token for the specified database.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X POST 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}/auth/tokens?expiration=2w&authorization=full-access' \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const token = await turso.databases.createToken("my-db", {
    expiration: "2w",
    authorization: "full-access",
  });
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
    "jwt": "TOKEN"
  }
  ```
</ResponseExample>


## OpenAPI

````yaml POST /v1/organizations/{organizationSlug}/databases/{databaseName}/auth/tokens
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
  /v1/organizations/{organizationSlug}/databases/{databaseName}/auth/tokens:
    post:
      summary: Generate Database Auth Token
      description: Generates an authorization token for the specified database.
      operationId: createDatabaseToken
      parameters:
        - $ref: '#/components/parameters/organizationSlug'
        - $ref: '#/components/parameters/databaseName'
        - name: expiration
          in: query
          schema:
            type: string
            default: never
          description: Expiration time for the token (e.g., 2w1d30m).
        - name: authorization
          in: query
          schema:
            type: string
            default: full-access
            enum:
              - full-access
              - read-only
          description: Authorization level for the token (full-access or read-only).
      requestBody:
        description: Additional context such as claims required for the token.
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateTokenInput'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  jwt:
                    type: string
                    description: The generated authorization token (JWT).
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
                    example: Invalid expiration format
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
    CreateTokenInput:
      type: object
      properties:
        permissions:
          type: object
          description: The permissions for the token.
          properties:
            read_attach:
              type: object
              description: Read `ATTACH` permission for the token.
              properties:
                databases:
                  type: array
                  items:
                    type: string
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