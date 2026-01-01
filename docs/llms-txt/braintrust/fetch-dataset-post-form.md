# Source: https://braintrust.dev/docs/api-reference/datasets/fetch-dataset-post-form.md

# Fetch dataset (POST form)

> Fetch the events in a dataset. Equivalent to the GET form of the same path, but with the parameters in the request body rather than in the URL query. For more complex queries, use the `POST /btql` endpoint.



## OpenAPI

````yaml openapi.yaml post /v1/dataset/{dataset_id}/fetch
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
  /v1/dataset/{dataset_id}/fetch:
    post:
      tags:
        - Datasets
      summary: Fetch dataset (POST form)
      description: >-
        Fetch the events in a dataset. Equivalent to the GET form of the same
        path, but with the parameters in the request body rather than in the URL
        query. For more complex queries, use the `POST /btql` endpoint.
      operationId: postDatasetIdFetch
      parameters:
        - $ref: '#/components/parameters/DatasetIdParam'
      requestBody:
        description: Filters for the fetch query
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FetchEventsRequest'
      responses:
        '200':
          description: Returns the fetched rows
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FetchDatasetEventsResponse'
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
    FetchEventsRequest:
      type: object
      properties:
        limit:
          $ref: '#/components/schemas/FetchLimit'
        cursor:
          $ref: '#/components/schemas/FetchPaginationCursor'
        max_xact_id:
          $ref: '#/components/schemas/MaxXactId'
          nullable: true
        max_root_span_id:
          $ref: '#/components/schemas/MaxRootSpanId'
          nullable: true
        version:
          $ref: '#/components/schemas/Version'
          nullable: true
    FetchDatasetEventsResponse:
      type: object
      properties:
        events:
          type: array
          items:
            $ref: '#/components/schemas/DatasetEvent'
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
    DatasetIdParam:
      type: string
      format: uuid
      description: Dataset id
    FetchLimit:
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
    FetchPaginationCursor:
      type: string
      nullable: true
      description: >-
        An opaque string to be used as a cursor for the next page of results, in
        order from latest to earliest.


        The string can be obtained directly from the `cursor` property of the
        previous fetch query
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
    DatasetEvent:
      type: object
      properties:
        id:
          type: string
          description: >-
            A unique identifier for the dataset event. If you don't provide one,
            Braintrust will generate one for you
        _xact_id:
          type: string
          description: >-
            The transaction id of an event is unique to the network operation
            that processed the event insertion. Transaction ids are
            monotonically increasing over time and can be used to retrieve a
            versioned snapshot of the dataset (see the `version` parameter)
        created:
          type: string
          format: date-time
          description: The timestamp the dataset event was created
        _pagination_key:
          type: string
          nullable: true
          description: >-
            A stable, time-ordered key that can be used to paginate over dataset
            events. This field is auto-generated by Braintrust and only exists
            in Brainstore.
        project_id:
          type: string
          format: uuid
          description: Unique identifier for the project that the dataset belongs under
        dataset_id:
          type: string
          format: uuid
          description: Unique identifier for the dataset
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
        span_id:
          type: string
          description: >-
            A unique identifier used to link different dataset events together
            as part of a full trace. See the [tracing
            guide](https://www.braintrust.dev/docs/guides/tracing) for full
            details on tracing
        root_span_id:
          type: string
          description: A unique identifier for the trace this dataset event belongs to
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
      required:
        - id
        - _xact_id
        - created
        - project_id
        - dataset_id
        - span_id
        - root_span_id
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