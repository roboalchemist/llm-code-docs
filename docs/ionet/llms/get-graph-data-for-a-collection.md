# Source: https://io.net/docs/reference/rag/graphs/get-graph-data-for-a-collection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve graph details

> Retrieves detailed information about a specific graph by ID.



## OpenAPI

````yaml openapi/rag-graphs/get-graph-data-for-a-collection.json get /api/r2r/v3/graphs/{collection_id}
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/graphs/{collection_id}:
    get:
      summary: Retrieve graph details
      description: Retrieves detailed information about a specific graph by ID.
      operationId: get-graph-data-for-a-collection
      parameters:
        - name: collection_id
          in: path
          description: ID of the collection to inspect
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
                      id: id
                      collection_id: collection_id
                      name: name
                      status: status
                      created_at: '2024-01-15T09:30:00Z'
                      updated_at: '2024-01-15T09:30:00Z'
                      document_ids:
                        - document_ids
                      description: description
              schema:
                type: object
                properties:
                  results:
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