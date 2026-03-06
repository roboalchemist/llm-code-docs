# Source: https://io.net/docs/reference/rag/chunks/get-chunk-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve Chunk

> Get a specific chunk by its ID.

Returns the chunk’s content, metadata, and associated document/collection information. Users can only retrieve chunks they own or have access to through collections.


## OpenAPI

````yaml openapi/rag-chunks/get-chunk-by-id.json get /api/r2r/v3/chunks/{id}
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/chunks/{id}:
    get:
      summary: Retrieve Chunk
      description: Get a specific chunk by its ID.
      operationId: get-chunk-by-id
      parameters:
        - name: id
          in: path
          description: ID of the chunk
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
                      document_id: document_id
                      owner_id: owner_id
                      collection_ids:
                        - collection_ids
                      text: text
                      metadata:
                        key: value
                      vector:
                        - 1.1
              schema:
                type: object
                properties:
                  results:
                    type: object
                    properties:
                      id:
                        type: string
                        example: id
                      document_id:
                        type: string
                        example: document_id
                      owner_id:
                        type: string
                        example: owner_id
                      collection_ids:
                        type: array
                        items:
                          type: string
                          example: collection_ids
                      text:
                        type: string
                        example: text
                      metadata:
                        type: object
                        properties:
                          key:
                            type: string
                            example: value
                      vector:
                        type: array
                        items:
                          type: number
                          example: 1.1
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