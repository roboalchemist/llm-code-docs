# Source: https://docs.dify.ai/api-reference/datasets/delete-a-knowledge-base.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a Knowledge Base

> Deletes a knowledge base and all its associated documents and data.



## OpenAPI

````yaml en/api-reference/openapi_knowledge.json delete /datasets/{dataset_id}
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
  /datasets/{dataset_id}:
    delete:
      tags:
        - Datasets
      summary: Delete a Knowledge Base
      description: Deletes a knowledge base and all its associated documents and data.
      operationId: deleteDataset
      parameters:
        - name: dataset_id
          in: path
          required: true
          description: The unique identifier of the knowledge base to delete.
          schema:
            type: string
            format: uuid
      responses:
        '204':
          description: Successfully deleted the dataset.
components:
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