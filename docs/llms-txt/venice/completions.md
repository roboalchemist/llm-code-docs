# Source: https://docs.venice.ai/api-reference/endpoint/chat/completions.md

# Chat Completions

> Run text inference based on the supplied parameters. Long running requests should use the streaming API by setting stream=true in your request.

## OpenAPI

````yaml POST /chat/completions
paths:
  path: /chat/completions
  method: post
  servers:
    - url: https://api.venice.ai/api/v1
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
      header:
        Accept-Encoding:
          schema:
            - type: string
              required: false
              description: >-
                Supported compression encodings (gzip, br). Only applied when
                stream is false.
              example: gzip, br
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              frequency_penalty:
                allOf:
                  - type: number
                    maximum: 2
                    minimum: -2
                    default: 0
                    description: >-
                      Number between -2.0 and 2.0. Positive values penalize new
                      tokens based on their existing frequency in the text so
                      far, decreasing the model's likelihood to repeat the same
                      line verbatim.
              logprobs:
                allOf:
                  - type: boolean
                    description: >-
                      Whether to include log probabilities in the response. This
                      is not supported by all models.
                    example: true
              top_logprobs:
                allOf:
                  - type: integer
                    minimum: 0
                    description: >-
                      The number of highest probability tokens to return for
                      each token position.
                    example: 1
              max_completion_tokens:
                allOf:
                  - type: integer
                    description: >-
                      An upper bound for the number of tokens that can be
                      generated for a completion, including visible output
                      tokens and reasoning tokens.
              max_temp:
                allOf:
                  - type: number
                    minimum: 0
                    maximum: 2
                    description: Maximum temperature value for dynamic temperature scaling.
                    example: 1.5
              max_tokens:
                allOf:
                  - type: integer
                    description: >-
                      The maximum number of tokens that can be generated in the
                      chat completion. This value can be used to control costs
                      for text generated via API. This value is now deprecated
                      in favor of max_completion_tokens.
              messages:
                allOf:
                  - type: array
                    items:
                      anyOf:
                        - type: object
                          properties:
                            content:
                              anyOf:
                                - type: string
                                  title: String
                                - type: array
                                  items:
                                    oneOf:
                                      - type: object
                                        properties:
                                          text:
                                            type: string
                                            minLength: 1
                                            description: >-
                                              The prompt text of the message. Must be
                                              at-least one character in length
                                            example: Why is the sky blue?
                                            title: Text Content Object
                                          type:
                                            type: string
                                            enum:
                                              - text
                                            title: Text Content String
                                        required:
                                          - text
                                          - type
                                        additionalProperties: false
                                        description: Text message type.
                                        example:
                                          text: Why is the sky blue?
                                          type: text
                                        title: text
                                      - type: object
                                        properties:
                                          image_url:
                                            type: object
                                            properties:
                                              url:
                                                type: string
                                                description: >-
                                                  The URL of the image. Can be a data URL
                                                  with a base64 encoded image or a public
                                                  URL. URL must be publicly accessible.
                                                  Image must pass validation checks and be
                                                  >= 64 pixels square.
                                                format: uri
                                            required:
                                              - url
                                            description: >-
                                              Object containing the image URL
                                              information
                                            title: Image URL Object
                                          type:
                                            type: string
                                            enum:
                                              - image_url
                                        required:
                                          - image_url
                                          - type
                                        additionalProperties: false
                                        description: image_url message type.
                                        title: image_url
                                  title: Objects
                            role:
                              type: string
                              enum:
                                - user
                          required:
                            - content
                            - role
                          description: >-
                            The user message is the input from the user. It is
                            part of the conversation and is visible to the
                            assistant.
                          title: User Message
                        - type: object
                          properties:
                            content:
                              anyOf:
                                - type: string
                                  title: String
                                - type: array
                                  items:
                                    type: object
                                    properties:
                                      text:
                                        type: string
                                        minLength: 1
                                        description: >-
                                          The prompt text of the message. Must be
                                          at-least one character in length
                                        example: Why is the sky blue?
                                        title: Text Content Object
                                      type:
                                        type: string
                                        enum:
                                          - text
                                        title: Text Content String
                                    required:
                                      - text
                                      - type
                                    additionalProperties: false
                                    description: Text message type.
                                    example:
                                      text: Why is the sky blue?
                                      type: text
                                    title: text
                                  title: Objects
                                - nullable: true
                                  title: 'null'
                            name:
                              type: string
                            reasoning_content:
                              type: string
                              nullable: true
                            role:
                              type: string
                              enum:
                                - assistant
                            tool_calls:
                              type: array
                              nullable: true
                              items:
                                nullable: true
                          required:
                            - role
                          description: >-
                            The assistant message contains the response from the
                            LLM. Must have either content or tool_calls.
                          title: Assistant Message
                        - type: object
                          properties:
                            content:
                              type: string
                            name:
                              type: string
                            reasoning_content:
                              type: string
                              nullable: true
                            role:
                              type: string
                              enum:
                                - tool
                            tool_call_id:
                              type: string
                            tool_calls:
                              type: array
                              nullable: true
                              items:
                                nullable: true
                          required:
                            - content
                            - role
                            - tool_call_id
                          description: >-
                            The tool message is a special message that is used
                            to call a tool. It is not part of the conversation
                            and is not visible to the user.
                          title: Tool Message
                        - type: object
                          properties:
                            content:
                              anyOf:
                                - type: string
                                  title: String
                                - type: array
                                  items:
                                    type: object
                                    properties:
                                      text:
                                        type: string
                                        minLength: 1
                                        description: >-
                                          The prompt text of the message. Must be
                                          at-least one character in length
                                        example: Why is the sky blue?
                                        title: Text Content Object
                                      type:
                                        type: string
                                        enum:
                                          - text
                                        title: Text Content String
                                    required:
                                      - text
                                      - type
                                    additionalProperties: false
                                    description: Text message type.
                                    example:
                                      text: Why is the sky blue?
                                      type: text
                                    title: text
                                  title: Objects
                            name:
                              type: string
                            role:
                              type: string
                              enum:
                                - system
                          required:
                            - content
                            - role
                          description: >-
                            The system message is a special message that
                            provides context to the model. It is not part of the
                            conversation and is not visible to the user.
                          title: System Message
                    minItems: 1
                    description: >-
                      A list of messages comprising the conversation so far.
                      Depending on the model you use, different message types
                      (modalities) are supported, like text and images. For
                      compatibility purposes, the schema supports submitting
                      multiple image_url messages, however, only the last
                      image_url message will be passed to and processed by the
                      model.
              min_p:
                allOf:
                  - type: number
                    minimum: 0
                    maximum: 1
                    description: >-
                      Sets a minimum probability threshold for token selection.
                      Tokens with probabilities below this value are filtered
                      out.
                    example: 0.05
              min_temp:
                allOf:
                  - type: number
                    minimum: 0
                    maximum: 2
                    description: Minimum temperature value for dynamic temperature scaling.
                    example: 0.1
              model:
                allOf:
                  - type: string
                    description: >-
                      The ID of the model you wish to prompt. May also be a
                      model trait, or a model compatibility mapping. See the
                      models endpoint for a list of models available to you. You
                      can use feature suffixes to enable features from the
                      venice_parameters object. Please see "Model Feature
                      Suffix" documentation for more details.
                    example: zai-org-glm-4.6
              'n':
                allOf:
                  - type: integer
                    default: 1
                    description: >-
                      How many chat completion choices to generate for each
                      input message. Note that you will be charged based on the
                      number of generated tokens across all of the choices. Keep
                      n as 1 to minimize costs.
              presence_penalty:
                allOf:
                  - type: number
                    maximum: 2
                    minimum: -2
                    default: 0
                    description: >-
                      Number between -2.0 and 2.0. Positive values penalize new
                      tokens based on whether they appear in the text so far,
                      increasing the model's likelihood to talk about new
                      topics.
              repetition_penalty:
                allOf:
                  - type: number
                    minimum: 0
                    description: >-
                      The parameter for repetition penalty. 1.0 means no
                      penalty. Values > 1.0 discourage repetition.
                    example: 1.2
              seed:
                allOf:
                  - type: integer
                    minimum: 0
                    exclusiveMinimum: true
                    description: >-
                      The random seed used to generate the response. This is
                      useful for reproducibility.
                    example: 42
              stop:
                allOf:
                  - anyOf:
                      - type: string
                        title: String
                      - type: array
                        items:
                          type: string
                        minItems: 1
                        maxItems: 4
                        title: Array of Strings
                      - nullable: true
                        title: 'null'
                    description: >-
                      Up to 4 sequences where the API will stop generating
                      further tokens. Defaults to null.
              stop_token_ids:
                allOf:
                  - type: array
                    items:
                      type: number
                    description: >-
                      Array of token IDs where the API will stop generating
                      further tokens.
                    example:
                      - 151643
                      - 151645
              stream:
                allOf:
                  - type: boolean
                    description: >-
                      Whether to stream back partial progress. Defaults to
                      false.
                    example: true
              stream_options:
                allOf:
                  - type: object
                    properties:
                      include_usage:
                        type: boolean
                        description: Whether to include usage information in the stream.
              temperature:
                allOf:
                  - type: number
                    minimum: 0
                    maximum: 2
                    default: 0.7
                    description: >-
                      What sampling temperature to use, between 0 and 2. Higher
                      values like 0.8 will make the output more random, while
                      lower values like 0.2 will make it more focused and
                      deterministic. We generally recommend altering this or
                      top_p but not both.
                    example: 0.7
              top_k:
                allOf:
                  - type: integer
                    minimum: 0
                    description: >-
                      The number of highest probability vocabulary tokens to
                      keep for top-k-filtering.
                    example: 40
              top_p:
                allOf:
                  - type: number
                    minimum: 0
                    maximum: 1
                    default: 0.9
                    description: >-
                      An alternative to sampling with temperature, called
                      nucleus sampling, where the model considers the results of
                      the tokens with top_p probability mass. So 0.1 means only
                      the tokens comprising the top 10% probability mass are
                      considered.
                    example: 0.9
              user:
                allOf:
                  - type: string
                    description: >-
                      This field is discarded on the request but is supported in
                      the Venice API for compatibility with OpenAI clients.
              venice_parameters:
                allOf:
                  - type: object
                    properties:
                      character_slug:
                        type: string
                        description: >-
                          The character slug of a public Venice character.
                          Discoverable as the "Public ID" on the published
                          character page.
                      strip_thinking_response:
                        type: boolean
                        default: false
                        description: >-
                          Strip <think></think> blocks from the response.
                          Applicable only to reasoning / thinking models. Also
                          available to use as a model feature suffix. Defaults
                          to false.
                        example: false
                      disable_thinking:
                        type: boolean
                        default: false
                        description: >-
                          On supported reasoning models, will disable thinking
                          and strip the <think></think> blocks from the
                          response. Defaults to false.
                        example: false
                      enable_web_search:
                        type: string
                        enum:
                          - auto
                          - 'off'
                          - 'on'
                        default: 'off'
                        description: >-
                          Enable web search for this request. Defaults to off.
                          On will force web search on the request. Auto will
                          enable it based on the model's discretion. Citations
                          will be returned either in the first chunk of a
                          streaming result, or in the non streaming response.
                        example: 'off'
                      enable_web_scraping:
                        type: boolean
                        default: false
                        description: >-
                          Enable Venice web scraping of URLs in the latest user
                          message using Firecrawl. Off by default.
                        example: false
                      enable_web_citations:
                        type: boolean
                        default: false
                        description: >-
                          When web search is enabled, this will request that the
                          LLM cite its sources using a [REF]0[/REF] format.
                          Defaults to false.
                      include_search_results_in_stream:
                        type: boolean
                        default: false
                        description: >-
                          Experimental feature - When set to true, the LLM will
                          include search results in the stream as the first
                          emitted chunk. Defaults to false.
                      return_search_results_as_documents:
                        type: boolean
                        description: >-
                          When set, search results are also surfaced in an
                          OpenAI-compatible tool call named
                          "venice_web_search_documents" to ease LangChain
                          consumption.
                      include_venice_system_prompt:
                        type: boolean
                        default: true
                        description: >-
                          Whether to include the Venice supplied system prompts
                          along side specified system prompts. Defaults to true.
                    description: >-
                      Unique parameters to Venice's API implementation.
                      Customize these to control the behavior of the model.
              parallel_tool_calls:
                allOf:
                  - type: boolean
                    default: true
                    description: >-
                      Whether to enable parallel function calling during tool
                      use.
                    example: false
              response_format:
                allOf:
                  - oneOf:
                      - type: object
                        properties:
                          json_schema:
                            type: object
                            additionalProperties:
                              nullable: true
                          type:
                            type: string
                            enum:
                              - json_schema
                        required:
                          - json_schema
                          - type
                        additionalProperties: false
                        description: >-
                          The JSON Schema that should be used to validate and
                          format the response.
                        example:
                          json_schema:
                            properties:
                              age:
                                type: number
                              name:
                                type: string
                            required:
                              - name
                              - age
                            type: object
                          type: json_schema
                        title: json_schema
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - json_object
                        required:
                          - type
                        additionalProperties: false
                        description: >-
                          The response should be formatted as a JSON object.
                          This is a deprecated implementation and the preferred
                          use is json_schema.
                        title: json_object
                    description: Format in which the response should be returned.
              tool_choice:
                allOf:
                  - anyOf:
                      - type: object
                        properties:
                          function:
                            type: object
                            properties:
                              name:
                                type: string
                            required:
                              - name
                            additionalProperties: false
                          type:
                            type: string
                        required:
                          - function
                          - type
                        additionalProperties: false
                      - type: string
              tools:
                allOf:
                  - type: array
                    nullable: true
                    items:
                      type: object
                      properties:
                        function:
                          type: object
                          properties:
                            description:
                              type: string
                            name:
                              type: string
                            parameters:
                              type: object
                              additionalProperties:
                                nullable: true
                            strict:
                              type: boolean
                              default: false
                              description: >-
                                If set to true, the model will follow the exact
                                schema defined in the parameters field. Only a
                                subset of JSON Schema is supported when strict
                                is true.
                              example: false
                          required:
                            - name
                          additionalProperties: false
                        id:
                          type: string
                        type:
                          type: string
                      required:
                        - function
                      description: >-
                        A tool that can be called by the model. Currently, only
                        functions are supported as tools.
                      title: Tool Call
                    description: >-
                      A list of tools the model may call. Currently, only
                      functions are supported as a tool. Use this to provide a
                      list of functions the model may generate JSON inputs for.
            refIdentifier: '#/components/schemas/ChatCompletionRequest'
            requiredProperties:
              - messages
              - model
            additionalProperties: false
        examples:
          example:
            value:
              frequency_penalty: 0
              logprobs: true
              top_logprobs: 1
              max_completion_tokens: 123
              max_temp: 1.5
              max_tokens: 123
              messages:
                - content: <string>
                  role: user
              min_p: 0.05
              min_temp: 0.1
              model: zai-org-glm-4.6
              'n': 1
              presence_penalty: 0
              repetition_penalty: 1.2
              seed: 42
              stop: <string>
              stop_token_ids:
                - 151643
                - 151645
              stream: true
              stream_options:
                include_usage: true
              temperature: 0.7
              top_k: 40
              top_p: 0.9
              user: <string>
              venice_parameters:
                character_slug: <string>
                strip_thinking_response: false
                disable_thinking: false
                enable_web_search: 'off'
                enable_web_scraping: false
                enable_web_citations: false
                include_search_results_in_stream: false
                return_search_results_as_documents: true
                include_venice_system_prompt: true
              parallel_tool_calls: false
              response_format:
                json_schema:
                  properties:
                    age:
                      type: number
                    name:
                      type: string
                  required:
                    - name
                    - age
                  type: object
                type: json_schema
              tool_choice:
                function:
                  name: <string>
                type: <string>
              tools:
                - function:
                    description: <string>
                    name: <string>
                    parameters: {}
                    strict: false
                  id: <string>
                  type: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              choices:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        finish_reason:
                          type: string
                          enum:
                            - stop
                            - length
                          description: The reason the completion finished.
                          example: stop
                        index:
                          type: integer
                          description: The index of the choice in the list.
                          example: 0
                        logprobs:
                          type: object
                          nullable: true
                          properties:
                            bytes:
                              type: array
                              items:
                                type: number
                              description: Raw bytes of the token
                              example:
                                - 104
                                - 101
                                - 108
                                - 108
                                - 111
                            logprob:
                              type: number
                              description: The log probability of this token
                              example: -0.34
                            token:
                              type: string
                              description: The token string
                              example: hello
                            top_logprobs:
                              type: array
                              items:
                                type: object
                                properties:
                                  bytes:
                                    type: array
                                    items:
                                      type: number
                                  logprob:
                                    type: number
                                  token:
                                    type: string
                                required:
                                  - logprob
                                  - token
                              description: >-
                                Top tokens considered with their log
                                probabilities
                          required:
                            - logprob
                            - token
                        message:
                          anyOf:
                            - type: object
                              properties:
                                content:
                                  anyOf:
                                    - type: string
                                      title: String
                                    - type: array
                                      items:
                                        type: object
                                        properties:
                                          text:
                                            type: string
                                            minLength: 1
                                            description: >-
                                              The prompt text of the message. Must be
                                              at-least one character in length
                                            example: Why is the sky blue?
                                            title: Text Content Object
                                          type:
                                            type: string
                                            enum:
                                              - text
                                            title: Text Content String
                                        required:
                                          - text
                                          - type
                                        additionalProperties: false
                                        description: Text message type.
                                        example:
                                          text: Why is the sky blue?
                                          type: text
                                        title: text
                                      title: Objects
                                    - nullable: true
                                      title: 'null'
                                name:
                                  type: string
                                reasoning_content:
                                  type: string
                                  nullable: true
                                role:
                                  type: string
                                  enum:
                                    - assistant
                                tool_calls:
                                  type: array
                                  nullable: true
                                  items:
                                    nullable: true
                              required:
                                - role
                              description: >-
                                The assistant message contains the response from
                                the LLM. Must have either content or tool_calls.
                              title: Assistant Message
                            - type: object
                              properties:
                                content:
                                  type: string
                                name:
                                  type: string
                                reasoning_content:
                                  type: string
                                  nullable: true
                                role:
                                  type: string
                                  enum:
                                    - tool
                                tool_call_id:
                                  type: string
                                tool_calls:
                                  type: array
                                  nullable: true
                                  items:
                                    nullable: true
                              required:
                                - content
                                - role
                                - tool_call_id
                              description: >-
                                The tool message is a special message that is
                                used to call a tool. It is not part of the
                                conversation and is not visible to the user.
                              title: Tool Message
                        stop_reason:
                          type: string
                          nullable: true
                          enum:
                            - stop
                            - length
                          description: The reason the completion stopped.
                          example: stop
                      required:
                        - finish_reason
                        - index
                        - logprobs
                        - message
                    description: >-
                      A list of chat completion choices. Can be more than one if
                      n is greater than 1.
                    example:
                      - finish_reason: stop
                        index: 0
                        logprobs: null
                        message:
                          content: >-
                            The sky appears blue because of the way Earth's
                            atmosphere scatters sunlight. When sunlight reaches
                            Earth's atmosphere, it is made up of various colors
                            of the spectrum, but blue light waves are shorter
                            and scatter more easily when they hit the gases and
                            particles in the atmosphere. This scattering occurs
                            in all directions, but from our perspective on the
                            ground, it appears as a blue hue that dominates the
                            sky's color. This phenomenon is known as Rayleigh
                            scattering. During sunrise and sunset, the sunlight
                            has to travel further through the atmosphere, which
                            allows more time for the blue light to scatter away
                            from our direct line of sight, leaving the longer
                            wavelengths, such as red, yellow, and orange, to
                            dominate the sky's color.
                          reasoning_content: null
                          role: assistant
                          tool_calls: []
                        stop_reason: null
              created:
                allOf:
                  - type: integer
                    description: The time at which the request was created.
                    example: 1677858240
              id:
                allOf:
                  - type: string
                    description: The ID of the request.
                    example: chatcmpl-abc123
              model:
                allOf:
                  - type: string
                    description: The model id used for the request.
                    example: zai-org-glm-4.6
              object:
                allOf:
                  - type: string
                    enum:
                      - chat.completion
                    description: The type of the object returned.
                    example: chat.completion
              prompt_logprobs:
                allOf:
                  - anyOf:
                      - nullable: true
                        title: 'null'
                      - type: object
                        additionalProperties:
                          nullable: true
                      - nullable: true
                        title: 'null'
                    description: Log probability information for the prompt.
              usage:
                allOf:
                  - type: object
                    properties:
                      completion_tokens:
                        type: integer
                        description: The number of tokens in the completion.
                        example: 20
                      prompt_tokens:
                        type: integer
                        description: The number of tokens in the prompt.
                        example: 10
                      prompt_tokens_details:
                        type: object
                        nullable: true
                        properties: {}
                        description: >-
                          Breakdown of tokens used in the prompt. Not presently
                          used by Venice.
                      total_tokens:
                        type: integer
                        description: The total number of tokens used in the request.
                        example: 30
                    required:
                      - completion_tokens
                      - prompt_tokens
                      - total_tokens
              venice_parameters:
                allOf:
                  - type: object
                    properties:
                      enable_web_search:
                        type: string
                        enum:
                          - auto
                          - 'off'
                          - 'on'
                        description: Did the request enable web search?
                        example: auto
                      enable_web_citations:
                        type: boolean
                        description: Did the request enable web citations?
                        example: true
                      enable_web_scraping:
                        type: boolean
                        description: >-
                          Did the request enable web scraping of URLs via
                          Firecrawl?
                        example: false
                      include_venice_system_prompt:
                        type: boolean
                        description: Did the request include the Venice system prompt?
                        example: true
                      include_search_results_in_stream:
                        type: boolean
                        description: Did the request include search results in the stream?
                        example: false
                      return_search_results_as_documents:
                        type: boolean
                        description: >-
                          Did the request also return search results as a
                          tool-call documents block?
                        example: true
                      character_slug:
                        type: string
                        description: The character slug of a public Venice character.
                        example: venice
                      strip_thinking_response:
                        type: boolean
                        description: Did the request strip thinking response?
                        example: true
                      disable_thinking:
                        type: boolean
                        description: Did the request disable thinking?
                        example: true
                      web_search_citations:
                        type: array
                        items:
                          type: object
                          properties:
                            content:
                              type: string
                            date:
                              type: string
                            title:
                              type: string
                            url:
                              type: string
                          required:
                            - title
                            - url
                        description: Citations from web search results.
                        example:
                          - content: >-
                              What&#x27;s the scientific reason behind
                              Earth&#x27;s sky appearing blue to the human eye?
                              And what&#x27;s the real colour of the sky?


                              Save 30% on the shop price when you subscribe to
                              BBC Sky at Night Magazine today!


                              In this article we'll look at the science behind
                              why the sky is blue, or at least why it appears
                              blue to our eyes.


                              A beautiful blue sky is the sign of a pleasant day
                              ahead. But what makes the sky appear blue?


                              So, the sky appears blue because the molecules of
                              nitrogen and oxygen in the atmosphere scatter
                              light in short wavelengths towards the blue end of
                              the visible spectrum.
                            date: '2024-08-13T13:45:16.000Z'
                            title: Why is the sky blue? | BBC Sky at Night Magazine
                            url: >-
                              https://www.skyatnightmagazine.com/space-science/why-is-the-sky-blue
                          - content: >-
                              It was around 1870 when the British physicist John
                              William Strutt, better known as Lord Rayleigh,
                              first found an explanation for why the sky is
                              blue: Blue light from the Sun is scattered the
                              most when it passes through the atmosphere.


                              Published: January 20, 2025 8:34am EST · Daniel
                              Freedman, University of Wisconsin-Stout · Daniel
                              Freedman · Dean of the College of Science,
                              Technology, Engineering, Mathematics & Management,
                              University of Wisconsin-Stout ·


                              The answer has to do with molecules.


                              It was around 1870 when the British physicist John
                              William Strutt, better known as Lord Rayleigh,
                              first found an explanation for why the sky is
                              blue: Blue light from the Sun is scattered the
                              most when it passes through the atmosphere.


                              When the Sun is near the horizon, its light passes
                              through a lot more of the atmosphere to reach the
                              Earth’s surface than when it is directly overhead.
                              The blue and green light is scattered so well that
                              you can hardly see it. The sky is colored,
                              instead, with red and orange light.
                            date: '2025-04-16T16:55:11.000Z'
                            title: Why is the sky blue?
                            url: >-
                              https://theconversation.com/why-is-the-sky-blue-246393
                    required:
                      - enable_web_search
                      - enable_web_citations
                      - enable_web_scraping
                      - include_venice_system_prompt
                      - include_search_results_in_stream
                      - return_search_results_as_documents
                      - strip_thinking_response
                      - disable_thinking
                    description: Unique parameters to Venice's API implementation.
            requiredProperties:
              - choices
              - created
              - id
              - model
              - object
              - usage
            example:
              choices:
                - finish_reason: stop
                  index: 0
                  logprobs: null
                  message:
                    content: >-
                      The sky appears blue because of the way Earth's atmosphere
                      scatters sunlight. When sunlight reaches Earth's
                      atmosphere, it is made up of various colors of the
                      spectrum, but blue light waves are shorter and scatter
                      more easily when they hit the gases and particles in the
                      atmosphere. This scattering occurs in all directions, but
                      from our perspective on the ground, it appears as a blue
                      hue that dominates the sky's color. This phenomenon is
                      known as Rayleigh scattering. During sunrise and sunset,
                      the sunlight has to travel further through the atmosphere,
                      which allows more time for the blue light to scatter away
                      from our direct line of sight, leaving the longer
                      wavelengths, such as red, yellow, and orange, to dominate
                      the sky's color.
                    reasoning_content: null
                    role: assistant
                    tool_calls: []
                  stop_reason: null
              created: 1739928524
              id: chatcmpl-a81fbc2d81a7a083bb83ccf9f44c6e5e
              model: qwen-2.5-vl
              object: chat.completion
              prompt_logprobs: null
              usage:
                completion_tokens: 146
                prompt_tokens: 612
                prompt_tokens_details: null
                total_tokens: 758
              venice_parameters:
                include_venice_system_prompt: true
                include_search_results_in_stream: false
                return_search_results_as_documents: false
                web_search_citations: []
                enable_web_search: auto
                enable_web_scraping: false
                enable_web_citations: true
                strip_thinking_response: true
                disable_thinking: true
                character_slug: venice
        examples:
          example:
            value:
              choices:
                - finish_reason: stop
                  index: 0
                  logprobs: null
                  message:
                    content: >-
                      The sky appears blue because of the way Earth's atmosphere
                      scatters sunlight. When sunlight reaches Earth's
                      atmosphere, it is made up of various colors of the
                      spectrum, but blue light waves are shorter and scatter
                      more easily when they hit the gases and particles in the
                      atmosphere. This scattering occurs in all directions, but
                      from our perspective on the ground, it appears as a blue
                      hue that dominates the sky's color. This phenomenon is
                      known as Rayleigh scattering. During sunrise and sunset,
                      the sunlight has to travel further through the atmosphere,
                      which allows more time for the blue light to scatter away
                      from our direct line of sight, leaving the longer
                      wavelengths, such as red, yellow, and orange, to dominate
                      the sky's color.
                    reasoning_content: null
                    role: assistant
                    tool_calls: []
                  stop_reason: null
              created: 1739928524
              id: chatcmpl-a81fbc2d81a7a083bb83ccf9f44c6e5e
              model: qwen-2.5-vl
              object: chat.completion
              prompt_logprobs: null
              usage:
                completion_tokens: 146
                prompt_tokens: 612
                prompt_tokens_details: null
                total_tokens: 758
              venice_parameters:
                include_venice_system_prompt: true
                include_search_results_in_stream: false
                return_search_results_as_documents: false
                web_search_citations: []
                enable_web_search: auto
                enable_web_scraping: false
                enable_web_citations: true
                strip_thinking_response: true
                disable_thinking: true
                character_slug: venice
        description: OK
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              details:
                allOf:
                  - type: object
                    properties: {}
                    description: Details about the incorrect input
                    example:
                      _errors: []
                      field:
                        _errors:
                          - Field is required
              error:
                allOf:
                  - type: string
                    description: A description of the error
            refIdentifier: '#/components/schemas/DetailedError'
            requiredProperties:
              - error
        examples:
          example:
            value:
              details:
                _errors: []
                field:
                  _errors:
                    - Field is required
              error: <string>
        description: Invalid request parameters
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: string
                    description: A description of the error
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: &ref_1
              - error
        examples:
          example:
            value:
              error: <string>
        description: Authentication failed
    '402':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: Insufficient USD or Diem balance to complete request
    '415':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: Invalid request content-type
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: Rate limit exceeded
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: Inference processing failed
    '503':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: The model is at capacity. Please try again later.
    '504':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: >-
          The request took too long to complete and was timed-out. For
          long-running inference requests, use the streaming API by setting
          stream=true in your request.
  deprecated: false
  type: path
components:
  schemas: {}

````