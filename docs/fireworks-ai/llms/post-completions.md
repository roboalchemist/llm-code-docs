# Source: https://docs.fireworks.ai/api-reference/post-completions.md

# Create Completion

> Creates a completion for the provided prompt and parameters.

## OpenAPI

````yaml post /completions
paths:
  path: /completions
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
              prompt:
                allOf:
                  - description: >
                      The prompt to generate completions for.

                      It can be a single string or an array of strings.

                      It can also be an array of integers or an array of integer
                      arrays,

                      which allows to pass already tokenized prompt.

                      If multiple prompts are specified, several choices with
                      corresponding `index` will be returned in the output."
                    oneOf:
                      - type: string
                        example: The sky is
                      - type: array
                        minItems: 1
                        items:
                          type: string
                          example: The sky is
                      - type: array
                        minItems: 1
                        items:
                          type: integer
                        example: '[123, 10, 456]'
                      - type: array
                        minItems: 1
                        items:
                          type: array
                          minItems: 1
                          items:
                            type: integer
                        example: '[[123, 10, 456], [100, 543]]'
              images:
                allOf:
                  - description: >
                      The list of base64 encoded images for visual language
                      completition generation.

                      They should be formatted as MIME_TYPE,\<base64 encoded
                      str\>

                      eg. data:image/jpeg;base64,\<base64 encoded str\>

                      Additionally, the number of images provided should match
                      the number of '\<image\>' special token in the prompt
                    type: array
                    items:
                      type: string
              max_tokens:
                allOf:
                  - type: integer
                    minimum: 0
                    default: 16
                    example: 16
                    nullable: true
                    description: >
                      The maximum number of tokens to generate in the
                      completion.


                      If the token count of your prompt plus `max_tokens` exceed
                      the model's context length, the behavior is depends on
                      `context_length_exceeded_behavior`. By default,
                      `max_tokens` will be lowered to fit in the context window
                      instead of returning an error.
              echo_last:
                allOf:
                  - type: integer
                    minimum: 0
                    nullable: true
                    description: >
                      Echo back the last N tokens of the prompt in addition to
                      the completion. This is useful for obtaining logprobs of
                      the prompt suffix but without transferring too much data.
                      Passing `echo_last=len(prompt)` is the same as `echo=True`
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
              - prompt
        examples:
          example:
            value:
              model: accounts/fireworks/models/llama-v3p1-8b-instruct
              prompt: The sky is
              images:
                - <string>
              max_tokens: 16
              echo_last: 1
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
                    description: The object type, which is always "text_completion".
              created:
                allOf:
                  - type: integer
                    description: The Unix time in seconds when the response was generated.
              model:
                allOf:
                  - type: string
                    description: The model used for the completion.
              choices:
                allOf:
                  - type: array
                    description: The list of generated completion choices.
                    items:
                      type: object
                      required:
                        - text
                        - index
                        - logprobs
                        - finish_reason
                      properties:
                        text:
                          type: string
                          description: The completion response.
                        index:
                          type: integer
                          description: The index of the completion choice.
                        logprobs:
                          type: object
                          description: The log probabilities of the most likely tokens.
                          nullable: true
                          properties:
                            tokens:
                              type: array
                              items:
                                type: string
                            token_logprobs:
                              type: array
                              items:
                                type: number
                            top_logprobs:
                              type: array
                              items:
                                type: object
                                additionalProperties:
                                  type: integer
                            text_offset:
                              type: array
                              items:
                                type: integer
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
            refIdentifier: '#/components/schemas/CreateCompletionResponse'
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
                - text: <string>
                  index: 123
                  logprobs:
                    tokens:
                      - <string>
                    token_logprobs:
                      - 123
                    top_logprobs:
                      - {}
                    text_offset:
                      - 123
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

````