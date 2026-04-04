# Source: https://braintrust.dev/docs/api-reference/evals/launch-an-eval.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Launch an eval

> Launch an evaluation. This is the API-equivalent of the `Eval` function that is built into the Braintrust SDK. In the Eval API, you provide pointers to a dataset, task function, and scoring functions. The API will then run the evaluation, create an experiment, and return the results along with a link to the experiment. To learn more about evals, see the [Evals guide](https://www.braintrust.dev/docs/evaluate).



## OpenAPI

````yaml openapi.yaml post /v1/eval
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
  /v1/eval:
    post:
      tags:
        - Evals
      summary: Launch an eval
      description: >-
        Launch an evaluation. This is the API-equivalent of the `Eval` function
        that is built into the Braintrust SDK. In the Eval API, you provide
        pointers to a dataset, task function, and scoring functions. The API
        will then run the evaluation, create an experiment, and return the
        results along with a link to the experiment. To learn more about evals,
        see the [Evals guide](https://www.braintrust.dev/docs/evaluate).
      operationId: evalLaunch
      requestBody:
        description: Eval launch parameters
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RunEval'
      responses:
        '200':
          description: Eval launch response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SummarizeExperimentResponse'
      security:
        - bearerAuth: []
        - {}
components:
  schemas:
    RunEval:
      type: object
      properties:
        project_id:
          type: string
          description: Unique identifier for the project to run the eval in
        data:
          anyOf:
            - type: object
              properties:
                dataset_id:
                  type: string
                _internal_btql:
                  type: object
                  nullable: true
                  additionalProperties:
                    nullable: true
              required:
                - dataset_id
              description: Dataset id
              title: dataset_id
            - type: object
              properties:
                project_name:
                  type: string
                dataset_name:
                  type: string
                _internal_btql:
                  type: object
                  nullable: true
                  additionalProperties:
                    nullable: true
              required:
                - project_name
                - dataset_name
              description: Project and dataset name
              title: project_dataset_name
            - type: object
              properties:
                data:
                  type: array
                  items:
                    nullable: true
              required:
                - data
              description: Dataset rows
              title: dataset_rows
          description: The dataset to use
        task:
          $ref: '#/components/schemas/FunctionId'
        scores:
          type: array
          items:
            allOf:
              - $ref: '#/components/schemas/FunctionId'
              - description: Options for identifying a function
          description: The functions to score the eval on
        experiment_name:
          type: string
          description: >-
            An optional name for the experiment created by this eval. If it
            conflicts with an existing experiment, it will be suffixed with a
            unique identifier.
        metadata:
          type: object
          additionalProperties:
            nullable: true
          description: >-
            Optional experiment-level metadata to store about the evaluation.
            You can later use this to slice & dice across experiments.
        parent:
          allOf:
            - $ref: '#/components/schemas/InvokeParent'
            - description: Options for tracing the evaluation
        stream:
          type: boolean
          description: >-
            Whether to stream the results of the eval. If true, the request will
            return two events: one to indicate the experiment has started, and
            another upon completion. If false, the request will return the
            evaluation's summary upon completion.
        trial_count:
          type: number
          nullable: true
          description: >-
            The number of times to run the evaluator per input. This is useful
            for evaluating applications that have non-deterministic behavior and
            gives you both a stronger aggregate measure and a sense of the
            variance in the results.
        is_public:
          type: boolean
          nullable: true
          description: Whether the experiment should be public. Defaults to false.
        timeout:
          type: number
          nullable: true
          description: >-
            The maximum duration, in milliseconds, to run the evaluation.
            Defaults to undefined, in which case there is no timeout.
        max_concurrency:
          type: number
          nullable: true
          default: 10
          description: >-
            The maximum number of tasks/scorers that will be run concurrently.
            Defaults to 10. If null is provided, no max concurrency will be
            used.
        base_experiment_name:
          type: string
          nullable: true
          description: >-
            An optional experiment name to use as a base. If specified, the new
            experiment will be summarized and compared to this experiment.
        base_experiment_id:
          type: string
          nullable: true
          description: >-
            An optional experiment id to use as a base. If specified, the new
            experiment will be summarized and compared to this experiment.
        git_metadata_settings:
          $ref: '#/components/schemas/GitMetadataSettings'
        repo_info:
          allOf:
            - $ref: '#/components/schemas/RepoInfo'
            - description: >-
                Optionally explicitly specify the git metadata for this
                experiment. This takes precedence over `gitMetadataSettings` if
                specified.
        strict:
          type: boolean
          nullable: true
          description: >-
            If true, throw an error if one of the variables in the prompt is not
            present in the input
        stop_token:
          type: string
          nullable: true
          description: The token to stop the run
        extra_messages:
          type: string
          description: >-
            A template path of extra messages to append to the conversion. These
            messages will be appended to the end of the conversation, after the
            last message.
        tags:
          type: array
          items:
            type: string
          description: Optional tags that will be added to the experiment.
        mcp_auth:
          type: object
          additionalProperties:
            type: object
            properties:
              oauth_token:
                type: string
                description: The OAuth token to use
      required:
        - project_id
        - data
        - task
        - scores
    SummarizeExperimentResponse:
      type: object
      properties:
        project_name:
          type: string
          description: Name of the project that the experiment belongs to
        experiment_name:
          type: string
          description: Name of the experiment
        project_url:
          type: string
          format: uri
          description: URL to the project's page in the Braintrust app
        experiment_url:
          type: string
          format: uri
          description: URL to the experiment's page in the Braintrust app
        comparison_experiment_name:
          type: string
          nullable: true
          description: The experiment which scores are baselined against
        scores:
          type: object
          nullable: true
          additionalProperties:
            $ref: '#/components/schemas/ScoreSummary'
          description: Summary of the experiment's scores
        metrics:
          type: object
          nullable: true
          additionalProperties:
            $ref: '#/components/schemas/MetricSummary'
          description: Summary of the experiment's metrics
      required:
        - project_name
        - experiment_name
        - project_url
        - experiment_url
      description: Summary of an experiment
    FunctionId:
      anyOf:
        - type: object
          properties:
            function_id:
              type: string
              description: The ID of the function
            version:
              type: string
              description: The version of the function
          required:
            - function_id
          description: Function id
          title: function_id
        - type: object
          properties:
            project_name:
              type: string
              description: The name of the project containing the function
            slug:
              type: string
              description: The slug of the function
            version:
              type: string
              description: The version of the function
          required:
            - project_name
            - slug
          description: Project name and slug
          title: project_slug
        - type: object
          properties:
            global_function:
              type: string
              description: >-
                The name of the global function. Currently, the global namespace
                includes the functions in autoevals
            function_type:
              $ref: '#/components/schemas/FunctionTypeEnum'
          required:
            - global_function
          description: Global function name
          title: global_function
        - type: object
          properties:
            prompt_session_id:
              type: string
              description: The ID of the prompt session
            prompt_session_function_id:
              type: string
              description: The ID of the function in the prompt session
            version:
              type: string
              description: The version of the function
          required:
            - prompt_session_id
            - prompt_session_function_id
          description: Prompt session id
          title: prompt_session_id
        - type: object
          properties:
            inline_context:
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
              description: The inline code to execute
            name:
              type: string
              nullable: true
              description: The name of the inline code function
          required:
            - inline_context
            - code
          description: Inline code function
          title: inline_code
        - type: object
          properties:
            inline_prompt:
              $ref: '#/components/schemas/PromptData'
            inline_function:
              type: object
              additionalProperties:
                nullable: true
            function_type:
              $ref: '#/components/schemas/FunctionTypeEnum'
            name:
              type: string
              nullable: true
              description: The name of the inline function
          required:
            - inline_function
          description: Inline function definition
          title: inline_function
        - type: object
          properties:
            inline_prompt:
              $ref: '#/components/schemas/PromptData'
            function_type:
              $ref: '#/components/schemas/FunctionTypeEnum'
            name:
              type: string
              nullable: true
              description: The name of the inline prompt
          required:
            - inline_prompt
          description: Inline prompt definition
          title: inline_prompt
      description: The function to evaluate
    InvokeParent:
      anyOf:
        - type: object
          properties:
            object_type:
              type: string
              enum:
                - project_logs
                - experiment
                - playground_logs
            object_id:
              type: string
              description: The id of the container object you are logging to
            row_ids:
              type: object
              nullable: true
              properties:
                id:
                  type: string
                  description: The id of the row
                span_id:
                  type: string
                  description: The span_id of the row
                root_span_id:
                  type: string
                  description: The root_span_id of the row
              required:
                - id
                - span_id
                - root_span_id
              description: Identifiers for the row to to log a subspan under
            propagated_event:
              type: object
              nullable: true
              additionalProperties:
                nullable: true
              description: Include these properties in every span created under this parent
          required:
            - object_type
            - object_id
          description: Span parent properties
          title: span_parent_struct
        - type: string
          description: >-
            The parent's span identifier, created by calling `.export()` on a
            span
      description: Options for tracing the function call
    GitMetadataSettings:
      type: object
      nullable: true
      properties:
        collect:
          type: string
          enum:
            - all
            - none
            - some
        fields:
          type: array
          items:
            type: string
            enum:
              - commit
              - branch
              - tag
              - dirty
              - author_name
              - author_email
              - commit_message
              - commit_time
              - git_diff
      required:
        - collect
      additionalProperties: false
      description: >-
        Optional settings for collecting git metadata. By default, will collect
        all git metadata fields allowed in org-level settings.
    RepoInfo:
      type: object
      nullable: true
      properties:
        commit:
          type: string
          nullable: true
          description: SHA of most recent commit
        branch:
          type: string
          nullable: true
          description: Name of the branch the most recent commit belongs to
        tag:
          type: string
          nullable: true
          description: Name of the tag on the most recent commit
        dirty:
          type: boolean
          nullable: true
          description: Whether or not the repo had uncommitted changes when snapshotted
        author_name:
          type: string
          nullable: true
          description: Name of the author of the most recent commit
        author_email:
          type: string
          nullable: true
          description: Email of the author of the most recent commit
        commit_message:
          type: string
          nullable: true
          description: Most recent commit message
        commit_time:
          type: string
          nullable: true
          description: Time of the most recent commit
        git_diff:
          type: string
          nullable: true
          description: >-
            If the repo was dirty when run, this includes the diff between the
            current state of the repo and the most recent commit.
      description: Metadata about the state of the repo when the experiment was created
    ScoreSummary:
      type: object
      properties:
        name:
          type: string
          description: Name of the score
        score:
          type: number
          minimum: 0
          maximum: 1
          description: Average score across all examples
        diff:
          type: number
          minimum: -1
          maximum: 1
          description: Difference in score between the current and comparison experiment
        improvements:
          type: integer
          minimum: 0
          description: Number of improvements in the score
        regressions:
          type: integer
          minimum: 0
          description: Number of regressions in the score
      required:
        - name
        - score
        - improvements
        - regressions
      description: Summary of a score's performance
    MetricSummary:
      type: object
      properties:
        name:
          type: string
          description: Name of the metric
        metric:
          type: number
          description: Average metric across all examples
        unit:
          type: string
          description: Unit label for the metric
        diff:
          type: number
          description: Difference in metric between the current and comparison experiment
        improvements:
          type: integer
          minimum: 0
          description: Number of improvements in the metric
        regressions:
          type: integer
          minimum: 0
          description: Number of regressions in the metric
      required:
        - name
        - metric
        - unit
        - improvements
        - regressions
      description: Summary of a metric's performance
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
    PromptData:
      type: object
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