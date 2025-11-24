# Source: https://docs.infera.org/api-reference/endpoint/get-active-node-count.md

# Get Active Node Count

## OpenAPI

````yaml get /active_node_count
paths:
  path: /active_node_count
  method: get
  servers:
    - url: https://api.infera.org/
      description: Infera production servers
  request:
    security:
      - title: APIKeyHeader
        parameters:
          query: {}
          header:
            api_key:
              type: apiKey
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: any
        examples:
          example:
            value: <any>
        description: Successful Response
  deprecated: false
  type: path
components:
  schemas: {}

````