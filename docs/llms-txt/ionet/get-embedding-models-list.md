# Source: https://io.net/docs/reference/ai-models/get-embedding-models-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Embedding Models List

> Retrieves a list of available models for the Embeddings API.



## OpenAPI

````yaml openapi/ai-models/get-embedding-models-list.json get /api/v1/embedding-models
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/v1/embedding-models:
    get:
      tags:
        - OpenAI Compatible Developer API
      summary: Get Embedding Models List
      operationId: get_embedding_models_list_v1_embedding_models_get
      parameters:
        - name: token
          in: header
          required: false
          schema:
            type: string
            description: JWT token
            title: Token
          description: JWT token
        - name: Authorization
          in: header
          required: false
          schema:
            type: string
            description: io.net provided API Key
            title: Authorization
          description: io.net provided API Key
        - name: x-api-key
          in: header
          required: false
          schema:
            type: string
            description: API key set by an SDK client
            title: X-Api-Key
          description: API key set by an SDK client
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelList'
        '404':
          description: Not found
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    ModelList:
      properties:
        object:
          type: string
          title: Object
          default: list
        data:
          items:
            $ref: '#/components/schemas/ModelCard'
          type: array
          title: Data
      additionalProperties: true
      type: object
      title: ModelList
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ModelCard:
      properties:
        id:
          type: string
          title: Id
        object:
          type: string
          title: Object
          default: model
        created:
          type: integer
          title: Created
        owned_by:
          type: string
          title: Owned By
          default: io-intelligence
        root:
          anyOf:
            - type: string
            - type: 'null'
          title: Root
        parent:
          anyOf:
            - type: string
            - type: 'null'
          title: Parent
        max_model_len:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Model Len
        permission:
          items:
            $ref: '#/components/schemas/ModelPermission'
          type: array
          title: Permission
        max_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Tokens
          description: Maximum number of tokens that can be generated in a single response
        context_window:
          anyOf:
            - type: integer
            - type: 'null'
          title: Context Window
          description: >-
            Maximum number of tokens that can be processed in the model's
            context window
        supports_images_input:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Supports Images Input
          description: Whether the model supports image inputs for multimodal processing
        supports_prompt_cache:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Supports Prompt Cache
          description: Whether the model supports prompt caching to improve performance
        input_token_price:
          anyOf:
            - type: number
            - type: 'null'
          title: Input Token Price
          description: Price per token for input processing (in dollars)
        output_token_price:
          anyOf:
            - type: number
            - type: 'null'
          title: Output Token Price
          description: Price per token for output generation (in dollars)
        cache_write_token_price:
          anyOf:
            - type: number
            - type: 'null'
          title: Cache Write Token Price
          description: Price per token for writing to prompt cache (in dollars)
        cache_read_token_price:
          anyOf:
            - type: number
            - type: 'null'
          title: Cache Read Token Price
          description: Price per token for reading from prompt cache (in dollars)
        precision:
          anyOf:
            - type: string
            - type: 'null'
          title: Precision
          description: Model precision type (e.g., 'fp16', 'fp32', 'int8', 'int4')
      additionalProperties: true
      type: object
      required:
        - id
      title: ModelCard
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    ModelPermission:
      properties:
        id:
          type: string
          title: Id
        object:
          type: string
          title: Object
          default: model_permission
        created:
          type: integer
          title: Created
        allow_create_engine:
          type: boolean
          title: Allow Create Engine
          default: false
        allow_sampling:
          type: boolean
          title: Allow Sampling
          default: true
        allow_logprobs:
          type: boolean
          title: Allow Logprobs
          default: true
        allow_search_indices:
          type: boolean
          title: Allow Search Indices
          default: false
        allow_view:
          type: boolean
          title: Allow View
          default: true
        allow_fine_tuning:
          type: boolean
          title: Allow Fine Tuning
          default: false
        organization:
          type: string
          title: Organization
          default: '*'
        group:
          anyOf:
            - type: string
            - type: 'null'
          title: Group
        is_blocking:
          type: boolean
          title: Is Blocking
          default: false
      additionalProperties: true
      type: object
      title: ModelPermission
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````