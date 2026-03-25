# Source: https://docs.wandb.ai/weave/reference/service-api/evaluations/evaluation-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluation Create

> Create an evaluation object.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /v2/{entity}/{project}/evaluations
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/evaluations:
    post:
      tags:
        - Evaluations
      summary: Evaluation Create
      description: Create an evaluation object.
      operationId: evaluation_create_v2__entity___project__evaluations_post
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
              $ref: '#/components/schemas/EvaluationCreateBody'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EvaluationCreateRes'
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
    EvaluationCreateBody:
      properties:
        name:
          type: string
          title: Name
          description: >-
            The name of this evaluation.  Evaluations with the same name will be
            versioned together.
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: A description of this evaluation
        dataset:
          type: string
          title: Dataset
          description: Reference to the dataset (weave:// URI)
        scorers:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Scorers
          description: List of scorer references (weave:// URIs)
        trials:
          type: integer
          title: Trials
          description: Number of trials to run
          default: 1
        evaluation_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Evaluation Name
          description: Name for the evaluation run
        eval_attributes:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Eval Attributes
          description: Optional attributes for the evaluation
      type: object
      required:
        - name
        - dataset
      title: EvaluationCreateBody
    EvaluationCreateRes:
      properties:
        digest:
          type: string
          title: Digest
          description: The digest of the created evaluation
        object_id:
          type: string
          title: Object Id
          description: The ID of the created evaluation
        version_index:
          type: integer
          title: Version Index
          description: The version index of the created evaluation
        evaluation_ref:
          type: string
          title: Evaluation Ref
          description: Full reference to the created evaluation
      type: object
      required:
        - digest
        - object_id
        - version_index
        - evaluation_ref
      title: EvaluationCreateRes
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