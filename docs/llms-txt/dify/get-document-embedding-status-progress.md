# Source: https://docs.dify.ai/api-reference/documents/get-document-embedding-status-progress.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Document Embedding Status (Progress)

> Retrieves the indexing status for a batch of documents, showing the progress of embedding and processing.



## OpenAPI

````yaml en/api-reference/openapi_knowledge.json get /datasets/{dataset_id}/documents/{batch}/indexing-status
openapi: 3.0.1
info:
  title: Knowledge API
  description: >-
    API for managing knowledge bases (datasets), documents, and segments,
    including creation, retrieval, and configuration.
  version: 1.0.0
servers:
  - url: '{apiBaseUrl}'
    description: The base URL for the Knowledge API.
    variables:
      apiBaseUrl:
        default: https://api.dify.ai/v1
        description: Actual base URL of the API
security:
  - ApiKeyAuth: []
tags:
  - name: Datasets
    description: Operations related to managing knowledge bases (datasets).
  - name: Documents
    description: >-
      Operations for creating, updating, and managing documents within a
      dataset.
  - name: Chunks
    description: Operations for managing document chunks (segments).
  - name: Metadata & Tags
    description: Operations for managing dataset tags and metadata.
  - name: Models
    description: Operations for retrieving available models.
paths:
  /datasets/{dataset_id}/documents/{batch}/indexing-status:
    get:
      tags:
        - Documents
      summary: Get Document Embedding Status (Progress)
      description: >-
        Retrieves the indexing status for a batch of documents, showing the
        progress of embedding and processing.
      operationId: getDocumentIndexingStatus
      parameters:
        - name: dataset_id
          in: path
          required: true
          description: The ID of the knowledge base.
          schema:
            type: string
            format: uuid
        - name: batch
          in: path
          required: true
          description: The batch number returned from the document creation endpoint.
          schema:
            type: string
      responses:
        '200':
          description: Indexing status of the documents in the batch.
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/IndexingStatus'
components:
  schemas:
    IndexingStatus:
      type: object
      properties:
        id:
          type: string
          format: uuid
        indexing_status:
          type: string
        processing_started_at:
          type: number
          format: float
        parsing_completed_at:
          type: number
          format: float
        cleaning_completed_at:
          type: number
          format: float
        splitting_completed_at:
          type: number
          format: float
        completed_at:
          type: number
          format: float
          nullable: true
        paused_at:
          type: number
          format: float
          nullable: true
        error:
          type: string
          nullable: true
        stopped_at:
          type: number
          format: float
          nullable: true
        completed_segments:
          type: integer
        total_segments:
          type: integer
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: >-
        API Key authentication. For all API requests, include your API Key in
        the `Authorization` HTTP Header, prefixed with 'Bearer '. Example:
        `Authorization: Bearer {API_KEY}`. **Strongly recommend storing your API
        Key on the server-side, not shared or stored on the client-side, to
        avoid possible API-Key leakage that can lead to serious consequences.**

````

Built with [Mintlify](https://mintlify.com).