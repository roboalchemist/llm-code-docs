# Source: https://docs.wandb.ai/weave/reference/service-api/evaluations/evaluation-read.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluation Read

> Get an evaluation object.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json get /v2/{entity}/{project}/evaluations/{object_id}/versions/{digest}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/evaluations/{object_id}/versions/{digest}:
    get:
      tags:
        - Evaluations
      summary: Evaluation Read
      description: Get an evaluation object.
      operationId: >-
        evaluation_read_v2__entity___project__evaluations__object_id__versions__digest__get
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
        - name: object_id
          in: path
          required: true
          schema:
            type: string
            title: Object Id
        - name: digest
          in: path
          required: true
          schema:
            type: string
            title: Digest
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EvaluationReadRes'
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
    EvaluationReadRes:
      properties:
        object_id:
          type: string
          title: Object Id
          description: The evaluation ID
        digest:
          type: string
          title: Digest
          description: The digest of the evaluation
        version_index:
          type: integer
          title: Version Index
          description: The version index of the evaluation
        created_at:
          type: string
          format: date-time
          title: Created At
          description: When the evaluation was created
        name:
          type: string
          title: Name
          description: The name of the evaluation
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: A description of the evaluation
        dataset:
          type: string
          title: Dataset
          description: Dataset reference (weave:// URI)
        scorers:
          items:
            type: string
          type: array
          title: Scorers
          description: List of scorer references (weave:// URIs)
        trials:
          type: integer
          title: Trials
          description: Number of trials
        evaluation_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Evaluation Name
          description: Name for the evaluation run
        evaluate_op:
          anyOf:
            - type: string
            - type: 'null'
          title: Evaluate Op
          description: Evaluate op reference (weave:// URI)
        predict_and_score_op:
          anyOf:
            - type: string
            - type: 'null'
          title: Predict And Score Op
          description: Predict and score op reference (weave:// URI)
        summarize_op:
          anyOf:
            - type: string
            - type: 'null'
          title: Summarize Op
          description: Summarize op reference (weave:// URI)
      type: object
      required:
        - object_id
        - digest
        - version_index
        - created_at
        - name
        - dataset
        - scorers
        - trials
      title: EvaluationReadRes
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