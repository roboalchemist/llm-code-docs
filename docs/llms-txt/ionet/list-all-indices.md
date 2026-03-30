# Source: https://io.net/docs/reference/rag/indices/list-all-indices.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Vector Indices

> List existing vector similarity search indices with pagination support.

Returns details about each index including:

* Name and table name
* Indexing method and parameters
* Size and row count
* Creation timestamp and last updated
* Performance statistics (if available)

The response can be filtered using the filter\_by parameter to narrow down results based on table name, index method, or other attributes.


## OpenAPI

````yaml openapi/rag-indices/list-all-indices.json get /api/r2r/v3/indices
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/indices:
    get:
      summary: List Vector Indices
      description: List existing vector similarity search indices with pagination support.
      operationId: list-all-indices
      parameters:
        - name: offset
          in: query
          description: Specifies the number of objects to skip. Defaults to 0. >=0
          schema:
            type: integer
            format: int32
            default: 0
        - name: limit
          in: query
          description: >-
            Specifies a limit on the number of objects to return, ranging
            between 1 and 100. Defaults to 100. >=1 <=1000
          schema:
            type: integer
            format: int32
            default: 100
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    results:
                      indices:
                        - index:
                            key: value
                    total_entries: 1
              schema:
                type: object
                properties:
                  results:
                    type: object
                    properties:
                      indices:
                        type: array
                        items:
                          type: object
                          properties:
                            index:
                              type: object
                              properties:
                                key:
                                  type: string
                                  example: value
                  total_entries:
                    type: integer
                    example: 1
                    default: 0
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