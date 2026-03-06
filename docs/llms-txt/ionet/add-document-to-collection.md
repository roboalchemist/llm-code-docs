# Source: https://io.net/docs/reference/rag/collections/add-document-to-collection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add document to collection

> Add a document to a collection.



## OpenAPI

````yaml openapi/rag-collections/add-document-to-collection.json post /api/r2r/v3/collections/{id}/documents/{document_id}
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/collections/{id}/documents/{document_id}:
    post:
      summary: Add document to collection
      description: Add a document to a collection.
      operationId: add-document-to-collection
      parameters:
        - name: id
          in: path
          description: Collection ID
          schema:
            type: string
          required: true
        - name: document_id
          in: path
          description: Document ID to add
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