# Source: https://docs.edenai.co/v3/how-to/llm/chat-completions.md

# Source: https://docs.edenai.co/api-reference/completions/chat-completions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Chat Completions

> OpenAI-compatible chat completions endpoint (v3).



## OpenAPI

````yaml openapi/v3-openapi.json post /v3/llm/chat/completions
openapi: 3.1.0
info:
  title: Eden AI API V3
  version: 3.0.0
servers:
  - url: https://api.edenai.run
    description: Production server
security: []
paths:
  /v3/llm/chat/completions:
    post:
      tags:
        - Completions
      summary: Chat Completions
      description: OpenAI-compatible chat completions endpoint (v3).
      operationId: chat_completions_v3_llm_chat_completions_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LlmFeatureBody'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - AuthBearer: []
components:
  schemas:
    LlmFeatureBody:
      properties:
        model:
          type: string
          title: Model
          description: The name of the LLM model to use.
        messages:
          items:
            $ref: '#/components/schemas/Message'
          type: array
          title: Messages
          description: The messages to send to the LLM model.
        router_candidates:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Router Candidates
          description: >-
            List of model candidates for dynamic routing when using
            model='@edenai'. If not provided, defaults to all available models.
        'n':
          anyOf:
            - type: integer
              minimum: 1
            - type: 'null'
          title: 'N'
          description: >-
            The number of completions to generate for each prompt. Defaults to
            1.
          default: 1
        reasoning_effort:
          anyOf:
            - type: string
              enum:
                - low
                - medium
                - high
            - type: 'null'
          title: Reasoning Effort
          description: The reasoning effort level for the LLM model.
        metadata:
          anyOf:
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
          title: Metadata
          description: |-
            list of metadata associated with the chat request. 
            Can be used to provide additional context or tracking information.
        frequency_penalty:
          anyOf:
            - type: number
              maximum: 2
              minimum: -2
            - type: 'null'
          title: Frequency Penalty
          description: Penalty for repeated tokens in the output.
        logit_bias:
          anyOf:
            - additionalProperties:
                type: number
              type: object
            - type: 'null'
          title: Logit Bias
          description: Logit bias to influence token generation.
        logprobs:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Logprobs
          description: >-
            Whether to include log probabilities of tokens in the output.
            Defaults to False.
          default: false
        top_logprobs:
          anyOf:
            - type: integer
              maximum: 20
              minimum: 1
            - type: 'null'
          title: Top Logprobs
          description: Number of top log probabilities to return with each token.
        max_tokens:
          anyOf:
            - type: integer
              minimum: 1
            - type: 'null'
          title: Max Tokens
          description: The maximum number of tokens to generate in the chat completion
        max_completion_tokens:
          anyOf:
            - type: integer
              minimum: 1
            - type: 'null'
          title: Max Completion Tokens
          description: >-
            An upper bound for the number of tokens that can be generated for a
            completion, including visible output tokens and reasoning tokens.
        modalities:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Modalities
          description: List of supported input/output modalities for the chat.
        prediction:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Prediction
          description: field for storing prediction-related information.
        audio:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Audio
          description: dictionary for audio-related parameters or metadata.
        presence_penalty:
          anyOf:
            - type: number
              maximum: 2
              minimum: -2
            - type: 'null'
          title: Presence Penalty
          description: Penalty for new tokens based on their presence in the text so far.
        response_format:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Response Format
          description: Specify the desired response format for the completion.
        seed:
          anyOf:
            - type: integer
            - type: 'null'
          title: Seed
          description: Seed for random number generation.
        service_tier:
          anyOf:
            - type: string
              enum:
                - auto
                - default
            - type: 'null'
          title: Service Tier
          description: |-
            'auto': Automatically select appropriate tier
            'default': Use the default service tier
        stop:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Stop
          description: List of stop sequences to end the generation.
        stream:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Stream
          description: Whether to stream the response in real-time. Defaults to False.
          default: false
        stream_options:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Stream Options
          description: Options for streaming responses, such as chunk size or format.
        temperature:
          anyOf:
            - type: number
              maximum: 2
              minimum: 0
            - type: 'null'
          title: Temperature
          description: Sampling temperature for controlling randomness in output.
        top_p:
          anyOf:
            - type: number
              maximum: 1
              minimum: 0
            - type: 'null'
          title: Top P
          description: >-
            Nucleus sampling parameter for controlling diversity in output.
            Defaults to 1.0.
          default: 1
        tools:
          anyOf:
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
          title: Tools
          description: >-
            List of tools that can be used by the model to assist in generating
            responses.
        tool_choice:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/ToolChoiceFunction'
            - type: 'null'
          title: Tool Choice
          description: >-
            Specify how tools should be used. Can be 'auto', 'required', 'none',
            or an object like {'type': 'function', 'function': {'name':
            'tool_name'}} to force a specific tool.
        parallel_tool_calls:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Parallel Tool Calls
          description: Whether to allow parallel tool calls in the completion.
        user:
          anyOf:
            - type: string
            - type: 'null'
          title: User
          description: User identifier for tracking or personalization purposes.
        function_call:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Function Call
          description: >-
            Function call parameters for invoking specific functions during the
            chat.
        functions:
          anyOf:
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
          title: Functions
          description: >-
            List of functions that can be called by the model to assist in
            generating responses.
        thinking:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Thinking
          description: Parameters related to the model's reasoning or thinking process.
        web_search_options:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Web Search Options
          description: >-
            Options for web search integration. Example: json
            web_search_options={ "search_context_size": "medium" # Options:
            "low", "medium", "high" }
        verbosity:
          anyOf:
            - type: string
              enum:
                - low
                - medium
                - high
            - type: 'null'
          title: Verbosity
          description: >-
            Hint the model to be more or less expansive in its replies. Values:
            "low", "medium", "high". low (gpt5 models)
      type: object
      required:
        - model
        - messages
      title: LlmFeatureBody
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    Message:
      properties:
        role:
          type: string
          enum:
            - user
            - assistant
            - system
            - tool
          title: Role
          description: The role of the message sender (e.g., 'user', 'assistant').
        content:
          anyOf:
            - type: string
            - items:
                anyOf:
                  - $ref: '#/components/schemas/MessageTextContent'
                  - $ref: '#/components/schemas/MessageImageContent'
                  - $ref: '#/components/schemas/MessageFileContent'
              type: array
            - type: 'null'
          title: Content
          description: The content of the message, either text or image.
      additionalProperties: true
      type: object
      required:
        - role
        - content
      title: Message
    ToolChoiceFunction:
      properties:
        type:
          type: string
          const: function
          title: Type
        function:
          $ref: '#/components/schemas/ToolChoiceFunctionName'
          description: The function to force the model to call.
      type: object
      required:
        - type
        - function
      title: ToolChoiceFunction
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
    MessageTextContent:
      properties:
        type:
          type: string
          const: text
          title: Type
        text:
          type: string
          minLength: 1
          title: Text
          description: The text content of the message.
      type: object
      required:
        - type
        - text
      title: MessageTextContent
    MessageImageContent:
      properties:
        type:
          type: string
          const: image_url
          title: Type
        image_url:
          $ref: '#/components/schemas/MessageImageUrl'
      type: object
      required:
        - type
        - image_url
      title: MessageImageContent
    MessageFileContent:
      properties:
        type:
          type: string
          const: file
          title: Type
        file:
          anyOf:
            - $ref: '#/components/schemas/MessageFileUrlInput'
            - $ref: '#/components/schemas/MessageFileB64Input'
          title: File
      type: object
      required:
        - type
        - file
      title: MessageFileContent
    ToolChoiceFunctionName:
      properties:
        name:
          type: string
          title: Name
          description: The name of the function to call.
      type: object
      required:
        - name
      title: ToolChoiceFunctionName
    MessageImageUrl:
      properties:
        url:
          type: string
          title: Url
      type: object
      required:
        - url
      title: MessageImageUrl
    MessageFileUrlInput:
      properties:
        file_id:
          type: string
          title: File Id
          description: >-
            File identifier: either a UUID from /v3/upload endpoint or an
            HTTP(S) URL.
      type: object
      required:
        - file_id
      title: MessageFileUrlInput
    MessageFileB64Input:
      properties:
        file_data:
          type: string
          title: File Data
          description: The file data in base64 format.
      type: object
      required:
        - file_data
      title: MessageFileB64Input
  securitySchemes:
    AuthBearer:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).