# Source: https://docs.tavus.io/api-reference/documents/create-document.md

# Create Document

> Upload documents to your knowledge base for personas to reference during conversations

## OpenAPI

````yaml post /v2/documents
paths:
  path: /v2/documents
  method: post
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              document_url:
                allOf:
                  - type: string
                    description: The URL of the document to be processed
                    example: https://example.com/document.pdf
              document_name:
                allOf:
                  - type: string
                    description: >-
                      Optional name for the document. If not provided, a default
                      name will be generated.
                    example: Important Document
              callback_url:
                allOf:
                  - type: string
                    description: >-
                      Optional URL that will receive status updates about the
                      document processing
                    example: https://your-server.com/webhook
              properties:
                allOf:
                  - type: object
                    description: >-
                      Optional key-value pairs for additional document
                      properties
                    example:
                      department: sales
                      priority: high
              tags:
                allOf:
                  - type: array
                    description: Optional array of tags to categorize the document
                    items:
                      type: string
                    example:
                      - important
                      - meeting
            requiredProperties:
              - document_url
        examples:
          example:
            value:
              document_url: https://example.com/document.pdf
              document_name: Important Document
              callback_url: https://your-server.com/webhook
              properties:
                department: sales
                priority: high
              tags:
                - important
                - meeting
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              uuid:
                allOf:
                  - type: string
                    description: Unique identifier for the created document
                    example: d290f1ee-6c54-4b01-90e6-d701748f0851
              document_name:
                allOf:
                  - type: string
                    description: Name of the document
                    example: Important Document
              document_url:
                allOf:
                  - type: string
                    description: URL of the document
                    example: https://example.com/document.pdf
              status:
                allOf:
                  - type: string
                    description: Current status of the document processing
                    example: processing
              created_at:
                allOf:
                  - type: string
                    description: ISO 8601 timestamp of when the document was created
                    example: '2024-01-01T12:00:00Z'
              updated_at:
                allOf:
                  - type: string
                    description: ISO 8601 timestamp of when the document was last updated
                    example: '2024-01-01T12:00:00Z'
              callback_url:
                allOf:
                  - type: string
                    description: URL that will receive status updates
                    example: https://your-server.com/webhook
              tags:
                allOf:
                  - type: array
                    description: Array of document tags
                    items:
                      type: string
                    example:
                      - important
                      - meeting
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
              document_name: Important Document
              document_url: https://example.com/document.pdf
              status: processing
              created_at: '2024-01-01T12:00:00Z'
              updated_at: '2024-01-01T12:00:00Z'
              callback_url: https://your-server.com/webhook
              tags:
                - important
                - meeting
              properties:
                department: sales
                priority: high
        description: Document created successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message
                    example: 'Invalid request: document_url is required'
        examples:
          example:
            value:
              error: 'Invalid request: document_url is required'
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
  deprecated: false
  type: path
components:
  schemas: {}

````