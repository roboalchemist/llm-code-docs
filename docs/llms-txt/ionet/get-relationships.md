# Source: https://io.net/docs/reference/rag/documents/get-relationships.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Relationships

> View semantic or knowledge graph relationships from extracted content.



## OpenAPI

````yaml openapi/rag-documents/get-relationships.json get /api/r2r/v3/documents/{id}/relationships
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/documents/{id}/relationships:
    get:
      summary: Get Relationships
      description: View semantic or knowledge graph relationships from extracted content.
      operationId: get-relationships
      parameters:
        - name: id
          in: path
          description: Document ID
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
                  value: {}
              schema:
                type: object
                properties: {}
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