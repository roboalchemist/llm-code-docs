# Source: https://docs.wandb.ai/api-reference/training-jobs/create-sft-training-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create SFT Training Job

> Create a new SFT (Supervised Fine-Tuning) training job.



## OpenAPI

````yaml /training/api-reference/openapi.json post /v1/preview/sft-training-jobs
openapi: 3.1.0
info:
  title: W&B Training
  version: 1.0.0
servers: []
security: []
paths:
  /v1/preview/sft-training-jobs:
    post:
      tags:
        - training-jobs
      summary: Create SFT Training Job
      description: Create a new SFT (Supervised Fine-Tuning) training job.
      operationId: create_sft_training_job_v1_preview_sft_training_jobs_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateSFTTrainingJob'
        required: true
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
    CreateSFTTrainingJob:
      properties:
        model_id:
          type: string
          format: uuid
          title: Model Id
        training_data_url:
          type: string
          title: Training Data Url
          description: >-
            W&B artifact path for training data (e.g.,
            'wandb-artifact:///entity/project/artifact-name:version')
        config:
          anyOf:
            - $ref: '#/components/schemas/SFTTrainingConfig'
            - type: 'null'
        experimental_config:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Experimental Config
      type: object
      required:
        - model_id
        - training_data_url
      title: CreateSFTTrainingJob
      description: >-
        Schema for creating a new SFT (Supervised Fine-Tuning) TrainingJob.


        The client should upload the training data (trajectories.jsonl and
        metadata.json)

        to W&B Artifacts and provide the artifact URL.
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
    SFTTrainingConfig:
      properties:
        batch_size:
          anyOf:
            - type: integer
            - type: string
              const: auto
            - type: 'null'
          title: Batch Size
        learning_rate:
          anyOf:
            - type: number
            - items:
                type: number
              type: array
            - type: 'null'
          title: Learning Rate
      type: object
      title: SFTTrainingConfig
      description: Schema for SFT training config.
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