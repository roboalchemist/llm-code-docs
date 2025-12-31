# Source: https://docs.turso.tech/api-reference/databases/stats.md

# Retrieve Database Stats

> Fetch the top queries of a database, including the count of rows read and written.

## OpenAPI

````yaml GET /v1/organizations/{organizationSlug}/databases/{databaseName}/stats
paths:
  path: /v1/organizations/{organizationSlug}/databases/{databaseName}/stats
  method: get
  servers:
    - url: https://api.turso.tech
      description: Turso's Platform API
  request:
    security: []
    parameters:
      path:
        organizationSlug:
          schema:
            - type: string
              required: true
              description: The slug of the organization or user account.
        databaseName:
          schema:
            - type: string
              required: true
              description: The name of the database.
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              top_queries:
                allOf:
                  - type: array
                    description: >-
                      The top queries performed on the given database as well as
                      the total rows read and written.
                    nullable: true
                    items:
                      $ref: '#/components/schemas/DatabaseStatsOutput'
        examples:
          example:
            value:
              top_queries:
                - query: >-
                    SELECT COUNT(*), CustomerID FROM Orders GROUP BY CustomerID
                    HAVING COUNT(*) > 5;
                  rows_read: 123
                  rows_written: 4567
        description: Successful response
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message
                    example: >-
                      could not find database with name [databaseName]: record
                      not found
        examples:
          example:
            value:
              error: >-
                could not find database with name [databaseName]: record not
                found
        description: Database not found
  deprecated: false
  type: path
components:
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

````