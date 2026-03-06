# Source: https://io.net/docs/reference/rag/documents/get-document-chunks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List document chunks

> Retrieves the text chunks that were generated from a document during ingestion.

Chunks represent semantic sections of the document and are used for retrieval and analysis. Users can only access chunks from documents they own or have access to through collections. Vector embeddings are only included if specifically requested. Results are returned in chunk sequence order, representing their position in the original document.


## OpenAPI

````yaml openapi/rag-documents/get-document-chunks.json get /api/r2r/v3/documents/{id}/chunks
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/documents/{id}/chunks:
    get:
      summary: List document chunks
      description: >-
        Retrieves the text chunks that were generated from a document during
        ingestion.
      operationId: get-document-chunks
      parameters:
        - name: id
          in: path
          description: The ID of the document to retrieve chunks for.
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
                      - id: id
                        document_id: document_id
                        owner_id: owner_id
                        collection_ids:
                          - collection_ids
                        text: text
                        metadata:
                          key: value
                        vector:
                          - 1.1
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