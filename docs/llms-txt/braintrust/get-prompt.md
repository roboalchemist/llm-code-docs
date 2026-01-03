# Source: https://braintrust.dev/docs/api-reference/prompts/get-prompt.md

# Get prompt

> Get a prompt object by its id



## OpenAPI

````yaml openapi.yaml get /v1/prompt/{prompt_id}
openapi: 3.1.1
info:
  version: 1.0.0
  title: Braintrust API
  description: >-
    API specification for the backend data server. The API is hosted globally at

    https://api.braintrust.dev or in your own environment.


    You can access the OpenAPI spec for this API at
    https://github.com/braintrustdata/braintrust-openapi.
  license:
    name: Apache 2.0
servers:
  - url: https://api.braintrust.dev
security:
  - bearerAuth: []
  - {}
paths:
  /v1/prompt/{prompt_id}:
    get:
      tags:
        - Prompts
      summary: Get prompt
      description: Get a prompt object by its id
      operationId: getPromptId
      parameters:
        - $ref: '#/components/parameters/PromptIdParam'
        - $ref: '#/components/parameters/PromptVersion'
      responses:
        '200':
          description: Returns the prompt object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Prompt'
        '400':
          description: >-
            The request was unacceptable, often due to missing a required
            parameter
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '401':
          description: No valid API key provided
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '403':
          description: The API key doesn’t have permissions to perform the request
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '429':
          description: >-
            Too many requests hit the API too quickly. We recommend an
            exponential backoff of your requests
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '500':
          description: Something went wrong on Braintrust's end. (These are rare.)
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
      security:
        - bearerAuth: []
        - {}
components:
  parameters:
    PromptIdParam:
      schema:
        $ref: '#/components/schemas/PromptIdParam'
      required: true
      description: Prompt id
      name: prompt_id
      in: path
    PromptVersion:
      schema:
        $ref: '#/components/schemas/PromptVersion'
      required: false
      description: >-
        Retrieve prompt at a specific version.


        The version id can either be a transaction id (e.g.
        '1000192656880881099') or a version identifier (e.g.
        '81cd05ee665fdfb3').
      name: version
      in: query
  schemas:
    Prompt:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the prompt
        _xact_id:
          type: string
          description: >-
            The transaction id of an event is unique to the network operation
            that processed the event insertion. Transaction ids are
            monotonically increasing over time and can be used to retrieve a
            versioned snapshot of the prompt (see the `version` parameter)
        project_id:
          type: string
          format: uuid
          description: Unique identifier for the project that the prompt belongs under
        log_id:
          type: string
          enum:
            - p
          description: A literal 'p' which identifies the object as a project prompt
        org_id:
          type: string
          format: uuid
          description: Unique identifier for the organization
        name:
          type: string
          description: Name of the prompt
        slug:
          type: string
          description: Unique identifier for the prompt
        description:
          type: string
          nullable: true
          description: Textual description of the prompt
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of prompt creation
        prompt_data:
          $ref: '#/components/schemas/PromptDataNullish'
        tags:
          type: array
          nullable: true
          items:
            type: string
          description: A list of tags for the prompt
        metadata:
          type: object
          nullable: true
          additionalProperties:
            nullable: true
          description: User-controlled metadata about the prompt
        function_type:
          $ref: '#/components/schemas/FunctionTypeEnumNullish'
      required:
        - id
        - _xact_id
        - project_id
        - log_id
        - org_id
        - name
        - slug
    PromptIdParam:
      type: string
      format: uuid
      description: Prompt id
    PromptVersion:
      type: string
      description: >-
        Retrieve prompt at a specific version.


        The version id can either be a transaction id (e.g.
        '1000192656880881099') or a version identifier (e.g.
        '81cd05ee665fdfb3').
    PromptDataNullish:
      type: object
      nullable: true
      properties:
        prompt:
          $ref: '#/components/schemas/PromptBlockDataNullish'
        options:
          $ref: '#/components/schemas/PromptOptionsNullish'
        parser:
          $ref: '#/components/schemas/PromptParserNullish'
        tool_functions:
          type: array
          nullable: true
          items:
            $ref: '#/components/schemas/SavedFunctionId'
        mcp:
          type: object
          nullable: true
          additionalProperties:
            oneOf:
              - type: object
                properties:
                  type:
                    type: string
                    enum:
                      - id
                  id:
                    type: string
                    format: uuid
                  is_disabled:
                    type: boolean
                  enabled_tools:
                    type: array
                    nullable: true
                    items:
                      type: string
                    description: If omitted, all tools are enabled
                required:
                  - type
                  - id
                title: >-
                  MCP server id. This is used for project-level MCP server
                  definitions.
              - type: object
                properties:
                  type:
                    type: string
                    enum:
                      - url
                  url:
                    type: string
                  is_disabled:
                    type: boolean
                  enabled_tools:
                    type: array
                    nullable: true
                    items:
                      type: string
                    description: If omitted, all tools are enabled
                required:
                  - type
                  - url
                title: >-
                  MCP server url. This is used for inline definitions of MCP
                  servers.
        origin:
          type: object
          nullable: true
          properties:
            prompt_id:
              type: string
            project_id:
              type: string
            prompt_version:
              type: string
      description: The prompt, model, and its parameters
    FunctionTypeEnumNullish:
      type: string
      nullable: true
      enum:
        - llm
        - scorer
        - task
        - tool
        - custom_view
        - null
    PromptBlockDataNullish:
      anyOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - chat
            messages:
              type: array
              items:
                $ref: '#/components/schemas/ChatCompletionMessageParam'
            tools:
              type: string
          required:
            - type
            - messages
          title: chat
        - type: object
          properties:
            type:
              type: string
              enum:
                - completion
            content:
              type: string
          required:
            - type
            - content
          title: completion
        - type: 'null'
    PromptOptionsNullish:
      type: object
      nullable: true
      properties:
        model:
          type: string
        params:
          $ref: '#/components/schemas/ModelParams'
        position:
          type: string
    PromptParserNullish:
      type: object
      nullable: true
      properties:
        type:
          type: string
          enum:
            - llm_classifier
        use_cot:
          type: boolean
        choice_scores:
          type: object
          additionalProperties:
            type: number
            minimum: 0
            maximum: 1
      required:
        - type
        - use_cot
        - choice_scores
    SavedFunctionId:
      anyOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - function
            id:
              type: string
          required:
            - type
            - id
          title: function
        - type: object
          properties:
            type:
              type: string
              enum:
                - global
            name:
              type: string
          required:
            - type
            - name
          title: global
    ChatCompletionMessageParam:
      anyOf:
        - type: object
          properties:
            content:
              anyOf:
                - type: string
                  default: ''
                  title: text
                - type: array
                  items:
                    $ref: '#/components/schemas/ChatCompletionContentPartText'
                  title: array
            role:
              type: string
              enum:
                - system
            name:
              type: string
          required:
            - role
          title: system
        - type: object
          properties:
            content:
              anyOf:
                - type: string
                  default: ''
                  title: text
                - type: array
                  items:
                    $ref: '#/components/schemas/ChatCompletionContentPart'
                  title: array
            role:
              type: string
              enum:
                - user
            name:
              type: string
          required:
            - role
          title: user
        - type: object
          properties:
            role:
              type: string
              enum:
                - assistant
            content:
              anyOf:
                - type: string
                - type: array
                  items:
                    $ref: '#/components/schemas/ChatCompletionContentPartText'
                - type: 'null'
            function_call:
              type: object
              nullable: true
              properties:
                arguments:
                  type: string
                name:
                  type: string
              required:
                - arguments
                - name
            name:
              type: string
              nullable: true
            tool_calls:
              type: array
              nullable: true
              items:
                $ref: '#/components/schemas/ChatCompletionMessageToolCall'
            reasoning:
              type: array
              nullable: true
              items:
                $ref: '#/components/schemas/ChatCompletionMessageReasoning'
          required:
            - role
          title: assistant
        - type: object
          properties:
            content:
              anyOf:
                - type: string
                  default: ''
                  title: text
                - type: array
                  items:
                    $ref: '#/components/schemas/ChatCompletionContentPartText'
                  title: array
            role:
              type: string
              enum:
                - tool
            tool_call_id:
              type: string
              default: ''
          required:
            - role
          title: tool
        - type: object
          properties:
            content:
              type: string
              nullable: true
            name:
              type: string
            role:
              type: string
              enum:
                - function
          required:
            - content
            - name
            - role
          title: function
        - type: object
          properties:
            content:
              anyOf:
                - type: string
                  default: ''
                  title: text
                - type: array
                  items:
                    $ref: '#/components/schemas/ChatCompletionContentPartText'
                  title: array
            role:
              type: string
              enum:
                - developer
            name:
              type: string
          required:
            - role
          title: developer
        - type: object
          properties:
            role:
              type: string
              enum:
                - model
            content:
              type: string
              nullable: true
          required:
            - role
          title: fallback
    ModelParams:
      anyOf:
        - type: object
          properties:
            use_cache:
              type: boolean
            reasoning_enabled:
              type: boolean
            reasoning_budget:
              type: number
            temperature:
              type: number
            top_p:
              type: number
            max_tokens:
              type: number
            max_completion_tokens:
              type: number
              description: The successor to max_tokens
            frequency_penalty:
              type: number
            presence_penalty:
              type: number
            response_format:
              $ref: '#/components/schemas/ResponseFormatNullish'
            tool_choice:
              anyOf:
                - type: string
                  enum:
                    - auto
                  title: auto
                - type: string
                  enum:
                    - none
                  title: none
                - type: string
                  enum:
                    - required
                  title: required
                - type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - function
                    function:
                      type: object
                      properties:
                        name:
                          type: string
                      required:
                        - name
                  required:
                    - type
                    - function
                  title: function
            function_call:
              anyOf:
                - type: string
                  enum:
                    - auto
                  title: auto
                - type: string
                  enum:
                    - none
                  title: none
                - type: object
                  properties:
                    name:
                      type: string
                  required:
                    - name
                  title: function
            'n':
              type: number
            stop:
              type: array
              items:
                type: string
            reasoning_effort:
              type: string
              enum:
                - none
                - minimal
                - low
                - medium
                - high
            verbosity:
              type: string
              enum:
                - low
                - medium
                - high
          additionalProperties:
            nullable: true
          title: OpenAIModelParams
          x-stainless-skip:
            - go
        - type: object
          properties:
            use_cache:
              type: boolean
            reasoning_enabled:
              type: boolean
            reasoning_budget:
              type: number
            max_tokens:
              type: number
            temperature:
              type: number
            top_p:
              type: number
            top_k:
              type: number
            stop_sequences:
              type: array
              items:
                type: string
            max_tokens_to_sample:
              type: number
              description: This is a legacy parameter that should not be used.
          required:
            - max_tokens
            - temperature
          additionalProperties:
            nullable: true
          title: AnthropicModelParams
          x-stainless-skip:
            - go
        - type: object
          properties:
            use_cache:
              type: boolean
            reasoning_enabled:
              type: boolean
            reasoning_budget:
              type: number
            temperature:
              type: number
            maxOutputTokens:
              type: number
            topP:
              type: number
            topK:
              type: number
          additionalProperties:
            nullable: true
          title: GoogleModelParams
          x-stainless-skip:
            - go
        - type: object
          properties:
            use_cache:
              type: boolean
            reasoning_enabled:
              type: boolean
            reasoning_budget:
              type: number
            temperature:
              type: number
            topK:
              type: number
          additionalProperties:
            nullable: true
          title: WindowAIModelParams
          x-stainless-skip:
            - go
        - type: object
          properties:
            use_cache:
              type: boolean
            reasoning_enabled:
              type: boolean
            reasoning_budget:
              type: number
          additionalProperties:
            nullable: true
          title: JsCompletionParams
          x-stainless-skip:
            - go
    ChatCompletionContentPartText:
      type: object
      properties:
        text:
          type: string
          default: ''
        type:
          type: string
          enum:
            - text
        cache_control:
          type: object
          properties:
            type:
              type: string
              enum:
                - ephemeral
          required:
            - type
      required:
        - type
    ChatCompletionContentPart:
      anyOf:
        - $ref: '#/components/schemas/ChatCompletionContentPartTextWithTitle'
        - $ref: '#/components/schemas/ChatCompletionContentPartImageWithTitle'
        - $ref: '#/components/schemas/ChatCompletionContentPartFileWithTitle'
      title: chat_completion_content_part
    ChatCompletionMessageToolCall:
      type: object
      properties:
        id:
          type: string
        function:
          type: object
          properties:
            arguments:
              type: string
            name:
              type: string
          required:
            - arguments
            - name
        type:
          type: string
          enum:
            - function
      required:
        - id
        - function
        - type
    ChatCompletionMessageReasoning:
      type: object
      properties:
        id:
          type: string
          nullable: true
        content:
          type: string
          nullable: true
      description: >-
        Note: This is not part of the OpenAI API spec, but we added it for
        interoperability with multiple reasoning models.
    ResponseFormatNullish:
      anyOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - json_object
          required:
            - type
          title: json_object
        - type: object
          properties:
            type:
              type: string
              enum:
                - json_schema
            json_schema:
              $ref: '#/components/schemas/ResponseFormatJsonSchema'
          required:
            - type
            - json_schema
          title: json_schema
        - type: object
          properties:
            type:
              type: string
              enum:
                - text
          required:
            - type
          title: text
        - type: 'null'
    ChatCompletionContentPartTextWithTitle:
      type: object
      properties:
        text:
          type: string
          default: ''
        type:
          type: string
          enum:
            - text
        cache_control:
          type: object
          properties:
            type:
              type: string
              enum:
                - ephemeral
          required:
            - type
      required:
        - type
      title: text
    ChatCompletionContentPartImageWithTitle:
      type: object
      properties:
        image_url:
          type: object
          properties:
            url:
              type: string
            detail:
              anyOf:
                - type: string
                  enum:
                    - auto
                  title: auto
                - type: string
                  enum:
                    - low
                  title: low
                - type: string
                  enum:
                    - high
                  title: high
          required:
            - url
        type:
          type: string
          enum:
            - image_url
      required:
        - image_url
        - type
      title: image_url
    ChatCompletionContentPartFileWithTitle:
      type: object
      properties:
        file:
          $ref: '#/components/schemas/ChatCompletionContentPartFileFile'
        type:
          type: string
          enum:
            - file
      required:
        - file
        - type
      title: file
    ResponseFormatJsonSchema:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
        schema:
          anyOf:
            - type: object
              additionalProperties:
                nullable: true
              title: object
              x-stainless-skip:
                - go
            - type: string
              title: string
        strict:
          type: boolean
          nullable: true
      required:
        - name
    ChatCompletionContentPartFileFile:
      type: object
      properties:
        file_data:
          type: string
        filename:
          type: string
        file_id:
          type: string
          title: The ID of an uploaded file to use as input.
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API key or JWT
      description: >-
        Most Braintrust endpoints are authenticated by providing your API key as
        a header `Authorization: Bearer [api_key]` to your HTTP request. You can
        create an API key in the Braintrust [organization settings
        page](https://www.braintrustdata.com/app/settings?subroute=api-keys).

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt