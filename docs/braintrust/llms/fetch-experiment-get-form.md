# Source: https://braintrust.dev/docs/api-reference/experiments/fetch-experiment-get-form.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Fetch experiment (GET form)

> Fetch the events in an experiment. Equivalent to the POST form of the same path, but with the parameters in the URL query rather than in the request body. For more complex queries, use the `POST /btql` endpoint.



## OpenAPI

````yaml openapi.yaml get /v1/experiment/{experiment_id}/fetch
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
  /v1/experiment/{experiment_id}/fetch:
    get:
      tags:
        - Experiments
      summary: Fetch experiment (GET form)
      description: >-
        Fetch the events in an experiment. Equivalent to the POST form of the
        same path, but with the parameters in the URL query rather than in the
        request body. For more complex queries, use the `POST /btql` endpoint.
      operationId: getExperimentIdFetch
      parameters:
        - $ref: '#/components/parameters/ExperimentIdParam'
        - $ref: '#/components/parameters/FetchLimitParam'
        - $ref: '#/components/parameters/MaxXactId'
        - $ref: '#/components/parameters/MaxRootSpanId'
        - $ref: '#/components/parameters/Version'
      responses:
        '200':
          description: Returns the fetched rows
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FetchExperimentEventsResponse'
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
    ExperimentIdParam:
      schema:
        $ref: '#/components/schemas/ExperimentIdParam'
      required: true
      description: Experiment id
      name: experiment_id
      in: path
    FetchLimitParam:
      schema:
        $ref: '#/components/schemas/FetchLimitParam'
      required: false
      description: >-
        limit the number of traces fetched


        Fetch queries may be paginated if the total result size is expected to
        be large (e.g. project_logs which accumulate over a long time). Note
        that fetch queries only support pagination in descending time order
        (from latest to earliest `_xact_id`. Furthermore, later pages may return
        rows which showed up in earlier pages, except with an earlier
        `_xact_id`. This happens because pagination occurs over the whole
        version history of the event log. You will most likely want to exclude
        any such duplicate, outdated rows (by `id`) from your combined result
        set.


        The `limit` parameter controls the number of full traces to return. So
        you may end up with more individual rows than the specified limit if you
        are fetching events containing traces.
      name: limit
      in: query
    MaxXactId:
      schema:
        $ref: '#/components/schemas/MaxXactId'
      required: false
      description: >-
        DEPRECATION NOTICE: The manually-constructed pagination cursor is
        deprecated in favor of the explicit 'cursor' returned by object fetch
        requests. Please prefer the 'cursor' argument going forwards.


        Together, `max_xact_id` and `max_root_span_id` form a pagination cursor


        Since a paginated fetch query returns results in order from latest to
        earliest, the cursor for the next page can be found as the row with the
        minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See
        the documentation of `limit` for an overview of paginating fetch
        queries.
      name: max_xact_id
      in: query
    MaxRootSpanId:
      schema:
        $ref: '#/components/schemas/MaxRootSpanId'
      required: false
      description: >-
        DEPRECATION NOTICE: The manually-constructed pagination cursor is
        deprecated in favor of the explicit 'cursor' returned by object fetch
        requests. Please prefer the 'cursor' argument going forwards.


        Together, `max_xact_id` and `max_root_span_id` form a pagination cursor


        Since a paginated fetch query returns results in order from latest to
        earliest, the cursor for the next page can be found as the row with the
        minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See
        the documentation of `limit` for an overview of paginating fetch
        queries.
      name: max_root_span_id
      in: query
    Version:
      schema:
        $ref: '#/components/schemas/Version'
      required: false
      description: >-
        Retrieve a snapshot of events from a past time


        The version id is essentially a filter on the latest event transaction
        id. You can use the `max_xact_id` returned by a past fetch as the
        version to reproduce that exact fetch.
      name: version
      in: query
  schemas:
    FetchExperimentEventsResponse:
      type: object
      properties:
        events:
          type: array
          items:
            $ref: '#/components/schemas/ExperimentEvent'
          description: A list of fetched events
        cursor:
          type: string
          nullable: true
          description: >-
            Pagination cursor


            Pass this string directly as the `cursor` param to your next fetch
            request to get the next page of results. Not provided if the
            returned result set is empty.
      required:
        - events
    ExperimentIdParam:
      type: string
      format: uuid
      description: Experiment id
    FetchLimitParam:
      type: integer
      nullable: true
      minimum: 0
      description: >-
        limit the number of traces fetched


        Fetch queries may be paginated if the total result size is expected to
        be large (e.g. project_logs which accumulate over a long time). Note
        that fetch queries only support pagination in descending time order
        (from latest to earliest `_xact_id`. Furthermore, later pages may return
        rows which showed up in earlier pages, except with an earlier
        `_xact_id`. This happens because pagination occurs over the whole
        version history of the event log. You will most likely want to exclude
        any such duplicate, outdated rows (by `id`) from your combined result
        set.


        The `limit` parameter controls the number of full traces to return. So
        you may end up with more individual rows than the specified limit if you
        are fetching events containing traces.
    MaxXactId:
      type: string
      description: >-
        DEPRECATION NOTICE: The manually-constructed pagination cursor is
        deprecated in favor of the explicit 'cursor' returned by object fetch
        requests. Please prefer the 'cursor' argument going forwards.


        Together, `max_xact_id` and `max_root_span_id` form a pagination cursor


        Since a paginated fetch query returns results in order from latest to
        earliest, the cursor for the next page can be found as the row with the
        minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See
        the documentation of `limit` for an overview of paginating fetch
        queries.
    MaxRootSpanId:
      type: string
      description: >-
        DEPRECATION NOTICE: The manually-constructed pagination cursor is
        deprecated in favor of the explicit 'cursor' returned by object fetch
        requests. Please prefer the 'cursor' argument going forwards.


        Together, `max_xact_id` and `max_root_span_id` form a pagination cursor


        Since a paginated fetch query returns results in order from latest to
        earliest, the cursor for the next page can be found as the row with the
        minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See
        the documentation of `limit` for an overview of paginating fetch
        queries.
    Version:
      type: string
      description: >-
        Retrieve a snapshot of events from a past time


        The version id is essentially a filter on the latest event transaction
        id. You can use the `max_xact_id` returned by a past fetch as the
        version to reproduce that exact fetch.
    ExperimentEvent:
      type: object
      properties:
        id:
          type: string
          description: >-
            A unique identifier for the experiment event. If you don't provide
            one, Braintrust will generate one for you
        _xact_id:
          type: string
          description: >-
            The transaction id of an event is unique to the network operation
            that processed the event insertion. Transaction ids are
            monotonically increasing over time and can be used to retrieve a
            versioned snapshot of the experiment (see the `version` parameter)
        created:
          type: string
          format: date-time
          description: The timestamp the experiment event was created
        _pagination_key:
          type: string
          nullable: true
          description: >-
            A stable, time-ordered key that can be used to paginate over
            experiment events. This field is auto-generated by Braintrust and
            only exists in Brainstore.
        project_id:
          type: string
          format: uuid
          description: Unique identifier for the project that the experiment belongs under
        experiment_id:
          type: string
          format: uuid
          description: Unique identifier for the experiment
        input:
          nullable: true
          description: >-
            The arguments that uniquely define a test case (an arbitrary, JSON
            serializable object). Later on, Braintrust will use the `input` to
            know whether two test cases are the same between experiments, so
            they should not contain experiment-specific state. A simple rule of
            thumb is that if you run the same experiment twice, the `input`
            should be identical
        output:
          nullable: true
          description: >-
            The output of your application, including post-processing (an
            arbitrary, JSON serializable object), that allows you to determine
            whether the result is correct or not. For example, in an app that
            generates SQL queries, the `output` should be the _result_ of the
            SQL query generated by the model, not the query itself, because
            there may be multiple valid queries that answer a single question
        expected:
          nullable: true
          description: >-
            The ground truth value (an arbitrary, JSON serializable object) that
            you'd compare to `output` to determine if your `output` value is
            correct or not. Braintrust currently does not compare `output` to
            `expected` for you, since there are so many different ways to do
            that correctly. Instead, these values are just used to help you
            navigate your experiments while digging into analyses. However, we
            may later use these values to re-score outputs or fine-tune your
            models
        error:
          nullable: true
          description: The error that occurred, if any.
        scores:
          type: object
          nullable: true
          additionalProperties:
            type: number
            nullable: true
            minimum: 0
            maximum: 1
          description: >-
            A dictionary of numeric values (between 0 and 1) to log. The scores
            should give you a variety of signals that help you determine how
            accurate the outputs are compared to what you expect and diagnose
            failures. For example, a summarization app might have one score that
            tells you how accurate the summary is, and another that measures the
            word similarity between the generated and grouth truth summary. The
            word similarity score could help you determine whether the
            summarization was covering similar concepts or not. You can use
            these scores to help you sort, filter, and compare experiments
        metadata:
          type: object
          nullable: true
          properties:
            model:
              type: string
              nullable: true
              description: The model used for this example
          additionalProperties:
            nullable: true
          description: >-
            A dictionary with additional data about the test example, model
            outputs, or just about anything else that's relevant, that you can
            use to help find and analyze examples later. For example, you could
            log the `prompt`, example's `id`, or anything else that would be
            useful to slice/dice later. The values in `metadata` can be any
            JSON-serializable type, but its keys must be strings
        tags:
          type: array
          nullable: true
          items:
            type: string
          description: A list of tags to log
        metrics:
          type: object
          nullable: true
          properties:
            start:
              type: number
              nullable: true
              description: >-
                A unix timestamp recording when the section of code which
                produced the experiment event started
            end:
              type: number
              nullable: true
              description: >-
                A unix timestamp recording when the section of code which
                produced the experiment event finished
            prompt_tokens:
              type: integer
              nullable: true
              description: >-
                The number of tokens in the prompt used to generate the
                experiment event (only set if this is an LLM span)
            completion_tokens:
              type: integer
              nullable: true
              description: >-
                The number of tokens in the completion generated by the model
                (only set if this is an LLM span)
            tokens:
              type: integer
              nullable: true
              description: >-
                The total number of tokens in the input and output of the
                experiment event.
            caller_functionname:
              nullable: true
              description: This metric is deprecated
            caller_filename:
              nullable: true
              description: This metric is deprecated
            caller_lineno:
              nullable: true
              description: This metric is deprecated
          additionalProperties:
            type: number
          description: >-
            Metrics are numerical measurements tracking the execution of the
            code that produced the experiment event. Use "start" and "end" to
            track the time span over which the experiment event was produced
        context:
          type: object
          nullable: true
          properties:
            caller_functionname:
              type: string
              nullable: true
              description: The function in code which created the experiment event
            caller_filename:
              type: string
              nullable: true
              description: Name of the file in code where the experiment event was created
            caller_lineno:
              type: integer
              nullable: true
              description: Line of code where the experiment event was created
          additionalProperties:
            nullable: true
          description: >-
            Context is additional information about the code that produced the
            experiment event. It is essentially the textual counterpart to
            `metrics`. Use the `caller_*` attributes to track the location in
            code which produced the experiment event
        span_id:
          type: string
          description: >-
            A unique identifier used to link different experiment events
            together as part of a full trace. See the [tracing
            guide](https://www.braintrust.dev/docs/instrument) for full details
            on tracing
        span_parents:
          type: array
          nullable: true
          items:
            type: string
          description: >-
            An array of the parent `span_ids` of this experiment event. This
            should be empty for the root span of a trace, and should most often
            contain just one parent element for subspans
        root_span_id:
          type: string
          description: A unique identifier for the trace this experiment event belongs to
        span_attributes:
          $ref: '#/components/schemas/SpanAttributes'
        is_root:
          type: boolean
          nullable: true
          description: Whether this span is a root span
        origin:
          $ref: '#/components/schemas/ObjectReferenceNullish'
        comments:
          type: array
          nullable: true
          items:
            nullable: true
          description: Optional list of comments attached to this event
        audit_data:
          type: array
          nullable: true
          items:
            nullable: true
          description: Optional list of audit entries attached to this event
        facets:
          type: object
          nullable: true
          additionalProperties:
            nullable: true
          description: Facets for categorization (dictionary from facet id to value)
        classifications:
          type: object
          nullable: true
          additionalProperties:
            type: array
            items:
              type: object
              properties:
                id:
                  type: string
                  description: Stable classification identifier
                label:
                  type: string
                  description: >-
                    Original label of the classification item, which is useful
                    for search and indexing purposes
                confidence:
                  type: number
                  nullable: true
                  description: Optional confidence score for the classification
                metadata:
                  type: object
                  nullable: true
                  additionalProperties:
                    nullable: true
                  description: Optional metadata associated with the classification
                source:
                  $ref: '#/components/schemas/SavedFunctionId'
              required:
                - id
          description: >-
            Classifications for this event (dictionary from classification name
            to items)
      required:
        - id
        - _xact_id
        - created
        - project_id
        - experiment_id
        - span_id
        - root_span_id
    SpanAttributes:
      type: object
      nullable: true
      properties:
        name:
          type: string
          nullable: true
          description: Name of the span, for display purposes only
        type:
          $ref: '#/components/schemas/SpanType'
      additionalProperties:
        nullable: true
      description: Human-identifying attributes of the span, such as name, type, etc.
    ObjectReferenceNullish:
      type: object
      nullable: true
      properties:
        object_type:
          type: string
          enum:
            - project_logs
            - experiment
            - dataset
            - prompt
            - function
            - prompt_session
          description: Type of the object the event is originating from.
        object_id:
          type: string
          format: uuid
          description: ID of the object the event is originating from.
        id:
          type: string
          description: ID of the original event.
        _xact_id:
          type: string
          nullable: true
          description: Transaction ID of the original event.
        created:
          type: string
          nullable: true
          description: Created timestamp of the original event. Used to help sort in the UI
      required:
        - object_type
        - object_id
        - id
      description: Indicates the event was copied from another object.
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
    SpanType:
      type: string
      nullable: true
      enum:
        - llm
        - score
        - function
        - eval
        - task
        - tool
        - automation
        - facet
        - preprocessor
        - classifier
        - null
      description: Type of the span, for display purposes only
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