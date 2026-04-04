# Source: https://docs.helicone.ai/rest/request/get-v1request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Single Request

> Retrieve a single request visible in the request table at Helicone.

<Warning>
  <strong>For users in the European Union:</strong> Please use `eu.api.helicone.ai` instead of
  `api.helicone.ai`.
</Warning>


## OpenAPI

````yaml get /v1/request/{requestId}
openapi: 3.0.0
info:
  title: helicone-api
  version: 1.0.0
  license:
    name: MIT
  contact: {}
servers:
  - url: https://api.helicone.ai/
  - url: http://localhost:8585/
security: []
paths:
  /v1/request/{requestId}:
    get:
      tags:
        - Request
      operationId: GetRequestById
      parameters:
        - in: path
          name: requestId
          required: true
          schema:
            type: string
        - in: query
          name: includeBody
          required: false
          schema:
            default: false
            type: boolean
      responses:
        '200':
          description: Ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Result_HeliconeRequest.string_'
      security:
        - api_key: []
components:
  schemas:
    Result_HeliconeRequest.string_:
      anyOf:
        - $ref: '#/components/schemas/ResultSuccess_HeliconeRequest_'
        - $ref: '#/components/schemas/ResultError_string_'
    ResultSuccess_HeliconeRequest_:
      properties:
        data:
          $ref: '#/components/schemas/HeliconeRequest'
        error:
          type: number
          enum:
            - null
          nullable: true
      required:
        - data
        - error
      type: object
      additionalProperties: false
    ResultError_string_:
      properties:
        data:
          type: number
          enum:
            - null
          nullable: true
        error:
          type: string
      required:
        - data
        - error
      type: object
      additionalProperties: false
    HeliconeRequest:
      properties:
        response_id:
          type: string
          nullable: true
        response_created_at:
          type: string
          nullable: true
        response_body: {}
        response_status:
          type: number
          format: double
        response_model:
          type: string
          nullable: true
        request_id:
          type: string
        request_created_at:
          type: string
        request_body: {}
        request_path:
          type: string
        request_user_id:
          type: string
          nullable: true
        request_properties:
          allOf:
            - $ref: '#/components/schemas/Record_string.string_'
          nullable: true
        request_model:
          type: string
          nullable: true
        model_override:
          type: string
          nullable: true
        helicone_user:
          type: string
          nullable: true
        provider:
          $ref: '#/components/schemas/Provider'
        delay_ms:
          type: number
          format: double
          nullable: true
        time_to_first_token:
          type: number
          format: double
          nullable: true
        total_tokens:
          type: number
          format: double
          nullable: true
        prompt_tokens:
          type: number
          format: double
          nullable: true
        prompt_cache_write_tokens:
          type: number
          format: double
          nullable: true
        prompt_cache_read_tokens:
          type: number
          format: double
          nullable: true
        completion_tokens:
          type: number
          format: double
          nullable: true
        reasoning_tokens:
          type: number
          format: double
          nullable: true
        prompt_audio_tokens:
          type: number
          format: double
          nullable: true
        completion_audio_tokens:
          type: number
          format: double
          nullable: true
        cost:
          type: number
          format: double
          nullable: true
        prompt_id:
          type: string
          nullable: true
        prompt_version:
          type: string
          nullable: true
        feedback_created_at:
          type: string
          nullable: true
        feedback_id:
          type: string
          nullable: true
        feedback_rating:
          type: boolean
          nullable: true
        signed_body_url:
          type: string
          nullable: true
        llmSchema:
          allOf:
            - $ref: '#/components/schemas/LlmSchema'
          nullable: true
        country_code:
          type: string
          nullable: true
        asset_ids:
          items:
            type: string
          type: array
          nullable: true
        asset_urls:
          allOf:
            - $ref: '#/components/schemas/Record_string.string_'
          nullable: true
        scores:
          allOf:
            - $ref: '#/components/schemas/Record_string.number_'
          nullable: true
        costUSD:
          type: number
          format: double
          nullable: true
        properties:
          $ref: '#/components/schemas/Record_string.string_'
        assets:
          items:
            type: string
          type: array
        target_url:
          type: string
        model:
          type: string
        cache_reference_id:
          type: string
          nullable: true
        cache_enabled:
          type: boolean
        updated_at:
          type: string
        request_referrer:
          type: string
          nullable: true
        ai_gateway_body_mapping:
          type: string
          nullable: true
        storage_location:
          type: string
      required:
        - response_id
        - response_created_at
        - response_status
        - response_model
        - request_id
        - request_created_at
        - request_body
        - request_path
        - request_user_id
        - request_properties
        - request_model
        - model_override
        - helicone_user
        - provider
        - delay_ms
        - time_to_first_token
        - total_tokens
        - prompt_tokens
        - prompt_cache_write_tokens
        - prompt_cache_read_tokens
        - completion_tokens
        - reasoning_tokens
        - prompt_audio_tokens
        - completion_audio_tokens
        - cost
        - prompt_id
        - prompt_version
        - llmSchema
        - country_code
        - asset_ids
        - asset_urls
        - scores
        - properties
        - assets
        - target_url
        - model
        - cache_reference_id
        - cache_enabled
        - ai_gateway_body_mapping
      type: object
      additionalProperties: false
    Record_string.string_:
      properties: {}
      additionalProperties:
        type: string
      type: object
      description: Construct a type with a set of properties K of type T
    Provider:
      anyOf:
        - $ref: '#/components/schemas/ProviderName'
        - $ref: '#/components/schemas/ModelProviderName'
        - type: string
          enum:
            - CUSTOM
    LlmSchema:
      properties:
        request:
          $ref: '#/components/schemas/LLMRequestBody'
        response:
          allOf:
            - $ref: '#/components/schemas/LLMResponseBody'
          nullable: true
      required:
        - request
      type: object
      additionalProperties: false
    Record_string.number_:
      properties: {}
      additionalProperties:
        type: number
        format: double
      type: object
      description: Construct a type with a set of properties K of type T
    ProviderName:
      type: string
      enum:
        - OPENAI
        - ANTHROPIC
        - AZURE
        - LOCAL
        - HELICONE
        - AMDBARTEK
        - ANYSCALE
        - CLOUDFLARE
        - 2YFV
        - TOGETHER
        - LEMONFOX
        - FIREWORKS
        - PERPLEXITY
        - GOOGLE
        - OPENROUTER
        - WISDOMINANUTSHELL
        - GROQ
        - COHERE
        - MISTRAL
        - DEEPINFRA
        - QSTASH
        - FIRECRAWL
        - AWS
        - BEDROCK
        - DEEPSEEK
        - X
        - AVIAN
        - NEBIUS
        - NOVITA
        - OPENPIPE
        - CHUTES
        - LLAMA
        - NVIDIA
        - VERCEL
        - CEREBRAS
        - BASETEN
        - CANOPYWAVE
    ModelProviderName:
      type: string
      enum:
        - baseten
        - anthropic
        - azure
        - bedrock
        - canopywave
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
    LLMRequestBody:
      properties:
        llm_type:
          $ref: '#/components/schemas/LlmType'
        provider:
          type: string
        model:
          type: string
        messages:
          items:
            $ref: '#/components/schemas/Message'
          type: array
          nullable: true
        prompt:
          type: string
          nullable: true
        instructions:
          type: string
          nullable: true
        max_tokens:
          type: number
          format: double
          nullable: true
        temperature:
          type: number
          format: double
          nullable: true
        top_p:
          type: number
          format: double
          nullable: true
        seed:
          type: number
          format: double
          nullable: true
        stream:
          type: boolean
          nullable: true
        presence_penalty:
          type: number
          format: double
          nullable: true
        frequency_penalty:
          type: number
          format: double
          nullable: true
        stop:
          anyOf:
            - items:
                type: string
              type: array
            - type: string
          nullable: true
        reasoning_effort:
          type: string
          enum:
            - minimal
            - low
            - medium
            - high
            - null
          nullable: true
        verbosity:
          type: string
          enum:
            - low
            - medium
            - high
            - null
          nullable: true
        tools:
          items:
            $ref: '#/components/schemas/Tool'
          type: array
        parallel_tool_calls:
          type: boolean
          nullable: true
        tool_choice:
          properties:
            name:
              type: string
            type:
              type: string
              enum:
                - none
                - auto
                - any
                - tool
          required:
            - type
          type: object
        response_format:
          properties:
            json_schema: {}
            type:
              type: string
          required:
            - type
          type: object
        toolDetails:
          $ref: '#/components/schemas/HeliconeEventTool'
        vectorDBDetails:
          $ref: '#/components/schemas/HeliconeEventVectorDB'
        dataDetails:
          $ref: '#/components/schemas/HeliconeEventData'
        input:
          anyOf:
            - type: string
            - items:
                type: string
              type: array
        'n':
          type: number
          format: double
          nullable: true
        size:
          type: string
        quality:
          type: string
      type: object
      additionalProperties: false
    LLMResponseBody:
      properties:
        dataDetailsResponse:
          properties:
            name:
              type: string
            _type:
              type: string
              enum:
                - data
              nullable: false
            metadata:
              properties:
                timestamp:
                  type: string
              additionalProperties: {}
              required:
                - timestamp
              type: object
            message:
              type: string
            status:
              type: string
          additionalProperties: {}
          required:
            - name
            - _type
            - metadata
            - message
            - status
          type: object
        vectorDBDetailsResponse:
          properties:
            _type:
              type: string
              enum:
                - vector_db
              nullable: false
            metadata:
              properties:
                timestamp:
                  type: string
                destination_parsed:
                  type: boolean
                destination:
                  type: string
              required:
                - timestamp
              type: object
            actualSimilarity:
              type: number
              format: double
            similarityThreshold:
              type: number
              format: double
            message:
              type: string
            status:
              type: string
          required:
            - _type
            - metadata
            - message
            - status
          type: object
        toolDetailsResponse:
          properties:
            toolName:
              type: string
            _type:
              type: string
              enum:
                - tool
              nullable: false
            metadata:
              properties:
                timestamp:
                  type: string
              required:
                - timestamp
              type: object
            tips:
              items:
                type: string
              type: array
            message:
              type: string
            status:
              type: string
          required:
            - toolName
            - _type
            - metadata
            - tips
            - message
            - status
          type: object
        error:
          properties:
            heliconeMessage: {}
          required:
            - heliconeMessage
          type: object
        model:
          type: string
          nullable: true
        instructions:
          type: string
          nullable: true
        responses:
          items:
            $ref: '#/components/schemas/Response'
          type: array
          nullable: true
        messages:
          items:
            $ref: '#/components/schemas/Message'
          type: array
          nullable: true
      type: object
    LlmType:
      type: string
      enum:
        - chat
        - completion
    Message:
      properties:
        ending_event_id:
          type: string
        trigger_event_id:
          type: string
        start_timestamp:
          type: string
        annotations:
          items:
            properties:
              content:
                type: string
              title:
                type: string
              url:
                type: string
              type:
                type: string
                enum:
                  - url_citation
                nullable: false
            required:
              - title
              - url
              - type
            type: object
          type: array
        reasoning:
          type: string
        deleted:
          type: boolean
        contentArray:
          items:
            $ref: '#/components/schemas/Message'
          type: array
        idx:
          type: number
          format: double
        detail:
          type: string
        filename:
          type: string
        file_id:
          type: string
        file_data:
          type: string
        type:
          type: string
          enum:
            - input_image
            - input_text
            - input_file
        audio_data:
          type: string
        image_url:
          type: string
        timestamp:
          type: string
        tool_call_id:
          type: string
        tool_calls:
          items:
            $ref: '#/components/schemas/FunctionCall'
          type: array
        mime_type:
          type: string
        content:
          type: string
        name:
          type: string
        instruction:
          type: string
        role:
          anyOf:
            - type: string
            - type: string
              enum:
                - user
                - assistant
                - system
                - developer
        id:
          type: string
        _type:
          type: string
          enum:
            - functionCall
            - function
            - image
            - file
            - message
            - autoInput
            - contentArray
            - audio
      required:
        - _type
      type: object
    Tool:
      properties:
        name:
          type: string
        description:
          type: string
        parameters:
          $ref: '#/components/schemas/Record_string.any_'
      required:
        - name
        - description
      type: object
      additionalProperties: false
    HeliconeEventTool:
      properties:
        _type:
          type: string
          enum:
            - tool
          nullable: false
        toolName:
          type: string
        input: {}
      required:
        - _type
        - toolName
        - input
      type: object
      additionalProperties: {}
    HeliconeEventVectorDB:
      properties:
        _type:
          type: string
          enum:
            - vector_db
          nullable: false
        operation:
          type: string
          enum:
            - search
            - insert
            - delete
            - update
        text:
          type: string
        vector:
          items:
            type: number
            format: double
          type: array
        topK:
          type: number
          format: double
        filter:
          additionalProperties: false
          type: object
        databaseName:
          type: string
      required:
        - _type
        - operation
      type: object
      additionalProperties: {}
    HeliconeEventData:
      properties:
        _type:
          type: string
          enum:
            - data
          nullable: false
        name:
          type: string
        meta:
          $ref: '#/components/schemas/Record_string.any_'
      required:
        - _type
        - name
      type: object
      additionalProperties: {}
    Response:
      properties:
        contentArray:
          items:
            $ref: '#/components/schemas/Response'
          type: array
        detail:
          type: string
        filename:
          type: string
        file_id:
          type: string
        file_data:
          type: string
        idx:
          type: number
          format: double
        audio_data:
          type: string
        image_url:
          type: string
        timestamp:
          type: string
        tool_call_id:
          type: string
        tool_calls:
          items:
            $ref: '#/components/schemas/FunctionCall'
          type: array
        text:
          type: string
        type:
          type: string
          enum:
            - input_image
            - input_text
            - input_file
        name:
          type: string
        role:
          type: string
          enum:
            - user
            - assistant
            - system
            - developer
        id:
          type: string
        _type:
          type: string
          enum:
            - functionCall
            - function
            - image
            - text
            - file
            - contentArray
      required:
        - type
        - role
        - _type
      type: object
    FunctionCall:
      properties:
        id:
          type: string
        name:
          type: string
        arguments:
          $ref: '#/components/schemas/Record_string.any_'
      required:
        - name
        - arguments
      type: object
      additionalProperties: false
    Record_string.any_:
      properties: {}
      additionalProperties: {}
      type: object
      description: Construct a type with a set of properties K of type T
  securitySchemes:
    api_key:
      type: apiKey
      name: Authorization
      in: header
      description: 'Bearer token authentication. Format: ''Bearer YOUR_API_KEY'''

````