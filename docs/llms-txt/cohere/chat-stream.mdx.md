# Source: https://docs.cohere.com/reference/chat-stream.mdx

# Chat with Streaming

POST https://api.cohere.com/v2/chat
Content-Type: application/json

Generates a text response to a user message. To learn how to use the Chat API and RAG follow our [Text Generation guides](https://docs.cohere.com/v2/docs/chat-api).

Follow the [Migration Guide](https://docs.cohere.com/v2/docs/migrating-v1-to-v2) for instructions on moving from API v1 to API v2.


Reference: https://docs.cohere.com/reference/chat-stream

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v2/chat:
    post:
      operationId: chat-stream
      summary: Chat API (v2)
      description: >
        Generates a text response to a user message. To learn how to use the
        Chat API and RAG follow our [Text Generation
        guides](https://docs.cohere.com/v2/docs/chat-api).


        Follow the [Migration
        Guide](https://docs.cohere.com/v2/docs/migrating-v1-to-v2) for
        instructions on moving from API v1 to API v2.
      tags:
        - subpackage_v2
      parameters:
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: >
            Generates a text response to a user message. To learn how to use the
            Chat API and RAG follow our [Text Generation
            guides](https://docs.cohere.com/v2/docs/chat-api).


            Follow the [Migration
            Guide](https://docs.cohere.com/v2/docs/migrating-v1-to-v2) for
            instructions on moving from API v1 to API v2.
          content:
            text/event-stream:
              schema:
                $ref: '#/components/schemas/v2_chat_Response_stream_streaming'
        '400':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Chatv2RequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Chatv2RequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Chatv2RequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Chatv2RequestNotFoundError'
        '422':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Chatv2RequestUnprocessableEntityError'
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Chatv2RequestTooManyRequestsError'
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Chatv2RequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Chatv2RequestClientClosedRequestError'
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Chatv2RequestInternalServerError'
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Chatv2RequestNotImplementedError'
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Chatv2RequestServiceUnavailableError'
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Chatv2RequestGatewayTimeoutError'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                stream:
                  type: boolean
                  enum:
                    - true
                  description: >
                    Defaults to `false`.


                    When `true`, the response will be a SSE stream of events.


                    Streaming is beneficial for user interfaces that render the
                    contents of the response piece by piece, as it gets
                    generated.
                model:
                  type: string
                  description: >-
                    The name of a compatible [Cohere
                    model](https://docs.cohere.com/v2/docs/models).
                messages:
                  $ref: '#/components/schemas/ChatMessages'
                tools:
                  type: array
                  items:
                    $ref: '#/components/schemas/ToolV2'
                  description: >
                    A list of tools (functions) available to the model. The
                    model response may contain 'tool_calls' to the specified
                    tools.


                    Learn more in the [Tool Use
                    guide](https://docs.cohere.com/docs/tools).
                strict_tools:
                  type: boolean
                  description: >
                    When set to `true`, tool calls in the Assistant message will
                    be forced to follow the tool definition strictly. Learn more
                    in the [Structured Outputs (Tools)
                    guide](https://docs.cohere.com/docs/structured-outputs-json#structured-outputs-tools).


                    **Note**: The first few requests with a new set of tools
                    will take longer to process.
                documents:
                  type: array
                  items:
                    $ref: >-
                      #/components/schemas/V2ChatPostRequestBodyContentApplicationJsonSchemaDocumentsItems
                  description: >
                    A list of relevant documents that the model can cite to
                    generate a more accurate reply. Each document is either a
                    string or document object with content and metadata.
                citation_options:
                  $ref: '#/components/schemas/CitationOptions'
                response_format:
                  $ref: '#/components/schemas/ResponseFormatV2'
                safety_mode:
                  $ref: >-
                    #/components/schemas/V2ChatPostRequestBodyContentApplicationJsonSchemaSafetyMode
                  description: >
                    Used to select the [safety
                    instruction](https://docs.cohere.com/v2/docs/safety-modes)
                    inserted into the prompt. Defaults to `CONTEXTUAL`.

                    When `OFF` is specified, the safety instruction will be
                    omitted.


                    Safety modes are not yet configurable in combination with
                    `tools` and `documents` parameters.


                    **Note**: This parameter is only compatible newer Cohere
                    models, starting with [Command R
                    08-2024](https://docs.cohere.com/docs/command-r#august-2024-release)
                    and [Command R+
                    08-2024](https://docs.cohere.com/docs/command-r-plus#august-2024-release).


                    **Note**: `command-r7b-12-2024` and newer models only
                    support `"CONTEXTUAL"` and `"STRICT"` modes.
                max_tokens:
                  type: integer
                  description: >
                    The maximum number of output tokens the model will generate
                    in the response. If not set, `max_tokens` defaults to the
                    model's maximum output token limit. You can find the maximum
                    output token limits for each model in the [model
                    documentation](https://docs.cohere.com/docs/models).


                    **Note**: Setting a low value may result in incomplete
                    generations. In such cases, the `finish_reason` field in the
                    response will be set to `"MAX_TOKENS"`.


                    **Note**: If `max_tokens` is set higher than the model's
                    maximum output token limit, the generation will be capped at
                    that model-specific maximum limit.
                stop_sequences:
                  type: array
                  items:
                    type: string
                  description: >
                    A list of up to 5 strings that the model will use to stop
                    generation. If the model generates a string that matches any
                    of the strings in the list, it will stop generating tokens
                    and return the generated text up to that point not including
                    the stop sequence.
                temperature:
                  type: number
                  format: double
                  description: >
                    Defaults to `0.3`.


                    A non-negative float that tunes the degree of randomness in
                    generation. Lower temperatures mean less random generations,
                    and higher temperatures mean more random generations.


                    Randomness can be further maximized by increasing the  value
                    of the `p` parameter.
                seed:
                  type: integer
                  description: >
                    If specified, the backend will make a best effort to sample
                    tokens

                    deterministically, such that repeated requests with the same

                    seed and parameters should return the same result. However,

                    determinism cannot be totally guaranteed.
                frequency_penalty:
                  type: number
                  format: double
                  description: >
                    Defaults to `0.0`, min value of `0.0`, max value of `1.0`.

                    Used to reduce repetitiveness of generated tokens. The
                    higher the value, the stronger a penalty is applied to
                    previously present tokens, proportional to how many times
                    they have already appeared in the prompt or prior
                    generation.
                presence_penalty:
                  type: number
                  format: double
                  description: >
                    Defaults to `0.0`, min value of `0.0`, max value of `1.0`.

                    Used to reduce repetitiveness of generated tokens. Similar
                    to `frequency_penalty`, except that this penalty is applied
                    equally to all tokens that have already appeared, regardless
                    of their exact frequencies.
                k:
                  type: integer
                  default: 0
                  description: >
                    Ensures that only the top `k` most likely tokens are
                    considered for generation at each step. When `k` is set to
                    `0`, k-sampling is disabled.

                    Defaults to `0`, min value of `0`, max value of `500`.
                p:
                  type: number
                  format: double
                  description: >
                    Ensures that only the most likely tokens, with total
                    probability mass of `p`, are considered for generation at
                    each step. If both `k` and `p` are enabled, `p` acts after
                    `k`.

                    Defaults to `0.75`. min value of `0.01`, max value of
                    `0.99`.
                logprobs:
                  type: boolean
                  description: >
                    Defaults to `false`. When set to `true`, the log
                    probabilities of the generated tokens will be included in
                    the response.
                tool_choice:
                  $ref: >-
                    #/components/schemas/V2ChatPostRequestBodyContentApplicationJsonSchemaToolChoice
                  description: >
                    Used to control whether or not the model will be forced to
                    use a tool when answering. When `REQUIRED` is specified, the
                    model will be forced to use at least one of the user-defined
                    tools, and the `tools` parameter must be passed in the
                    request.

                    When `NONE` is specified, the model will be forced **not**
                    to use one of the specified tools, and give a direct
                    response.

                    If tool_choice isn't specified, then the model is free to
                    choose whether to use the specified tools or not.


                    **Note**: This parameter is only compatible with models
                    [Command-r7b](https://docs.cohere.com/v2/docs/command-r7b)
                    and newer.
                thinking:
                  $ref: '#/components/schemas/Thinking'
                priority:
                  type: integer
                  default: 0
                  description: >-
                    Controls how early the request is handled. Lower numbers
                    indicate higher priority (default: 0, the highest). When the
                    system is under load, higher-priority requests are processed
                    first and are the least likely to be dropped.
              required:
                - stream
                - model
                - messages
servers:
  - url: https://api.cohere.com
components:
  schemas:
    ImageUrlDetail:
      type: string
      enum:
        - auto
        - low
        - high
      description: >
        Controls the level of detail in image processing. `"auto"` is the
        default and lets the system choose, `"low"` is faster but less detailed,
        and `"high"` preserves maximum detail. You can save tokens and speed up
        responses by using detail: `"low"`.
      title: ImageUrlDetail
    ImageUrl:
      type: object
      properties:
        url:
          type: string
          description: |
            URL of an image. Can be either a base64 data URI or a web URL.
        detail:
          $ref: '#/components/schemas/ImageUrlDetail'
          description: >
            Controls the level of detail in image processing. `"auto"` is the
            default and lets the system choose, `"low"` is faster but less
            detailed, and `"high"` preserves maximum detail. You can save tokens
            and speed up responses by using detail: `"low"`.
      required:
        - url
      title: ImageUrl
    Content:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - text
              description: 'Discriminator value: text'
            text:
              type: string
          required:
            - type
            - text
          description: text variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - image_url
              description: 'Discriminator value: image_url'
            image_url:
              $ref: '#/components/schemas/ImageUrl'
          required:
            - type
            - image_url
          description: image_url variant
      discriminator:
        propertyName: type
      description: >-
        A Content block which contains information about the content type and
        the content itself.
      title: Content
    ChatMessageV2DiscriminatorMappingUserContent1:
      type: array
      items:
        $ref: '#/components/schemas/Content'
      title: ChatMessageV2DiscriminatorMappingUserContent1
    ChatMessageV2DiscriminatorMappingUserContent:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ChatMessageV2DiscriminatorMappingUserContent1'
      description: >
        The content of the message. This can be a string or a list of content
        blocks.

        If a string is provided, it will be treated as a text content block.
      title: ChatMessageV2DiscriminatorMappingUserContent
    ToolCallV2Type:
      type: string
      enum:
        - function
      title: ToolCallV2Type
    ToolCallV2Function:
      type: object
      properties:
        name:
          type: string
        arguments:
          type: string
      title: ToolCallV2Function
    ToolCallV2:
      type: object
      properties:
        id:
          type: string
        type:
          $ref: '#/components/schemas/ToolCallV2Type'
        function:
          $ref: '#/components/schemas/ToolCallV2Function'
      required:
        - id
        - type
      description: An array of tool calls to be made.
      title: ToolCallV2
    ChatMessageV2DiscriminatorMappingAssistantContentOneOf1Items:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - text
              description: 'Discriminator value: text'
            text:
              type: string
          required:
            - type
            - text
          description: text variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - thinking
              description: 'Discriminator value: thinking'
            thinking:
              type: string
          required:
            - type
            - thinking
          description: thinking variant
      discriminator:
        propertyName: type
      title: ChatMessageV2DiscriminatorMappingAssistantContentOneOf1Items
    ChatMessageV2DiscriminatorMappingAssistantContent1:
      type: array
      items:
        $ref: >-
          #/components/schemas/ChatMessageV2DiscriminatorMappingAssistantContentOneOf1Items
      title: ChatMessageV2DiscriminatorMappingAssistantContent1
    ChatMessageV2DiscriminatorMappingAssistantContent:
      oneOf:
        - type: string
        - $ref: >-
            #/components/schemas/ChatMessageV2DiscriminatorMappingAssistantContent1
      title: ChatMessageV2DiscriminatorMappingAssistantContent
    Source:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - tool
              description: 'Discriminator value: tool'
            id:
              type: string
              description: The unique identifier of the document
            tool_output:
              type: object
              additionalProperties:
                description: Any type
          required:
            - type
          description: tool variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - document
              description: 'Discriminator value: document'
            id:
              type: string
              description: The unique identifier of the document
            document:
              type: object
              additionalProperties:
                description: Any type
          required:
            - type
          description: document variant
      discriminator:
        propertyName: type
      description: >-
        A source object containing information about the source of the data
        cited.
      title: Source
    CitationType:
      type: string
      enum:
        - TEXT_CONTENT
        - THINKING_CONTENT
        - PLAN
      description: >
        The type of citation which indicates what part of the response the
        citation is for.
      title: CitationType
    Citation:
      type: object
      properties:
        start:
          type: integer
          description: Start index of the cited snippet in the original source text.
        end:
          type: integer
          description: End index of the cited snippet in the original source text.
        text:
          type: string
          description: Text snippet that is being cited.
        sources:
          type: array
          items:
            $ref: '#/components/schemas/Source'
        content_index:
          type: integer
          description: Index of the content block in which this citation appears.
        type:
          $ref: '#/components/schemas/CitationType'
      description: Citation information containing sources and the text cited.
      title: Citation
    ChatMessageV2DiscriminatorMappingSystemContentOneOf1Items:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - text
              description: 'Discriminator value: text'
            text:
              type: string
          required:
            - type
            - text
          description: text variant
      discriminator:
        propertyName: type
      title: ChatMessageV2DiscriminatorMappingSystemContentOneOf1Items
    ChatMessageV2DiscriminatorMappingSystemContent1:
      type: array
      items:
        $ref: >-
          #/components/schemas/ChatMessageV2DiscriminatorMappingSystemContentOneOf1Items
      title: ChatMessageV2DiscriminatorMappingSystemContent1
    ChatMessageV2DiscriminatorMappingSystemContent:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ChatMessageV2DiscriminatorMappingSystemContent1'
      title: ChatMessageV2DiscriminatorMappingSystemContent
    Document-qmvpd9:
      type: object
      properties: {}
      description: >
        A relevant document that the model can cite to generate a more accurate
        reply. Each document is a string-any dictionary.
      title: Document-qmvpd9
    Document:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/Document-qmvpd9'
          description: >
            A relevant document that the model can cite to generate a more
            accurate reply. Each document is a string-any dictionary.
        id:
          type: string
          description: >-
            Unique identifier for this document which will be referenced in
            citations. If not provided an ID will be automatically generated.
      required:
        - data
      description: >
        Relevant information that could be used by the model to generate a more
        accurate reply.

        The content of each document are generally short (should be under 300
        words). Metadata should be used to provide additional information, both
        the key name and the value will be

        passed to the model.
      title: Document
    ToolContent:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - text
              description: 'Discriminator value: text'
            text:
              type: string
          required:
            - type
            - text
          description: text variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - document
              description: 'Discriminator value: document'
            document:
              $ref: '#/components/schemas/Document'
          required:
            - type
            - document
          description: document variant
      discriminator:
        propertyName: type
      description: >-
        A content block which contains information about the content of a tool
        result
      title: ToolContent
    ChatMessageV2DiscriminatorMappingToolContent1:
      type: array
      items:
        $ref: '#/components/schemas/ToolContent'
      title: ChatMessageV2DiscriminatorMappingToolContent1
    ChatMessageV2DiscriminatorMappingToolContent:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/ChatMessageV2DiscriminatorMappingToolContent1'
      description: >-
        Outputs from a tool. The content should formatted as a JSON object
        string, or a list of tool content blocks
      title: ChatMessageV2DiscriminatorMappingToolContent
    ChatMessageV2:
      oneOf:
        - type: object
          properties:
            role:
              type: string
              enum:
                - user
              description: 'Discriminator value: user'
            content:
              $ref: >-
                #/components/schemas/ChatMessageV2DiscriminatorMappingUserContent
              description: >
                The content of the message. This can be a string or a list of
                content blocks.

                If a string is provided, it will be treated as a text content
                block.
          required:
            - role
            - content
          description: user variant
        - type: object
          properties:
            role:
              type: string
              enum:
                - assistant
              description: 'Discriminator value: assistant'
            tool_calls:
              type: array
              items:
                $ref: '#/components/schemas/ToolCallV2'
            tool_plan:
              type: string
              description: >-
                A chain-of-thought style reflection and plan that the model
                generates when working with Tools.
            content:
              $ref: >-
                #/components/schemas/ChatMessageV2DiscriminatorMappingAssistantContent
            citations:
              type: array
              items:
                $ref: '#/components/schemas/Citation'
          required:
            - role
          description: assistant variant
        - type: object
          properties:
            role:
              type: string
              enum:
                - system
              description: 'Discriminator value: system'
            content:
              $ref: >-
                #/components/schemas/ChatMessageV2DiscriminatorMappingSystemContent
          required:
            - role
            - content
          description: system variant
        - type: object
          properties:
            role:
              type: string
              enum:
                - tool
              description: 'Discriminator value: tool'
            tool_call_id:
              type: string
              description: >-
                The id of the associated tool call that has provided the given
                content
            content:
              $ref: >-
                #/components/schemas/ChatMessageV2DiscriminatorMappingToolContent
              description: >-
                Outputs from a tool. The content should formatted as a JSON
                object string, or a list of tool content blocks
          required:
            - role
            - tool_call_id
            - content
          description: tool variant
      discriminator:
        propertyName: role
      description: Represents a single message in the chat history from a given role.
      title: ChatMessageV2
    ChatMessages:
      type: array
      items:
        $ref: '#/components/schemas/ChatMessageV2'
      description: >
        A list of chat messages in chronological order, representing a
        conversation between the user and the model.


        Messages can be from `User`, `Assistant`, `Tool` and `System` roles.
        Learn more about messages and roles in [the Chat API
        guide](https://docs.cohere.com/v2/docs/chat-api).
      title: ChatMessages
    ToolV2Type:
      type: string
      enum:
        - function
      title: ToolV2Type
    ToolV2-6eoehf:
      type: object
      properties: {}
      description: The parameters of the function as a JSON schema.
      title: ToolV2-6eoehf
    ToolV2Function:
      type: object
      properties:
        name:
          type: string
          description: The name of the function.
        description:
          type: string
          description: The description of the function.
        parameters:
          $ref: '#/components/schemas/ToolV2-6eoehf'
          description: The parameters of the function as a JSON schema.
      required:
        - name
        - parameters
      description: The function to be executed.
      title: ToolV2Function
    ToolV2:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ToolV2Type'
        function:
          $ref: '#/components/schemas/ToolV2Function'
          description: The function to be executed.
      required:
        - type
      title: ToolV2
    V2ChatPostRequestBodyContentApplicationJsonSchemaDocumentsItems:
      oneOf:
        - type: string
        - $ref: '#/components/schemas/Document'
      title: V2ChatPostRequestBodyContentApplicationJsonSchemaDocumentsItems
    CitationOptionsMode:
      type: string
      enum:
        - ENABLED
        - DISABLED
        - FAST
        - ACCURATE
        - 'OFF'
      description: >
        Defaults to `"enabled"`.

        Citations are enabled by default for models that support it, but can be
        turned off by setting `"type": "disabled"`.
      title: CitationOptionsMode
    CitationOptions:
      type: object
      properties:
        mode:
          $ref: '#/components/schemas/CitationOptionsMode'
          description: >
            Defaults to `"enabled"`.

            Citations are enabled by default for models that support it, but can
            be turned off by setting `"type": "disabled"`.
      description: Options for controlling citation generation.
      title: CitationOptions
    JsonResponseFormatV2-uu9wid:
      type: object
      properties: {}
      description: >
        A [JSON schema](https://json-schema.org/overview/what-is-jsonschema)
        object that the output will adhere to. There are some restrictions we
        have on the schema, refer to [our
        guide](https://docs.cohere.com/docs/structured-outputs-json#schema-constraints)
        for more information.

        Example (required name and age object):

        ```json

        {
          "type": "object",
          "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"}
          },
          "required": ["name", "age"]
        }

        ```


        **Note**: This field must not be specified when the `type` is set to
        `"text"`.
      title: JsonResponseFormatV2-uu9wid
    ResponseFormatV2:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - text
              description: 'Discriminator value: text'
          required:
            - type
          description: text variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - json_object
              description: 'Discriminator value: json_object'
            json_schema:
              $ref: '#/components/schemas/JsonResponseFormatV2-uu9wid'
              description: >
                A [JSON
                schema](https://json-schema.org/overview/what-is-jsonschema)
                object that the output will adhere to. There are some
                restrictions we have on the schema, refer to [our
                guide](https://docs.cohere.com/docs/structured-outputs-json#schema-constraints)
                for more information.

                Example (required name and age object):

                ```json

                {
                  "type": "object",
                  "properties": {
                    "name": {"type": "string"},
                    "age": {"type": "integer"}
                  },
                  "required": ["name", "age"]
                }

                ```


                **Note**: This field must not be specified when the `type` is
                set to `"text"`.
          required:
            - type
          description: json_object variant
      discriminator:
        propertyName: type
      description: >
        Configuration for forcing the model output to adhere to the specified
        format. Supported on [Command
        R](https://docs.cohere.com/v2/docs/command-r), [Command
        R+](https://docs.cohere.com/v2/docs/command-r-plus) and newer models.


        The model can be forced into outputting JSON objects by setting `{
        "type": "json_object" }`.


        A [JSON Schema](https://json-schema.org/) can optionally be provided, to
        ensure a specific structure.


        **Note**: When using  `{ "type": "json_object" }` your `message` should
        always explicitly instruct the model to generate a JSON (eg: _"Generate
        a JSON ..."_) . Otherwise the model may end up getting stuck generating
        an infinite stream of characters and eventually run out of context
        length.


        **Note**: When `json_schema` is not specified, the generated object can
        have up to 5 layers of nesting.


        **Limitation**: The parameter is not supported when used in combinations
        with the `documents` or `tools` parameters.
      title: ResponseFormatV2
    V2ChatPostRequestBodyContentApplicationJsonSchemaSafetyMode:
      type: string
      enum:
        - CONTEXTUAL
        - STRICT
        - 'OFF'
      description: >
        Used to select the [safety
        instruction](https://docs.cohere.com/v2/docs/safety-modes) inserted into
        the prompt. Defaults to `CONTEXTUAL`.

        When `OFF` is specified, the safety instruction will be omitted.


        Safety modes are not yet configurable in combination with `tools` and
        `documents` parameters.


        **Note**: This parameter is only compatible newer Cohere models,
        starting with [Command R
        08-2024](https://docs.cohere.com/docs/command-r#august-2024-release) and
        [Command R+
        08-2024](https://docs.cohere.com/docs/command-r-plus#august-2024-release).


        **Note**: `command-r7b-12-2024` and newer models only support
        `"CONTEXTUAL"` and `"STRICT"` modes.
      title: V2ChatPostRequestBodyContentApplicationJsonSchemaSafetyMode
    V2ChatPostRequestBodyContentApplicationJsonSchemaToolChoice:
      type: string
      enum:
        - REQUIRED
        - NONE
      description: >
        Used to control whether or not the model will be forced to use a tool
        when answering. When `REQUIRED` is specified, the model will be forced
        to use at least one of the user-defined tools, and the `tools` parameter
        must be passed in the request.

        When `NONE` is specified, the model will be forced **not** to use one of
        the specified tools, and give a direct response.

        If tool_choice isn't specified, then the model is free to choose whether
        to use the specified tools or not.


        **Note**: This parameter is only compatible with models
        [Command-r7b](https://docs.cohere.com/v2/docs/command-r7b) and newer.
      title: V2ChatPostRequestBodyContentApplicationJsonSchemaToolChoice
    ThinkingType:
      type: string
      enum:
        - enabled
        - disabled
      description: >
        Reasoning is enabled by default for models that support it, but can be
        turned off by setting `"type": "disabled"`.
      title: ThinkingType
    Thinking:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ThinkingType'
          description: >
            Reasoning is enabled by default for models that support it, but can
            be turned off by setting `"type": "disabled"`.
        token_budget:
          type: integer
          description: >
            The maximum number of tokens the model can use for thinking, which
            must be set to a positive integer.

            The model will stop thinking if it reaches the thinking token budget
            and will proceed with the response.
      required:
        - type
      description: >
        Configuration for [reasoning
        features](https://docs.cohere.com/docs/reasoning).
      title: Thinking
    ChatStreamEventTypeType:
      type: string
      enum:
        - message-start
        - content-start
        - content-delta
        - content-end
        - tool-call-start
        - tool-call-delta
        - tool-call-end
        - tool-plan-delta
        - citation-start
        - citation-end
        - message-end
      title: ChatStreamEventTypeType
    ChatMessageStartEventDeltaMessageRole:
      type: string
      enum:
        - assistant
      description: The role of the message.
      title: ChatMessageStartEventDeltaMessageRole
    ChatMessageStartEventDeltaMessage:
      type: object
      properties:
        role:
          $ref: '#/components/schemas/ChatMessageStartEventDeltaMessageRole'
          description: The role of the message.
      title: ChatMessageStartEventDeltaMessage
    ChatMessageStartEventDelta:
      type: object
      properties:
        message:
          $ref: '#/components/schemas/ChatMessageStartEventDeltaMessage'
      title: ChatMessageStartEventDelta
    ChatContentStartEventDeltaMessageContentType:
      type: string
      enum:
        - text
        - thinking
      title: ChatContentStartEventDeltaMessageContentType
    ChatContentStartEventDeltaMessageContent:
      type: object
      properties:
        thinking:
          type: string
        text:
          type: string
        type:
          $ref: '#/components/schemas/ChatContentStartEventDeltaMessageContentType'
      title: ChatContentStartEventDeltaMessageContent
    ChatContentStartEventDeltaMessage:
      type: object
      properties:
        content:
          $ref: '#/components/schemas/ChatContentStartEventDeltaMessageContent'
      title: ChatContentStartEventDeltaMessage
    ChatContentStartEventDelta:
      type: object
      properties:
        message:
          $ref: '#/components/schemas/ChatContentStartEventDeltaMessage'
      title: ChatContentStartEventDelta
    ChatContentDeltaEventDeltaMessageContent:
      type: object
      properties:
        thinking:
          type: string
        text:
          type: string
      title: ChatContentDeltaEventDeltaMessageContent
    ChatContentDeltaEventDeltaMessage:
      type: object
      properties:
        content:
          $ref: '#/components/schemas/ChatContentDeltaEventDeltaMessageContent'
      title: ChatContentDeltaEventDeltaMessage
    ChatContentDeltaEventDelta:
      type: object
      properties:
        message:
          $ref: '#/components/schemas/ChatContentDeltaEventDeltaMessage'
      title: ChatContentDeltaEventDelta
    LogprobItem:
      type: object
      properties:
        text:
          type: string
          description: The text chunk for which the log probabilities was calculated.
        token_ids:
          type: array
          items:
            type: integer
          description: The token ids of each token used to construct the text chunk.
        logprobs:
          type: array
          items:
            type: number
            format: double
          description: The log probability of each token used to construct the text chunk.
      required:
        - token_ids
      title: LogprobItem
    ChatToolPlanDeltaEventDeltaMessage:
      type: object
      properties:
        tool_plan:
          type: string
      title: ChatToolPlanDeltaEventDeltaMessage
    ChatToolPlanDeltaEventDelta:
      type: object
      properties:
        message:
          $ref: '#/components/schemas/ChatToolPlanDeltaEventDeltaMessage'
      title: ChatToolPlanDeltaEventDelta
    ChatToolCallStartEventDeltaMessage:
      type: object
      properties:
        tool_calls:
          $ref: '#/components/schemas/ToolCallV2'
      title: ChatToolCallStartEventDeltaMessage
    ChatToolCallStartEventDelta:
      type: object
      properties:
        message:
          $ref: '#/components/schemas/ChatToolCallStartEventDeltaMessage'
      title: ChatToolCallStartEventDelta
    ChatToolCallDeltaEventDeltaMessageToolCallsFunction:
      type: object
      properties:
        arguments:
          type: string
      title: ChatToolCallDeltaEventDeltaMessageToolCallsFunction
    ChatToolCallDeltaEventDeltaMessageToolCalls:
      type: object
      properties:
        function:
          $ref: >-
            #/components/schemas/ChatToolCallDeltaEventDeltaMessageToolCallsFunction
      title: ChatToolCallDeltaEventDeltaMessageToolCalls
    ChatToolCallDeltaEventDeltaMessage:
      type: object
      properties:
        tool_calls:
          $ref: '#/components/schemas/ChatToolCallDeltaEventDeltaMessageToolCalls'
      title: ChatToolCallDeltaEventDeltaMessage
    ChatToolCallDeltaEventDelta:
      type: object
      properties:
        message:
          $ref: '#/components/schemas/ChatToolCallDeltaEventDeltaMessage'
      title: ChatToolCallDeltaEventDelta
    CitationStartEventDeltaMessage:
      type: object
      properties:
        citations:
          $ref: '#/components/schemas/Citation'
      title: CitationStartEventDeltaMessage
    CitationStartEventDelta:
      type: object
      properties:
        message:
          $ref: '#/components/schemas/CitationStartEventDeltaMessage'
      title: CitationStartEventDelta
    ChatFinishReason:
      type: string
      enum:
        - COMPLETE
        - STOP_SEQUENCE
        - MAX_TOKENS
        - TOOL_CALL
        - ERROR
        - TIMEOUT
      description: >
        The reason a chat request has finished.


        - **complete**: The model finished sending a complete message.

        - **max_tokens**: The number of generated tokens exceeded the model's
        context length or the value specified via the `max_tokens` parameter.

        - **stop_sequence**: One of the provided `stop_sequence` entries was
        reached in the model's generation.

        - **tool_call**: The model generated a Tool Call and is expecting a Tool
        Message in return

        - **error**: The generation failed due to an internal error

        - **timeout**: The generation was stopped because it exceeded the
        allowed time limit.
      title: ChatFinishReason
    UsageBilledUnits:
      type: object
      properties:
        input_tokens:
          type: number
          format: double
          description: |
            The number of billed input tokens.
        output_tokens:
          type: number
          format: double
          description: |
            The number of billed output tokens.
        search_units:
          type: number
          format: double
          description: |
            The number of billed search units.
        classifications:
          type: number
          format: double
          description: |
            The number of billed classifications units.
      title: UsageBilledUnits
    UsageTokens:
      type: object
      properties:
        input_tokens:
          type: number
          format: double
          description: |
            The number of tokens used as input to the model.
        output_tokens:
          type: number
          format: double
          description: |
            The number of tokens produced by the model.
      title: UsageTokens
    Usage:
      type: object
      properties:
        billed_units:
          $ref: '#/components/schemas/UsageBilledUnits'
        tokens:
          $ref: '#/components/schemas/UsageTokens'
        cached_tokens:
          type: number
          format: double
          description: |
            The number of prompt tokens that hit the inference cache.
      title: Usage
    ChatMessageEndEventDelta:
      type: object
      properties:
        error:
          type: string
          description: |
            An error message if an error occurred during the generation.
        finish_reason:
          $ref: '#/components/schemas/ChatFinishReason'
        usage:
          $ref: '#/components/schemas/Usage'
      title: ChatMessageEndEventDelta
    ChatStreamEventEventType:
      type: string
      enum:
        - stream-start
        - search-queries-generation
        - search-results
        - text-generation
        - citation-generation
        - stream-end
        - debug
      title: ChatStreamEventEventType
    v2_chat_Response_stream_streaming:
      oneOf:
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            id:
              type: string
              description: Unique identifier for the generated reply.
            delta:
              $ref: '#/components/schemas/ChatMessageStartEventDelta'
          required:
            - type
          description: message-start variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            index:
              type: integer
            delta:
              $ref: '#/components/schemas/ChatContentStartEventDelta'
          required:
            - type
          description: content-start variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            index:
              type: integer
            delta:
              $ref: '#/components/schemas/ChatContentDeltaEventDelta'
            logprobs:
              $ref: '#/components/schemas/LogprobItem'
          required:
            - type
          description: content-delta variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            index:
              type: integer
          required:
            - type
          description: content-end variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            delta:
              $ref: '#/components/schemas/ChatToolPlanDeltaEventDelta'
          required:
            - type
          description: tool-plan-delta variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            index:
              type: integer
            delta:
              $ref: '#/components/schemas/ChatToolCallStartEventDelta'
          required:
            - type
          description: tool-call-start variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            index:
              type: integer
            delta:
              $ref: '#/components/schemas/ChatToolCallDeltaEventDelta'
          required:
            - type
          description: tool-call-delta variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            index:
              type: integer
          required:
            - type
          description: tool-call-end variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            index:
              type: integer
            delta:
              $ref: '#/components/schemas/CitationStartEventDelta'
          required:
            - type
          description: citation-start variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            index:
              type: integer
          required:
            - type
          description: citation-end variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/ChatStreamEventTypeType'
            id:
              type: string
            delta:
              $ref: '#/components/schemas/ChatMessageEndEventDelta'
          required:
            - type
          description: message-end variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - debug
              description: 'Discriminator value: debug'
            event_type:
              $ref: '#/components/schemas/ChatStreamEventEventType'
            prompt:
              type: string
          required:
            - type
            - event_type
          description: debug variant
      discriminator:
        propertyName: type
      description: >-
        StreamedChatResponse is returned in streaming mode (specified with
        `stream=True` in the request).
      title: v2_chat_Response_stream_streaming
    Chatv2RequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Chatv2RequestBadRequestError
    Chatv2RequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Chatv2RequestUnauthorizedError
    Chatv2RequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Chatv2RequestForbiddenError
    Chatv2RequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Chatv2RequestNotFoundError
    Chatv2RequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Chatv2RequestUnprocessableEntityError
    Chatv2RequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Chatv2RequestTooManyRequestsError
    Chatv2RequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Chatv2RequestInvalidTokenError
    Chatv2RequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Chatv2RequestClientClosedRequestError
    Chatv2RequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Chatv2RequestInternalServerError
    Chatv2RequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Chatv2RequestNotImplementedError
    Chatv2RequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Chatv2RequestServiceUnavailableError
    Chatv2RequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Chatv2RequestGatewayTimeoutError
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript Default
const { CohereClientV2 } = require('cohere-ai');

const cohere = new CohereClientV2({});

(async () => {
  const stream = await cohere.chatStream({
    model: 'command-a-03-2025',
    messages: [
      {
        role: 'user',
        content: 'Tell me about LLMs',
      },
    ],
  });

  for await (const chatEvent of stream) {
    if (chatEvent.type === 'content-delta') {
      console.log(chatEvent.delta?.message);
    }
  }
})();

```

```typescript Default
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.v2.chatStream({
        stream: true,
        model: "command-a-03-2025",
        messages: [
            {
                role: "user",
                content: "Tell me about LLMs",
            },
        ],
    });
}
main();

```

```python Default
import cohere

co = cohere.ClientV2()

response = co.chat_stream(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": "Tell me about LLMs"}],
)

for event in response:
    if event.type == "content-delta":
        print(event.delta.message.content.text, end="")

```

```python Default
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.v2.chat_stream(
    model="command-a-03-2025",
    messages=[
        {
            "role": "user",
            "content": "Tell me about LLMs"
        }
    ]
)

```

```java Default
/* (C)2024 */
package chatv2post;

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2ChatStreamRequest;
import com.cohere.api.types.*;
import java.util.List;

public class Stream {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    Iterable<StreamedChatResponseV2> response =
        cohere
            .v2()
            .chatStream(
                V2ChatStreamRequest.builder()
                    .model("command-a-03-2025")
                    .messages(
                        List.of(
                            ChatMessageV2.user(
                                UserMessage.builder()
                                    .content(UserMessageContent.of("Tell me about LLMs"))
                                    .build())))
                    .build());

    for (StreamedChatResponseV2 chatResponse : response) {
      if (chatResponse.isContentDelta()) {
        System.out.println(
            chatResponse
                .getContentDelta()
                .flatMap(ChatContentDeltaEvent::getDelta)
                .flatMap(ChatContentDeltaEventDelta::getMessage)
                .flatMap(ChatContentDeltaEventDeltaMessage::getContent)
                .flatMap(ChatContentDeltaEventDeltaMessageContent::getText)
                .orElse(""));
      }
    }

    System.out.println(response);
  }
}

```

```go Default
package main

import (
	"context"
	"errors"
	"io"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.ChatStream(
		context.TODO(),
		&cohere.V2ChatStreamRequest{
			Model: "command-a-03-2025",
			Messages: cohere.ChatMessages{
				{
					Role: "user",
					User: &cohere.UserMessageV2{
						Content: &cohere.UserMessageV2Content{
							String: "Tell me about LLMs",
						},
					},
				},
			},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	// Make sure to close the stream when you're done reading.
	// This is easily handled with defer.
	defer resp.Close()

	for {
		message, err := resp.Recv()

		if errors.Is(err, io.EOF) {
			// An io.EOF error means the server is done sending messages
			// and should be treated as a success.
			break
		}

		if message.ContentDelta != nil {
			log.Printf("%+v", message)
		}
	}
}

```

```ruby Default
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/chat")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"stream\": true,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Tell me about LLMs\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Default
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/chat', [
  'body' => '{
  "stream": true,
  "model": "command-a-03-2025",
  "messages": [
    {
      "role": "user",
      "content": "Tell me about LLMs"
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Default
using RestSharp;

var client = new RestClient("https://api.cohere.com/v2/chat");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"stream\": true,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Tell me about LLMs\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Default
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "stream": true,
  "model": "command-a-03-2025",
  "messages": [
    [
      "role": "user",
      "content": "Tell me about LLMs"
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/chat")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```typescript Documents
const { CohereClientV2 } = require('cohere-ai');

const cohere = new CohereClientV2({});

(async () => {
  const stream = await cohere.chatStream({
    model: 'command-a-03-2025',
    documents: [
      {
        data: {
          title: 'CSPC: Backstreet Boys Popularity Analysis - ChartMasters',
          snippet:
            '↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: Backstreet Boys Popularity Analysis\n\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\n\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\n\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.',
        },
      },
      {
        data: {
          title: 'CSPC: NSYNC Popularity Analysis - ChartMasters',
          snippet:
            "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven't study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn't a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.",
        },
      },
      {
        data: {
          title: 'CSPC: Backstreet Boys Popularity Analysis - ChartMasters',
          snippet:
            " 1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\n\nYet the way many music consumers – especially teenagers and young women's – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\n\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.",
        },
      },
      {
        data: {
          title: 'CSPC: NSYNC Popularity Analysis - ChartMasters',
          snippet:
            " Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\n\nAs usual, I'll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC's albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.",
        },
      },
    ],
    messages: [
      {
        role: 'user',
        content: 'Who is more popular: Nsync or Backstreet Boys?',
      },
    ],
  });

  for await (const chatEvent of stream) {
    console.log(chatEvent);
  }
})();

```

```typescript Documents
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.v2.chatStream({
        stream: true,
        model: "command-a-03-2025",
        messages: [
            {
                role: "user",
                content: "Who is more popular: Nsync or Backstreet Boys?",
            },
        ],
        documents: [
            {
                data: {
                    "content": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
                    "snippet": "↓ Skip to Main Content
                    
                    Music industry – One step closer to being accurate
                    
                    CSPC: Backstreet Boys Popularity Analysis
                    
                    Hernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band
                    
                    At one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.
                    
                    It is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.",
                },
            },
            {
                data: {
                    "content": "CSPC: NSYNC Popularity Analysis - ChartMasters",
                    "snippet": "↓ Skip to Main Content
                    
                    Music industry – One step closer to being accurate
                    
                    CSPC: NSYNC Popularity Analysis
                    
                    MJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync
                    
                    At the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.
                    
                    It wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.",
                },
            },
            {
                data: {
                    "content": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
                    "snippet": "1997, 1998, 2000 and 2001 also rank amongst some of the very best years.
                    Yet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.
                    
                    We will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.",
                },
            },
            {
                data: {
                    "content": "CSPC: NSYNC Popularity Analysis - ChartMasters",
                    "snippet": "Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?
                    As usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.",
                },
            },
        ],
    });
}
main();

```

```python Documents
import cohere

co = cohere.ClientV2()

response = co.chat_stream(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": "Who is more popular: Nsync or Backstreet Boys?"}],
    documents=[
        {
            "data":  {
                "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
                "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: Backstreet Boys Popularity Analysis\n\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\n\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\n\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.",
            }
        },
        {
            "data":  {
                "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
                "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven't study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn't a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.",
            }
        },
        {
            "data":  {
                "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
                "snippet": " 1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\n\nYet the way many music consumers – especially teenagers and young women's – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\n\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.",
            }
        },
        {
            "data":  {
                "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
                "snippet": " Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\n\nAs usual, I'll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC's albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.",
            }
        }
    ],
)

for event in response:
    if event.type == "message-start":
        print("\nMessage started.")
    elif event.type == "message-end":
        print("\nMessage ended.")
    elif event.type == "content-delta":
        print(event.delta.message.content.text, end="")


```

```python Documents
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.v2.chat_stream(
    model="command-a-03-2025",
    messages=[
        {
            "role": "user",
            "content": "Who is more popular: Nsync or Backstreet Boys?"
        }
    ],
    documents=[
        {
            "data": {
                "content": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
                "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: Backstreet Boys Popularity Analysis\n\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\n\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\n\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak."
            }
        },
        {
            "data": {
                "content": "CSPC: NSYNC Popularity Analysis - ChartMasters",
                "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N\'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold."
            }
        },
        {
            "data": {
                "content": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
                "snippet": "1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\n\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers."
            }
        },
        {
            "data": {
                "content": "CSPC: NSYNC Popularity Analysis - ChartMasters",
                "snippet": "Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures."
            }
        }
    ]
)

```

```java Documents
/* (C)2024 */
package chatv2post;

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2ChatStreamRequest;
import com.cohere.api.resources.v2.types.V2ChatStreamRequestDocumentsItem;
import com.cohere.api.types.*;
import java.util.List;

public class StreamDocuments {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    Iterable<StreamedChatResponseV2> response =
        cohere
            .v2()
            .chatStream(
                V2ChatStreamRequest.builder()
                    .model("command-a-03-2025")
                    .messages(
                        List.of(
                            ChatMessageV2.user(
                                UserMessage.builder()
                                    .content(UserMessageContent.of("Who is the most popular?"))
                                    .build())))
                    .documents(
                        List.of(
                            V2ChatStreamRequestDocumentsItem.of(
                                "↓ Skip to Main Content\n\n"
                                    + "Music industry – One step closer to being accurate\n\n"
                                    + "CSPC: Backstreet Boys Popularity Analysis\n\n"
                                    + "At one point, Backstreet Boys defined success: massive album"
                                    + " sales..."),
                            V2ChatStreamRequestDocumentsItem.of(
                                "↓ Skip to Main Content\n\n"
                                    + "CSPC: NSYNC Popularity Analysis\n\n"
                                    + "At the turn of the millennium, three teen acts were huge:"
                                    + " Backstreet Boys, Britney Spears, and NSYNC..."),
                            V2ChatStreamRequestDocumentsItem.of(
                                "Yet the way many music consumers embraced Backstreet Boys deserves"
                                    + " its own chapter..."),
                            V2ChatStreamRequestDocumentsItem.of(
                                "Was NSYNC only successful in the US, or were they a global"
                                    + " phenomenon?...")))
                    .build());

    for (StreamedChatResponseV2 chatResponse : response) {
      if (chatResponse.isContentDelta()) {
        String text =
            chatResponse
                .getContentDelta()
                .flatMap(ChatContentDeltaEvent::getDelta)
                .flatMap(ChatContentDeltaEventDelta::getMessage)
                .flatMap(ChatContentDeltaEventDeltaMessage::getContent)
                .flatMap(ChatContentDeltaEventDeltaMessageContent::getText)
                .orElse("");
        System.out.println(text);
      }
    }
  }
}

```

```go Documents
package main

import (
	"context"
	"errors"
	"io"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.ChatStream(
		context.TODO(),
		&cohere.V2ChatStreamRequest{
			Model: "command-a-03-2025",
			Documents: []*cohere.V2ChatStreamRequestDocumentsItem{
				{
					Document: &cohere.Document{
						Data: map[string]interface{}{
							"title":   "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
							"snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: Backstreet Boys Popularity Analysis\n\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\n\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\n\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.",
						},
					},
				},
				{
					Document: &cohere.Document{
						Data: map[string]interface{}{
							"title":   "CSPC: NSYNC Popularity Analysis - ChartMasters",
							"snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven't study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn't a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.",
						},
					},
				},
				{
					Document: &cohere.Document{
						Data: map[string]interface{}{
							"title":   "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
							"snippet": " 1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\n\nYet the way many music consumers – especially teenagers and young women's – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\n\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.",
						},
					},
				},
				{
					Document: &cohere.Document{
						Data: map[string]interface{}{
							"title":   "CSPC: NSYNC Popularity Analysis - ChartMasters",
							"snippet": " Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\n\nAs usual, I'll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC's albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.",
						},
					},
				},
			},
			Messages: cohere.ChatMessages{
				{
					Role: "user",
					User: &cohere.UserMessageV2{
						Content: &cohere.UserMessageV2Content{
							String: "Who is more popular: Nsync or Backstreet Boys?",
						},
					},
				},
			},
		},
	)

	if err != nil {
		log.Fatal(err)
	}
	defer resp.Close()

	for {
		message, err := resp.Recv()

		if errors.Is(err, io.EOF) {
			// An io.EOF error means the server is done sending messages
			// and should be treated as a success.
			break
		}

		// Log the received message
		if message.ContentDelta != nil {
			log.Printf("%+v", message)
		}
	}
}

```

```ruby Documents
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/chat")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"stream\": true,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Who is more popular: Nsync or Backstreet Boys?\"\n    }\n  ],\n  \"documents\": [\n    {\n      \"data\": {\n        \"content\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n        \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: Backstreet Boys Popularity Analysis\\n\\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\\n\\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\\n\\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n        \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: NSYNC Popularity Analysis\\n\\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\\n\\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\\n\\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n        \"snippet\": \"1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\\n\\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n        \"snippet\": \"Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.\"\n      }\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Documents
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/chat', [
  'body' => '{
  "stream": true,
  "model": "command-a-03-2025",
  "messages": [
    {
      "role": "user",
      "content": "Who is more popular: Nsync or Backstreet Boys?"
    }
  ],
  "documents": [
    {
      "data": {
        "content": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
        "snippet": "↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: Backstreet Boys Popularity Analysis\\n\\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\\n\\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\\n\\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak."
      }
    },
    {
      "data": {
        "content": "CSPC: NSYNC Popularity Analysis - ChartMasters",
        "snippet": "↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: NSYNC Popularity Analysis\\n\\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N\'Sync\\n\\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\\n\\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold."
      }
    },
    {
      "data": {
        "content": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
        "snippet": "1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\\n\\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers."
      }
    },
    {
      "data": {
        "content": "CSPC: NSYNC Popularity Analysis - ChartMasters",
        "snippet": "Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures."
      }
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Documents
using RestSharp;

var client = new RestClient("https://api.cohere.com/v2/chat");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"stream\": true,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Who is more popular: Nsync or Backstreet Boys?\"\n    }\n  ],\n  \"documents\": [\n    {\n      \"data\": {\n        \"content\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n        \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: Backstreet Boys Popularity Analysis\\n\\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\\n\\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\\n\\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n        \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: NSYNC Popularity Analysis\\n\\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\\n\\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\\n\\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n        \"snippet\": \"1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\\n\\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n        \"snippet\": \"Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.\"\n      }\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Documents
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "stream": true,
  "model": "command-a-03-2025",
  "messages": [
    [
      "role": "user",
      "content": "Who is more popular: Nsync or Backstreet Boys?"
    ]
  ],
  "documents": [["data": [
        "content": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
        "snippet": "↓ Skip to Main Content

Music industry – One step closer to being accurate

CSPC: Backstreet Boys Popularity Analysis

Hernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band

At one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.

It is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak."
      ]], ["data": [
        "content": "CSPC: NSYNC Popularity Analysis - ChartMasters",
        "snippet": "↓ Skip to Main Content

Music industry – One step closer to being accurate

CSPC: NSYNC Popularity Analysis

MJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync

At the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.

It wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold."
      ]], ["data": [
        "content": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
        "snippet": "1997, 1998, 2000 and 2001 also rank amongst some of the very best years.
Yet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.

We will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers."
      ]], ["data": [
        "content": "CSPC: NSYNC Popularity Analysis - ChartMasters",
        "snippet": "Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?
As usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures."
      ]]]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/chat")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```typescript Tools
const { CohereClientV2 } = require('cohere-ai');

const cohere = new CohereClientV2({});

(async () => {
  const stream = await cohere.chatStream({
    model: 'command-a-03-2025',
    messages: [
      {
        role: 'user',
        content:
          "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?",
      },
    ],
    tools: [
      {
        type: 'function',
        function: {
          name: 'query_daily_sales_report',
          description:
            'Connects to a database to retrieve overall sales volumes and sales information for a given day.',
          parameters: {
            type: 'object',
            properties: {
              day: {
                description: 'Retrieves sales data for this day, formatted as YYYY-MM-DD.',
                type: 'string',
              },
            },
            required: ['day'],
          },
        },
      },
      {
        type: 'function',
        function: {
          name: 'query_product_catalog',
          description:
            'Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels.',
          parameters: {
            type: 'object',
            properties: {
              category: {
                description:
                  'Retrieves product information data for all products in this category.',
                type: 'string',
              },
            },
            required: ['category'],
          },
        },
      },
    ],
  });

  for await (const chatEvent of stream) {
    if (chatEvent.type === 'tool-call-delta') {
      console.log(chatEvent.delta?.message);
    }
  }
})();

```

```typescript Tools
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.v2.chatStream({
        stream: true,
        model: "command-a-03-2025",
        messages: [
            {
                role: "user",
                content: "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?",
            },
        ],
        tools: [
            {
                type: "function",
                function: {
                    name: "query_daily_sales_report",
                    parameters: {
                        "type": "object",
                        "properties": {
                            day: {
                                description: "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
                                type: "string",
                            },
                        },
                    },
                    description: "Connects to a database to retrieve overall sales volumes and sales information for a given day.",
                },
            },
            {
                type: "function",
                function: {
                    name: "query_product_catalog",
                    parameters: {
                        "type": "object",
                        "properties": {
                            category: {
                                description: "Retrieves product information data for all products in this category.",
                                type: "string",
                            },
                        },
                    },
                    description: "Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels.",
                },
            },
        ],
    });
}
main();

```

```python Tools
import cohere

co = cohere.ClientV2()

response = co.chat_stream(
    model="command-a-03-2025",
    messages=[
        {
            "role": "user",
            "content": "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?",
        }
    ],
    tools=[
        cohere.ToolV2(
            type="function",
            function={
                "name": "query_daily_sales_report",
                "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "day": {
                            "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
                            "type": "string",
                        }
                    },
                    "required": ["day"],
                },
            },
        ),
        cohere.ToolV2(
            type="function",
            function={
                "name": "query_product_catalog",
                "description": "Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "description": "Retrieves product information data for all products in this category.",
                            "type": "string",
                        }
                    },
                    "required": ["category"],
                },
            },
        ),
    ],
)

for event in response:
    if event.type in ["tool-call-start", "tool-call-delta"]:
        for tool_call in event.delta.message.tool_calls:
            print(tool_call)

```

```python Tools
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.v2.chat_stream(
    model="command-a-03-2025",
    messages=[
        {
            "role": "user",
            "content": "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the \'Electronics\' category, for example their prices and stock levels?"
        }
    ],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "query_daily_sales_report",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "day": {
                            "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
                            "type": "string",
                        },
                    }
                },
                "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day."
            }
        },
        {
            "type": "function",
            "function": {
                "name": "query_product_catalog",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "description": "Retrieves product information data for all products in this category.",
                            "type": "string",
                        },
                    }
                },
                "description": "Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels."
            }
        }
    ]
)

```

```java Tools
/* (C)2024 */
package chatv2post;

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2ChatStreamRequest;
import com.cohere.api.types.*;
import java.util.List;
import java.util.Map;

public class StreamTools {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    Iterable<StreamedChatResponseV2> response =
        cohere
            .v2()
            .chatStream(
                V2ChatStreamRequest.builder()
                    .model("command-a-03-2025")
                    .tools(
                        List.of(
                            ToolV2.builder()
                                .function(
                                    ToolV2Function.builder()
                                        .name("query_daily_sales_report")
                                        .description(
                                            "Connects to a database to retrieve overall sales"
                                                + " volumes and sales information for a given day.")
                                        .parameters(
                                            Map.of(
                                                "day",
                                                ToolParameterDefinitionsValue.builder()
                                                    .type("str")
                                                    .description(
                                                        "Retrieves sales data for this day,"
                                                            + " formatted as YYYY-MM-DD.")
                                                    .required(true)
                                                    .build()))
                                        .build())
                                .build(),
                            ToolV2.builder()
                                .function(
                                    ToolV2Function.builder()
                                        .name("query_product_catalog")
                                        .description(
                                            "Connects to a product catalog with information about"
                                                + " all the products being sold, including"
                                                + " categories, prices, and stock levels.")
                                        .parameters(
                                            Map.of(
                                                "category",
                                                ToolParameterDefinitionsValue.builder()
                                                    .type("str")
                                                    .description(
                                                        "Retrieves product information data for all"
                                                            + " products in this category.")
                                                    .required(true)
                                                    .build()))
                                        .build())
                                .build()))
                    .messages(
                        List.of(
                            ChatMessageV2.user(
                                UserMessage.builder()
                                    .content(
                                        UserMessageContent.of(
                                            "Can you provide a sales summary for 29th September"
                                                + " 2023, and also give me some details about the"
                                                + " products in the 'Electronics' category?"))
                                    .build())))
                    .build());

    for (StreamedChatResponseV2 chatResponse : response) {
      if (chatResponse.isContentDelta()) {
        String text =
            chatResponse
                .getContentDelta()
                .flatMap(ChatContentDeltaEvent::getDelta)
                .flatMap(ChatContentDeltaEventDelta::getMessage)
                .flatMap(ChatContentDeltaEventDeltaMessage::getContent)
                .flatMap(ChatContentDeltaEventDeltaMessageContent::getText)
                .orElse("");
        System.out.println(text);
      }
    }
  }
}

```

```go Tools
package main

import (
	"context"
	"errors"
	"io"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.ChatStream(
		context.TODO(),
		&cohere.V2ChatStreamRequest{
			Model: "command-a-03-2025",
			Messages: cohere.ChatMessages{
				{
					Role: "user",
					User: &cohere.UserMessageV2{
						Content: &cohere.UserMessageV2Content{
							String: "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?",
						},
					},
				},
			},
			Tools: []*cohere.ToolV2{
				{
					Function: &cohere.ToolV2Function{
						Name:        "query_daily_sales_report",
						Description: cohere.String("Connects to a database to retrieve overall sales volumes and sales information for a given day."),
						Parameters: map[string]interface{}{
							"type": "object",
							"properties": map[string]interface{}{
								"day": map[string]interface{}{
									"type":        "string",
									"description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
								},
							},
							"required": []string{"day"},
						},
					},
				},
				{
					Function: &cohere.ToolV2Function{
						Name:        "query_product_catalog",
						Description: cohere.String("Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels."),
						Parameters: map[string]interface{}{
							"type": "object",
							"properties": map[string]interface{}{
								"category": map[string]interface{}{
									"type":        "string",
									"description": "Retrieves product information data for all products in this category.",
								},
							},
							"required": []string{"category"},
						},
					},
				},
			},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	// Make sure to close the stream when you're done reading.
	// This is easily handled with defer.
	defer resp.Close()

	for {
		message, err := resp.Recv()

		if errors.Is(err, io.EOF) {
			// An io.EOF error means the server is done sending messages
			// and should be treated as a success.
			break
		}

		// Log the received message
		if message.ToolCallDelta != nil {
			log.Printf("%+v", message)
		}
	}
}

```

```ruby Tools
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/chat")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"stream\": true,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"function\": {\n        \"name\": \"query_daily_sales_report\",\n        \"parameters\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"day\": {\n              \"description\": \"Retrieves sales data for this day, formatted as YYYY-MM-DD.\",\n              \"type\": \"string\"\n            }\n          }\n        },\n        \"description\": \"Connects to a database to retrieve overall sales volumes and sales information for a given day.\"\n      }\n    },\n    {\n      \"type\": \"function\",\n      \"function\": {\n        \"name\": \"query_product_catalog\",\n        \"parameters\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"category\": {\n              \"description\": \"Retrieves product information data for all products in this category.\",\n              \"type\": \"string\"\n            }\n          }\n        },\n        \"description\": \"Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels.\"\n      }\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Tools
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/chat', [
  'body' => '{
  "stream": true,
  "model": "command-a-03-2025",
  "messages": [
    {
      "role": "user",
      "content": "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the \'Electronics\' category, for example their prices and stock levels?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "query_daily_sales_report",
        "parameters": {
          "type": "object",
          "properties": {
            "day": {
              "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
              "type": "string"
            }
          }
        },
        "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day."
      }
    },
    {
      "type": "function",
      "function": {
        "name": "query_product_catalog",
        "parameters": {
          "type": "object",
          "properties": {
            "category": {
              "description": "Retrieves product information data for all products in this category.",
              "type": "string"
            }
          }
        },
        "description": "Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels."
      }
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Tools
using RestSharp;

var client = new RestClient("https://api.cohere.com/v2/chat");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"stream\": true,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"function\": {\n        \"name\": \"query_daily_sales_report\",\n        \"parameters\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"day\": {\n              \"description\": \"Retrieves sales data for this day, formatted as YYYY-MM-DD.\",\n              \"type\": \"string\"\n            }\n          }\n        },\n        \"description\": \"Connects to a database to retrieve overall sales volumes and sales information for a given day.\"\n      }\n    },\n    {\n      \"type\": \"function\",\n      \"function\": {\n        \"name\": \"query_product_catalog\",\n        \"parameters\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"category\": {\n              \"description\": \"Retrieves product information data for all products in this category.\",\n              \"type\": \"string\"\n            }\n          }\n        },\n        \"description\": \"Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels.\"\n      }\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Tools
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "stream": true,
  "model": "command-a-03-2025",
  "messages": [
    [
      "role": "user",
      "content": "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?"
    ]
  ],
  "tools": [
    [
      "type": "function",
      "function": [
        "name": "query_daily_sales_report",
        "parameters": [
          "type": "object",
          "properties": ["day": [
              "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
              "type": "string"
            ]]
        ],
        "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day."
      ]
    ],
    [
      "type": "function",
      "function": [
        "name": "query_product_catalog",
        "parameters": [
          "type": "object",
          "properties": ["category": [
              "description": "Retrieves product information data for all products in this category.",
              "type": "string"
            ]]
        ],
        "description": "Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels."
      ]
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/chat")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```typescript Images
const { CohereClientV2 } = require('cohere-ai');

const cohere = new CohereClientV2({});

(async () => {
  const stream = await cohere.chatStream({
    model: 'command-a-vision-07-2025',
    messages: [
      {
        role: 'user',
        content: [
          { type: 'text', text: 'Describe this image' },
          {
            type: 'image_url',
            imageUrl: {
              // Can be either a base64 data URI or a web URL.
              url: 'https://cohere.com/favicon-32x32.png',
              detail: 'auto',
            },
          },
        ],
      },
    ],
  });

  for await (const chatEvent of stream) {
    if (chatEvent.type === 'content-delta') {
      console.log(chatEvent.delta?.message);
    }
  }
})();

```

```typescript Images
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.v2.chatStream({
        stream: true,
        model: "command-a-vision-07-2025",
        messages: [
            {
                role: "user",
                content: [
                    {
                        type: "text",
                        text: "Describe this image",
                    },
                    {
                        type: "image_url",
                        imageUrl: {
                            url: "https://cohere.com/favicon-32x32.png",
                            detail: "auto",
                        },
                    },
                ],
            },
        ],
    });
}
main();

```

```python Images
import cohere

co = cohere.ClientV2()

response = co.chat_stream(
    model="command-a-vision-07-2025",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Describe this image"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        # Can be either a base64 data URI or a web URL.
                        "url": "https://cohere.com/favicon-32x32.png",
                        "detail": "auto"
                    }
                }
            ]
        }
    ]
)

for event in response:
    if event.type == "content-delta":
        print(event.delta.message.content.text, end="")
```

```python Images
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.v2.chat_stream(
    model="command-a-vision-07-2025",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Describe this image"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://cohere.com/favicon-32x32.png",
                        "detail": "auto"
                    }
                }
            ]
        }
    ]
)

```

```java Images
/* (C)2024 */
package chatv2post;

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2ChatStreamRequest;
import com.cohere.api.types.*;
import java.util.List;

public class Stream {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    Iterable<StreamedChatResponseV2> response =
        cohere
            .v2()
            .chatStream(
                V2ChatStreamRequest.builder()
                    .model("command-a-vision-07-2025")
                    .messages(
                        List.of(
                            ChatMessageV2.user(
                                UserMessage.builder()
                                    .content(
                                        UserMessageContent.of(
                                            List.of(
                                                Content.text(
                                                    TextContent.builder()
                                                        .text("Describe this image")
                                                        .build()),
                                                Content.imageUrl(
                                                    ImageContent.builder()
                                                        .imageUrl(
                                                            ImageUrl.builder()
                                                                // Can be either a base64 data URI or a web URL.
                                                                .url(
                                                                    "https://cohere.com/favicon-32x32.png")
                                                                .build())
                                                        .build()))))
                                    .build())))
                    .build());

    for (StreamedChatResponseV2 chatResponse : response) {
      if (chatResponse.isContentDelta()) {
        System.out.println(
            chatResponse
                .getContentDelta()
                .flatMap(ChatContentDeltaEvent::getDelta)
                .flatMap(ChatContentDeltaEventDelta::getMessage)
                .flatMap(ChatContentDeltaEventDeltaMessage::getContent)
                .flatMap(ChatContentDeltaEventDeltaMessageContent::getText)
                .orElse(""));
      }
    }

    System.out.println(response);
  }
}

```

```go Images
package main

import (
	"context"
	"errors"
	"io"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.ChatStream(
		context.TODO(),
		&cohere.V2ChatStreamRequest{
			Model: "command-a-vision-07-2025",
			Messages: cohere.ChatMessages{
				{
					Role: "user",
					User: &cohere.UserMessageV2{
						Content: &cohere.UserMessageV2Content{
							ContentList: []*cohere.Content{
								{Type: "text", Text: &cohere.ChatTextContent{Text: "Describe this image"}},
								{Type: "image_url", ImageUrl: &cohere.ImageContent{
									ImageUrl: &cohere.ImageUrl{
										// Can be either a base64 data URI or a web URL.
										Url:    "https://cohere.com/favicon-32x32.png",
										Detail: cohere.ImageUrlDetailAuto.Ptr(),
									},
								}},
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	// Make sure to close the stream when you're done reading.
	// This is easily handled with defer.
	defer resp.Close()

	for {
		message, err := resp.Recv()

		if errors.Is(err, io.EOF) {
			// An io.EOF error means the server is done sending messages
			// and should be treated as a success.
			break
		}

		if message.ContentDelta != nil {
			log.Printf("%+v", message)
		}
	}
}

```

```ruby Images
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/chat")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"stream\": true,\n  \"model\": \"command-a-vision-07-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": [\n        {\n          \"type\": \"text\",\n          \"text\": \"Describe this image\"\n        },\n        {\n          \"type\": \"image_url\",\n          \"image_url\": {\n            \"url\": \"https://cohere.com/favicon-32x32.png\",\n            \"detail\": \"auto\"\n          }\n        }\n      ]\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Images
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/chat', [
  'body' => '{
  "stream": true,
  "model": "command-a-vision-07-2025",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Describe this image"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://cohere.com/favicon-32x32.png",
            "detail": "auto"
          }
        }
      ]
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Images
using RestSharp;

var client = new RestClient("https://api.cohere.com/v2/chat");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"stream\": true,\n  \"model\": \"command-a-vision-07-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": [\n        {\n          \"type\": \"text\",\n          \"text\": \"Describe this image\"\n        },\n        {\n          \"type\": \"image_url\",\n          \"image_url\": {\n            \"url\": \"https://cohere.com/favicon-32x32.png\",\n            \"detail\": \"auto\"\n          }\n        }\n      ]\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Images
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "stream": true,
  "model": "command-a-vision-07-2025",
  "messages": [
    [
      "role": "user",
      "content": [
        [
          "type": "text",
          "text": "Describe this image"
        ],
        [
          "type": "image_url",
          "image_url": [
            "url": "https://cohere.com/favicon-32x32.png",
            "detail": "auto"
          ]
        ]
      ]
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/chat")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```