# Source: https://docs.tavus.io/api-reference/documents/create-document.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Document

> Upload documents to your knowledge base for personas to reference during conversations

<Note>
  For now, our Knowledge Base only supports documents written in English and works best for conversations in English.

  We'll be expanding our Knowledge Base language support soon!
</Note>

Create a new document in your [Knowledge Base](/sections/conversational-video-interface/knowledge-base).

When you hit this endpoint, Tavus kicks off the processing of the document, so it can be used as part of your knowledge base in conversations once processing is complete.

The file size limit is 50MB. The processing can take up to a few minutes depending on file size.

Currently, we support the following file formats: .pdf, .txt, .docx, .doc, .png, .jpg, .pptx, .csv, and .xlsx.

Website URLs are also supported, where a website snapshot will be processed and transformed into a document.

You can manage documents by adding tags using the `tags` field in the request body.

Once created, you can add the document to your personas (see [Create Persona](/api-reference/personas/create-persona)) and your conversations (see [Create Conversation](/api-reference/conversations/create-conversation)).

## Website Crawling

When creating a document from a website URL, you can optionally enable multi-page crawling by providing the `crawl` parameter. This allows the system to follow links from your starting URL and process multiple pages into a single document.

### Without Crawling (Default)

By default, only the single page at the provided URL is scraped and processed.

### With Crawling

When you include the `crawl` object, the system will:

1. Start at your provided URL
2. Follow links to discover additional pages
3. Process all discovered pages into a single document

**Example request with crawling enabled:**

```json  theme={null}
{
  "document_name": "Company Knowledge Base",
  "document_url": "https://docs.example.com/",
  "crawl": {
    "depth": 2,
    "max_pages": 20
  },
  "callback_url": "https://your-server.com/webhook"
}
```

### Crawl Parameters

| Parameter   | Type            | Description                                                                                                                      |
| ----------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `depth`     | integer (1-10)  | How many levels deep to follow links from the starting URL. A depth of 1 means only pages directly linked from the starting URL. |
| `max_pages` | integer (1-100) | Maximum number of pages to crawl. Processing stops once this limit is reached.                                                   |

### Rate Limits

To prevent abuse, crawling has the following limits:

* Maximum **100 crawl documents** per user
* Maximum **5 concurrent crawls** at any time
* **1-hour cooldown** between recrawls of the same document

### Keeping Content Fresh

Once a document is created with crawl configuration, you can trigger a recrawl to fetch fresh content using the [Recrawl Document](/api-reference/documents/recrawl-document) endpoint.


## OpenAPI

````yaml post /v2/documents
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
    post:
      tags:
        - Documents
      summary: Create Document
      description: >
        Create a new document for your [Knowledge
        Base](/sections/conversational-video-interface/knowledge-base). This
        endpoint allows you to submit a document URL for processing and
        analysis.
      operationId: createDocument
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                document_url:
                  type: string
                  description: The URL of the document or website to be processed
                  example: https://docs.example.com/
                document_name:
                  type: string
                  description: >-
                    Optional name for the document. If not provided, a default
                    name will be generated.
                  example: Example Docs
                callback_url:
                  type: string
                  description: >-
                    Optional URL that will receive status updates about the
                    document processing
                  example: https://your-server.com/webhook
                tags:
                  type: array
                  description: Optional array of tags to categorize the document
                  items:
                    type: string
                  example:
                    - docs
                    - website
                crawl:
                  type: object
                  description: >
                    Optional configuration for website crawling. When provided
                    with a website URL, the system will follow links from the
                    starting URL and process multiple pages. Without this
                    parameter, only the single page at the URL is scraped.
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
              required:
                - document_url
      responses:
        '200':
          description: Document created successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  document_id:
                    type: string
                    description: Unique identifier for the created document
                    example: d8-5c71baca86fc
                  document_name:
                    type: string
                    description: Name of the document
                    example: Example Docs
                  document_url:
                    type: string
                    description: URL of the document or website
                    example: https://docs.example.com/
                  status:
                    type: string
                    description: Current status of the document processing
                    example: started
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
                    example: '2024-01-01T12:00:00Z'
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
                    example: 'Invalid request: document_url is required'
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
        '429':
          description: Too Many Requests - Crawl rate limit exceeded
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message
                    example: >-
                      Crawl document limit reached (100). Contact
                      support@tavus.io to increase your limit.
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````