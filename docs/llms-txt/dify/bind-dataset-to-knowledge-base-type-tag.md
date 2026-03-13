# Source: https://docs.dify.ai/api-reference/metadata-&-tags/bind-dataset-to-knowledge-base-type-tag.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Bind Dataset to Knowledge Base Type Tag

> Binds one or more tags to a specific knowledge base.



## OpenAPI

````yaml en/api-reference/openapi_knowledge.json post /datasets/tags/binding
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
  /datasets/tags/binding:
    post:
      tags:
        - Metadata & Tags
      summary: Bind Dataset to Knowledge Base Type Tag
      description: Binds one or more tags to a specific knowledge base.
      operationId: bindTagsToDataset
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - target_id
                - tag_ids
              properties:
                target_id:
                  type: string
                  description: The ID of the dataset to bind tags to.
                  format: uuid
                tag_ids:
                  type: array
                  description: A list of tag IDs to bind.
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