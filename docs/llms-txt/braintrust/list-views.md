# Source: https://braintrust.dev/docs/api-reference/views/list-views.md

# List views

> List out all views. The views are sorted by creation date, with the most recently-created views coming first



## OpenAPI

````yaml openapi.yaml get /v1/view
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
  /v1/view:
    get:
      tags:
        - Views
      summary: List views
      description: >-
        List out all views. The views are sorted by creation date, with the most
        recently-created views coming first
      operationId: getView
      parameters:
        - $ref: '#/components/parameters/AppLimitParam'
        - $ref: '#/components/parameters/StartingAfter'
        - $ref: '#/components/parameters/EndingBefore'
        - $ref: '#/components/parameters/Ids'
        - $ref: '#/components/parameters/ViewName'
        - $ref: '#/components/parameters/ViewType'
        - $ref: '#/components/parameters/AclObjectType'
        - $ref: '#/components/parameters/AclObjectId'
      responses:
        '200':
          description: Returns a list of view objects
          content:
            application/json:
              schema:
                type: object
                properties:
                  objects:
                    type: array
                    items:
                      $ref: '#/components/schemas/View'
                    description: A list of view objects
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
    ViewName:
      schema:
        $ref: '#/components/schemas/ViewName'
      required: false
      description: Name of the view to search for
      name: view_name
      in: query
      allowReserved: true
    ViewType:
      schema:
        $ref: '#/components/schemas/ViewType'
      required: false
      description: Type of object that the view corresponds to.
      name: view_type
      in: query
    AclObjectType:
      schema:
        $ref: '#/components/schemas/AclObjectType'
      required: true
      description: The object type that the ACL applies to
      name: object_type
      in: query
    AclObjectId:
      schema:
        $ref: '#/components/schemas/AclObjectId'
      required: true
      description: The id of the object the ACL applies to
      name: object_id
      in: query
  schemas:
    View:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the view
        object_type:
          $ref: '#/components/schemas/AclObjectType'
        object_id:
          type: string
          format: uuid
          description: The id of the object the view applies to
        view_type:
          type: string
          enum:
            - projects
            - experiments
            - experiment
            - playgrounds
            - playground
            - datasets
            - dataset
            - prompts
            - tools
            - scorers
            - logs
            - agents
            - monitor
            - for_review
            - null
          description: Type of object that the view corresponds to.
        name:
          type: string
          description: Name of the view
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of view creation
        view_data:
          $ref: '#/components/schemas/ViewData'
        options:
          $ref: '#/components/schemas/ViewOptions'
        user_id:
          type: string
          nullable: true
          format: uuid
          description: Identifies the user who created the view
        deleted_at:
          type: string
          nullable: true
          format: date-time
          description: Date of role deletion, or null if the role is still active
      required:
        - id
        - object_type
        - object_id
        - view_type
        - name
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
    ViewName:
      type: string
      description: Name of the view to search for
    ViewType:
      type: string
      enum:
        - projects
        - experiments
        - experiment
        - playgrounds
        - playground
        - datasets
        - dataset
        - prompts
        - tools
        - scorers
        - logs
        - agents
        - monitor
        - for_review
        - null
      description: Type of object that the view corresponds to.
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
    AclObjectId:
      type: string
      format: uuid
      description: The id of the object the ACL applies to
    ViewData:
      type: object
      nullable: true
      properties:
        search:
          $ref: '#/components/schemas/ViewDataSearch'
        custom_charts:
          nullable: true
      description: The view definition
    ViewOptions:
      anyOf:
        - type: object
          properties:
            viewType:
              type: string
              enum:
                - monitor
            options:
              type: object
              properties:
                spanType:
                  type: string
                  nullable: true
                  enum:
                    - range
                    - frame
                    - null
                rangeValue:
                  type: string
                  nullable: true
                frameStart:
                  type: string
                  nullable: true
                frameEnd:
                  type: string
                  nullable: true
                tzUTC:
                  type: boolean
                  nullable: true
                chartVisibility:
                  type: object
                  nullable: true
                  additionalProperties:
                    type: boolean
                projectId:
                  type: string
                  nullable: true
                type:
                  type: string
                  nullable: true
                  enum:
                    - project
                    - experiment
                    - null
                groupBy:
                  type: string
                  nullable: true
            freezeColumns:
              type: boolean
              nullable: true
          required:
            - viewType
            - options
          title: MonitorViewOptions
        - type: object
          properties:
            columnVisibility:
              type: object
              nullable: true
              additionalProperties:
                type: boolean
            columnOrder:
              type: array
              nullable: true
              items:
                type: string
            columnSizing:
              type: object
              nullable: true
              additionalProperties:
                type: number
            grouping:
              type: string
              nullable: true
            rowHeight:
              type: string
              nullable: true
            tallGroupRows:
              type: boolean
              nullable: true
            layout:
              type: string
              nullable: true
            chartHeight:
              type: number
              nullable: true
            excludedMeasures:
              type: array
              nullable: true
              items:
                type: object
                properties:
                  type:
                    type: string
                    enum:
                      - none
                      - score
                      - metric
                      - metadata
                  value:
                    type: string
                required:
                  - type
                  - value
            yMetric:
              type: object
              nullable: true
              properties:
                type:
                  type: string
                  enum:
                    - none
                    - score
                    - metric
                    - metadata
                value:
                  type: string
              required:
                - type
                - value
            xAxis:
              type: object
              nullable: true
              properties:
                type:
                  type: string
                  enum:
                    - none
                    - score
                    - metric
                    - metadata
                value:
                  type: string
              required:
                - type
                - value
            symbolGrouping:
              type: object
              nullable: true
              properties:
                type:
                  type: string
                  enum:
                    - none
                    - score
                    - metric
                    - metadata
                value:
                  type: string
              required:
                - type
                - value
            xAxisAggregation:
              type: string
              nullable: true
              description: One of 'avg', 'sum', 'min', 'max', 'median', 'all'
            chartAnnotations:
              type: array
              nullable: true
              items:
                type: object
                properties:
                  id:
                    type: string
                  text:
                    type: string
                required:
                  - id
                  - text
            timeRangeFilter:
              anyOf:
                - type: string
                - type: object
                  properties:
                    from:
                      type: string
                    to:
                      type: string
                  required:
                    - from
                    - to
                - type: 'null'
            queryShape:
              type: string
              nullable: true
              enum:
                - traces
                - spans
                - null
            freezeColumns:
              type: boolean
              nullable: true
          title: TableViewOptions
        - type: 'null'
      description: Options for the view in the app
    ViewDataSearch:
      type: object
      nullable: true
      properties:
        filter:
          type: array
          nullable: true
          items:
            nullable: true
        tag:
          type: array
          nullable: true
          items:
            nullable: true
        match:
          type: array
          nullable: true
          items:
            nullable: true
        sort:
          type: array
          nullable: true
          items:
            nullable: true
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