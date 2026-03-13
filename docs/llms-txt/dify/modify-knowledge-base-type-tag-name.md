# Source: https://docs.dify.ai/api-reference/metadata-&-tags/modify-knowledge-base-type-tag-name.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Modify Knowledge Base Type Tag Name

> Updates the name of an existing tag.



## OpenAPI

````yaml en/api-reference/openapi_knowledge.json patch /datasets/tags
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
  /datasets/tags:
    patch:
      tags:
        - Metadata & Tags
      summary: Modify Knowledge Base Type Tag Name
      description: Updates the name of an existing tag.
      operationId: updateKnowledgeTag
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - tag_id
                - name
              properties:
                tag_id:
                  type: string
                  description: The ID of the tag to modify.
                  format: uuid
                name:
                  type: string
                  description: The new name for the tag.
                  maxLength: 50
      responses:
        '200':
          description: Successfully updated tag.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Tag'
components:
  schemas:
    Tag:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        type:
          type: string
          example: knowledge
        binding_count:
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