# Source: https://docs.infera.org/api-reference/endpoint/get-active-node-count.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Active Node Count



## OpenAPI

````yaml get /active_node_count
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.infera.org/
    description: Infera production servers
security: []
paths:
  /active_node_count:
    get:
      summary: Get Active Node Count
      operationId: get_active_node_count_active_node_count_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
      security:
        - APIKeyHeader: []
components:
  securitySchemes:
    APIKeyHeader:
      type: apiKey
      in: header
      name: api_key

````