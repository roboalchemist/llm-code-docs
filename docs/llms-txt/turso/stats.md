# Source: https://docs.turso.tech/api-reference/databases/stats.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve Database Stats

> Fetch the top queries of a database, including the count of rows read and written.

<RequestExample>
  ```bash cURL theme={null}
  curl -L -X GET 'https://api.turso.tech/v1/organizations/{organizationSlug}/databases/{databaseName}/stats' \
  -H 'Authorization: Bearer TOKEN'
  ```
</RequestExample>


## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/databases/{databaseName}/stats
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
  /v1/organizations/{organizationSlug}/databases/{databaseName}/stats:
    get:
      summary: Retrieve Database Stats
      description: >-
        Fetch the top queries of a database, including the count of rows read
        and written.
      operationId: getDatabaseStats
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
                  top_queries:
                    type: array
                    description: >-
                      The top queries performed on the given database as well as
                      the total rows read and written.
                    nullable: true
                    items:
                      $ref: '#/components/schemas/DatabaseStatsOutput'
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
    DatabaseStatsOutput:
      type: object
      properties:
        query:
          type: string
          description: A string representing the SQL query executed.
          example: >-
            SELECT COUNT(*), CustomerID FROM Orders GROUP BY CustomerID HAVING
            COUNT(*) > 5;
        rows_read:
          type: integer
          description: >-
            An integer indicating the number of rows read by the query, which
            reflects the volume of data the query processed from the database.
          example: 123
        rows_written:
          type: integer
          description: >-
            An integer indicating the number of rows written (inserted, updated,
            or deleted) by the query, which reflects the impact of the query on
            the database data.
          example: 4567
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