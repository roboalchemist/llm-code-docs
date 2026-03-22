# Source: https://docs.wandb.ai/api-reference/training-jobs/get-training-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Training Job

> Get a training job by ID.



## OpenAPI

````yaml /training/api-reference/openapi.json get /v1/preview/training-jobs/{training_job_id}
openapi: 3.1.0
info:
  title: W&B Training
  version: 1.0.0
servers: []
security: []
paths:
  /v1/preview/training-jobs/{training_job_id}:
    get:
      tags:
        - training-jobs
      summary: Get Training Job
      description: Get a training job by ID.
      operationId: get_training_job_v1_preview_training_jobs__training_job_id__get
      parameters:
        - name: training_job_id
          in: path
          required: true
          schema:
            type: string
            title: Training Job Id
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TrainingJobResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - HTTPBearer: []
components:
  schemas:
    TrainingJobResponse:
      properties:
        id:
          type: string
          format: uuid
          title: Id
      type: object
      required:
        - id
      title: TrainingJobResponse
      description: Schema for TrainingJob response.
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
    HTTPBearer:
      type: http
      scheme: bearer

````