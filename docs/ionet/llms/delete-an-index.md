# Source: https://io.net/docs/reference/rag/indices/delete-an-index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Vector Index

> Delete an existing vector similarity search index.

This endpoint removes the specified index from the database. Important considerations:

* Deletion is permanent and cannot be undone
* Underlying vector data remains intact
* Queries will fall back to sequential scan
* Running queries during deletion may be slower
* Use run\_with\_orchestration=True for large indices to prevent timeouts
* Consider index dependencies before deletion

The operation returns immediately but cleanup may continue in background.


## OpenAPI

````yaml openapi/rag-indices/delete-an-index.json delete /api/r2r/v3/indices/{table_name}/{index_name}
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
    delete:
      summary: Delete Vector Index
      description: Delete an existing vector similarity search index.
      operationId: delete-an-index
      parameters:
        - name: table_name
          in: path
          description: >-
            The table of vector embeddings to delete (e.g. vectors, entity,
            document_collections)
          schema:
            type: string
            enum:
              - chunks
              - documents_entities
              - graphs_entities
              - graphs_communities
          required: true
        - name: index_name
          in: path
          description: The name of the index to delete
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
                      message: message
              schema:
                type: object
                properties:
                  results:
                    type: object
                    properties:
                      message:
                        type: string
                        example: message
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