# Source: https://docs.venice.ai/api-reference/endpoint/models/list.md

# List Models

> Returns a list of available models supported by the Venice.ai API for both text and image inference.

## OpenAPI

````yaml GET /models
paths:
  path: /models
  method: get
  servers:
    - url: https://api.venice.ai/api/v1
  request:
    security:
      - title: ''
        parameters:
          query: {}
          header: {}
          cookie: {}
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path: {}
      query:
        type:
          schema:
            - type: enum<string>
              enum:
                - asr
                - embedding
                - image
                - text
                - tts
                - upscale
                - inpaint
                - video
              required: false
              description: Filter models by type. Use "all" to get all model types.
              example: text
            - type: enum<string>
              enum:
                - all
                - code
              required: false
              description: Filter models by type. Use "all" to get all model types.
              example: text
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/ModelResponse'
                    description: List of available models
              object:
                allOf:
                  - type: string
                    enum:
                      - list
              type:
                allOf:
                  - anyOf:
                      - type: string
                        enum:
                          - asr
                          - embedding
                          - image
                          - text
                          - tts
                          - upscale
                          - inpaint
                          - video
                      - type: string
                        enum:
                          - all
                          - code
                    description: Type of models returned.
                    example: text
            requiredProperties:
              - data
              - object
              - type
        examples:
          example:
            value:
              data:
                - created: 1727966436
                  id: llama-3.2-3b
                  model_spec:
                    availableContextTokens: 131072
                    capabilities:
                      optimizedForCode: false
                      quantization: fp16
                      supportsFunctionCalling: true
                      supportsReasoning: false
                      supportsResponseSchema: true
                      supportsVision: false
                      supportsWebSearch: true
                      supportsLogProbs: true
                    constraints:
                      temperature:
                        default: 0.8
                      top_p:
                        default: 0.9
                    name: Llama 3.2 3B
                    modelSource: https://huggingface.co/meta-llama/Llama-3.2-3B
                    offline: false
                    pricing:
                      input:
                        usd: 0.15
                        diem: 0.15
                      output:
                        usd: 0.6
                        diem: 0.6
                    traits:
                      - fastest
                  object: model
                  owned_by: venice.ai
                  type: text
              object: list
              type: text
        description: OK
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: A description of the error
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties:
              - error
        examples:
          example:
            value:
              error: <string>
        description: An unknown error occurred
  deprecated: false
  type: path
components:
  schemas:
    ModelResponse:
      type: object
      properties:
        created:
          type: number
          description: Release date on Venice API
          example: 1699000000
        id:
          type: string
          description: Model ID
          example: venice-uncensored
        model_spec:
          type: object
          properties:
            availableContextTokens:
              type: number
              description: >-
                The context length supported by the model. Only applicable for
                text models.
              example: 32768
            beta:
              type: boolean
              description: Is this model in beta?
              example: false
            capabilities:
              type: object
              properties:
                optimizedForCode:
                  type: boolean
                  description: Is the LLM optimized for coding?
                  example: true
                quantization:
                  type: string
                  enum:
                    - fp4
                    - fp8
                    - fp16
                    - bf16
                    - not-available
                  description: The quantization type of the running model.
                  example: fp8
                supportsFunctionCalling:
                  type: boolean
                  description: Does the LLM model support function calling?
                  example: true
                supportsReasoning:
                  type: boolean
                  description: >-
                    Does the model support reasoning with <thinking> blocks of
                    output.
                  example: true
                supportsResponseSchema:
                  type: boolean
                  description: >-
                    Does the LLM model support response schema? Only models that
                    support function calling can support response_schema.
                  example: true
                supportsVision:
                  type: boolean
                  description: Does the LLM support vision?
                  example: true
                supportsWebSearch:
                  type: boolean
                  description: Does the LLM model support web search?
                  example: true
                supportsLogProbs:
                  type: boolean
                  description: Does the LLM model support logprobs parameter?
                  example: true
              required:
                - optimizedForCode
                - quantization
                - supportsFunctionCalling
                - supportsReasoning
                - supportsResponseSchema
                - supportsVision
                - supportsWebSearch
                - supportsLogProbs
              additionalProperties: false
              description: Text model specific capabilities.
            constraints:
              anyOf:
                - type: object
                  properties:
                    promptCharacterLimit:
                      type: number
                      description: The maximum supported prompt length.
                      example: 2048
                    steps:
                      type: object
                      properties:
                        default:
                          type: number
                          description: The default steps value for the model
                          example: 25
                        max:
                          type: number
                          description: The maximum supported steps value for the model
                          example: 50
                      required:
                        - default
                        - max
                    widthHeightDivisor:
                      type: number
                      description: >-
                        The requested width and height of the image generation
                        must be divisible by this value.
                      example: 8
                  required:
                    - promptCharacterLimit
                    - steps
                    - widthHeightDivisor
                  description: Constraints that apply to image models.
                  title: Image Model Constraints
                - type: object
                  properties:
                    temperature:
                      type: object
                      properties:
                        default:
                          type: number
                          description: The default temperature value for the model
                          example: 0.7
                      required:
                        - default
                    top_p:
                      type: object
                      properties:
                        default:
                          type: number
                          description: The default top_p value for the model
                          example: 0.9
                      required:
                        - default
                  required:
                    - temperature
                    - top_p
                  description: Constraints that apply to text models.
                  title: Text Model Constraints
              description: Constraints that apply to this model.
            name:
              type: string
              description: The name of the model.
              example: Venice Uncensored 1.1
            modelSource:
              type: string
              description: The source of the model, such as a URL to the model repository.
              example: >-
                https://huggingface.co/cognitivecomputations/Dolphin-Mistral-24B-Venice-Edition
            offline:
              type: boolean
              default: false
              description: Is this model presently offline?
              example: false
            pricing:
              anyOf:
                - type: object
                  properties:
                    input:
                      type: object
                      properties:
                        usd:
                          type: number
                          description: USD cost per million input tokens
                          example: 0.7
                        diem:
                          type: number
                          description: Diem cost per million input tokens
                          example: 7
                      required:
                        - usd
                        - diem
                    output:
                      type: object
                      properties:
                        usd:
                          type: number
                          description: USD cost per million output tokens
                          example: 2.8
                        diem:
                          type: number
                          description: Diem cost per million output tokens
                          example: 28
                      required:
                        - usd
                        - diem
                  required:
                    - input
                    - output
                  description: Token-based pricing for chat models
                  title: LLM Model Pricing
                - type: object
                  properties:
                    generation:
                      type: object
                      properties:
                        usd:
                          type: number
                          description: USD cost per image generation
                          example: 0.01
                        diem:
                          type: number
                          description: Diem cost per image generation
                          example: 0.1
                      required:
                        - usd
                        - diem
                    upscale:
                      type: object
                      properties:
                        2x:
                          type: object
                          properties:
                            usd:
                              type: number
                              description: USD cost for 2x upscale
                              example: 0.02
                            diem:
                              type: number
                              description: Diem cost for 2x upscale
                              example: 0.2
                          required:
                            - usd
                            - diem
                        4x:
                          type: object
                          properties:
                            usd:
                              type: number
                              description: USD cost for 4x upscale
                              example: 0.08
                            diem:
                              type: number
                              description: Diem cost for 4x upscale
                              example: 0.8
                          required:
                            - usd
                            - diem
                      required:
                        - 2x
                        - 4x
                  required:
                    - generation
                    - upscale
                  description: Pricing for image generation and upscaling
                  title: Image Model Pricing
                - type: object
                  properties:
                    input:
                      type: object
                      properties:
                        usd:
                          type: number
                          description: USD cost per million input characters
                          example: 3.5
                        diem:
                          type: number
                          description: Diem cost per million input characters
                          example: 35
                      required:
                        - usd
                        - diem
                  required:
                    - input
                  description: Pricing for audio models (TTS)
                  title: Audio Model Pricing
              description: Pricing details for the model
            traits:
              type: array
              items:
                type: string
              description: >-
                Traits that apply to this model. You can specify a trait to
                auto-select a model vs. specifying the model ID in your request
                to avoid breakage as Venice updates and iterates on its models.
              example:
                - default_code
            voices:
              type: array
              items:
                type: string
              description: >-
                The voices available for this TTS model. Only applicable for TTS
                models.
              example:
                - af_alloy
                - af_aoede
                - af_bella
                - af_heart
                - af_jadzia
        object:
          type: string
          enum:
            - model
          description: Object type
          example: model
        owned_by:
          type: string
          enum:
            - venice.ai
          description: Who runs the model
          example: venice.ai
        type:
          type: string
          enum:
            - asr
            - embedding
            - image
            - text
            - tts
            - upscale
            - inpaint
            - video
          description: Model type
          example: text
      required:
        - id
        - model_spec
        - object
        - owned_by
        - type
      description: Response schema for model information
      example:
        created: 1727966436
        id: llama-3.2-3b
        model_spec:
          availableContextTokens: 131072
          capabilities:
            optimizedForCode: false
            quantization: fp16
            supportsFunctionCalling: true
            supportsReasoning: false
            supportsResponseSchema: true
            supportsVision: false
            supportsWebSearch: true
            supportsLogProbs: true
          constraints:
            temperature:
              default: 0.8
            top_p:
              default: 0.9
          name: Llama 3.2 3B
          modelSource: https://huggingface.co/meta-llama/Llama-3.2-3B
          offline: false
          pricing:
            input:
              usd: 0.15
              diem: 0.15
            output:
              usd: 0.6
              diem: 0.6
          traits:
            - fastest
        object: model
        owned_by: venice.ai
        type: text

````