# Source: https://docs.ollama.com/api/create.md

# Create a model

## OpenAPI

````yaml openapi.yaml post /api/create
paths:
  path: /api/create
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
                    description: Name for the model to create
              from:
                allOf:
                  - type: string
                    description: Existing model to create from
              template:
                allOf:
                  - type: string
                    description: Prompt template to use for the model
              license:
                allOf:
                  - oneOf:
                      - type: string
                      - type: array
                        items:
                          type: string
                    description: License string or list of licenses for the model
              system:
                allOf:
                  - type: string
                    description: System prompt to embed in the model
              parameters:
                allOf:
                  - type: object
                    description: Key-value parameters for the model
              messages:
                allOf:
                  - description: Message history to use for the model
                    type: array
                    items:
                      $ref: '#/components/schemas/ChatMessage'
              quantize:
                allOf:
                  - type: string
                    description: Quantization level to apply (e.g. `q4_K_M`, `q8_0`)
              stream:
                allOf:
                  - type: boolean
                    default: true
                    description: Stream status updates
            required: true
            refIdentifier: '#/components/schemas/CreateRequest'
            requiredProperties:
              - model
        examples:
          example:
            value:
              model: mario
              from: gemma3
              system: You are Mario from Super Mario Bros.
    codeSamples:
      - label: Default
        lang: bash
        source: |
          curl http://localhost:11434/api/create -d '{
            "from": "gemma3",
            "model": "alpaca",
            "system": "You are Alpaca, a helpful AI assistant. You only answer with Emojis."
          }'
      - label: Create from existing
        lang: bash
        source: |
          curl http://localhost:11434/api/create -d '{
            "model": "ollama",
            "from": "gemma3",
            "system": "You are Ollama the llama."
          }'
      - label: Quantize
        lang: bash
        source: |
          curl http://localhost:11434/api/create -d '{
            "model": "llama3.1:8b-instruct-Q4_K_M",
            "from": "llama3.1:8b-instruct-fp16",
            "quantize": "q4_K_M"
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
        description: Stream of create status updates
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
        description: Stream of create status updates
  deprecated: false
  type: path
  xMint:
    href: /api/create
components:
  schemas:
    ChatMessage:
      type: object
      required:
        - role
        - content
      properties:
        role:
          type: string
          enum:
            - system
            - user
            - assistant
            - tool
          description: Author of the message.
        content:
          type: string
          description: Message text content
        images:
          type: array
          items:
            type: string
            description: Base64-encoded image content
          description: Optional list of inline images for multimodal models
        tool_calls:
          type: array
          items:
            $ref: '#/components/schemas/ToolCall'
          description: Tool call requests produced by the model
    ToolCall:
      type: object
      properties:
        function:
          type: object
          required:
            - name
          properties:
            name:
              type: string
              description: Name of the function to call
            description:
              type: string
              description: What the function does
            arguments:
              type: object
              description: JSON object of arguments to pass to the function

````