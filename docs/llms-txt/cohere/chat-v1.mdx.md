# Source: https://docs.cohere.com/reference/chat-v1.mdx

# Chat (V1)

POST https://api.cohere.com/v1/chat
Content-Type: application/json

Generates a text response to a user message.
To learn how to use the Chat API and RAG follow our [Text Generation guides](https://docs.cohere.com/docs/chat-api).


Reference: https://docs.cohere.com/reference/chat-v1

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/chat:
    post:
      operationId: chat
      summary: Chat API (v1)
      description: >
        Generates a text response to a user message.

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
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/chat_Response_stream'
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
                    - false
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
    chat_Response_stream:
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
      title: chat_Response_stream
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

```go Default
package main

import (
	"context"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.Chat(
		context.TODO(),
		&cohere.ChatRequest{
			Model:   cohere.String("command-a-03-2025"),
			Message: "Tell me about LLMs",
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```typescript Default
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const response = await cohere.chat({
    model: 'command-a-03-2025',
    message: 'Tell me about LLMs',
  });

  console.log(response);
})();

```

```typescript Default
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.chatStream({
        message: "Tell me about LLMs",
        stream: false,
        model: "command-a-03-2025",
    });
}
main();

```

```java Default
/* (C)2024 */
package chatpost;

import com.cohere.api.Cohere;
import com.cohere.api.requests.ChatRequest;
import com.cohere.api.types.ChatMessage;
import com.cohere.api.types.Message;
import com.cohere.api.types.NonStreamedChatResponse;
import java.util.List;

public class Default {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    NonStreamedChatResponse response =
        cohere.chat(
            ChatRequest.builder()
                .model("command-a-03-2025")
                .message("Tell me about LLMs")
                .build());

    System.out.println(response);
  }
}

```

```python Sync
import cohere

co = cohere.Client()

response = co.chat(
    model="command-a-03-2025",
    message="Tell me about LLMs",
)

print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    return await co.chat(
        model="command-a-03-2025",
        message="Tell me about LLMs"
    )


asyncio.run(main())

```

```python Default
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.chat_stream(
    message="Tell me about LLMs",
    model="command-a-03-2025"
)

```

```ruby Default
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/chat")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"message\": \"Tell me about LLMs\",\n  \"stream\": false,\n  \"model\": \"command-a-03-2025\"\n}"

response = http.request(request)
puts response.read_body
```

```php Default
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/chat', [
  'body' => '{
  "message": "Tell me about LLMs",
  "stream": false,
  "model": "command-a-03-2025"
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

var client = new RestClient("https://api.cohere.com/v1/chat");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"message\": \"Tell me about LLMs\",\n  \"stream\": false,\n  \"model\": \"command-a-03-2025\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Default
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "message": "Tell me about LLMs",
  "stream": false,
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

```typescript Documents
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const response = await cohere.chat({
    model: 'command-a-03-2025',
    message: 'Who is more popular: Nsync or Backstreet Boys?',
    documents: [
      {
        title: 'CSPC: Backstreet Boys Popularity Analysis - ChartMasters',
        snippet:
          '↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: Backstreet Boys Popularity Analysis\n\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\n\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\n\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.',
      },
      {
        title: 'CSPC: NSYNC Popularity Analysis - ChartMasters',
        snippet:
          "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.",
      },
      {
        title: 'CSPC: Backstreet Boys Popularity Analysis - ChartMasters',
        snippet:
          ' 1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\n\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\n\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.',
      },
      {
        title: 'CSPC: NSYNC Popularity Analysis - ChartMasters',
        snippet:
          ' Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\n\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.',
      },
    ],
  });

  console.log(response);
})();

```

```typescript Documents
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.chatStream({
        message: "Who is more popular: Nsync or Backstreet Boys?",
        stream: false,
        model: "command-a-03-2025",
        documents: [
            {
                "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
                "snippet": `↓ Skip to Main Content

Music industry – One step closer to being accurate

CSPC: Backstreet Boys Popularity Analysis

Hernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band

At one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.

It is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.`,
            },
            {
                "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
                "snippet": `↓ Skip to Main Content

Music industry – One step closer to being accurate

CSPC: NSYNC Popularity Analysis

MJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync

At the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.

It wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.`,
            },
            {
                "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
                "snippet": `1997, 1998, 2000 and 2001 also rank amongst some of the very best years.
Yet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.

We will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.`,
            },
            {
                "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
                "snippet": `Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?
As usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.`,
            },
        ],
    });
}
main();

```

```java Documents
/* (C)2024 */
package chatpost;

import com.cohere.api.Cohere;
import com.cohere.api.requests.ChatRequest;
import com.cohere.api.types.NonStreamedChatResponse;
import java.util.List;
import java.util.Map;

public class Documents {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    NonStreamedChatResponse response =
        cohere.chat(
            ChatRequest.builder()
                .model("command-a-03-2025")
                .message("What year was he born?")
                .documents(
                    List.of(
                        Map.of(
                            "title",
                                "CSPC: Backstreet Boys Popularity" + " Analysis - ChartMasters",
                            "snippet",
                                "↓ Skip to Main Content\n\n"
                                    + "Music industry – One step"
                                    + " closer to being"
                                    + " accurate\n\n"
                                    + "CSPC: Backstreet Boys"
                                    + " Popularity Analysis\n\n"
                                    + "Hernán Lopez Posted on"
                                    + " February 9, 2017 Posted in"
                                    + " CSPC 72 Comments Tagged"
                                    + " with Backstreet Boys, Boy"
                                    + " band\n\n"
                                    + "At one point, Backstreet"
                                    + " Boys defined success:"
                                    + " massive albums sales across"
                                    + " the globe, great singles"
                                    + " sales, plenty of chart"
                                    + " topping releases, hugely"
                                    + " hyped tours and tremendous"
                                    + " media coverage.\n\n"
                                    + "It is true that they"
                                    + " benefited from"
                                    + " extraordinarily good market"
                                    + " conditions in all markets."
                                    + " After all, the all-time"
                                    + " record year for the music"
                                    + " business, as far as"
                                    + " revenues in billion dollars"
                                    + " are concerned, was actually"
                                    + " 1999. That is, back when"
                                    + " this five men group was at"
                                    + " its peak."),
                        Map.of(
                            "title", "CSPC: NSYNC Popularity Analysis -" + " ChartMasters",
                            "snippet",
                                "↓ Skip to Main Content\n\n"
                                    + "Music industry – One step"
                                    + " closer to being"
                                    + " accurate\n\n"
                                    + "CSPC: NSYNC Popularity"
                                    + " Analysis\n\n"
                                    + "MJD Posted on February 9,"
                                    + " 2018 Posted in CSPC 27"
                                    + " Comments Tagged with Boy"
                                    + " band, N'Sync\n\n"
                                    + "At the turn of the"
                                    + " millennium three teen acts"
                                    + " were huge in the US, the"
                                    + " Backstreet Boys, Britney"
                                    + " Spears and NSYNC. The"
                                    + " latter is the only one we"
                                    + " haven’t study so far. It"
                                    + " took 15 years and Adele to"
                                    + " break their record of 2,4"
                                    + " million units sold of No"
                                    + " Strings Attached in its"
                                    + " first week alone.\n\n"
                                    + "It wasn’t a fluke, as the"
                                    + " second fastest selling"
                                    + " album of the Soundscan era"
                                    + " prior 2015, was also theirs"
                                    + " since Celebrity debuted"
                                    + " with 1,88 million units"
                                    + " sold."),
                        Map.of(
                            "title",
                                "CSPC: Backstreet Boys Popularity" + " Analysis - ChartMasters",
                            "snippet",
                                " 1997, 1998, 2000 and 2001 also"
                                    + " rank amongst some of the"
                                    + " very best years.\n\n"
                                    + "Yet the way many music"
                                    + " consumers – especially"
                                    + " teenagers and young women’s"
                                    + " – embraced their output"
                                    + " deserves its own chapter."
                                    + " If Jonas Brothers and more"
                                    + " recently One Direction"
                                    + " reached a great level of"
                                    + " popularity during the past"
                                    + " decade, the type of success"
                                    + " achieved by Backstreet Boys"
                                    + " is in a completely"
                                    + " different level as they"
                                    + " really dominated the"
                                    + " business for a few years"
                                    + " all over the world,"
                                    + " including in some countries"
                                    + " that were traditionally"
                                    + " hard to penetrate for"
                                    + " Western artists.\n\n"
                                    + "We will try to analyze the"
                                    + " extent of that hegemony"
                                    + " with this new article with"
                                    + " final results which will"
                                    + " more than surprise many"
                                    + " readers."),
                        Map.of(
                            "title",
                            "CSPC: NSYNC Popularity Analysis -" + " ChartMasters",
                            "snippet",
                            " Was the teen group led by Justin"
                                + " Timberlake really that big? Was it"
                                + " only in the US where they found"
                                + " success? Or were they a global"
                                + " phenomenon?\n\n"
                                + "As usual, I’ll be using the"
                                + " Commensurate Sales to Popularity"
                                + " Concept in order to relevantly"
                                + " gauge their results. This concept"
                                + " will not only bring you sales"
                                + " information for all NSYNC‘s albums,"
                                + " physical and download singles, as"
                                + " well as audio and video streaming,"
                                + " but it will also determine their"
                                + " true popularity. If you are not yet"
                                + " familiar with the CSPC method, the"
                                + " next page explains it with a short"
                                + " video. I fully recommend watching"
                                + " the video before getting into the"
                                + " sales figures.")))
                .build());

    System.out.println(response);
  }
}

```

```python Documents
import cohere

co = cohere.Client()

response = co.chat(
    model="command-a-03-2025",
    message="Who is more popular: Nsync or Backstreet Boys?",
    documents=[
        {
            "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
            "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: Backstreet Boys Popularity Analysis\n\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\n\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\n\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.",
        },
        {
            "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
            "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.",
        },
        {
            "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
            "snippet": " 1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\n\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\n\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.",
        },
        {
            "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
            "snippet": " Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\n\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.",
        },
    ],
)

print(response)

```

```python Documents
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.chat_stream(
    message="Who is more popular: Nsync or Backstreet Boys?",
    model="command-a-03-2025",
    documents=[
        {
            "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
            "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: Backstreet Boys Popularity Analysis\n\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\n\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\n\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak."
        },
        {
            "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
            "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N\'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold."
        },
        {
            "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
            "snippet": "1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\n\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers."
        },
        {
            "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
            "snippet": "Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures."
        }
    ]
)

```

```ruby Documents
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/chat")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"message\": \"Who is more popular: Nsync or Backstreet Boys?\",\n  \"stream\": false,\n  \"model\": \"command-a-03-2025\",\n  \"documents\": [\n    {\n      \"title\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n      \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: Backstreet Boys Popularity Analysis\\n\\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\\n\\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\\n\\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.\"\n    },\n    {\n      \"title\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n      \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: NSYNC Popularity Analysis\\n\\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\\n\\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\\n\\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.\"\n    },\n    {\n      \"title\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n      \"snippet\": \"1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\\n\\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.\"\n    },\n    {\n      \"title\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n      \"snippet\": \"Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Documents
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/chat', [
  'body' => '{
  "message": "Who is more popular: Nsync or Backstreet Boys?",
  "stream": false,
  "model": "command-a-03-2025",
  "documents": [
    {
      "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
      "snippet": "↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: Backstreet Boys Popularity Analysis\\n\\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\\n\\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\\n\\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak."
    },
    {
      "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
      "snippet": "↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: NSYNC Popularity Analysis\\n\\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N\'Sync\\n\\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\\n\\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold."
    },
    {
      "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
      "snippet": "1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\\n\\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers."
    },
    {
      "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
      "snippet": "Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures."
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

var client = new RestClient("https://api.cohere.com/v1/chat");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"message\": \"Who is more popular: Nsync or Backstreet Boys?\",\n  \"stream\": false,\n  \"model\": \"command-a-03-2025\",\n  \"documents\": [\n    {\n      \"title\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n      \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: Backstreet Boys Popularity Analysis\\n\\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\\n\\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\\n\\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.\"\n    },\n    {\n      \"title\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n      \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: NSYNC Popularity Analysis\\n\\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\\n\\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\\n\\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.\"\n    },\n    {\n      \"title\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n      \"snippet\": \"1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\\n\\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.\"\n    },\n    {\n      \"title\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n      \"snippet\": \"Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Documents
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "message": "Who is more popular: Nsync or Backstreet Boys?",
  "stream": false,
  "model": "command-a-03-2025",
  "documents": [
    [
      "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
      "snippet": "↓ Skip to Main Content

Music industry – One step closer to being accurate

CSPC: Backstreet Boys Popularity Analysis

Hernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band

At one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.

It is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak."
    ],
    [
      "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
      "snippet": "↓ Skip to Main Content

Music industry – One step closer to being accurate

CSPC: NSYNC Popularity Analysis

MJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync

At the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.

It wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold."
    ],
    [
      "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
      "snippet": "1997, 1998, 2000 and 2001 also rank amongst some of the very best years.
Yet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.

We will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers."
    ],
    [
      "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
      "snippet": "Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?
As usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures."
    ]
  ]
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

```go Tools
package main

import (
	"context"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.Chat(
		context.TODO(),
		&cohere.ChatRequest{
			Model:   cohere.String("command-a-03-2025"),
			Message: "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?",
			Tools: []*cohere.Tool{
				{
					Name:        "query_daily_sales_report",
					Description: "Connects to a database to retrieve overall sales volumes and sales information for a given day.",
					ParameterDefinitions: map[string]*cohere.ToolParameterDefinitionsValue{
						"day": {
							Description: cohere.String("Retrieves sales data for this day, formatted as YYYY-MM-DD."),
							Type:        "str",
							Required:    cohere.Bool(true),
						},
					},
				},
				{
					Name:        "query_product_catalog",
					Description: "Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels.",
					ParameterDefinitions: map[string]*cohere.ToolParameterDefinitionsValue{
						"category": {
							Description: cohere.String("Retrieves product information data for all products in this category."),
							Type:        "str",
							Required:    cohere.Bool(true),
						},
					},
				},
			},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```typescript Tools
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const response = await cohere.chat({
    model: 'command-a-03-2025',
    message:
      "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?",
    tools: [
      {
        name: 'query_daily_sales_report',
        description:
          'Connects to a database to retrieve overall sales volumes and sales information for a given day.',
        parameterDefinitions: {
          day: {
            description: 'Retrieves sales data for this day, formatted as YYYY-MM-DD.',
            type: 'str',
            required: true,
          },
        },
      },
      {
        name: 'query_product_catalog',
        description:
          'Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels.',
        parameterDefinitions: {
          category: {
            description: 'Retrieves product information data for all products in this category.',
            type: 'str',
            required: true,
          },
        },
      },
    ],
  });

  console.log(response);
})();

```

```typescript Tools
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.chatStream({
        message: "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?",
        stream: false,
        model: "command-a-03-2025",
        tools: [
            {
                name: "query_daily_sales_report",
                description: "Connects to a database to retrieve overall sales volumes and sales information for a given day.",
                parameterDefinitions: {
                    "day": {
                        type: "str",
                        description: "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
                        required: true,
                    },
                },
            },
            {
                name: "query_product_catalog",
                description: "Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels.",
                parameterDefinitions: {
                    "category": {
                        type: "str",
                        description: "Retrieves product information data for all products in this category.",
                        required: true,
                    },
                },
            },
        ],
    });
}
main();

```

```java Tools
/* (C)2024 */
package chatpost;

import com.cohere.api.Cohere;
import com.cohere.api.requests.ChatRequest;
import com.cohere.api.types.NonStreamedChatResponse;
import com.cohere.api.types.Tool;
import com.cohere.api.types.ToolParameterDefinitionsValue;
import java.util.List;
import java.util.Map;

public class Tools {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    NonStreamedChatResponse response =
        cohere.chat(
            ChatRequest.builder()
                .model("command-a-03-2025")
                .message(
                    "Can you provide a sales summary for 29th September 2023,"
                        + " and also give me some details about the products in"
                        + " the 'Electronics' category, for example their"
                        + " prices and stock levels?")
                .tools(
                    List.of(
                        Tool.builder()
                            .name("query_daily_sales_report")
                            .description(
                                "Connects to a database to retrieve"
                                    + " overall sales volumes and"
                                    + " sales information for a"
                                    + " given day.")
                            .parameterDefinitions(
                                Map.of(
                                    "day",
                                    ToolParameterDefinitionsValue.builder()
                                        .type("str")
                                        .description(
                                            "Retrieves"
                                                + " sales"
                                                + " data"
                                                + " for this"
                                                + " day,"
                                                + " formatted"
                                                + " as YYYY-MM-DD.")
                                        .required(true)
                                        .build()))
                            .build(),
                        Tool.builder()
                            .name("query_product_catalog")
                            .description(
                                "Connects to a a product catalog"
                                    + " with information about all"
                                    + " the products being sold,"
                                    + " including categories,"
                                    + " prices, and stock levels.")
                            .parameterDefinitions(
                                Map.of(
                                    "category",
                                    ToolParameterDefinitionsValue.builder()
                                        .type("str")
                                        .description(
                                            "Retrieves"
                                                + " product"
                                                + " information"
                                                + " data"
                                                + " for all"
                                                + " products"
                                                + " in this"
                                                + " category.")
                                        .required(true)
                                        .build()))
                            .build()))
                .build());

    System.out.println(response);
  }
}

```

```python Tools
import cohere

co = cohere.Client()

# tool descriptions that the model has access to
tools = [
    {
        "name": "query_daily_sales_report",
        "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day.",
        "parameter_definitions": {
            "day": {
                "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
                "type": "str",
                "required": True,
            }
        },
    },
    {
        "name": "query_product_catalog",
        "description": "Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels.",
        "parameter_definitions": {
            "category": {
                "description": "Retrieves product information data for all products in this category.",
                "type": "str",
                "required": True,
            }
        },
    },
]


# user request
message = "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?"

response = co.chat(
    model="command-a-03-2025",
    message=message,
    tools=tools,
)

print(response)

```

```python Tools
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.chat_stream(
    message="Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the \'Electronics\' category, for example their prices and stock levels?",
    model="command-a-03-2025",
    tools=[
        {
            "name": "query_daily_sales_report",
            "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day.",
            "parameter_definitions": {
                "day": {
                    "type": "str",
                    "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
                    "required": True
                }
            }
        },
        {
            "name": "query_product_catalog",
            "description": "Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels.",
            "parameter_definitions": {
                "category": {
                    "type": "str",
                    "description": "Retrieves product information data for all products in this category.",
                    "required": True
                }
            }
        }
    ]
)

```

```ruby Tools
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/chat")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"message\": \"Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?\",\n  \"stream\": false,\n  \"model\": \"command-a-03-2025\",\n  \"tools\": [\n    {\n      \"name\": \"query_daily_sales_report\",\n      \"description\": \"Connects to a database to retrieve overall sales volumes and sales information for a given day.\",\n      \"parameter_definitions\": {\n        \"day\": {\n          \"type\": \"str\",\n          \"description\": \"Retrieves sales data for this day, formatted as YYYY-MM-DD.\",\n          \"required\": true\n        }\n      }\n    },\n    {\n      \"name\": \"query_product_catalog\",\n      \"description\": \"Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels.\",\n      \"parameter_definitions\": {\n        \"category\": {\n          \"type\": \"str\",\n          \"description\": \"Retrieves product information data for all products in this category.\",\n          \"required\": true\n        }\n      }\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Tools
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/chat', [
  'body' => '{
  "message": "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the \'Electronics\' category, for example their prices and stock levels?",
  "stream": false,
  "model": "command-a-03-2025",
  "tools": [
    {
      "name": "query_daily_sales_report",
      "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day.",
      "parameter_definitions": {
        "day": {
          "type": "str",
          "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
          "required": true
        }
      }
    },
    {
      "name": "query_product_catalog",
      "description": "Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels.",
      "parameter_definitions": {
        "category": {
          "type": "str",
          "description": "Retrieves product information data for all products in this category.",
          "required": true
        }
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

var client = new RestClient("https://api.cohere.com/v1/chat");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"message\": \"Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?\",\n  \"stream\": false,\n  \"model\": \"command-a-03-2025\",\n  \"tools\": [\n    {\n      \"name\": \"query_daily_sales_report\",\n      \"description\": \"Connects to a database to retrieve overall sales volumes and sales information for a given day.\",\n      \"parameter_definitions\": {\n        \"day\": {\n          \"type\": \"str\",\n          \"description\": \"Retrieves sales data for this day, formatted as YYYY-MM-DD.\",\n          \"required\": true\n        }\n      }\n    },\n    {\n      \"name\": \"query_product_catalog\",\n      \"description\": \"Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels.\",\n      \"parameter_definitions\": {\n        \"category\": {\n          \"type\": \"str\",\n          \"description\": \"Retrieves product information data for all products in this category.\",\n          \"required\": true\n        }\n      }\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Tools
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "message": "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?",
  "stream": false,
  "model": "command-a-03-2025",
  "tools": [
    [
      "name": "query_daily_sales_report",
      "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day.",
      "parameter_definitions": ["day": [
          "type": "str",
          "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
          "required": true
        ]]
    ],
    [
      "name": "query_product_catalog",
      "description": "Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels.",
      "parameter_definitions": ["category": [
          "type": "str",
          "description": "Retrieves product information data for all products in this category.",
          "required": true
        ]]
    ]
  ]
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