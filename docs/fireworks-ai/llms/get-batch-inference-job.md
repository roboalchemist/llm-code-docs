# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-batch-inference-job.md

# Source: https://docs.fireworks.ai/api-reference/get-batch-inference-job.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-batch-inference-job.md

# Source: https://docs.fireworks.ai/api-reference/get-batch-inference-job.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-batch-inference-job.md

# Source: https://docs.fireworks.ai/api-reference/get-batch-inference-job.md

# Get Batch Inference Job

## OpenAPI

````yaml get /v1/accounts/{account_id}/batchInferenceJobs/{batch_inference_job_id}
paths:
  path: /v1/accounts/{account_id}/batchInferenceJobs/{batch_inference_job_id}
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
        batch_inference_job_id:
          schema:
            - type: string
              required: true
              description: The Batch Inference Job Id
      query:
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
              name:
                allOf:
                  - type: string
                    title: >-
                      The resource name of the batch inference job. e.g.
                      accounts/my-account/batchInferenceJobs/my-batch-inference-job
                    readOnly: true
              displayName:
                allOf:
                  - type: string
                    title: >-
                      Human-readable display name of the batch inference job.
                      e.g. "My Batch Inference Job"
              createTime:
                allOf:
                  - type: string
                    format: date-time
                    description: The creation time of the batch inference job.
                    readOnly: true
              createdBy:
                allOf:
                  - type: string
                    description: >-
                      The email address of the user who initiated this batch
                      inference job.
                    readOnly: true
              state:
                allOf:
                  - $ref: '#/components/schemas/gatewayJobState'
                    description: >-
                      JobState represents the state an asynchronous job can be
                      in.
                    readOnly: true
              status:
                allOf:
                  - $ref: '#/components/schemas/gatewayStatus'
                    readOnly: true
              model:
                allOf:
                  - type: string
                    description: >-
                      The name of the model to use for inference. This is
                      required, except when continued_from_job_name is
                      specified.
              inputDatasetId:
                allOf:
                  - type: string
                    description: >-
                      The name of the dataset used for inference. This is
                      required, except when continued_from_job_name is
                      specified.
              outputDatasetId:
                allOf:
                  - type: string
                    description: >-
                      The name of the dataset used for storing the results. This
                      will also contain the error file.
              inferenceParameters:
                allOf:
                  - $ref: '#/components/schemas/gatewayInferenceParameters'
                    description: Parameters controlling the inference process.
              updateTime:
                allOf:
                  - type: string
                    format: date-time
                    description: The update time for the batch inference job.
                    readOnly: true
              precision:
                allOf:
                  - $ref: '#/components/schemas/DeploymentPrecision'
                    description: >-
                      The precision with which the model should be served.

                      If PRECISION_UNSPECIFIED, a default will be chosen based
                      on the model.
              jobProgress:
                allOf:
                  - $ref: '#/components/schemas/gatewayJobProgress'
                    description: Job progress.
                    readOnly: true
              continuedFromJobName:
                allOf:
                  - type: string
                    description: >-
                      The resource name of the batch inference job that this job
                      continues from.

                      Used for lineage tracking to understand job continuation
                      chains.
            title: 'Next ID: 31'
            refIdentifier: '#/components/schemas/gatewayBatchInferenceJob'
        examples:
          example:
            value:
              name: <string>
              displayName: <string>
              createTime: '2023-11-07T05:31:56Z'
              createdBy: <string>
              state: JOB_STATE_UNSPECIFIED
              status:
                code: OK
                message: <string>
              model: <string>
              inputDatasetId: <string>
              outputDatasetId: <string>
              inferenceParameters:
                maxTokens: 123
                temperature: 123
                topP: 123
                'n': 123
                extraBody: <string>
                topK: 123
              updateTime: '2023-11-07T05:31:56Z'
              precision: PRECISION_UNSPECIFIED
              jobProgress:
                percent: 123
                epoch: 123
                totalInputRequests: 123
                totalProcessedRequests: 123
                successfullyProcessedRequests: 123
                failedRequests: 123
                outputRows: 123
                inputTokens: 123
                outputTokens: 123
                cachedInputTokenCount: 123
              continuedFromJobName: <string>
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas:
    DeploymentPrecision:
      type: string
      enum:
        - PRECISION_UNSPECIFIED
        - FP16
        - FP8
        - FP8_MM
        - FP8_AR
        - FP8_MM_KV_ATTN
        - FP8_KV
        - FP8_MM_V2
        - FP8_V2
        - FP8_MM_KV_ATTN_V2
        - NF4
        - FP4
        - BF16
        - FP4_BLOCKSCALED_MM
        - FP4_MX_MOE
      default: PRECISION_UNSPECIFIED
      title: >-
        - PRECISION_UNSPECIFIED: if left unspecified we will treat this as a
        legacy model created before

        self serve
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
    gatewayInferenceParameters:
      type: object
      properties:
        maxTokens:
          type: integer
          format: int32
          description: Maximum number of tokens to generate per response.
        temperature:
          type: number
          format: float
          description: Sampling temperature, typically between 0 and 2.
        topP:
          type: number
          format: float
          description: Top-p sampling parameter, typically between 0 and 1.
        'n':
          type: integer
          format: int32
          description: Number of response candidates to generate per input.
        extraBody:
          type: string
          description: |-
            Additional parameters for the inference request as a JSON string.
            For example: "{\"stop\": [\"\\n\"]}".
        topK:
          type: integer
          format: int32
          description: >-
            Top-k sampling parameter, limits the token selection to the top k
            tokens.
      description: Parameters for the inference requests.
    gatewayJobProgress:
      type: object
      properties:
        percent:
          type: integer
          format: int32
          description: Progress percent, within the range from 0 to 100.
        epoch:
          type: integer
          format: int32
          description: >-
            The epoch for which the progress percent is reported, usually
            starting from 0.

            This is optional for jobs that don't run in an epoch fasion, e.g.
            BIJ, EVJ.
        totalInputRequests:
          type: integer
          format: int32
          description: Total number of input requests/rows in the job.
        totalProcessedRequests:
          type: integer
          format: int32
          description: >-
            Total number of requests that have been processed (successfully or
            failed).
        successfullyProcessedRequests:
          type: integer
          format: int32
          description: Number of requests that were processed successfully.
        failedRequests:
          type: integer
          format: int32
          description: Number of requests that failed to process.
        outputRows:
          type: integer
          format: int32
          description: Number of output rows generated.
        inputTokens:
          type: integer
          format: int32
          description: Total number of input tokens processed.
        outputTokens:
          type: integer
          format: int32
          description: Total number of output tokens generated.
        cachedInputTokenCount:
          type: integer
          format: int32
          description: The number of input tokens that hit the prompt cache.
      description: Progress of a job, e.g. RLOR, EVJ, BIJ etc.
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

````