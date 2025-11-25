# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-dataset.md

# Source: https://docs.fireworks.ai/api-reference/create-dataset.md

# Create Dataset

## OpenAPI

````yaml post /v1/accounts/{account_id}/datasets
paths:
  path: /v1/accounts/{account_id}/datasets
  method: post
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              dataset:
                allOf:
                  - $ref: '#/components/schemas/gatewayDataset'
              datasetId:
                allOf:
                  - type: string
              sourceDatasetId:
                allOf:
                  - type: string
                    title: >-
                      If set, indicates we are creating a new dataset by
                      filtering this existing dataset ID
              filter:
                allOf:
                  - type: string
                    title: >-
                      Filter condition (SQL-like WHERE clause) to apply to the
                      source dataset
            required: true
            refIdentifier: '#/components/schemas/GatewayCreateDatasetBody'
            requiredProperties:
              - dataset
              - datasetId
        examples:
          example:
            value:
              dataset:
                displayName: <string>
                exampleCount: <string>
                userUploaded: {}
                evaluationResult:
                  evaluationJobId: <string>
                transformed:
                  sourceDatasetId: <string>
                  filter: <string>
                  originalFormat: FORMAT_UNSPECIFIED
                splitted:
                  sourceDatasetId: <string>
                evalProtocol: {}
                externalUrl: <string>
                format: FORMAT_UNSPECIFIED
                sourceJobName: <string>
              datasetId: <string>
              sourceDatasetId: <string>
              filter: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - &ref_0
                    type: string
                    readOnly: true
              displayName:
                allOf:
                  - &ref_1
                    type: string
              createTime:
                allOf:
                  - &ref_2
                    type: string
                    format: date-time
                    readOnly: true
              state:
                allOf:
                  - &ref_3
                    $ref: '#/components/schemas/gatewayDatasetState'
                    readOnly: true
              status:
                allOf:
                  - &ref_4
                    $ref: '#/components/schemas/gatewayStatus'
                    readOnly: true
              exampleCount:
                allOf:
                  - &ref_5
                    type: string
                    format: int64
              userUploaded:
                allOf:
                  - &ref_6
                    $ref: '#/components/schemas/gatewayUserUploaded'
              evaluationResult:
                allOf:
                  - &ref_7
                    $ref: '#/components/schemas/gatewayEvaluationResult'
              transformed:
                allOf:
                  - &ref_8
                    $ref: '#/components/schemas/gatewayTransformed'
              splitted:
                allOf:
                  - &ref_9
                    $ref: '#/components/schemas/gatewaySplitted'
              evalProtocol:
                allOf:
                  - &ref_10
                    $ref: '#/components/schemas/gatewayEvalProtocol'
              externalUrl:
                allOf:
                  - &ref_11
                    type: string
                    title: >-
                      The external URI of the dataset. e.g.
                      gs://foo/bar/baz.jsonl
              format:
                allOf:
                  - &ref_12
                    $ref: '#/components/schemas/DatasetFormat'
              createdBy:
                allOf:
                  - &ref_13
                    type: string
                    description: >-
                      The email address of the user who initiated this
                      fine-tuning job.
                    readOnly: true
              updateTime:
                allOf:
                  - &ref_14
                    type: string
                    format: date-time
                    description: The update time for the dataset.
                    readOnly: true
              sourceJobName:
                allOf:
                  - &ref_15
                    type: string
                    description: >-
                      The resource name of the job that created this dataset
                      (e.g., batch inference job).

                      Used for lineage tracking to understand dataset
                      provenance.
              estimatedTokenCount:
                allOf:
                  - &ref_16
                    type: string
                    format: int64
                    description: The estimated number of tokens in the dataset.
                    readOnly: true
            title: 'Next ID: 23'
            refIdentifier: '#/components/schemas/gatewayDataset'
        examples:
          example:
            value:
              name: <string>
              displayName: <string>
              createTime: '2023-11-07T05:31:56Z'
              state: STATE_UNSPECIFIED
              status:
                code: OK
                message: <string>
              exampleCount: <string>
              userUploaded: {}
              evaluationResult:
                evaluationJobId: <string>
              transformed:
                sourceDatasetId: <string>
                filter: <string>
                originalFormat: FORMAT_UNSPECIFIED
              splitted:
                sourceDatasetId: <string>
              evalProtocol: {}
              externalUrl: <string>
              format: FORMAT_UNSPECIFIED
              createdBy: <string>
              updateTime: '2023-11-07T05:31:56Z'
              sourceJobName: <string>
              estimatedTokenCount: <string>
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas:
    DatasetFormat:
      type: string
      enum:
        - FORMAT_UNSPECIFIED
        - CHAT
        - COMPLETION
        - RL
      default: FORMAT_UNSPECIFIED
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
    gatewayDataset:
      type: object
      properties:
        name: *ref_0
        displayName: *ref_1
        createTime: *ref_2
        state: *ref_3
        status: *ref_4
        exampleCount: *ref_5
        userUploaded: *ref_6
        evaluationResult: *ref_7
        transformed: *ref_8
        splitted: *ref_9
        evalProtocol: *ref_10
        externalUrl: *ref_11
        format: *ref_12
        createdBy: *ref_13
        updateTime: *ref_14
        sourceJobName: *ref_15
        estimatedTokenCount: *ref_16
      title: 'Next ID: 23'
    gatewayDatasetState:
      type: string
      enum:
        - STATE_UNSPECIFIED
        - UPLOADING
        - READY
      default: STATE_UNSPECIFIED
    gatewayEvalProtocol:
      type: object
    gatewayEvaluationResult:
      type: object
      properties:
        evaluationJobId:
          type: string
      required:
        - evaluationJobId
    gatewaySplitted:
      type: object
      properties:
        sourceDatasetId:
          type: string
      required:
        - sourceDatasetId
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
    gatewayTransformed:
      type: object
      properties:
        sourceDatasetId:
          type: string
        filter:
          type: string
        originalFormat:
          $ref: '#/components/schemas/DatasetFormat'
      required:
        - sourceDatasetId
    gatewayUserUploaded:
      type: object

````