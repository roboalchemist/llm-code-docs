# Source: https://docs.fireworks.ai/api-reference-dlde/create-environment.md

# Create Environment

## OpenAPI

````yaml post /v1/accounts/{account_id}/environments
paths:
  path: /v1/accounts/{account_id}/environments
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
              environment:
                allOf:
                  - $ref: '#/components/schemas/gatewayEnvironment'
                    description: The properties of the Environment being created.
              environmentId:
                allOf:
                  - type: string
                    title: >-
                      The environment ID to use in the environment name. e.g.
                      my-env
            required: true
            refIdentifier: '#/components/schemas/GatewayCreateEnvironmentBody'
            requiredProperties:
              - environment
              - environmentId
        examples:
          example:
            value:
              environment:
                displayName: <string>
                baseImageRef: <string>
                shared: true
                annotations: {}
              environmentId: <string>
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
                    title: >-
                      The resource name of the environment. e.g.
                      accounts/my-account/clusters/my-cluster/environments/my-env
                    readOnly: true
              displayName:
                allOf:
                  - &ref_1
                    type: string
                    title: >-
                      Human-readable display name of the environment. e.g. "My
                      Environment"
              createTime:
                allOf:
                  - &ref_2
                    type: string
                    format: date-time
                    description: The creation time of the environment.
                    readOnly: true
              createdBy:
                allOf:
                  - &ref_3
                    type: string
                    description: >-
                      The email address of the user who created this
                      environment.
                    readOnly: true
              state:
                allOf:
                  - &ref_4
                    $ref: '#/components/schemas/gatewayEnvironmentState'
                    description: The current state of the environment.
                    readOnly: true
              status:
                allOf:
                  - &ref_5
                    $ref: '#/components/schemas/gatewayStatus'
                    description: The current error status of the environment.
                    readOnly: true
              connection:
                allOf:
                  - &ref_6
                    $ref: '#/components/schemas/gatewayEnvironmentConnection'
                    description: Information about the current environment connection.
                    readOnly: true
              baseImageRef:
                allOf:
                  - &ref_7
                    type: string
                    description: >-
                      The URI of the base container image used for this
                      environment.
              imageRef:
                allOf:
                  - &ref_8
                    type: string
                    description: >-
                      The URI of the container image used for this environment.
                      This is a

                      image is an immutable snapshot of the base_image_ref when
                      the environment

                      was created.
                    readOnly: true
              snapshotImageRef:
                allOf:
                  - &ref_9
                    type: string
                    description: >-
                      The URI of the latest container image snapshot for this
                      environment.
                    readOnly: true
              shared:
                allOf:
                  - &ref_10
                    type: boolean
                    description: >-
                      Whether the environment is shared with all users in the
                      account.

                      This allows all users to connect, disconnect, update,
                      delete, clone, and

                      create batch jobs using the environment.
              annotations:
                allOf:
                  - &ref_11
                    type: object
                    additionalProperties:
                      type: string
                    description: >-
                      Arbitrary, user-specified metadata.

                      Keys and values must adhere to Kubernetes constraints:
                      https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set

                      Additionally, the "fireworks.ai/" prefix is reserved.
              updateTime:
                allOf:
                  - &ref_12
                    type: string
                    format: date-time
                    description: The update time for the environment.
                    readOnly: true
            title: 'Next ID: 14'
            refIdentifier: '#/components/schemas/gatewayEnvironment'
        examples:
          example:
            value:
              name: <string>
              displayName: <string>
              createTime: '2023-11-07T05:31:56Z'
              createdBy: <string>
              state: STATE_UNSPECIFIED
              status:
                code: OK
                message: <string>
              connection:
                nodePoolId: <string>
                numRanks: 123
                role: <string>
                zone: <string>
                useLocalStorage: true
              baseImageRef: <string>
              imageRef: <string>
              snapshotImageRef: <string>
              shared: true
              annotations: {}
              updateTime: '2023-11-07T05:31:56Z'
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas:
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
    gatewayEnvironment:
      type: object
      properties:
        name: *ref_0
        displayName: *ref_1
        createTime: *ref_2
        createdBy: *ref_3
        state: *ref_4
        status: *ref_5
        connection: *ref_6
        baseImageRef: *ref_7
        imageRef: *ref_8
        snapshotImageRef: *ref_9
        shared: *ref_10
        annotations: *ref_11
        updateTime: *ref_12
      title: 'Next ID: 14'
    gatewayEnvironmentConnection:
      type: object
      properties:
        nodePoolId:
          type: string
          description: The resource id of the node pool the environment is connected to.
        numRanks:
          type: integer
          format: int32
          description: |-
            For GPU node pools: one GPU per rank w/ host packing,
            for CPU node pools: one host per rank.
            If not specified, the default is 1.
        role:
          type: string
          description: |-
            The ARN of the AWS IAM role that the connection should assume.
            If not specified, the connection will fall back to the node
            pool's node_role.
        zone:
          type: string
          description: >-
            Current for the last zone that this environment is connected to. We

            want to warn the users about cross zone migration latency when they
            are

            connecting to node pool in a different zone as their persistent
            volume.
          readOnly: true
        useLocalStorage:
          type: boolean
          description: >-
            If true, the node's local storage will be mounted on /tmp. This flag
            has

            no effect if the node does not have local storage.
      title: 'Next ID: 8'
      required:
        - nodePoolId
    gatewayEnvironmentState:
      type: string
      enum:
        - STATE_UNSPECIFIED
        - CREATING
        - DISCONNECTED
        - CONNECTING
        - CONNECTED
        - DISCONNECTING
        - RECONNECTING
        - DELETING
      default: STATE_UNSPECIFIED
      description: |-
        - CREATING: The environment is being created.
         - DISCONNECTED: The environment is not connected.
         - CONNECTING: The environment is being connected to a node.
         - CONNECTED: The environment is connected to a node.
         - DISCONNECTING: The environment is being disconnected from a node.
         - RECONNECTING: The environment is reconnecting with new connection parameters.
         - DELETING: The environment is being deleted.
      title: 'Next ID: 8'
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