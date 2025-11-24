# Source: https://docs.ollama.com/api/delete.md

# Delete a model

## OpenAPI

````yaml openapi.yaml delete /api/delete
paths:
  path: /api/delete
  method: delete
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
                    description: Model name to delete
            required: true
            refIdentifier: '#/components/schemas/DeleteRequest'
            requiredProperties:
              - model
        examples:
          example:
            value:
              model: gemma3
    codeSamples:
      - label: Delete model
        lang: bash
        source: |
          curl -X DELETE http://localhost:11434/api/delete -d '{
            "model": "gemma3"
          }'
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Model successfully deleted
        examples: {}
        description: Model successfully deleted
  deprecated: false
  type: path
  xMint:
    href: /api/delete
components:
  schemas: {}

````