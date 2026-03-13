# Source: https://docs.dify.ai/api-reference/datasets/retrieve-chunks-from-a-knowledge-base-test-retrieval.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve Chunks from a Knowledge Base / Test Retrieval

> Performs a search query against a knowledge base to retrieve the most relevant chunks (segments). This endpoint can be used for both production retrieval and test retrieval.



## OpenAPI

````yaml en/api-reference/openapi_knowledge.json post /datasets/{dataset_id}/retrieve
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
  /datasets/{dataset_id}/retrieve:
    post:
      tags:
        - Datasets
      summary: Retrieve Chunks from a Knowledge Base / Test Retrieval
      description: >-
        Performs a search query against a knowledge base to retrieve the most
        relevant chunks (segments). This endpoint can be used for both
        production retrieval and test retrieval.
      operationId: retrieveSegments
      parameters:
        - name: dataset_id
          in: path
          required: true
          description: The ID of the knowledge base to retrieve from.
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RetrieveRequest'
      responses:
        '200':
          description: List of retrieved segments matching the query.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RetrieveResponse'
components:
  schemas:
    RetrieveRequest:
      type: object
      required:
        - query
      properties:
        query:
          type: string
          description: The search query string.
        retrieval_model:
          allOf:
            - $ref: '#/components/schemas/RetrievalModel'
            - type: object
              properties:
                metadata_filtering_conditions:
                  type: object
                  description: Conditions for filtering results based on metadata.
                  properties:
                    logical_operator:
                      type: string
                      enum:
                        - and
                        - or
                    conditions:
                      type: array
                      items:
                        type: object
                        properties:
                          name:
                            type: string
                            description: Name of the metadata field.
                          comparison_operator:
                            type: string
                            description: The operator for comparison.
                          value:
                            oneOf:
                              - type: string
                              - type: number
                            nullable: true
                            description: The value to compare against.
    RetrieveResponse:
      type: object
      properties:
        query:
          type: object
          properties:
            content:
              type: string
        records:
          type: array
          items:
            $ref: '#/components/schemas/RetrievedSegment'
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
    RetrievedSegment:
      type: object
      properties:
        segment:
          allOf:
            - $ref: '#/components/schemas/Segment'
            - type: object
              properties:
                document:
                  type: object
                  properties:
                    id:
                      type: string
                      format: uuid
                    data_source_type:
                      type: string
                    name:
                      type: string
        score:
          type: number
          format: float
    Segment:
      type: object
      properties:
        id:
          type: string
          format: uuid
        position:
          type: integer
        document_id:
          type: string
          format: uuid
        content:
          type: string
        answer:
          type: string
          nullable: true
        word_count:
          type: integer
        tokens:
          type: integer
        keywords:
          type: array
          items:
            type: string
        index_node_id:
          type: string
        index_node_hash:
          type: string
        hit_count:
          type: integer
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
        summary:
          type: string
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