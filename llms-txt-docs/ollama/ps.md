# Source: https://docs.ollama.com/api/ps.md

# List running models

> Retrieve a list of models that are currently running

## OpenAPI

````yaml openapi.yaml get /api/ps
paths:
  path: /api/ps
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
      - label: List running models
        lang: bash
        source: |
          curl http://localhost:11434/api/ps
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
                      $ref: '#/components/schemas/Ps'
                    description: Currently running models
            refIdentifier: '#/components/schemas/PsResponse'
        examples:
          example:
            value:
              models:
                - model: gemma3
                  size: 6591830464
                  digest: >-
                    a2af6cc3eb7fa8be8504abaf9b04e88f17a119ec3f04a3addf55f92841195f5a
                  details:
                    parent_model: ''
                    format: gguf
                    family: gemma3
                    families:
                      - gemma3
                    parameter_size: 4.3B
                    quantization_level: Q4_K_M
                  expires_at: '2025-10-17T16:47:07.93355-07:00'
                  size_vram: 5333539264
                  context_length: 4096
        description: Models currently loaded into memory
  deprecated: false
  type: path
  xMint:
    href: /api/ps
components:
  schemas:
    Ps:
      type: object
      properties:
        model:
          type: string
          description: Name of the running model
        size:
          type: integer
          description: Size of the model in bytes
        digest:
          type: string
          description: SHA256 digest of the model
        details:
          type: object
          description: Model details such as format and family
        expires_at:
          type: string
          description: Time when the model will be unloaded
        size_vram:
          type: integer
          description: VRAM usage in bytes
        context_length:
          type: integer
          description: Context length for the running model

````