# Source: https://docs.wandb.ai/weave/reference/service-api/evaluation-runs/evaluation-run-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluation Run Delete

> Delete evaluation runs.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json delete /v2/{entity}/{project}/evaluation_runs
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/evaluation_runs:
    delete:
      tags:
        - Evaluation Runs
      summary: Evaluation Run Delete
      description: Delete evaluation runs.
      operationId: evaluation_run_delete_v2__entity___project__evaluation_runs_delete
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
        - name: evaluation_run_ids
          in: query
          required: true
          schema:
            type: array
            items:
              type: string
            description: List of evaluation run IDs to delete
            title: Evaluation Run Ids
          description: List of evaluation run IDs to delete
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EvaluationRunDeleteRes'
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
    EvaluationRunDeleteRes:
      properties:
        num_deleted:
          type: integer
          title: Num Deleted
          description: Number of evaluation runs deleted
      type: object
      required:
        - num_deleted
      title: EvaluationRunDeleteRes
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