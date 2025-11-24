# Source: https://upstash.com/docs/api-reference/search/reset-password.md

# Reset Password

> This endpoint resets the regular and readonly tokens of a search index.

## OpenAPI

````yaml devops/developer-api/openapi.yml post /search/{id}/reset-password
paths:
  path: /search/{id}/reset-password
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
        description: Search index passwords reset successfully
  deprecated: false
  type: path
components:
  schemas: {}

````