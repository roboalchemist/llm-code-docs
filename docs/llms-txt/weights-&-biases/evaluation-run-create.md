# Source: https://docs.wandb.ai/weave/reference/service-api/evaluation-runs/evaluation-run-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluation Run Create

> Create an evaluation run.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /v2/{entity}/{project}/evaluation_runs
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/evaluation_runs:
    post:
      tags:
        - Evaluation Runs
      summary: Evaluation Run Create
      description: Create an evaluation run.
      operationId: evaluation_run_create_v2__entity___project__evaluation_runs_post
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EvaluationRunCreateBody'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EvaluationRunCreateRes'
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
    EvaluationRunCreateBody:
      properties:
        evaluation:
          type: string
          title: Evaluation
          description: Reference to the evaluation (weave:// URI)
        model:
          type: string
          title: Model
          description: Reference to the model (weave:// URI)
      type: object
      required:
        - evaluation
        - model
      title: EvaluationRunCreateBody
    EvaluationRunCreateRes:
      properties:
        evaluation_run_id:
          type: string
          title: Evaluation Run Id
          description: The ID of the created evaluation run
      type: object
      required:
        - evaluation_run_id
      title: EvaluationRunCreateRes
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