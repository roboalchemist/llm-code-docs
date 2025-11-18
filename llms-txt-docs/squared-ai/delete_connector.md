# Source: https://docs.squared.ai/api-reference/connectors/delete_connector.md

# Delete Connector

## OpenAPI

````yaml DELETE /api/v1/connectors/{id}
paths:
  path: /api/v1/connectors/{id}
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
              description: Unique ID of the connector
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: No content, indicating successful deletion
        examples: {}
        description: No content, indicating successful deletion
  deprecated: false
  type: path
components:
  schemas: {}

````