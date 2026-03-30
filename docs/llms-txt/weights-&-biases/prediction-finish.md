# Source: https://docs.wandb.ai/weave/reference/service-api/predictions/prediction-finish.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Prediction Finish

> Finish a prediction.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /v2/{entity}/{project}/predictions/{prediction_id}/finish
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/predictions/{prediction_id}/finish:
    post:
      tags:
        - Predictions
      summary: Prediction Finish
      description: Finish a prediction.
      operationId: >-
        prediction_finish_v2__entity___project__predictions__prediction_id__finish_post
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
        - name: prediction_id
          in: path
          required: true
          schema:
            type: string
            title: Prediction Id
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PredictionFinishRes'
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
    PredictionFinishRes:
      properties:
        success:
          type: boolean
          title: Success
          description: Whether the prediction was finished successfully
      type: object
      required:
        - success
      title: PredictionFinishRes
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