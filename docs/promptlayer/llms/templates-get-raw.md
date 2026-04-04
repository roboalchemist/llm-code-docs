# Source: https://docs.promptlayer.com/reference/templates-get-raw.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Prompt Template (Raw)

> Retrieve raw prompt template data without applying input variables. Designed for GitHub sync, local caching, and template inspection. By default, snippets are resolved (expanded). Use resolve_snippets=false to get the raw template with snippet references intact.

Retrieve raw prompt template data without applying input variables. This endpoint is designed for:

* **GitHub sync**: Use `resolve_snippets=false` to get the raw template with `@@@snippet@@@` references intact
* **Local caching**: Fetch resolved templates with optional `llm_kwargs` for offline use
* **Template inspection**: View template structure and metadata without executing

Unlike the [POST endpoint](/reference/templates-get), this GET endpoint does not accept `input_variables` or `provider` in a request body. Instead, it returns the raw template data with placeholders preserved.

### Query Parameters

| Parameter            | Type    | Default | Description                                                                                     |
| -------------------- | ------- | ------- | ----------------------------------------------------------------------------------------------- |
| `version`            | integer | -       | Specific version number. Mutually exclusive with `label`.                                       |
| `label`              | string  | -       | Release label name (e.g. `prod`). Mutually exclusive with `version`.                            |
| `resolve_snippets`   | boolean | `true`  | When `true`, snippets are expanded. When `false`, raw `@@@snippet@@@` references are preserved. |
| `include_llm_kwargs` | boolean | `false` | When `true`, includes provider-specific LLM API format in the response.                         |

### Caching

Responses are cached by default. To bypass the cache, send the `Cache-Control: no-cache` header.

<Warning>
  **Provider-Specific Schema Notice**

  The `llm_kwargs` field (when requested via `include_llm_kwargs=true`) is provider-specific and its structure may change without notice as LLM providers update their APIs.

  For stable, provider-agnostic prompt data, use `prompt_template` instead of `llm_kwargs`.
</Warning>

### Examples

```bash  theme={null}
# Default: resolved snippets, latest version
curl -H "X-API-KEY: your_api_key" \
  https://api.promptlayer.com/prompt-templates/my-prompt

# Raw template with snippet references (for GitHub sync)
curl -H "X-API-KEY: your_api_key" \
  "https://api.promptlayer.com/prompt-templates/my-prompt?resolve_snippets=false"

# With llm_kwargs (for local caching)
curl -H "X-API-KEY: your_api_key" \
  "https://api.promptlayer.com/prompt-templates/my-prompt?include_llm_kwargs=true"

# Specific version
curl -H "X-API-KEY: your_api_key" \
  "https://api.promptlayer.com/prompt-templates/my-prompt?version=2"

# By release label
curl -H "X-API-KEY: your_api_key" \
  "https://api.promptlayer.com/prompt-templates/my-prompt?label=prod"
```

### Authentication

This endpoint requires API key authentication via the `X-API-KEY` header.


## OpenAPI

````yaml GET /prompt-templates/{identifier}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /prompt-templates/{identifier}:
    get:
      tags:
        - prompt-templates
      summary: Get Prompt Template Raw Data
      description: >-
        Retrieve raw prompt template data without applying input variables.
        Designed for GitHub sync, local caching, and template inspection. By
        default, snippets are resolved (expanded). Use resolve_snippets=false to
        get the raw template with snippet references intact.
      operationId: get_prompt_template_raw
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
        - name: version
          in: query
          required: false
          schema:
            type: integer
            exclusiveMinimum: 0
            title: Version
            description: >-
              Specific version number to retrieve. Mutually exclusive with
              `label`.
        - name: label
          in: query
          required: false
          schema:
            type: string
            title: Label
            description: >-
              Release label name to retrieve (e.g. 'prod', 'staging'). Mutually
              exclusive with `version`.
        - name: resolve_snippets
          in: query
          required: false
          schema:
            type: boolean
            default: true
            title: Resolve Snippets
            description: >-
              When true (default), snippets are expanded in the returned
              prompt_template. When false, raw @@@snippet@@@ references are
              preserved.
        - name: include_llm_kwargs
          in: query
          required: false
          schema:
            type: boolean
            default: false
            title: Include LLM Kwargs
            description: >-
              When true, includes provider-specific llm_kwargs in the response.
              Requires model metadata to be set on the template.
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetPromptTemplateRawResponse'
        '404':
          description: Prompt template not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    GetPromptTemplateRawResponse:
      properties:
        success:
          type: boolean
          title: Success
        id:
          type: integer
          title: Id
          description: The prompt template ID.
        prompt_name:
          type: string
          title: Prompt Name
          description: The name of the prompt template.
        version:
          type: integer
          title: Version
          description: The version number of the prompt template.
        workspace_id:
          type: integer
          title: Workspace Id
          description: The workspace this prompt template belongs to.
        prompt_template:
          oneOf:
            - $ref: '#/components/schemas/CompletionPrompt'
            - $ref: '#/components/schemas/ChatPrompt'
          title: Prompt Template
          description: >-
            The prompt template content. When resolve_snippets is true
            (default), snippets are expanded. When false, raw @@@snippet@@@
            references are preserved.
          discriminator:
            propertyName: type
            mapping:
              chat: '#/components/schemas/ChatPrompt'
              completion: '#/components/schemas/CompletionPrompt'
        metadata:
          anyOf:
            - $ref: '#/components/schemas/Metadata'
            - type: 'null'
          description: Model configuration including provider, model name, and parameters.
        commit_message:
          anyOf:
            - type: string
            - type: 'null'
          title: Commit Message
          description: The commit message for this version.
        tags:
          type: array
          items:
            type: string
          title: Tags
          description: Tags associated with the prompt template.
        created_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Created At
          description: Timestamp when this version was created.
        snippets:
          type: array
          items:
            $ref: '#/components/schemas/SnippetReference'
          title: Snippets
          description: List of snippet references used in this template.
        llm_kwargs:
          anyOf:
            - type: object
            - type: 'null'
          title: LLM Kwargs
          description: >-
            Provider-specific LLM arguments. Only present when
            include_llm_kwargs=true. Structure is provider-specific and may
            change without notice.
      type: object
      required:
        - success
        - id
        - prompt_name
        - version
        - workspace_id
        - prompt_template
        - snippets
      title: GetPromptTemplateRawResponse
    ErrorResponse:
      type: object
      properties:
        success:
          type: boolean
          default: false
          description: Indicates that the request failed.
        error:
          type: string
          description: Error message explaining why the request failed.
      required:
        - success
        - error
      description: Error response format.
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
    SnippetReference:
      properties:
        prompt_name:
          type: string
          title: Prompt Name
          description: The name of the snippet prompt template.
        version:
          type: integer
          title: Version
          description: The version number of the snippet used.
        label:
          anyOf:
            - type: string
            - type: 'null'
          title: Label
          description: The release label of the snippet, if applicable.
      type: object
      required:
        - prompt_name
        - version
      title: SnippetReference
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