# Source: https://docs.wandb.ai/weave/reference/service-api/evaluation-runs/evaluation-run-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluation Run List

> List evaluation runs.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json get /v2/{entity}/{project}/evaluation_runs
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/evaluation_runs:
    get:
      tags:
        - Evaluation Runs
      summary: Evaluation Run List
      description: List evaluation runs.
      operationId: evaluation_run_list_v2__entity___project__evaluation_runs_get
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
        - name: evaluations
          in: query
          required: false
          schema:
            anyOf:
              - items:
                  type: string
                type: array
              - type: 'null'
            description: Filter by evaluation references
            title: Evaluations
          description: Filter by evaluation references
        - name: models
          in: query
          required: false
          schema:
            anyOf:
              - items:
                  type: string
                type: array
              - type: 'null'
            description: Filter by model references
            title: Models
          description: Filter by model references
        - name: evaluation_run_ids
          in: query
          required: false
          schema:
            anyOf:
              - items:
                  type: string
                type: array
              - type: 'null'
            description: Filter by evaluation run IDs
            title: Evaluation Run Ids
          description: Filter by evaluation run IDs
        - name: limit
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: Maximum number of evaluation runs to return
            title: Limit
          description: Maximum number of evaluation runs to return
        - name: offset
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: Number of evaluation runs to skip
            title: Offset
          description: Number of evaluation runs to skip
      responses:
        '200':
          description: Stream of data in JSONL format
          content:
            application/jsonl:
              schema:
                type: array
                items:
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