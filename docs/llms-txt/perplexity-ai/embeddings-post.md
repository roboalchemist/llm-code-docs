# Source: https://docs.perplexity.ai/api-reference/embeddings-post.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Embeddings

> Generate embeddings for a list of texts. Use these embeddings for semantic search, clustering, and other machine learning applications.



## OpenAPI

````yaml post /v1/embeddings
openapi: 3.1.0
info:
  title: Perplexity AI API
  description: Perplexity AI API
  version: 1.0.0
servers:
  - url: https://api.perplexity.ai
    description: Perplexity AI API
security: []
paths:
  /v1/embeddings:
    post:
      summary: Create Embeddings
      description: >-
        Generate embeddings for a list of texts. Use these embeddings for
        semantic search, clustering, and other machine learning applications.
      operationId: embeddings_v1_embeddings_post
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EmbeddingsRequest'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EmbeddingsResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - HTTPBearer: []
components:
  schemas:
    EmbeddingsRequest:
      type: object
      title: Embeddings Request
      description: Request body for creating embeddings
      required:
        - input
        - model
      properties:
        input:
          title: Input
          description: >-
            Input text to embed, encoded as a string or array of strings.
            Maximum 512 texts per request. Each input must not exceed 32K
            tokens. All inputs in a single request must not exceed 120,000
            tokens combined. Empty strings are not allowed.
          oneOf:
            - type: string
              minLength: 1
            - type: array
              items:
                type: string
                minLength: 1
              minItems: 1
              maxItems: 512
        model:
          type: string
          title: Model
          description: The embedding model to use
          enum:
            - pplx-embed-v1-0.6b
            - pplx-embed-v1-4b
        dimensions:
          type: integer
          title: Dimensions
          description: >-
            Number of dimensions for output embeddings (Matryoshka). Range:
            128-1024 for pplx-embed-v1-0.6b, 128-2560 for pplx-embed-v1-4b.
            Defaults to full dimensions (1024 or 2560).
          minimum: 128
          maximum: 2560
        encoding_format:
          type: string
          title: Encoding Format
          description: >-
            Output encoding format for embeddings. base64_int8 returns
            base64-encoded signed int8 values. base64_binary returns
            base64-encoded packed binary (1 bit per dimension).
          enum:
            - base64_int8
            - base64_binary
          default: base64_int8
    EmbeddingsResponse:
      type: object
      title: Embeddings Response
      description: Response body for embeddings request
      properties:
        object:
          type: string
          title: Object
          description: The object type
          example: list
        data:
          type: array
          title: Data
          description: List of embedding objects
          items:
            $ref: '#/components/schemas/EmbeddingObject'
        model:
          type: string
          title: Model
          description: The model used to generate embeddings
        usage:
          $ref: '#/components/schemas/EmbeddingsUsage'
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    EmbeddingObject:
      type: object
      title: Embedding Object
      description: A single embedding result
      properties:
        object:
          type: string
          title: Object
          description: The object type
          example: embedding
        index:
          type: integer
          title: Index
          description: The index of the input text this embedding corresponds to
        embedding:
          type: string
          title: Embedding
          description: >-
            Base64-encoded embedding vector. For base64_int8: decode to signed
            int8 array (length = dimensions). For base64_binary: decode to
            packed bits (length = dimensions / 8 bytes).
    EmbeddingsUsage:
      type: object
      title: Embeddings Usage
      description: Token usage for the embeddings request
      properties:
        prompt_tokens:
          type: integer
          title: Prompt Tokens
          description: Number of tokens in the input texts
        total_tokens:
          type: integer
          title: Total Tokens
          description: Total number of tokens processed
        cost:
          type: object
          title: Cost
          description: Cost breakdown for the request
          properties:
            input_cost:
              type: number
              title: Input Cost
              description: Cost for input tokens in USD
            total_cost:
              type: number
              title: Total Cost
              description: Total cost for the request in USD
            currency:
              type: string
              title: Currency
              description: Currency of the cost values
              enum:
                - USD
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
  securitySchemes:
    HTTPBearer:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).