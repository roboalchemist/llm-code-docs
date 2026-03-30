# Source: https://docs.dify.ai/api-reference/documents/update-a-document-with-a-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a Document with a File

> Updates an existing document by uploading a new file, replacing its content.



## OpenAPI

````yaml en/api-reference/openapi_knowledge.json post /datasets/{dataset_id}/documents/{document_id}/update-by-file
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
  /datasets/{dataset_id}/documents/{document_id}/update-by-file:
    post:
      tags:
        - Documents
      summary: Update a Document with a File
      description: >-
        Updates an existing document by uploading a new file, replacing its
        content.
      operationId: updateDocumentByFile
      parameters:
        - name: dataset_id
          in: path
          required: true
          description: The ID of the knowledge base containing the document.
          schema:
            type: string
            format: uuid
        - name: document_id
          in: path
          required: true
          description: The ID of the document to update.
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                data:
                  type: string
                  description: >-
                    A JSON string containing optional document name and
                    processing rules. See `UpdateDocumentByFileRequestData`
                    schema.
                  example: '{"name":"new_name.txt","process_rule":{"mode":"automatic"}}'
                file:
                  type: string
                  format: binary
                  description: The new file to upload.
      responses:
        '200':
          description: Document updated successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DocumentCreationResponse'
components:
  schemas:
    DocumentCreationResponse:
      type: object
      properties:
        document:
          $ref: '#/components/schemas/Document'
        batch:
          type: string
          description: A batch identifier for tracking indexing progress.
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