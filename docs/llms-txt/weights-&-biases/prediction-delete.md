# Source: https://docs.wandb.ai/weave/reference/service-api/predictions/prediction-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Prediction Delete

> Delete predictions.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json delete /v2/{entity}/{project}/predictions
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/predictions:
    delete:
      tags:
        - Predictions
      summary: Prediction Delete
      description: Delete predictions.
      operationId: prediction_delete_v2__entity___project__predictions_delete
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
        - name: prediction_ids
          in: query
          required: true
          schema:
            type: array
            items:
              type: string
            description: List of prediction IDs to delete
            title: Prediction Ids
          description: List of prediction IDs to delete
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PredictionDeleteRes'
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
    PredictionDeleteRes:
      properties:
        num_deleted:
          type: integer
          title: Num Deleted
          description: Number of predictions deleted
      type: object
      required:
        - num_deleted
      title: PredictionDeleteRes
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