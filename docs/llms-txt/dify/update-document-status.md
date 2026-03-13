# Source: https://docs.dify.ai/api-reference/documents/update-document-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Document Status

> Performs a batch action to update the status of one or more documents (e.g., enable, disable, archive).



## OpenAPI

````yaml en/api-reference/openapi_knowledge.json patch /datasets/{dataset_id}/documents/status/{action}
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
  /datasets/{dataset_id}/documents/status/{action}:
    patch:
      tags:
        - Documents
      summary: Update Document Status
      description: >-
        Performs a batch action to update the status of one or more documents
        (e.g., enable, disable, archive).
      operationId: batchUpdateDocumentStatus
      parameters:
        - name: dataset_id
          in: path
          required: true
          description: The ID of the knowledge base.
          schema:
            type: string
            format: uuid
        - name: action
          in: path
          required: true
          description: The action to perform on the documents.
          schema:
            type: string
            enum:
              - enable
              - disable
              - archive
              - un_archive
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - document_ids
              properties:
                document_ids:
                  type: array
                  description: A list of document IDs to perform the action on.
                  items:
                    type: string
                    format: uuid
      responses:
        '200':
          $ref: '#/components/responses/Success'
components:
  responses:
    Success:
      description: Operation successful.
      content:
        application/json:
          schema:
            type: object
            properties:
              result:
                type: string
                example: success
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