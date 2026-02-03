# Source: https://docs.turso.tech/api-reference/databases/retrieve-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve Database Instance

> Return the individual database instance by name.

<RequestExample>
  ```bash cURL theme={null}
  curl -L https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}/instances/{instanceName} \
    -H 'Authorization: Bearer TOKEN'
  ```

  ```ts Node.js theme={null}
  import { createClient } from "@tursodatabase/api";

  const turso = createClient({
    org: "...",
    token: "",
  });

  const instance = await turso.databases.retrieveInstance(
    "my-db",
    "instanceName",
  );
  ```
</RequestExample>


## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/databases/{databaseName}/instances/{instanceName}
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
  /v1/organizations/{organizationSlug}/databases/{databaseName}/instances/{instanceName}:
    get:
      summary: Retrieve Database Instance
      description: Return the individual database instance by name.
      operationId: getDatabaseInstance
      parameters:
        - $ref: '#/components/parameters/organizationSlug'
        - $ref: '#/components/parameters/databaseName'
        - $ref: '#/components/parameters/instanceName'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  instance:
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
    instanceName:
      name: instanceName
      in: path
      required: true
      schema:
        type: string
      description: The name of the instance (location code).
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