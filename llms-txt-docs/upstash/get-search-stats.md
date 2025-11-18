# Source: https://upstash.com/docs/api-reference/search/get-search-stats.md

# Get Search Stats

> Get search statistics for all the search indices associated with the authenticated user

## OpenAPI

````yaml devops/developer-api/openapi.yml get /search/stats
paths:
  path: /search/stats
  method: get
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              record_count:
                allOf:
                  - type: integer
                    description: Total number of indexed records across all indexes
                    example: 10
              request:
                allOf:
                  - type: integer
                    description: Total API requests count across all indexes
                    example: 10
              bandwidth:
                allOf:
                  - type: integer
                    description: Total bandwidth usage in bytes across all indexes
                    example: 750
              storage:
                allOf:
                  - type: integer
                    description: Total storage usage in bytes across all indexes
                    example: 950
              billing:
                allOf:
                  - type: number
                    format: float
                    description: Current billing amount across all indexes
                    example: 0.001
              rerank_count:
                allOf:
                  - type: integer
                    description: Total reranking operations count across all indexes
                    example: 0
            refIdentifier: '#/components/schemas/GlobalStats'
        examples:
          example:
            value:
              record_count: 10
              request: 10
              bandwidth: 750
              storage: 950
              billing: 0.001
              rerank_count: 0
        description: Statistics for the search indices retrieved successfully
  deprecated: false
  type: path
components:
  schemas: {}

````