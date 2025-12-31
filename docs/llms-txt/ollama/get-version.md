# Source: https://docs.ollama.com/api-reference/get-version.md

# Get version

> Retrieve the version of the Ollama

## OpenAPI

````yaml openapi.yaml get /api/version
paths:
  path: /api/version
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
      - label: Default
        lang: bash
        source: |
          curl http://localhost:11434/api/version
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              version:
                allOf:
                  - type: string
                    description: Version of Ollama
            refIdentifier: '#/components/schemas/VersionResponse'
        examples:
          example:
            value:
              version: 0.12.6
        description: Version information
  deprecated: false
  type: path
components:
  schemas: {}

````