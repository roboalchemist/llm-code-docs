# Source: https://docs.helicone.ai/rest/models/get-v1public-model-registry-models.md

# Get Model Registry

> Returns all models and endpoints supported by the Helicone AI Gateway

## OpenAPI

````yaml get /v1/public/model-registry/models
paths:
  path: /v1/public/model-registry/models
  method: get
  servers:
    - url: https://api.helicone.ai/
    - url: http://localhost:8585/
  request:
    security: []
    parameters:
      path: {}
      query: {}
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
                  - $ref: '#/components/schemas/ModelRegistryResponse'
              error:
                allOf:
                  - type: number
                    enum:
                      - null
                    nullable: true
            refIdentifier: '#/components/schemas/ResultSuccess_ModelRegistryResponse_'
            requiredProperties:
              - data
              - error
            additionalProperties: false
          - type: object
            properties:
              data:
                allOf:
                  - type: number
                    enum:
                      - null
                    nullable: true
              error:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/ResultError_string_'
            requiredProperties:
              - data
              - error
            additionalProperties: false
        examples:
          Example 1:
            value:
              models:
                - id: claude-opus-4-1
                  name: 'Anthropic: Claude Opus 4.1'
                  author: anthropic
                  contextLength: 200000
                  endpoints:
                    - provider: anthropic
                      providerSlug: anthropic
                      supportsPtb: true
                      pricing:
                        prompt: 15
                        completion: 75
                        cacheRead: 1.5
                        cacheWrite: 18.75
                  maxOutput: 32000
                  trainingDate: '2025-08-05'
                  description: Most capable Claude model with extended context
                  inputModalities:
                    - null
                  outputModalities:
                    - null
                  supportedParameters:
                    - null
                    - null
                    - null
                    - null
                    - null
                    - null
                    - null
              total: 150
              filters:
                providers:
                  - name: anthropic
                    displayName: Anthropic
                  - name: openai
                    displayName: OpenAI
                  - name: google
                    displayName: Google
                authors:
                  - anthropic
                  - openai
                  - google
                  - meta
                capabilities:
                  - audio
                  - image
                  - thinking
                  - caching
                  - reasoning
        description: Complete model registry with models and filter options
  deprecated: false
  type: path
components:
  schemas:
    ModelProviderName:
      type: string
      enum:
        - baseten
        - anthropic
        - azure
        - bedrock
        - cerebras
        - chutes
        - deepinfra
        - deepseek
        - fireworks
        - google-ai-studio
        - groq
        - helicone
        - mistral
        - nebius
        - novita
        - openai
        - openrouter
        - perplexity
        - vertex
        - xai
      nullable: false
    AuthorName:
      type: string
      enum:
        - anthropic
        - deepseek
        - mistral
        - openai
        - perplexity
        - xai
        - google
        - meta-llama
        - amazon
        - microsoft
        - nvidia
        - qwen
        - moonshotai
        - alibaba
        - zai
        - baidu
        - passthrough
    StandardParameter:
      type: string
      enum:
        - max_tokens
        - max_completion_tokens
        - temperature
        - top_p
        - top_k
        - stop
        - stream
        - frequency_penalty
        - presence_penalty
        - repetition_penalty
        - seed
        - tools
        - tool_choice
        - functions
        - function_call
        - reasoning
        - include_reasoning
        - thinking
        - response_format
        - json_mode
        - truncate
        - min_p
        - logit_bias
        - logprobs
        - top_logprobs
        - structured_outputs
        - verbosity
        - 'n'
    PluginId:
      type: string
      enum:
        - web
      nullable: false
    RateLimits:
      properties:
        rpm:
          type: number
          format: double
        tpm:
          type: number
          format: double
        tpd:
          type: number
          format: double
      type: object
      additionalProperties: false
    ModelPricing:
      properties:
        threshold:
          type: number
          format: double
        input:
          type: number
          format: double
        output:
          type: number
          format: double
        image:
          type: number
          format: double
        cacheMultipliers:
          properties:
            write1h:
              type: number
              format: double
            write5m:
              type: number
              format: double
            cachedInput:
              type: number
              format: double
          required:
            - cachedInput
          type: object
        cacheStoragePerHour:
          type: number
          format: double
        thinking:
          type: number
          format: double
        request:
          type: number
          format: double
        audio:
          type: number
          format: double
        video:
          type: number
          format: double
        web_search:
          type: number
          format: double
      required:
        - threshold
        - input
        - output
      type: object
      additionalProperties: false
    BodyMappingType:
      type: string
      enum:
        - OPENAI
        - NO_MAPPING
        - RESPONSES
    EndpointConfig:
      properties:
        region:
          type: string
        location:
          type: string
        projectId:
          type: string
        baseUri:
          type: string
        deploymentName:
          type: string
        resourceName:
          type: string
        apiVersion:
          type: string
        crossRegion:
          type: boolean
        gatewayMapping:
          $ref: '#/components/schemas/BodyMappingType'
        modelName:
          type: string
        heliconeModelId:
          type: string
        providerModelId:
          type: string
        pricing:
          items:
            $ref: '#/components/schemas/ModelPricing'
          type: array
        contextLength:
          type: number
          format: double
        maxCompletionTokens:
          type: number
          format: double
        ptbEnabled:
          type: boolean
        version:
          type: string
        rateLimits:
          $ref: '#/components/schemas/RateLimits'
        priority:
          type: number
          format: double
      type: object
      additionalProperties: false
    Record_string.EndpointConfig_:
      properties: {}
      additionalProperties:
        $ref: '#/components/schemas/EndpointConfig'
      type: object
      description: Construct a type with a set of properties K of type T
    ResponseFormat:
      type: string
      enum:
        - ANTHROPIC
        - OPENAI
    ModelProviderConfig:
      properties:
        pricing:
          items:
            $ref: '#/components/schemas/ModelPricing'
          type: array
        contextLength:
          type: number
          format: double
        maxCompletionTokens:
          type: number
          format: double
        ptbEnabled:
          type: boolean
        version:
          type: string
        unsupportedParameters:
          items:
            $ref: '#/components/schemas/StandardParameter'
          type: array
        providerModelId:
          type: string
        provider:
          $ref: '#/components/schemas/ModelProviderName'
        author:
          $ref: '#/components/schemas/AuthorName'
        supportedParameters:
          items:
            $ref: '#/components/schemas/StandardParameter'
          type: array
        supportedPlugins:
          items:
            $ref: '#/components/schemas/PluginId'
          type: array
        rateLimits:
          $ref: '#/components/schemas/RateLimits'
        endpointConfigs:
          $ref: '#/components/schemas/Record_string.EndpointConfig_'
        crossRegion:
          type: boolean
        priority:
          type: number
          format: double
        quantization:
          type: string
          enum:
            - fp4
            - fp8
            - fp16
            - bf16
            - int4
        responseFormat:
          $ref: '#/components/schemas/ResponseFormat'
        requireExplicitRouting:
          type: boolean
        providerModelIdAliases:
          items:
            type: string
          type: array
      required:
        - pricing
        - contextLength
        - maxCompletionTokens
        - ptbEnabled
        - providerModelId
        - provider
        - author
        - supportedParameters
        - endpointConfigs
      type: object
      additionalProperties: false
    UserEndpointConfig:
      properties:
        region:
          type: string
        location:
          type: string
        projectId:
          type: string
        baseUri:
          type: string
        deploymentName:
          type: string
        resourceName:
          type: string
        apiVersion:
          type: string
        crossRegion:
          type: boolean
        gatewayMapping:
          $ref: '#/components/schemas/BodyMappingType'
        modelName:
          type: string
        heliconeModelId:
          type: string
      type: object
      additionalProperties: false
    Endpoint:
      properties:
        pricing:
          items:
            $ref: '#/components/schemas/ModelPricing'
          type: array
        contextLength:
          type: number
          format: double
        maxCompletionTokens:
          type: number
          format: double
        ptbEnabled:
          type: boolean
        version:
          type: string
        unsupportedParameters:
          items:
            $ref: '#/components/schemas/StandardParameter'
          type: array
        modelConfig:
          $ref: '#/components/schemas/ModelProviderConfig'
        userConfig:
          $ref: '#/components/schemas/UserEndpointConfig'
        provider:
          $ref: '#/components/schemas/ModelProviderName'
        author:
          $ref: '#/components/schemas/AuthorName'
        providerModelId:
          type: string
        supportedParameters:
          items:
            $ref: '#/components/schemas/StandardParameter'
          type: array
        priority:
          type: number
          format: double
      required:
        - pricing
        - contextLength
        - maxCompletionTokens
        - ptbEnabled
        - modelConfig
        - userConfig
        - provider
        - author
        - providerModelId
        - supportedParameters
      type: object
      additionalProperties: false
    SimplifiedPricing:
      properties:
        prompt:
          type: number
          format: double
        completion:
          type: number
          format: double
        audio:
          type: number
          format: double
        thinking:
          type: number
          format: double
        web_search:
          type: number
          format: double
        image:
          type: number
          format: double
        video:
          type: number
          format: double
        cacheRead:
          type: number
          format: double
        cacheWrite:
          type: number
          format: double
        threshold:
          type: number
          format: double
      required:
        - prompt
        - completion
      type: object
      additionalProperties: false
    ModelEndpoint:
      properties:
        provider:
          type: string
        providerSlug:
          type: string
        endpoint:
          $ref: '#/components/schemas/Endpoint'
        supportsPtb:
          type: boolean
        pricing:
          $ref: '#/components/schemas/SimplifiedPricing'
        pricingTiers:
          items:
            $ref: '#/components/schemas/SimplifiedPricing'
          type: array
      required:
        - provider
        - providerSlug
        - pricing
      type: object
      additionalProperties: false
    InputModality:
      type: string
      enum:
        - text
        - image
        - audio
        - video
    OutputModality:
      type: string
      enum:
        - text
        - image
        - audio
        - video
    ModelRegistryItem:
      properties:
        id:
          type: string
        name:
          type: string
        author:
          type: string
        contextLength:
          type: number
          format: double
        endpoints:
          items:
            $ref: '#/components/schemas/ModelEndpoint'
          type: array
        maxOutput:
          type: number
          format: double
        trainingDate:
          type: string
        description:
          type: string
        inputModalities:
          items:
            $ref: '#/components/schemas/InputModality'
          type: array
        outputModalities:
          items:
            $ref: '#/components/schemas/OutputModality'
          type: array
        supportedParameters:
          items:
            $ref: '#/components/schemas/StandardParameter'
          type: array
        pinnedVersionOfModel:
          type: string
      required:
        - id
        - name
        - author
        - contextLength
        - endpoints
        - inputModalities
        - outputModalities
        - supportedParameters
      type: object
      additionalProperties: false
    ModelCapability:
      type: string
      enum:
        - audio
        - video
        - image
        - thinking
        - web_search
        - caching
        - reasoning
    ModelRegistryResponse:
      properties:
        models:
          items:
            $ref: '#/components/schemas/ModelRegistryItem'
          type: array
        total:
          type: number
          format: double
        filters:
          properties:
            capabilities:
              items:
                $ref: '#/components/schemas/ModelCapability'
              type: array
            authors:
              items:
                type: string
              type: array
            providers:
              items:
                properties:
                  displayName:
                    type: string
                  name:
                    type: string
                required:
                  - displayName
                  - name
                type: object
              type: array
          required:
            - capabilities
            - authors
            - providers
          type: object
      required:
        - models
        - total
        - filters
      type: object
      additionalProperties: false

````