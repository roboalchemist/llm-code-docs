# Source: https://braintrust.dev/docs/api-reference/projectscores/list-project_scores.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List project_scores

> List out all project_scores. The project_scores are sorted by creation date, with the most recently-created project_scores coming first



## OpenAPI

````yaml openapi.yaml get /v1/project_score
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
  /v1/project_score:
    get:
      tags:
        - ProjectScores
      summary: List project_scores
      description: >-
        List out all project_scores. The project_scores are sorted by creation
        date, with the most recently-created project_scores coming first
      operationId: getProjectScore
      parameters:
        - $ref: '#/components/parameters/AppLimitParam'
        - $ref: '#/components/parameters/StartingAfter'
        - $ref: '#/components/parameters/EndingBefore'
        - $ref: '#/components/parameters/Ids'
        - $ref: '#/components/parameters/ProjectScoreName'
        - $ref: '#/components/parameters/ProjectName'
        - $ref: '#/components/parameters/ProjectIdQuery'
        - $ref: '#/components/parameters/OrgName'
        - $ref: '#/components/parameters/ProjectScoreType'
      responses:
        '200':
          description: Returns a list of project_score objects
          content:
            application/json:
              schema:
                type: object
                properties:
                  objects:
                    type: array
                    items:
                      $ref: '#/components/schemas/ProjectScore'
                    description: A list of project_score objects
                required:
                  - objects
                additionalProperties: false
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
    AppLimitParam:
      schema:
        $ref: '#/components/schemas/AppLimitParam'
      required: false
      description: Limit the number of objects to return
      name: limit
      in: query
    StartingAfter:
      schema:
        $ref: '#/components/schemas/StartingAfter'
      required: false
      description: >-
        Pagination cursor id.


        For example, if the final item in the last page you fetched had an id of
        `foo`, pass `starting_after=foo` to fetch the next page. Note: you may
        only pass one of `starting_after` and `ending_before`
      name: starting_after
      in: query
    EndingBefore:
      schema:
        $ref: '#/components/schemas/EndingBefore'
      required: false
      description: >-
        Pagination cursor id.


        For example, if the initial item in the last page you fetched had an id
        of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you
        may only pass one of `starting_after` and `ending_before`
      name: ending_before
      in: query
    Ids:
      schema:
        $ref: '#/components/schemas/Ids'
      required: false
      description: >-
        Filter search results to a particular set of object IDs. To specify a
        list of IDs, include the query param multiple times
      name: ids
      in: query
    ProjectScoreName:
      schema:
        $ref: '#/components/schemas/ProjectScoreName'
      required: false
      description: Name of the project_score to search for
      name: project_score_name
      in: query
      allowReserved: true
    ProjectName:
      schema:
        $ref: '#/components/schemas/ProjectName'
      required: false
      description: Name of the project to search for
      name: project_name
      in: query
      allowReserved: true
    ProjectIdQuery:
      schema:
        $ref: '#/components/schemas/ProjectIdQuery'
      required: false
      description: Project id
      name: project_id
      in: query
    OrgName:
      schema:
        $ref: '#/components/schemas/OrgName'
      required: false
      description: Filter search results to within a particular organization
      name: org_name
      in: query
      allowReserved: true
    ProjectScoreType:
      schema:
        anyOf:
          - $ref: '#/components/schemas/ProjectScoreType'
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/ProjectScoreType'
                - title: project_score_type
      required: false
      name: score_type
      in: query
  schemas:
    ProjectScore:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the project score
        project_id:
          type: string
          format: uuid
          description: >-
            Unique identifier for the project that the project score belongs
            under
        user_id:
          type: string
          format: uuid
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of project score creation
        name:
          type: string
          description: Name of the project score
        description:
          type: string
          nullable: true
          description: Textual description of the project score
        score_type:
          $ref: '#/components/schemas/ProjectScoreType'
        categories:
          $ref: '#/components/schemas/ProjectScoreCategories'
        config:
          $ref: '#/components/schemas/ProjectScoreConfig'
        position:
          type: string
          nullable: true
          description: >-
            An optional LexoRank-based string that sets the sort position for
            the score in the UI
      required:
        - id
        - project_id
        - user_id
        - name
        - score_type
      description: >-
        A project score is a user-configured score, which can be
        manually-labeled through the UI
    AppLimitParam:
      type: integer
      nullable: true
      minimum: 0
      description: Limit the number of objects to return
    StartingAfter:
      type: string
      format: uuid
      description: >-
        Pagination cursor id.


        For example, if the final item in the last page you fetched had an id of
        `foo`, pass `starting_after=foo` to fetch the next page. Note: you may
        only pass one of `starting_after` and `ending_before`
    EndingBefore:
      type: string
      format: uuid
      description: >-
        Pagination cursor id.


        For example, if the initial item in the last page you fetched had an id
        of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you
        may only pass one of `starting_after` and `ending_before`
    Ids:
      anyOf:
        - type: string
          format: uuid
        - type: array
          items:
            type: string
            format: uuid
      description: >-
        Filter search results to a particular set of object IDs. To specify a
        list of IDs, include the query param multiple times
    ProjectScoreName:
      type: string
      description: Name of the project_score to search for
    ProjectName:
      type: string
      description: Name of the project to search for
    ProjectIdQuery:
      type: string
      format: uuid
      description: Project id
    OrgName:
      type: string
      description: Filter search results to within a particular organization
    ProjectScoreType:
      type: string
      enum:
        - slider
        - categorical
        - weighted
        - minimum
        - maximum
        - online
        - free-form
      description: The type of the configured score
      title: project_score_type_single
    ProjectScoreCategories:
      anyOf:
        - type: array
          items:
            $ref: '#/components/schemas/ProjectScoreCategory'
          description: For categorical-type project scores, the list of all categories
          title: categorical
        - type: object
          additionalProperties:
            type: number
          description: For weighted-type project scores, the weights of each score
          title: weighted
          x-stainless-skip:
            - go
        - type: array
          items:
            type: string
          description: For minimum-type project scores, the list of included scores
          title: minimum
        - type: 'null'
    ProjectScoreConfig:
      type: object
      nullable: true
      properties:
        multi_select:
          type: boolean
          nullable: true
        destination:
          type: string
          nullable: true
        online:
          $ref: '#/components/schemas/OnlineScoreConfig'
    ProjectScoreCategory:
      type: object
      properties:
        name:
          type: string
          description: Name of the category
        value:
          type: number
          description: Numerical value of the category. Must be between 0 and 1, inclusive
      required:
        - name
        - value
      description: For categorical-type project scores, defines a single category
    OnlineScoreConfig:
      type: object
      nullable: true
      properties:
        sampling_rate:
          type: number
          minimum: 0
          maximum: 1
          description: The sampling rate for online scoring
        scorers:
          type: array
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
          description: >-
            The list of functions to run for online scoring. Can include
            scorers, facets, or other function types.
        btql_filter:
          type: string
          nullable: true
          description: Filter logs using BTQL
        apply_to_root_span:
          type: boolean
          nullable: true
          description: >-
            Whether to trigger online scoring on the root span of each trace.
            Only applies when scope is 'span' or unset.
        apply_to_span_names:
          type: array
          nullable: true
          items:
            type: string
          description: >-
            Trigger online scoring on any spans with a name in this list. Only
            applies when scope is 'span' or unset.
        skip_logging:
          type: boolean
          nullable: true
          description: Whether to skip adding scorer spans when computing scores
        scope:
          anyOf:
            - $ref: '#/components/schemas/SpanScope'
            - $ref: '#/components/schemas/TraceScope'
            - $ref: '#/components/schemas/GroupScope'
            - type: 'null'
          description: >-
            The scope at which to run the functions. Defaults to span-level
            execution. Trace/group scope requires all functions to be facets.
      required:
        - sampling_rate
        - scorers
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
    SpanScope:
      type: object
      properties:
        type:
          type: string
          enum:
            - span
      required:
        - type
      description: Process individual spans
    TraceScope:
      type: object
      properties:
        type:
          type: string
          enum:
            - trace
        idle_seconds:
          type: number
          description: >-
            Consider trace complete after this many seconds of inactivity
            (default: 30)
      required:
        - type
      description: Process entire traces (all spans sharing the same root_span_id)
    GroupScope:
      type: object
      properties:
        type:
          type: string
          enum:
            - group
        group_by:
          type: string
          description: Field path to group by, e.g. metadata.session_id
        idle_seconds:
          type: number
          description: 'Optional: trigger after this many seconds of inactivity'
      required:
        - type
        - group_by
      description: Process spans/traces grouped by a field (e.g., session_id)
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