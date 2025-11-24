# Source: https://upstash.com/docs/api-reference/search/rename-search-index.md

# Rename Search Index

> Renames a search index.

## OpenAPI

````yaml devops/developer-api/openapi.yml post /search/{id}/rename
paths:
  path: /search/{id}/rename
  method: post
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
              description: The ID of the search index
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    description: New name for the index
                    example: new-index-name
            required: true
            requiredProperties:
              - name
        examples:
          example:
            value:
              name: new-index-name
  response:
    '200':
      application/json:
        schemaArray:
          - type: string
            example: OK
        examples:
          example:
            value: OK
        description: Search index renamed successfully
  deprecated: false
  type: path
components:
  schemas: {}

````