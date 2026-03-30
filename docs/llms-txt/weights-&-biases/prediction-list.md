# Source: https://docs.wandb.ai/weave/reference/service-api/predictions/prediction-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Prediction List

> List predictions.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json get /v2/{entity}/{project}/predictions
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/predictions:
    get:
      tags:
        - Predictions
      summary: Prediction List
      description: List predictions.
      operationId: prediction_list_v2__entity___project__predictions_get
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
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: Filter by evaluation run ID
            title: Evaluation Run Id
          description: Filter by evaluation run ID
        - name: limit
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: Maximum number of predictions to return
            title: Limit
          description: Maximum number of predictions to return
        - name: offset
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: Number of predictions to skip
            title: Offset
          description: Number of predictions to skip
      responses:
        '200':
          description: Stream of data in JSONL format
          content:
            application/jsonl:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/PredictionReadRes'
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
    PredictionReadRes:
      properties:
        prediction_id:
          type: string
          title: Prediction Id
          description: The prediction ID
        model:
          type: string
          title: Model
          description: The model reference (weave:// URI)
        inputs:
          additionalProperties: true
          type: object
          title: Inputs
          description: The inputs to the prediction
        output:
          title: Output
          description: The output of the prediction
        evaluation_run_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Evaluation Run Id
          description: Evaluation run ID if this prediction is linked to one
        wb_user_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Wb User Id
          description: Do not set directly. Server will automatically populate this field.
      type: object
      required:
        - prediction_id
        - model
        - inputs
        - output
      title: PredictionReadRes
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