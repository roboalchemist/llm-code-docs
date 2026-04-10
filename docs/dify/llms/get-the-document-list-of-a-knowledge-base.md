# Source: https://docs.dify.ai/api-reference/documents/get-the-document-list-of-a-knowledge-base.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get the Document List of a Knowledge Base

> Retrieves a paginated list of all documents within a specified knowledge base.



## OpenAPI

````yaml en/api-reference/openapi_knowledge.json get /datasets/{dataset_id}/documents
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
  /datasets/{dataset_id}/documents:
    get:
      tags:
        - Documents
      summary: Get the Document List of a Knowledge Base
      description: >-
        Retrieves a paginated list of all documents within a specified knowledge
        base.
      operationId: listDocuments
      parameters:
        - name: dataset_id
          in: path
          required: true
          description: The ID of the knowledge base.
          schema:
            type: string
            format: uuid
        - name: keyword
          in: query
          description: Keyword to search for in document names.
          schema:
            type: string
        - name: page
          in: query
          description: Page number for pagination.
          schema:
            type: integer
            default: 1
        - name: limit
          in: query
          description: Number of items to return per page.
          schema:
            type: integer
            default: 20
            minimum: 1
            maximum: 100
      responses:
        '200':
          description: A paginated list of documents.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DocumentListResponse'
components:
  schemas:
    DocumentListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/Document'
        has_more:
          type: boolean
        limit:
          type: integer
        total:
          type: integer
        page:
          type: integer
    Document:
      type: object
      properties:
        id:
          type: string
          format: uuid
        position:
          type: integer
        data_source_type:
          type: string
        data_source_info:
          type: object
          nullable: true
        dataset_process_rule_id:
          type: string
          format: uuid
          nullable: true
        name:
          type: string
        created_from:
          type: string
        created_by:
          type: string
          format: uuid
        created_at:
          type: integer
          format: int64
        tokens:
          type: integer
        indexing_status:
          type: string
        error:
          type: string
          nullable: true
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
        archived:
          type: boolean
        display_status:
          type: string
        word_count:
          type: integer
        hit_count:
          type: integer
        doc_form:
          type: string
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