# Source: https://docs.turso.tech/api-reference/databases/list-instances.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# List Database Instances

> Returns a list of instances of a database. Instances are the individual primary or replica databases in each region defined by the group.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}/instances \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const instances = await turso.databases.listInstances("my-db");
  ```
</RequestExample>


## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/databases/{databaseName}/instances
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
  /v1/organizations/{organizationSlug}/databases/{databaseName}/instances:
    get:
      summary: List Database Instances
      description: >-
        Returns a list of instances of a database. Instances are the individual
        primary or replica databases in each region defined by the group.
      operationId: listDatabaseInstances
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
                  instances:
                    type: array
                    items:
                      $ref: '#/components/schemas/Instance'
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
    Instance:
      type: object
      properties:
        uuid:
          type: string
          description: The instance universal unique identifier (UUID).
          example: 0be90471-6906-11ee-8553-eaa7715aeaf2
        name:
          type: string
          description: The name of the instance (location code).
          example: lhr
        type:
          type: string
          description: The type of database instance this, will be `primary` or `replica`.
          enum:
            - primary
            - replica
          example: primary
        region:
          type: string
          description: The location code for the region this instance is located.
          example: lhr
        hostname:
          type: string
          description: >-
            The DNS hostname used for client libSQL and HTTP connections
            (specific to this instance only).
          example: '[databaseName]-[organizationSlug].turso.io'

````