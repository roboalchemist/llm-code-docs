# Source: https://docs.tavus.io/api-reference/documents/delete-document.md

# Delete Document

> Delete a specific document

## OpenAPI

````yaml delete /v2/documents/{document_id}
paths:
  path: /v2/documents/{document_id}
  method: delete
  servers:
    - url: https://tavusapi.com
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
          cookie: {}
    parameters:
      path:
        document_id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the document to delete
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Document deleted successfully
        examples: {}
        description: Document deleted successfully
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message
                    example: Invalid or missing authentication
        examples:
          example:
            value:
              error: Invalid or missing authentication
        description: Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message
                    example: Access denied
        examples:
          example:
            value:
              error: Access denied
        description: Forbidden
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message
                    example: Document not found
        examples:
          example:
            value:
              error: Document not found
        description: Not Found
  deprecated: false
  type: path
components:
  schemas: {}

````