# Source: https://io.net/docs/reference/rag/chunks/list-chunks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Chunks

> List chunks with pagination support.

Returns a paginated list of chunks that the user has access to. Results can be filtered and sorted based on various parameters. Vector embeddings are only included if specifically requested. Regular users can only list chunks they own or have access to through collections. Superusers can list all chunks in the system.


## OpenAPI

````yaml openapi/rag-chunks/list-chunks.json get /api/r2r/v3/chunks
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/chunks:
    get:
      summary: List Chunks
      description: List chunks with pagination support.
      operationId: list-chunks
      parameters:
        - name: metadata_filter
          in: query
          description: Filter by metadata
          schema:
            type: string
        - name: include_vectors
          in: query
          description: Include vector data in response
          schema:
            type: boolean
            default: false
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