# Source: https://docs.together.ai/reference/post-fine-tunes.md

# Create Job

> Create a fine-tuning job with the provided model and training data.



## OpenAPI

````yaml POST /fine-tunes
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
  /fine-tunes:
    post:
      tags:
        - Fine-tuning
      summary: Create job
      description: Create a fine-tuning job with the provided model and training data.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - training_file
                - model
              properties:
                training_file:
                  type: string
                  description: File-ID of a training file uploaded to the Together API
                validation_file:
                  type: string
                  description: File-ID of a validation file uploaded to the Together API
                model:
                  type: string
                  description: Name of the base model to run fine-tune job on
                n_epochs:
                  type: integer
                  default: 1
                  description: >-
                    Number of complete passes through the training dataset
                    (higher values may improve results but increase cost and
                    risk of overfitting)
                n_checkpoints:
                  type: integer
                  default: 1
                  description: >-
                    Number of intermediate model versions saved during training
                    for evaluation
                n_evals:
                  type: integer
                  default: 0
                  description: >-
                    Number of evaluations to be run on a given validation set
                    during training
                batch_size:
                  oneOf:
                    - type: integer
                    - type: string
                      enum:
                        - max
                  default: max
                  description: >-
                    Number of training examples processed together (larger
                    batches use more memory but may train faster). Defaults to
                    "max". We use training optimizations like packing, so the
                    effective batch size may be different than the value you
                    set.
                learning_rate:
                  type: number
                  format: float
                  default: 0.00001
                  description: >-
                    Controls how quickly the model adapts to new information
                    (too high may cause instability, too low may slow
                    convergence)
                lr_scheduler:
                  $ref: '#/components/schemas/LRScheduler'
                  type: object
                  default: none
                  description: >-
                    The learning rate scheduler to use. It specifies how the
                    learning rate is adjusted during training.
                warmup_ratio:
                  type: number
                  format: float
                  default: 0
                  description: >-
                    The percent of steps at the start of training to linearly
                    increase the learning rate.
                max_grad_norm:
                  type: number
                  format: float
                  default: 1
                  description: >-
                    Max gradient norm to be used for gradient clipping. Set to 0
                    to disable.
                weight_decay:
                  type: number
                  format: float
                  default: 0
                  description: Weight decay. Regularization parameter for the optimizer.
                suffix:
                  type: string
                  description: Suffix that will be added to your fine-tuned model name
                wandb_api_key:
                  type: string
                  description: >-
                    Integration key for tracking experiments and model metrics
                    on W&B platform
                wandb_base_url:
                  type: string
                  description: The base URL of a dedicated Weights & Biases instance.
                wandb_project_name:
                  type: string
                  description: >-
                    The Weights & Biases project for your run. If not specified,
                    will use `together` as the project name.
                wandb_name:
                  type: string
                  description: The Weights & Biases name for your run.
                train_on_inputs:
                  oneOf:
                    - type: boolean
                    - type: string
                      enum:
                        - auto
                  type: boolean
                  default: auto
                  description: >-
                    Whether to mask the user messages in conversational data or
                    prompts in instruction data.
                  deprecated: true
                training_method:
                  type: object
                  oneOf:
                    - $ref: '#/components/schemas/TrainingMethodSFT'
                    - $ref: '#/components/schemas/TrainingMethodDPO'
                  description: >-
                    The training method to use. 'sft' for Supervised Fine-Tuning
                    or 'dpo' for Direct Preference Optimization.
                training_type:
                  type: object
                  oneOf:
                    - $ref: '#/components/schemas/FullTrainingType'
                    - $ref: '#/components/schemas/LoRATrainingType'
                multimodal_params:
                  $ref: '#/components/schemas/MultimodalParams'
                from_checkpoint:
                  type: string
                  description: >-
                    The checkpoint identifier to continue training from a
                    previous fine-tuning job. Format is `{$JOB_ID}` or
                    `{$OUTPUT_MODEL_NAME}` or `{$JOB_ID}:{$STEP}` or
                    `{$OUTPUT_MODEL_NAME}:{$STEP}`. The step value is optional;
                    without it, the final checkpoint will be used.
                from_hf_model:
                  type: string
                  description: >-
                    The Hugging Face Hub repo to start training from. Should be
                    as close as possible to the base model (specified by the
                    `model` argument) in terms of architecture and size.
                hf_model_revision:
                  type: string
                  description: >-
                    The revision of the Hugging Face Hub model to continue
                    training from. E.g., hf_model_revision=main (default, used
                    if the argument is not provided) or
                    hf_model_revision='607a30d783dfa663caf39e06633721c8d4cfcd7e'
                    (specific commit).
                hf_api_token:
                  type: string
                  description: The API token for the Hugging Face Hub.
                hf_output_repo_name:
                  type: string
                  description: >-
                    The name of the Hugging Face repository to upload the
                    fine-tuned model to.
      responses:
        '200':
          description: Fine-tuning job initiated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FinetuneResponseTruncated'
components:
  schemas:
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
    FinetuneResponseTruncated:
      type: object
      description: >-
        A truncated version of the fine-tune response, used for POST
        /fine-tunes, GET /fine-tunes and POST /fine-tunes/{id}/cancel endpoints
      required:
        - id
        - status
        - created_at
        - updated_at
      example:
        id: ft-01234567890123456789
        status: completed
        created_at: '2023-05-17T17:35:45.123Z'
        updated_at: '2023-05-17T18:46:23.456Z'
        user_id: user_01234567890123456789
        owner_address: user@example.com
        total_price: 1500
        token_count: 850000
        events: []
        model: meta-llama/Llama-2-7b-hf
        model_output_name: mynamespace/meta-llama/Llama-2-7b-hf-32162631
        n_epochs: 3
        training_file: file-01234567890123456789
        wandb_project_name: my-finetune-project
      properties:
        id:
          type: string
          description: Unique identifier for the fine-tune job
        status:
          $ref: '#/components/schemas/FinetuneJobStatus'
        created_at:
          type: string
          format: date-time
          description: Creation timestamp of the fine-tune job
        updated_at:
          type: string
          format: date-time
          description: Last update timestamp of the fine-tune job
        user_id:
          type: string
          description: Identifier for the user who created the job
        owner_address:
          type: string
          description: Owner address information
        total_price:
          type: integer
          description: Total price for the fine-tuning job
        token_count:
          type: integer
          description: Count of tokens processed
        events:
          type: array
          items:
            $ref: '#/components/schemas/FineTuneEvent'
          description: Events related to this fine-tune job
        training_file:
          type: string
          description: File-ID of the training file
        validation_file:
          type: string
          description: File-ID of the validation file
        model:
          type: string
          description: Base model used for fine-tuning
        model_output_name:
          type: string
        suffix:
          type: string
          description: Suffix added to the fine-tuned model name
        n_epochs:
          type: integer
          description: Number of training epochs
        n_evals:
          type: integer
          description: Number of evaluations during training
        n_checkpoints:
          type: integer
          description: Number of checkpoints saved during training
        batch_size:
          type: integer
          description: Batch size used for training
        training_type:
          oneOf:
            - $ref: '#/components/schemas/FullTrainingType'
            - $ref: '#/components/schemas/LoRATrainingType'
          description: Type of training used (full or LoRA)
        training_method:
          oneOf:
            - $ref: '#/components/schemas/TrainingMethodSFT'
            - $ref: '#/components/schemas/TrainingMethodDPO'
          description: Method of training used
        learning_rate:
          type: number
          format: float
          description: Learning rate used for training
        lr_scheduler:
          $ref: '#/components/schemas/LRScheduler'
          description: Learning rate scheduler configuration
        warmup_ratio:
          type: number
          format: float
          description: Ratio of warmup steps
        max_grad_norm:
          type: number
          format: float
          description: Maximum gradient norm for clipping
        weight_decay:
          type: number
          format: float
          description: Weight decay value used
        wandb_project_name:
          type: string
          description: Weights & Biases project name
        wandb_name:
          type: string
          description: Weights & Biases run name
        from_checkpoint:
          type: string
          description: Checkpoint used to continue training
        from_hf_model:
          type: string
          description: Hugging Face Hub repo to start training from
        hf_model_revision:
          type: string
          description: The revision of the Hugging Face Hub model to continue training from
        progress:
          $ref: '#/components/schemas/FineTuneProgress'
          description: Progress information for the fine-tuning job
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