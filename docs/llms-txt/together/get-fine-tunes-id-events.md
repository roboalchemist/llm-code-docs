# Source: https://docs.together.ai/reference/get-fine-tunes-id-events.md

# List Job Events

> List the events for a single fine-tuning job.



## OpenAPI

````yaml GET /fine-tunes/{id}/events
openapi: 3.1.0
info:
  title: Together APIs
  description: The Together REST API. Please see https://docs.together.ai for more details.
  version: 2.0.0
  termsOfService: https://www.together.ai/terms-of-service
  contact:
    name: Together Support
    url: https://www.together.ai/contact
  license:
    name: MIT
    url: https://github.com/togethercomputer/openapi/blob/main/LICENSE
servers:
  - url: https://api.together.xyz/v1
security:
  - bearerAuth: []
paths:
  /fine-tunes/{id}/events:
    get:
      tags:
        - Fine-tuning
      summary: List job events
      description: List the events for a single fine-tuning job.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: List of fine-tune events
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FinetuneListEvents'
components:
  schemas:
    FinetuneListEvents:
      type: object
      required:
        - data
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/FineTuneEvent'
    FineTuneEvent:
      type: object
      required:
        - object
        - created_at
        - message
        - type
        - param_count
        - token_count
        - total_steps
        - wandb_url
        - step
        - checkpoint_path
        - model_path
        - training_offset
        - hash
      properties:
        object:
          type: string
          enum:
            - fine-tune-event
        created_at:
          type: string
        level:
          anyOf:
            - $ref: '#/components/schemas/FinetuneEventLevels'
        message:
          type: string
        type:
          $ref: '#/components/schemas/FinetuneEventType'
        param_count:
          type: integer
        token_count:
          type: integer
        total_steps:
          type: integer
        wandb_url:
          type: string
        step:
          type: integer
        checkpoint_path:
          type: string
        model_path:
          type: string
        training_offset:
          type: integer
        hash:
          type: string
    FinetuneEventLevels:
      type: string
      enum:
        - null
        - info
        - warning
        - error
        - legacy_info
        - legacy_iwarning
        - legacy_ierror
    FinetuneEventType:
      type: string
      enum:
        - job_pending
        - job_start
        - job_stopped
        - model_downloading
        - model_download_complete
        - training_data_downloading
        - training_data_download_complete
        - validation_data_downloading
        - validation_data_download_complete
        - wandb_init
        - training_start
        - checkpoint_save
        - billing_limit
        - epoch_complete
        - training_complete
        - model_compressing
        - model_compression_complete
        - model_uploading
        - model_upload_complete
        - job_complete
        - job_error
        - cancel_requested
        - job_restarted
        - refund
        - warning
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt