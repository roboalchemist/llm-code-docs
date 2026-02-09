# Source: https://docs.infera.org/api-reference/endpoint/network-stats.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Network Stats



## OpenAPI

````yaml get /network_stats
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.infera.org/
    description: Infera production servers
security: []
paths:
  /network_stats:
    get:
      summary: Network Stats
      operationId: network_stats_network_stats_get
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