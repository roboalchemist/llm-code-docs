# Source: https://docs.fireworks.ai/api-reference/post-chatcompletions.md

# Create Chat Completion

> Creates a model response for the given chat conversation.

## OpenAPI

````yaml post /chat/completions
paths:
  path: /chat/completions
  method: post
  servers:
    - url: https://api.fireworks.ai/inference/v1/
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
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
                  - description: The name of the model to use.
                    type: string
                    example: accounts/fireworks/models/llama-v3p1-8b-instruct
              messages:
                allOf:
                  - description: A list of messages comprising the conversation so far.
                    type: array
                    minItems: 1
                    items:
                      $ref: '#/components/schemas/ChatCompletionRequestMessage'
              tool_choice:
                allOf:
                  - description: >
                      Controls which (if any) tool is called by the model.


                      - `none`: the model will not call any tool and instead
                      generates a message.

                      - `auto`: the model can pick between generating a message
                      or calling one or more tools.

                      - `required` (alias: `any`): the model must call one or
                      more tools. To force a specific function, pass an object
                      of the form `{ "type": "function", "name": "my_function"
                      }` or `{ "type": "function", "function": { "name":
                      "my_function" }` for OpenAI compatibility.
                    oneOf:
                      - $ref: '#/components/schemas/ToolChoiceOptions'
                      - $ref: '#/components/schemas/ToolChoiceFunction'
              tools:
                allOf:
                  - type: array
                    description: >
                      A list of tools the model may call. Currently, only
                      functions are supported as a tool.

                      Use this to provide a list of functions the model may
                      generate JSON inputs for.

                      See the guide for more information and the list of
                      supported models:
                      https://docs.fireworks.ai/guides/function-calling#supported-models
                    items:
                      $ref: '#/components/schemas/ChatCompletionTool'
              max_tokens:
                allOf:
                  - description: >
                      The maximum number of tokens to generate in the
                      completion.


                      If the token count of your prompt (previous messages) plus
                      `max_tokens` exceed the model's context length, the
                      behavior is depends on `context_length_exceeded_behavior`.
                      By default, `max_tokens` will be lowered to fit in the
                      context window instead of returning an error.
                    default: 2000
                    type: integer
              prompt_truncate_len:
                allOf:
                  - description: >
                      The size (in tokens) to which to truncate chat prompts.
                      This includes the system prompt (if any), previous
                      user/assistant messages, and the current user message.
                      Earlier user/assistant messages will be evicted first to
                      fit the prompt into this length. The system prompt is
                      preserved whenever possible and only truncated as a last
                      resort.


                      This should usually be set to a number much smaller <<
                      than the model's maximum context size, to allow enough
                      remaining tokens for generating a response.


                      If omitted, you may receive "prompt too long" errors in
                      your responses as conversations grow. Note that even with
                      this set, you may still receive "prompt too long" errors
                      if individual messages (such as a very long system prompt
                      or user message) exceed the model's context window on
                      their own.
                    default: 1500
                    nullable: true
                    type: integer
              temperature:
                allOf:
                  - type: number
                    minimum: 0
                    maximum: 2
                    default: 1
                    example: 1
                    nullable: true
                    description: >
                      What sampling temperature to use, between 0 and 2. Higher
                      values like 0.8 will make the output more random, while
                      lower values like 0.2 will make it more focused and
                      deterministic.


                      We generally recommend altering this or `top_p` but not
                      both.
              top_p:
                allOf:
                  - type: number
                    minimum: 0
                    maximum: 1
                    default: 1
                    example: 1
                    nullable: true
                    description: >
                      An alternative to sampling with temperature, called
                      nucleus sampling, where the model considers the results of
                      the tokens with top_p probability mass. So 0.1 means only
                      the tokens comprising the top 10% probability mass are
                      considered.


                      We generally recommend altering this or `temperature` but
                      not both.
              top_k:
                allOf:
                  - type: integer
                    minimum: 0
                    maximum: 100
                    example: 50
                    nullable: true
                    description: >
                      Top-k sampling is another sampling method where the k most
                      probable next tokens are filtered and the probability mass
                      is redistributed among only those k next tokens. The value
                      of k controls the number of candidates for the next token
                      at each step during text generation. Must be between 0 and
                      100.
              frequency_penalty:
                allOf:
                  - type: number
                    default: 0
                    minimum: -2
                    maximum: 2
                    nullable: true
                    description: >
                      Number between -2.0 and 2.0. Positive values penalize new
                      tokens based on their existing frequency in the text so
                      far, decreasing the model's likelihood to repeat the same
                      line verbatim.


                      Reasonable value is around 0.1 to 1 if the aim is to just
                      reduce repetitive samples somewhat. If the aim is to
                      strongly suppress repetition, then one can increase the
                      coefficients up to 2, but this can noticeably degrade the
                      quality of samples. Negative values can be used to
                      increase the likelihood of repetition.


                      See also `presence_penalty` for penalizing tokens that
                      have at least one appearance at a fixed rate.


                      OpenAI compatible (follows OpenAI's conventions for
                      handling token frequency and repetition penalties).
              perf_metrics_in_response:
                allOf:
                  - type: boolean
                    default: false
                    nullable: true
                    description: >
                      Whether to include performance metrics in the response
                      body.


                      **Non-streaming requests:** Performance metrics are always
                      included in response headers (e.g.,
                      `fireworks-prompt-tokens`,
                      `fireworks-server-time-to-first-token`). Setting this to
                      `true` additionally includes the same metrics in the
                      response body under the `perf_metrics` field.


                      **Streaming requests:** Performance metrics are only
                      included in the response body under the `perf_metrics`
                      field in the final chunk (when `finish_reason` is set).
                      This is because headers may not be accessible during
                      streaming.


                      The response body `perf_metrics` field contains the
                      following metrics:


                      **Basic Metrics (all deployments):**

                      - `prompt-tokens`: Number of tokens in the prompt

                      - `server-time-to-first-token`: Time from request start to
                      first token (in seconds)

                      - `server-processing-time`: Total processing time (in
                      seconds, only for completed requests)


                      **Predicted Outputs Metrics:**

                      - `speculation-prompt-tokens`: Number of speculative
                      prompt tokens

                      - `speculation-prompt-matched-tokens`: Number of matched
                      speculative prompt tokens (for completed requests)


                      **Dedicated Deployment Only Metrics:**

                      - `speculation-generated-tokens`: Number of speculative
                      generated tokens (for completed requests)

                      - `speculation-acceptance`: Speculation acceptance rates
                      by position

                      - `cached-prompt-tokens`: Number of cached prompt tokens

                      - `backend-host`: Hostname of the backend server

                      - `num-concurrent-requests`: Number of concurrent requests

                      - `deployment`: Deployment name

                      - `tokenizer-queue-duration`: Time spent in tokenizer
                      queue

                      - `tokenizer-duration`: Time spent in tokenizer

                      - `prefill-queue-duration`: Time spent in prefill queue

                      - `prefill-duration`: Time spent in prefill

                      - `generation-queue-duration`: Time spent in generation
                      queue
              presence_penalty:
                allOf:
                  - type: number
                    default: 0
                    minimum: -2
                    maximum: 2
                    nullable: true
                    description: >
                      Number between -2.0 and 2.0. Positive values penalize new
                      tokens based on whether they appear in the text so far,
                      increasing the model's likelihood to talk about new
                      topics.


                      Reasonable value is around 0.1 to 1 if the aim is to just
                      reduce repetitive samples somewhat. If the aim is to
                      strongly suppress repetition, then one can increase the
                      coefficients up to 2, but this can noticeably degrade the
                      quality of samples. Negative values can be used to
                      increase the likelihood of repetition.


                      See also `frequence_penalty` for penalizing tokens at an
                      increasing rate depending on how often they appear.


                      OpenAI compatible (follows OpenAI's conventions for
                      handling token frequency and repetition penalties).
              repetition_penalty:
                allOf:
                  - type: number
                    default: 1
                    minimum: 0
                    maximum: 2
                    nullable: true
                    description: >
                      Applies a penalty to repeated tokens to discourage or
                      encourage repetition. A value of `1.0` means no penalty,
                      allowing free repetition. Values above `1.0` penalize
                      repetition, reducing the likelihood of repeating tokens.
                      Values between `0.0` and `1.0` reward repetition,
                      increasing the chance of repeated tokens. For a good
                      balance, a value of `1.2` is often recommended. Note that
                      the penalty is applied to both the generated output and
                      the prompt in decoder-only models.
              reasoning_effort:
                allOf:
                  - oneOf:
                      - type: string
                        enum:
                          - none
                          - low
                          - medium
                          - high
                      - type: integer
                    nullable: true
                    description: >
                      Applicable to reasoning models only, this option controls
                      the reasoning token length, and can be set to either
                      'none', 'low', 'medium', 'high' or an integer. 'low',
                      'medium' and 'high' correspond to progressively higher
                      thinking effort and thus longer reasoning tokens. 'none'
                      means disable thinking. You can alterntively set the
                      option to an integer controlling the hard-cutoff for
                      reasoning token length (this is not entirely OpenAI
                      compatible, you might have to use fireworks.ai client
                      library to bypass the schema check).

                      Note: For OpenAI GPT OSS models, only the string values
                      ('low', 'medium', 'high') are supported. Integer values
                      will not work with these models.
              mirostat_lr:
                allOf:
                  - type: number
                    default: 0.1
                    nullable: true
                    description: >
                      Specifies the learning rate for the Mirostat sampling
                      algorithm, which controls how quickly the model adjusts
                      its token distribution to maintain the target perplexity.
                      A smaller value slows down the adjustments, leading to
                      more stable but gradual shifts, while higher values speed
                      up corrections at the cost of potential instability.
              mirostat_target:
                allOf:
                  - type: number
                    nullable: true
                    description: >
                      Defines the target perplexity for the Mirostat algorithm.
                      Perplexity measures the unpredictability of the generated
                      text, with higher values encouraging more diverse and
                      creative outputs, while lower values prioritize
                      predictability and coherence. The algorithm dynamically
                      adjusts the token selection to maintain this target during
                      text generation.


                      If not specified, Mirostat sampling is disabled.
              'n':
                allOf:
                  - type: integer
                    minimum: 1
                    maximum: 128
                    default: 1
                    example: 1
                    nullable: true
                    description: >
                      How many completions to generate for each prompt.


                      **Note:** Because this parameter generates many
                      completions, it can quickly consume your token quota. Use
                      carefully and ensure that you have reasonable settings for
                      `max_tokens` and `stop`.
              ignore_eos:
                allOf:
                  - description: >
                      This setting controls whether the model should ignore the
                      End of Sequence (EOS) token. When set to `True`, the model
                      will continue generating tokens even after the EOS token
                      is produced. By default, it stops when the EOS token is
                      reached.
                    type: boolean
                    nullable: true
                    default: false
              stop:
                allOf:
                  - description: >
                      Up to 4 sequences where the API will stop generating
                      further tokens. The returned text will NOT contain the
                      stop sequence.
                    default: null
                    oneOf:
                      - type: string
                        nullable: true
                      - type: array
                        minItems: 1
                        maxItems: 4
                        items:
                          type: string
              response_format:
                allOf:
                  - type: object
                    description: >
                      Allows to force the model to produce specific output
                      format.


                      Setting to `{ "type": "json_object" }` enables JSON mode,
                      which guarantees the message the model generates is valid
                      JSON.


                      If "type" is "json_schema", a JSON schema must be
                      provided. E.g., `response_format = {"type": "json_schema",
                      "json_schema": <json_schema>}`.


                      **Important:** when using JSON mode, it's crucial to also
                      instruct the model to produce JSON via a system or user
                      message. Without this, the model may generate an unending
                      stream of whitespace until the generation reaches the
                      token limit, resulting in a long-running and seemingly
                      "stuck" request. Also note that the message content may be
                      partially cut off if `finish_reason="length"`, which
                      indicates the generation exceeded `max_tokens` or the
                      conversation exceeded the max context length. In this case
                      the return value might not be a valid JSON.
                    nullable: true
                    default: null
                    properties:
                      type:
                        type: string
                        enum:
                          - text
                          - json_object
                          - json_schema
                        example: json_object
                        default: text
                        description: Must be one of `text`, `json_object` or `json_schema`.
                      json_schema:
                        type: object
                        default: null
                        nullable: true
                        description: >
                          JSON schema according to
                          https://json-schema.org/specification that can be
                          provided if `"type": "json_schema"`.


                          Most common fields like `type`, `properties`, `items`,
                          `required` and `anyOf` are supported.


                          More sophisticated cases like `oneOf` might not be
                          covered.


                          Note: it's an OpenAI API extension.


                          Example: `{"type": "object", "properties": {"foo":
                          {"type": "string"}, "bar": {"type": "integer"}},
                          "required": ["foo"]}`
                    required:
                      - type
              stream:
                allOf:
                  - description: >
                      Whether to stream back partial progress. If set, tokens
                      will be sent as data-only [server-sent
                      events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)

                      as they become available, with the stream terminated by a
                      `data: [DONE]` message.
                    type: boolean
                    nullable: true
                    default: false
              context_length_exceeded_behavior:
                allOf:
                  - type: string
                    enum:
                      - truncate
                      - error
                    description: >
                      What to do if the token count of prompt plus `max_tokens`
                      exceeds the model's context window.


                      Passing `truncate` limits the `max_tokens` to at most
                      `context_window_length - prompt_length`. This is the
                      default.


                      Passing `error` would trigger a request error.


                      The default of 'truncate' is selected as it allows to ask
                      for high `max_tokens` value while respecting the context
                      window length without having to do client-side prompt
                      tokenization.


                      Note, that it differs from OpenAI's behavior that matches
                      that of `error`.
              logprobs:
                allOf:
                  - oneOf:
                      - type: boolean
                      - type: integer
                        minimum: 0
                        maximum: 5
                    default: null
                    nullable: true
                    description: >
                      Include log probabilities in the response. This accepts
                      either a boolean or an integer:


                      - If set to `true`, log probabilities are included and the
                      number of alternatives can be controlled via
                      `top_logprobs` (OpenAI-compatible behavior).

                      - If set to an integer N (0-5), include log probabilities
                      for up to N most likely tokens per position in the legacy
                      format.


                      The API will always return the `logprob` of the sampled
                      token, so there may be up to `logprobs+1` elements in the
                      response when an integer is used. The maximum value for
                      the integer form is 5.
              top_logprobs:
                allOf:
                  - type: integer
                    minimum: 0
                    maximum: 5
                    default: null
                    nullable: true
                    description: >
                      An integer between 0 and 5 specifying the number of most
                      likely tokens to return at each token position, each with
                      an associated log probability. The minimum value is 0 and
                      the maximum value is 5.


                      When `logprobs` is set, `top_logprobs` can be used to
                      modify how many top log probabilities are returned. If
                      `top_logprobs` is not set, the API will return up to
                      `logprobs` tokens per position.
              echo:
                allOf:
                  - type: boolean
                    default: false
                    nullable: true
                    description: Echo back the prompt in addition to the completion.
              min_p:
                allOf:
                  - type: number
                    minimum: 0
                    maximum: 1
                    default: 0
                    nullable: true
                    description: >
                      Minimum probability threshold for token selection. Only
                      tokens with probability >= min_p are considered for
                      selection. This is an alternative to top_p and top_k
                      sampling.
              typical_p:
                allOf:
                  - type: number
                    minimum: 0
                    maximum: 1
                    default: 1
                    nullable: true
                    description: >
                      Typical-p sampling is an alternative to nucleus sampling.
                      It considers the most typical tokens whose cumulative
                      probability is at most typical_p.
              logit_bias:
                allOf:
                  - type: object
                    additionalProperties:
                      type: number
                    nullable: true
                    description: >
                      Modify the likelihood of specified tokens appearing in the
                      completion. Accepts a json object that maps tokens
                      (specified by their token ID in the tokenizer) to an
                      associated bias value from -100 to 100. Mathematically,
                      the bias is added to the logits generated by the model
                      prior to sampling.
              user:
                allOf:
                  - description: >-
                      A unique identifier representing your end-user, which can
                      help monitor and detect abuse
                    type: string
                    nullable: true
            required: true
            refIdentifier: '#/components/schemas/BaseCreateCompletionRequest'
            requiredProperties:
              - model
              - messages
        examples:
          example:
            value:
              model: accounts/fireworks/models/llama-v3p1-8b-instruct
              messages:
                - role: system
                  content: <string>
                  name: <string>
              tool_choice: none
              tools:
                - type: function
                  function:
                    description: <string>
                    name: <string>
                    parameters:
                      type: object
                      required:
                        - <string>
                      properties: {}
              max_tokens: 2000
              prompt_truncate_len: 1500
              temperature: 1
              top_p: 1
              top_k: 50
              frequency_penalty: 0
              perf_metrics_in_response: false
              presence_penalty: 0
              repetition_penalty: 1
              reasoning_effort: none
              mirostat_lr: 0.1
              mirostat_target: 123
              'n': 1
              ignore_eos: false
              stop: <string>
              response_format: null
              stream: false
              context_length_exceeded_behavior: truncate
              logprobs: true
              top_logprobs: null
              echo: false
              min_p: 0
              typical_p: 1
              logit_bias: {}
              user: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: A unique identifier of the response.
              object:
                allOf:
                  - type: string
                    description: The object type, which is always "chat.completion".
              created:
                allOf:
                  - type: integer
                    description: The Unix time in seconds when the response was generated.
              model:
                allOf:
                  - type: string
                    description: The model used for the chat completion.
              choices:
                allOf:
                  - type: array
                    description: The list of chat completion choices.
                    items:
                      type: object
                      required:
                        - index
                        - message
                        - finish_reason
                      properties:
                        index:
                          type: integer
                          description: The index of the chat completion choice.
                        message:
                          $ref: '#/components/schemas/ChatCompletionResponseMessage'
                        finish_reason:
                          type: string
                          description: >
                            The reason the model stopped generating tokens. This
                            will be "stop" if

                            the model hit a natural stop point or a provided
                            stop sequence, or

                            "length" if the maximum number of tokens specified
                            in the request was

                            reached.
                          enum:
                            - stop
                            - length
              usage:
                allOf:
                  - $ref: '#/components/schemas/UsageInfo'
            refIdentifier: '#/components/schemas/CreateChatCompletionResponse'
            requiredProperties:
              - id
              - object
              - created
              - model
              - choices
        examples:
          example:
            value:
              id: <string>
              object: <string>
              created: 123
              model: <string>
              choices:
                - index: 123
                  message:
                    role: system
                    content: <string>
                    reasoning_content: <string>
                    tool_calls:
                      - id: <string>
                        type: function
                        function:
                          name: <string>
                          arguments: <string>
                  finish_reason: stop
              usage:
                prompt_tokens: 123
                completion_tokens: 123
                total_tokens: 123
        description: OK
  deprecated: false
  type: path
components:
  schemas:
    ChatCompletionRequestMessage:
      type: object
      properties:
        role:
          type: string
          enum:
            - system
            - user
            - assistant
          description: >-
            The role of the messages author. One of `system`, `user`, or
            `assistant`.
        content:
          oneOf:
            - type: string
              nullable: true
              description: >
                The contents of the message. `content` is required for all

                messages, and may be null for assistant messages with function
                calls.
            - type: array
              description: A list of chat messages that could contain images or texts
              items:
                $ref: '#/components/schemas/ChatMessageContent'
        name:
          type: string
          description: >-
            The name of the author of this message. May contain a-z, A-Z, 0-9,
            and underscores, with a maximum length of 64 characters.
      required:
        - role
        - content
    ChatMessageContent:
      description: |
        The content of the message. Can either be text or image_url.
      oneOf:
        - type: object
          description: A message containing text
          properties:
            type:
              type: string
              enum:
                - text
            text:
              type: string
              description: The content of the message.
        - type: object
          description: A message containing image
          properties:
            type:
              type: string
              enum:
                - image_url
            image_url:
              type: object
              properties:
                url:
                  type: string
                  description: >
                    base64 encoded string for image formatted as
                    MIME_TYPE,\<base64 encoded str\>

                    eg. data:image/jpeg;base64,\<base64 encoded str\>
    ChatCompletionResponseMessage:
      type: object
      properties:
        role:
          type: string
          enum:
            - system
            - user
            - assistant
          description: The role of the author of this message.
        content:
          type: string
          description: The contents of the message.
          nullable: true
        reasoning_content:
          type: string
          description: >-
            The reasoning or thinking process generated by the model. This field
            is only available for certain reasoning models (GLM 4.5, GLM 4.5
            Air, GPT OSS 120B, GPT OSS 20B) and contains the model's internal
            reasoning that would otherwise appear in <think></think> tags within
            the content field.
          nullable: true
        tool_calls:
          $ref: '#/components/schemas/ChatCompletionMessageToolCalls'
      required:
        - role
    ChatCompletionMessageToolCalls:
      type: array
      description: The tool calls generated by the model, such as function calls.
      items:
        $ref: '#/components/schemas/ChatCompletionMessageToolCall'
    ChatCompletionMessageToolCall:
      type: object
      properties:
        id:
          type: string
          description: The ID of the tool call.
        type:
          type: string
          enum:
            - function
          description: The type of the tool. Currently, only `function` is supported.
        function:
          type: object
          description: The function that the model called.
          properties:
            name:
              type: string
              description: The name of the function to call.
            arguments:
              type: string
              description: >-
                The arguments to call the function with, as generated by the
                model in JSON format. Note that the model does not always
                generate valid JSON, and may hallucinate parameters not defined
                by your function schema. Validate the arguments in your code
                before calling your function.
          required:
            - name
            - arguments
      required:
        - id
        - type
        - function
    ChatCompletionTool:
      type: object
      properties:
        type:
          type: string
          enum:
            - function
          description: The type of the tool. Currently, only `function` is supported.
        function:
          $ref: '#/components/schemas/FunctionObject'
      required:
        - type
        - function
    FunctionObject:
      type: object
      properties:
        description:
          type: string
          description: >-
            A description of what the function does, used by the model to choose
            when and how to call the function.
        name:
          type: string
          description: >-
            The name of the function to be called. Must be a-z, A-Z, 0-9, or
            contain underscores and dashes, with a maximum length of 64.
        parameters:
          $ref: '#/components/schemas/FunctionParameters'
      required:
        - name
        - parameters
    FunctionParameters:
      type: object
      properties:
        type:
          type: string
          enum:
            - object
          description: type of parameter
        required:
          type: array
          description: which one of the parameter is required
          items:
            type: string
        properties:
          type: object
          additionalProperties:
            type: object
            properties:
              type:
                type: string
                description: The type of the property
              description:
                type: string
                description: A description of the property
          description: >-
            A map of property names to their types and descriptions. Each
            property is an object with 'type' and 'description' fields.
      description: >-
        The parameters the functions accepts, described as a JSON Schema
        object. 


        To describe a function that accepts no parameters, provide the value
        `{"type": "object", "properties": {}}`.
    UsageInfo:
      type: object
      description: >
        Usage statistics.


        For streaming responses, `usage` field is included in the very last
        response chunk returned.


        Note that returning `usage` for streaming requests is an OpenAI API
        extension. If you use OpenAI SDK, you might access the field directly
        even if it's not present in the type signature in the SDK.
      properties:
        prompt_tokens:
          type: integer
          description: The number of tokens in the prompt.
        completion_tokens:
          type: integer
          description: The number of tokens in the generated completion.
        total_tokens:
          type: integer
          description: >-
            The total number of tokens used in the request (prompt +
            completion).
      required:
        - prompt_tokens
        - completion_tokens
        - total_tokens
    ToolChoiceOptions:
      type: string
      title: Tool choice mode
      description: >
        Controls which (if any) tool is called by the model.


        `none` means the model will not call any tool and instead generates a
        message.


        `auto` means the model can pick between generating a message or calling
        one or

        more tools.


        `required` means the model must call one or more tools. This is
        equivalent to `any`.
      enum:
        - none
        - auto
        - required
        - any
    ToolChoiceFunction:
      type: object
      title: Function tool
      description: |
        Use this option to force the model to call a specific function.
      properties:
        type:
          type: string
          enum:
            - function
          description: For function calling, the type is always `function`.
          x-stainless-const: true
        name:
          type: string
          description: The name of the function to call.
        function:
          type: object
          description: >-
            OpenAI-compatible nested function object. Either `name` or
            `function.name` must be provided.
          properties:
            name:
              type: string
              description: The name of the function to call.
      required:
        - type

````