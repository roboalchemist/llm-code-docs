# Source: https://braintrust.dev/docs/api-reference/views/partially-update-view.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Partially update view

> Partially update a view object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.



## OpenAPI

````yaml openapi.yaml patch /v1/view/{view_id}
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
  /v1/view/{view_id}:
    patch:
      tags:
        - Views
      summary: Partially update view
      description: >-
        Partially update a view object. Specify the fields to update in the
        payload. Any object-type fields will be deep-merged with existing
        content. Currently we do not support removing fields or setting them to
        null.
      operationId: patchViewId
      parameters:
        - $ref: '#/components/parameters/ViewIdParam'
      requestBody:
        description: Fields to update
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchView'
      responses:
        '200':
          description: Returns the view object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/View'
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
    ViewIdParam:
      schema:
        $ref: '#/components/schemas/ViewIdParam'
      required: true
      description: View id
      name: view_id
      in: path
  schemas:
    PatchView:
      type: object
      properties:
        object_type:
          $ref: '#/components/schemas/AclObjectType'
        object_id:
          type: string
          format: uuid
          description: The id of the object the view applies to
        view_type:
          type: string
          nullable: true
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
            - classifiers
            - logs
            - monitor
            - for_review_project_log
            - for_review_experiments
            - for_review_datasets
            - null
          description: Type of object that the view corresponds to.
        name:
          type: string
          nullable: true
          description: Name of the view
        view_data:
          $ref: '#/components/schemas/ViewData'
        options:
          $ref: '#/components/schemas/ViewOptions'
        user_id:
          type: string
          nullable: true
          format: uuid
          description: Identifies the user who created the view
      required:
        - object_type
        - object_id
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
            - classifiers
            - logs
            - monitor
            - for_review_project_log
            - for_review_experiments
            - for_review_datasets
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
    ViewIdParam:
      type: string
      format: uuid
      description: View id
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