# Source: https://docs.tavus.io/api-reference/documents/get-documents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List Documents

> Retrieve a list of documents with optional filtering and pagination

Retrieve a list of documents with support for pagination, sorting, and filtering by various criteria.


## OpenAPI

````yaml get /v2/documents
openapi: 3.0.3
info:
  title: Tavus Developer API Collection
  version: 1.0.0
  contact: {}
servers:
  - url: https://tavusapi.com
security:
  - apiKey: []
tags:
  - name: Videos
  - name: Replicas
  - name: Conversations
  - name: Personas
  - name: Replacements
  - name: Transcriptions
  - name: Documents
paths:
  /v2/documents:
    get:
      tags:
        - Documents
      summary: List Documents
      description: >
        Retrieve a list of documents with support for pagination, sorting, and
        filtering by various criteria.
      operationId: listDocuments
      parameters:
        - in: query
          name: limit
          schema:
            type: integer
          description: 'Number of documents to return per page (default: 10)'
          example: 10
        - in: query
          name: page
          schema:
            type: integer
          description: 'Page number for pagination (0-based, default: 0)'
          example: 0
        - in: query
          name: sort
          schema:
            type: string
            enum:
              - ascending
              - descending
          description: 'Sort direction for the results (default: ascending)'
          example: ascending
        - in: query
          name: status
          schema:
            type: string
          description: Filter documents by status
        - in: query
          name: name_or_uuid
          schema:
            type: string
          description: Search for documents by name or UUID
        - in: query
          name: tags
          schema:
            type: string
          description: Comma-separated list of tags to filter by
          example: important,meeting
      responses:
        '200':
          description: List of documents
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        document_id:
                          type: string
                          description: Unique identifier for the document
                          example: d8-5c71baca86fc
                        document_name:
                          type: string
                          description: Name of the document
                          example: Example Docs
                        document_url:
                          type: string
                          description: URL of the document
                          example: https://docs.example.com/
                        status:
                          type: string
                          description: Current status of the document processing
                          example: ready
                        progress:
                          type: string
                          nullable: true
                          description: Progress indicator for document processing
                          example: null
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
                            - docs
                            - website
                        crawl_config:
                          type: object
                          nullable: true
                          description: >-
                            The crawl configuration used for this document (only
                            present for crawled websites)
                          properties:
                            depth:
                              type: integer
                              description: Crawl depth setting
                              example: 2
                            max_pages:
                              type: integer
                              description: Maximum pages setting
                              example: 10
                        crawled_urls:
                          type: array
                          nullable: true
                          description: >-
                            List of URLs that were crawled (only present for
                            crawled websites after processing completes)
                          items:
                            type: string
                          example:
                            - https://docs.example.com/
                            - https://docs.example.com/getting-started
                        last_crawled_at:
                          type: string
                          nullable: true
                          description: >-
                            ISO 8601 timestamp of when the document was last
                            crawled
                          example: '2024-01-01T12:00:00Z'
                        crawl_count:
                          type: integer
                          nullable: true
                          description: Number of times the document has been crawled
                          example: 1
                  total_count:
                    type: integer
                    description: Total number of documents matching the filter criteria
                    example: 42
                  page:
                    type: integer
                    description: Current page number
                    example: 0
                  limit:
                    type: integer
                    description: Number of documents per page
                    example: 10
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message
                    example: 'Invalid request: limit must be a positive integer'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: The error message
                    example: Invalid access token
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````