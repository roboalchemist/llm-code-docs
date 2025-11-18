# Source: https://upstash.com/docs/api-reference/search/delete-search-index.md

# Delete Search Index

> Permanently deletes a search index and all its data

## OpenAPI

````yaml devops/developer-api/openapi.yml delete /search/{id}
paths:
  path: /search/{id}
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
              description: The unique ID of the search index to be deleted
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
        description: Search Index Deleted Successfully
  deprecated: false
  type: path
components:
  schemas: {}

````