# Source: https://docs.fireworks.ai/api-reference/list-responses.md

# List Responses

> Get a list of all responses for the authenticated account.

Args:
    limit: Maximum number of responses to return (default: 20, max: 100)
    after: Cursor for pagination - return responses after this ID
    before: Cursor for pagination - return responses before this ID

## OpenAPI

````yaml get /v1/responses
paths:
  path: /v1/responses
  method: get
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
      query:
        limit:
          schema:
            - type: integer
              required: false
              title: Limit
              default: 20
        after:
          schema:
            - type: string
              required: false
              title: After
            - type: 'null'
              required: false
              title: After
        before:
          schema:
            - type: string
              required: false
              title: Before
            - type: 'null'
              required: false
              title: Before
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              object:
                allOf:
                  - type: string
                    title: Object
                    description: The object type, which is always 'list'.
                    default: list
              data:
                allOf:
                  - items:
                      $ref: '#/components/schemas/Response'
                    type: array
                    title: Data
                    description: >-
                      An array of response objects, sorted by creation time in
                      descending order (most recent first).
              has_more:
                allOf:
                  - type: boolean
                    title: Has More
                    description: >-
                      Indicates whether there are more responses available
                      beyond this page. If true, use the 'last_id' value as the
                      'after' cursor to fetch the next page.
              first_id:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: First Id
                    description: >-
                      The ID of the first response in the current page. Used for
                      pagination.
              last_id:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Last Id
                    description: >-
                      The ID of the last response in the current page. Use this
                      as the 'after' cursor to fetch the next page if has_more
                      is true.
            title: ResponseList
            description: >-
              Response model for listing responses.


              Returned from the GET /v1/responses endpoint. Provides a paginated
              list

              of response objects with cursor-based pagination support.
            refIdentifier: '#/components/schemas/ResponseList'
            requiredProperties:
              - data
              - has_more
        examples:
          example:
            value:
              object: list
              data:
                - id: <string>
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
              has_more: true
              first_id: <string>
              last_id: <string>
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