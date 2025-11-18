# Source: https://docs.squared.ai/api-reference/models/delete-model.md

# Delete Model

## OpenAPI

````yaml DELETE /api/v1/models/{id}
paths:
  path: /api/v1/models/{id}
  method: delete
  servers:
    - url: https://api.squared.ai
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: integer
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Model deleted
        examples: {}
        description: Model deleted
  deprecated: false
  type: path
components:
  schemas: {}

````