# Source: https://docs.wandb.ai/weave/reference/service-api/evaluations/evaluation-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluation Status



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /evaluations/status
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /evaluations/status:
    post:
      tags:
        - Evaluations
      summary: Evaluation Status
      operationId: evaluation_status_evaluations_status_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EvaluationStatusReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EvaluationStatusRes'
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
    EvaluationStatusReq:
      properties:
        project_id:
          type: string
          title: Project Id
        call_id:
          type: string
          title: Call Id
      additionalProperties: false
      type: object
      required:
        - project_id
        - call_id
      title: EvaluationStatusReq
    EvaluationStatusRes:
      properties:
        status:
          anyOf:
            - $ref: '#/components/schemas/EvaluationStatusNotFound'
            - $ref: '#/components/schemas/EvaluationStatusRunning'
            - $ref: '#/components/schemas/EvaluationStatusFailed'
            - $ref: '#/components/schemas/EvaluationStatusComplete'
          title: Status
      type: object
      required:
        - status
      title: EvaluationStatusRes
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    EvaluationStatusNotFound:
      properties:
        code:
          type: string
          const: not_found
          title: Code
          default: not_found
      additionalProperties: false
      type: object
      title: EvaluationStatusNotFound
    EvaluationStatusRunning:
      properties:
        code:
          type: string
          const: running
          title: Code
          default: running
        completed_rows:
          type: integer
          title: Completed Rows
        total_rows:
          type: integer
          title: Total Rows
      additionalProperties: false
      type: object
      required:
        - completed_rows
        - total_rows
      title: EvaluationStatusRunning
    EvaluationStatusFailed:
      properties:
        code:
          type: string
          const: failed
          title: Code
          default: failed
        error:
          anyOf:
            - type: string
            - type: 'null'
          title: Error
      additionalProperties: false
      type: object
      title: EvaluationStatusFailed
    EvaluationStatusComplete:
      properties:
        code:
          type: string
          const: complete
          title: Code
          default: complete
        output:
          additionalProperties: true
          type: object
          title: Output
      additionalProperties: false
      type: object
      required:
        - output
      title: EvaluationStatusComplete
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