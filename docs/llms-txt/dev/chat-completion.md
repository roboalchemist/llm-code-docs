# Source: https://dev.writer.com/home/chat-completion.md

# Source: https://dev.writer.com/api-reference/completion-api/chat-completion.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Chat completion

> Generate a chat completion based on the provided messages. The response shown below is for non-streaming. To learn about streaming responses, see the [chat completion guide](https://dev.writer.com/home/chat-completion).



## OpenAPI

````yaml post /v1/chat
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/chat:
    post:
      tags:
        - Generation API
      summary: Chat completion
      description: >-
        Generate a chat completion based on the provided messages. The response
        shown below is for non-streaming. To learn about streaming responses,
        see the [chat completion
        guide](https://dev.writer.com/home/chat-completion).
      operationId: chat
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/chat_request'
        required: true
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/chat_response'
                example:
                  id: 57e4f58f-f7b1-41d8-be17-a6279c073aad
                  object: chat.completion
                  choices:
                    - index: 0
                      finish_reason: stop
                      message:
                        content: The earnings report shows...
                        role: assistant
                        refusal: null
                        tool_calls: []
                        graph_data:
                          sources: []
                          status: finished
                          subqueries: []
                        llm_data:
                          prompt: Write a memo summarizing this earnings report.
                          model: palmyra-x5
                        translation_data: null
                        web_search_data: null
                  created: 1715361795
                  model: palmyra-x5
                  usage:
                    prompt_tokens: 40
                    total_tokens: 340
                    completion_tokens: 300
                    prompt_token_details:
                      cached_tokens: 0
                    completion_token_details:
                      reasoning_tokens: 0
                  system_fingerprint: v1
                  service_tier: standard
            text/event-stream:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/chat_completion_chunk'
              examples:
                '200':
                  value:
                    id: 57e4f58f-f7b1-41d8-be17-a6279c073aad
                    object: chat.completion
                    choices:
                      - index: 0
                        finish_reason: length
                        message:
                          content: The earnings report shows...
                          role: assistant
                          tool_calls: []
                          refusal: null
                          graph_data:
                            sources: []
                            status: finished
                            subqueries: []
                          llm_data:
                            prompt: Write a memo summarizing this earnings report.
                            model: palmyra-x5
                          translation_data: null
                          web_search_data: null
                        delta:
                          content: The earnings report shows...
                          role: assistant
                          tool_calls: []
                          refusal: null
                          graph_data:
                            sources: []
                            status: finished
                            subqueries: []
                          llm_data:
                            prompt: Write a memo summarizing this earnings report.
                            model: palmyra-x5
                          translation_data: null
                          web_search_data: null
                    created: 1715361795
                    model: palmyra-x5
                    usage:
                      prompt_tokens: 40
                      total_tokens: 340
                      completion_tokens: 300
                      prompt_token_details:
                        cached_tokens: 0
                      completion_token_details:
                        reasoning_tokens: 0
                    system_fingerprint: v1
                    service_tier: standard
      security:
        - bearerAuth: []
components:
  schemas:
    chat_request:
      required:
        - model
        - messages
      type: object
      properties:
        model:
          type: string
          description: >-
            The [ID of the model](https://dev.writer.com/home/models) to use for
            creating the chat completion. Supports `palmyra-x5`, `palmyra-x4`,
            `palmyra-fin`, `palmyra-med`, `palmyra-creative`, and
            `palmyra-x-003-instruct`.
        messages:
          type: array
          items:
            $ref: '#/components/schemas/chat_message'
          minItems: 1
          description: >-
            An array of message objects that form the conversation history or
            context for the model to respond to. The array must contain at least
            one message.
        max_tokens:
          type: integer
          format: int32
          description: >-
            Defines the maximum number of tokens (words and characters) that the
            model can generate in the response. This can be adjusted to allow
            for longer or shorter responses as needed. The maximum value varies
            by model. See the [models overview](/home/models) for more
            information about the maximum number of tokens for each model.
        temperature:
          type: number
          format: double
          default: 1
          description: >-
            Controls the randomness or creativity of the model's responses. A
            higher temperature results in more varied and less predictable text,
            while a lower temperature produces more deterministic and
            conservative outputs.
        top_p:
          type: number
          format: double
          description: >-
            Sets the threshold for "nucleus sampling," a technique to focus the
            model's token generation on the most likely subset of tokens. Only
            tokens with cumulative probability above this threshold are
            considered, controlling the trade-off between creativity and
            coherence.
        'n':
          type: integer
          format: int32
          description: >-
            Specifies the number of completions (responses) to generate from the
            model in a single request. This parameter allows for generating
            multiple responses, offering a variety of potential replies from
            which to choose.
        stop:
          oneOf:
            - type: array
              items:
                type: string
            - type: string
          description: >-
            A token or sequence of tokens that, when generated, will cause the
            model to stop producing further content. This can be a single token
            or an array of tokens, acting as a signal to end the output.
        logprobs:
          type: boolean
          default: 'false'
          description: Specifies whether to return log probabilities of the output tokens.
        stream:
          type: boolean
          description: >-
            Indicates whether the response should be streamed incrementally as
            it is generated or only returned once fully complete. Streaming can
            be useful for providing real-time feedback in interactive
            applications.
          default: false
        tools:
          type: array
          description: >-
            An array containing tool definitions for tools that the model can
            use to generate responses. The tool definitions use JSON schema. You
            can define your own functions or use one of the built-in `graph`,
            `llm`, `translation`, or `vision` tools. Note that you can only use
            one built-in tool type in the array (only one of `graph`, `llm`,
            `translation`, or `vision`). You can pass multiple [custom
            tools](https://dev.writer.com/home/tool-calling) of type `function`
            in the same request.
          items:
            $ref: '#/components/schemas/tool'
            minItems: 1
        tool_choice:
          $ref: '#/components/schemas/tool_choice'
        stream_options:
          $ref: '#/components/schemas/stream_options'
        response_format:
          $ref: '#/components/schemas/response_format'
      example:
        model: palmyra-x5
        messages:
          - content: Write a memo summarizing this earnings report.
            role: user
    chat_response:
      required:
        - id
        - object
        - choices
        - created
        - model
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: >-
            A globally unique identifier (UUID) for the response generated by
            the API. This ID can be used to reference the specific operation or
            transaction within the system for tracking or debugging purposes.
        object:
          type: string
          description: >-
            The type of object returned, which is always `chat.completion` for
            chat responses.
          enum:
            - chat.completion
        choices:
          type: array
          items:
            $ref: '#/components/schemas/chat_completion_choice'
          minItems: 1
          description: >-
            An array of objects representing the different outcomes or results
            produced by the model based on the input provided.
        created:
          type: integer
          format: int64
          description: >-
            The Unix timestamp (in seconds) when the response was created. This
            timestamp can be used to verify the timing of the response relative
            to other events or operations.
        model:
          type: string
          description: Identifies the specific model used to generate the response.
        usage:
          $ref: '#/components/schemas/chat_completion_usage'
        system_fingerprint:
          type: string
          description: >-
            A string representing the backend configuration that the model runs
            with.
        service_tier:
          type: string
          description: The service tier used for processing the request.
      example:
        id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
        choices:
          - finish_reason: stop
            message:
              content: Hello! How can I assist you today?
              role: user
        created: 1678587532773
        model: palmyra-x5
    chat_completion_chunk:
      required:
        - id
        - object
        - created
        - choices
        - model
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: >-
            A globally unique identifier (UUID) for the response generated by
            the API. This ID can be used to reference the specific operation or
            transaction within the system for tracking or debugging purposes.
        object:
          type: string
          description: >-
            The type of object returned, which is always `chat.completion.chunk`
            for streaming chat responses.
          enum:
            - chat.completion.chunk
        choices:
          type: array
          items:
            $ref: '#/components/schemas/chat_completion_streaming_choice'
          minItems: 1
          description: >-
            An array of objects representing the different outcomes or results
            produced by the model based on the input provided.
        created:
          type: integer
          format: int64
          description: >-
            The Unix timestamp (in seconds) when the response was created. This
            timestamp can be used to verify the timing of the response relative
            to other events or operations.
        model:
          type: string
          description: Identifies the specific model used to generate the response.
        usage:
          $ref: '#/components/schemas/chat_completion_usage'
        system_fingerprint:
          type: string
        service_tier:
          type: string
      example:
        id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
        choices:
          - finish_reason: stop
            message:
              content: Hello! How can I assist you today?
              role: user
        created: 1678587532773
        model: palmyra-x5
    chat_message:
      title: chat_message
      required:
        - role
      type: object
      properties:
        content:
          description: >-
            The content of the message. Can be either a string (for text-only
            messages) or an array of content fragments (for mixed text and image
            messages).
          nullable: true
          oneOf:
            - type: string
              title: TextContent
            - type: array
              title: MixedContent
              items:
                $ref: '#/components/schemas/composite_content'
              minItems: 1
        role:
          $ref: '#/components/schemas/chat_message_request_role'
        name:
          type: string
          description: >-
            An optional name for the message sender. Useful for identifying
            different users, personas, or tools in multi-participant
            conversations.
          nullable: true
        tool_call_id:
          type: string
          nullable: true
        tool_calls:
          type: array
          items:
            $ref: '#/components/schemas/tool_call'
          nullable: true
          minItems: 1
        graph_data:
          $ref: '#/components/schemas/graph_data'
          nullable: true
        refusal:
          type: string
          nullable: true
    tool:
      type: object
      discriminator:
        propertyName: type
        mapping:
          function: '#/components/schemas/function_tool'
          graph: '#/components/schemas/graph_tool'
          llm: '#/components/schemas/llm_tool'
          translation: '#/components/schemas/translation_tool'
          vision: '#/components/schemas/vision_tool'
          web_search: '#/components/schemas/web_search_tool'
      oneOf:
        - $ref: '#/components/schemas/function_tool'
        - $ref: '#/components/schemas/graph_tool'
        - $ref: '#/components/schemas/llm_tool'
        - $ref: '#/components/schemas/translation_tool'
        - $ref: '#/components/schemas/vision_tool'
        - $ref: '#/components/schemas/web_search_tool'
    tool_choice:
      description: >-
        Configure how the model will call functions:

        - `auto`: allows the model to automatically choose the tool to use, or
        not call a tool

        - `none`: disables tool calling; the model will instead generate a
        message

        - `required`: requires the model to call one or more tools


        You can also use a JSON object to force the model to call a specific
        tool. For example, `{"type": "function", "function": {"name":
        "get_current_weather"}}` requires the model to call the
        `get_current_weather` function, regardless of the prompt.
      oneOf:
        - $ref: '#/components/schemas/string_tool_choice'
        - $ref: '#/components/schemas/json_object_tool_choice'
    stream_options:
      title: stream_options
      description: Additional options for streaming.
      required:
        - include_usage
      type: object
      properties:
        include_usage:
          type: boolean
          description: Indicate whether to include usage information.
    response_format:
      title: response_format
      description: >-
        The response format to use for the chat completion, available with
        `palmyra-x4` and `palmyra-x5`.


        `text` is the default response format. [JSON
        Schema](https://json-schema.org/) is supported for structured responses.
        If you specify `json_schema`, you must also provide a `json_schema`
        object.
      required:
        - type
      type: object
      properties:
        type:
          type: string
          description: The type of response format to use.
          enum:
            - text
            - json_schema
        json_schema:
          type: object
          description: The JSON schema to use for the response format.
    chat_completion_choice:
      required:
        - index
        - finish_reason
        - message
      type: object
      properties:
        index:
          type: integer
          format: int32
          description: >-
            The index of the choice in the list of completions generated by the
            model.
        finish_reason:
          $ref: '#/components/schemas/chat_completion_finish_reason'
          description: >-
            Describes the condition under which the model ceased generating
            content. Common reasons include 'length' (reached the maximum output
            size), 'stop' (encountered a stop sequence), 'content_filter'
            (harmful content filtered out), or 'tool_calls' (encountered tool
            calls).
        message:
          $ref: '#/components/schemas/chat_completion_response_message'
        logprobs:
          $ref: '#/components/schemas/logprobs'
          description: Log probability information for the choice.
    chat_completion_usage:
      title: chat_completion_usage
      description: >-
        Usage information for the chat completion response. Please note that at
        this time Knowledge Graph tool usage is not included in this object.
      required:
        - prompt_tokens
        - total_tokens
        - completion_tokens
      type: object
      properties:
        prompt_tokens:
          type: integer
          format: int32
        total_tokens:
          type: integer
          format: int32
        completion_tokens:
          type: integer
          format: int32
        prompt_token_details:
          $ref: '#/components/schemas/prompt_token_details'
        completion_tokens_details:
          $ref: '#/components/schemas/completion_token_details'
    chat_completion_streaming_choice:
      required:
        - index
        - finish_reason
        - delta
      type: object
      properties:
        index:
          type: integer
          format: int32
          description: >-
            The index of the choice in the list of completions generated by the
            model.
        finish_reason:
          $ref: '#/components/schemas/chat_completion_finish_reason'
          description: >-
            Describes the condition under which the model ceased generating
            content. Common reasons include 'length' (reached the maximum output
            size), 'stop' (encountered a stop sequence), 'content_filter'
            (harmful content filtered out), or 'tool_calls' (encountered tool
            calls).
          nullable: true
        message:
          $ref: '#/components/schemas/chat_completion_response_message'
        delta:
          $ref: '#/components/schemas/chat_completion_streaming_delta'
          description: A chat completion delta generated by streamed model responses.
        logprobs:
          $ref: '#/components/schemas/logprobs'
          description: Log probability information for the choice.
    composite_content:
      title: composite_content
      description: >-
        A union type that can contain either text or image content fragments.
        This enables chat messages to include mixed content types, allowing
        users to send both text and images in a single message. Note: Image
        fragments are only supported with the Palmyra X5 model.
      oneOf:
        - $ref: '#/components/schemas/text_fragment'
        - $ref: '#/components/schemas/image_fragment'
    chat_message_request_role:
      type: string
      description: >-
        The role of the chat message. You can provide a system prompt by setting
        the role to `system`, or specify that a message is the result of a [tool
        call](https://dev.writer.com/home/tool-calling) by setting the role to
        `tool`.
      enum:
        - user
        - assistant
        - system
        - tool
    tool_call:
      title: tool_call
      type: object
      required:
        - id
        - type
        - function
      properties:
        index:
          type: integer
          format: int32
        id:
          type: string
        type:
          type: string
          enum:
            - function
        function:
          $ref: '#/components/schemas/function'
    graph_data:
      title: graph_data
      type: object
      properties:
        sources:
          type: array
          items:
            $ref: '#/components/schemas/source'
        status:
          $ref: '#/components/schemas/graph_stage_status'
        subqueries:
          type: array
          items:
            $ref: '#/components/schemas/sub_query'
        references:
          $ref: '#/components/schemas/references'
    function_tool:
      title: Function tool
      required:
        - function
        - type
      type: object
      properties:
        type:
          type: string
          description: The type of tool.
          enum:
            - function
        function:
          $ref: '#/components/schemas/tool_function'
    graph_tool:
      title: Graph tool
      required:
        - function
        - type
      type: object
      properties:
        type:
          type: string
          description: The type of tool.
          enum:
            - graph
        function:
          $ref: '#/components/schemas/graph_function'
    llm_tool:
      title: LLM tool
      required:
        - function
        - type
      type: object
      properties:
        type:
          type: string
          description: The type of tool.
          enum:
            - llm
        function:
          $ref: '#/components/schemas/llm_function'
    translation_tool:
      title: Translation tool
      description: >-
        A tool that uses Palmyra Translate to translate text. Note that this
        tool does not stream results. The response is returned after the
        translation is complete.
      required:
        - function
        - type
      type: object
      properties:
        type:
          type: string
          description: The type of tool.
          enum:
            - translation
        function:
          $ref: '#/components/schemas/translation_function'
    vision_tool:
      title: Vision tool
      required:
        - function
        - type
      type: object
      properties:
        type:
          type: string
          description: The type of tool.
          enum:
            - vision
        function:
          $ref: '#/components/schemas/vision_function'
    web_search_tool:
      title: Web search tool
      required:
        - function
        - type
      type: object
      properties:
        type:
          type: string
          description: The type of tool.
          enum:
            - web_search
        function:
          $ref: '#/components/schemas/web_search_function'
    string_tool_choice:
      title: String
      required:
        - value
      type: object
      properties:
        value:
          $ref: '#/components/schemas/string_tool_choice_options'
    json_object_tool_choice:
      title: JSON object
      required:
        - value
      type: object
      properties:
        value:
          type: object
          description: >-
            A JSON object that specifies the tool to call. For example,
            `{"type": "function", "function": {"name": "get_current_weather"}}`
          additionalProperties: true
    chat_completion_finish_reason:
      type: string
      enum:
        - stop
        - length
        - content_filter
        - tool_calls
    chat_completion_response_message:
      required:
        - content
        - role
        - refusal
      type: object
      description: >-
        The chat completion message from the model. Note: this field is
        deprecated for streaming. Use `delta` instead.
      properties:
        content:
          type: string
          description: >-
            The text content produced by the model. This field contains the
            actual output generated, reflecting the model's response to the
            input query or command.
        role:
          type: string
          enum:
            - assistant
          description: Specifies the role associated with the content.
        tool_calls:
          type: array
          items:
            $ref: '#/components/schemas/tool_call'
          minItems: 1
        graph_data:
          $ref: '#/components/schemas/graph_data'
        llm_data:
          $ref: '#/components/schemas/llm_data'
        translation_data:
          $ref: '#/components/schemas/translation_data'
        web_search_data:
          $ref: '#/components/schemas/web_search_data'
        refusal:
          type: string
          nullable: true
    logprobs:
      type: object
      required:
        - content
        - refusal
      nullable: true
      properties:
        content:
          type: array
          items:
            $ref: '#/components/schemas/logprobs_token'
          nullable: true
        refusal:
          type: array
          items:
            $ref: '#/components/schemas/logprobs_token'
          nullable: true
    prompt_token_details:
      title: prompt_token_details
      required:
        - cached_tokens
      type: object
      properties:
        cached_tokens:
          type: integer
          format: int32
    completion_token_details:
      title: completion_token_details
      required:
        - reasoning_tokens
      type: object
      properties:
        reasoning_tokens:
          type: integer
          format: int32
    chat_completion_streaming_delta:
      type: object
      description: >-
        The chat completion message from the model. Note: this field is
        deprecated for streaming. Use `delta` instead.
      properties:
        content:
          type: string
          description: >-
            The text content produced by the model. This field contains the
            actual output generated, reflecting the model's response to the
            input query or command.
        role:
          $ref: '#/components/schemas/chat_message_role'
          description: >-
            Specifies the role associated with the content, indicating whether
            the message is from the 'assistant' or another defined role, helping
            to contextualize the output within the interaction flow.
        tool_calls:
          type: array
          items:
            $ref: '#/components/schemas/tool_call_streaming'
          minItems: 1
        graph_data:
          $ref: '#/components/schemas/graph_data'
        llm_data:
          $ref: '#/components/schemas/llm_data'
        translation_data:
          $ref: '#/components/schemas/translation_data'
        refusal:
          type: string
          nullable: true
    text_fragment:
      title: Text
      description: Represents a text content fragment within a chat message.
      required:
        - type
        - text
      type: object
      properties:
        type:
          type: string
          description: The type of content fragment. Must be `text` for text fragments.
          enum:
            - text
        text:
          type: string
          description: The actual text content of the message fragment.
    image_fragment:
      title: Image
      description: >-
        Represents an image content fragment within a chat message. Note: This
        content type is only supported with the Palmyra X5 model.
      required:
        - type
        - image_url
      type: object
      properties:
        type:
          type: string
          description: >-
            The type of content fragment. Must be `image_url` for image
            fragments.
          enum:
            - image_url
        image_url:
          type: object
          description: The image URL object containing the location of the image.
          required:
            - url
          properties:
            url:
              type: string
              description: >-
                The URL pointing to the image file. Supports common image
                formats like JPEG, PNG, GIF, etc.
    function:
      title: function
      type: object
      required:
        - name
        - arguments
      properties:
        name:
          type: string
        arguments:
          type: string
    source:
      title: source
      description: >-
        A source snippet containing text and fileId from Knowledge Graph
        content.
      required:
        - file_id
        - snippet
      type: object
      nullable: true
      properties:
        file_id:
          type: string
          description: The unique identifier of the file in your Writer account.
        snippet:
          type: string
          description: >-
            The exact text snippet from the source document that was used to
            support the response.
    graph_stage_status:
      title: graph_stage_status
      type: string
      nullable: true
      enum:
        - processing
        - finished
    sub_query:
      title: sub_query
      description: >-
        A sub-question generated to break down complex queries into more
        manageable parts, along with its answer and supporting sources.
      required:
        - query
        - answer
        - sources
      type: object
      nullable: true
      properties:
        query:
          type: string
          description: The subquery that was generated to help answer the main question.
        answer:
          type: string
          description: The answer to the subquery based on Knowledge Graph content.
        sources:
          type: array
          description: Array of source snippets that were used to answer this subquery.
          items:
            $ref: '#/components/schemas/source'
    references:
      title: references
      description: >-
        Detailed source information organized by reference type, providing
        comprehensive metadata about the sources used to generate the response.
      type: object
      properties:
        files:
          type: array
          description: >-
            Array of file-based references from uploaded documents in the
            Knowledge Graph.
          items:
            $ref: '#/components/schemas/file'
          minItems: 1
        web:
          type: array
          description: >-
            Array of web-based references from online sources accessed during
            the query.
          items:
            $ref: '#/components/schemas/web'
          minItems: 1
    tool_function:
      title: tool_function
      description: A tool that uses a custom function.
      required:
        - name
      type: object
      properties:
        description:
          type: string
          description: Description of the function.
        name:
          type: string
          description: Name of the function.
        parameters:
          type: object
          additionalProperties: true
          description: The parameters of the function.
    graph_function:
      title: graph_function
      description: A tool that uses Knowledge Graphs as context for responses.
      required:
        - graph_ids
        - subqueries
      type: object
      properties:
        description:
          type: string
          description: A description of the graph content.
        graph_ids:
          type: array
          description: An array of graph IDs to use in the tool.
          items:
            type: string
            format: uuid
          minItems: 1
        subqueries:
          type: boolean
          description: Boolean to indicate whether to include subqueries in the response.
        query_config:
          $ref: '#/components/schemas/graph_query_config'
          description: >-
            Configuration options for Knowledge Graph queries, including search
            parameters and citation settings.
    llm_function:
      title: LLM function
      description: A tool that uses another Writer model to generate a response.
      required:
        - description
        - model
      type: object
      properties:
        description:
          type: string
          description: A description of the model to use.
        model:
          type: string
          description: The model to use.
    translation_function:
      title: Translation function
      description: A tool that uses Palmyra Translate to translate text.
      required:
        - model
        - formality
        - length_control
        - mask_profanity
      type: object
      properties:
        model:
          type: string
          description: The model to use for translation.
          enum:
            - palmyra-translate
        source_language_code:
          type: string
          description: >-
            Optional. The
            [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
            language code of the original text to translate. For example, `en`
            for English, `zh` for Chinese, `fr` for French, `es` for Spanish. If
            the language has a variant, the code appends the two-digit [ISO-3166
            country
            code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
            If you do not provide a language code, the LLM detects the language
            of the text.
        target_language_code:
          type: string
          description: >-
            Optional. The
            [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
            language code of the target language for the translation. For
            example, `en` for English, `zh` for Chinese, `fr` for French, `es`
            for Spanish. If the language has a variant, the code appends the
            two-digit [ISO-3166 country
            code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
            If you do not provide a language code, the LLM uses the content of
            the chat message to determine the target language.
        formality:
          type: boolean
          description: >-
            Whether to use formal or informal language in the translation. See
            the [list of languages that support
            formality](https://dev.writer.com/api-reference/translation-api/language-support#formality).
            If the language does not support formality, this parameter is
            ignored.
        length_control:
          type: boolean
          description: >-
            Whether to control the length of the translated text. See the [list
            of languages that support length
            control](https://dev.writer.com/api-reference/translation-api/language-support#length-control).
            If the language does not support length control, this parameter is
            ignored.
        mask_profanity:
          type: boolean
          description: >-
            Whether to mask profane words in the translated text. See the [list
            of languages that do not support profanity
            masking](https://dev.writer.com/api-reference/translation-api/language-support#profanity-masking).
            If the language does not support profanity masking, this parameter
            is ignored.
    vision_function:
      title: Vision function
      description: >-
        A tool that uses Palmyra Vision to analyze images and documents.
        Supports JPG, PNG, PDF, and TXT files up to 7MB each.
      required:
        - model
        - variables
      type: object
      properties:
        variables:
          type: array
          items:
            $ref: '#/components/schemas/vision_tool_request_file_variable'
        model:
          type: string
          description: The model to use for image analysis.
          enum:
            - palmyra-vision
    web_search_function:
      title: web_search_function
      description: A tool that uses web search to find information.
      required:
        - exclude_domains
        - include_domains
      type: object
      properties:
        exclude_domains:
          type: array
          description: An array of domains to exclude from the search results.
          items:
            type: string
        include_domains:
          type: array
          description: An array of domains to include in the search results.
          items:
            type: string
    string_tool_choice_options:
      title: string_tool_choice_options
      type: string
      enum:
        - none
        - auto
        - required
    llm_data:
      title: llm_data
      required:
        - prompt
        - model
      type: object
      nullable: true
      properties:
        prompt:
          type: string
          description: The prompt processed by the model.
        model:
          type: string
          description: The model used by the tool.
    translation_data:
      title: translation_data
      required:
        - source_text
        - source_language_code
        - target_language_code
      type: object
      properties:
        source_text:
          type: string
          description: The text the tool translated.
        source_language_code:
          type: string
          description: The language code of the source text.
        target_language_code:
          type: string
          description: The language code of the target text.
    web_search_data:
      title: web_search_data
      required:
        - sources
      type: object
      properties:
        sources:
          type: array
          items:
            type: object
            properties:
              url:
                type: string
              raw_content:
                type: string
    logprobs_token:
      title: logprobs_token
      required:
        - token
        - logprob
        - top_logprobs
      type: object
      properties:
        token:
          type: string
        logprob:
          type: number
          format: double
        bytes:
          type: array
          items:
            type: integer
            format: int32
        top_logprobs:
          type: array
          items:
            $ref: '#/components/schemas/top_log_prob'
    chat_message_role:
      type: string
      enum:
        - user
        - assistant
        - system
    tool_call_streaming:
      title: tool_call
      type: object
      required:
        - index
      properties:
        index:
          type: integer
          format: int32
        id:
          type: string
        type:
          type: string
          enum:
            - function
        function:
          $ref: '#/components/schemas/function'
    file:
      title: file
      description: >-
        A file-based reference containing text snippets from uploaded documents
        in the Knowledge Graph.
      required:
        - text
        - fileId
        - score
      type: object
      properties:
        text:
          type: string
          description: >-
            The exact text snippet from the source document that was used to
            support the response.
        fileId:
          type: string
          description: The unique identifier of the file in your Writer account.
        score:
          type: number
          description: >-
            Internal score used during the retrieval process for ranking and
            selecting relevant snippets.
        page:
          type: integer
          format: int32
          description: Page number where this snippet was found in the source document.
        cite:
          type: string
          description: >-
            Unique citation ID that appears in inline citations within the
            response text (null if not cited).
    web:
      title: web
      description: >-
        A web-based reference containing text snippets from online sources
        accessed during the query.
      required:
        - text
        - url
        - title
        - score
      type: object
      properties:
        text:
          type: string
          description: >-
            The exact text snippet from the web source that was used to support
            the response.
        url:
          type: string
          description: The URL of the web page where this content was found.
          format: uri
        title:
          type: string
          description: The title of the web page where this content was found.
        score:
          type: number
          description: >-
            Internal score used during the retrieval process for ranking and
            selecting relevant snippets.
    graph_query_config:
      title: graph_query_config
      description: Configuration options for Knowledge Graph queries.
      type: object
      properties:
        max_subquestions:
          type: integer
          format: int32
          minimum: 1
          maximum: 10
          default: 6
          description: >-
            Maximum number of subquestions to generate when processing complex
            queries. Set higher to improve detail, set lower to reduce response
            time. Range: 1-10, Default: 6.
        search_weight:
          type: integer
          format: int32
          minimum: 0
          maximum: 100
          default: 50
          description: >-
            Weight given to search results when ranking and selecting relevant
            information. Higher values (closer to 100) prioritize keyword-based
            matching, while lower values (closer to 0) prioritize semantic
            similarity matching. Use higher values for exact keyword searches,
            lower values for conceptual similarity searches. Range: 0-100,
            Default: 50.
        grounding_level:
          type: number
          format: double
          minimum: 0
          maximum: 1
          default: 0
          description: >-
            Level of grounding required for responses, controlling how closely
            answers must be tied to source material. Set lower for grounded
            outputs, higher for creativity. Higher values (closer to 1.0) allow
            more creative interpretation, while lower values (closer to 0.0)
            stick more closely to source material. Range: 0.0-1.0, Default: 0.0.
        max_snippets:
          type: integer
          format: int32
          minimum: 1
          maximum: 60
          default: 30
          description: >-
            Maximum number of text snippets to retrieve from the Knowledge Graph
            for context. Works in concert with `search_weight` to control best
            matches vs broader coverage. While technically supports 1-60, values
            below 5 may return no results due to RAG implementation. Recommended
            range: 5-25. Due to RAG system behavior, you may see more snippets
            than requested. Range: 1-60, Default: 30.
        max_tokens:
          type: integer
          format: int32
          minimum: 100
          maximum: 8000
          default: 4000
          description: >-
            Maximum number of tokens the model can generate in the response.
            This controls the length of the AI's answer. Set higher for longer
            answers, set lower for shorter, faster answers. Range: 100-8000,
            Default: 4000.
        keyword_threshold:
          type: number
          format: double
          minimum: 0
          maximum: 1
          default: 0.7
          description: >-
            Threshold for keyword-based matching when searching Knowledge Graph
            content. Set higher for stricter relevance, lower for broader range.
            Higher values (closer to 1.0) require stronger keyword matches,
            while lower values (closer to 0.0) allow more lenient matching.
            Range: 0.0-1.0, Default: 0.7.
        semantic_threshold:
          type: number
          format: double
          minimum: 0
          maximum: 1
          default: 0.7
          description: >-
            Threshold for semantic similarity matching when searching Knowledge
            Graph content. Set higher for stricter relevance, lower for broader
            range. Higher values (closer to 1.0) require stronger semantic
            similarity, while lower values (closer to 0.0) allow more lenient
            semantic matching. Range: 0.0-1.0, Default: 0.7.
        inline_citations:
          type: boolean
          default: false
          description: >-
            Whether to include inline citations in the response, showing which
            Knowledge Graph sources were used. Default: false.
    vision_tool_request_file_variable:
      title: Vision Tool Request File Variable
      required:
        - name
        - file_id
      type: object
      properties:
        name:
          type: string
          description: >-
            The name of the file variable. You must reference this name in the
            `message.content` field of the request to the chat completions
            endpoint. Use double curly braces (`{{}}`) to reference the file.
            For example, `Describe the difference between the image {{image_1}}
            and the image {{image_2}}`.
        file_id:
          type: string
          description: >-
            The File ID of the file to analyze. The file must be uploaded to the
            Writer platform before you use it with the Vision tool. Supported
            file types: JPG, PNG, PDF, TXT. The maximum allowed file size is
            7MB.
    top_log_prob:
      title: top_log_prob
      description: >-
        An array of mappings for each token to its top log probabilities,
        showing detailed prediction probabilities.
      required:
        - token
        - logprob
      type: object
      properties:
        token:
          type: string
        logprob:
          type: number
          format: double
        bytes:
          type: array
          items:
            type: integer
            format: int32
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        Bearer authentication header of the form `Bearer <token>`, where
        `<token>` is your [Writer API
        key](https://dev.writer.com/api-reference/api-keys).

````