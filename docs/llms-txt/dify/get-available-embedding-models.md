# Source: https://docs.dify.ai/api-reference/models/get-available-embedding-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get available embedding models

> Fetches a list of all available text embedding models that can be used for creating and querying knowledge bases.



## OpenAPI

````yaml en/api-reference/openapi_knowledge.json get /workspaces/current/models/model-types/text-embedding
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
  /workspaces/current/models/model-types/text-embedding:
    get:
      tags:
        - Models
      summary: Get available embedding models
      description: >-
        Fetches a list of all available text embedding models that can be used
        for creating and querying knowledge bases.
      operationId: getAvailableEmbeddingModels
      responses:
        '200':
          description: A list of available embedding models grouped by provider.
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/ModelProvider'
components:
  schemas:
    ModelProvider:
      type: object
      properties:
        provider:
          type: string
        label:
          type: object
          additionalProperties:
            type: string
        icon_small:
          type: object
          additionalProperties:
            type: string
            format: uri
        icon_large:
          type: object
          additionalProperties:
            type: string
            format: uri
        status:
          type: string
        models:
          type: array
          items:
            $ref: '#/components/schemas/Model'
    Model:
      type: object
      properties:
        model:
          type: string
        label:
          type: object
          additionalProperties:
            type: string
        model_type:
          type: string
        features:
          type: array
          items: {}
          nullable: true
        fetch_from:
          type: string
        model_properties:
          type: object
          properties:
            context_size:
              type: integer
        deprecated:
          type: boolean
        status:
          type: string
        load_balancing_enabled:
          type: boolean
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