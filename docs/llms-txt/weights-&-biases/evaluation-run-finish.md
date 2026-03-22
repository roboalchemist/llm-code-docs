# Source: https://docs.wandb.ai/weave/reference/service-api/evaluation-runs/evaluation-run-finish.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluation Run Finish

> Finish an evaluation run.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /v2/{entity}/{project}/evaluation_runs/{evaluation_run_id}/finish
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/evaluation_runs/{evaluation_run_id}/finish:
    post:
      tags:
        - Evaluation Runs
      summary: Evaluation Run Finish
      description: Finish an evaluation run.
      operationId: >-
        evaluation_run_finish_v2__entity___project__evaluation_runs__evaluation_run_id__finish_post
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EvaluationRunFinishBody'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EvaluationRunFinishRes'
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
    EvaluationRunFinishBody:
      properties:
        summary:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Summary
          description: Optional summary dictionary for the evaluation run
      type: object
      title: EvaluationRunFinishBody
      description: >-
        Request body for finishing an evaluation run via REST API.


        This model excludes project_id and evaluation_run_id since they come
        from the URL path in RESTful endpoints.
    EvaluationRunFinishRes:
      properties:
        success:
          type: boolean
          title: Success
          description: Whether the evaluation run was finished successfully
      type: object
      required:
        - success
      title: EvaluationRunFinishRes
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