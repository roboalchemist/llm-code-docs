# Source: https://docs.fireworks.ai/api-reference/create-supervised-fine-tuning-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Supervised Fine-tuning Job



## OpenAPI

````yaml post /v1/accounts/{account_id}/supervisedFineTuningJobs
openapi: 3.1.0
info:
  title: Gateway REST API
  version: 4.21.6
servers:
  - url: https://api.fireworks.ai
security:
  - BearerAuth: []
tags:
  - name: Gateway
paths:
  /v1/accounts/{account_id}/supervisedFineTuningJobs:
    post:
      tags:
        - Gateway
      summary: Create Supervised Fine-tuning Job
      operationId: Gateway_CreateSupervisedFineTuningJob
      parameters:
        - name: supervisedFineTuningJobId
          description: >-
            ID of the supervised fine-tuning job, a random UUID will be
            generated if not specified.
          in: query
          required: false
          schema:
            type: string
        - name: account_id
          in: path
          required: true
          description: The Account Id
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/gatewaySupervisedFineTuningJob'
        required: true
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/gatewaySupervisedFineTuningJob'
components:
  schemas:
    gatewaySupervisedFineTuningJob:
      type: object
      properties:
        name:
          type: string
          readOnly: true
        displayName:
          type: string
        createTime:
          type: string
          format: date-time
          readOnly: true
        completedTime:
          type: string
          format: date-time
          readOnly: true
        dataset:
          type: string
          description: The name of the dataset used for training.
        awsS3Config:
          $ref: '#/components/schemas/gatewayAwsS3Config'
          description: The AWS configuration for S3 dataset access.
        state:
          $ref: '#/components/schemas/gatewayJobState'
          readOnly: true
        status:
          $ref: '#/components/schemas/gatewayStatus'
          readOnly: true
        createdBy:
          type: string
          description: The email address of the user who initiated this fine-tuning job.
          readOnly: true
        outputModel:
          type: string
          description: >-
            The model ID to be assigned to the resulting fine-tuned model. If
            not specified, the job ID will be used.
        baseModel:
          type: string
          description: |-
            The name of the base model to be fine-tuned
            Only one of 'base_model' or 'warm_start_from' should be specified.
        warmStartFrom:
          type: string
          description: |-
            The PEFT addon model in Fireworks format to be fine-tuned from
            Only one of 'base_model' or 'warm_start_from' should be specified.
        jinjaTemplate:
          type: string
          title: >-
            The Jinja template for conversation formatting. If not specified,
            defaults to the base model's conversation template configuration
        earlyStop:
          type: boolean
          description: >-
            Whether to stop training early if the validation loss does not
            improve.
        epochs:
          type: integer
          format: int32
          description: The number of epochs to train for.
        learningRate:
          type: number
          format: float
          description: The learning rate used for training.
        maxContextLength:
          type: integer
          format: int32
          description: The maximum context length to use with the model.
        loraRank:
          type: integer
          format: int32
          description: The rank of the LoRA layers.
        wandbConfig:
          $ref: '#/components/schemas/gatewayWandbConfig'
          description: >-
            The Weights & Biases team/user account for logging training
            progress.
        evaluationDataset:
          type: string
          description: The name of a separate dataset to use for evaluation.
        isTurbo:
          type: boolean
          description: Whether to run the fine-tuning job in turbo mode.
        evalAutoCarveout:
          type: boolean
          description: Whether to auto-carve the dataset for eval.
        region:
          $ref: '#/components/schemas/gatewayRegion'
          description: The region where the fine-tuning job is located.
        updateTime:
          type: string
          format: date-time
          description: The update time for the supervised fine-tuning job.
          readOnly: true
        nodes:
          type: integer
          format: int32
          description: The number of nodes to use for the fine-tuning job.
        batchSize:
          type: integer
          format: int32
          title: The batch size for sequence packing in training
        mtpEnabled:
          type: boolean
          title: Whether to enable MTP (Model-Token-Prediction) mode
        mtpNumDraftTokens:
          type: integer
          format: int32
          title: Number of draft tokens to use in MTP mode
        mtpFreezeBaseModel:
          type: boolean
          title: Whether to freeze the base model parameters during MTP training
        metricsFileSignedUrl:
          type: string
          title: The signed URL for the metrics file
        trainerLogsSignedUrl:
          type: string
          description: |-
            The signed URL for the trainer logs file (stdout/stderr).
            Only populated if the account has trainer log reading enabled.
          readOnly: true
        gradientAccumulationSteps:
          type: integer
          format: int32
          title: Number of gradient accumulation steps
        learningRateWarmupSteps:
          type: integer
          format: int32
          title: Number of steps for learning rate warm up
        batchSizeSamples:
          type: integer
          format: int32
          description: The number of samples per gradient batch.
        estimatedCost:
          $ref: '#/components/schemas/typeMoney'
          description: The estimated cost of the job.
          readOnly: true
        optimizerWeightDecay:
          type: number
          format: float
          description: Weight decay (L2 regularization) for optimizer.
      title: 'Next ID: 49'
      required:
        - dataset
    gatewayAwsS3Config:
      type: object
      properties:
        credentialsSecret:
          type: string
          title: >-
            Reference to a Secret resource containing AWS access key
            credentials.

            Format: accounts/{account_id}/secrets/{secret_id}

            The secret value must be JSON: {"aws_access_key_id": "AKIA...",
            "aws_secret_access_key": "..."}
        iamRoleArn:
          type: string
          title: >-
            IAM role ARN to assume for accessing S3 datasets via GCP OIDC
            federation.

            Format: arn:aws:iam::account-id:role/role-name
      description: |-
        AwsS3Config is the configuration for AWS S3 dataset access which
        will be used by a training job.
    gatewayJobState:
      type: string
      enum:
        - JOB_STATE_UNSPECIFIED
        - JOB_STATE_CREATING
        - JOB_STATE_RUNNING
        - JOB_STATE_COMPLETED
        - JOB_STATE_FAILED
        - JOB_STATE_CANCELLED
        - JOB_STATE_DELETING
        - JOB_STATE_WRITING_RESULTS
        - JOB_STATE_VALIDATING
        - JOB_STATE_DELETING_CLEANING_UP
        - JOB_STATE_PENDING
        - JOB_STATE_EXPIRED
        - JOB_STATE_RE_QUEUEING
        - JOB_STATE_CREATING_INPUT_DATASET
        - JOB_STATE_IDLE
        - JOB_STATE_CANCELLING
        - JOB_STATE_EARLY_STOPPED
        - JOB_STATE_PAUSED
      default: JOB_STATE_UNSPECIFIED
      description: |-
        JobState represents the state an asynchronous job can be in.

         - JOB_STATE_PAUSED: Job is paused, typically due to account suspension or manual intervention.
    gatewayStatus:
      type: object
      properties:
        code:
          $ref: '#/components/schemas/gatewayCode'
          description: The status code.
        message:
          type: string
          description: A developer-facing error message in English.
      title: >-
        Mimics
        [https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto]
    gatewayWandbConfig:
      type: object
      properties:
        enabled:
          type: boolean
          description: Whether to enable wandb logging.
        apiKey:
          type: string
          description: The API key for the wandb service.
        project:
          type: string
          description: The project name for the wandb service.
        entity:
          type: string
          description: The entity name for the wandb service.
        runId:
          type: string
          description: The run ID for the wandb service.
        url:
          type: string
          description: The URL for the wandb service.
          readOnly: true
      description: >-
        WandbConfig is the configuration for the Weights & Biases (wandb)
        logging which

        will be used by a training job.
    gatewayRegion:
      type: string
      enum:
        - REGION_UNSPECIFIED
        - US_IOWA_1
        - US_VIRGINIA_1
        - US_VIRGINIA_2
        - US_ILLINOIS_1
        - AP_TOKYO_1
        - EU_LONDON_1
        - US_ARIZONA_1
        - US_TEXAS_1
        - US_ILLINOIS_2
        - EU_FRANKFURT_1
        - US_TEXAS_2
        - EU_PARIS_1
        - EU_HELSINKI_1
        - US_NEVADA_1
        - EU_ICELAND_1
        - EU_ICELAND_2
        - US_WASHINGTON_1
        - US_WASHINGTON_2
        - EU_ICELAND_DEV_1
        - US_WASHINGTON_3
        - US_ARIZONA_2
        - AP_TOKYO_2
        - US_CALIFORNIA_1
        - US_MISSOURI_1
        - US_UTAH_1
        - US_TEXAS_3
        - US_ARIZONA_3
        - US_GEORGIA_1
        - US_GEORGIA_2
        - US_WASHINGTON_4
        - US_GEORGIA_3
        - NA_BRITISHCOLUMBIA_1
        - US_GEORGIA_4
        - EU_ICELAND_3
        - US_OHIO_1
      default: REGION_UNSPECIFIED
      description: |-
        - US_IOWA_1: GCP us-central1 (Iowa)
         - US_VIRGINIA_1: AWS us-east-1 (N. Virginia)
         - US_VIRGINIA_2: OCI us-ashburn-1 [HIDE_FROM_DOCS]
         - US_ILLINOIS_1: OCI us-chicago-1
         - AP_TOKYO_1: OCI ap-tokyo-1
         - EU_LONDON_1: OCI uk-london-1 [HIDE_FROM_DOCS]
         - US_ARIZONA_1: OCI us-phoenix-1
         - US_TEXAS_1: Lambda us-south-3 (C. Texas)
         - US_ILLINOIS_2: Lambda us-midwest-1 (Illinois)
         - EU_FRANKFURT_1: OCI eu-frankfurt-1
         - US_TEXAS_2: Lambda us-south-2 (N. Texas)
         - EU_PARIS_1: Nebius eu-west1 [HIDE_FROM_DOCS]
         - EU_HELSINKI_1: Nebius eu-north1 [HIDE_FROM_DOCS]
         - US_NEVADA_1: GCP us-west4 [HIDE_FROM_DOCS]
         - EU_ICELAND_1: Crusoe eu-iceland1
         - EU_ICELAND_2: Crusoe eu-iceland1 (network1)
         - US_WASHINGTON_1: Voltage Park us-pyl-1 (Detach audio cluster from control_plane)
         - US_WASHINGTON_2: Voltage Park us-seattle-2
         - EU_ICELAND_DEV_1: Crusoe eu-iceland1 (dev) [HIDE_FROM_DOCS]
         - US_WASHINGTON_3: Vultr Seattle 1
         - US_ARIZONA_2: Azure westus3 (Anysphere BYOC) [HIDE_FROM_DOCS]
         - AP_TOKYO_2: AWS ap-northeast-1
         - US_CALIFORNIA_1: AWS us-west-1 (N. California)
         - US_MISSOURI_1: Nebius us-central1 (Anysphere BYOC) [HIDE_FROM_DOCS]
         - US_UTAH_1: GCP us-west3 (Utah)
         - US_TEXAS_3: Crusoe us-southcentral1 [HIDE_FROM_DOCS]
         - US_ARIZONA_3: Coreweave us-west-04a-1 [HIDE_FROM_DOCS]
         - US_GEORGIA_1: DigitalOcean us-atl1
         - US_GEORGIA_2: Vultr Atlanta 1
         - US_WASHINGTON_4: Coreweave us-west-09b-1
         - US_GEORGIA_3: Alicloud us-southeast-1
         - NA_BRITISHCOLUMBIA_1: Fluidstack ca-west-1
         - US_GEORGIA_4: DigitalOcean us-atl1 MI350X
         - EU_ICELAND_3: Crusoe eu-iceland1 (Anysphere BYOC) [HIDE_FROM_DOCS]
         - US_OHIO_1: Lambda us-midwest-2 (Ohio)
      title: 'Next ID: 35'
    typeMoney:
      type: object
      properties:
        currencyCode:
          type: string
          description: The three-letter currency code defined in ISO 4217.
        units:
          type: string
          format: int64
          description: >-
            The whole units of the amount.

            For example if `currencyCode` is `"USD"`, then 1 unit is one US
            dollar.
        nanos:
          type: integer
          format: int32
          description: >-
            Number of nano (10^-9) units of the amount.

            The value must be between -999,999,999 and +999,999,999 inclusive.

            If `units` is positive, `nanos` must be positive or zero.

            If `units` is zero, `nanos` can be positive, zero, or negative.

            If `units` is negative, `nanos` must be negative or zero.

            For example $-1.75 is represented as `units`=-1 and
            `nanos`=-750,000,000.
      description: Represents an amount of money with its currency type.
    gatewayCode:
      type: string
      enum:
        - OK
        - CANCELLED
        - UNKNOWN
        - INVALID_ARGUMENT
        - DEADLINE_EXCEEDED
        - NOT_FOUND
        - ALREADY_EXISTS
        - PERMISSION_DENIED
        - UNAUTHENTICATED
        - RESOURCE_EXHAUSTED
        - FAILED_PRECONDITION
        - ABORTED
        - OUT_OF_RANGE
        - UNIMPLEMENTED
        - INTERNAL
        - UNAVAILABLE
        - DATA_LOSS
      default: OK
      description: |-
        - OK: Not an error; returned on success.

        HTTP Mapping: 200 OK
         - CANCELLED: The operation was cancelled, typically by the caller.

        HTTP Mapping: 499 Client Closed Request
         - UNKNOWN: Unknown error.  For example, this error may be returned when
        a `Status` value received from another address space belongs to
        an error space that is not known in this address space.  Also
        errors raised by APIs that do not return enough error information
        may be converted to this error.

        HTTP Mapping: 500 Internal Server Error
         - INVALID_ARGUMENT: The client specified an invalid argument.  Note that this differs
        from `FAILED_PRECONDITION`.  `INVALID_ARGUMENT` indicates arguments
        that are problematic regardless of the state of the system
        (e.g., a malformed file name).

        HTTP Mapping: 400 Bad Request
         - DEADLINE_EXCEEDED: The deadline expired before the operation could complete. For operations
        that change the state of the system, this error may be returned
        even if the operation has completed successfully.  For example, a
        successful response from a server could have been delayed long
        enough for the deadline to expire.

        HTTP Mapping: 504 Gateway Timeout
         - NOT_FOUND: Some requested entity (e.g., file or directory) was not found.

        Note to server developers: if a request is denied for an entire class
        of users, such as gradual feature rollout or undocumented allowlist,
        `NOT_FOUND` may be used. If a request is denied for some users within
        a class of users, such as user-based access control, `PERMISSION_DENIED`
        must be used.

        HTTP Mapping: 404 Not Found
         - ALREADY_EXISTS: The entity that a client attempted to create (e.g., file or directory)
        already exists.

        HTTP Mapping: 409 Conflict
         - PERMISSION_DENIED: The caller does not have permission to execute the specified
        operation. `PERMISSION_DENIED` must not be used for rejections
        caused by exhausting some resource (use `RESOURCE_EXHAUSTED`
        instead for those errors). `PERMISSION_DENIED` must not be
        used if the caller can not be identified (use `UNAUTHENTICATED`
        instead for those errors). This error code does not imply the
        request is valid or the requested entity exists or satisfies
        other pre-conditions.

        HTTP Mapping: 403 Forbidden
         - UNAUTHENTICATED: The request does not have valid authentication credentials for the
        operation.

        HTTP Mapping: 401 Unauthorized
         - RESOURCE_EXHAUSTED: Some resource has been exhausted, perhaps a per-user quota, or
        perhaps the entire file system is out of space.

        HTTP Mapping: 429 Too Many Requests
         - FAILED_PRECONDITION: The operation was rejected because the system is not in a state
        required for the operation's execution.  For example, the directory
        to be deleted is non-empty, an rmdir operation is applied to
        a non-directory, etc.

        Service implementors can use the following guidelines to decide
        between `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`:
         (a) Use `UNAVAILABLE` if the client can retry just the failing call.
         (b) Use `ABORTED` if the client should retry at a higher level. For
             example, when a client-specified test-and-set fails, indicating the
             client should restart a read-modify-write sequence.
         (c) Use `FAILED_PRECONDITION` if the client should not retry until
             the system state has been explicitly fixed. For example, if an "rmdir"
             fails because the directory is non-empty, `FAILED_PRECONDITION`
             should be returned since the client should not retry unless
             the files are deleted from the directory.

        HTTP Mapping: 400 Bad Request
         - ABORTED: The operation was aborted, typically due to a concurrency issue such as
        a sequencer check failure or transaction abort.

        See the guidelines above for deciding between `FAILED_PRECONDITION`,
        `ABORTED`, and `UNAVAILABLE`.

        HTTP Mapping: 409 Conflict
         - OUT_OF_RANGE: The operation was attempted past the valid range.  E.g., seeking or
        reading past end-of-file.

        Unlike `INVALID_ARGUMENT`, this error indicates a problem that may
        be fixed if the system state changes. For example, a 32-bit file
        system will generate `INVALID_ARGUMENT` if asked to read at an
        offset that is not in the range [0,2^32-1], but it will generate
        `OUT_OF_RANGE` if asked to read from an offset past the current
        file size.

        There is a fair bit of overlap between `FAILED_PRECONDITION` and
        `OUT_OF_RANGE`.  We recommend using `OUT_OF_RANGE` (the more specific
        error) when it applies so that callers who are iterating through
        a space can easily look for an `OUT_OF_RANGE` error to detect when
        they are done.

        HTTP Mapping: 400 Bad Request
         - UNIMPLEMENTED: The operation is not implemented or is not supported/enabled in this
        service.

        HTTP Mapping: 501 Not Implemented
         - INTERNAL: Internal errors.  This means that some invariants expected by the
        underlying system have been broken.  This error code is reserved
        for serious errors.

        HTTP Mapping: 500 Internal Server Error
         - UNAVAILABLE: The service is currently unavailable.  This is most likely a
        transient condition, which can be corrected by retrying with
        a backoff. Note that it is not always safe to retry
        non-idempotent operations.

        See the guidelines above for deciding between `FAILED_PRECONDITION`,
        `ABORTED`, and `UNAVAILABLE`.

        HTTP Mapping: 503 Service Unavailable
         - DATA_LOSS: Unrecoverable data loss or corruption.

        HTTP Mapping: 500 Internal Server Error
      title: >-
        Mimics
        [https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto]
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````