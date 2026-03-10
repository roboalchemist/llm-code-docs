# Source: https://docs.cohere.com/reference/chat-stream-v1.mdx

# Chat with Streaming Outputs (API V1)

POST https://api.cohere.com/v1/chat
Content-Type: application/json

Generates a streamed text response to a user message.

To learn how to use the Chat API and RAG follow our [Text Generation guides](https://docs.cohere.com/docs/chat-api).


Reference: https://docs.cohere.com/reference/chat-stream-v1

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/chat:
    post:
      operationId: chat-stream
      summary: Chat API (v1)
      description: >
        Generates a streamed text response to a user message.


        To learn how to use the Chat API and RAG follow our [Text Generation
        guides](https://docs.cohere.com/docs/chat-api).
      tags:
        - ''
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
        - name: Accepts
          in: header
          description: >
            Pass text/event-stream to receive the streamed response as
            server-sent events. The default is `\n` delimited events.
          required: false
          schema:
            $ref: '#/components/schemas/V1ChatPostParametersAccepts'
      responses:
        '200':
          description: >
            Generates a streamed text response to a user message.


            To learn how to use the Chat API and RAG follow our [Text Generation
            guides](https://docs.cohere.com/docs/chat-api).
          content:
            text/event-stream:
              schema:
                $ref: '#/components/schemas/chat_Response_stream_streaming'
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
                $ref: '#/components/schemas/ChatRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatRequestNotFoundError'
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
                $ref: '#/components/schemas/ChatRequestUnprocessableEntityError'
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatRequestTooManyRequestsError'
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatRequestClientClosedRequestError'
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatRequestInternalServerError'
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatRequestNotImplementedError'
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatRequestServiceUnavailableError'
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatRequestGatewayTimeoutError'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  description: >
                    Text input for the model to respond to.


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
                model:
                  type: string
                  description: >
                    The name of a compatible [Cohere
                    model](https://docs.cohere.com/docs/models) or the ID of a
                    [fine-tuned](https://docs.cohere.com/docs/chat-fine-tuning)
                    model.


                    Compatible Deployments: Cohere Platform, Private Deployments
                stream:
                  type: boolean
                  enum:
                    - true
                  description: >
                    Defaults to `false`.


                    When `true`, the response will be a JSON stream of events.
                    The final event will contain the complete response, and will
                    have an `event_type` of `"stream-end"`.


                    Streaming is beneficial for user interfaces that render the
                    contents of the response piece by piece, as it gets
                    generated.


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
                preamble:
                  type: string
                  description: >
                    When specified, the default Cohere preamble will be replaced
                    with the provided one. Preambles are a part of the prompt
                    used to adjust the model's overall behavior and conversation
                    style, and use the `SYSTEM` role.


                    The `SYSTEM` role is also used for the contents of the
                    optional `chat_history=` parameter. When used with the
                    `chat_history=` parameter it adds content throughout a
                    conversation. Conversely, when used with the `preamble=`
                    parameter it adds content at the start of the conversation
                    only.


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
                chat_history:
                  type: array
                  items:
                    $ref: '#/components/schemas/Message'
                  description: >
                    A list of previous messages between the user and the model,
                    giving the model conversational context for responding to
                    the user's `message`.


                    Each item represents a single message in the chat history,
                    excluding the current user turn. It has two properties:
                    `role` and `message`. The `role` identifies the sender
                    (`CHATBOT`, `SYSTEM`, or `USER`), while the `message`
                    contains the text content.


                    The chat_history parameter should not be used for `SYSTEM`
                    messages in most cases. Instead, to add a `SYSTEM` role
                    message at the beginning of a conversation, the `preamble`
                    parameter should be used.


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
                conversation_id:
                  type: string
                  description: >
                    An alternative to `chat_history`.


                    Providing a `conversation_id` creates or resumes a persisted
                    conversation with the specified ID. The ID can be any non
                    empty string.


                    Compatible Deployments: Cohere Platform
                prompt_truncation:
                  $ref: >-
                    #/components/schemas/V1ChatPostRequestBodyContentApplicationJsonSchemaPromptTruncation
                  description: >
                    Defaults to `AUTO` when `connectors` are specified and `OFF`
                    in all other cases.


                    Dictates how the prompt will be constructed.


                    With `prompt_truncation` set to "AUTO", some elements from
                    `chat_history` and `documents` will be dropped in an attempt
                    to construct a prompt that fits within the model's context
                    length limit. During this process the order of the documents
                    and chat history will be changed and ranked by relevance.


                    With `prompt_truncation` set to "AUTO_PRESERVE_ORDER", some
                    elements from `chat_history` and `documents` will be dropped
                    in an attempt to construct a prompt that fits within the
                    model's context length limit. During this process the order
                    of the documents and chat history will be preserved as they
                    are inputted into the API.


                    With `prompt_truncation` set to "OFF", no elements will be
                    dropped. If the sum of the inputs exceeds the model's
                    context length limit, a `TooManyTokens` error will be
                    returned.


                    Compatible Deployments:
                     - AUTO: Cohere Platform Only
                     - AUTO_PRESERVE_ORDER: Azure, AWS Sagemaker/Bedrock, Private Deployments
                connectors:
                  type: array
                  items:
                    $ref: '#/components/schemas/ChatConnector'
                  description: >
                    Accepts `{"id": "web-search"}`, and/or the `"id"` for a
                    custom [connector](https://docs.cohere.com/docs/connectors),
                    if you've
                    [created](https://docs.cohere.com/v1/docs/creating-and-deploying-a-connector)
                    one.


                    When specified, the model's reply will be enriched with
                    information found by querying each of the connectors (RAG).


                    Compatible Deployments: Cohere Platform
                search_queries_only:
                  type: boolean
                  description: >
                    Defaults to `false`.


                    When `true`, the response will only contain a list of
                    generated search queries, but no search will take place, and
                    no reply from the model to the user's `message` will be
                    generated.


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
                documents:
                  type: array
                  items:
                    $ref: '#/components/schemas/ChatDocument'
                  description: >
                    A list of relevant documents that the model can cite to
                    generate a more accurate reply. Each document is a
                    string-string dictionary.


                    Example:

                    ```

                    [
                      { "title": "Tall penguins", "text": "Emperor penguins are the tallest." },
                      { "title": "Penguin habitats", "text": "Emperor penguins only live in Antarctica." },
                    ]

                    ```


                    Keys and values from each document will be serialized to a
                    string and passed to the model. The resulting generation
                    will include citations that reference some of these
                    documents.


                    Some suggested keys are "text", "author", and "date". For
                    better generation quality, it is recommended to keep the
                    total word count of the strings in the dictionary to under
                    300 words.


                    An `id` field (string) can be optionally supplied to
                    identify the document in the citations. This field will not
                    be passed to the model.


                    An `_excludes` field (array of strings) can be optionally
                    supplied to omit some key-value pairs from being shown to
                    the model. The omitted fields will still show up in the
                    citation object. The "_excludes" field will not be passed to
                    the model.


                    See ['Document
                    Mode'](https://docs.cohere.com/docs/retrieval-augmented-generation-rag#document-mode)
                    in the guide for more information.


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
                citation_quality:
                  $ref: >-
                    #/components/schemas/V1ChatPostRequestBodyContentApplicationJsonSchemaCitationQuality
                  description: >
                    Defaults to `"enabled"`.

                    Citations are enabled by default for models that support it,
                    but can be turned off by setting `"type": "disabled"`.


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
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


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
                max_tokens:
                  type: integer
                  description: >
                    The maximum number of tokens the model will generate as part
                    of the response. Note: Setting a low value may result in
                    incomplete generations.


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
                max_input_tokens:
                  type: integer
                  description: >
                    The maximum number of input tokens to send to the model. If
                    not specified, `max_input_tokens` is the model's context
                    length limit minus a small buffer.


                    Input will be truncated according to the `prompt_truncation`
                    parameter.


                    Compatible Deployments: Cohere Platform
                k:
                  type: integer
                  default: 0
                  description: >
                    Ensures only the top `k` most likely tokens are considered
                    for generation at each step.

                    Defaults to `0`, min value of `0`, max value of `500`.


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
                p:
                  type: number
                  format: double
                  default: 0.75
                  description: >
                    Ensures that only the most likely tokens, with total
                    probability mass of `p`, are considered for generation at
                    each step. If both `k` and `p` are enabled, `p` acts after
                    `k`.

                    Defaults to `0.75`. min value of `0.01`, max value of
                    `0.99`.


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
                seed:
                  type: integer
                  description: >
                    If specified, the backend will make a best effort to sample
                    tokens

                    deterministically, such that repeated requests with the same

                    seed and parameters should return the same result. However,

                    determinism cannot be totally guaranteed.


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
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


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
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


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
                presence_penalty:
                  type: number
                  format: double
                  description: >
                    Defaults to `0.0`, min value of `0.0`, max value of `1.0`.


                    Used to reduce repetitiveness of generated tokens. Similar
                    to `frequency_penalty`, except that this penalty is applied
                    equally to all tokens that have already appeared, regardless
                    of their exact frequencies.


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
                raw_prompting:
                  type: boolean
                  description: >
                    When enabled, the user's prompt will be sent to the model
                    without

                    any pre-processing.


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
                tools:
                  type: array
                  items:
                    $ref: '#/components/schemas/Tool'
                  description: >
                    A list of available tools (functions) that the model may
                    suggest invoking before producing a text response.


                    When `tools` is passed (without `tool_results`), the `text`
                    field in the response will be `""` and the `tool_calls`
                    field in the response will be populated with a list of tool
                    calls that need to be made. If no calls need to be made, the
                    `tool_calls` array will be empty.


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
                tool_results:
                  type: array
                  items:
                    $ref: '#/components/schemas/ToolResult'
                  description: >
                    A list of results from invoking tools recommended by the
                    model in the previous chat turn. Results are used to produce
                    a text response and will be referenced in citations. When
                    using `tool_results`, `tools` must be passed as well.

                    Each tool_result contains information about how it was
                    invoked, as well as a list of outputs in the form of
                    dictionaries.


                    **Note**: `outputs` must be a list of objects. If your tool
                    returns a single object (eg `{"status": 200}`), make sure to
                    wrap it in a list.

                    ```

                    tool_results = [
                      {
                        "call": {
                          "name": <tool name>,
                          "parameters": {
                            <param name>: <param value>
                          }
                        },
                        "outputs": [{
                          <key>: <value>
                        }]
                      },
                      ...
                    ]

                    ```

                    **Note**: Chat calls with `tool_results` should not be
                    included in the Chat history to avoid duplication of the
                    message text.


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
                force_single_step:
                  type: boolean
                  description: Forces the chat to be single step. Defaults to `false`.
                response_format:
                  $ref: '#/components/schemas/ResponseFormat'
                safety_mode:
                  $ref: >-
                    #/components/schemas/V1ChatPostRequestBodyContentApplicationJsonSchemaSafetyMode
                  description: >
                    Used to select the [safety
                    instruction](https://docs.cohere.com/docs/safety-modes)
                    inserted into the prompt. Defaults to `CONTEXTUAL`.

                    When `NONE` is specified, the safety instruction will be
                    omitted.


                    Safety modes are not yet configurable in combination with
                    `tools`, `tool_results` and `documents` parameters.


                    **Note**: This parameter is only compatible newer Cohere
                    models, starting with [Command R
                    08-2024](https://docs.cohere.com/docs/command-r#august-2024-release)
                    and [Command R+
                    08-2024](https://docs.cohere.com/docs/command-r-plus#august-2024-release).


                    **Note**: `command-r7b-12-2024` and newer models only
                    support `"CONTEXTUAL"` and `"STRICT"` modes.


                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
              required:
                - message
                - stream
servers:
  - url: https://api.cohere.com
components:
  schemas:
    V1ChatPostParametersAccepts:
      type: string
      enum:
        - text/event-stream
      title: V1ChatPostParametersAccepts
    ToolCall:
      type: object
      properties:
        name:
          type: string
          description: Name of the tool to call.
        parameters:
          type: object
          additionalProperties:
            description: Any type
          description: The name and value of the parameters to use when invoking a tool.
      required:
        - name
        - parameters
      description: >
        Contains the tool calls generated by the model. Use it to invoke your
        tools.
      title: ToolCall
    ToolResult:
      type: object
      properties:
        call:
          $ref: '#/components/schemas/ToolCall'
        outputs:
          type: array
          items:
            type: object
            additionalProperties:
              description: Any type
      required:
        - call
        - outputs
      title: ToolResult
    Message:
      oneOf:
        - type: object
          properties:
            role:
              type: string
              enum:
                - CHATBOT
              description: 'Discriminator value: CHATBOT'
            message:
              type: string
              description: |
                Contents of the chat message.
            tool_calls:
              type: array
              items:
                $ref: '#/components/schemas/ToolCall'
          required:
            - role
            - message
          description: CHATBOT variant
        - type: object
          properties:
            role:
              type: string
              enum:
                - SYSTEM
              description: 'Discriminator value: SYSTEM'
            message:
              type: string
              description: |
                Contents of the chat message.
            tool_calls:
              type: array
              items:
                $ref: '#/components/schemas/ToolCall'
          required:
            - role
            - message
          description: SYSTEM variant
        - type: object
          properties:
            role:
              type: string
              enum:
                - USER
              description: 'Discriminator value: USER'
            message:
              type: string
              description: |
                Contents of the chat message.
            tool_calls:
              type: array
              items:
                $ref: '#/components/schemas/ToolCall'
          required:
            - role
            - message
          description: USER variant
        - type: object
          properties:
            role:
              type: string
              enum:
                - TOOL
              description: 'Discriminator value: TOOL'
            tool_results:
              type: array
              items:
                $ref: '#/components/schemas/ToolResult'
          required:
            - role
          description: TOOL variant
      discriminator:
        propertyName: role
      title: Message
    V1ChatPostRequestBodyContentApplicationJsonSchemaPromptTruncation:
      type: string
      enum:
        - 'OFF'
        - AUTO
        - AUTO_PRESERVE_ORDER
      description: >
        Defaults to `AUTO` when `connectors` are specified and `OFF` in all
        other cases.


        Dictates how the prompt will be constructed.


        With `prompt_truncation` set to "AUTO", some elements from
        `chat_history` and `documents` will be dropped in an attempt to
        construct a prompt that fits within the model's context length limit.
        During this process the order of the documents and chat history will be
        changed and ranked by relevance.


        With `prompt_truncation` set to "AUTO_PRESERVE_ORDER", some elements
        from `chat_history` and `documents` will be dropped in an attempt to
        construct a prompt that fits within the model's context length limit.
        During this process the order of the documents and chat history will be
        preserved as they are inputted into the API.


        With `prompt_truncation` set to "OFF", no elements will be dropped. If
        the sum of the inputs exceeds the model's context length limit, a
        `TooManyTokens` error will be returned.


        Compatible Deployments:
         - AUTO: Cohere Platform Only
         - AUTO_PRESERVE_ORDER: Azure, AWS Sagemaker/Bedrock, Private Deployments
      title: V1ChatPostRequestBodyContentApplicationJsonSchemaPromptTruncation
    ChatConnector-7ur0eu:
      type: object
      properties: {}
      description: >
        Provides the connector with different settings at request time. The
        key/value pairs of this object are specific to each connector.


        For example, the connector `web-search` supports the `site` option,
        which limits search results to the specified domain.
      title: ChatConnector-7ur0eu
    ChatConnector:
      type: object
      properties:
        id:
          type: string
          description: |
            The identifier of the connector.
        user_access_token:
          type: string
          description: >
            When specified, this user access token will be passed to the
            connector in the Authorization header instead of the Cohere
            generated one.
        continue_on_failure:
          type: boolean
          description: >
            Defaults to `false`.


            When `true`, the request will continue if this connector returned an
            error.
        options:
          $ref: '#/components/schemas/ChatConnector-7ur0eu'
          description: >
            Provides the connector with different settings at request time. The
            key/value pairs of this object are specific to each connector.


            For example, the connector `web-search` supports the `site` option,
            which limits search results to the specified domain.
      required:
        - id
      description: |
        The connector used for fetching documents.
      title: ChatConnector
    ChatDocument:
      type: object
      additionalProperties:
        type: string
      description: >
        Relevant information that could be used by the model to generate a more
        accurate reply.

        The contents of each document are generally short (under 300 words), and
        are passed in the form of a

        dictionary of strings. Some suggested keys are "text", "author", "date".
        Both the key name and the value will be

        passed to the model.
      title: ChatDocument
    V1ChatPostRequestBodyContentApplicationJsonSchemaCitationQuality:
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


        Compatible Deployments: Cohere Platform, Azure, AWS Sagemaker/Bedrock,
        Private Deployments
      title: V1ChatPostRequestBodyContentApplicationJsonSchemaCitationQuality
    ToolParameterDefinitions:
      type: object
      properties:
        description:
          type: string
          description: |
            The description of the parameter.
        type:
          type: string
          description: |
            The type of the parameter. Must be a valid Python type.
        required:
          type: boolean
          default: false
          description: >
            Denotes whether the parameter is always present (required) or not.
            Defaults to not required.
      required:
        - type
      title: ToolParameterDefinitions
    Tool:
      type: object
      properties:
        name:
          type: string
          description: >
            The name of the tool to be called. Valid names contain only the
            characters `a-z`, `A-Z`, `0-9`, `_` and must not begin with a digit.
        description:
          type: string
          description: >
            The description of what the tool does, the model uses the
            description to choose when and how to call the function.
        parameter_definitions:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/ToolParameterDefinitions'
          description: >
            The input parameters of the tool. Accepts a dictionary where the key
            is the name of the parameter and the value is the parameter spec.
            Valid parameter names contain only the characters `a-z`, `A-Z`,
            `0-9`, `_` and must not begin with a digit.

            ```

            {
              "my_param": {
                "description": <string>,
                "type": <string>, // any python data type, such as 'str', 'bool'
                "required": <boolean>
              }
            }

            ```
      required:
        - name
        - description
      title: Tool
    JSONResponseFormat-g7xopi:
      type: object
      properties: {}
      description: >
        A JSON schema object that the output will adhere to. There are some
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


        **Note**: This field must not be specified when the `type` is set to
        `"text"`.
      title: JSONResponseFormat-g7xopi
    ResponseFormat:
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
            schema:
              $ref: '#/components/schemas/JSONResponseFormat-g7xopi'
              description: >
                A JSON schema object that the output will adhere to. There are
                some restrictions we have on the schema, refer to [our
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
        format. Supported on [Command R
        03-2024](https://docs.cohere.com/docs/command-r), [Command R+
        04-2024](https://docs.cohere.com/docs/command-r-plus) and newer models.


        The model can be forced into outputting JSON objects (with up to 5
        levels of nesting) by setting `{ "type": "json_object" }`.


        A [JSON Schema](https://json-schema.org/) can optionally be provided, to
        ensure a specific structure.


        **Note**: When using  `{ "type": "json_object" }` your `message` should
        always explicitly instruct the model to generate a JSON (eg: _"Generate
        a JSON ..."_) . Otherwise the model may end up getting stuck generating
        an infinite stream of characters and eventually run out of context
        length.

        **Limitation**: The parameter is not supported in RAG mode (when any of
        `connectors`, `documents`, `tools`, `tool_results` are provided).
      title: ResponseFormat
    V1ChatPostRequestBodyContentApplicationJsonSchemaSafetyMode:
      type: string
      enum:
        - CONTEXTUAL
        - STRICT
        - NONE
      description: >
        Used to select the [safety
        instruction](https://docs.cohere.com/docs/safety-modes) inserted into
        the prompt. Defaults to `CONTEXTUAL`.

        When `NONE` is specified, the safety instruction will be omitted.


        Safety modes are not yet configurable in combination with `tools`,
        `tool_results` and `documents` parameters.


        **Note**: This parameter is only compatible newer Cohere models,
        starting with [Command R
        08-2024](https://docs.cohere.com/docs/command-r#august-2024-release) and
        [Command R+
        08-2024](https://docs.cohere.com/docs/command-r-plus#august-2024-release).


        **Note**: `command-r7b-12-2024` and newer models only support
        `"CONTEXTUAL"` and `"STRICT"` modes.


        Compatible Deployments: Cohere Platform, Azure, AWS Sagemaker/Bedrock,
        Private Deployments
      title: V1ChatPostRequestBodyContentApplicationJsonSchemaSafetyMode
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
    ChatSearchQuery:
      type: object
      properties:
        text:
          type: string
          description: |
            The text of the search query.
        generation_id:
          type: string
          format: uuid
          description: >
            Unique identifier for the generated search query. Useful for
            submitting feedback.
      required:
        - text
        - generation_id
      description: >
        The generated search query. Contains the text of the query and a unique
        identifier for the query.
      title: ChatSearchQuery
    ChatSearchResultConnector:
      type: object
      properties:
        id:
          type: string
          description: |
            The identifier of the connector.
      required:
        - id
      description: |
        The connector used for fetching documents.
      title: ChatSearchResultConnector
    ChatSearchResult:
      type: object
      properties:
        search_query:
          $ref: '#/components/schemas/ChatSearchQuery'
        connector:
          $ref: '#/components/schemas/ChatSearchResultConnector'
          description: |
            The connector from which this result comes from.
        document_ids:
          type: array
          items:
            type: string
          description: |
            Identifiers of documents found by this search query.
        error_message:
          type: string
          description: |
            An error message if the search failed.
        continue_on_failure:
          type: boolean
          description: >
            Whether a chat request should continue or not if the request to this
            connector fails.
      required:
        - connector
        - document_ids
      title: ChatSearchResult
    ChatCitationType:
      type: string
      enum:
        - TEXT_CONTENT
        - PLAN
      description: >
        The type of citation which indicates what part of the response the
        citation is for.
      title: ChatCitationType
    ChatCitation:
      type: object
      properties:
        start:
          type: integer
          description: >
            The index of text that the citation starts at, counting from zero.
            For example, a generation of `Hello, world!` with a citation on
            `world` would have a start value of `7`. This is because the
            citation starts at `w`, which is the seventh character.
        end:
          type: integer
          description: >
            The index of text that the citation ends after, counting from zero.
            For example, a generation of `Hello, world!` with a citation on
            `world` would have an end value of `11`. This is because the
            citation ends after `d`, which is the eleventh character.
        text:
          type: string
          description: >
            The text of the citation. For example, a generation of `Hello,
            world!` with a citation of `world` would have a text value of
            `world`.
        document_ids:
          type: array
          items:
            type: string
          description: >
            Identifiers of documents cited by this section of the generated
            reply.
        type:
          $ref: '#/components/schemas/ChatCitationType'
          description: >
            The type of citation which indicates what part of the response the
            citation is for.
      required:
        - start
        - end
        - text
        - document_ids
      description: |
        A section of the generated reply which cites external knowledge.
      title: ChatCitation
    ChatStreamEndEventFinishReason:
      type: string
      enum:
        - COMPLETE
        - ERROR_LIMIT
        - MAX_TOKENS
        - ERROR
        - ERROR_TOXIC
      description: >
        - `COMPLETE` - the model sent back a finished reply

        - `ERROR_LIMIT` - the reply was cut off because the model reached the
        maximum number of tokens for its context length

        - `MAX_TOKENS` - the reply was cut off because the model reached the
        maximum number of tokens specified by the max_tokens parameter

        - `ERROR` - something went wrong when generating the reply

        - `ERROR_TOXIC` - the model generated a reply that was deemed toxic
      title: ChatStreamEndEventFinishReason
    FinishReason:
      type: string
      enum:
        - COMPLETE
        - STOP_SEQUENCE
        - ERROR
        - ERROR_TOXIC
        - ERROR_LIMIT
        - USER_CANCEL
        - MAX_TOKENS
        - TIMEOUT
      title: FinishReason
    ApiMetaApiVersion:
      type: object
      properties:
        version:
          type: string
        is_deprecated:
          type: boolean
        is_experimental:
          type: boolean
      required:
        - version
      title: ApiMetaApiVersion
    ApiMetaBilledUnits:
      type: object
      properties:
        images:
          type: number
          format: double
          description: |
            The number of billed images.
        input_tokens:
          type: number
          format: double
          description: |
            The number of billed input tokens.
        image_tokens:
          type: number
          format: double
          description: |
            The number of billed image tokens.
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
      title: ApiMetaBilledUnits
    ApiMetaTokens:
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
      title: ApiMetaTokens
    ApiMeta:
      type: object
      properties:
        api_version:
          $ref: '#/components/schemas/ApiMetaApiVersion'
        billed_units:
          $ref: '#/components/schemas/ApiMetaBilledUnits'
        tokens:
          $ref: '#/components/schemas/ApiMetaTokens'
        cached_tokens:
          type: number
          format: double
          description: |
            The number of prompt tokens that hit the inference cache.
        warnings:
          type: array
          items:
            type: string
      title: ApiMeta
    NonStreamedChatResponse:
      type: object
      properties:
        text:
          type: string
          description: Contents of the reply generated by the model.
        generation_id:
          type: string
          format: uuid
          description: >-
            Unique identifier for the generated reply. Useful for submitting
            feedback.
        response_id:
          type: string
          format: uuid
          description: Unique identifier for the response.
        citations:
          type: array
          items:
            $ref: '#/components/schemas/ChatCitation'
          description: Inline citations for the generated reply.
        documents:
          type: array
          items:
            $ref: '#/components/schemas/ChatDocument'
          description: Documents seen by the model when generating the reply.
        is_search_required:
          type: boolean
          description: Denotes that a search for documents is required during the RAG flow.
        search_queries:
          type: array
          items:
            $ref: '#/components/schemas/ChatSearchQuery'
          description: Generated search queries, meant to be used as part of the RAG flow.
        search_results:
          type: array
          items:
            $ref: '#/components/schemas/ChatSearchResult'
          description: Documents retrieved from each of the conducted searches.
        finish_reason:
          $ref: '#/components/schemas/FinishReason'
        tool_calls:
          type: array
          items:
            $ref: '#/components/schemas/ToolCall'
        chat_history:
          type: array
          items:
            $ref: '#/components/schemas/Message'
          description: >
            A list of previous messages between the user and the model, meant to
            give the model conversational context for responding to the user's
            `message`.
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - text
      title: NonStreamedChatResponse
    ToolCallDelta:
      type: object
      properties:
        name:
          type: string
          description: |
            Name of the tool call
        index:
          type: number
          format: double
          description: |
            Index of the tool call generated
        parameters:
          type: string
          description: |
            Chunk of the tool parameters
        text:
          type: string
          description: |
            Chunk of the tool plan text
      description: |
        Contains the chunk of the tool call generation in the stream.
      title: ToolCallDelta
    chat_Response_stream_streaming:
      oneOf:
        - type: object
          properties:
            event_type:
              $ref: '#/components/schemas/ChatStreamEventEventType'
            generation_id:
              type: string
              format: uuid
              description: >
                Unique identifier for the generated reply. Useful for submitting
                feedback.
          required:
            - event_type
            - generation_id
          description: stream-start variant
        - type: object
          properties:
            event_type:
              $ref: '#/components/schemas/ChatStreamEventEventType'
            search_queries:
              type: array
              items:
                $ref: '#/components/schemas/ChatSearchQuery'
              description: >-
                Generated search queries, meant to be used as part of the RAG
                flow.
          required:
            - event_type
            - search_queries
          description: search-queries-generation variant
        - type: object
          properties:
            event_type:
              $ref: '#/components/schemas/ChatStreamEventEventType'
            search_results:
              type: array
              items:
                $ref: '#/components/schemas/ChatSearchResult'
              description: >
                Conducted searches and the ids of documents retrieved from each
                of them.
            documents:
              type: array
              items:
                $ref: '#/components/schemas/ChatDocument'
              description: |
                Documents fetched from searches or provided by the user.
          required:
            - event_type
          description: search-results variant
        - type: object
          properties:
            event_type:
              $ref: '#/components/schemas/ChatStreamEventEventType'
            text:
              type: string
              description: |
                The next batch of text generated by the model.
          required:
            - event_type
            - text
          description: text-generation variant
        - type: object
          properties:
            event_type:
              $ref: '#/components/schemas/ChatStreamEventEventType'
            citations:
              type: array
              items:
                $ref: '#/components/schemas/ChatCitation'
              description: |
                Citations for the generated reply.
          required:
            - event_type
            - citations
          description: citation-generation variant
        - type: object
          properties:
            event_type:
              $ref: '#/components/schemas/ChatStreamEventEventType'
            text:
              type: string
              description: |
                The text generated related to the tool calls generated
            tool_calls:
              type: array
              items:
                $ref: '#/components/schemas/ToolCall'
          required:
            - event_type
            - tool_calls
          description: tool-calls-generation variant
        - type: object
          properties:
            event_type:
              $ref: '#/components/schemas/ChatStreamEventEventType'
            finish_reason:
              $ref: '#/components/schemas/ChatStreamEndEventFinishReason'
              description: >
                - `COMPLETE` - the model sent back a finished reply

                - `ERROR_LIMIT` - the reply was cut off because the model
                reached the maximum number of tokens for its context length

                - `MAX_TOKENS` - the reply was cut off because the model reached
                the maximum number of tokens specified by the max_tokens
                parameter

                - `ERROR` - something went wrong when generating the reply

                - `ERROR_TOXIC` - the model generated a reply that was deemed
                toxic
            response:
              $ref: '#/components/schemas/NonStreamedChatResponse'
              description: >
                The consolidated response from the model. Contains the generated
                reply and all the other information streamed back in the
                previous events.
          required:
            - event_type
            - finish_reason
            - response
          description: stream-end variant
        - type: object
          properties:
            event_type:
              $ref: '#/components/schemas/ChatStreamEventEventType'
            tool_call_delta:
              $ref: '#/components/schemas/ToolCallDelta'
            text:
              type: string
          required:
            - event_type
            - tool_call_delta
          description: tool-calls-chunk variant
        - type: object
          properties:
            event_type:
              $ref: '#/components/schemas/ChatStreamEventEventType'
            prompt:
              type: string
          required:
            - event_type
          description: debug variant
      discriminator:
        propertyName: event_type
      description: >-
        StreamedChatResponse is returned in streaming mode (specified with
        `stream=True` in the request).
      title: chat_Response_stream_streaming
    ChatRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ChatRequestBadRequestError
    ChatRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ChatRequestUnauthorizedError
    ChatRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ChatRequestForbiddenError
    ChatRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ChatRequestNotFoundError
    ChatRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ChatRequestUnprocessableEntityError
    ChatRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ChatRequestTooManyRequestsError
    ChatRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ChatRequestInvalidTokenError
    ChatRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ChatRequestClientClosedRequestError
    ChatRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ChatRequestInternalServerError
    ChatRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ChatRequestNotImplementedError
    ChatRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ChatRequestServiceUnavailableError
    ChatRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ChatRequestGatewayTimeoutError
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

```

## SDK Code Examples

```go Streaming
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

	resp, err := co.ChatStream(
		context.TODO(),
		&cohere.ChatStreamRequest{
			Model:   cohere.String("command-a-03-2025"),
			Message: "Tell me about LLMs",
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

		if message.TextGeneration != nil {
			log.Printf("%+v", resp)
		}
	}

}

```

```typescript Streaming
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const chatStream = await cohere.chatStream({
    model: 'command-a-03-2025',
    message: 'Tell me about LLMs',
  });

  for await (const message of chatStream) {
    if (message.eventType === 'text-generation') {
      process.stdout.write(message);
    }
  }
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.chatStream({
        message: "hello!",
        stream: true,
        model: "command-a-03-2025",
    });
}
main();

```

```java Streaming
/* (C)2024 */
package chatpost;

import com.cohere.api.Cohere;
import com.cohere.api.requests.ChatStreamRequest;
import com.cohere.api.types.ChatMessage;
import com.cohere.api.types.ChatTextGenerationEvent;
import com.cohere.api.types.Message;
import com.cohere.api.types.StreamedChatResponse;
import java.util.List;

public class Stream {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    Iterable<StreamedChatResponse> response =
        cohere.chatStream(
            ChatStreamRequest.builder()
                .model("command-a-03-2025")
                .message("Tell me about LLMs")
                .build());

    for (StreamedChatResponse chatResponse : response) {
      if (chatResponse.isTextGeneration()) {
        System.out.println(
            chatResponse.getTextGeneration().map(ChatTextGenerationEvent::getText).orElse(""));
      }
    }

    System.out.println(response);
  }
}

```

```python Streaming
import cohere

co = cohere.Client()

response = co.chat_stream(
    model="command-a-03-2025",
    message="Tell me about LLMs",
)

for event in response:
    if event.event_type == "text-generation":
        print(event.text, end="")

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.chat_stream(
    message="hello!",
    model="command-a-03-2025"
)

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/chat")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"message\": \"hello!\",\n  \"stream\": true,\n  \"model\": \"command-a-03-2025\"\n}"

response = http.request(request)
puts response.read_body
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/chat', [
  'body' => '{
  "message": "hello!",
  "stream": true,
  "model": "command-a-03-2025"
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.cohere.com/v1/chat");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"message\": \"hello!\",\n  \"stream\": true,\n  \"model\": \"command-a-03-2025\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "message": "hello!",
  "stream": true,
  "model": "command-a-03-2025"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/chat")! as URL,
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