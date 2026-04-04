# Source: https://docs.fireworks.ai/api-reference/get-response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Response



## OpenAPI

````yaml get /v1/responses/{response_id}
openapi: 3.1.0
info:
  title: Gateway REST API
  version: 4.21.6
servers: []
security: []
tags:
  - name: gateway.openapi_Gateway
    x-displayName: Gateway
  - name: gateway-extra.openapi_Gateway
    x-displayName: Gateway
  - name: responses.openapi_other
    x-displayName: other
  - name: text-completion.openapi_other
    x-displayName: other
paths:
  /v1/responses/{response_id}:
    servers:
      - url: https://api.fireworks.ai/inference
    get:
      tags:
        - responses.openapi_other
      summary: Get Response
      operationId: get_response_v1_responses__response_id__get
      parameters:
        - name: response_id
          in: path
          required: true
          schema:
            type: string
            title: Response Id
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Response'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - BearerAuth: []
components:
  schemas:
    Response:
      properties:
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
          description: The unique identifier of the response. Will be None if store=False.
        object:
          type: string
          title: Object
          description: The object type, which is always 'response'.
          default: response
        created_at:
          type: integer
          title: Created At
          description: The Unix timestamp (in seconds) when the response was created.
        status:
          type: string
          title: Status
          description: >-
            The status of the response. Can be 'completed', 'in_progress',
            'incomplete', 'failed', or 'cancelled'.
        model:
          type: string
          title: Model
          description: >-
            The model used to generate the response (e.g.,
            `accounts/<ACCOUNT_ID>/models/<MODEL_ID>`).
        output:
          items:
            anyOf:
              - $ref: '#/components/schemas/Message'
              - $ref: '#/components/schemas/ToolCall'
              - $ref: '#/components/schemas/ToolOutput'
          type: array
          title: Output
          description: >-
            An array of output items produced by the model. Can contain
            messages, tool calls, and tool outputs.
        previous_response_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Previous Response Id
          description: >-
            The ID of the previous response in the conversation, if this
            response continues a conversation.
        usage:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Usage
          description: >-
            Token usage information for the request. Contains 'prompt_tokens',
            'completion_tokens', and 'total_tokens'.
        error:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Error
          description: >-
            Error information if the response failed. Contains 'type', 'code',
            and 'message' fields.
        incomplete_details:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Incomplete Details
          description: >-
            Details about why the response is incomplete, if status is
            'incomplete'. Contains 'reason' field which can be
            'max_output_tokens', 'max_tool_calls', or 'content_filter'.
        instructions:
          anyOf:
            - type: string
            - type: 'null'
          title: Instructions
          description: >-
            System instructions that guide the model's behavior. Similar to a
            system message.
        max_output_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Output Tokens
          description: >-
            The maximum number of tokens that can be generated in the response.
            Must be at least 1.
        max_tool_calls:
          anyOf:
            - type: integer
              minimum: 1
            - type: 'null'
          title: Max Tool Calls
          description: >-
            The maximum number of tool calls allowed in a single response. Must
            be at least 1.
        parallel_tool_calls:
          type: boolean
          title: Parallel Tool Calls
          description: >-
            Whether to enable parallel function calling during tool use. Default
            is True.
          default: true
        reasoning:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Reasoning
          description: >-
            Reasoning output from the model, if reasoning is enabled. Contains
            'content' and 'type' fields.
        store:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Store
          description: >-
            Whether to store this response for future retrieval. If False, the
            response will not be persisted and previous_response_id cannot
            reference it. Default is True.
          default: true
        temperature:
          type: number
          maximum: 2
          minimum: 0
          title: Temperature
          description: >-
            The sampling temperature to use, between 0 and 2. Higher values like
            0.8 make output more random, while lower values like 0.2 make it
            more focused and deterministic. Default is 1.0.
          default: 1
        text:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Text
          description: Text generation configuration parameters, if applicable.
        tool_choice:
          anyOf:
            - type: string
            - additionalProperties: true
              type: object
          title: Tool Choice
          description: >-
            Controls which (if any) tool the model should use. Can be 'none',
            'auto', 'required', or an object specifying a particular tool.
            Default is 'auto'.
          default: auto
        tools:
          items:
            additionalProperties: true
            type: object
          type: array
          title: Tools
          description: >-
            A list of tools the model may call. Each tool is defined with a type
            and function specification following the OpenAI tool format.
            Supports 'function', 'mcp', 'sse', and 'python' tool types.
        top_p:
          type: number
          maximum: 1
          minimum: 0
          title: Top P
          description: >-
            An alternative to temperature sampling, called nucleus sampling,
            where the model considers the results of tokens with top_p
            probability mass. So 0.1 means only tokens comprising the top 10%
            probability mass are considered. Default is 1.0.
          default: 1
        truncation:
          type: string
          title: Truncation
          description: >-
            The truncation strategy to use for the context. Can be 'auto' or
            'disabled'. Default is 'disabled'.
          default: disabled
        user:
          anyOf:
            - type: string
            - type: 'null'
          title: User
          description: >-
            A unique identifier representing your end-user, which can help
            Fireworks to monitor and detect abuse.
        metadata:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Metadata
          description: >-
            Set of up to 16 key-value pairs that can be attached to the
            response. Useful for storing additional information about the
            response in a structured format.
      type: object
      required:
        - created_at
        - status
        - model
        - output
      title: Response
      description: >-
        Represents a response object returned from the API.


        A response includes the model output, token usage, configuration
        parameters,

        and metadata about the conversation state.
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
        id:
          type: string
          title: Id
          description: The unique identifier of the message.
        type:
          type: string
          title: Type
          description: The object type, always 'message'.
          default: message
        role:
          type: string
          title: Role
          description: >-
            The role of the message sender. Can be 'user', 'assistant', or
            'system'.
        content:
          items:
            $ref: '#/components/schemas/MessageContent'
          type: array
          title: Content
          description: >-
            An array of content parts that make up the message. Each part has a
            type and associated data.
        status:
          type: string
          title: Status
          description: The status of the message. Can be 'in_progress' or 'completed'.
      type: object
      required:
        - id
        - role
        - content
        - status
      title: Message
      description: Represents a message in a conversation.
    ToolCall:
      properties:
        id:
          type: string
          title: Id
          description: The unique identifier of the tool call.
        type:
          type: string
          title: Type
          description: The type of tool call. Can be 'function_call' or 'mcp_call'.
        call_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Call Id
          description: >-
            The call ID for function calls, used to match with
            function_call_output.
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
          description: The name of the function to call (for function_call type).
        arguments:
          anyOf:
            - type: string
            - type: 'null'
          title: Arguments
          description: >-
            The arguments for the function call as a JSON string (for
            function_call type).
        status:
          anyOf:
            - type: string
            - type: 'null'
          title: Status
          description: >-
            The status of the tool call. Can be 'in_progress', 'completed', or
            'incomplete'.
        function:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Function
          description: >-
            The function definition for function tool calls. Contains 'name' and
            'arguments' keys. Deprecated for function_call type.
        mcp:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Mcp
          description: >-
            The MCP (Model Context Protocol) tool call definition for MCP tool
            calls.
      type: object
      required:
        - id
        - type
      title: ToolCall
      description: Represents a tool call made by the model.
    ToolOutput:
      properties:
        type:
          type: string
          title: Type
          description: The object type, always 'tool_output'.
          default: tool_output
        tool_call_id:
          type: string
          title: Tool Call Id
          description: The ID of the tool call that this output corresponds to.
        output:
          type: string
          title: Output
          description: The output content from the tool execution.
      type: object
      required:
        - tool_call_id
        - output
      title: ToolOutput
      description: Represents the output/result of a tool call.
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
    MessageContent:
      properties:
        type:
          type: string
          title: Type
          description: >-
            The type of the content part. Can be 'input_text', 'output_text',
            'image', etc.
        text:
          anyOf:
            - type: string
            - type: 'null'
          title: Text
          description: The text content, if applicable.
      type: object
      required:
        - type
      title: MessageContent
      description: Represents a piece of content within a message.
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>

````