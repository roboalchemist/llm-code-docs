# Source: https://braintrust.dev/docs/api-reference/projects/delete-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete project

> Delete a project object by its id



## OpenAPI

````yaml openapi.yaml delete /v1/project/{project_id}
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
  /v1/project/{project_id}:
    delete:
      tags:
        - Projects
      summary: Delete project
      description: Delete a project object by its id
      operationId: deleteProjectId
      parameters:
        - $ref: '#/components/parameters/ProjectIdParam'
      responses:
        '200':
          description: Returns the deleted project object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Project'
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
    ProjectIdParam:
      schema:
        $ref: '#/components/schemas/ProjectIdParam'
      required: true
      description: Project id
      name: project_id
      in: path
  schemas:
    Project:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the project
        org_id:
          type: string
          format: uuid
          description: Unique id for the organization that the project belongs under
        name:
          type: string
          description: Name of the project
        description:
          type: string
          nullable: true
          description: Textual description of the project
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of project creation
        deleted_at:
          type: string
          nullable: true
          format: date-time
          description: Date of project deletion, or null if the project is still active
        user_id:
          type: string
          nullable: true
          format: uuid
          description: Identifies the user who created the project
        settings:
          $ref: '#/components/schemas/ProjectSettings'
      required:
        - id
        - org_id
        - name
    ProjectIdParam:
      type: string
      format: uuid
      description: Project id
    ProjectSettings:
      type: object
      nullable: true
      properties:
        comparison_key:
          type: string
          nullable: true
          description: The key used to join two experiments (defaults to `input`)
        baseline_experiment_id:
          type: string
          nullable: true
          format: uuid
          description: >-
            The id of the experiment to use as the default baseline for
            comparisons
        spanFieldOrder:
          type: array
          nullable: true
          items:
            type: object
            properties:
              object_type:
                type: string
              column_id:
                type: string
              position:
                type: string
              layout:
                anyOf:
                  - type: string
                    enum:
                      - full
                  - type: string
                    enum:
                      - two_column
                  - type: 'null'
            required:
              - object_type
              - column_id
              - position
          description: The order of the fields to display in the trace view
        remote_eval_sources:
          type: array
          nullable: true
          items:
            type: object
            properties:
              url:
                type: string
              name:
                type: string
              description:
                type: string
                nullable: true
            required:
              - url
              - name
          description: The remote eval sources to use for the project
        disable_realtime_queries:
          type: boolean
          nullable: true
          description: >-
            If true, disable real-time queries for this project. This can
            improve query performance for high-volume logs.
        default_preprocessor:
          $ref: '#/components/schemas/NullableSavedFunctionId'
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