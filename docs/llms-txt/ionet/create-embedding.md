# Source: https://io.net/docs/reference/ai-models/create-embedding.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Embeddings

> Computes an embedding vector that encodes the input text.



## OpenAPI

````yaml openapi/ai-models/create-embedding.json post /api/v1/embeddings
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/v1/embeddings:
    post:
      tags:
        - OpenAI Compatible Developer API
      summary: Create Embedding
      operationId: create_embedding_v1_embeddings_post
      parameters:
        - name: token
          in: header
          required: false
          schema:
            type: string
            description: JWT token
            title: Token
          description: JWT token
        - name: Authorization
          in: header
          required: false
          schema:
            type: string
            description: io.net provided API Key
            title: Authorization
          description: io.net provided API Key
        - name: x-api-key
          in: header
          required: false
          schema:
            type: string
            description: API key set by an SDK client
            title: X-Api-Key
          description: API key set by an SDK client
      requestBody:
        required: true
        content:
          application/json:
            schema:
              anyOf:
                - $ref: '#/components/schemas/EmbeddingCompletionRequest'
                - $ref: '#/components/schemas/EmbeddingChatRequest'
              title: Request
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '404':
          description: Not found
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    EmbeddingCompletionRequest:
      properties:
        model:
          type: string
          title: Model
        input:
          anyOf:
            - items:
                type: integer
              type: array
            - items:
                items:
                  type: integer
                type: array
              type: array
            - type: string
            - items:
                type: string
              type: array
          title: Input
        encoding_format:
          type: string
          enum:
            - float
            - base64
          title: Encoding Format
          default: float
        dimensions:
          anyOf:
            - type: integer
            - type: 'null'
          title: Dimensions
        user:
          anyOf:
            - type: string
            - type: 'null'
          title: User
        truncate_prompt_tokens:
          anyOf:
            - type: integer
              minimum: 1
            - type: 'null'
          title: Truncate Prompt Tokens
        additional_data:
          anyOf:
            - {}
            - type: 'null'
          title: Additional Data
        add_special_tokens:
          type: boolean
          title: Add Special Tokens
          description: >-
            If true (the default), special tokens (e.g. BOS) will be added to
            the prompt.
          default: true
        priority:
          type: integer
          title: Priority
          description: >-
            The priority of the request (lower means earlier handling; default:
            0). Any priority other than 0 will raise an error if the served
            model does not use priority scheduling.
          default: 0
      additionalProperties: true
      type: object
      required:
        - model
        - input
      title: EmbeddingCompletionRequest
    EmbeddingChatRequest:
      properties:
        model:
          type: string
          title: Model
        messages:
          items:
            anyOf:
              - $ref: '#/components/schemas/ChatCompletionDeveloperMessageParam'
              - $ref: '#/components/schemas/ChatCompletionSystemMessageParam'
              - $ref: '#/components/schemas/ChatCompletionUserMessageParam'
              - $ref: '#/components/schemas/ChatCompletionAssistantMessageParam'
              - $ref: '#/components/schemas/ChatCompletionToolMessageParam'
              - $ref: '#/components/schemas/ChatCompletionFunctionMessageParam'
          type: array
          title: Messages
        encoding_format:
          type: string
          enum:
            - float
            - base64
          title: Encoding Format
          default: float
        dimensions:
          anyOf:
            - type: integer
            - type: 'null'
          title: Dimensions
        user:
          anyOf:
            - type: string
            - type: 'null'
          title: User
        truncate_prompt_tokens:
          anyOf:
            - type: integer
              minimum: 1
            - type: 'null'
          title: Truncate Prompt Tokens
        additional_data:
          anyOf:
            - {}
            - type: 'null'
          title: Additional Data
        add_special_tokens:
          type: boolean
          title: Add Special Tokens
          description: >-
            If true, special tokens (e.g. BOS) will be added to the prompt on
            top of what is added by the chat template. For most models, the chat
            template takes care of adding the special tokens so this should be
            set to false (as is the default).
          default: false
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
            Additional kwargs to pass to the template renderer. Will be
            accessible by the chat template.
        priority:
          type: integer
          title: Priority
          description: >-
            The priority of the request (lower means earlier handling; default:
            0). Any priority other than 0 will raise an error if the served
            model does not use priority scheduling.
          default: 0
      additionalProperties: true
      type: object
      required:
        - model
        - messages
      title: EmbeddingChatRequest
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
      type: object
      required:
        - content
        - role
      title: ChatCompletionDeveloperMessageParam
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
      type: object
      required:
        - content
        - role
      title: ChatCompletionSystemMessageParam
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
      type: object
      required:
        - content
        - role
      title: ChatCompletionUserMessageParam
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
            - $ref: '#/components/schemas/FunctionCall'
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
      type: object
      required:
        - role
      title: ChatCompletionAssistantMessageParam
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
      type: object
      required:
        - content
        - name
        - role
      title: ChatCompletionFunctionMessageParam
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
      type: object
      required:
        - text
        - type
      title: ChatCompletionContentPartTextParam
    ChatCompletionContentPartImageParam:
      properties:
        image_url:
          $ref: '#/components/schemas/ImageURL'
        type:
          type: string
          const: image_url
          title: Type
      type: object
      required:
        - image_url
        - type
      title: ChatCompletionContentPartImageParam
    ChatCompletionContentPartInputAudioParam:
      properties:
        input_audio:
          $ref: '#/components/schemas/InputAudio'
        type:
          type: string
          const: input_audio
          title: Type
      type: object
      required:
        - input_audio
        - type
      title: ChatCompletionContentPartInputAudioParam
    File:
      properties:
        file:
          $ref: '#/components/schemas/FileFile'
        type:
          type: string
          const: file
          title: Type
      type: object
      required:
        - file
        - type
      title: File
    Audio:
      properties:
        id:
          type: string
          title: Id
      type: object
      required:
        - id
      title: Audio
    ChatCompletionContentPartRefusalParam:
      properties:
        refusal:
          type: string
          title: Refusal
        type:
          type: string
          const: refusal
          title: Type
      type: object
      required:
        - refusal
        - type
      title: ChatCompletionContentPartRefusalParam
    FunctionCall:
      properties:
        arguments:
          type: string
          title: Arguments
        name:
          type: string
          title: Name
      type: object
      required:
        - arguments
        - name
      title: FunctionCall
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
      type: object
      required:
        - id
        - function
        - type
      title: ChatCompletionMessageFunctionToolCallParam
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
      type: object
      required:
        - id
        - custom
        - type
      title: ChatCompletionMessageCustomToolCallParam
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
      type: object
      required:
        - arguments
        - name
      title: Function
    Custom:
      properties:
        input:
          type: string
          title: Input
        name:
          type: string
          title: Name
      type: object
      required:
        - input
        - name
      title: Custom
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````