# Source: https://docs.tavus.io/api-reference/documents/patch-document.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Document

> Update a specific document's metadata

Update metadata for a specific document. This endpoint allows you to modify the document name and its tags.


## OpenAPI

````yaml patch /v2/documents/{document_id}
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
    patch:
      tags:
        - Documents
      summary: Update Document
      description: >
        Update metadata for a specific document. This endpoint allows you to
        modify the document's name and tags.
      operationId: patchDocument
      parameters:
        - in: path
          name: document_id
          required: true
          schema:
            type: string
          description: The unique identifier of the document to update
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                document_name:
                  type: string
                  description: New name for the document
                  example: Updated Document Name
                tags:
                  type: array
                  description: >-
                    New array of tags for the document. This will overwrite the
                    existing tags for the document.
                  items:
                    type: string
                  example:
                    - docs
                    - website
                    - updated
      responses:
        '200':
          description: Document updated successfully
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
                    description: Updated name of the document
                    example: Updated Document Name
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
                    example: '2024-01-01T13:00:00Z'
                  callback_url:
                    type: string
                    description: URL that receives status updates
                    example: https://your-server.com/webhook
                  tags:
                    type: array
                    description: Updated array of document tags
                    items:
                      type: string
                    example:
                      - docs
                      - website
                      - updated
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
                    example: 'Invalid request: document_name must be a string'
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