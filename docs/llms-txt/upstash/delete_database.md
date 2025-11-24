# Source: https://upstash.com/docs/devops/developer-api/redis/delete_database.md

# Delete Database

> This endpoint deletes a database.

## OpenAPI

````yaml devops/developer-api/openapi.yml delete /redis/database/{id}
paths:
  path: /redis/database/{id}
  method: delete
  servers:
    - url: https://api.upstash.com/v2
  request:
    security:
      - title: basicAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: basic
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: The ID of the database to be deleted
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: string
            example: OK
        examples:
          example:
            value: OK
        description: OK
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/redis/delete_database
components:
  schemas: {}

````