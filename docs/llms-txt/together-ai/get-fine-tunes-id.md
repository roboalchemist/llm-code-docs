# Source: https://docs.together.ai/reference/get-fine-tunes-id.md

# List Job

> List the metadata for a single fine-tuning job.



## OpenAPI

````yaml GET /fine-tunes/{id}
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
  /fine-tunes/{id}:
    get:
      tags:
        - Fine-tuning
      summary: List job
      description: List the metadata for a single fine-tuning job.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Fine-tune job details retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FinetuneResponse'
components:
  schemas:
    FinetuneResponse:
      type: object
      required:
        - id
        - status
      properties:
        id:
          type: string
          format: uuid
        training_file:
          type: string
        validation_file:
          type: string
        model:
          type: string
        model_output_name:
          type: string
        model_output_path:
          type: string
        trainingfile_numlines:
          type: integer
        trainingfile_size:
          type: integer
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        n_epochs:
          type: integer
        n_checkpoints:
          type: integer
        n_evals:
          type: integer
        batch_size:
          oneOf:
            - type: integer
            - type: string
              enum:
                - max
          default: max
        learning_rate:
          type: number
        lr_scheduler:
          $ref: '#/components/schemas/LRScheduler'
          type: object
        warmup_ratio:
          type: number
        max_grad_norm:
          type: number
          format: float
        weight_decay:
          type: number
          format: float
        eval_steps:
          type: integer
        train_on_inputs:
          oneOf:
            - type: boolean
            - type: string
              enum:
                - auto
          default: auto
        training_method:
          type: object
          oneOf:
            - $ref: '#/components/schemas/TrainingMethodSFT'
            - $ref: '#/components/schemas/TrainingMethodDPO'
        training_type:
          type: object
          oneOf:
            - $ref: '#/components/schemas/FullTrainingType'
            - $ref: '#/components/schemas/LoRATrainingType'
        multimodal_params:
          $ref: '#/components/schemas/MultimodalParams'
        status:
          $ref: '#/components/schemas/FinetuneJobStatus'
        job_id:
          type: string
        events:
          type: array
          items:
            $ref: '#/components/schemas/FineTuneEvent'
        token_count:
          type: integer
        param_count:
          type: integer
        total_price:
          type: integer
        epochs_completed:
          type: integer
        queue_depth:
          type: integer
        wandb_project_name:
          type: string
        wandb_url:
          type: string
        from_checkpoint:
          type: string
        from_hf_model:
          type: string
        hf_model_revision:
          type: string
        progress:
          $ref: '#/components/schemas/FineTuneProgress'
    LRScheduler:
      type: object
      properties:
        lr_scheduler_type:
          type: string
          enum:
            - linear
            - cosine
        lr_scheduler_args:
          oneOf:
            - $ref: '#/components/schemas/LinearLRSchedulerArgs'
            - $ref: '#/components/schemas/CosineLRSchedulerArgs'
      required:
        - lr_scheduler_type
    TrainingMethodSFT:
      type: object
      properties:
        method:
          type: string
          enum:
            - sft
        train_on_inputs:
          oneOf:
            - type: boolean
            - type: string
              enum:
                - auto
          type: boolean
          default: auto
          description: >-
            Whether to mask the user messages in conversational data or prompts
            in instruction data.
      required:
        - method
        - train_on_inputs
    TrainingMethodDPO:
      type: object
      properties:
        method:
          type: string
          enum:
            - dpo
        dpo_beta:
          type: number
          format: float
          default: 0.1
        rpo_alpha:
          type: number
          format: float
          default: 0
        dpo_normalize_logratios_by_length:
          type: boolean
          default: false
        dpo_reference_free:
          type: boolean
          default: false
        simpo_gamma:
          type: number
          format: float
          default: 0
      required:
        - method
    FullTrainingType:
      type: object
      properties:
        type:
          type: string
          enum:
            - Full
      required:
        - type
    LoRATrainingType:
      type: object
      properties:
        type:
          type: string
          enum:
            - Lora
        lora_r:
          type: integer
        lora_alpha:
          type: integer
        lora_dropout:
          type: number
          format: float
          default: 0
        lora_trainable_modules:
          type: string
          default: all-linear
      required:
        - type
        - lora_r
        - lora_alpha
    MultimodalParams:
      type: object
      properties:
        train_vision:
          type: boolean
          description: >-
            Whether to train the vision encoder of the model. Only available for
            multimodal models.
    FinetuneJobStatus:
      type: string
      enum:
        - pending
        - queued
        - running
        - compressing
        - uploading
        - cancel_requested
        - cancelled
        - error
        - completed
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
    FineTuneProgress:
      type: object
      description: Progress information for a fine-tuning job
      required:
        - estimate_available
        - seconds_remaining
      properties:
        estimate_available:
          type: boolean
          description: Whether time estimate is available
        seconds_remaining:
          type: integer
          description: >-
            Estimated time remaining in seconds for the fine-tuning job to next
            state
    LinearLRSchedulerArgs:
      type: object
      properties:
        min_lr_ratio:
          type: number
          format: float
          default: 0
          description: The ratio of the final learning rate to the peak learning rate
    CosineLRSchedulerArgs:
      type: object
      properties:
        min_lr_ratio:
          type: number
          format: float
          default: 0
          description: The ratio of the final learning rate to the peak learning rate
        num_cycles:
          type: number
          format: float
          default: 0.5
          description: Number or fraction of cycles for the cosine learning rate scheduler
      required:
        - min_lr_ratio
        - num_cycles
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