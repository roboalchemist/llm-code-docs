# Source: https://docs.fireworks.ai/api-reference/list-datasets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List Datasets



## OpenAPI

````yaml get /v1/accounts/{account_id}/datasets
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
  /v1/accounts/{account_id}/datasets:
    get:
      tags:
        - Gateway
      summary: List Datasets
      operationId: Gateway_ListDatasets
      parameters:
        - name: pageSize
          description: >-
            The maximum number of datasets to return. The maximum page_size is
            200,

            values above 200 will be coerced to 200.

            If unspecified, the default is 50.
          in: query
          required: false
          schema:
            type: integer
            format: int32
        - name: pageToken
          description: >-
            A page token, received from a previous ListDatasets call. Provide
            this

            to retrieve the subsequent page. When paginating, all other
            parameters

            provided to ListDatasets must match the call that provided the page

            token.
          in: query
          required: false
          schema:
            type: string
        - name: filter
          description: |-
            Only model satisfying the provided filter (if specified) will be
            returned. See https://google.aip.dev/160 for the filter grammar.
          in: query
          required: false
          schema:
            type: string
        - name: orderBy
          description: >-
            A comma-separated list of fields to order by. e.g. "foo,bar"

            The default sort order is ascending. To specify a descending order
            for a

            field, append a " desc" suffix. e.g. "foo desc,bar"

            Subfields are specified with a "." character. e.g. "foo.bar"

            If not specified, the default order is by "name".
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
                $ref: '#/components/schemas/gatewayListDatasetsResponse'
components:
  schemas:
    gatewayListDatasetsResponse:
      type: object
      properties:
        datasets:
          type: array
          items:
            $ref: '#/components/schemas/gatewayDataset'
            type: object
        nextPageToken:
          type: string
          description: >-
            A token, which can be sent as `page_token` to retrieve the next
            page.

            If this field is omitted, there are no subsequent pages.
        totalSize:
          type: integer
          format: int32
          title: The total number of datasets
    gatewayDataset:
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
        state:
          $ref: '#/components/schemas/gatewayDatasetState'
          readOnly: true
        status:
          $ref: '#/components/schemas/gatewayStatus'
          readOnly: true
        exampleCount:
          type: string
          format: int64
        userUploaded:
          $ref: '#/components/schemas/gatewayUserUploaded'
        evaluationResult:
          $ref: '#/components/schemas/gatewayEvaluationResult'
        transformed:
          $ref: '#/components/schemas/gatewayTransformed'
        splitted:
          $ref: '#/components/schemas/gatewaySplitted'
        evalProtocol:
          $ref: '#/components/schemas/gatewayEvalProtocol'
        externalUrl:
          type: string
          title: The external URI of the dataset. e.g. gs://foo/bar/baz.jsonl
        format:
          $ref: '#/components/schemas/DatasetFormat'
        createdBy:
          type: string
          description: The email address of the user who initiated this fine-tuning job.
          readOnly: true
        updateTime:
          type: string
          format: date-time
          description: The update time for the dataset.
          readOnly: true
        sourceJobName:
          type: string
          description: >-
            The resource name of the job that created this dataset (e.g., batch
            inference job).

            Used for lineage tracking to understand dataset provenance.
        estimatedTokenCount:
          type: string
          format: int64
          description: The estimated number of tokens in the dataset.
          readOnly: true
        averageTurnCount:
          type: number
          format: float
          description: >-
            An estimate of the average number of turns per sample in the
            dataset.
          readOnly: true
      title: 'Next ID: 24'
      required:
        - exampleCount
    gatewayDatasetState:
      type: string
      enum:
        - STATE_UNSPECIFIED
        - UPLOADING
        - READY
      default: STATE_UNSPECIFIED
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
    gatewayUserUploaded:
      type: object
    gatewayEvaluationResult:
      type: object
      properties:
        evaluationJobId:
          type: string
      required:
        - evaluationJobId
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
    gatewaySplitted:
      type: object
      properties:
        sourceDatasetId:
          type: string
      required:
        - sourceDatasetId
    gatewayEvalProtocol:
      type: object
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````