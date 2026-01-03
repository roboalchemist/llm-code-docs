# Source: https://docs.promptlayer.com/reference/spans-bulk.md

# Create Spans Bulk

Create multiple spans in bulk with optional log request for each span. This endpoint is used for creating observability spans from telemetry data.

## Request Body

The request body must contain a `spans` array, where each span can optionally include a `log_request` field to simultaneously create a request log associated with the span.

### Span Fields

* **name** (string, required): The name of the span
* **context** (object, required): Contains trace\_id, span\_id, and trace\_state
* **kind** (enum, required): One of SpanKind.CLIENT, SpanKind.CONSUMER, SpanKind.INTERNAL, SpanKind.PRODUCER, SpanKind.SERVER
* **parent\_id** (string, optional): The ID of the parent span
* **start\_time** (integer, required): Start time in nanoseconds since epoch
* **end\_time** (integer, required): End time in nanoseconds since epoch
* **status** (object, required): Contains status\_code (StatusCode.ERROR, StatusCode.OK, StatusCode.UNSET) and optional description
* **attributes** (object, required): Key-value pairs of span attributes
* **events** (array, optional): Array of span events
* **links** (array, optional): Array of span links
* **resource** (object, required): Contains attributes object and schema\_url
* **log\_request** (object, optional): Optional request log data to create alongside the span

### Log Request Fields (Optional)

When included, the `log_request` field creates a request log associated with the span:

* **provider** (string, required): The LLM provider (e.g., "openai", "anthropic")
* **model** (string, required): The model name
* **input** (object, required): The input template (chat or completion format)
* **output** (object, required): The output template (chat or completion format)
* **request\_start\_time** (datetime, required): ISO format datetime
* **request\_end\_time** (datetime, required): ISO format datetime
* **parameters** (object, optional): Model parameters used
* **tags** (array\[string], optional): Tags to associate with the request
* **metadata** (object, optional): Metadata key-value pairs
* **prompt\_name** (string, optional): Name of the prompt template
* **prompt\_version\_number** (integer, optional): Version number of the prompt
* **prompt\_input\_variables** (object, optional): Variables used in the prompt
* **input\_tokens** (integer, optional): Number of input tokens
* **output\_tokens** (integer, optional): Number of output tokens
* **price** (float, optional): Cost of the request
* **function\_name** (string, optional): Name of the function called
* **score** (integer, optional): Score between 0-100

## Response

Returns a JSON object with:

* **success** (boolean): Whether the operation succeeded
* **spans** (array): Array of created span objects
* **request\_logs** (array, optional): Array of created request log objects (only present if log\_request was provided)

## Example Request

```json  theme={null}
{
  "spans": [
    {
      "name": "llm_call",
      "context": {
        "trace_id": "d4b5e2a1-3c8f-4e9a-b7d6-1a2b3c4d5e6f",
        "span_id": "a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
        "trace_state": "promptlayer=enabled"
      },
      "kind": "SpanKind.CLIENT",
      "parent_id": "parent123",
      "start_time": 1630000000000000000,
      "end_time": 1630000001000000000,
      "status": {
        "status_code": "StatusCode.OK",
        "description": "Success"
      },
      "attributes": {
        "llm.provider": "openai",
        "llm.model": "gpt-3.5-turbo"
      },
      "resource": {
        "attributes": {
          "service.name": "my-app"
        },
        "schema_url": "https://opentelemetry.io/schemas/1.9.0"
      },
      "log_request": {
        "provider": "openai",
        "model": "gpt-3.5-turbo",
        "input": {
          "type": "chat",
          "messages": [
            {
              "role": "user",
              "content": [{"type": "text", "text": "Hello!"}]
            }
          ]
        },
        "output": {
          "type": "chat",
          "messages": [
            {
              "role": "assistant",
              "content": [{"type": "text", "text": "Hi there! How can I help you?"}]
            }
          ]
        },
        "request_start_time": "2024-01-20T10:00:00Z",
        "request_end_time": "2024-01-20T10:00:01Z",
        "prompt_name": "greeting_prompt",
        "prompt_version_number": 1,
        "input_tokens": 10,
        "output_tokens": 12,
        "tags": ["production", "greeting"],
        "metadata": {
          "user_id": "user123",
          "session": "abc123"
        }
      }
    }
  ]
}
```

## Notes

* Spans with names "openai.OpenAI" or "anthropic.Anthropic" are excluded from processing
* When `log_request` is provided, the created request log will be associated with the span via the span\_id
* If a prompt\_name is specified but not found, the span will still be created but the log\_request creation will be skipped for that span
* All operations are atomic - if any span creation fails, the entire batch is rolled back


## OpenAPI

````yaml POST /spans-bulk
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /spans-bulk:
    post:
      tags:
        - spans
      summary: Create Spans Bulk
      operationId: createSpansBulk
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
              $ref: '#/components/schemas/CreateSpansBulk'
      responses:
        '201':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateSpansBulkResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ValidationError'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    CreateSpansBulk:
      type: object
      properties:
        spans:
          type: array
          items:
            $ref: '#/components/schemas/Span'
          title: Spans
      required:
        - spans
      title: CreateSpansBulk
    CreateSpansBulkResponse:
      type: object
      properties:
        success:
          type: boolean
          title: Success
        spans:
          type: array
          items:
            type: object
          title: Spans
        request_logs:
          type: array
          items:
            type: object
          title: Request Logs
          nullable: true
      required:
        - success
        - spans
      title: CreateSpansBulkResponse
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
    Span:
      type: object
      properties:
        name:
          type: string
          title: Name
        context:
          $ref: '#/components/schemas/SpanContext'
        kind:
          $ref: '#/components/schemas/SpanKind'
        parent_id:
          type: string
          title: Parent ID
          nullable: true
        start_time:
          type: integer
          title: Start Time
        end_time:
          type: integer
          title: End Time
        status:
          $ref: '#/components/schemas/SpanStatus'
        attributes:
          type: object
          title: Attributes
        events:
          type: array
          items:
            type: object
          title: Events
          default: []
        links:
          type: array
          items:
            type: object
          title: Links
          default: []
        resource:
          $ref: '#/components/schemas/SpanResource'
        log_request:
          anyOf:
            - $ref: '#/components/schemas/LogRequest'
            - type: 'null'
          title: Log Request
          nullable: true
      required:
        - name
        - context
        - kind
        - start_time
        - end_time
        - status
        - attributes
        - resource
      title: Span
    SpanContext:
      type: object
      properties:
        trace_id:
          type: string
          title: Trace ID
        span_id:
          type: string
          title: Span ID
        trace_state:
          type: string
          title: Trace State
      required:
        - trace_id
        - span_id
        - trace_state
      title: SpanContext
    SpanKind:
      type: string
      enum:
        - SpanKind.CLIENT
        - SpanKind.CONSUMER
        - SpanKind.INTERNAL
        - SpanKind.PRODUCER
        - SpanKind.SERVER
      title: SpanKind
    SpanStatus:
      type: object
      properties:
        status_code:
          $ref: '#/components/schemas/StatusCode'
        description:
          type: string
          title: Description
          nullable: true
      required:
        - status_code
      title: SpanStatus
    SpanResource:
      type: object
      properties:
        attributes:
          type: object
          additionalProperties:
            type: string
          title: Attributes
        schema_url:
          type: string
          title: Schema URL
      required:
        - attributes
        - schema_url
      title: SpanResource
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
    StatusCode:
      type: string
      enum:
        - StatusCode.ERROR
        - StatusCode.OK
        - StatusCode.UNSET
      title: StatusCode
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