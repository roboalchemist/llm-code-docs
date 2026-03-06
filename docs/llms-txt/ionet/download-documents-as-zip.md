# Source: https://io.net/docs/reference/rag/documents/download-documents-as-zip.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Export multiple documents as zip

> Export multiple documents as a zip file. Documents can be filtered by IDs and/or date range.

The endpoint allows downloading:

* Specific documents by providing their IDs
* Documents within a date range
* All accessible documents if no filters are provided

Files are streamed as a zip archive to handle potentially large downloads efficiently.


## OpenAPI

````yaml openapi/rag-documents/download-documents-as-zip.json get /api/r2r/v3/documents/download_zip
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/documents/download_zip:
    get:
      tags:
        - R2R-compatible API
      summary: Reverse Proxy Auth
      operationId: reverse_proxy_auth_r2r_v3_documents_download_zip_get
      parameters:
        - name: token
          in: header
          required: false
          schema:
            type: string
            description: JWT token
            title: Token
          description: JWT token
        - name: Authorization
          in: header
          required: false
          schema:
            type: string
            description: io.net provided API Key
            title: Authorization
          description: io.net provided API Key
        - name: x-api-key
          in: header
          required: false
          schema:
            type: string
            description: API key set by an SDK client
            title: X-Api-Key
          description: API key set by an SDK client
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '404':
          description: Not found
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````