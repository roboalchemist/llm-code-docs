# Source: https://docs.tavus.io/api-reference/documents/get-document.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Document

> Retrieve a specific document by ID

Retrieve detailed information about a specific document using its unique identifier.


## OpenAPI

````yaml get /v2/documents/{document_id}
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
  /v2/documents/{document_id}:
    get:
      tags:
        - Documents
      summary: Get Document
      description: >
        Retrieve detailed information about a specific document using its unique
        identifier.
      operationId: getDocument
      parameters:
        - in: path
          name: document_id
          required: true
          schema:
            type: string
          description: The unique identifier of the document to retrieve
          example: d8-5c71baca86fc
      responses:
        '200':
          description: Document details
          content:
            application/json:
              schema:
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
                    description: ISO 8601 timestamp of when the document was last updated
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
                      List of URLs that were crawled (only present for crawled
                      websites after processing completes)
                    items:
                      type: string
                    example:
                      - https://docs.example.com/
                      - https://docs.example.com/getting-started
                      - https://docs.example.com/api
                  last_crawled_at:
                    type: string
                    nullable: true
                    description: ISO 8601 timestamp of when the document was last crawled
                    example: '2024-01-01T12:00:00Z'
                  crawl_count:
                    type: integer
                    nullable: true
                    description: Number of times the document has been crawled
                    example: 1
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
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: The error message
                    example: Document not found
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````