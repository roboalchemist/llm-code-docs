# Source: https://io.net/docs/reference/rag/documents/download-original-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Download document content

> Downloads the original file content of a document.

For uploaded files, returns the original file with its proper MIME type. For text-only documents, returns the content as plain text.

Users can only download documents they own or have access to through collections.


## OpenAPI

````yaml openapi/rag-documents/download-original-file.json get /api/r2r/v3/documents/{id}/download
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/documents/{id}/download:
    get:
      summary: Download document content
      description: Downloads the original file content of a document.
      operationId: download-original-file
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