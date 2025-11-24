# Source: https://docs.ollama.com/api/pull.md

# Pull a model

## OpenAPI

````yaml openapi.yaml post /api/pull
paths:
  path: /api/pull
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
                    description: Name of the model to download
              insecure:
                allOf:
                  - type: boolean
                    description: Allow downloading over insecure connections
              stream:
                allOf:
                  - type: boolean
                    default: true
                    description: Stream progress updates
            required: true
            refIdentifier: '#/components/schemas/PullRequest'
            requiredProperties:
              - model
        examples:
          example:
            value:
              model: gemma3
    codeSamples:
      - label: Default
        lang: bash
        source: |
          curl http://localhost:11434/api/pull -d '{
            "model": "gemma3"
          }'
      - label: Non-streaming
        lang: bash
        source: |
          curl http://localhost:11434/api/pull -d '{
            "model": "gemma3",
            "stream": false
          }'
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: string
                    description: Current status message
            refIdentifier: '#/components/schemas/StatusResponse'
        examples:
          example:
            value:
              status: success
        description: Pull status updates.
      application/x-ndjson:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: string
                    description: Human-readable status message
              digest:
                allOf:
                  - type: string
                    description: Content digest associated with the status, if applicable
              total:
                allOf:
                  - type: integer
                    description: Total number of bytes expected for the operation
              completed:
                allOf:
                  - type: integer
                    description: Number of bytes transferred so far
            refIdentifier: '#/components/schemas/StatusEvent'
        examples:
          example:
            value:
              status: success
        description: Pull status updates.
  deprecated: false
  type: path
  xMint:
    href: /api/pull
components:
  schemas: {}

````