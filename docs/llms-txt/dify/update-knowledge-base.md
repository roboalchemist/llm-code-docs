# Source: https://docs.dify.ai/api-reference/datasets/update-knowledge-base.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Knowledge Base

> Updates the settings of a specific knowledge base.



## OpenAPI

````yaml en/api-reference/openapi_knowledge.json patch /datasets/{dataset_id}
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
    patch:
      tags:
        - Datasets
      summary: Update Knowledge Base
      description: Updates the settings of a specific knowledge base.
      operationId: updateDataset
      parameters:
        - name: dataset_id
          in: path
          required: true
          description: The unique identifier of the knowledge base.
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateDatasetRequest'
      responses:
        '200':
          description: Successfully updated dataset details.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DatasetDetail'
        '409':
          $ref: '#/components/responses/DatasetNameDuplicate'
components:
  schemas:
    UpdateDatasetRequest:
      type: object
      properties:
        name:
          type: string
          description: New name for the knowledge base.
        description:
          type: string
          description: New description for the knowledge base.
        indexing_technique:
          type: string
          enum:
            - high_quality
            - economy
        permission:
          type: string
          enum:
            - only_me
            - all_team_members
            - partial_members
        embedding_model_provider:
          type: string
        embedding_model:
          type: string
        retrieval_model:
          $ref: '#/components/schemas/RetrievalModel'
        summary_index_setting:
          $ref: '#/components/schemas/SummaryIndexSetting'
          description: Configuration for Summary Auto-Gen.
        partial_member_list:
          type: array
          description: List of members for 'partial_members' permission.
          items:
            type: object
            required:
              - user_id
            properties:
              user_id:
                type: string
                description: User ID of the member.
    DatasetDetail:
      allOf:
        - $ref: '#/components/schemas/Dataset'
        - type: object
          properties:
            retrieval_model_dict:
              $ref: '#/components/schemas/RetrievalModel'
            tags:
              type: array
              items:
                type: object
            doc_form:
              type: string
              nullable: true
    RetrievalModel:
      type: object
      properties:
        search_method:
          type: string
          description: The search method to use for retrieval.
          enum:
            - hybrid_search
            - semantic_search
            - full_text_search
            - keyword_search
        reranking_enable:
          type: boolean
          description: Whether to enable a rerank model to improve search results.
        reranking_mode:
          type: string
          description: The reranking mode.
          default: reranking_model
          enum:
            - reranking_model
            - weighted_score
        reranking_model:
          type: object
          description: Configuration for the rerank model.
          properties:
            reranking_provider_name:
              type: string
              description: The provider of the rerank model.
            reranking_model_name:
              type: string
              description: The name of the rerank model.
          nullable: true
        top_k:
          type: integer
          description: The number of top matching results to return.
        score_threshold_enabled:
          type: boolean
          description: Whether to apply a score threshold to filter results.
        score_threshold:
          type: number
          format: float
          description: The minimum score for a result to be included.
          nullable: true
        weights:
          type: number
          format: float
          description: The weight of semantic search in a hybrid search mode.
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
    ErrorResponse:
      type: object
      properties:
        code:
          type: string
          description: A machine-readable error code.
        message:
          type: string
          description: A human-readable error message.
        status:
          type: integer
          description: The HTTP status code.
      example:
        code: no_file_uploaded
        message: Please upload your file.
        status: 400
  responses:
    DatasetNameDuplicate:
      description: The dataset name already exists.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
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