# Source: https://braintrust.dev/docs/api-reference/experiments/get-experiment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get experiment

> Get an experiment object by its id



## OpenAPI

````yaml openapi.yaml get /v1/experiment/{experiment_id}
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
  /v1/experiment/{experiment_id}:
    get:
      tags:
        - Experiments
      summary: Get experiment
      description: Get an experiment object by its id
      operationId: getExperimentId
      parameters:
        - $ref: '#/components/parameters/ExperimentIdParam'
      responses:
        '200':
          description: Returns the experiment object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Experiment'
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
    ExperimentIdParam:
      type: string
      format: uuid
      description: Experiment id
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