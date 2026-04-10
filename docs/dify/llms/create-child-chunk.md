# Source: https://docs.dify.ai/api-reference/chunks/create-child-chunk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Child Chunk

> Creates a new child chunk under a parent segment in a document using the hierarchical mode.



## OpenAPI

````yaml en/api-reference/openapi_knowledge.json post /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks
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
  /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks:
    post:
      tags:
        - Chunks
      summary: Create Child Chunk
      description: >-
        Creates a new child chunk under a parent segment in a document using the
        hierarchical mode.
      operationId: createChildChunk
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
        - name: segment_id
          in: path
          required: true
          description: The ID of the parent segment.
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateChildChunkRequest'
      responses:
        '200':
          description: Successfully created child chunk.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChildChunkResponse'
components:
  schemas:
    CreateChildChunkRequest:
      type: object
      required:
        - content
      properties:
        content:
          type: string
          description: The content of the child chunk.
    ChildChunkResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/ChildChunk'
    ChildChunk:
      type: object
      description: Represents a child chunk in a hierarchical segmentation.
      properties:
        id:
          type: string
          format: uuid
        segment_id:
          type: string
          format: uuid
        content:
          type: string
        word_count:
          type: integer
        tokens:
          type: integer
        index_node_id:
          type: string
        index_node_hash:
          type: string
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