# Source: https://io.net/docs/reference/rag/documents/upload-and-ingest-a-document.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new document

> Creates a new Document object from an input file, text content, or chunks.

The chosen `ingestion_mode` determines how the ingestion process is configured:

**Ingestion Modes:**

* `hi-res`: Comprehensive parsing and enrichment, including summaries and possibly more thorough parsing.
* `fast`: Speed-focused ingestion that skips certain enrichment steps like summaries.
* `custom`: Provide a full `ingestion_config` to customize the entire ingestion process.

Either a file or text content must be provided, but not both. Documents are shared through `Collections` which allow for tightly specified cross-user interactions.

The ingestion process runs asynchronously and its progress can be tracked using the returned task\_id.


## OpenAPI

````yaml openapi/rag-documents/upload-and-ingest-a-document.json post /api/r2r/v3/documents
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/documents:
    post:
      summary: Create a new document
      description: >-
        Creates a new Document object from an input file, text content, or
        chunks.
      operationId: upload-and-ingest-a-document
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                file:
                  type: string
                  description: >-
                    The file to ingest. Exactly one of file, raw_text, or chunks
                    must be provided.
                  default: 'format: "binary"'
                raw_text:
                  type: string
                  description: >-
                    Raw text content to ingest. Exactly one of file, raw_text,
                    or chunks must be provided.
                chunks:
                  type: string
                  description: >-
                    Pre-processed text chunks to ingest. Exactly one of file,
                    raw_text, or chunks must be provided.
                id:
                  type: string
                  description: >-
                    The ID of the document. If not provided, a new ID will be
                    generated.
                  default: 'format: "uuid"'
                collection_ids:
                  type: string
                  description: >-
                    Collection IDs to associate with the document. If none are
                    provided, the document will be assigned to the user's
                    default collection.
                metadata:
                  type: string
                  description: >-
                    Metadata to associate with the document, such as title,
                    description, or custom fields.
                ingestion_mode:
                  type: string
                  description: >-
                    Ingestion modes:  hi-res: Thorough ingestion with full
                    summaries and enrichment. ocr: OCR via Mistral and full
                    summaries. fast: Quick ingestion with minimal enrichment and
                    no summaries. custom: Full control via ingestion_config. If
                    filters or limit (in ingestion_config) are provided
                    alongside hi-res or fast, they will override the default
                    settings for that mode.
                  enum:
                    - hi-res
                    - ocr
                    - fast
                    - custom
                ingestion_config:
                  type: string
                  description: >-
                    An optional dictionary to override the default chunking
                    configuration for the ingestion process. If not provided,
                    the system will use the default server-side chunking
                    configuration.
                run_with_orchestration:
                  type: boolean
                  description: >-
                    Whether or not ingestion runs with orchestration, default is
                    True. When set to False, the ingestion process will run
                    synchronous and directly return the result.
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    results:
                      message: Ingestion task queued successfully.
                      document_id: 9fbe403b-c11c-5aae-8ade-ef22980c3ad1
                      task_id: c68dc72e-fc23-5452-8f49-d7bd46088a96
              schema:
                type: object
                properties:
                  results:
                    type: object
                    properties:
                      message:
                        type: string
                        example: Ingestion task queued successfully.
                      document_id:
                        type: string
                        example: 9fbe403b-c11c-5aae-8ade-ef22980c3ad1
                      task_id:
                        type: string
                        example: c68dc72e-fc23-5452-8f49-d7bd46088a96
        '404':
          description: '404'
          content:
            application/json:
              examples:
                Result:
                  value: {}
              schema:
                type: object
                properties: {}
        '422':
          description: '422'
          content:
            application/json:
              examples:
                Result:
                  value:
                    detail:
                      - loc:
                          - string
                          - 0
                        msg: string
                        type: string
              schema:
                type: object
                properties:
                  detail:
                    type: array
                    items:
                      type: object
                      properties:
                        loc:
                          type: array
                        msg:
                          type: string
                          example: string
                        type:
                          type: string
                          example: string
      deprecated: false
components:
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````