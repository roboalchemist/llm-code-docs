# Source: https://docs.fireworks.ai/api-reference/post-chatcompletions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Chat Completion

> Create a completion for the provided prompt and parameters.



## OpenAPI

````yaml post /v1/chat/completions
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
  /v1/chat/completions:
    servers:
      - url: https://api.fireworks.ai/inference
    post:
      tags:
        - text-completion.openapi_other
      summary: Create Chat Completion
      description: Create a completion for the provided prompt and parameters.
      operationId: create_chat_completion_v1_chat_completions_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ChatCompletionRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatCompletionResponse'
            text/event-stream:
              schema:
                $ref: '#/components/schemas/ChatCompletionStreamResponse'
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
    ChatCompletionRequest:
      properties:
        model:
          type: string
          title: Model
          description: |-
            The name of the model to use.

            Example: `"accounts/fireworks/models/kimi-k2-instruct-0905"`
        messages:
          items:
            $ref: '#/components/schemas/ChatMessage'
          type: array
          title: Messages
          description: A list of messages comprising the conversation so far.
        tools:
          items:
            $ref: '#/components/schemas/ChatCompletionTool'
          type: array
          title: Tools
          description: >-
            A list of tools the model may call. Currently, only functions are
            supported as a tool.


            Use this to provide a list of functions the model may generate JSON
            inputs for.


            See the our [model
            library](https://app.fireworks.ai/models/?filter=LLM&functionCalling=true)
            for the list of supported models
        tool_choice:
          anyOf:
            - type: string
              enum:
                - auto
                - none
                - any
                - required
            - $ref: '#/components/schemas/FunctionSelection'
          title: Tool Choice
          description: >-
            Controls which (if any) tool is called by the model.


            - `none`: the model will not call any tool and instead generates a
            message.

            - `auto`: the model can pick between generating a message or calling
            one or more tools.

            - `required` (alias: `any`): the model must call one or more tools.
              To force a specific function, pass an object of the form `{ "type": "function", "name": "my_function" }` or `{ "type": "function", "function": { "name": "my_function" } }` for OpenAI compatibility.
          default: auto
        stream:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Stream
          description: >-
            Whether to stream back partial progress. If set, tokens will be sent
            as data-only [server-sent
            events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
            as they become available, with the stream terminated by a `data:
            [DONE]` message.
          default: false
        response_format:
          anyOf:
            - $ref: '#/components/schemas/ResponseFormat'
            - type: 'null'
          description: >-
            Allows to force the model to produce specific output format.


            Setting to `{ "type": "json_object" }` enables JSON mode, which
            guarantees the message the model generates is valid JSON.


            If `"type"` is `"json_schema"`, a JSON schema must be provided.
            E.g., `response_format = {"type": "json_schema", "json_schema":
            <json_schema>}`.


            Important: when using JSON mode, it's crucial to also instruct the
            model to produce JSON via a system or user message. Without this,
            the model may generate an unending stream of whitespace until the
            generation reaches the token limit, resulting in a long-running and
            seemingly "stuck" request.


            Also note that the message content may be partially cut off if
            `finish_reason="length"`, which indicates the generation exceeded
            `max_tokens` or the conversation exceeded the max context length. In
            this case the return value might not be a valid JSON.
        temperature:
          anyOf:
            - type: number
            - type: 'null'
          title: Temperature
          description: >-
            What sampling temperature to use, between 0 and 2. Higher values
            like 0.8 will make the output more random, while lower values like
            0.2 will make it more focused and deterministic.


            We generally recommend altering this or top_p but not both.


            Required range: `0 <= x <= 2`


            Example: `1`
        top_k:
          anyOf:
            - type: integer
            - type: 'null'
          title: Top K
          description: >-
            Top-k sampling is another sampling method where the k most probable
            next tokens are filtered and the probability mass is redistributed
            among only those k next tokens. The value of k controls the number
            of candidates for the next token at each step during text
            generation. Must be between 0 and 100.


            Required range: `0 <= x <= 100`


            Example: `50`
        user:
          anyOf:
            - type: string
            - type: 'null'
          title: User
          description: >-
            A unique identifier representing your end-user, which can help
            monitor and detect abuse.
        prompt_cache_isolation_key:
          anyOf:
            - type: string
            - type: 'null'
          title: Prompt Cache Isolation Key
          description: Isolation key for prompt caching to separate cache entries.
        raw_output:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Raw Output
          description: Return raw output from the model.
          default: false
        perf_metrics_in_response:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Perf Metrics In Response
          description: >-
            Whether to include performance metrics in the response body.


            **Non-streaming requests:** Performance metrics are always included
            in response headers (e.g., `fireworks-prompt-tokens`,
            `fireworks-server-time-to-first-token`). Setting this to `true`
            additionally includes the same metrics in the response body under
            the `perf_metrics` field.


            **Streaming requests:** Performance metrics are only included in the
            response body under the `perf_metrics` field in the final chunk
            (when `finish_reason` is set). This is because headers may not be
            accessible during streaming.


            The response body `perf_metrics` field contains the following
            metrics:


            **Basic Metrics (all deployments):**


            - `prompt-tokens`: Number of tokens in the prompt

            - `cached-prompt-tokens`: Number of cached prompt tokens

            - `server-time-to-first-token`: Time from request start to first
            token (in seconds)

            - `server-processing-time`: Total processing time (in seconds, only
            for completed requests)


            **Predicted Outputs Metrics:**


            - `speculation-prompt-tokens`: Number of speculative prompt tokens

            - `speculation-prompt-matched-tokens`: Number of matched speculative
            prompt tokens (for completed requests)


            **Dedicated Deployment Only Metrics:**


            - `speculation-generated-tokens`: Number of speculative generated
            tokens (for completed requests)

            - `speculation-acceptance`: Speculation acceptance rates by position

            - `backend-host`: Hostname of the backend server

            - `num-concurrent-requests`: Number of concurrent requests

            - `deployment`: Deployment name

            - `tokenizer-queue-duration`: Time spent in tokenizer queue

            - `tokenizer-duration`: Time spent in tokenizer

            - `prefill-queue-duration`: Time spent in prefill queue

            - `prefill-duration`: Time spent in prefill

            - `generation-queue-duration`: Time spent in generation queue
          default: false
        'n':
          type: integer
          title: 'N'
          description: >-
            How many completions to generate for each prompt.


            **Note:** Because this parameter generates many completions, it can
            quickly consume your token quota. Use carefully and ensure that you
            have reasonable settings for `max_tokens` and `stop`.


            Required range: `1 <= x <= 128`


            Example: `1`
          default: 1
        stop:
          anyOf:
            - type: string
            - type: array
              items:
                type: string
            - type: 'null'
          title: Stop
          description: >-
            Up to 4 sequences where the API will stop generating further tokens.
            The returned text will NOT contain the stop sequence.
        max_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Tokens
          description: >-
            The maximum number of tokens to generate in the completion. If the
            token count of your prompt plus max_tokens exceeds the model's
            context length, the behavior depends on
            context_length_exceeded_behavior. By default, max_tokens will be
            lowered to fit in the context window instead of returning an error.
        max_completion_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Completion Tokens
          description: Alias for max_tokens. Cannot be specified together with max_tokens.
        top_p:
          anyOf:
            - type: number
            - type: 'null'
          title: Top P
          description: >-
            An alternative to sampling with temperature, called nucleus
            sampling, where the model considers the results of the tokens with
            top_p probability mass. So 0.1 means only the tokens comprising the
            top 10% probability mass are considered.


            We generally recommend altering this or temperature but not both.


            Required range: `0 <= x <= 1`


            Example: `1`
        min_p:
          anyOf:
            - type: number
            - type: 'null'
          title: Min P
          description: >-
            Minimum probability threshold for token selection. Only tokens with
            probability >= min_p are considered for selection. This is an
            alternative to `top_p` and `top_k` sampling.


            Required range: `0 <= x <= 1`
        typical_p:
          anyOf:
            - type: number
            - type: 'null'
          title: Typical P
          description: >-
            Typical-p sampling is an alternative to nucleus sampling. It
            considers the most typical tokens whose cumulative probability is at
            most typical_p.


            Required range: `0 <= x <= 1`
        frequency_penalty:
          anyOf:
            - type: number
            - type: 'null'
          title: Frequency Penalty
          description: >-
            Number between -2.0 and 2.0. Positive values penalize new tokens
            based on their existing frequency in the text so far, decreasing the
            model's likelihood to repeat the same line verbatim.


            Reasonable value is around 0.1 to 1 if the aim is to just reduce
            repetitive samples somewhat. If the aim is to strongly suppress
            repetition, then one can increase the coefficients up to 2, but this
            can noticeably degrade the quality of samples. Negative values can
            be used to increase the likelihood of repetition.


            See also `presence_penalty` for penalizing tokens that have at least
            one appearance at a fixed rate.


            OpenAI compatible (follows OpenAI's conventions for handling token
            frequency and repetition penalties).


            Required range: `-2 <= x <= 2`
        presence_penalty:
          anyOf:
            - type: number
            - type: 'null'
          title: Presence Penalty
          description: >-
            Number between -2.0 and 2.0. Positive values penalize new tokens
            based on whether they appear in the text so far, increasing the
            model's likelihood to talk about new topics.


            Reasonable value is around 0.1 to 1 if the aim is to just reduce
            repetitive samples somewhat. If the aim is to strongly suppress
            repetition, then one can increase the coefficients up to 2, but this
            can noticeably degrade the quality of samples. Negative values can
            be used to increase the likelihood of repetition.


            See also `frequency_penalty` for penalizing tokens at an increasing
            rate depending on how often they appear.


            OpenAI compatible (follows OpenAI's conventions for handling token
            frequency and repetition penalties).


            Required range: `-2 <= x <= 2`
        repetition_penalty:
          anyOf:
            - type: number
            - type: 'null'
          title: Repetition Penalty
          description: >-
            Applies a penalty to repeated tokens to discourage or encourage
            repetition. A value of `1.0` means no penalty, allowing free
            repetition. Values above `1.0` penalize repetition, reducing the
            likelihood of repeating tokens. Values between `0.0` and `1.0`
            reward repetition, increasing the chance of repeated tokens. For a
            good balance, a value of `1.2` is often recommended. Note that the
            penalty is applied to both the generated output and the prompt in
            decoder-only models.


            Required range: `0 <= x <= 2`
        mirostat_target:
          anyOf:
            - type: number
            - type: 'null'
          title: Mirostat Target
          description: >-
            Defines the target perplexity for the Mirostat algorithm. Perplexity
            measures the unpredictability of the generated text, with higher
            values encouraging more diverse and creative outputs, while lower
            values prioritize predictability and coherence. The algorithm
            dynamically adjusts the token selection to maintain this target
            during text generation.


            If not specified, Mirostat sampling is disabled.
        mirostat_lr:
          anyOf:
            - type: number
            - type: 'null'
          title: Mirostat Lr
          description: >-
            Specifies the learning rate for the Mirostat sampling algorithm,
            which controls how quickly the model adjusts its token distribution
            to maintain the target perplexity. A smaller value slows down the
            adjustments, leading to more stable but gradual shifts, while higher
            values speed up corrections at the cost of potential instability.
        seed:
          anyOf:
            - type: integer
            - type: 'null'
          title: Seed
          description: Random seed for deterministic sampling.
        logprobs:
          anyOf:
            - type: integer
            - type: boolean
            - type: 'null'
          title: Logprobs
          description: >-
            Include log probabilities in the response. This accepts either a
            boolean or an integer:


            If set to `true`, log probabilities are included and the number of
            alternatives can be controlled via `top_logprobs` (OpenAI-compatible
            behavior).


            If set to an integer N (0-5), include log probabilities for up to N
            most likely tokens per position in the legacy format.


            The API will always return the logprob of the sampled token, so
            there may be up to `logprobs+1` elements in the response when an
            integer is used. The maximum value for the integer form is 5.
        top_logprobs:
          anyOf:
            - type: integer
            - type: 'null'
          title: Top Logprobs
          description: >-
            An integer between 0 and 5 specifying the number of most likely
            tokens to return at each token position, each with an associated log
            probability. The minimum value is 0 and the maximum value is 5.


            When `logprobs` is set, `top_logprobs` can be used to modify how
            many top log probabilities are returned. If `top_logprobs` is not
            set, the API will return up to `logprobs` tokens per position.


            Required range: `0 <= x <= 5`
        echo:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Echo
          description: Echo back the prompt in addition to the completion.
          default: false
        echo_last:
          anyOf:
            - type: integer
            - type: 'null'
          title: Echo Last
          description: >-
            Echo back the last N tokens of the prompt in addition to the
            completion. This is useful for obtaining logprobs of the prompt
            suffix but without transferring too much data. Passing
            `echo_last=len(prompt)` is the same as `echo=True`
        ignore_eos:
          type: boolean
          title: Ignore Eos
          description: >-
            This setting controls whether the model should ignore the End of
            Sequence (EOS) token. When set to `True`, the model will continue
            generating tokens even after the EOS token is produced. By default,
            it stops when the EOS token is reached.
          default: false
        context_length_exceeded_behavior:
          type: string
          enum:
            - error
            - truncate
          title: Context Length Exceeded Behavior
          description: >-
            What to do if the token count of prompt plus `max_tokens` exceeds
            the model's context window.


            Passing `truncate` limits the `max_tokens` to at most
            `context_window_length - prompt_length`. This is the default.


            Passing `error` would trigger a request error.


            The default of `'truncate'` is selected as it allows to ask for high
            `max_tokens` value while respecting the context window length
            without having to do client-side prompt tokenization.


            Note, that it differs from OpenAI's behavior that matches that of
            `error`.
          default: truncate
        logit_bias:
          anyOf:
            - additionalProperties:
                type: number
              type: object
            - type: 'null'
          title: Logit Bias
          description: >-
            Modify the likelihood of specified tokens appearing in the
            completion. Accepts a json object that maps tokens (specified by
            their token ID in the tokenizer) to an associated bias value from
            -100 to 100. Mathematically, the bias is added to the logits
            generated by the model prior to sampling.
        speculation:
          anyOf:
            - type: string
            - items:
                type: integer
              type: array
            - type: 'null'
          title: Speculation
          description: Speculative decoding prompt or token IDs to speed up generation.
        prediction:
          anyOf:
            - $ref: '#/components/schemas/PredictedOutput'
            - type: string
            - type: 'null'
          title: Prediction
          description: >-
            OpenAI-compatible predicted output for speculative decoding. Can be
            a PredictedOutput object or a simple string. Automatically
            transformed to speculation.
        metadata:
          anyOf:
            - type: object
              additionalProperties:
                type: string
            - type: 'null'
          title: Metadata
          description: >-
            Additional metadata to store with the request for
            tracing/distillation.
        reasoning_effort:
          anyOf:
            - type: string
              enum:
                - low
                - medium
                - high
                - none
            - type: integer
            - type: boolean
            - type: 'null'
          title: Reasoning Effort
          description: >-
            Controls reasoning behavior for supported models. When enabled, the
            model's reasoning appears in the `reasoning_content` field of the
            response, separate from the final answer in `content`.


            **Accepted values:**


            - **String** (OpenAI-compatible): `'low'`, `'medium'`, or `'high'`
            to enable reasoning with varying effort levels; `'none'` to disable
            reasoning.

            - **Boolean** (Fireworks extension): `true` to enable reasoning,
            `false` to disable it.

            - **Integer** (Fireworks extension): A positive integer to set a
            hard token limit on reasoning output (only effective for
            grammar-based reasoning models).


            **Important:** Boolean values are normalized internally: `true`
            becomes `'medium'`, and `false` becomes `'none'`. This normalization
            happens before model-specific validation, so if a model doesn't
            support `'none'`, passing `false` will produce an error referencing
            `'none'`.


            **Model-specific behavior:**


            - **Qwen3 (e.g., Qwen3-8B)**: Grammar-based reasoning. Default
            reasoning on. Use `'none'` or `false` to disable. Supports integer
            token limits to cap reasoning output. `'low'` maps to a default
            token limit (~3000 tokens).

            - **MiniMax M2**: Reasoning is required (always on). Defaults to
            `'medium'` when omitted. Accepts only string `reasoning_effort`:
            `'low'`, `'medium'`, or `'high'`. `'none'` and boolean values are
            rejected.

            - **DeepSeek V3.1, DeepSeek V3.2**: Binary on/off reasoning. Default
            reasoning on. Use `'none'` or `false` to disable; effort levels and
            integers have no additional effect.

            - **GLM 4.5, GLM 4.5 Air, GLM 4.6, GLM 4.7**: Binary on/off
            reasoning. Default reasoning on. Use `'none'` or `false` to disable;
            effort levels and integers have no additional effect.

            - **Harmony (OpenAI GPT-OSS 120B, GPT-OSS 20B)**: Accepts only
            `'low'`, `'medium'`, or `'high'`. Does not support `'none'`,
            `false`, or integer values — using these will return an error (e.g.,
            "Invalid reasoning effort: none"). When omitted, defaults to
            `'medium'`. Lower effort produces faster responses with shorter
            reasoning.
        reasoning_history:
          anyOf:
            - type: string
              enum:
                - disabled
                - interleaved
                - preserved
            - type: 'null'
          title: Reasoning History
          description: >-
            Controls how historical assistant reasoning content is included in
            the prompt for multi-turn conversations.


            **Accepted values:**


            - `null`: Use model/template default behavior (for **GLM-4.7**, the
            model/template default is `'interleaved'`, i.e. historical reasoning
            is cleared by default)

            - `'disabled'`: Strip `reasoning_content` from all messages before
            prompt construction

            - `'interleaved'`: Strip `reasoning_content` from messages up to
            (and including) the last user message

            - `'preserved'`: Preserve historical `reasoning_content` across the
            conversation


            **Model support:**


            | Model | Default | Supported values |

            | --- | --- | --- |

            | Kimi K2 Instruct | `'preserved'` | `'disabled'`, `'interleaved'`,
            `'preserved'` |

            | MiniMax M2 | `'interleaved'` | `'disabled'`, `'interleaved'` |

            | GLM-4.7 | `'interleaved'` | `'disabled'`, `'interleaved'`,
            `'preserved'` |

            | GLM-4.6 | `'interleaved'` | `'disabled'`, `'interleaved'` |


            For other models, refer to the model provider's documentation.


            **Note:** This parameter controls prompt formatting only. To disable
            reasoning computation entirely, use `reasoning_effort='none'`.
        thinking:
          anyOf:
            - $ref: '#/components/schemas/ThinkingConfigEnabled'
            - $ref: '#/components/schemas/ThinkingConfigDisabled'
            - type: 'null'
          title: Thinking
          description: >-
            Configuration for enabling extended thinking (Anthropic-compatible
            format). This is an alternative to `reasoning_effort` for
            controlling reasoning behavior.


            **Format:**


            - `{"type": "enabled"}` - Enable thinking (equivalent to
            `reasoning_effort: true`)

            - `{"type": "enabled", "budget_tokens": <int>}` - Enable thinking
            with a token budget (equivalent to `reasoning_effort: <int>`). Must
            be >= 1024.

            - `{"type": "disabled"}` - Disable thinking (equivalent to
            `reasoning_effort: "none"`)


            **Note:** Cannot be specified together with `reasoning_effort`. If
            both are provided, a validation error will be raised.
        return_token_ids:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Return Token Ids
          description: Return token IDs alongside text to avoid retokenization drift.
          default: false
        functions:
          items:
            $ref: '#/components/schemas/ChatCompletionFunction'
          type: array
          title: Functions
          description: >-
            Deprecated in OpenAI. Use 'tools' instead. This will be
            automatically transformed to tools.
          deprecated: true
        prompt_truncate_len:
          anyOf:
            - type: integer
            - type: 'null'
          title: Prompt Truncate Len
          description: >-
            The size (in tokens) to which to truncate chat prompts. This
            includes the system prompt (if any), previous user/assistant
            messages, and the current user message. Earlier user/assistant
            messages will be evicted first to fit the prompt into this length.
            The system prompt is preserved whenever possible and only truncated
            as a last resort.


            This should usually be set to a number much smaller << than the
            model's maximum context size, to allow enough remaining tokens for
            generating a response.


            If omitted, you may receive "prompt too long" errors in your
            responses as conversations grow. Note that even with this set, you
            may still receive "prompt too long" errors if individual messages
            (such as a very long system prompt or user message) exceed the
            model's context window on their own.
        parallel_tool_calls:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Parallel Tool Calls
          description: Enable parallel function calling.
        function_call:
          anyOf:
            - type: string
              enum:
                - auto
                - none
            - $ref: '#/components/schemas/FunctionNameSpec'
            - type: 'null'
          title: Function Call
          description: >-
            Deprecated in OpenAI. Use 'tool_choice' instead. This will be
            automatically transformed to tool_choice.
          deprecated: true
      additionalProperties: false
      type: object
      required:
        - messages
        - model
      title: ChatCompletionRequest
    ChatCompletionResponse:
      additionalProperties: false
      description: The response message from a /v1/chat/completions call.
      properties:
        id:
          description: A unique identifier of the response
          title: Id
          type: string
        object:
          default: chat.completion
          description: The object type, which is always "chat.completion"
          title: Object
          type: string
        created:
          description: The Unix time in seconds when the response was generated
          title: Created
          type: integer
        model:
          description: The model used for the chat completion
          title: Model
          type: string
        choices:
          description: The list of chat completion choices
          items:
            $ref: '#/components/schemas/ChatCompletionResponseChoice'
          title: Choices
          type: array
        usage:
          anyOf:
            - $ref: '#/components/schemas/UsageInfo'
            - type: 'null'
          default: null
        perf_metrics:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          default: null
          description: >-
            See parameter
            [perf_metrics_in_response](#body-perf-metrics-in-response)
          title: Perf Metrics
        prompt_token_ids:
          anyOf:
            - items:
                type: integer
              type: array
            - type: 'null'
          default: null
          description: Token IDs for the prompt (when return_token_ids=true)
          title: Prompt Token Ids
      required:
        - id
        - created
        - model
        - choices
      title: ChatCompletionResponse
      type: object
    ChatCompletionStreamResponse:
      additionalProperties: false
      description: The streamed response message from a /v1/chat/completions call.
      properties:
        id:
          description: A unique identifier of the response
          title: Id
          type: string
        object:
          default: chat.completion.chunk
          description: The object type, which is always "chat.completion.chunk"
          title: Object
          type: string
        created:
          description: The Unix time in seconds when the response was generated
          title: Created
          type: integer
        model:
          description: The model used for the chat completion
          title: Model
          type: string
        choices:
          description: The list of streamed chat completion choices
          items:
            $ref: '#/components/schemas/ChatCompletionResponseStreamChoice'
          title: Choices
          type: array
        usage:
          anyOf:
            - $ref: '#/components/schemas/UsageInfo'
            - type: 'null'
          default: null
        perf_metrics:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          default: null
          description: >-
            See parameter
            [perf_metrics_in_response](#body-perf-metrics-in-response)
          title: Perf Metrics
        prompt_token_ids:
          anyOf:
            - items:
                type: integer
              type: array
            - type: 'null'
          default: null
          description: >-
            Token IDs for the prompt (when return_token_ids=true, sent in first
            chunk)
          title: Prompt Token Ids
      required:
        - id
        - created
        - model
        - choices
      title: ChatCompletionStreamResponse
      type: object
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ChatMessage:
      properties:
        role:
          type: string
          title: Role
          description: >-
            The role of the messages author. One of `system`, `user`, or
            `assistant`.
        content:
          anyOf:
            - type: string
            - items:
                $ref: '#/components/schemas/ChatMessageContent'
              type: array
            - type: 'null'
          title: Content
          description: >-
            The contents of the message. `content` is required for all messages,
            and may be null for assistant messages with function calls.
        reasoning_content:
          anyOf:
            - type: string
            - type: 'null'
          title: Reasoning Content
          description: >-
            The reasoning or thinking process generated by the model. This field
            is only available for certain reasoning models (GLM 4.5, GLM 4.5
            Air, GPT OSS 120B, GPT OSS 20B) and contains the model's internal
            reasoning that would otherwise appear in `<think></think>` tags
            within the content field.
        tool_calls:
          anyOf:
            - items:
                $ref: '#/components/schemas/ChatCompletionMessageToolCall'
              type: array
            - type: 'null'
          title: Tool Calls
          description: The tool calls generated by the model, such as function calls.
        tool_call_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Tool Call Id
      additionalProperties: false
      type: object
      required:
        - role
      title: ChatMessage
      description: A chat completion message.
    ChatCompletionTool:
      properties:
        type:
          type: string
          enum:
            - function
          title: Type
          description: The type of the tool. Currently, only `function` is supported.
        function:
          anyOf:
            - $ref: '#/components/schemas/ChatCompletionFunction'
            - type: 'null'
          description: Required for function tools.
      additionalProperties: false
      type: object
      required:
        - type
      title: ChatCompletionTool
    FunctionSelection:
      properties:
        type:
          type: string
          const: function
          title: Type
        function:
          anyOf:
            - $ref: '#/components/schemas/FunctionNameSpec'
            - type: 'null'
      additionalProperties: false
      type: object
      required:
        - type
      title: FunctionSelection
    ResponseFormat:
      properties:
        type:
          type: string
          enum:
            - json_object
            - json_schema
            - grammar
            - text
          title: Type
        schema:
          anyOf:
            - type: string
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Schema
        grammar:
          anyOf:
            - type: string
            - type: 'null'
          title: Grammar
        json_schema:
          anyOf:
            - type: string
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Json Schema
      additionalProperties: false
      type: object
      required:
        - type
      title: ResponseFormat
    PredictedOutput:
      properties:
        content:
          anyOf:
            - type: string
            - items:
                $ref: '#/components/schemas/ChatMessageContent'
              type: array
          title: Content
        type:
          type: string
          const: content
          title: Type
          default: content
      additionalProperties: false
      type: object
      required:
        - content
      title: PredictedOutput
      description: OpenAI-compatible struct for the "speculation" field.
    ThinkingConfigEnabled:
      properties:
        type:
          type: string
          const: enabled
          title: Type
        budget_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Budget Tokens
          description: >-
            Determines how many tokens the model can use for its internal
            reasoning process. Larger budgets can enable more thorough analysis
            for complex problems, improving response quality. Must be >= 1024 if
            specified.
      additionalProperties: false
      type: object
      required:
        - type
      title: ThinkingConfigEnabled
      description: >-
        Configuration for enabling extended thinking (Anthropic-compatible
        format).
    ThinkingConfigDisabled:
      properties:
        type:
          type: string
          const: disabled
          title: Type
      additionalProperties: false
      type: object
      required:
        - type
      title: ThinkingConfigDisabled
      description: >-
        Configuration for disabling extended thinking (Anthropic-compatible
        format).
    ChatCompletionFunction:
      properties:
        name:
          type: string
          title: Name
          description: >-
            The name of the function to be called. Must be a-z, A-Z, 0-9, or
            contain underscores and dashes, with a maximum length of 64.
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: >-
            A description of what the function does, used by the model to choose
            when and how to call the function.
        parameters:
          additionalProperties: true
          type: object
          title: Parameters
          description: >-
            The parameters the function accepts, described as a JSON Schema
            object.


            The JSON Schema object should have the following structure:


            ```json

            {
              "type": "object",
              "required": ["param1", "param2"],
              "properties": {
                "param1": {
                  "type": "string",
                  "description": "..."
                },
                "param2": {
                  "type": "number",
                  "description": "..."
                }
              }
            }

            ```


            - The `type` field must be `"object"`.

            - The `required` field is an array of strings indicating which
            parameters are required.

            - The `properties` field is a map of property names to their
            definitions, where each property is an object with `type` (string)
            and `description` (string) fields.


            To describe a function that accepts no parameters, provide the
            value:


            ```json

            {"type": "object", "properties": {}}

            ```
        strict:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Strict
      additionalProperties: false
      type: object
      required:
        - name
      title: ChatCompletionFunction
    FunctionNameSpec:
      properties:
        name:
          type: string
          title: Name
      additionalProperties: false
      type: object
      required:
        - name
      title: FunctionNameSpec
    ChatCompletionResponseChoice:
      additionalProperties: false
      description: |-
        A chat completion choice generated by a chat model.

        Attributes:
          index (int): The index of the chat completion choice.
          message (ChatMessage): The chat completion message.
          finish_reason (Optional[str]): The reason the model stopped generating tokens. This will be "stop" if
            the model hit a natural stop point or a provided stop sequence, or
            "length" if the maximum number of tokens specified in the request was
            reached.
          token_ids (Optional[List[int]]): Token IDs for the generated message content (when return_token_ids=true)
      properties:
        index:
          title: Index
          type: integer
        message:
          $ref: '#/components/schemas/ChatMessage'
        finish_reason:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          title: Finish Reason
        logprobs:
          anyOf:
            - $ref: '#/components/schemas/LogProbs'
            - $ref: '#/components/schemas/NewLogProbs'
            - type: 'null'
          default: null
          title: Logprobs
        raw_output:
          anyOf:
            - $ref: '#/components/schemas/RawOutput'
            - type: 'null'
          default: null
        token_ids:
          anyOf:
            - items:
                type: integer
              type: array
            - type: 'null'
          default: null
          title: Token Ids
      required:
        - index
        - message
      title: ChatCompletionResponseChoice
      type: object
    UsageInfo:
      additionalProperties: false
      description: Usage statistics.
      properties:
        prompt_tokens:
          description: The number of tokens in the prompt
          title: Prompt Tokens
          type: integer
        total_tokens:
          description: The total number of tokens used in the request (prompt + completion)
          title: Total Tokens
          type: integer
        completion_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          description: The number of tokens in the generated completion
          title: Completion Tokens
        prompt_tokens_details:
          anyOf:
            - $ref: '#/components/schemas/PromptTokensDetails'
            - type: 'null'
          default: null
          description: Details about prompt tokens, including cached tokens
      required:
        - prompt_tokens
        - total_tokens
      title: UsageInfo
      type: object
    ChatCompletionResponseStreamChoice:
      additionalProperties: false
      description: A streamed chat completion choice.
      properties:
        index:
          description: The index of the chat completion choice
          title: Index
          type: integer
        delta:
          $ref: '#/components/schemas/DeltaMessage'
          description: The message delta
        finish_reason:
          anyOf:
            - enum:
                - stop
                - length
                - function_call
                - tool_calls
              type: string
            - type: 'null'
          default: null
          description: >-
            The reason the model stopped generating tokens. This will be "stop"
            if the model hit a natural stop point or a provided stop sequence,
            or "length" if the maximum number of tokens specified in the request
            was reached
          title: Finish Reason
        logprobs:
          anyOf:
            - $ref: '#/components/schemas/LogProbs'
            - $ref: '#/components/schemas/NewLogProbs'
            - type: 'null'
          default: null
          title: Logprobs
        raw_output:
          anyOf:
            - $ref: '#/components/schemas/RawOutput'
            - type: 'null'
          default: null
        prompt_token_ids:
          anyOf:
            - items:
                type: integer
              type: array
            - type: 'null'
          default: null
          description: Token IDs for the prompt (when return_token_ids=true)
          title: Prompt Token Ids
        token_ids:
          anyOf:
            - items:
                type: integer
              type: array
            - type: 'null'
          default: null
          description: Token IDs for this chunk (when return_token_ids=true)
          title: Token Ids
      required:
        - index
        - delta
      title: ChatCompletionResponseStreamChoice
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
    ChatMessageContent:
      properties:
        type:
          type: string
          title: Type
        text:
          anyOf:
            - type: string
            - type: 'null'
          title: Text
        image_url:
          anyOf:
            - $ref: '#/components/schemas/ChatMessageContentImageURL'
            - type: 'null'
      additionalProperties: false
      type: object
      required:
        - type
      title: ChatMessageContent
    ChatCompletionMessageToolCall:
      properties:
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
          description: The ID of the tool call.
        type:
          type: string
          title: Type
          description: The type of the tool. Currently, only `function` is supported.
          default: function
        function:
          anyOf:
            - $ref: '#/components/schemas/ChatCompletionMessageToolCallFunction'
            - type: string
          title: Function
          description: The function that the model called.
      additionalProperties: false
      type: object
      required:
        - function
      title: ChatCompletionMessageToolCall
    LogProbs:
      additionalProperties: false
      description: Legacy log probabilities format
      properties:
        tokens:
          items:
            type: string
          title: Tokens
          type: array
        token_logprobs:
          items:
            type: number
          title: Token Logprobs
          type: array
        top_logprobs:
          anyOf:
            - items:
                additionalProperties:
                  type: number
                type: object
              type: array
            - type: 'null'
          title: Top Logprobs
        text_offset:
          items:
            type: integer
          title: Text Offset
          type: array
        token_ids:
          anyOf:
            - items:
                type: integer
              type: array
            - type: 'null'
          default: null
          title: Token Ids
      title: LogProbs
      type: object
    NewLogProbs:
      additionalProperties: false
      description: OpenAI-compatible log probabilities format
      properties:
        content:
          items:
            $ref: '#/components/schemas/NewLogProbsContent'
          title: Content
          type: array
      title: NewLogProbs
      type: object
    RawOutput:
      additionalProperties: false
      description: |-
        Extension of OpenAI that returns low-level interaction of what the model
        sees, including the formatted prompt and function calls
      properties:
        prompt_fragments:
          description: >-
            Pieces of the prompt (like individual messages) before truncation
            and concatenation. Depending on prompt_truncate_len some of the
            messages might be dropped. Contains a mix of strings to be tokenized
            and individual tokens (if dictated by the conversation template)
          items:
            anyOf:
              - type: string
              - type: integer
          title: Prompt Fragments
          type: array
        prompt_token_ids:
          description: Fully processed prompt as seen by the model
          items:
            type: integer
          title: Prompt Token Ids
          type: array
        completion:
          description: >-
            Raw completion produced by the model before any tool calls are
            parsed
          title: Completion
          type: string
        completion_token_ids:
          anyOf:
            - items:
                type: integer
              type: array
            - type: 'null'
          default: null
          description: Token IDs for the raw completion
          title: Completion Token Ids
        completion_logprobs:
          anyOf:
            - $ref: '#/components/schemas/NewLogProbs'
            - type: 'null'
          default: null
          description: >-
            Log probabilities for the completion. Only populated if logprobs is
            specified in the request
        images:
          anyOf:
            - type: array
              items:
                type: string
            - type: 'null'
          default: null
          description: Images in the prompt
          title: Images
        grammar:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: >-
            Grammar used for constrained decoding, can be either user provided
            (directly or JSON schema) or inferred by the chat template
          title: Grammar
      required:
        - prompt_fragments
        - prompt_token_ids
        - completion
      title: RawOutput
      type: object
    PromptTokensDetails:
      additionalProperties: false
      properties:
        cached_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          default: null
          title: Cached Tokens
      title: PromptTokensDetails
      type: object
    DeltaMessage:
      additionalProperties: false
      description: A message delta.
      properties:
        role:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: The role of the author of this message
          title: Role
        content:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: The contents of the chunk message
          title: Content
        reasoning_content:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          description: >-
            The reasoning or thinking process generated by the model. This field
            is only available for certain reasoning models (GLM 4.5, GLM 4.5
            Air, GPT OSS 120B, GPT OSS 20B) and contains the model's internal
            reasoning that would otherwise appear in `<think></think>` tags
            within the content field.
          title: Reasoning Content
        tool_calls:
          anyOf:
            - items:
                $ref: '#/components/schemas/ChatCompletionMessageToolCall'
              type: array
            - type: 'null'
          default: null
          title: Tool Calls
      title: DeltaMessage
      type: object
    ChatMessageContentImageURL:
      properties:
        url:
          type: string
          title: Url
        detail:
          anyOf:
            - type: string
            - type: 'null'
          title: Detail
      additionalProperties: false
      type: object
      required:
        - url
      title: ChatMessageContentImageURL
    ChatCompletionMessageToolCallFunction:
      properties:
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
          description: The name of the function to call.
        arguments:
          anyOf:
            - type: string
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Arguments
          description: >-
            The arguments to call the function with, as generated by the model
            in JSON format. Note that the model does not always generate valid
            JSON, and may hallucinate parameters not defined by your function
            schema. Validate the arguments in your code before calling your
            function.
      additionalProperties: false
      type: object
      title: ChatCompletionMessageToolCallFunction
    NewLogProbsContent:
      additionalProperties: false
      properties:
        token:
          title: Token
          type: string
        logprob:
          title: Logprob
          type: number
        sampling_logprob:
          anyOf:
            - type: number
            - type: 'null'
          title: Sampling Logprob
        bytes:
          items:
            type: integer
          title: Bytes
          type: array
        top_logprobs:
          items:
            $ref: '#/components/schemas/NewLogProbsContentTopLogProbs'
          title: Top Logprobs
          type: array
        token_id:
          title: Token Id
          type: integer
        text_offset:
          title: Text Offset
          type: integer
        last_activation:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          title: Last Activation
        routing_matrix:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          title: Routing Matrix
      required:
        - token
        - logprob
        - sampling_logprob
        - bytes
        - token_id
        - text_offset
      title: NewLogProbsContent
      type: object
    NewLogProbsContentTopLogProbs:
      additionalProperties: false
      properties:
        token:
          title: Token
          type: string
        logprob:
          title: Logprob
          type: number
        token_id:
          title: Token Id
          type: integer
        bytes:
          items:
            type: integer
          title: Bytes
          type: array
      required:
        - token
        - logprob
        - token_id
      title: NewLogProbsContentTopLogProbs
      type: object
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>

````