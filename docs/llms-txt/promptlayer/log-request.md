# Source: https://docs.promptlayer.com/reference/log-request.md

# Log Request

Log a request to the system. This is useful for logging requests from custom LLM providers.

## Using Structured Outputs

When logging requests that use structured outputs (JSON schemas), include the schema configuration in the `parameters` field using the `response_format.json_schema` structure.

**Example:**

```json  theme={null}
{
  "provider": "openai",
  "model": "gpt-4",
  "api_type": "chat-completions"
  "parameters": {
    "temperature": 0.7,
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "YourSchemaName",
        "schema": {
          "type": "object",
          "properties": {
            "field1": {"type": "string"}
          },
          "required": ["field1"]
        }
      }
    }
  }
}
```

For complete examples with OpenAI, Anthropic, Google Gemini, and detailed implementation guidance, see:

**[Logging Structured Outputs Guide →](/features/prompt-history/structured-output-logging)**

## Related Documentation

* [Custom Logging Guide](/features/prompt-history/custom-logging) - General guide to logging requests
* [Structured Outputs in Prompt Registry](/features/prompt-registry/structured-outputs) - Creating prompts with structured outputs
* [Metadata Documentation](/features/prompt-history/metadata) - Using metadata for tracking


## OpenAPI

````yaml POST /log-request
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /log-request:
    post:
      tags:
        - request
      summary: Log Request
      operationId: logRequest
      parameters:
        - name: X-API-KEY
          in: header
          required: true
          schema:
            type: string
            title: X-Api-Key
          description: API key to authorize the operation.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LogRequest'
      responses:
        '201':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LogRequestResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                anyOf:
                  - $ref: '#/components/schemas/BadRequestError'
                  - $ref: '#/components/schemas/ValidationError'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BadRequestError'
components:
  schemas:
    LogRequest:
      properties:
        provider:
          title: Provider
          type: string
        model:
          title: Model
          type: string
        input:
          discriminator:
            mapping:
              chat: '#/components/schemas/ChatPrompt'
              completion: '#/components/schemas/CompletionPrompt'
            propertyName: type
          oneOf:
            - $ref: '#/components/schemas/CompletionPrompt'
            - $ref: '#/components/schemas/ChatPrompt'
          title: Input
        output:
          discriminator:
            mapping:
              chat: '#/components/schemas/ChatPrompt'
              completion: '#/components/schemas/CompletionPrompt'
            propertyName: type
          oneOf:
            - $ref: '#/components/schemas/CompletionPrompt'
            - $ref: '#/components/schemas/ChatPrompt'
          title: Output
        request_start_time:
          format: date-time
          title: Request Start Time
          type: string
        request_end_time:
          format: date-time
          title: Request End Time
          type: string
        parameters:
          default: {}
          title: Parameters
          type: object
          description: >-
            Model parameters including temperature, max_tokens, etc. Can also
            include structured output configuration via
            response_format.json_schema. See documentation for structured output
            examples.
        tags:
          default: []
          items:
            maxLength: 512
            type: string
          title: Tags
          type: array
        metadata:
          additionalProperties:
            type: string
          default: {}
          title: Metadata
          type: object
          description: >-
            Custom key-value pairs for tracking additional request information.
            Keys are limited to 1024 characters.
        prompt_name:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          title: Prompt Name
        prompt_id:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          title: Prompt Id
          description: >-
            The ID of the prompt template used for this request. This is useful
            for tracking which prompt was used in the request.
        prompt_version_number:
          anyOf:
            - type: integer
              exclusiveMinimum: 0
            - type: 'null'
          default: null
          title: Prompt Version Number
        prompt_input_variables:
          default: {}
          title: Prompt Input Variables
          type: object
        input_tokens:
          default: 0
          minimum: 0
          title: Input Tokens
          type: integer
        output_tokens:
          default: 0
          minimum: 0
          title: Output Tokens
          type: integer
        price:
          default: 0
          minimum: 0
          title: Price
          type: number
        function_name:
          default: ''
          title: Function Name
          type: string
        score:
          default: 0
          maximum: 100
          minimum: 0
          title: Score
          type: integer
        api_type:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          title: Api Type
      required:
        - provider
        - model
        - input
        - output
        - request_start_time
        - request_end_time
      title: LogRequest
      type: object
    LogRequestResponse:
      properties:
        id:
          type: integer
          title: Id
        prompt_version:
          $ref: '#/components/schemas/PromptVersion'
      required:
        - id
        - prompt_version
      title: LogRequestResponse
      type: object
    BadRequestError:
      properties:
        success:
          const: false
          default: false
          enum:
            - false
          title: Success
          type: boolean
        message:
          type: string
          title: Message
      required:
        - message
      title: BadRequestError
      type: object
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
    PromptVersion:
      properties:
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
        commit_message:
          anyOf:
            - type: string
              maxLength: 72
            - type: 'null'
          title: Commit Message
        metadata:
          anyOf:
            - $ref: '#/components/schemas/Metadata'
            - type: 'null'
      type: object
      required:
        - prompt_template
      title: PromptVersion
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

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt