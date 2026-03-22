# Source: https://docs.wandb.ai/api-reference/chat-completions/create-chat-completion-1.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Chat Completion

> Create a new chat completion.



## OpenAPI

````yaml /training/api-reference/openapi.json post /v1/chat/completions
openapi: 3.1.0
info:
  title: W&B Training
  version: 1.0.0
servers: []
security: []
paths:
  /v1/chat/completions:
    post:
      tags:
        - chat-completions
      summary: Create Chat Completion
      description: Create a new chat completion.
      operationId: create_chat_completion_v1_chat_completions_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ChatCompletionRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatCompletionResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - HTTPBearer: []
components:
  schemas:
    ChatCompletionRequest:
      properties:
        messages:
          items:
            anyOf:
              - $ref: '#/components/schemas/ChatCompletionDeveloperMessageParam'
              - $ref: '#/components/schemas/ChatCompletionSystemMessageParam'
              - $ref: '#/components/schemas/ChatCompletionUserMessageParam'
              - $ref: '#/components/schemas/ChatCompletionAssistantMessageParam'
              - $ref: '#/components/schemas/ChatCompletionToolMessageParam'
              - $ref: '#/components/schemas/ChatCompletionFunctionMessageParam'
              - $ref: '#/components/schemas/CustomChatCompletionMessageParam'
              - $ref: '#/components/schemas/Message'
          type: array
          title: Messages
        model:
          anyOf:
            - type: string
            - type: 'null'
          title: Model
        frequency_penalty:
          anyOf:
            - type: number
            - type: 'null'
          title: Frequency Penalty
          default: 0
        logit_bias:
          anyOf:
            - additionalProperties:
                type: number
              type: object
            - type: 'null'
          title: Logit Bias
        logprobs:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Logprobs
          default: false
        top_logprobs:
          anyOf:
            - type: integer
            - type: 'null'
          title: Top Logprobs
          default: 0
        max_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Tokens
          deprecated: true
        max_completion_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Completion Tokens
        'n':
          anyOf:
            - type: integer
            - type: 'null'
          title: 'N'
          default: 1
        presence_penalty:
          anyOf:
            - type: number
            - type: 'null'
          title: Presence Penalty
          default: 0
        response_format:
          anyOf:
            - $ref: '#/components/schemas/ResponseFormat'
            - $ref: '#/components/schemas/StructuralTagResponseFormat'
            - $ref: '#/components/schemas/LegacyStructuralTagResponseFormat'
            - type: 'null'
          title: Response Format
        seed:
          anyOf:
            - type: integer
              maximum: 9223372036854776000
              minimum: -9223372036854776000
            - type: 'null'
          title: Seed
        stop:
          anyOf:
            - type: string
            - items:
                type: string
              type: array
            - type: 'null'
          title: Stop
          default: []
        stream:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Stream
          default: false
        stream_options:
          anyOf:
            - $ref: '#/components/schemas/StreamOptions'
            - type: 'null'
        temperature:
          anyOf:
            - type: number
            - type: 'null'
          title: Temperature
        top_p:
          anyOf:
            - type: number
            - type: 'null'
          title: Top P
        tools:
          anyOf:
            - items:
                $ref: '#/components/schemas/ChatCompletionToolsParam'
              type: array
            - type: 'null'
          title: Tools
        tool_choice:
          anyOf:
            - type: string
              const: none
            - type: string
              const: auto
            - type: string
              const: required
            - $ref: '#/components/schemas/ChatCompletionNamedToolChoiceParam'
            - type: 'null'
          title: Tool Choice
          default: none
        reasoning_effort:
          anyOf:
            - type: string
              enum:
                - low
                - medium
                - high
            - type: 'null'
          title: Reasoning Effort
        include_reasoning:
          type: boolean
          title: Include Reasoning
          default: true
        parallel_tool_calls:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Parallel Tool Calls
          default: true
        user:
          anyOf:
            - type: string
            - type: 'null'
          title: User
        use_beam_search:
          type: boolean
          title: Use Beam Search
          default: false
        top_k:
          anyOf:
            - type: integer
            - type: 'null'
          title: Top K
        min_p:
          anyOf:
            - type: number
            - type: 'null'
          title: Min P
        repetition_penalty:
          anyOf:
            - type: number
            - type: 'null'
          title: Repetition Penalty
        length_penalty:
          type: number
          title: Length Penalty
          default: 1
        stop_token_ids:
          anyOf:
            - items:
                type: integer
              type: array
            - type: 'null'
          title: Stop Token Ids
          default: []
        include_stop_str_in_output:
          type: boolean
          title: Include Stop Str In Output
          default: false
        ignore_eos:
          type: boolean
          title: Ignore Eos
          default: false
        min_tokens:
          type: integer
          title: Min Tokens
          default: 0
        skip_special_tokens:
          type: boolean
          title: Skip Special Tokens
          default: true
        spaces_between_special_tokens:
          type: boolean
          title: Spaces Between Special Tokens
          default: true
        truncate_prompt_tokens:
          anyOf:
            - type: integer
              minimum: -1
            - type: 'null'
          title: Truncate Prompt Tokens
        prompt_logprobs:
          anyOf:
            - type: integer
            - type: 'null'
          title: Prompt Logprobs
        allowed_token_ids:
          anyOf:
            - items:
                type: integer
              type: array
            - type: 'null'
          title: Allowed Token Ids
        bad_words:
          items:
            type: string
          type: array
          title: Bad Words
        echo:
          type: boolean
          title: Echo
          description: >-
            If true, the new message will be prepended with the last message if
            they belong to the same role.
          default: false
        add_generation_prompt:
          type: boolean
          title: Add Generation Prompt
          description: >-
            If true, the generation prompt will be added to the chat template.
            This is a parameter used by chat template in tokenizer config of the
            model.
          default: true
        continue_final_message:
          type: boolean
          title: Continue Final Message
          description: >-
            If this is set, the chat will be formatted so that the final message
            in the chat is open-ended, without any EOS tokens. The model will
            continue this message rather than starting a new one. This allows
            you to "prefill" part of the model's response for it. Cannot be used
            at the same time as `add_generation_prompt`.
          default: false
        add_special_tokens:
          type: boolean
          title: Add Special Tokens
          description: >-
            If true, special tokens (e.g. BOS) will be added to the prompt on
            top of what is added by the chat template. For most models, the chat
            template takes care of adding the special tokens so this should be
            set to false (as is the default).
          default: false
        documents:
          anyOf:
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - type: 'null'
          title: Documents
          description: >-
            A list of dicts representing documents that will be accessible to
            the model if it is performing RAG (retrieval-augmented generation).
            If the template does not support RAG, this argument will have no
            effect. We recommend that each document should be a dict containing
            "title" and "text" keys.
        chat_template:
          anyOf:
            - type: string
            - type: 'null'
          title: Chat Template
          description: >-
            A Jinja template to use for this conversion. As of transformers
            v4.44, default chat template is no longer allowed, so you must
            provide a chat template if the tokenizer does not define one.
        chat_template_kwargs:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Chat Template Kwargs
          description: >-
            Additional keyword args to pass to the template renderer. Will be
            accessible by the chat template.
        mm_processor_kwargs:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Mm Processor Kwargs
          description: Additional kwargs to pass to the HF processor.
        structured_outputs:
          anyOf:
            - $ref: '#/components/schemas/StructuredOutputsParams'
            - type: 'null'
          description: Additional kwargs for structured outputs
        priority:
          type: integer
          title: Priority
          description: >-
            The priority of the request (lower means earlier handling; default:
            0). Any priority other than 0 will raise an error if the served
            model does not use priority scheduling.
          default: 0
        request_id:
          type: string
          title: Request Id
          description: >-
            The request_id related to this request. If the caller does not set
            it, a random_uuid will be generated. This id is used through out the
            inference process and return in response.
        logits_processors:
          anyOf:
            - items:
                anyOf:
                  - type: string
                  - $ref: '#/components/schemas/LogitsProcessorConstructor'
              type: array
            - type: 'null'
          title: Logits Processors
          description: >-
            A list of either qualified names of logits processors, or
            constructor objects, to apply when sampling. A constructor is a JSON
            object with a required 'qualname' field specifying the qualified
            name of the processor class/factory, and optional 'args' and
            'kwargs' fields containing positional and keyword arguments. For
            example: {'qualname': 'my_module.MyLogitsProcessor', 'args': [1, 2],
            'kwargs': {'param': 'value'}}.
        return_tokens_as_token_ids:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Return Tokens As Token Ids
          description: >-
            If specified with 'logprobs', tokens are represented  as strings of
            the form 'token_id:{token_id}' so that tokens that are not
            JSON-encodable can be identified.
        return_token_ids:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Return Token Ids
          description: >-
            If specified, the result will include token IDs alongside the
            generated text. In streaming mode, prompt_token_ids is included only
            in the first chunk, and token_ids contains the delta tokens for each
            chunk. This is useful for debugging or when you need to map
            generated text back to input tokens.
        cache_salt:
          anyOf:
            - type: string
            - type: 'null'
          title: Cache Salt
          description: >-
            If specified, the prefix cache will be salted with the provided
            string to prevent an attacker to guess prompts in multi-user
            environments. The salt should be random, protected from access by
            3rd parties, and long enough to be unpredictable (e.g., 43
            characters base64-encoded, corresponding to 256 bit).
        kv_transfer_params:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Kv Transfer Params
          description: KVTransfer parameters used for disaggregated serving.
        vllm_xargs:
          anyOf:
            - additionalProperties:
                anyOf:
                  - type: string
                  - type: integer
                  - type: number
                  - items:
                      anyOf:
                        - type: string
                        - type: integer
                        - type: number
                    type: array
              type: object
            - type: 'null'
          title: Vllm Xargs
          description: >-
            Additional request parameters with (list of) string or numeric
            values, used by custom extensions.
      additionalProperties: true
      type: object
      required:
        - messages
      title: ChatCompletionRequest
    ChatCompletionResponse:
      properties:
        id:
          type: string
          title: Id
        object:
          type: string
          const: chat.completion
          title: Object
          default: chat.completion
        created:
          type: integer
          title: Created
        model:
          type: string
          title: Model
        choices:
          items:
            $ref: '#/components/schemas/ChatCompletionResponseChoice'
          type: array
          title: Choices
        service_tier:
          anyOf:
            - type: string
              enum:
                - auto
                - default
                - flex
                - scale
                - priority
            - type: 'null'
          title: Service Tier
        system_fingerprint:
          anyOf:
            - type: string
            - type: 'null'
          title: System Fingerprint
        usage:
          $ref: '#/components/schemas/UsageInfo'
        prompt_logprobs:
          anyOf:
            - items:
                anyOf:
                  - additionalProperties:
                      $ref: '#/components/schemas/Logprob'
                    type: object
                  - type: 'null'
              type: array
            - type: 'null'
          title: Prompt Logprobs
        prompt_token_ids:
          anyOf:
            - items:
                type: integer
              type: array
            - type: 'null'
          title: Prompt Token Ids
        kv_transfer_params:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Kv Transfer Params
          description: KVTransfer parameters.
      additionalProperties: true
      type: object
      required:
        - model
        - choices
        - usage
      title: ChatCompletionResponse
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ChatCompletionDeveloperMessageParam:
      properties:
        content:
          anyOf:
            - type: string
            - items:
                $ref: '#/components/schemas/ChatCompletionContentPartTextParam'
              type: array
          title: Content
        role:
          type: string
          const: developer
          title: Role
        name:
          type: string
          title: Name
      additionalProperties: true
      type: object
      required:
        - content
        - role
      title: ChatCompletionDeveloperMessageParam
      description: >-
        Developer-provided instructions that the model should follow, regardless
        of

        messages sent by the user. With o1 models and newer, `developer`
        messages

        replace the previous `system` messages.
    ChatCompletionSystemMessageParam:
      properties:
        content:
          anyOf:
            - type: string
            - items:
                $ref: '#/components/schemas/ChatCompletionContentPartTextParam'
              type: array
          title: Content
        role:
          type: string
          const: system
          title: Role
        name:
          type: string
          title: Name
      additionalProperties: true
      type: object
      required:
        - content
        - role
      title: ChatCompletionSystemMessageParam
      description: >-
        Developer-provided instructions that the model should follow, regardless
        of

        messages sent by the user. With o1 models and newer, use `developer`
        messages

        for this purpose instead.
    ChatCompletionUserMessageParam:
      properties:
        content:
          anyOf:
            - type: string
            - items:
                anyOf:
                  - $ref: '#/components/schemas/ChatCompletionContentPartTextParam'
                  - $ref: '#/components/schemas/ChatCompletionContentPartImageParam'
                  - $ref: >-
                      #/components/schemas/ChatCompletionContentPartInputAudioParam
                  - $ref: '#/components/schemas/File'
              type: array
          title: Content
        role:
          type: string
          const: user
          title: Role
        name:
          type: string
          title: Name
      additionalProperties: true
      type: object
      required:
        - content
        - role
      title: ChatCompletionUserMessageParam
      description: |-
        Messages sent by an end user, containing prompts or additional context
        information.
    ChatCompletionAssistantMessageParam:
      properties:
        role:
          type: string
          const: assistant
          title: Role
        audio:
          anyOf:
            - $ref: '#/components/schemas/Audio'
            - type: 'null'
        content:
          anyOf:
            - type: string
            - items:
                anyOf:
                  - $ref: '#/components/schemas/ChatCompletionContentPartTextParam'
                  - $ref: '#/components/schemas/ChatCompletionContentPartRefusalParam'
              type: array
            - type: 'null'
          title: Content
        function_call:
          anyOf:
            - $ref: '#/components/schemas/FunctionCall-Input'
            - type: 'null'
        name:
          type: string
          title: Name
        refusal:
          anyOf:
            - type: string
            - type: 'null'
          title: Refusal
        tool_calls:
          items:
            anyOf:
              - $ref: >-
                  #/components/schemas/ChatCompletionMessageFunctionToolCallParam
              - $ref: '#/components/schemas/ChatCompletionMessageCustomToolCallParam'
          type: array
          title: Tool Calls
      additionalProperties: true
      type: object
      required:
        - role
      title: ChatCompletionAssistantMessageParam
      description: Messages sent by the model in response to user messages.
    ChatCompletionToolMessageParam:
      properties:
        content:
          anyOf:
            - type: string
            - items:
                $ref: '#/components/schemas/ChatCompletionContentPartTextParam'
              type: array
          title: Content
        role:
          type: string
          const: tool
          title: Role
        tool_call_id:
          type: string
          title: Tool Call Id
      additionalProperties: true
      type: object
      required:
        - content
        - role
        - tool_call_id
      title: ChatCompletionToolMessageParam
    ChatCompletionFunctionMessageParam:
      properties:
        content:
          anyOf:
            - type: string
            - type: 'null'
          title: Content
        name:
          type: string
          title: Name
        role:
          type: string
          const: function
          title: Role
      additionalProperties: true
      type: object
      required:
        - content
        - name
        - role
      title: ChatCompletionFunctionMessageParam
    CustomChatCompletionMessageParam:
      properties:
        role:
          type: string
          title: Role
        content:
          anyOf:
            - type: string
            - items:
                anyOf:
                  - $ref: '#/components/schemas/ChatCompletionContentPartTextParam'
                  - $ref: '#/components/schemas/ChatCompletionContentPartImageParam'
                  - $ref: >-
                      #/components/schemas/ChatCompletionContentPartInputAudioParam
                  - $ref: '#/components/schemas/File'
                  - $ref: '#/components/schemas/ChatCompletionContentPartAudioParam'
                  - $ref: '#/components/schemas/ChatCompletionContentPartVideoParam'
                  - $ref: '#/components/schemas/ChatCompletionContentPartRefusalParam'
                  - $ref: >-
                      #/components/schemas/CustomChatCompletionContentSimpleImageParam
                  - $ref: >-
                      #/components/schemas/ChatCompletionContentPartImageEmbedsParam
                  - $ref: >-
                      #/components/schemas/ChatCompletionContentPartAudioEmbedsParam
                  - $ref: >-
                      #/components/schemas/CustomChatCompletionContentSimpleAudioParam
                  - $ref: >-
                      #/components/schemas/CustomChatCompletionContentSimpleVideoParam
                  - type: string
                  - $ref: '#/components/schemas/CustomThinkCompletionContentParam'
              type: array
          title: Content
        name:
          type: string
          title: Name
        tool_call_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Tool Call Id
        tool_calls:
          anyOf:
            - items:
                $ref: >-
                  #/components/schemas/ChatCompletionMessageFunctionToolCallParam
              type: array
            - type: 'null'
          title: Tool Calls
        reasoning:
          anyOf:
            - type: string
            - type: 'null'
          title: Reasoning
        tools:
          anyOf:
            - items:
                $ref: '#/components/schemas/ChatCompletionFunctionToolParam'
              type: array
            - type: 'null'
          title: Tools
      additionalProperties: true
      type: object
      required:
        - role
      title: CustomChatCompletionMessageParam
      description: Enables custom roles in the Chat Completion API.
    Message:
      properties:
        author:
          $ref: '#/components/schemas/Author'
        content:
          items:
            $ref: '#/components/schemas/Content'
          type: array
          title: Content
        channel:
          anyOf:
            - type: string
            - type: 'null'
          title: Channel
        recipient:
          anyOf:
            - type: string
            - type: 'null'
          title: Recipient
        content_type:
          anyOf:
            - type: string
            - type: 'null'
          title: Content Type
      type: object
      required:
        - author
      title: Message
    ResponseFormat:
      properties:
        type:
          type: string
          enum:
            - text
            - json_object
            - json_schema
          title: Type
        json_schema:
          anyOf:
            - $ref: '#/components/schemas/JsonSchemaResponseFormat'
            - type: 'null'
      additionalProperties: true
      type: object
      required:
        - type
      title: ResponseFormat
    StructuralTagResponseFormat:
      properties:
        type:
          type: string
          const: structural_tag
          title: Type
        format:
          title: Format
      additionalProperties: true
      type: object
      required:
        - type
        - format
      title: StructuralTagResponseFormat
    LegacyStructuralTagResponseFormat:
      properties:
        type:
          type: string
          const: structural_tag
          title: Type
        structures:
          items:
            $ref: '#/components/schemas/LegacyStructuralTag'
          type: array
          title: Structures
        triggers:
          items:
            type: string
          type: array
          title: Triggers
      additionalProperties: true
      type: object
      required:
        - type
        - structures
        - triggers
      title: LegacyStructuralTagResponseFormat
    StreamOptions:
      properties:
        include_usage:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Include Usage
          default: true
        continuous_usage_stats:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Continuous Usage Stats
          default: false
      additionalProperties: true
      type: object
      title: StreamOptions
    ChatCompletionToolsParam:
      properties:
        type:
          type: string
          const: function
          title: Type
          default: function
        function:
          $ref: '#/components/schemas/FunctionDefinition'
      additionalProperties: true
      type: object
      required:
        - function
      title: ChatCompletionToolsParam
    ChatCompletionNamedToolChoiceParam:
      properties:
        function:
          $ref: '#/components/schemas/ChatCompletionNamedFunction'
        type:
          type: string
          const: function
          title: Type
          default: function
      additionalProperties: true
      type: object
      required:
        - function
      title: ChatCompletionNamedToolChoiceParam
    StructuredOutputsParams:
      properties:
        json:
          anyOf:
            - type: string
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Json
        regex:
          anyOf:
            - type: string
            - type: 'null'
          title: Regex
        choice:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Choice
        grammar:
          anyOf:
            - type: string
            - type: 'null'
          title: Grammar
        json_object:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Json Object
        disable_fallback:
          type: boolean
          title: Disable Fallback
          default: false
        disable_any_whitespace:
          type: boolean
          title: Disable Any Whitespace
          default: false
        disable_additional_properties:
          type: boolean
          title: Disable Additional Properties
          default: false
        whitespace_pattern:
          anyOf:
            - type: string
            - type: 'null'
          title: Whitespace Pattern
        structural_tag:
          anyOf:
            - type: string
            - type: 'null'
          title: Structural Tag
        _backend:
          anyOf:
            - type: string
            - type: 'null'
          title: Backend
        _backend_was_auto:
          type: boolean
          title: Backend Was Auto
          default: false
      type: object
      title: StructuredOutputsParams
    LogitsProcessorConstructor:
      properties:
        qualname:
          type: string
          title: Qualname
        args:
          anyOf:
            - items: {}
              type: array
            - type: 'null'
          title: Args
        kwargs:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Kwargs
      additionalProperties: false
      type: object
      required:
        - qualname
      title: LogitsProcessorConstructor
    ChatCompletionResponseChoice:
      properties:
        index:
          type: integer
          title: Index
        message:
          $ref: '#/components/schemas/ChatMessage'
        logprobs:
          anyOf:
            - $ref: '#/components/schemas/ChatCompletionLogProbs'
            - type: 'null'
        finish_reason:
          anyOf:
            - type: string
            - type: 'null'
          title: Finish Reason
          default: stop
        stop_reason:
          anyOf:
            - type: integer
            - type: string
            - type: 'null'
          title: Stop Reason
        token_ids:
          anyOf:
            - items:
                type: integer
              type: array
            - type: 'null'
          title: Token Ids
      additionalProperties: true
      type: object
      required:
        - index
        - message
      title: ChatCompletionResponseChoice
    UsageInfo:
      properties:
        prompt_tokens:
          type: integer
          title: Prompt Tokens
          default: 0
        total_tokens:
          type: integer
          title: Total Tokens
          default: 0
        completion_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Completion Tokens
          default: 0
        prompt_tokens_details:
          anyOf:
            - $ref: '#/components/schemas/PromptTokenUsageInfo'
            - type: 'null'
      additionalProperties: true
      type: object
      title: UsageInfo
    Logprob:
      properties:
        logprob:
          type: number
          title: Logprob
        rank:
          anyOf:
            - type: integer
            - type: 'null'
          title: Rank
        decoded_token:
          anyOf:
            - type: string
            - type: 'null'
          title: Decoded Token
      type: object
      required:
        - logprob
      title: Logprob
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    ChatCompletionContentPartTextParam:
      properties:
        text:
          type: string
          title: Text
        type:
          type: string
          const: text
          title: Type
      additionalProperties: true
      type: object
      required:
        - text
        - type
      title: ChatCompletionContentPartTextParam
      description: >-
        Learn about [text
        inputs](https://platform.openai.com/docs/guides/text-generation).
    ChatCompletionContentPartImageParam:
      properties:
        image_url:
          $ref: '#/components/schemas/ImageURL'
        type:
          type: string
          const: image_url
          title: Type
      additionalProperties: true
      type: object
      required:
        - image_url
        - type
      title: ChatCompletionContentPartImageParam
      description: >-
        Learn about [image
        inputs](https://platform.openai.com/docs/guides/vision).
    ChatCompletionContentPartInputAudioParam:
      properties:
        input_audio:
          $ref: '#/components/schemas/InputAudio'
        type:
          type: string
          const: input_audio
          title: Type
      additionalProperties: true
      type: object
      required:
        - input_audio
        - type
      title: ChatCompletionContentPartInputAudioParam
      description: >-
        Learn about [audio
        inputs](https://platform.openai.com/docs/guides/audio).
    File:
      properties:
        file:
          $ref: '#/components/schemas/FileFile'
        type:
          type: string
          const: file
          title: Type
      additionalProperties: true
      type: object
      required:
        - file
        - type
      title: File
      description: >-
        Learn about [file inputs](https://platform.openai.com/docs/guides/text)
        for text generation.
    Audio:
      properties:
        id:
          type: string
          title: Id
      additionalProperties: true
      type: object
      required:
        - id
      title: Audio
      description: |-
        Data about a previous audio response from the model.
        [Learn more](https://platform.openai.com/docs/guides/audio).
    ChatCompletionContentPartRefusalParam:
      properties:
        refusal:
          type: string
          title: Refusal
        type:
          type: string
          const: refusal
          title: Type
      additionalProperties: true
      type: object
      required:
        - refusal
        - type
      title: ChatCompletionContentPartRefusalParam
    FunctionCall-Input:
      properties:
        arguments:
          type: string
          title: Arguments
        name:
          type: string
          title: Name
      additionalProperties: true
      type: object
      required:
        - arguments
        - name
      title: FunctionCall
      description: >-
        Deprecated and replaced by `tool_calls`.


        The name and arguments of a function that should be called, as generated
        by the model.
    ChatCompletionMessageFunctionToolCallParam:
      properties:
        id:
          type: string
          title: Id
        function:
          $ref: '#/components/schemas/Function'
        type:
          type: string
          const: function
          title: Type
      additionalProperties: true
      type: object
      required:
        - id
        - function
        - type
      title: ChatCompletionMessageFunctionToolCallParam
      description: A call to a function tool created by the model.
    ChatCompletionMessageCustomToolCallParam:
      properties:
        id:
          type: string
          title: Id
        custom:
          $ref: '#/components/schemas/Custom'
        type:
          type: string
          const: custom
          title: Type
      additionalProperties: true
      type: object
      required:
        - id
        - custom
        - type
      title: ChatCompletionMessageCustomToolCallParam
      description: A call to a custom tool created by the model.
    ChatCompletionContentPartAudioParam:
      properties:
        audio_url:
          $ref: '#/components/schemas/AudioURL'
        type:
          type: string
          const: audio_url
          title: Type
      additionalProperties: true
      type: object
      required:
        - audio_url
        - type
      title: ChatCompletionContentPartAudioParam
    ChatCompletionContentPartVideoParam:
      properties:
        video_url:
          $ref: '#/components/schemas/VideoURL'
        type:
          type: string
          const: video_url
          title: Type
      additionalProperties: true
      type: object
      required:
        - video_url
        - type
      title: ChatCompletionContentPartVideoParam
    CustomChatCompletionContentSimpleImageParam:
      properties:
        image_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Image Url
        uuid:
          anyOf:
            - type: string
            - type: 'null'
          title: Uuid
      additionalProperties: true
      type: object
      title: CustomChatCompletionContentSimpleImageParam
      description: |-
        A simpler version of the param that only accepts a plain image_url.
        This is supported by OpenAI API, although it is not documented.

        Example:
        {
            "image_url": "https://example.com/image.jpg"
        }
    ChatCompletionContentPartImageEmbedsParam:
      properties:
        image_embeds:
          anyOf:
            - type: string
            - additionalProperties:
                type: string
              type: object
            - type: 'null'
          title: Image Embeds
        type:
          type: string
          const: image_embeds
          title: Type
        uuid:
          anyOf:
            - type: string
            - type: 'null'
          title: Uuid
      additionalProperties: true
      type: object
      required:
        - type
      title: ChatCompletionContentPartImageEmbedsParam
    ChatCompletionContentPartAudioEmbedsParam:
      properties:
        audio_embeds:
          anyOf:
            - type: string
            - additionalProperties:
                type: string
              type: object
            - type: 'null'
          title: Audio Embeds
        type:
          type: string
          const: audio_embeds
          title: Type
        uuid:
          anyOf:
            - type: string
            - type: 'null'
          title: Uuid
      additionalProperties: true
      type: object
      required:
        - type
      title: ChatCompletionContentPartAudioEmbedsParam
    CustomChatCompletionContentSimpleAudioParam:
      properties:
        audio_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Audio Url
      additionalProperties: true
      type: object
      title: CustomChatCompletionContentSimpleAudioParam
      description: |-
        A simpler version of the param that only accepts a plain audio_url.

        Example:
        {
            "audio_url": "https://example.com/audio.mp3"
        }
    CustomChatCompletionContentSimpleVideoParam:
      properties:
        video_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Video Url
        uuid:
          anyOf:
            - type: string
            - type: 'null'
          title: Uuid
      additionalProperties: true
      type: object
      title: CustomChatCompletionContentSimpleVideoParam
      description: |-
        A simpler version of the param that only accepts a plain audio_url.

        Example:
        {
            "video_url": "https://example.com/video.mp4"
        }
    CustomThinkCompletionContentParam:
      properties:
        thinking:
          type: string
          title: Thinking
        closed:
          type: boolean
          title: Closed
        type:
          type: string
          const: thinking
          title: Type
      additionalProperties: true
      type: object
      required:
        - thinking
        - type
      title: CustomThinkCompletionContentParam
      description: >-
        A Think Completion Content Param that accepts a plain text and a
        boolean.


        Example:

        {
            "thinking": "I am thinking about the answer",
            "closed": True,
            "type": "thinking"
        }
    ChatCompletionFunctionToolParam:
      properties:
        function:
          $ref: >-
            #/components/schemas/openai__types__shared_params__function_definition__FunctionDefinition
        type:
          type: string
          const: function
          title: Type
      additionalProperties: true
      type: object
      required:
        - function
        - type
      title: ChatCompletionFunctionToolParam
      description: A function tool that can be used to generate a response.
    Author:
      properties:
        role:
          $ref: '#/components/schemas/Role'
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
      type: object
      required:
        - role
      title: Author
    Content:
      properties: {}
      type: object
      title: Content
    JsonSchemaResponseFormat:
      properties:
        name:
          type: string
          title: Name
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
        schema:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Schema
        strict:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Strict
      additionalProperties: true
      type: object
      required:
        - name
      title: JsonSchemaResponseFormat
    LegacyStructuralTag:
      properties:
        begin:
          type: string
          title: Begin
        schema:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Schema
        end:
          type: string
          title: End
      additionalProperties: true
      type: object
      required:
        - begin
        - end
      title: LegacyStructuralTag
    FunctionDefinition:
      properties:
        name:
          type: string
          title: Name
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
        parameters:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Parameters
      additionalProperties: true
      type: object
      required:
        - name
      title: FunctionDefinition
    ChatCompletionNamedFunction:
      properties:
        name:
          type: string
          title: Name
      additionalProperties: true
      type: object
      required:
        - name
      title: ChatCompletionNamedFunction
    ChatMessage:
      properties:
        role:
          type: string
          title: Role
        content:
          anyOf:
            - type: string
            - type: 'null'
          title: Content
        refusal:
          anyOf:
            - type: string
            - type: 'null'
          title: Refusal
        annotations:
          anyOf:
            - $ref: '#/components/schemas/Annotation'
            - type: 'null'
        audio:
          anyOf:
            - $ref: '#/components/schemas/ChatCompletionAudio'
            - type: 'null'
        function_call:
          anyOf:
            - $ref: '#/components/schemas/FunctionCall-Output'
            - type: 'null'
        tool_calls:
          items:
            $ref: '#/components/schemas/ToolCall'
          type: array
          title: Tool Calls
        reasoning:
          anyOf:
            - type: string
            - type: 'null'
          title: Reasoning
        reasoning_content:
          anyOf:
            - type: string
            - type: 'null'
          title: Reasoning Content
      additionalProperties: true
      type: object
      required:
        - role
      title: ChatMessage
    ChatCompletionLogProbs:
      properties:
        content:
          anyOf:
            - items:
                $ref: '#/components/schemas/ChatCompletionLogProbsContent'
              type: array
            - type: 'null'
          title: Content
      additionalProperties: true
      type: object
      title: ChatCompletionLogProbs
    PromptTokenUsageInfo:
      properties:
        cached_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Cached Tokens
      additionalProperties: true
      type: object
      title: PromptTokenUsageInfo
    ImageURL:
      properties:
        url:
          type: string
          title: Url
        detail:
          type: string
          enum:
            - auto
            - low
            - high
          title: Detail
      additionalProperties: true
      type: object
      required:
        - url
      title: ImageURL
    InputAudio:
      properties:
        data:
          type: string
          title: Data
        format:
          type: string
          enum:
            - wav
            - mp3
          title: Format
      additionalProperties: true
      type: object
      required:
        - data
        - format
      title: InputAudio
    FileFile:
      properties:
        file_data:
          type: string
          title: File Data
        file_id:
          type: string
          title: File Id
        filename:
          type: string
          title: Filename
      additionalProperties: true
      type: object
      title: FileFile
    Function:
      properties:
        arguments:
          type: string
          title: Arguments
        name:
          type: string
          title: Name
      additionalProperties: true
      type: object
      required:
        - arguments
        - name
      title: Function
      description: The function that the model called.
    Custom:
      properties:
        input:
          type: string
          title: Input
        name:
          type: string
          title: Name
      additionalProperties: true
      type: object
      required:
        - input
        - name
      title: Custom
      description: The custom tool that the model called.
    AudioURL:
      properties:
        url:
          type: string
          title: Url
      additionalProperties: true
      type: object
      required:
        - url
      title: AudioURL
    VideoURL:
      properties:
        url:
          type: string
          title: Url
      additionalProperties: true
      type: object
      required:
        - url
      title: VideoURL
    openai__types__shared_params__function_definition__FunctionDefinition:
      properties:
        name:
          type: string
          title: Name
        description:
          type: string
          title: Description
        parameters:
          additionalProperties: true
          type: object
          title: Parameters
        strict:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Strict
      additionalProperties: true
      type: object
      required:
        - name
      title: FunctionDefinition
    Role:
      type: string
      enum:
        - user
        - assistant
        - system
        - developer
        - tool
      title: Role
      description: The role of a message author (mirrors ``chat::Role``).
    Annotation:
      properties:
        type:
          type: string
          const: url_citation
          title: Type
        url_citation:
          $ref: '#/components/schemas/AnnotationURLCitation'
      additionalProperties: true
      type: object
      required:
        - type
        - url_citation
      title: Annotation
      description: A URL citation when using web search.
    ChatCompletionAudio:
      properties:
        id:
          type: string
          title: Id
        data:
          type: string
          title: Data
        expires_at:
          type: integer
          title: Expires At
        transcript:
          type: string
          title: Transcript
      additionalProperties: true
      type: object
      required:
        - id
        - data
        - expires_at
        - transcript
      title: ChatCompletionAudio
      description: >-
        If the audio output modality is requested, this object contains data

        about the audio response from the model. [Learn
        more](https://platform.openai.com/docs/guides/audio).
    FunctionCall-Output:
      properties:
        name:
          type: string
          title: Name
        arguments:
          type: string
          title: Arguments
      additionalProperties: true
      type: object
      required:
        - name
        - arguments
      title: FunctionCall
    ToolCall:
      properties:
        id:
          type: string
          title: Id
        type:
          type: string
          const: function
          title: Type
          default: function
        function:
          $ref: '#/components/schemas/FunctionCall-Output'
      additionalProperties: true
      type: object
      required:
        - function
      title: ToolCall
    ChatCompletionLogProbsContent:
      properties:
        token:
          type: string
          title: Token
        logprob:
          type: number
          title: Logprob
          default: -9999
        bytes:
          anyOf:
            - items:
                type: integer
              type: array
            - type: 'null'
          title: Bytes
        top_logprobs:
          items:
            $ref: '#/components/schemas/ChatCompletionLogProb'
          type: array
          title: Top Logprobs
      additionalProperties: true
      type: object
      required:
        - token
      title: ChatCompletionLogProbsContent
    AnnotationURLCitation:
      properties:
        end_index:
          type: integer
          title: End Index
        start_index:
          type: integer
          title: Start Index
        title:
          type: string
          title: Title
        url:
          type: string
          title: Url
      additionalProperties: true
      type: object
      required:
        - end_index
        - start_index
        - title
        - url
      title: AnnotationURLCitation
      description: A URL citation when using web search.
    ChatCompletionLogProb:
      properties:
        token:
          type: string
          title: Token
        logprob:
          type: number
          title: Logprob
          default: -9999
        bytes:
          anyOf:
            - items:
                type: integer
              type: array
            - type: 'null'
          title: Bytes
      additionalProperties: true
      type: object
      required:
        - token
      title: ChatCompletionLogProb
  securitySchemes:
    HTTPBearer:
      type: http
      scheme: bearer

````