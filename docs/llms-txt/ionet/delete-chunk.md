# Source: https://io.net/docs/reference/rag/chunks/delete-chunk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Chunk

> Delete a specific chunk by ID.

Delete a specific chunk by ID. This permanently removes the chunk and its associated vector embeddings. The parent document remains unchanged. Users can only delete chunks they own unless they are superusers.


## OpenAPI

````yaml openapi/rag-chunks/delete-chunk.json delete /api/r2r/v3/chunks/{id}
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
    delete:
      summary: Delete Chunk
      description: Delete a specific chunk by ID.
      operationId: delete-chunk
      parameters:
        - name: id
          in: path
          description: ID of the chunk
          required: true
          schema:
            type: string
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    results:
                      success: true
              schema:
                type: object
                properties:
                  results:
                    type: object
                    properties:
                      success:
                        type: boolean
                        example: true
                        default: true
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