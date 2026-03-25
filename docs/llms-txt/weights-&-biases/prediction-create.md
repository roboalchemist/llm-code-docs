# Source: https://docs.wandb.ai/weave/reference/service-api/predictions/prediction-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Prediction Create

> Create a prediction.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /v2/{entity}/{project}/predictions
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/predictions:
    post:
      tags:
        - Predictions
      summary: Prediction Create
      description: Create a prediction.
      operationId: prediction_create_v2__entity___project__predictions_post
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
              $ref: '#/components/schemas/PredictionCreateBody'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PredictionCreateRes'
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
    PredictionCreateBody:
      properties:
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
          description: Optional evaluation run ID to link this prediction as a child call
      type: object
      required:
        - model
        - inputs
        - output
      title: PredictionCreateBody
      description: >-
        Request body for creating a Prediction via REST API.


        This model excludes project_id since it comes from the URL path in
        RESTful endpoints.
    PredictionCreateRes:
      properties:
        prediction_id:
          type: string
          title: Prediction Id
          description: The prediction ID
      type: object
      required:
        - prediction_id
      title: PredictionCreateRes
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