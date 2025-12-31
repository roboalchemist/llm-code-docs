# Source: https://docs.ollama.com/api/embed.md

# Generate embeddings

> Creates vector embeddings representing the input text

## OpenAPI

````yaml openapi.yaml post /api/embed
paths:
  path: /api/embed
  method: post
  servers:
    - url: http://localhost:11434
      description: Ollama
  request:
    security: []
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              model:
                allOf:
                  - type: string
                    description: Model name
              input:
                allOf:
                  - oneOf:
                      - type: string
                      - type: array
                        items:
                          type: string
                    description: Text or array of texts to generate embeddings for
              truncate:
                allOf:
                  - type: boolean
                    default: true
                    description: >-
                      If true, truncate inputs that exceed the context window.
                      If false, returns an error.
              dimensions:
                allOf:
                  - type: integer
                    description: Number of dimensions to generate embeddings for
              keep_alive:
                allOf:
                  - type: string
                    description: Model keep-alive duration
              options:
                allOf:
                  - $ref: '#/components/schemas/ModelOptions'
            required: true
            refIdentifier: '#/components/schemas/EmbedRequest'
            requiredProperties:
              - model
              - input
        examples:
          example:
            value:
              model: embeddinggemma
              input: Generate embeddings for this text
    codeSamples:
      - label: Default
        lang: bash
        source: |
          curl http://localhost:11434/api/embed -d '{
            "model": "embeddinggemma",
            "input": "Why is the sky blue?"
          }'
      - label: Multiple inputs
        lang: bash
        source: |
          curl http://localhost:11434/api/embed -d '{
            "model": "embeddinggemma",
            "input": [
              "Why is the sky blue?",
              "Why is the grass green?"
            ]
          }'
      - label: Truncation
        lang: bash
        source: |
          curl http://localhost:11434/api/embed -d '{
            "model": "embeddinggemma",
            "input": "Generate embeddings for this text",
            "truncate": true
          }'
      - label: Dimensions
        lang: bash
        source: |
          curl http://localhost:11434/api/embed -d '{
            "model": "embeddinggemma",
            "input": "Generate embeddings for this text",
            "dimensions": 128
          }'
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              model:
                allOf:
                  - type: string
                    description: Model that produced the embeddings
              embeddings:
                allOf:
                  - type: array
                    items:
                      type: array
                      items:
                        type: number
                    description: Array of vector embeddings
              total_duration:
                allOf:
                  - type: integer
                    description: Total time spent generating in nanoseconds
              load_duration:
                allOf:
                  - type: integer
                    description: Load time in nanoseconds
              prompt_eval_count:
                allOf:
                  - type: integer
                    description: Number of input tokens processed to generate embeddings
            refIdentifier: '#/components/schemas/EmbedResponse'
        examples:
          example:
            value:
              model: embeddinggemma
              embeddings:
                - - 0.010071029
                  - -0.0017594862
                  - 0.05007221
                  - 0.04692972
                  - 0.054916814
                  - 0.008599704
                  - 0.105441414
                  - -0.025878139
                  - 0.12958129
                  - 0.031952348
              total_duration: 14143917
              load_duration: 1019500
              prompt_eval_count: 8
        description: Vector embeddings for the input text
  deprecated: false
  type: path
  xMint:
    href: /api/embed
components:
  schemas:
    ModelOptions:
      type: object
      description: Runtime options that control text generation
      properties:
        seed:
          type: integer
          description: Random seed used for reproducible outputs
        temperature:
          type: number
          format: float
          description: Controls randomness in generation (higher = more random)
        top_k:
          type: integer
          description: Limits next token selection to the K most likely
        top_p:
          type: number
          format: float
          description: Cumulative probability threshold for nucleus sampling
        min_p:
          type: number
          format: float
          description: Minimum probability threshold for token selection
        stop:
          oneOf:
            - type: string
            - type: array
              items:
                type: string
          description: Stop sequences that will halt generation
        num_ctx:
          type: integer
          description: Context length size (number of tokens)
        num_predict:
          type: integer
          description: Maximum number of tokens to generate
      additionalProperties: true

````