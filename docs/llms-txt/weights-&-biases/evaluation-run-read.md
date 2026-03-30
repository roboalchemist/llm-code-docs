# Source: https://docs.wandb.ai/weave/reference/service-api/evaluation-runs/evaluation-run-read.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluation Run Read

> Read an evaluation run.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json get /v2/{entity}/{project}/evaluation_runs/{evaluation_run_id}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/evaluation_runs/{evaluation_run_id}:
    get:
      tags:
        - Evaluation Runs
      summary: Evaluation Run Read
      description: Read an evaluation run.
      operationId: >-
        evaluation_run_read_v2__entity___project__evaluation_runs__evaluation_run_id__get
      parameters:
        - name: entity
          in: path
          required: true
          schema:
            type: string
            title: Entity
        - name: project
          in: path
          required: true
          schema:
            type: string
            title: Project
        - name: evaluation_run_id
          in: path
          required: true
          schema:
            type: string
            title: Evaluation Run Id
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EvaluationRunReadRes'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - HTTPBasic: []
components:
  schemas:
    EvaluationRunReadRes:
      properties:
        evaluation_run_id:
          type: string
          title: Evaluation Run Id
          description: The evaluation run ID
        evaluation:
          type: string
          title: Evaluation
          description: Reference to the evaluation (weave:// URI)
        model:
          type: string
          title: Model
          description: Reference to the model (weave:// URI)
        status:
          anyOf:
            - type: string
            - type: 'null'
          title: Status
          description: Status of the evaluation run
        started_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Started At
          description: When the evaluation run started
        finished_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Finished At
          description: When the evaluation run finished
        summary:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Summary
          description: Summary data for the evaluation run
      type: object
      required:
        - evaluation_run_id
        - evaluation
        - model
      title: EvaluationRunReadRes
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
  securitySchemes:
    HTTPBasic:
      type: http
      scheme: basic

````