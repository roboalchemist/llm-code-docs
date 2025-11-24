# Source: https://docs.ollama.com/api/tags.md

# List models

> Fetch a list of models and their details

## OpenAPI

````yaml openapi.yaml get /api/tags
paths:
  path: /api/tags
  method: get
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
    body: {}
    codeSamples:
      - label: List models
        lang: bash
        source: |
          curl http://localhost:11434/api/tags
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              models:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/ModelSummary'
            refIdentifier: '#/components/schemas/ListResponse'
        examples:
          example:
            value:
              models:
                - name: gemma3
                  modified_at: '2025-10-03T23:34:03.409490317-07:00'
                  size: 3338801804
                  digest: >-
                    a2af6cc3eb7fa8be8504abaf9b04e88f17a119ec3f04a3addf55f92841195f5a
                  details:
                    format: gguf
                    family: gemma
                    families:
                      - gemma
                    parameter_size: 4.3B
                    quantization_level: Q4_K_M
        description: List available models
  deprecated: false
  type: path
  xMint:
    href: /api/tags
components:
  schemas:
    ModelSummary:
      type: object
      description: Summary information for a locally available model
      properties:
        name:
          type: string
          description: Model name
        modified_at:
          type: string
          description: Last modified timestamp in ISO 8601 format
        size:
          type: integer
          description: Total size of the model on disk in bytes
        digest:
          type: string
          description: SHA256 digest identifier of the model contents
        details:
          type: object
          description: Additional information about the model's format and family
          properties:
            format:
              type: string
              description: Model file format (for example `gguf`)
            family:
              type: string
              description: Primary model family (for example `llama`)
            families:
              type: array
              items:
                type: string
              description: All families the model belongs to, when applicable
            parameter_size:
              type: string
              description: Approximate parameter count label (for example `7B`, `13B`)
            quantization_level:
              type: string
              description: Quantization level used (for example `Q4_0`)

````