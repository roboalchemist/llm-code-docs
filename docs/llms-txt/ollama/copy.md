# Source: https://docs.ollama.com/api/copy.md

# Copy a model

## OpenAPI

````yaml openapi.yaml post /api/copy
paths:
  path: /api/copy
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
              source:
                allOf:
                  - type: string
                    description: Existing model name to copy from
              destination:
                allOf:
                  - type: string
                    description: New model name to create
            required: true
            refIdentifier: '#/components/schemas/CopyRequest'
            requiredProperties:
              - source
              - destination
        examples:
          example:
            value:
              source: gemma3
              destination: gemma3-backup
    codeSamples:
      - label: Copy a model to a new name
        lang: bash
        source: |
          curl http://localhost:11434/api/copy -d '{
            "source": "gemma3",
            "destination": "gemma3-backup"
          }'
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Model successfully copied
        examples: {}
        description: Model successfully copied
  deprecated: false
  type: path
  xMint:
    href: /api/copy
components:
  schemas: {}

````