# Source: https://docs.tavus.io/api-reference/documents/recrawl-document.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Recrawl Document

> Trigger a recrawl of a website document to fetch fresh content

Trigger a recrawl of a document that was created with crawl configuration. This is useful for keeping your knowledge base up-to-date when website content changes.

## When to Recrawl

Use this endpoint when:

* The source website has been updated with new content
* You want to refresh the document's content on a schedule
* The initial crawl encountered errors and you want to retry

## How Recrawling Works

When you trigger a recrawl:

1. The system uses the same starting URL from the original document
2. Links are followed according to the crawl configuration (depth and max\_pages)
3. New content is processed and stored
4. Old vectors are replaced with the new content once processing completes
5. The document's `crawl_count` is incremented and `last_crawled_at` is updated

## Requirements

* **Document State**: The document must be in `ready` or `error` state
* **Crawl Configuration**: The document must have been created with a `crawl` configuration, or you must provide one in the request body

## Rate Limits

To prevent abuse, the following limits apply:

* **Cooldown Period**: 1 hour between recrawls of the same document
* **Concurrent Crawls**: Maximum 5 crawls running simultaneously per user
* **Total Documents**: Maximum 100 crawl documents per user

## Overriding Crawl Configuration

You can optionally provide a `crawl` object in the request body to override the stored configuration for this recrawl:

```json  theme={null}
{
  "crawl": {
    "depth": 3,
    "max_pages": 50
  }
}
```

If no `crawl` object is provided, the original crawl configuration from document creation is used.

## Monitoring Recrawl Progress

After initiating a recrawl:

1. The document status changes to `recrawling`
2. If you provided a `callback_url` during document creation, you'll receive status updates
3. When complete, the status changes to `ready` (or `error` if it failed)
4. Use [Get Document](/api-reference/documents/get-document) to check the current status


## OpenAPI

````yaml post /v2/documents/{document_id}/recrawl
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
  /v2/documents/{document_id}/recrawl:
    post:
      tags:
        - Documents
      summary: Recrawl Document
      description: >
        Trigger a recrawl of a document that was created with crawl
        configuration. The recrawl will fetch fresh content from the website and
        replace the existing vectors.


        **Requirements:**

        - Document must be in `ready` or `error` state

        - Document must have been created with a `crawl` configuration (or you
        must provide one in this request)

        - There is a 1-hour cooldown between recrawls of the same document


        **Rate Limits:**

        - Maximum 5 concurrent crawls per user

        - Maximum 100 crawl documents per user
      operationId: recrawlDocument
      parameters:
        - in: path
          name: document_id
          required: true
          schema:
            type: string
          description: The unique identifier of the document to recrawl
          example: d8-5c71baca86fc
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                crawl:
                  type: object
                  description: >
                    Optional crawl configuration to override the stored
                    settings. If not provided, the original crawl configuration
                    will be used.
                  properties:
                    depth:
                      type: integer
                      description: >-
                        How many levels deep to follow links from the starting
                        URL (1-10)
                      minimum: 1
                      maximum: 10
                      example: 2
                    max_pages:
                      type: integer
                      description: Maximum number of pages to crawl (1-100)
                      minimum: 1
                      maximum: 100
                      example: 10
      responses:
        '202':
          description: Recrawl initiated successfully
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
                    example: Company Website
                  document_url:
                    type: string
                    description: URL of the document
                    example: https://example.com/
                  status:
                    type: string
                    description: Current status of the document (will be 'recrawling')
                    example: recrawling
                  progress:
                    type: integer
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
                    example: '2024-01-15T10:30:00Z'
                  callback_url:
                    type: string
                    description: URL that will receive status updates
                    example: https://your-server.com/webhook
                  tags:
                    type: array
                    description: Array of document tags
                    items:
                      type: string
                    example:
                      - website
                      - company
                  crawl_config:
                    type: object
                    description: The crawl configuration being used for the recrawl
                    properties:
                      depth:
                        type: integer
                        example: 2
                      max_pages:
                        type: integer
                        example: 10
                  crawled_urls:
                    type: array
                    nullable: true
                    description: >-
                      List of URLs from the previous crawl (will be updated when
                      recrawl completes)
                    items:
                      type: string
                    example:
                      - https://docs.example.com/
                      - https://docs.example.com/getting-started
                  last_crawled_at:
                    type: string
                    nullable: true
                    description: ISO 8601 timestamp of the previous crawl
                    example: '2024-01-01T12:05:00Z'
                  crawl_count:
                    type: integer
                    description: >-
                      Number of times the document has been crawled (will
                      increment when recrawl completes)
                    example: 1
        '400':
          description: Bad Request - Validation error
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message
                    example: Document was not created with crawl configuration
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
        '409':
          description: Conflict - Document state prevents recrawl
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message
                    example: >-
                      Document must be in 'ready' or 'error' state to recrawl,
                      current status: processing
        '429':
          description: Too Many Requests - Rate limit exceeded or cooldown period
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message
                    example: >-
                      Recrawl cooldown: please wait 45 minutes before recrawling
                      this document.
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````