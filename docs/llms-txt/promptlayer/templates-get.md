# Source: https://docs.promptlayer.com/reference/templates-get.md

# Get Prompt Template

Retrieve a prompt template using either the `prompt_name` or `prompt_id`. Optionally, specify `version` (version number) or `label` (release label like "prod") to retrieve a specific version. If not specified, the latest version is returned.

PromptLayer will try to read the model provider from the parameters you attached to the prompt template. You can optionally pass in a `provider` to override the one set in the Prompt Registry. This will return LLM-specific arguments that can be passed directly into your LLM client. To format the template with input variables, use `input_variables`.


## OpenAPI

````yaml POST /prompt-templates/{identifier}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /prompt-templates/{identifier}:
    post:
      tags:
        - prompt-templates
      summary: Get Prompt Template by ID
      operationId: get_prompt_templates__prompt_identifier__post
      parameters:
        - required: true
          schema:
            type: string
            title: X-Api-Key
          name: X-API-KEY
          in: header
        - name: identifier
          in: path
          required: true
          schema:
            type: string
            title: identifier
            description: The identifier can be either the prompt name or the prompt id.
      requestBody:
        content:
          application/json:
            schema:
              anyOf:
                - $ref: '#/components/schemas/GetPromptTemplate'
                - type: 'null'
              title: Body
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetPromptTemplateResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    GetPromptTemplate:
      properties:
        version:
          anyOf:
            - type: integer
              exclusiveMinimum: 0
            - type: 'null'
          title: Version
        workspace_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Workspace Id
        label:
          anyOf:
            - type: string
            - type: 'null'
          title: Label
        provider:
          anyOf:
            - type: string
              enum:
                - openai
                - anthropic
            - type: 'null'
          title: Provider
        input_variables:
          anyOf:
            - additionalProperties:
                type: string
              type: object
            - type: 'null'
          title: Input Variables
        metadata_filters:
          anyOf:
            - additionalProperties:
                type: string
              type: object
            - type: 'null'
          title: Metadata Filters
          description: Optional dictionary of key values used for A/B release labels.
        model:
          anyOf:
            - type: string
            - type: 'null'
          title: Modal
          description: >-
            Optional model name used for returning default parameters with
            llm_kwargs.
        model_parameter_overrides:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          default: null
          title: Model Parameter Overrides
          description: >-
            Optional dictionary of model parameter overrides to use with the
            prompt template. This will override the parameters at runtime for
            the specified model and will try to make sure the model supports
            these parameters. For example, if you supply `maxOutputTokens` for
            OpenAI, it will be converted to `max_completion_tokens`.
      type: object
      title: GetPromptTemplate
    GetPromptTemplateResponse:
      properties:
        id:
          type: integer
          title: Id
        prompt_name:
          type: string
          title: Prompt Name
        prompt_template:
          oneOf:
            - $ref: '#/components/schemas/CompletionPrompt'
            - $ref: '#/components/schemas/ChatPrompt'
          title: Prompt Template
          discriminator:
            propertyName: type
            mapping:
              chat: '#/components/schemas/ChatPrompt'
              completion: '#/components/schemas/CompletionPrompt'
        metadata:
          anyOf:
            - $ref: '#/components/schemas/Metadata'
            - type: 'null'
        commit_message:
          anyOf:
            - type: string
            - type: 'null'
          title: Commit Message
        llm_kwargs:
          anyOf:
            - type: object
            - type: 'null'
          title: Llm Kwargs
          description: >-
            When you optionally specify `provider` in the body, `llm_kwargs`
            will be returned for that specific provider and you can pass these
            kwargs to the provider's API directly.
        version:
          type: integer
          title: Version
      type: object
      required:
        - id
        - prompt_name
        - prompt_template
      title: GetPromptTemplateResponse
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    CompletionPrompt:
      additionalProperties: true
      properties:
        content:
          items:
            discriminator:
              mapping:
                image_url: '#/components/schemas/ImageContent'
                text: '#/components/schemas/TextContent'
                thinking: '#/components/schemas/ThinkingContent'
              propertyName: type
            oneOf:
              - $ref: '#/components/schemas/TextContent'
              - $ref: '#/components/schemas/ThinkingContent'
              - $ref: '#/components/schemas/ImageContent'
              - $ref: '#/components/schemas/MediaContent'
              - $ref: '#/components/schemas/MediaVariable'
          title: Content
          type: array
        input_variables:
          default: []
          items:
            type: string
          title: Input Variables
          type: array
        template_format:
          default: f-string
          enum:
            - f-string
            - jinja2
          title: Template Format
          type: string
        type:
          const: completion
          default: completion
          enum:
            - completion
          title: Type
          type: string
      required:
        - content
      title: Completion Template
      type: object
    ChatPrompt:
      properties:
        messages:
          items:
            discriminator:
              mapping:
                assistant: '#/components/schemas/AssistantMessage'
                function: '#/components/schemas/FunctionMessage'
                placeholder: '#/components/schemas/PlaceholderMessage'
                system: '#/components/schemas/SystemMessage'
                tool: '#/components/schemas/ToolMessage'
                user: '#/components/schemas/UserMessage'
                developer: '#/components/schemas/DeveloperMessage'
              propertyName: role
            oneOf:
              - $ref: '#/components/schemas/SystemMessage'
              - $ref: '#/components/schemas/UserMessage'
              - $ref: '#/components/schemas/AssistantMessage'
              - $ref: '#/components/schemas/FunctionMessage'
              - $ref: '#/components/schemas/ToolMessage'
              - $ref: '#/components/schemas/PlaceholderMessage'
              - $ref: '#/components/schemas/DeveloperMessage'
          title: Messages
          type: array
        functions:
          anyOf:
            - items:
                $ref: '#/components/schemas/Function'
              type: array
            - type: 'null'
          default: null
          title: Functions
        tools:
          anyOf:
            - items:
                $ref: '#/components/schemas/Tool'
              type: array
            - type: 'null'
          default: null
          title: Tools
        function_call:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/MessageFunctionCall'
            - type: 'null'
          default: null
          title: Function Call
        tool_choice:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/ChatToolChoice'
            - type: 'null'
          default: null
          title: Tool Choice
        type:
          const: chat
          default: chat
          enum:
            - chat
          title: Type
          type: string
        input_variables:
          default: []
          items:
            type: string
          title: Input Variables
          type: array
      required:
        - messages
      title: Chat Template
      type: object
    Metadata:
      title: Metadata
      type: object
      properties:
        model:
          $ref: '#/components/schemas/Model'
        customField:
          type: string
      definitions:
        Model:
          title: Model
          type: object
          properties:
            provider:
              title: Provider
              type: string
            name:
              title: Name
              type: string
            parameters:
              title: Parameters
              default: {}
              type: object
          required:
            - provider
            - name
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
    TextContent:
      properties:
        type:
          const: text
          default: text
          enum:
            - text
          title: Type
          type: string
        text:
          title: Text
          type: string
      required:
        - text
      title: TextContent
      type: object
    ThinkingContent:
      properties:
        type:
          const: thinking
          default: thinking
          enum:
            - thinking
          title: Type
          type: string
        thinking:
          title: Text
          type: string
      required:
        - thinking
      title: ThinkingContent
      type: object
    ImageContent:
      properties:
        type:
          const: image_url
          default: image_url
          enum:
            - image_url
          title: Type
          type: string
        image_url:
          $ref: '#/components/schemas/ImageURL'
        image_variable:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          title: Image Variable
      required:
        - image_url
      title: ImageContent
      type: object
    MediaContent:
      properties:
        type:
          const: media
          default: media
          enum:
            - media
          title: Type
          type: string
        media:
          $ref: '#/components/schemas/Media'
      required:
        - media
      title: MediaContent
      type: object
    MediaVariable:
      properties:
        type:
          const: media_variable
          default: media_variable
          enum:
            - media_variable
          title: Type
          type: string
        name:
          type: string
          title: Name
          description: Name of the media variable
      required:
        - name
      title: MediaVariable
      type: object
    SystemMessage:
      properties:
        input_variables:
          default: []
          items:
            type: string
          title: Input Variables
          type: array
        template_format:
          default: f-string
          enum:
            - f-string
            - jinja2
          title: Template Format
          type: string
        content:
          items:
            oneOf:
              - $ref: '#/components/schemas/TextContent'
              - $ref: '#/components/schemas/ImageContent'
              - $ref: '#/components/schemas/MediaContent'
              - $ref: '#/components/schemas/MediaVariable'
            discriminator:
              propertyName: type
              mapping:
                image_url: '#/components/schemas/ImageContent'
                text: '#/components/schemas/TextContent'
          type: array
          title: Content
        role:
          const: system
          title: Role
          default: system
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
      type: object
      required:
        - content
      title: SystemMessage
    UserMessage:
      properties:
        input_variables:
          default: []
          items:
            type: string
          title: Input Variables
          type: array
        template_format:
          default: f-string
          enum:
            - f-string
            - jinja2
          title: Template Format
          type: string
        content:
          items:
            oneOf:
              - $ref: '#/components/schemas/TextContent'
              - $ref: '#/components/schemas/ImageContent'
              - $ref: '#/components/schemas/MediaContent'
              - $ref: '#/components/schemas/MediaVariable'
            discriminator:
              propertyName: type
              mapping:
                image_url: '#/components/schemas/ImageContent'
                text: '#/components/schemas/TextContent'
          type: array
          title: Content
        role:
          const: user
          title: Role
          default: user
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
      type: object
      required:
        - content
      title: UserMessage
    AssistantMessage:
      properties:
        input_variables:
          default: []
          items:
            type: string
          title: Input Variables
          type: array
        template_format:
          default: f-string
          enum:
            - f-string
            - jinja2
          title: Template Format
          type: string
        content:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/TextContent'
                  - $ref: '#/components/schemas/ThinkingContent'
                  - $ref: '#/components/schemas/ImageContent'
                discriminator:
                  propertyName: type
                  mapping:
                    image_url: '#/components/schemas/ImageContent'
                    text: '#/components/schemas/TextContent'
                    thinking: '#/components/schemas/ThinkingContent'
              type: array
            - type: 'null'
          title: Content
        role:
          const: assistant
          title: Role
          default: assistant
        function_call:
          anyOf:
            - $ref: '#/components/schemas/FunctionCall'
            - type: 'null'
          title: Function Call
          deprecated: true
          description: >-
            This field is deprecated. Please use `tool_calls` field to specify
            tool calls.
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        tool_calls:
          anyOf:
            - items:
                $ref: '#/components/schemas/ToolCall'
              type: array
            - type: 'null'
          title: Tool Calls
      type: object
      title: AssistantMessage
    FunctionMessage:
      properties:
        input_variables:
          default: []
          items:
            type: string
          title: Input Variables
          type: array
        template_format:
          default: f-string
          enum:
            - f-string
            - jinja2
          title: Template Format
          type: string
        content:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/TextContent'
                  - $ref: '#/components/schemas/ImageContent'
                discriminator:
                  propertyName: type
                  mapping:
                    image_url: '#/components/schemas/ImageContent'
                    text: '#/components/schemas/TextContent'
              type: array
            - type: 'null'
          title: Content
        role:
          const: function
          title: Role
          default: function
        name:
          type: string
          title: Name
      type: object
      required:
        - name
      title: FunctionMessage
    ToolMessage:
      properties:
        input_variables:
          default: []
          items:
            type: string
          title: Input Variables
          type: array
        template_format:
          default: f-string
          enum:
            - f-string
            - jinja2
          title: Template Format
          type: string
        content:
          items:
            discriminator:
              mapping:
                image_url: '#/components/schemas/ImageContent'
                text: '#/components/schemas/TextContent'
                thinking: '#/components/schemas/ThinkingContent'
              propertyName: type
            oneOf:
              - $ref: '#/components/schemas/TextContent'
              - $ref: '#/components/schemas/ThinkingContent'
              - $ref: '#/components/schemas/ImageContent'
              - $ref: '#/components/schemas/MediaContent'
              - $ref: '#/components/schemas/MediaVariable'
          title: Content
          type: array
        role:
          const: tool
          title: Role
          default: tool
        tool_call_id:
          type: string
          title: Tool Call Id
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
      type: object
      required:
        - content
        - tool_call_id
      title: ToolMessage
    PlaceholderMessage:
      properties:
        input_variables:
          default: []
          items:
            type: string
          title: Input Variables
          type: array
        template_format:
          default: f-string
          enum:
            - f-string
            - jinja2
          title: Template Format
          type: string
        content:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/TextContent'
                  - $ref: '#/components/schemas/ImageContent'
                discriminator:
                  propertyName: type
                  mapping:
                    image_url: '#/components/schemas/ImageContent'
                    text: '#/components/schemas/TextContent'
              type: array
            - type: 'null'
          default: null
          title: Content
        raw_request_display_role:
          default: ''
          title: Raw Request Display Role
          type: string
        role:
          const: placeholder
          default: placeholder
          enum:
            - placeholder
          title: Role
          type: string
        name:
          type: string
          title: Name
      required:
        - name
      title: PlaceholderMessage
      type: object
    DeveloperMessage:
      properties:
        input_variables:
          default: []
          items:
            type: string
          title: Input Variables
          type: array
        template_format:
          default: f-string
          enum:
            - f-string
            - jinja2
          title: Template Format
          type: string
        content:
          items:
            oneOf:
              - $ref: '#/components/schemas/TextContent'
              - $ref: '#/components/schemas/ImageContent'
              - $ref: '#/components/schemas/MediaContent'
              - $ref: '#/components/schemas/MediaVariable'
            discriminator:
              propertyName: type
              mapping:
                image_url: '#/components/schemas/ImageContent'
                text: '#/components/schemas/TextContent'
          type: array
          title: Content
        role:
          const: developer
          title: Role
          default: developer
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
      type: object
      required:
        - content
      title: DeveloperMessage
    Function:
      properties:
        name:
          type: string
          title: Name
        description:
          type: string
          title: Description
          default: ''
        parameters:
          type: object
          title: Parameters
          default:
            type: object
            properties: {}
      type: object
      required:
        - name
      title: Function
    Tool:
      properties:
        type:
          const: function
          title: Type
          default: function
        function:
          $ref: '#/components/schemas/Function'
      type: object
      required:
        - function
      title: Tool
    MessageFunctionCall:
      properties:
        name:
          type: string
          title: Name
      type: object
      required:
        - name
      title: MessageFunctionCall
    ChatToolChoice:
      properties:
        type:
          const: function
          title: Type
          default: function
        function:
          $ref: '#/components/schemas/MessageFunctionCall'
      type: object
      required:
        - function
      title: ChatToolChoice
    Model:
      title: Model
      type: object
      properties:
        provider:
          title: Provider
          type: string
        name:
          type: string
          title: Name
        parameters:
          title: Parameters
          default: {}
          type: object
      required:
        - provider
        - name
    ImageURL:
      properties:
        url:
          type: string
          title: Url
        detail:
          anyOf:
            - type: string
            - type: 'null'
          title: Detail
      type: object
      required:
        - url
      title: ImageURL
    Media:
      properties:
        title:
          type: string
          title: Title
          description: Title of the media
        type:
          type: string
          title: Type
          description: Type of the media. For example, image/png
        url:
          type: string
          title: Url
      type: object
      required:
        - url
      title: ImageURL
    FunctionCall:
      properties:
        name:
          type: string
          title: Name
        arguments:
          type: string
          title: Arguments
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
          const: function
          title: Type
          default: function
        function:
          $ref: '#/components/schemas/FunctionCall'
      type: object
      required:
        - id
        - function
      title: ToolCall

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt