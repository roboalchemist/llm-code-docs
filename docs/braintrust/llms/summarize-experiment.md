# Source: https://braintrust.dev/docs/api-reference/experiments/summarize-experiment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Summarize experiment

> Summarize experiment



## OpenAPI

````yaml openapi.yaml get /v1/experiment/{experiment_id}/summarize
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
  /v1/experiment/{experiment_id}/summarize:
    get:
      tags:
        - Experiments
      summary: Summarize experiment
      description: Summarize experiment
      operationId: getExperimentIdSummarize
      parameters:
        - $ref: '#/components/parameters/ExperimentIdParam'
        - $ref: '#/components/parameters/SummarizeScores'
        - $ref: '#/components/parameters/ComparisonExperimentId'
      responses:
        '200':
          description: Experiment summary
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SummarizeExperimentResponse'
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
components:
  parameters:
    ExperimentIdParam:
      schema:
        $ref: '#/components/schemas/ExperimentIdParam'
      required: true
      description: Experiment id
      name: experiment_id
      in: path
    SummarizeScores:
      schema:
        $ref: '#/components/schemas/SummarizeScores'
      required: false
      description: >-
        Whether to summarize the scores and metrics. If false (or omitted), only
        the metadata will be returned.
      name: summarize_scores
      in: query
    ComparisonExperimentId:
      schema:
        $ref: '#/components/schemas/ComparisonExperimentId'
      required: false
      description: >-
        The experiment to compare against, if summarizing scores and metrics. If
        omitted, will fall back to the `base_exp_id` stored in the experiment
        metadata, and then to the most recent experiment run in the same
        project. Must pass `summarize_scores=true` for this id to be used
      name: comparison_experiment_id
      in: query
  schemas:
    SummarizeExperimentResponse:
      type: object
      properties:
        project_name:
          type: string
          description: Name of the project that the experiment belongs to
        experiment_name:
          type: string
          description: Name of the experiment
        project_url:
          type: string
          format: uri
          description: URL to the project's page in the Braintrust app
        experiment_url:
          type: string
          format: uri
          description: URL to the experiment's page in the Braintrust app
        comparison_experiment_name:
          type: string
          nullable: true
          description: The experiment which scores are baselined against
        scores:
          type: object
          nullable: true
          additionalProperties:
            $ref: '#/components/schemas/ScoreSummary'
          description: Summary of the experiment's scores
        metrics:
          type: object
          nullable: true
          additionalProperties:
            $ref: '#/components/schemas/MetricSummary'
          description: Summary of the experiment's metrics
      required:
        - project_name
        - experiment_name
        - project_url
        - experiment_url
      description: Summary of an experiment
    ExperimentIdParam:
      type: string
      format: uuid
      description: Experiment id
    SummarizeScores:
      type: boolean
      nullable: true
      description: >-
        Whether to summarize the scores and metrics. If false (or omitted), only
        the metadata will be returned.
    ComparisonExperimentId:
      type: string
      format: uuid
      description: >-
        The experiment to compare against, if summarizing scores and metrics. If
        omitted, will fall back to the `base_exp_id` stored in the experiment
        metadata, and then to the most recent experiment run in the same
        project. Must pass `summarize_scores=true` for this id to be used
    ScoreSummary:
      type: object
      properties:
        name:
          type: string
          description: Name of the score
        score:
          type: number
          minimum: 0
          maximum: 1
          description: Average score across all examples
        diff:
          type: number
          minimum: -1
          maximum: 1
          description: Difference in score between the current and comparison experiment
        improvements:
          type: integer
          minimum: 0
          description: Number of improvements in the score
        regressions:
          type: integer
          minimum: 0
          description: Number of regressions in the score
      required:
        - name
        - score
        - improvements
        - regressions
      description: Summary of a score's performance
    MetricSummary:
      type: object
      properties:
        name:
          type: string
          description: Name of the metric
        metric:
          type: number
          description: Average metric across all examples
        unit:
          type: string
          description: Unit label for the metric
        diff:
          type: number
          description: Difference in metric between the current and comparison experiment
        improvements:
          type: integer
          minimum: 0
          description: Number of improvements in the metric
        regressions:
          type: integer
          minimum: 0
          description: Number of regressions in the metric
      required:
        - name
        - metric
        - unit
        - improvements
        - regressions
      description: Summary of a metric's performance
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