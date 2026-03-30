# Source: https://docs.wandb.ai/weave/reference/service-api/evaluations/evaluate-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluate Model



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /evaluations/evaluate_model
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /evaluations/evaluate_model:
    post:
      tags:
        - Evaluations
      summary: Evaluate Model
      operationId: evaluate_model_evaluations_evaluate_model_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EvaluateModelReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EvaluateModelRes'
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
    EvaluateModelReq:
      properties:
        project_id:
          type: string
          title: Project Id
        evaluation_ref:
          type: string
          title: Evaluation Ref
        model_ref:
          type: string
          title: Model Ref
        wb_user_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Wb User Id
          description: Do not set directly. Server will automatically populate this field.
      additionalProperties: false
      type: object
      required:
        - project_id
        - evaluation_ref
        - model_ref
      title: EvaluateModelReq
    EvaluateModelRes:
      properties:
        call_id:
          type: string
          title: Call Id
      type: object
      required:
        - call_id
      title: EvaluateModelRes
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