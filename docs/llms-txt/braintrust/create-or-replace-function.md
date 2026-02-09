# Source: https://braintrust.dev/docs/api-reference/functions/create-or-replace-function.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create or replace function

> Create or replace function. If there is an existing function in the project with the same slug as the one specified in the request, will replace the existing function with the provided fields



## OpenAPI

````yaml openapi.yaml put /v1/function
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
  /v1/function:
    put:
      tags:
        - Functions
      summary: Create or replace function
      description: >-
        Create or replace function. If there is an existing function in the
        project with the same slug as the one specified in the request, will
        replace the existing function with the provided fields
      operationId: putFunction
      requestBody:
        description: Any desired information about the new function object
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateFunction'
      responses:
        '200':
          description: Returns the new function object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Function'
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
  schemas:
    CreateFunction:
      type: object
      properties:
        project_id:
          type: string
          format: uuid
          description: Unique identifier for the project that the prompt belongs under
        name:
          type: string
          minLength: 1
          description: Name of the prompt
        slug:
          type: string
          minLength: 1
          description: Unique identifier for the prompt
        description:
          type: string
          nullable: true
          description: Textual description of the prompt
        prompt_data:
          $ref: '#/components/schemas/PromptDataNullish'
        tags:
          type: array
          nullable: true
          items:
            type: string
          description: A list of tags for the prompt
        function_type:
          $ref: '#/components/schemas/FunctionTypeEnumNullish'
        function_data:
          $ref: '#/components/schemas/FunctionData'
        origin:
          type: object
          nullable: true
          properties:
            object_type:
              $ref: '#/components/schemas/AclObjectType'
            object_id:
              type: string
              format: uuid
              description: Id of the object the function is originating from
            internal:
              type: boolean
              nullable: true
              description: >-
                The function exists for internal purposes and should not be
                displayed in the list of functions.
          required:
            - object_type
            - object_id
        function_schema:
          type: object
          nullable: true
          properties:
            parameters:
              nullable: true
            returns:
              nullable: true
          description: JSON schema for the function's parameters and return type
      required:
        - project_id
        - name
        - slug
        - function_data
    Function:
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
        function_data:
          $ref: '#/components/schemas/FunctionData'
        origin:
          type: object
          nullable: true
          properties:
            object_type:
              $ref: '#/components/schemas/AclObjectType'
            object_id:
              type: string
              format: uuid
              description: Id of the object the function is originating from
            internal:
              type: boolean
              nullable: true
              description: >-
                The function exists for internal purposes and should not be
                displayed in the list of functions.
          required:
            - object_type
            - object_id
        function_schema:
          type: object
          nullable: true
          properties:
            parameters:
              nullable: true
            returns:
              nullable: true
          description: JSON schema for the function's parameters and return type
      required:
        - id
        - _xact_id
        - project_id
        - log_id
        - org_id
        - name
        - slug
        - function_data
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
            allOf:
              - $ref: '#/components/schemas/SavedFunctionId'
              - anyOf:
                  - type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - function
                      id:
                        type: string
                      version:
                        type: string
                        description: The version of the function
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
                      function_type:
                        $ref: '#/components/schemas/FunctionTypeEnum'
                    required:
                      - type
                      - name
                    title: global
        template_format:
          type: string
          nullable: true
          enum:
            - mustache
            - nunjucks
            - none
            - null
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
        - preprocessor
        - facet
        - classifier
        - tag
        - null
    FunctionData:
      anyOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - prompt
          required:
            - type
          title: prompt
        - type: object
          properties:
            type:
              type: string
              enum:
                - code
            data:
              anyOf:
                - allOf:
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - bundle
                      required:
                        - type
                    - $ref: '#/components/schemas/CodeBundle'
                  title: bundle
                - type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - inline
                    runtime_context:
                      type: object
                      properties:
                        runtime:
                          type: string
                          enum:
                            - node
                            - python
                            - browser
                            - quickjs
                        version:
                          type: string
                      required:
                        - runtime
                        - version
                    code:
                      type: string
                    code_hash:
                      type: string
                      description: SHA256 hash of the code, computed at save time
                  required:
                    - type
                    - runtime_context
                    - code
                  title: inline
          required:
            - type
            - data
          title: code
        - $ref: '#/components/schemas/GraphData'
        - type: object
          properties:
            type:
              type: string
              enum:
                - remote_eval
            endpoint:
              type: string
            eval_name:
              type: string
            parameters:
              type: object
              additionalProperties:
                nullable: true
          required:
            - type
            - endpoint
            - eval_name
            - parameters
          description: A remote eval to run
          title: remote_eval
        - type: object
          properties:
            type:
              type: string
              enum:
                - global
            name:
              type: string
            function_type:
              $ref: '#/components/schemas/FunctionTypeEnum'
            config:
              type: object
              nullable: true
              additionalProperties:
                nullable: true
              description: >-
                Configuration options to pass to the global function (e.g., for
                preprocessor customization)
          required:
            - type
            - name
          title: global
        - $ref: '#/components/schemas/FacetData'
        - $ref: '#/components/schemas/BatchedFacetData'
        - allOf:
            - $ref: '#/components/schemas/TopicMapData'
            - title: topic_map
    AclObjectType:
      type: string
      enum:
        - organization
        - project
        - experiment
        - dataset
        - prompt
        - prompt_session
        - group
        - role
        - org_member
        - project_log
        - org_project
      description: The object type that the ACL applies to
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
          description: Map of choices to scores (0-1). Used by scorers.
        choice:
          type: array
          items:
            type: string
          description: >-
            List of valid choices without score mapping. Used by classifiers
            that deposit output to tags.
        allow_no_match:
          type: boolean
          description: >-
            If true, adds a 'No match' option. When selected, no tag is
            deposited.
      required:
        - type
        - use_cot
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
            version:
              type: string
              description: The version of the function
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
            function_type:
              $ref: '#/components/schemas/FunctionTypeEnum'
          required:
            - type
            - name
          title: global
        - type: 'null'
      description: Optional function identifier that produced the classification
    FunctionTypeEnum:
      type: string
      enum:
        - llm
        - scorer
        - task
        - tool
        - custom_view
        - preprocessor
        - facet
        - classifier
        - tag
        - null
      default: scorer
      description: The type of global function. Defaults to 'scorer'.
    CodeBundle:
      type: object
      properties:
        runtime_context:
          type: object
          properties:
            runtime:
              type: string
              enum:
                - node
                - python
                - browser
                - quickjs
            version:
              type: string
          required:
            - runtime
            - version
        location:
          anyOf:
            - type: object
              properties:
                type:
                  type: string
                  enum:
                    - experiment
                eval_name:
                  type: string
                position:
                  anyOf:
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - task
                      required:
                        - type
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - scorer
                        index:
                          type: integer
                          minimum: 0
                      required:
                        - type
                        - index
                      title: scorer
              required:
                - type
                - eval_name
                - position
              title: experiment
            - type: object
              properties:
                type:
                  type: string
                  enum:
                    - function
                index:
                  type: integer
                  minimum: 0
              required:
                - type
                - index
              title: function
        bundle_id:
          type: string
        preview:
          type: string
          nullable: true
          description: A preview of the code
      required:
        - runtime_context
        - location
        - bundle_id
    GraphData:
      type: object
      properties:
        type:
          type: string
          enum:
            - graph
        nodes:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/GraphNode'
        edges:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/GraphEdge'
      required:
        - type
        - nodes
        - edges
      description: This feature is preliminary and unsupported.
      title: graph
    FacetData:
      type: object
      properties:
        type:
          type: string
          enum:
            - facet
        preprocessor:
          allOf:
            - $ref: '#/components/schemas/NullableSavedFunctionId'
            - description: >-
                The preprocessor function to use for facet extraction. If not
                provided, the project default preprocessor will be used, falling
                back to the global 'thread' preprocessor.
        prompt:
          type: string
          description: >-
            The prompt to use for LLM extraction. The preprocessed text will be
            provided as context.
        model:
          type: string
          description: The model to use for facet extraction
        embedding_model:
          type: string
          description: The embedding model to use for vectorizing facet results.
        no_match_pattern:
          type: string
          description: >-
            Regex pattern to identify outputs that do not match the facet. If
            the output matches, the facet will be saved as 'no_match'
      required:
        - type
        - prompt
      title: facet
    BatchedFacetData:
      type: object
      properties:
        type:
          type: string
          enum:
            - batched_facet
        preprocessor:
          allOf:
            - $ref: '#/components/schemas/NullableSavedFunctionId'
            - description: >-
                The preprocessor function to use for facet extraction. If not
                provided, the project default preprocessor will be used, falling
                back to the global 'thread' preprocessor.
        facets:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                description: The name of the facet
              prompt:
                type: string
                description: >-
                  The prompt to use for LLM extraction. The preprocessed text
                  will be provided as context.
              model:
                type: string
                description: The model to use for facet extraction
              embedding_model:
                type: string
                description: The embedding model to use for vectorizing facet results.
              no_match_pattern:
                type: string
                description: >-
                  Regex pattern to identify outputs that do not match the facet.
                  If the output matches, the facet will be saved as 'no_match'
            required:
              - name
              - prompt
        topic_maps:
          type: object
          additionalProperties:
            type: object
            properties:
              function_name:
                type: string
                description: The name of the topic map function
              topic_map_id:
                type: string
                description: The id of the topic map function
              topic_map_data:
                $ref: '#/components/schemas/TopicMapData'
            required:
              - function_name
              - topic_map_data
          description: >-
            Topic maps that depend on facets in this batch, keyed by source
            facet name
      required:
        - type
        - facets
      title: batched_facet
    TopicMapData:
      type: object
      properties:
        type:
          type: string
          enum:
            - topic_map
        source_facet:
          type: string
          description: The facet field name to use as input for classification
        embedding_model:
          type: string
          description: The embedding model to use for embedding facet values
        bundle_key:
          type: string
          description: Key of the topic map bundle in code_bundles bucket
        distance_threshold:
          type: number
          description: Maximum distance to nearest centroid. If exceeded, returns no_match.
        report:
          $ref: '#/components/schemas/TopicMapReport'
      required:
        - type
        - source_facet
        - embedding_model
        - bundle_key
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
    GraphNode:
      anyOf:
        - type: object
          properties:
            description:
              type: string
              nullable: true
              description: The description of the node
            position:
              type: object
              nullable: true
              properties:
                x:
                  type: number
                  description: The x position of the node
                'y':
                  type: number
                  description: The y position of the node
              required:
                - x
                - 'y'
              description: The position of the node
            type:
              type: string
              enum:
                - function
            function:
              $ref: '#/components/schemas/FunctionIdRef'
          required:
            - type
            - function
        - type: object
          properties:
            description:
              type: string
              nullable: true
              description: The description of the node
            position:
              type: object
              nullable: true
              properties:
                x:
                  type: number
                  description: The x position of the node
                'y':
                  type: number
                  description: The y position of the node
              required:
                - x
                - 'y'
              description: The position of the node
            type:
              type: string
              enum:
                - input
              description: The input to the graph
          required:
            - type
        - type: object
          properties:
            description:
              type: string
              nullable: true
              description: The description of the node
            position:
              type: object
              nullable: true
              properties:
                x:
                  type: number
                  description: The x position of the node
                'y':
                  type: number
                  description: The y position of the node
              required:
                - x
                - 'y'
              description: The position of the node
            type:
              type: string
              enum:
                - output
              description: The output of the graph
          required:
            - type
        - type: object
          properties:
            description:
              type: string
              nullable: true
              description: The description of the node
            position:
              type: object
              nullable: true
              properties:
                x:
                  type: number
                  description: The x position of the node
                'y':
                  type: number
                  description: The y position of the node
              required:
                - x
                - 'y'
              description: The position of the node
            type:
              type: string
              enum:
                - literal
            value:
              nullable: true
              description: A literal value to be returned
          required:
            - type
        - type: object
          properties:
            description:
              type: string
              nullable: true
              description: The description of the node
            position:
              type: object
              nullable: true
              properties:
                x:
                  type: number
                  description: The x position of the node
                'y':
                  type: number
                  description: The y position of the node
              required:
                - x
                - 'y'
              description: The position of the node
            type:
              type: string
              enum:
                - btql
            expr:
              type: string
              description: A BTQL expression to be evaluated
          required:
            - type
            - expr
        - type: object
          properties:
            description:
              type: string
              nullable: true
              description: The description of the node
            position:
              type: object
              nullable: true
              properties:
                x:
                  type: number
                  description: The x position of the node
                'y':
                  type: number
                  description: The y position of the node
              required:
                - x
                - 'y'
              description: The position of the node
            type:
              type: string
              enum:
                - gate
            condition:
              type: string
              nullable: true
              description: A BTQL expression to be evaluated
          required:
            - type
        - type: object
          properties:
            description:
              type: string
              nullable: true
              description: The description of the node
            position:
              type: object
              nullable: true
              properties:
                x:
                  type: number
                  description: The x position of the node
                'y':
                  type: number
                  description: The y position of the node
              required:
                - x
                - 'y'
              description: The position of the node
            type:
              type: string
              enum:
                - aggregator
          required:
            - type
        - type: object
          properties:
            description:
              type: string
              nullable: true
              description: The description of the node
            position:
              type: object
              nullable: true
              properties:
                x:
                  type: number
                  description: The x position of the node
                'y':
                  type: number
                  description: The y position of the node
              required:
                - x
                - 'y'
              description: The position of the node
            type:
              type: string
              enum:
                - prompt_template
            prompt:
              $ref: '#/components/schemas/PromptBlockData'
          required:
            - type
            - prompt
    GraphEdge:
      type: object
      properties:
        source:
          type: object
          properties:
            node:
              type: string
              maxLength: 1024
              description: The id of the node in the graph
            variable:
              type: string
          required:
            - node
            - variable
        target:
          type: object
          properties:
            node:
              type: string
              maxLength: 1024
              description: The id of the node in the graph
            variable:
              type: string
          required:
            - node
            - variable
        purpose:
          type: string
          enum:
            - control
            - data
            - messages
          description: The purpose of the edge
      required:
        - source
        - target
        - purpose
    NullableSavedFunctionId:
      anyOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - function
            id:
              type: string
            version:
              type: string
              description: The version of the function
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
            function_type:
              $ref: '#/components/schemas/FunctionTypeEnum'
          required:
            - type
            - name
          title: global
        - type: 'null'
      description: >-
        Default preprocessor for this project. When set, functions that use
        preprocessors will use this instead of their built-in default.
    TopicMapReport:
      type: object
      properties:
        version:
          type: number
          enum:
            - 1
        created_at:
          type: string
        settings:
          type: object
          properties:
            algorithm:
              type: string
              enum:
                - hdbscan
                - kmeans
                - hierarchical
            dimension_reduction:
              type: string
              enum:
                - umap
                - pca
                - none
            vector_field:
              type: string
            embedding_model:
              type: string
            n_clusters:
              type: integer
              nullable: true
            umap_dimensions:
              type: integer
              nullable: true
            min_cluster_size:
              type: integer
              nullable: true
            min_samples:
              type: integer
              nullable: true
          required:
            - algorithm
            - dimension_reduction
            - vector_field
            - embedding_model
        query_settings:
          type: object
          properties:
            hierarchy_threshold:
              type: integer
              nullable: true
            auto_naming:
              type: boolean
            skip_cache:
              type: boolean
            viz_mode:
              type: string
              enum:
                - bar
                - scatter
            naming_model:
              type: string
        clusters:
          type: array
          items:
            type: object
            properties:
              cluster_id:
                type: number
              parent_cluster_id:
                type: number
                nullable: true
              topic_id:
                type: string
              count:
                type: number
              sample_texts:
                type: array
                items:
                  type: string
              samples:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                    text:
                      type: string
                    root_span_id:
                      type: string
                    span_id:
                      type: string
                  required:
                    - id
                    - text
                    - root_span_id
                    - span_id
              name:
                type: string
              description:
                type: string
              keywords:
                type: array
                items:
                  type: string
              centroid:
                type: array
                items:
                  type: number
              parent_id:
                type: number
                nullable: true
              is_leaf:
                type: boolean
              depth:
                type: number
            required:
              - cluster_id
              - topic_id
              - count
              - sample_texts
              - samples
        embedding_points:
          type: array
          items:
            type: object
            properties:
              x:
                type: number
              'y':
                type: number
              cluster:
                type: number
              text:
                type: string
            required:
              - x
              - 'y'
              - cluster
      required:
        - version
        - settings
        - query_settings
        - clusters
      description: Saved clustering report for UI rehydration
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
    FunctionIdRef:
      type: object
      properties: {}
      additionalProperties:
        nullable: true
      description: Options for identifying a function
    PromptBlockData:
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