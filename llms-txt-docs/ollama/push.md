# Source: https://docs.ollama.com/api/push.md

# Push a model

## OpenAPI

````yaml openapi.yaml post /api/push
paths:
  path: /api/push
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
                    description: Name of the model to publish
              insecure:
                allOf:
                  - type: boolean
                    description: Allow publishing over insecure connections
              stream:
                allOf:
                  - type: boolean
                    default: true
                    description: Stream progress updates
            required: true
            refIdentifier: '#/components/schemas/PushRequest'
            requiredProperties:
              - model
        examples:
          example:
            value:
              model: my-username/my-model
    codeSamples:
      - label: Push model
        lang: bash
        source: |
          curl http://localhost:11434/api/push -d '{
            "model": "my-username/my-model"
          }'
      - label: Non-streaming
        lang: bash
        source: |
          curl http://localhost:11434/api/push -d '{
            "model": "my-username/my-model",
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
        description: Push status updates.
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
        description: Push status updates.
  deprecated: false
  type: path
  xMint:
    href: /api/push
components:
  schemas: {}

````