# Source: https://io.net/docs/reference/rag/indices/get-specific-index-details.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Vector Index Details

> Get detailed information about a specific vector index.

Returns comprehensive information about the index including:

* Configuration details (method, measure, parameters)
* Current size and row count
* Build progress (if still under construction)
* Performance statistics:
  * Average query time
  * Memory usage
  * Cache hit rates
  * Recent query patterns
* Maintenance information:
  * Last vacuum
  * Fragmentation level
  * Recommended optimizations


## OpenAPI

````yaml openapi/rag-indices/get-specific-index-details.json get /api/r2r/v3/indices/{table_name}/{index_name}
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/indices/{table_name}/{index_name}:
    get:
      summary: Get Vector Index Details
      description: Get detailed information about a specific vector index.
      operationId: get-specific-index-details
      parameters:
        - name: table_name
          in: path
          description: Name of the table where the index resides
          schema:
            type: string
          required: true
        - name: index_name
          in: path
          description: Name of the specific index
          schema:
            type: string
          required: true
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    results:
                      index:
                        key: value
              schema:
                type: object
                properties:
                  results:
                    type: object
                    properties:
                      index:
                        type: object
                        properties:
                          key:
                            type: string
                            example: value
        '404':
          description: '404'
          content:
            application/json:
              examples:
                Result:
                  value: {}
              schema:
                type: object
                properties: {}
        '422':
          description: '422'
          content:
            text/plain:
              examples:
                Result:
                  value: ''
      deprecated: false
components:
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````