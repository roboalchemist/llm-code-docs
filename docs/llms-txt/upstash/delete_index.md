# Source: https://upstash.com/docs/devops/developer-api/vector/delete_index.md

# Delete Index

> This endpoint deletes an index.

## OpenAPI

````yaml devops/developer-api/openapi.yml delete /vector/index/{id}
paths:
  path: /vector/index/{id}
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
              description: The unique ID of the index to be deleted
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
        description: Index deleted successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/vector/delete_index
components:
  schemas: {}

````