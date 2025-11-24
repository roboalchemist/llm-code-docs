# Source: https://docs.tavus.io/api-reference/documents/get-documents.md

# List Documents

> Retrieve a list of documents with optional filtering and pagination

## OpenAPI

````yaml get /v2/documents
paths:
  path: /v2/documents
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
      path: {}
      query:
        limit:
          schema:
            - type: integer
              description: 'Number of documents to return per page (default: 10)'
        page:
          schema:
            - type: integer
              description: 'Page number for pagination (0-based, default: 0)'
        sort:
          schema:
            - type: enum<string>
              enum:
                - ascending
                - descending
              description: 'Sort direction for the results (default: ascending)'
        status:
          schema:
            - type: string
              description: Filter documents by status
        name_or_uuid:
          schema:
            - type: string
              description: Search for documents by name or UUID
        tags:
          schema:
            - type: string
              description: Comma-separated list of tags to filter by
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        uuid:
                          type: string
                          description: Unique identifier for the document
                          example: d290f1ee-6c54-4b01-90e6-d701748f0851
                        document_name:
                          type: string
                          description: Name of the document
                          example: Important Document
                        document_url:
                          type: string
                          description: URL of the document
                          example: https://example.com/document.pdf
                        status:
                          type: string
                          description: Current status of the document processing
                          example: ready
                        created_at:
                          type: string
                          description: ISO 8601 timestamp of when the document was created
                          example: '2024-01-01T12:00:00Z'
                        updated_at:
                          type: string
                          description: >-
                            ISO 8601 timestamp of when the document was last
                            updated
                          example: '2024-01-01T12:05:00Z'
                        callback_url:
                          type: string
                          description: URL that receives status updates
                          example: https://your-server.com/webhook
                        tags:
                          type: array
                          description: Array of document tags
                          items:
                            type: string
                          example:
                            - important
                            - meeting
                        properties:
                          type: object
                          description: Additional document properties
                          example:
                            department: sales
                            priority: high
              total_count:
                allOf:
                  - type: integer
                    description: Total number of documents matching the filter criteria
                    example: 42
              page:
                allOf:
                  - type: integer
                    description: Current page number
                    example: 0
              limit:
                allOf:
                  - type: integer
                    description: Number of documents per page
                    example: 10
        examples:
          example:
            value:
              data:
                - uuid: d290f1ee-6c54-4b01-90e6-d701748f0851
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
              total_count: 42
              page: 0
              limit: 10
        description: List of documents
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message
                    example: 'Invalid request: limit must be a positive integer'
        examples:
          example:
            value:
              error: 'Invalid request: limit must be a positive integer'
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