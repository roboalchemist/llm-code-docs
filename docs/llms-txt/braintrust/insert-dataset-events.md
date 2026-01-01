# Source: https://braintrust.dev/docs/api-reference/datasets/insert-dataset-events.md

# Insert dataset events

> Insert a set of events into the dataset



## OpenAPI

````yaml openapi.yaml post /v1/dataset/{dataset_id}/insert
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
  /v1/dataset/{dataset_id}/insert:
    post:
      tags:
        - Datasets
      summary: Insert dataset events
      description: Insert a set of events into the dataset
      operationId: postDatasetIdInsert
      parameters:
        - $ref: '#/components/parameters/DatasetIdParam'
      requestBody:
        description: An array of dataset events to insert
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/InsertDatasetEventRequest'
      responses:
        '200':
          description: Returns the inserted row ids
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/InsertEventsResponse'
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
    DatasetIdParam:
      schema:
        $ref: '#/components/schemas/DatasetIdParam'
      required: true
      description: Dataset id
      name: dataset_id
      in: path
  schemas:
    InsertDatasetEventRequest:
      type: object
      properties:
        events:
          type: array
          items:
            $ref: '#/components/schemas/InsertDatasetEvent'
          description: A list of dataset events to insert
      required:
        - events
    InsertEventsResponse:
      type: object
      properties:
        row_ids:
          type: array
          items:
            type: string
          description: >-
            The ids of all rows that were inserted, aligning one-to-one with the
            rows provided as input
      required:
        - row_ids
    DatasetIdParam:
      type: string
      format: uuid
      description: Dataset id
    InsertDatasetEvent:
      type: object
      properties:
        input:
          nullable: true
          description: >-
            The argument that uniquely define an input case (an arbitrary, JSON
            serializable object)
        expected:
          nullable: true
          description: >-
            The output of your application, including post-processing (an
            arbitrary, JSON serializable object)
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
        id:
          type: string
          nullable: true
          description: >-
            A unique identifier for the dataset event. If you don't provide one,
            Braintrust will generate one for you
        created:
          type: string
          nullable: true
          format: date-time
          description: The timestamp the dataset event was created
        origin:
          $ref: '#/components/schemas/ObjectReferenceNullish'
        _object_delete:
          type: boolean
          nullable: true
          description: >-
            Pass `_object_delete=true` to mark the dataset event deleted.
            Deleted events will not show up in subsequent fetches for this
            dataset
        _is_merge:
          type: boolean
          nullable: true
          description: >-
            The `_is_merge` field controls how the row is merged with any
            existing row with the same id in the DB. By default (or when set to
            `false`), the existing row is completely replaced by the new row.
            When set to `true`, the new row is deep-merged into the existing
            row, if one is found. If no existing row is found, the new row is
            inserted as is.


            For example, say there is an existing row in the DB `{"id": "foo",
            "input": {"a": 5, "b": 10}}`. If we merge a new row as
            `{"_is_merge": true, "id": "foo", "input": {"b": 11, "c": 20}}`, the
            new row will be `{"id": "foo", "input": {"a": 5, "b": 11, "c":
            20}}`. If we replace the new row as `{"id": "foo", "input": {"b":
            11, "c": 20}}`, the new row will be `{"id": "foo", "input": {"b":
            11, "c": 20}}`
        _merge_paths:
          type: array
          nullable: true
          items:
            type: array
            items:
              type: string
          description: >-
            The `_merge_paths` field allows controlling the depth of the merge,
            when `_is_merge=true`. `_merge_paths` is a list of paths, where each
            path is a list of field names. The deep merge will not descend below
            any of the specified merge paths.


            For example, say there is an existing row in the DB `{"id": "foo",
            "input": {"a": {"b": 10}, "c": {"d": 20}}, "output": {"a": 20}}`. If
            we merge a new row as `{"_is_merge": true, "_merge_paths":
            [["input", "a"], ["output"]], "input": {"a": {"q": 30}, "c": {"e":
            30}, "bar": "baz"}, "output": {"d": 40}}`, the new row will be
            `{"id": "foo": "input": {"a": {"q": 30}, "c": {"d": 20, "e": 30},
            "bar": "baz"}, "output": {"d": 40}}`. In this case, due to the merge
            paths, we have replaced `input.a` and `output`, but have still
            deep-merged `input` and `input.c`.
        _parent_id:
          type: string
          nullable: true
          description: >-
            DEPRECATED: The `_parent_id` field is deprecated and should not be
            used. Support for `_parent_id` will be dropped in a future version
            of Braintrust. Log `span_id`, `root_span_id`, and `span_parents`
            explicitly instead.


            Use the `_parent_id` field to create this row as a subspan of an
            existing row. Tracking hierarchical relationships are important for
            tracing (see the
            [guide](https://www.braintrust.dev/docs/guides/tracing) for full
            details).


            For example, say we have logged a row `{"id": "abc", "input": "foo",
            "output": "bar", "expected": "boo", "scores": {"correctness":
            0.33}}`. We can create a sub-span of the parent row by logging
            `{"_parent_id": "abc", "id": "llm_call", "input": {"prompt": "What
            comes after foo?"}, "output": "bar", "metrics": {"tokens": 1}}`. In
            the webapp, only the root span row `"abc"` will show up in the
            summary view. You can view the full trace hierarchy (in this case,
            the `"llm_call"` row) by clicking on the "abc" row.


            If the row is being merged into an existing row, this field will be
            ignored.
        span_id:
          type: string
          nullable: true
          description: >-
            Use `span_id`, `root_span_id`, and `span_parents` instead of
            `_parent_id`, which is now deprecated. The span_id is a unique
            identifier describing the row's place in the a trace, and the
            root_span_id is a unique identifier for the whole trace. See the
            [guide](https://www.braintrust.dev/docs/guides/tracing) for full
            details.


            For example, say we have logged a row `{"id": "abc", "span_id":
            "span0", "root_span_id": "root_span0", "input": "foo", "output":
            "bar", "expected": "boo", "scores": {"correctness": 0.33}}`. We can
            create a sub-span of the parent row by logging `{"id": "llm_call",
            "span_id": "span1", "root_span_id": "root_span0", "span_parents":
            ["span0"], "input": {"prompt": "What comes after foo?"}, "output":
            "bar", "metrics": {"tokens": 1}}`. In the webapp, only the root span
            row `"abc"` will show up in the summary view. You can view the full
            trace hierarchy (in this case, the `"llm_call"` row) by clicking on
            the "abc" row.


            If the row is being merged into an existing row, this field will be
            ignored.
        root_span_id:
          type: string
          nullable: true
          description: >-
            Use `span_id`, `root_span_id`, and `span_parents` instead of
            `_parent_id`, which is now deprecated. The span_id is a unique
            identifier describing the row's place in the a trace, and the
            root_span_id is a unique identifier for the whole trace. See the
            [guide](https://www.braintrust.dev/docs/guides/tracing) for full
            details.


            For example, say we have logged a row `{"id": "abc", "span_id":
            "span0", "root_span_id": "root_span0", "input": "foo", "output":
            "bar", "expected": "boo", "scores": {"correctness": 0.33}}`. We can
            create a sub-span of the parent row by logging `{"id": "llm_call",
            "span_id": "span1", "root_span_id": "root_span0", "span_parents":
            ["span0"], "input": {"prompt": "What comes after foo?"}, "output":
            "bar", "metrics": {"tokens": 1}}`. In the webapp, only the root span
            row `"abc"` will show up in the summary view. You can view the full
            trace hierarchy (in this case, the `"llm_call"` row) by clicking on
            the "abc" row.


            If the row is being merged into an existing row, this field will be
            ignored.
        span_parents:
          type: array
          nullable: true
          items:
            type: string
          description: >-
            Use `span_id`, `root_span_id`, and `span_parents` instead of
            `_parent_id`, which is now deprecated. The span_id is a unique
            identifier describing the row's place in the a trace, and the
            root_span_id is a unique identifier for the whole trace. See the
            [guide](https://www.braintrust.dev/docs/guides/tracing) for full
            details.


            For example, say we have logged a row `{"id": "abc", "span_id":
            "span0", "root_span_id": "root_span0", "input": "foo", "output":
            "bar", "expected": "boo", "scores": {"correctness": 0.33}}`. We can
            create a sub-span of the parent row by logging `{"id": "llm_call",
            "span_id": "span1", "root_span_id": "root_span0", "span_parents":
            ["span0"], "input": {"prompt": "What comes after foo?"}, "output":
            "bar", "metrics": {"tokens": 1}}`. In the webapp, only the root span
            row `"abc"` will show up in the summary view. You can view the full
            trace hierarchy (in this case, the `"llm_call"` row) by clicking on
            the "abc" row.


            If the row is being merged into an existing row, this field will be
            ignored.
      description: A dataset event
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