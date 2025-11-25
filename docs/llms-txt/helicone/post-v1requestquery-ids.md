# Source: https://docs.helicone.ai/rest/request/post-v1requestquery-ids.md

# Get Requests by IDs

> Retrieve all requests visible in the request table at Helicone.

## OpenAPI

````yaml post /v1/request/query-ids
paths:
  path: /v1/request/query-ids
  method: post
  servers:
    - url: https://api.helicone.ai/
    - url: http://localhost:8585/
  request:
    security:
      - title: api key
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: 'Bearer token authentication. Format: ''Bearer YOUR_API_KEY'''
          cookie: {}
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
              requestIds:
                allOf:
                  - items:
                      type: string
                    type: array
            required: true
            requiredProperties:
              - requestIds
        examples:
          example:
            value:
              requestIds:
                - <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - items:
                      $ref: '#/components/schemas/HeliconeRequest'
                    type: array
              error:
                allOf:
                  - type: number
                    enum:
                      - null
                    nullable: true
            refIdentifier: '#/components/schemas/ResultSuccess_HeliconeRequest-Array_'
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
          example:
            value:
              data:
                - response_id: <string>
                  response_created_at: <string>
                  response_body: <any>
                  response_status: 123
                  response_model: <string>
                  request_id: <string>
                  request_created_at: <string>
                  request_body: <any>
                  request_path: <string>
                  request_user_id: <string>
                  request_properties: {}
                  request_model: <string>
                  model_override: <string>
                  helicone_user: <string>
                  provider: OPENAI
                  delay_ms: 123
                  time_to_first_token: 123
                  total_tokens: 123
                  prompt_tokens: 123
                  prompt_cache_write_tokens: 123
                  prompt_cache_read_tokens: 123
                  completion_tokens: 123
                  prompt_audio_tokens: 123
                  completion_audio_tokens: 123
                  cost: 123
                  prompt_id: <string>
                  prompt_version: <string>
                  feedback_created_at: <string>
                  feedback_id: <string>
                  feedback_rating: true
                  signed_body_url: <string>
                  llmSchema:
                    request:
                      llm_type: chat
                      provider: <string>
                      model: <string>
                      messages:
                        - ending_event_id: <string>
                          trigger_event_id: <string>
                          start_timestamp: <string>
                          annotations:
                            - <any>
                          reasoning: <string>
                          deleted: true
                          contentArray:
                            - <any>
                          idx: 123
                          detail: <string>
                          filename: <string>
                          file_id: <string>
                          file_data: <string>
                          type: input_image
                          audio_data: <string>
                          image_url: <string>
                          timestamp: <string>
                          tool_call_id: <string>
                          tool_calls:
                            - <any>
                          mime_type: <string>
                          content: <string>
                          name: <string>
                          instruction: <string>
                          role: <string>
                          id: <string>
                          _type: functionCall
                      prompt: <string>
                      instructions: <string>
                      max_tokens: 123
                      temperature: 123
                      top_p: 123
                      seed: 123
                      stream: true
                      presence_penalty: 123
                      frequency_penalty: 123
                      stop:
                        - <string>
                      reasoning_effort: minimal
                      verbosity: low
                      tools:
                        - name: <string>
                          description: <string>
                          parameters: {}
                      parallel_tool_calls: true
                      tool_choice:
                        name: <string>
                        type: none
                      response_format:
                        json_schema: <any>
                        type: <string>
                      toolDetails:
                        _type: tool
                        toolName: <string>
                        input: <any>
                      vectorDBDetails:
                        _type: vector_db
                        operation: search
                        text: <string>
                        vector:
                          - 123
                        topK: 123
                        filter: {}
                        databaseName: <string>
                      dataDetails:
                        _type: data
                        name: <string>
                        meta: {}
                      input: <string>
                      'n': 123
                      size: <string>
                      quality: <string>
                    response:
                      dataDetailsResponse:
                        name: <string>
                        _type: data
                        metadata:
                          timestamp: <string>
                        message: <string>
                        status: <string>
                      vectorDBDetailsResponse:
                        _type: vector_db
                        metadata:
                          timestamp: <string>
                          destination_parsed: true
                          destination: <string>
                        actualSimilarity: 123
                        similarityThreshold: 123
                        message: <string>
                        status: <string>
                      toolDetailsResponse:
                        toolName: <string>
                        _type: tool
                        metadata:
                          timestamp: <string>
                        tips:
                          - <string>
                        message: <string>
                        status: <string>
                      error:
                        heliconeMessage: <any>
                      model: <string>
                      instructions: <string>
                      responses:
                        - contentArray:
                            - {}
                          detail: <string>
                          filename: <string>
                          file_id: <string>
                          file_data: <string>
                          idx: 123
                          audio_data: <string>
                          image_url: <string>
                          timestamp: <string>
                          tool_call_id: <string>
                          tool_calls:
                            - {}
                          text: <string>
                          type: input_image
                          name: <string>
                          role: user
                          id: <string>
                          _type: functionCall
                      messages:
                        - ending_event_id: <string>
                          trigger_event_id: <string>
                          start_timestamp: <string>
                          annotations:
                            - <any>
                          reasoning: <string>
                          deleted: true
                          contentArray:
                            - <any>
                          idx: 123
                          detail: <string>
                          filename: <string>
                          file_id: <string>
                          file_data: <string>
                          type: input_image
                          audio_data: <string>
                          image_url: <string>
                          timestamp: <string>
                          tool_call_id: <string>
                          tool_calls:
                            - <any>
                          mime_type: <string>
                          content: <string>
                          name: <string>
                          instruction: <string>
                          role: <string>
                          id: <string>
                          _type: functionCall
                  country_code: <string>
                  asset_ids:
                    - <string>
                  asset_urls: {}
                  scores: {}
                  costUSD: 123
                  properties: {}
                  assets:
                    - <string>
                  target_url: <string>
                  model: <string>
                  cache_reference_id: <string>
                  cache_enabled: true
                  updated_at: <string>
                  request_referrer: <string>
                  ai_gateway_body_mapping: <string>
                  storage_location: <string>
        description: Ok
  deprecated: false
  type: path
components:
  schemas:
    Record_string.any_:
      properties: {}
      additionalProperties: {}
      type: object
      description: Construct a type with a set of properties K of type T
    Record_string.string_:
      properties: {}
      additionalProperties:
        type: string
      type: object
      description: Construct a type with a set of properties K of type T
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
    Provider:
      anyOf:
        - $ref: '#/components/schemas/ProviderName'
        - $ref: '#/components/schemas/ModelProviderName'
        - type: string
          enum:
            - CUSTOM
    LlmType:
      type: string
      enum:
        - chat
        - completion
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

````