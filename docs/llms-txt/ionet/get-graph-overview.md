# Source: https://io.net/docs/reference/rag/graphs/get-graph-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get graph overview

> Returns a paginated list of graphs the authenticated user has access to.

Results can be filtered by providing specific graph IDs. Regular users will only see graphs they own or have access to. Superusers can see all graphs. The graphs are returned in order of last modification, with most recent first.


## OpenAPI

````yaml openapi/rag-graphs/get-graph-overview.json get /api/r2r/v3/graphs
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/graphs:
    get:
      summary: Get graph overview
      description: Returns a paginated list of graphs the authenticated user has access to.
      operationId: get-graph-overview
      parameters:
        - name: collection_ids
          in: query
          description: >-
            A list of graph IDs to retrieve. If not provided, all graphs will be
            returned.
          schema:
            type: string
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
                      - id: id
                        collection_id: collection_id
                        name: name
                        status: status
                        created_at: '2024-01-15T09:30:00Z'
                        updated_at: '2024-01-15T09:30:00Z'
                        document_ids:
                          - document_ids
                        description: description
                    total_entries: 1
              schema:
                type: object
                properties:
                  results:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          example: id
                        collection_id:
                          type: string
                          example: collection_id
                        name:
                          type: string
                          example: name
                        status:
                          type: string
                          example: status
                        created_at:
                          type: string
                          example: '2024-01-15T09:30:00Z'
                        updated_at:
                          type: string
                          example: '2024-01-15T09:30:00Z'
                        document_ids:
                          type: array
                          items:
                            type: string
                            example: document_ids
                        description:
                          type: string
                          example: description
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