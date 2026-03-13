# Source: https://docs.dify.ai/api-reference/datasets/get-knowledge-base-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Knowledge Base List

> Retrieves a list of knowledge bases, with options for pagination and filtering.



## OpenAPI

````yaml en/api-reference/openapi_knowledge.json get /datasets
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
  /datasets:
    get:
      tags:
        - Datasets
      summary: Get Knowledge Base List
      description: >-
        Retrieves a list of knowledge bases, with options for pagination and
        filtering.
      operationId: listDatasets
      parameters:
        - name: keyword
          in: query
          description: Search keyword to filter datasets by name.
          schema:
            type: string
        - name: tag_ids
          in: query
          description: List of tag IDs to filter by. Datasets must have all specified tags.
          schema:
            type: array
            items:
              type: string
          style: form
          explode: false
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
        - name: include_all
          in: query
          description: >-
            Whether to include all datasets. This is effective only for
            workspace owners.
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: A paginated list of datasets.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DatasetListResponse'
components:
  schemas:
    DatasetListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/Dataset'
        has_more:
          type: boolean
        limit:
          type: integer
        total:
          type: integer
        page:
          type: integer
    Dataset:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        description:
          type: string
          nullable: true
        provider:
          type: string
        permission:
          type: string
        data_source_type:
          type: string
          nullable: true
        indexing_technique:
          type: string
          nullable: true
        app_count:
          type: integer
        document_count:
          type: integer
        word_count:
          type: integer
        created_by:
          type: string
          format: uuid
        created_at:
          type: integer
          format: int64
        updated_by:
          type: string
          format: uuid
        updated_at:
          type: integer
          format: int64
        embedding_model:
          type: string
          nullable: true
        embedding_model_provider:
          type: string
          nullable: true
        embedding_available:
          type: boolean
          nullable: true
        summary_index_setting:
          $ref: '#/components/schemas/SummaryIndexSetting'
          description: Summary Auto-Gen configurations for this dataset.
          nullable: true
    SummaryIndexSetting:
      type: object
      description: Configuration for Summary Auto-Gen.
      properties:
        enable:
          type: boolean
          description: Whether to enable Summary Auto-Gen.
        model_name:
          type: string
          description: Name of the model to use for generating summaries.
        model_provider_name:
          type: string
          description: Provider of the summary model.
        summary_prompt:
          type: string
          description: Prompt template for generating summaries.
      required:
        - enable
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