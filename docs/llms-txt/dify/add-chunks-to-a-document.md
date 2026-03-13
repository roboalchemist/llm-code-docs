# Source: https://docs.dify.ai/api-reference/chunks/add-chunks-to-a-document.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Add Chunks to a Document

> Adds one or more new chunks (segments) to a specific document. This is useful for manually adding curated content.



## OpenAPI

````yaml en/api-reference/openapi_knowledge.json post /datasets/{dataset_id}/documents/{document_id}/segments
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
  /datasets/{dataset_id}/documents/{document_id}/segments:
    post:
      tags:
        - Chunks
      summary: Add Chunks to a Document
      description: >-
        Adds one or more new chunks (segments) to a specific document. This is
        useful for manually adding curated content.
      operationId: createSegments
      parameters:
        - name: dataset_id
          in: path
          required: true
          description: The ID of the knowledge base.
          schema:
            type: string
            format: uuid
        - name: document_id
          in: path
          required: true
          description: The ID of the document.
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateSegmentsRequest'
      responses:
        '200':
          description: List of newly created segments.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SegmentListResponse'
components:
  schemas:
    CreateSegmentsRequest:
      type: object
      properties:
        segments:
          type: array
          items:
            type: object
            required:
              - content
            properties:
              content:
                type: string
                description: The text content of the chunk (or question in Q&A mode).
              answer:
                type: string
                description: The answer content, required if the document is in Q&A mode.
              keywords:
                type: array
                description: Keywords associated with the chunk.
                items:
                  type: string
    SegmentListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/Segment'
        doc_form:
          type: string
    Segment:
      type: object
      properties:
        id:
          type: string
          format: uuid
        position:
          type: integer
        document_id:
          type: string
          format: uuid
        content:
          type: string
        answer:
          type: string
          nullable: true
        word_count:
          type: integer
        tokens:
          type: integer
        keywords:
          type: array
          items:
            type: string
        index_node_id:
          type: string
        index_node_hash:
          type: string
        hit_count:
          type: integer
        enabled:
          type: boolean
        disabled_at:
          type: integer
          format: int64
          nullable: true
        disabled_by:
          type: string
          format: uuid
          nullable: true
        status:
          type: string
        created_by:
          type: string
          format: uuid
        created_at:
          type: integer
          format: int64
        indexing_at:
          type: integer
          format: int64
        completed_at:
          type: integer
          format: int64
        error:
          type: string
          nullable: true
        stopped_at:
          type: integer
          format: int64
          nullable: true
        summary:
          type: string
          nullable: true
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