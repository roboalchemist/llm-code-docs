# Source: https://docs.promptlayer.com/reference/list-prompt-templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Prompt Templates

Get a paginated list of all prompt templates in your workspace.

### Filtering

* **label**: Filter prompt templates by release label (e.g., 'prod', 'dev', 'staging')
* **name**: Filter prompt templates by name (case-insensitive partial match)

### Filtering by Status

Use the `status` parameter to control which prompt templates are returned based on their deletion status:

* `active` (default): Returns only active prompt templates
* `deleted`: Returns only deleted/archived prompt templates
* `all`: Returns both active and deleted prompt templates

### Authentication

This endpoint requires API key authentication via the `X-API-KEY` header.


## OpenAPI

````yaml GET /prompt-templates
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /prompt-templates:
    get:
      tags:
        - prompt-templates
      summary: Get All
      operationId: get_all_prompt_templates__get
      parameters:
        - required: true
          schema:
            type: string
            title: X-Api-Key
          name: X-API-KEY
          in: header
        - in: query
          name: page
          schema:
            type: integer
            title: Page
        - in: query
          name: per_page
          schema:
            type: integer
            title: Per Page
        - in: query
          name: label
          schema:
            type: string
            title: Label
          description: >-
            Filter prompt templates by release label (e.g., 'prod', 'dev',
            'staging')
        - in: query
          name: name
          schema:
            type: string
            title: Name
          description: Filter prompt templates by name (case-insensitive partial match)
        - in: query
          name: status
          schema:
            type: string
            enum:
              - active
              - deleted
              - all
            default: active
            title: Status
          description: >-
            Filter prompt templates by status: 'active' (default) returns only
            active templates, 'deleted' returns only deleted/archived templates,
            'all' returns both
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListPromptTemplates'
components:
  schemas:
    ListPromptTemplates:
      properties:
        has_next:
          type: boolean
          title: Has Next
        has_prev:
          type: boolean
          title: Has Prev
        items:
          items:
            $ref: '#/components/schemas/GetPromptTemplateResponse'
          type: array
          title: Items
        next_num:
          type: integer
          title: Next Num
        prev_num:
          type: integer
          title: Prev Num
        page:
          type: integer
          title: Page
        pages:
          type: integer
          title: Pages
        total:
          type: integer
          title: Total
      type: object
      required:
        - has_next
        - has_prev
        - items
        - next_num
        - prev_num
        - page
        - pages
        - total
      title: ListPromptTemplates
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
            kwargs to the provider's API directly. **Important:** This object's
            structure is provider-specific and may change without notice as LLM
            providers update their APIs. For stable, provider-agnostic prompt
            data, use `prompt_template` instead.
        version:
          type: integer
          title: Version
      type: object
      required:
        - id
        - prompt_name
        - prompt_template
      title: GetPromptTemplateResponse
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