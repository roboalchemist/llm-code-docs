# Source: https://docs.fireworks.ai/api-reference/list-evaluation-jobs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List Evaluation Jobs



## OpenAPI

````yaml get /v1/accounts/{account_id}/evaluationJobs
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
  /v1/accounts/{account_id}/evaluationJobs:
    get:
      tags:
        - Gateway
      summary: List Evaluation Jobs
      operationId: Gateway_ListEvaluationJobs
      parameters:
        - name: pageSize
          in: query
          required: false
          schema:
            type: integer
            format: int32
        - name: pageToken
          in: query
          required: false
          schema:
            type: string
        - name: filter
          in: query
          required: false
          schema:
            type: string
        - name: orderBy
          in: query
          required: false
          schema:
            type: string
        - name: readMask
          description: >-
            The fields to be returned in the response. If empty or "*", all
            fields will be returned.
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
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/gatewayListEvaluationJobsResponse'
components:
  schemas:
    gatewayListEvaluationJobsResponse:
      type: object
      properties:
        evaluationJobs:
          type: array
          items:
            $ref: '#/components/schemas/gatewayEvaluationJob'
            type: object
        nextPageToken:
          type: string
        totalSize:
          type: integer
          format: int32
    gatewayEvaluationJob:
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
        createdBy:
          type: string
          readOnly: true
        state:
          $ref: '#/components/schemas/gatewayJobState'
          readOnly: true
        status:
          $ref: '#/components/schemas/gatewayStatus'
          readOnly: true
        evaluator:
          type: string
          description: >-
            The fully-qualified resource name of the Evaluation used by this
            job.


            Format: accounts/{account_id}/evaluators/{evaluator_id}
        inputDataset:
          type: string
          description: >-
            The fully-qualified resource name of the input Dataset used by this
            job.


            Format: accounts/{account_id}/datasets/{dataset_id}
        outputDataset:
          type: string
          description: >-
            The fully-qualified resource name of the output Dataset created by
            this job.


            Format: accounts/{account_id}/datasets/{output_dataset_id}
        metrics:
          type: object
          additionalProperties:
            type: number
            format: double
          readOnly: true
        outputStats:
          type: string
          description: The output dataset's aggregated stats for the evaluation job.
        updateTime:
          type: string
          format: date-time
          description: The update time for the evaluation job.
          readOnly: true
        awsS3Config:
          $ref: '#/components/schemas/gatewayAwsS3Config'
          description: The AWS configuration for S3 dataset access.
      title: 'Next ID: 19'
      required:
        - evaluator
        - inputDataset
        - outputDataset
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