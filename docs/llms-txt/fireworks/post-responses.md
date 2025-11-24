# Source: https://docs.fireworks.ai/api-reference/post-responses.md

# Create Response

> Creates a model response, optionally interacting with custom tools via the Model Context Protocol (MCP). This endpoint supports conversational continuation and streaming.

Explore our cookbooks for detailed examples:

- [Basic MCP Usage](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_mcp_examples.ipynb)
- [Streaming with MCP](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_mcp_with_streaming.ipynb)
- [Conversational History with `previous_response_id`](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_previous_response_cookbook.ipynb)
- [Basic Streaming](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_streaming_example.ipynb)
- [Controlling Response Storage](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/mcp_server_with_store_false_argument.ipynb)

## OpenAPI

````yaml post /v1/responses
paths:
  path: /v1/responses
  method: post
  servers:
    - url: https://api.fireworks.ai/inference
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication using your Fireworks API key. Format:
                Bearer <API_KEY>
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
              model:
                allOf:
                  - type: string
                    title: Model
                    description: >-
                      The model to use for generating the response. Example:
                      `accounts/<ACCOUNT_ID>/models/<MODEL_ID>`.
              input:
                allOf:
                  - anyOf:
                      - type: string
                      - items:
                          additionalProperties: true
                          type: object
                        type: array
                    title: Input
                    description: >-
                      The input to the model. Can be a simple text string or a
                      list of message objects for complex inputs with multiple
                      content types.
              previous_response_id:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Previous Response Id
                    description: >-
                      The ID of a previous response to continue the conversation
                      from. When provided, the conversation history from that
                      response will be automatically loaded.
              instructions:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Instructions
                    description: >-
                      System instructions that guide the model's behavior
                      throughout the conversation. Similar to a system message.
              max_output_tokens:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Output Tokens
                    description: >-
                      The maximum number of tokens that can be generated in the
                      response. Must be at least 1. If not specified, the model
                      will generate up to its maximum context length.
              max_tool_calls:
                allOf:
                  - anyOf:
                      - type: integer
                        minimum: 1
                      - type: 'null'
                    title: Max Tool Calls
                    description: >-
                      The maximum number of tool calls allowed in a single
                      response. Useful for controlling costs and limiting tool
                      execution. Must be at least 1.
              metadata:
                allOf:
                  - anyOf:
                      - additionalProperties: true
                        type: object
                      - type: 'null'
                    title: Metadata
                    description: >-
                      Set of up to 16 key-value pairs that can be attached to
                      the response. Useful for storing additional information in
                      a structured format.
              parallel_tool_calls:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Parallel Tool Calls
                    description: >-
                      Whether to enable parallel function calling during tool
                      use. When true, the model can call multiple tools
                      simultaneously. Default is True.
                    default: true
              reasoning:
                allOf:
                  - anyOf:
                      - additionalProperties: true
                        type: object
                      - type: 'null'
                    title: Reasoning
                    description: >-
                      Configuration for reasoning output. When enabled, the
                      model will return its reasoning process along with the
                      response.
              store:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Store
                    description: >-
                      Whether to store the response. When set to false, the
                      response will not be stored and will not be retrievable
                      via the API. This is useful for ephemeral or sensitive
                      data. See an example in our [Controlling Response Storage
                      cookbook](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/mcp_server_with_store_false_argument.ipynb).
                      Default is True.
                    default: true
              stream:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Stream
                    description: >-
                      Whether to stream the response back as Server-Sent Events
                      (SSE). When true, tokens are sent incrementally as they
                      are generated. Default is False.
                    default: false
              temperature:
                allOf:
                  - anyOf:
                      - type: number
                        maximum: 2
                        minimum: 0
                      - type: 'null'
                    title: Temperature
                    description: >-
                      The sampling temperature to use, between 0 and 2. Higher
                      values like 0.8 make output more random, while lower
                      values like 0.2 make it more focused and deterministic.
                      Default is 1.0.
                    default: 1
              text:
                allOf:
                  - anyOf:
                      - additionalProperties: true
                        type: object
                      - type: 'null'
                    title: Text
                    description: >-
                      Text generation configuration parameters. Used for
                      advanced text generation settings.
              tool_choice:
                allOf:
                  - anyOf:
                      - type: string
                      - additionalProperties: true
                        type: object
                      - type: 'null'
                    title: Tool Choice
                    description: >-
                      Controls which (if any) tool the model should use. Can be
                      'none' (never call tools), 'auto' (model decides),
                      'required' (must call at least one tool), or an object
                      specifying a particular tool to call. Default is 'auto'.
                    default: auto
              tools:
                allOf:
                  - anyOf:
                      - items:
                          additionalProperties: true
                          type: object
                        type: array
                      - type: 'null'
                    title: Tools
                    description: >-
                      A list of MCP tools the model may call. See our cookbooks
                      for examples on [basic MCP
                      usage](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_mcp_examples.ipynb)
                      and [streaming with
                      MCP](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_mcp_with_streaming.ipynb).
              top_p:
                allOf:
                  - anyOf:
                      - type: number
                        maximum: 1
                        minimum: 0
                      - type: 'null'
                    title: Top P
                    description: >-
                      An alternative to temperature sampling, called nucleus
                      sampling, where the model considers the results of tokens
                      with top_p probability mass. So 0.1 means only tokens
                      comprising the top 10% probability mass are considered.
                      Default is 1.0. We generally recommend altering this or
                      temperature but not both.
                    default: 1
              truncation:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Truncation
                    description: >-
                      The truncation strategy to use for the context when it
                      exceeds the model's maximum length. Can be 'auto'
                      (automatically truncate) or 'disabled' (return error if
                      context too long). Default is 'disabled'.
                    default: disabled
              user:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: User
                    description: >-
                      A unique identifier representing your end-user, which can
                      help Fireworks to monitor and detect abuse. This can be a
                      username, email, or any other unique identifier.
            required: true
            title: CreateResponse
            description: >-
              Request model for creating a new response.


              This model defines all the parameters needed to create a new model
              response,

              including model configuration, input data, tool definitions, and
              conversation continuation.
            refIdentifier: '#/components/schemas/CreateResponse'
            requiredProperties:
              - model
              - input
        examples:
          example:
            value:
              model: <string>
              input: <string>
              previous_response_id: <string>
              instructions: <string>
              max_output_tokens: 123
              max_tool_calls: 2
              metadata: {}
              parallel_tool_calls: true
              reasoning: {}
              store: true
              stream: true
              temperature: 1
              text: {}
              tool_choice: <string>
              tools:
                - {}
              top_p: 0.5
              truncation: <string>
              user: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Id
                    description: >-
                      The unique identifier of the response. Will be None if
                      store=False.
              object:
                allOf:
                  - type: string
                    title: Object
                    description: The object type, which is always 'response'.
                    default: response
              created_at:
                allOf:
                  - type: integer
                    title: Created At
                    description: >-
                      The Unix timestamp (in seconds) when the response was
                      created.
              status:
                allOf:
                  - type: string
                    title: Status
                    description: >-
                      The status of the response. Can be 'completed',
                      'in_progress', 'incomplete', 'failed', or 'cancelled'.
              model:
                allOf:
                  - type: string
                    title: Model
                    description: >-
                      The model used to generate the response (e.g.,
                      `accounts/<ACCOUNT_ID>/models/<MODEL_ID>`).
              output:
                allOf:
                  - items:
                      anyOf:
                        - $ref: '#/components/schemas/Message'
                        - $ref: '#/components/schemas/ToolCall'
                        - $ref: '#/components/schemas/ToolOutput'
                    type: array
                    title: Output
                    description: >-
                      An array of output items produced by the model. Can
                      contain messages, tool calls, and tool outputs.
              previous_response_id:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Previous Response Id
                    description: >-
                      The ID of the previous response in the conversation, if
                      this response continues a conversation.
              usage:
                allOf:
                  - anyOf:
                      - additionalProperties: true
                        type: object
                      - type: 'null'
                    title: Usage
                    description: >-
                      Token usage information for the request. Contains
                      'prompt_tokens', 'completion_tokens', and 'total_tokens'.
              error:
                allOf:
                  - anyOf:
                      - additionalProperties: true
                        type: object
                      - type: 'null'
                    title: Error
                    description: >-
                      Error information if the response failed. Contains 'type',
                      'code', and 'message' fields.
              incomplete_details:
                allOf:
                  - anyOf:
                      - additionalProperties: true
                        type: object
                      - type: 'null'
                    title: Incomplete Details
                    description: >-
                      Details about why the response is incomplete, if status is
                      'incomplete'. Contains 'reason' field which can be
                      'max_output_tokens', 'max_tool_calls', or
                      'content_filter'.
              instructions:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Instructions
                    description: >-
                      System instructions that guide the model's behavior.
                      Similar to a system message.
              max_output_tokens:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Output Tokens
                    description: >-
                      The maximum number of tokens that can be generated in the
                      response. Must be at least 1.
              max_tool_calls:
                allOf:
                  - anyOf:
                      - type: integer
                        minimum: 1
                      - type: 'null'
                    title: Max Tool Calls
                    description: >-
                      The maximum number of tool calls allowed in a single
                      response. Must be at least 1.
              parallel_tool_calls:
                allOf:
                  - type: boolean
                    title: Parallel Tool Calls
                    description: >-
                      Whether to enable parallel function calling during tool
                      use. Default is True.
                    default: true
              reasoning:
                allOf:
                  - anyOf:
                      - additionalProperties: true
                        type: object
                      - type: 'null'
                    title: Reasoning
                    description: >-
                      Reasoning output from the model, if reasoning is enabled.
                      Contains 'content' and 'type' fields.
              store:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Store
                    description: >-
                      Whether to store this response for future retrieval. If
                      False, the response will not be persisted and
                      previous_response_id cannot reference it. Default is True.
                    default: true
              temperature:
                allOf:
                  - type: number
                    maximum: 2
                    minimum: 0
                    title: Temperature
                    description: >-
                      The sampling temperature to use, between 0 and 2. Higher
                      values like 0.8 make output more random, while lower
                      values like 0.2 make it more focused and deterministic.
                      Default is 1.0.
                    default: 1
              text:
                allOf:
                  - anyOf:
                      - additionalProperties: true
                        type: object
                      - type: 'null'
                    title: Text
                    description: Text generation configuration parameters, if applicable.
              tool_choice:
                allOf:
                  - anyOf:
                      - type: string
                      - additionalProperties: true
                        type: object
                    title: Tool Choice
                    description: >-
                      Controls which (if any) tool the model should use. Can be
                      'none', 'auto', 'required', or an object specifying a
                      particular tool. Default is 'auto'.
                    default: auto
              tools:
                allOf:
                  - items:
                      additionalProperties: true
                      type: object
                    type: array
                    title: Tools
                    description: >-
                      A list of tools the model may call. Each tool is defined
                      with a type and function specification following the
                      OpenAI tool format. Supports 'function', 'mcp', 'sse', and
                      'python' tool types.
              top_p:
                allOf:
                  - type: number
                    maximum: 1
                    minimum: 0
                    title: Top P
                    description: >-
                      An alternative to temperature sampling, called nucleus
                      sampling, where the model considers the results of tokens
                      with top_p probability mass. So 0.1 means only tokens
                      comprising the top 10% probability mass are considered.
                      Default is 1.0.
                    default: 1
              truncation:
                allOf:
                  - type: string
                    title: Truncation
                    description: >-
                      The truncation strategy to use for the context. Can be
                      'auto' or 'disabled'. Default is 'disabled'.
                    default: disabled
              user:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: User
                    description: >-
                      A unique identifier representing your end-user, which can
                      help Fireworks to monitor and detect abuse.
              metadata:
                allOf:
                  - anyOf:
                      - additionalProperties: true
                        type: object
                      - type: 'null'
                    title: Metadata
                    description: >-
                      Set of up to 16 key-value pairs that can be attached to
                      the response. Useful for storing additional information
                      about the response in a structured format.
            title: Response
            description: >-
              Represents a response object returned from the API.


              A response includes the model output, token usage, configuration
              parameters,

              and metadata about the conversation state.
            refIdentifier: '#/components/schemas/Response'
            requiredProperties:
              - created_at
              - status
              - model
              - output
        examples:
          example:
            value:
              id: <string>
              object: response
              created_at: 123
              status: <string>
              model: <string>
              output:
                - id: <string>
                  type: message
                  role: <string>
                  content:
                    - type: <string>
                      text: <string>
                  status: <string>
              previous_response_id: <string>
              usage: {}
              error: {}
              incomplete_details: {}
              instructions: <string>
              max_output_tokens: 123
              max_tool_calls: 2
              parallel_tool_calls: true
              reasoning: {}
              store: true
              temperature: 1
              text: {}
              tool_choice: <string>
              tools:
                - {}
              top_p: 1
              truncation: disabled
              user: <string>
              metadata: {}
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    type: array
                    title: Detail
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
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
    ToolCall:
      properties:
        id:
          type: string
          title: Id
          description: The unique identifier of the tool call.
        type:
          type: string
          title: Type
          description: The type of tool call. Can be 'function', 'tool_call', or 'mcp'.
        function:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Function
          description: >-
            The function definition for function tool calls. Contains 'name' and
            'arguments' keys.
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

````