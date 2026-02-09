# Source: https://docs.pinecone.io/reference/api/2025-10/inference/list_models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List available models

> List the embedding and reranking models hosted by Pinecone. 

You can use hosted models as an integrated part of Pinecone operations or for standalone embedding and reranking. For more details, see [Vector embedding](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding) and [Rerank results](https://docs.pinecone.io/guides/search/rerank-results).

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/models" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2025-10"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "models": [
      {
        "model": "llama-text-embed-v2",
        "short_description": "A high performance dense embedding model optimized for multilingual and cross-lingual text question-answering retrieval with support for long documents (up to 2048 tokens) and dynamic embedding size (Matryoshka Embeddings).",
        "type": "embed",
        "vector_type": "dense",
        "default_dimension": 1024,
        "modality": "text",
        "max_sequence_length": 2048,
        "max_batch_size": 96,
        "provider_name": "NVIDIA",
        "supported_metrics": [
          "Cosine",
          "DotProduct"
        ],
        "supported_dimensions": [
          384,
          512,
          768,
          1024,
          2048
        ],
        "supported_parameters": [
          {
            "parameter": "input_type",
            "required": true,
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "query",
              "passage"
            ]
          },
          {
            "parameter": "truncate",
            "required": false,
            "default": "END",
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "END",
              "NONE",
              "START"
            ]
          },
          {
            "parameter": "dimension",
            "required": false,
            "default": 1024,
            "type": "one_of",
            "value_type": "integer",
            "allowed_values": [
              384,
              512,
              768,
              1024,
              2048
            ]
          }
        ]
      },
      {
        "model": "multilingual-e5-large",
        "short_description": "A high-performance dense embedding model trained on a mixture of multilingual datasets. It works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs)",
        "type": "embed",
        "vector_type": "dense",
        "default_dimension": 1024,
        "modality": "text",
        "max_sequence_length": 507,
        "max_batch_size": 96,
        "provider_name": "Microsoft",
        "supported_metrics": [
          "Cosine",
          "Euclidean"
        ],
        "supported_dimensions": [
          1024
        ],
        "supported_parameters": [
          {
            "parameter": "input_type",
            "required": true,
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "query",
              "passage"
            ]
          },
          {
            "parameter": "truncate",
            "required": false,
            "default": "END",
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "END",
              "NONE"
            ]
          }
        ]
      },
      {
        "model": "pinecone-sparse-english-v0",
        "short_description": "A sparse embedding model for converting text to sparse vectors for keyword or hybrid semantic/keyword search. Built on the innovations of the DeepImpact architecture.",
        "type": "embed",
        "vector_type": "sparse",
        "modality": "text",
        "max_sequence_length": 512,
        "max_batch_size": 96,
        "provider_name": "Pinecone",
        "supported_metrics": [
          "DotProduct"
        ],
        "supported_parameters": [
          {
            "parameter": "input_type",
            "required": true,
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "query",
              "passage"
            ]
          },
          {
            "parameter": "truncate",
            "required": false,
            "default": "END",
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "END",
              "NONE"
            ]
          },
          {
            "parameter": "return_tokens",
            "required": false,
            "default": false,
            "type": "any",
            "value_type": "boolean"
          }
        ]
      },
      {
        "model": "bge-reranker-v2-m3",
        "short_description": "A high-performance, multilingual reranking model that works well on messy data and short queries expected to return medium-length passages of text (1-2 paragraphs)",
        "type": "rerank",
        "modality": "text",
        "max_sequence_length": 1024,
        "max_batch_size": 100,
        "provider_name": "BAAI",
        "supported_parameters": [
          {
            "parameter": "truncate",
            "required": false,
            "default": "NONE",
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "END",
              "NONE"
            ]
          }
        ]
      },
      {
        "model": "cohere-rerank-3.5",
        "short_description": "Cohere's leading reranking model, balancing performance and latency for a wide range of enterprise search applications.",
        "type": "rerank",
        "modality": "text",
        "max_sequence_length": 40000,
        "max_batch_size": 200,
        "provider_name": "Cohere",
        "supported_parameters": [
          {
            "parameter": "max_chunks_per_doc",
            "required": false,
            "default": 3072,
            "type": "numeric_range",
            "value_type": "integer",
            "min": 1,
            "max": 3072
          }
        ]
      },
      {
        "model": "pinecone-rerank-v0",
        "short_description": "A state of the art reranking model that out-performs competitors on widely accepted benchmarks. It can handle chunks up to 512 tokens (1-2 paragraphs)",
        "type": "rerank",
        "modality": "text",
        "max_sequence_length": 512,
        "max_batch_size": 100,
        "provider_name": "Pinecone",
        "supported_parameters": [
          {
            "parameter": "truncate",
            "required": false,
            "default": "END",
            "type": "one_of",
            "value_type": "string",
            "allowed_values": [
              "END",
              "NONE"
            ]
          }
        ]
      }
    ]
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/inference_2025-10.oas.yaml get /models
openapi: 3.0.3
info:
  title: Pinecone Inference API
  description: >-
    Pinecone is a vector database that makes it easy to search and retrieve
    billions of high-dimensional vectors.
  contact:
    name: Pinecone Support
    url: https://support.pinecone.io
    email: support@pinecone.io
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0
  version: 2025-10
servers:
  - url: https://api.pinecone.io
    description: Production API endpoints
security:
  - ApiKeyAuth: []
tags:
  - name: Inference
    description: Model inference
externalDocs:
  description: More Pinecone.io API docs
  url: https://docs.pinecone.io/introduction
paths:
  /models:
    get:
      tags:
        - Inference
      summary: List available models
      description: >-
        List the embedding and reranking models hosted by Pinecone. 


        You can use hosted models as an integrated part of Pinecone operations
        or for standalone embedding and reranking. For more details, see [Vector
        embedding](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding)
        and [Rerank
        results](https://docs.pinecone.io/guides/search/rerank-results).
      operationId: list_models
      parameters:
        - in: header
          name: X-Pinecone-Api-Version
          description: Required date-based version header
          required: true
          schema:
            default: 2025-10
            type: string
          style: simple
        - in: query
          name: type
          description: Filter models by type ('embed' or 'rerank').
          schema:
            description: |-
              Filter models by type.
              Possible values: `embed` or `rerank`.
            x-enum:
              - embed
              - rerank
            type: string
          example: embed
          style: form
        - in: query
          name: vector_type
          description: >-
            Filter embedding models by vector type ('dense' or 'sparse'). Only
            relevant when `type=embed`.
          schema:
            description: |-
              Filter models by vector type.
              Possible values: `dense` or `sparse`.
            x-enum:
              - dense
              - sparse
            type: string
          example: sparse
          style: form
      responses:
        '200':
          description: The list of available models.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelInfoList'
              examples:
                multiple-models:
                  summary: Multiple available models.
                  value:
                    models:
                      - default_dimension: 256
                        max_batch_size: 96
                        max_sequence_length: 512
                        modality: text
                        model: example-embedding-model
                        provider_name: Embedding Model Provider
                        short_description: An example embedding model.
                        supported_dimensions:
                          - 256
                          - 512
                        supported_metrics:
                          - cosine
                          - euclidean
                        supported_parameters:
                          - allowed_values:
                              - value1
                              - value2
                            parameter: example_required_param
                            required: true
                            type: one_of
                            value_type: string
                          - allowed_values:
                              - value1
                              - value2
                            default: value1
                            parameter: example_param_with_default
                            required: false
                            type: one_of
                            value_type: string
                          - default: 5
                            max: 10
                            min: 0
                            parameter: example_numeric_range
                            required: false
                            type: numeric_range
                            value_type: integer
                        type: embed
                        vector_type: dense
                      - max_batch_size: 100
                        max_sequence_length: 1024
                        modality: text
                        model: example-reranking-model
                        provider_name: Reranking Model Provider
                        short_description: An example reranking model.
                        supported_parameters:
                          - default: true
                            parameter: example_any_value
                            required: false
                            type: any
                            value_type: boolean
                        type: rerank
        '401':
          description: 'Unauthorized. Possible causes: Invalid API key.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                unauthorized:
                  summary: Unauthorized
                  value:
                    error:
                      code: UNAUTHENTICATED
                      message: Invalid API key.
                    status: 401
        '404':
          description: Model not found.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                model-not-found:
                  summary: Model not found
                  value:
                    error:
                      code: NOT_FOUND
                      message: Model example-model not found.
                    status: 404
        '500':
          description: Internal server error.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                internal-server-error:
                  summary: Internal server error
                  value:
                    error:
                      code: UNKNOWN
                      message: Internal server error
                    status: 500
components:
  schemas:
    ModelInfoList:
      description: The list of available models.
      type: object
      properties:
        models:
          description: List of available models.
          type: array
          items:
            $ref: '#/components/schemas/ModelInfo'
    ErrorResponse:
      example:
        error:
          code: QUOTA_EXCEEDED
          message: >-
            The index exceeds the project quota of 5 pods by 2 pods. Upgrade
            your account or change the project settings to increase the quota.
        status: 429
      description: The response shape used for all error responses.
      type: object
      properties:
        status:
          example: 500
          description: The HTTP status code of the error.
          type: integer
        error:
          example:
            code: INVALID_ARGUMENT
            message: >-
              Index name must contain only lowercase alphanumeric characters or
              hyphens, and must not begin or end with a hyphen.
          description: Detailed information about the error that occurred.
          type: object
          properties:
            code:
              description: >-
                The error code.

                Possible values: `OK`, `UNKNOWN`, `INVALID_ARGUMENT`,
                `DEADLINE_EXCEEDED`, `QUOTA_EXCEEDED`, `NOT_FOUND`,
                `ALREADY_EXISTS`, `PERMISSION_DENIED`, `UNAUTHENTICATED`,
                `RESOURCE_EXHAUSTED`, `FAILED_PRECONDITION`, `ABORTED`,
                `OUT_OF_RANGE`, `UNIMPLEMENTED`, `INTERNAL`, `UNAVAILABLE`,
                `DATA_LOSS`, or `FORBIDDEN`.
              x-enum:
                - OK
                - UNKNOWN
                - INVALID_ARGUMENT
                - DEADLINE_EXCEEDED
                - QUOTA_EXCEEDED
                - NOT_FOUND
                - ALREADY_EXISTS
                - PERMISSION_DENIED
                - UNAUTHENTICATED
                - RESOURCE_EXHAUSTED
                - FAILED_PRECONDITION
                - ABORTED
                - OUT_OF_RANGE
                - UNIMPLEMENTED
                - INTERNAL
                - UNAVAILABLE
                - DATA_LOSS
                - FORBIDDEN
              type: string
            message:
              example: >-
                Index name must contain only lowercase alphanumeric characters
                or hyphens, and must not begin or end with a hyphen.
              description: A human-readable error message describing the error.
              type: string
            details:
              description: >-
                Additional information about the error. This field is not
                guaranteed to be present.
              type: object
          required:
            - code
            - message
      required:
        - status
        - error
    ModelInfo:
      description: >-
        Represents the model configuration including model type, supported
        parameters, and other model details.
      type: object
      properties:
        model:
          example: multilingual-e5-large
          description: The name of the model.
          type: string
        short_description:
          example: multilingual-e5-large
          description: A summary of the model.
          type: string
        type:
          example: embed
          description: The type of model (e.g. 'embed' or 'rerank').
          type: string
        vector_type:
          description: Whether the embedding model produces 'dense' or 'sparse' embeddings.
          type: string
        default_dimension:
          example: 1024
          description: >-
            The default embedding model dimension (applies to dense embedding
            models only).
          type: integer
          format: int32
          minimum: 1
          maximum: 20000
        modality:
          example: text
          description: The modality of the model (e.g. 'text').
          type: string
        max_sequence_length:
          example: 512
          description: The maximum tokens per sequence supported by the model.
          type: integer
          format: int32
          minimum: 1
        max_batch_size:
          example: 96
          description: The maximum batch size (number of sequences) supported by the model.
          type: integer
          format: int32
          minimum: 1
        provider_name:
          example: NVIDIA
          description: The name of the provider of the model.
          type: string
        supported_dimensions:
          description: >-
            The list of supported dimensions for the model (applies to dense
            embedding models only).
          type: array
          items:
            example: 1024
            type: integer
            format: int32
            minimum: 1
            maximum: 20000
        supported_metrics:
          $ref: '#/components/schemas/ModelInfoSupportedMetrics'
        supported_parameters:
          description: List of parameters supported by the model.
          type: array
          items:
            $ref: '#/components/schemas/ModelInfoSupportedParameter'
      required:
        - model
        - short_description
        - type
        - supported_parameters
    ModelInfoSupportedMetrics:
      description: The distance metrics supported by the model for similarity search.
      type: array
      items:
        $ref: '#/components/schemas/ModelInfoMetric'
    ModelInfoSupportedParameter:
      description: >-
        Describes a parameter supported by the model, including parameter value
        constraints.
      type: object
      properties:
        parameter:
          example: input_type
          description: The name of the parameter.
          type: string
        type:
          example: one_of
          description: >-
            The parameter type e.g. 'one_of', 'numeric_range', or 'any'.


            If the type is 'one_of', then 'allowed_values' will be set, and the
            value specified must be one of the allowed values. 'one_of' is only
            compatible with value_type 'string' or 'integer'.


            If 'numeric_range', then 'min' and 'max' will be set, then the value
            specified must adhere to the value_type and must fall within the
            `[min, max]` range (inclusive).


            If 'any' then any value is allowed, as long as it adheres to the
            value_type.
          type: string
        value_type:
          example: string
          description: >-
            The type of value the parameter accepts, e.g. 'string', 'integer',
            'float', or 'boolean'.
          type: string
        required:
          example: true
          description: Whether the parameter is required (true) or optional (false).
          type: boolean
        allowed_values:
          description: The allowed parameter values when the type is 'one_of'.
          type: array
          items:
            anyOf:
              - type: string
              - type: integer
        min:
          example: 1
          description: >-
            The minimum allowed value (inclusive) when the type is
            'numeric_range'.
          type: number
        max:
          example: 1
          description: >-
            The maximum allowed value (inclusive) when the type is
            'numeric_range'.
          type: number
        default:
          example: END
          description: The default value for the parameter when a parameter is optional.
          anyOf:
            - type: string
            - type: integer
              format: int32
            - type: number
              format: float
            - type: boolean
      required:
        - parameter
        - type
        - value_type
        - required
    ModelInfoMetric:
      description: >-
        A distance metric that the embedding model supports for similarity
        searches.

        Possible values: `cosine`, `euclidean`, or `dotproduct`.
      x-enum:
        - cosine
        - euclidean
        - dotproduct
      type: string
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: >-
        An API Key is required to call Pinecone APIs. Get yours from the
        [console](https://app.pinecone.io/).

````