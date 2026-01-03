# Source: https://braintrust.dev/docs/api-reference/experiments/list-experiments.md

# List experiments

> List out all experiments. The experiments are sorted by creation date, with the most recently-created experiments coming first



## OpenAPI

````yaml openapi.yaml get /v1/experiment
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
  /v1/experiment:
    get:
      tags:
        - Experiments
      summary: List experiments
      description: >-
        List out all experiments. The experiments are sorted by creation date,
        with the most recently-created experiments coming first
      operationId: getExperiment
      parameters:
        - $ref: '#/components/parameters/AppLimitParam'
        - $ref: '#/components/parameters/StartingAfter'
        - $ref: '#/components/parameters/EndingBefore'
        - $ref: '#/components/parameters/Ids'
        - $ref: '#/components/parameters/ExperimentName'
        - $ref: '#/components/parameters/ProjectName'
        - $ref: '#/components/parameters/ProjectIdQuery'
        - $ref: '#/components/parameters/OrgName'
      responses:
        '200':
          description: Returns a list of experiment objects
          content:
            application/json:
              schema:
                type: object
                properties:
                  objects:
                    type: array
                    items:
                      $ref: '#/components/schemas/Experiment'
                    description: A list of experiment objects
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
    ExperimentName:
      schema:
        $ref: '#/components/schemas/ExperimentName'
      required: false
      description: Name of the experiment to search for
      name: experiment_name
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
  schemas:
    Experiment:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the experiment
        project_id:
          type: string
          format: uuid
          description: Unique identifier for the project that the experiment belongs under
        name:
          type: string
          description: >-
            Name of the experiment. Within a project, experiment names are
            unique
        description:
          type: string
          nullable: true
          description: Textual description of the experiment
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of experiment creation
        repo_info:
          $ref: '#/components/schemas/RepoInfo'
        commit:
          type: string
          nullable: true
          description: Commit, taken directly from `repo_info.commit`
        base_exp_id:
          type: string
          nullable: true
          format: uuid
          description: >-
            Id of default base experiment to compare against when viewing this
            experiment
        deleted_at:
          type: string
          nullable: true
          format: date-time
          description: >-
            Date of experiment deletion, or null if the experiment is still
            active
        dataset_id:
          type: string
          nullable: true
          format: uuid
          description: >-
            Identifier of the linked dataset, or null if the experiment is not
            linked to a dataset
        dataset_version:
          type: string
          nullable: true
          description: >-
            Version number of the linked dataset the experiment was run against.
            This can be used to reproduce the experiment after the dataset has
            been modified.
        public:
          type: boolean
          description: >-
            Whether or not the experiment is public. Public experiments can be
            viewed by anybody inside or outside the organization
        user_id:
          type: string
          nullable: true
          format: uuid
          description: Identifies the user who created the experiment
        metadata:
          type: object
          nullable: true
          additionalProperties:
            nullable: true
          description: User-controlled metadata about the experiment
        tags:
          type: array
          nullable: true
          items:
            type: string
          description: A list of tags for the experiment
      required:
        - id
        - project_id
        - name
        - public
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
    ExperimentName:
      type: string
      description: Name of the experiment to search for
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