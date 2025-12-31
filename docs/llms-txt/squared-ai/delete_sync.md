# Source: https://docs.squared.ai/api-reference/syncs/delete_sync.md

# Delete Sync

## OpenAPI

````yaml DELETE /api/v1/syncs/{id}
paths:
  path: /api/v1/syncs/{id}
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
            - type: string
              required: true
              description: The ID of the sync operation to delete
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: No content, indicating the sync operation was successfully deleted
        examples: {}
        description: No content, indicating the sync operation was successfully deleted
  deprecated: false
  type: path
components:
  schemas: {}

````