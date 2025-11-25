# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-dpo-jobs.md

# Source: https://docs.fireworks.ai/api-reference/list-dpo-jobs.md

# null

## OpenAPI

````yaml get /v1/accounts/{account_id}/dpoJobs
paths:
  path: /v1/accounts/{account_id}/dpoJobs
  method: get
  servers:
    - url: https://api.fireworks.ai
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication using your Fireworks API key. Format:
                Bearer <API_KEY>
          cookie: {}
    parameters:
      path:
        account_id:
          schema:
            - type: string
              required: true
              description: The Account Id
      query:
        pageSize:
          schema:
            - type: integer
              required: false
              description: >-
                The maximum number of dpo jobs to return. The maximum page_size
                is 200,

                values above 200 will be coerced to 200.

                If unspecified, the default is 50.
        pageToken:
          schema:
            - type: string
              required: false
              description: >-
                A page token, received from a previous ListDpoJobs call. Provide
                this

                to retrieve the subsequent page. When paginating, all other
                parameters

                provided to ListDpoJobs must match the call that provided the
                page

                token.
        filter:
          schema:
            - type: string
              required: false
              description: >-
                Filter criteria for the returned jobs. See
                https://google.aip.dev/160 for the filter syntax specification.
        orderBy:
          schema:
            - type: string
              required: false
              description: >-
                A comma-separated list of fields to order by. e.g. "foo,bar"

                The default sort order is ascending. To specify a descending
                order for a

                field, append a " desc" suffix. e.g. "foo desc,bar"

                Subfields are specified with a "." character. e.g. "foo.bar"

                If not specified, the default order is by "name".
        readMask:
          schema:
            - type: string
              required: false
              description: >-
                The fields to be returned in the response. If empty or "*", all
                fields will be returned.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              dpoJobs:
                allOf:
                  - type: array
                    items:
                      type: object
                      $ref: '#/components/schemas/gatewayDpoJob'
              nextPageToken:
                allOf:
                  - type: string
                    description: >-
                      A token, which can be sent as `page_token` to retrieve the
                      next page.

                      If this field is omitted, there are no subsequent pages.
              totalSize:
                allOf:
                  - type: integer
                    format: int32
                    title: The total number of dpo jobs
            refIdentifier: '#/components/schemas/gatewayListDpoJobsResponse'
        examples:
          example:
            value:
              dpoJobs:
                - name: <string>
                  displayName: <string>
                  createTime: '2023-11-07T05:31:56Z'
                  completedTime: '2023-11-07T05:31:56Z'
                  dataset: <string>
                  state: JOB_STATE_UNSPECIFIED
                  status:
                    code: OK
                    message: <string>
                  createdBy: <string>
                  trainingConfig:
                    outputModel: <string>
                    baseModel: <string>
                    warmStartFrom: <string>
                    jinjaTemplate: <string>
                    learningRate: 123
                    maxContextLength: 123
                    loraRank: 123
                    region: REGION_UNSPECIFIED
                    epochs: 123
                    batchSize: 123
                    gradientAccumulationSteps: 123
                    learningRateWarmupSteps: 123
                  wandbConfig:
                    enabled: true
                    apiKey: <string>
                    project: <string>
                    entity: <string>
                    runId: <string>
                    url: <string>
              nextPageToken: <string>
              totalSize: 123
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas:
    gatewayBaseTrainingConfig:
      type: object
      properties:
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
        region:
          $ref: '#/components/schemas/gatewayRegion'
          description: The region where the fine-tuning job is located.
        epochs:
          type: integer
          format: int32
          description: The number of epochs to train for.
        batchSize:
          type: integer
          format: int32
          description: >-
            The maximum packed number of tokens per batch for training in
            sequence packing.
        gradientAccumulationSteps:
          type: integer
          format: int32
          title: Number of gradient accumulation steps
        learningRateWarmupSteps:
          type: integer
          format: int32
          title: Number of steps for learning rate warm up
      title: |-
        BaseTrainingConfig contains common configuration fields shared across
        different training job types.
        Next ID: 19
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
    gatewayDpoJob:
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
        state:
          $ref: '#/components/schemas/gatewayJobState'
          readOnly: true
        status:
          $ref: '#/components/schemas/gatewayStatus'
          readOnly: true
        createdBy:
          type: string
          description: The email address of the user who initiated this dpo job.
          readOnly: true
        trainingConfig:
          $ref: '#/components/schemas/gatewayBaseTrainingConfig'
          description: Common training configurations.
        wandbConfig:
          $ref: '#/components/schemas/gatewayWandbConfig'
          description: The Weights & Biases team/user account for logging job progress.
      title: 'Next ID: 13'
      required:
        - dataset
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
      default: JOB_STATE_UNSPECIFIED
      description: JobState represents the state an asynchronous job can be in.
    gatewayRegion:
      type: string
      enum:
        - REGION_UNSPECIFIED
        - US_IOWA_1
        - US_VIRGINIA_1
        - US_ILLINOIS_1
        - AP_TOKYO_1
        - US_ARIZONA_1
        - US_TEXAS_1
        - US_ILLINOIS_2
        - EU_FRANKFURT_1
        - US_TEXAS_2
        - EU_ICELAND_1
        - EU_ICELAND_2
        - US_WASHINGTON_1
        - US_WASHINGTON_2
        - US_WASHINGTON_3
        - AP_TOKYO_2
        - US_CALIFORNIA_1
        - US_UTAH_1
        - US_TEXAS_3
        - US_GEORGIA_1
        - US_GEORGIA_2
        - US_WASHINGTON_4
        - US_GEORGIA_3
      default: REGION_UNSPECIFIED
      title: |-
        - US_IOWA_1: GCP us-central1 (Iowa)
         - US_VIRGINIA_1: AWS us-east-1 (N. Virginia)
         - US_ILLINOIS_1: OCI us-chicago-1
         - AP_TOKYO_1: OCI ap-tokyo-1
         - US_ARIZONA_1: OCI us-phoenix-1
         - US_TEXAS_1: Lambda us-south-3 (C. Texas)
         - US_ILLINOIS_2: Lambda us-midwest-1 (Illinois)
         - EU_FRANKFURT_1: OCI eu-frankfurt-1
         - US_TEXAS_2: Lambda us-south-2 (N. Texas)
         - EU_ICELAND_1: Crusoe eu-iceland1
         - EU_ICELAND_2: Crusoe eu-iceland1 (network1)
         - US_WASHINGTON_1: Voltage Park us-pyl-1 (Detach audio cluster from control_plane)
         - US_WASHINGTON_2: Voltage Park us-seattle-2
         - US_WASHINGTON_3: Vultr Seattle 1
         - AP_TOKYO_2: AWS ap-northeast-1
         - US_CALIFORNIA_1: AWS us-west-1 (N. California)
         - US_UTAH_1: GCP us-west3 (Utah)
         - US_TEXAS_3: Crusoe us-southcentral1
         - US_GEORGIA_1: DigitalOcean us-atl1
         - US_GEORGIA_2: Vultr Atlanta 1
         - US_WASHINGTON_4: Coreweave us-west-09b-1
         - US_GEORGIA_3: Alicloud us-southeast-1
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

````