# Source: https://docs.tavus.io/api-reference/documents/patch-document.md

# Update Document

> Update a specific document's metadata

## OpenAPI

````yaml patch /v2/documents/{document_id}
paths:
  path: /v2/documents/{document_id}
  method: patch
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
              description: The unique identifier of the document to update
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              document_name:
                allOf:
                  - type: string
                    description: New name for the document
                    example: Updated Document Name
              tags:
                allOf:
                  - type: array
                    description: >-
                      New array of tags for the document. This will overwrite
                      the existing tags for the document.
                    items:
                      type: string
                    example:
                      - important
                      - meeting
                      - updated
        examples:
          example:
            value:
              document_name: Updated Document Name
              tags:
                - important
                - meeting
                - updated
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              uuid:
                allOf:
                  - type: string
                    description: Unique identifier for the document
                    example: d290f1ee-6c54-4b01-90e6-d701748f0851
              document_name:
                allOf:
                  - type: string
                    description: Updated name of the document
                    example: Updated Document Name
              document_url:
                allOf:
                  - type: string
                    description: URL of the document
                    example: https://example.com/document.pdf
              status:
                allOf:
                  - type: string
                    description: Current status of the document processing
                    example: ready
              created_at:
                allOf:
                  - type: string
                    description: ISO 8601 timestamp of when the document was created
                    example: '2024-01-01T12:00:00Z'
              updated_at:
                allOf:
                  - type: string
                    description: ISO 8601 timestamp of when the document was last updated
                    example: '2024-01-01T13:00:00Z'
              callback_url:
                allOf:
                  - type: string
                    description: URL that receives status updates
                    example: https://your-server.com/webhook
              tags:
                allOf:
                  - type: array
                    description: Updated array of document tags
                    items:
                      type: string
                    example:
                      - important
                      - meeting
                      - updated
              properties:
                allOf:
                  - type: object
                    description: Additional document properties
                    example:
                      department: sales
                      priority: high
        examples:
          example:
            value:
              uuid: d290f1ee-6c54-4b01-90e6-d701748f0851
              document_name: Updated Document Name
              document_url: https://example.com/document.pdf
              status: ready
              created_at: '2024-01-01T12:00:00Z'
              updated_at: '2024-01-01T13:00:00Z'
              callback_url: https://your-server.com/webhook
              tags:
                - important
                - meeting
                - updated
              properties:
                department: sales
                priority: high
        description: Document updated successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message
                    example: 'Invalid request: document_name must be a string'
        examples:
          example:
            value:
              error: 'Invalid request: document_name must be a string'
        description: Bad Request
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