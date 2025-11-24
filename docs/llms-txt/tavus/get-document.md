# Source: https://docs.tavus.io/api-reference/documents/get-document.md

# Get Document

> Retrieve a specific document by ID

## OpenAPI

````yaml get /v2/documents/{document_id}
paths:
  path: /v2/documents/{document_id}
  method: get
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
              description: The unique identifier of the document to retrieve
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - lang: curl
        source: >
          curl
          https://tavusapi.com/v2/documents/d290f1ee-6c54-4b01-90e6-d701748f0851
          \
            -H "x-api-key: YOUR_API_KEY"
      - lang: Python
        source: |
          import requests

          headers = {
              "x-api-key": "YOUR_API_KEY"
          }

          response = requests.get(
              "https://tavusapi.com/v2/documents/d290f1ee-6c54-4b01-90e6-d701748f0851",
              headers=headers
          )
      - lang: JavaScript
        source: |
          const response = await fetch(
            "https://tavusapi.com/v2/documents/d290f1ee-6c54-4b01-90e6-d701748f0851",
            {
              headers: {
                "x-api-key": "YOUR_API_KEY"
              }
            }
          );
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
                    example: '2024-01-01T12:05:00Z'
              callback_url:
                allOf:
                  - type: string
                    description: URL that receives status updates
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
              status: ready
              created_at: '2024-01-01T12:00:00Z'
              updated_at: '2024-01-01T12:05:00Z'
              callback_url: https://your-server.com/webhook
              tags:
                - important
                - meeting
              properties:
                department: sales
                priority: high
        description: Document details
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