# Source: https://braintrust.dev/docs/api-reference/projectscores/delete-project_score.md

# Delete project_score

> Delete a project_score object by its id



## OpenAPI

````yaml openapi.yaml delete /v1/project_score/{project_score_id}
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
  /v1/project_score/{project_score_id}:
    delete:
      tags:
        - ProjectScores
      summary: Delete project_score
      description: Delete a project_score object by its id
      operationId: deleteProjectScoreId
      parameters:
        - $ref: '#/components/parameters/ProjectScoreIdParam'
      responses:
        '200':
          description: Returns the deleted project_score object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProjectScore'
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
    ProjectScoreIdParam:
      schema:
        $ref: '#/components/schemas/ProjectScoreIdParam'
      required: true
      description: ProjectScore id
      name: project_score_id
      in: path
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
    ProjectScoreIdParam:
      type: string
      format: uuid
      description: ProjectScore id
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
            $ref: '#/components/schemas/SavedFunctionId'
          description: The list of scorers to use for online scoring
        btql_filter:
          type: string
          nullable: true
          description: Filter logs using BTQL
        apply_to_root_span:
          type: boolean
          nullable: true
          description: Whether to trigger online scoring on the root span of each trace
        apply_to_span_names:
          type: array
          nullable: true
          items:
            type: string
          description: Trigger online scoring on any spans with a name in this list
        skip_logging:
          type: boolean
          nullable: true
          description: Whether to skip adding scorer spans when computing scores
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