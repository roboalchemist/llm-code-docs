# Source: https://docs.fireworks.ai/api-reference-dlde/list-node-pools.md

# List Node Pools

## OpenAPI

````yaml get /v1/accounts/{account_id}/nodePools
paths:
  path: /v1/accounts/{account_id}/nodePools
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
                The maximum number of node pools to return. The maximum
                page_size is 200,

                values above 200 will be coerced to 200.

                If unspecified, the default is 50.
        pageToken:
          schema:
            - type: string
              required: false
              description: >-
                A page token, received from a previous ListNodePools call.
                Provide this

                to retrieve the subsequent page. When paginating, all other
                parameters

                provided to ListNodePools must match the call that provided the
                page

                token.
        filter:
          schema:
            - type: string
              required: false
              description: >-
                Only node pools satisfying the provided filter (if specified)
                will be

                returned. See https://google.aip.dev/160 for the filter grammar.
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
              nodePools:
                allOf:
                  - type: array
                    items:
                      type: object
                      $ref: '#/components/schemas/gatewayNodePool'
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
                    description: The total number of node pools.
            refIdentifier: '#/components/schemas/gatewayListNodePoolsResponse'
        examples:
          example:
            value:
              nodePools:
                - name: <string>
                  displayName: <string>
                  createTime: '2023-11-07T05:31:56Z'
                  minNodeCount: 123
                  maxNodeCount: 123
                  overprovisionNodeCount: 123
                  eksNodePool:
                    nodeRole: <string>
                    instanceType: <string>
                    spot: true
                    nodeGroupName: <string>
                    subnetIds:
                      - <string>
                    zone: <string>
                    placementGroup: <string>
                    launchTemplate: <string>
                  fakeNodePool:
                    machineType: <string>
                    numNodes: 123
                    serviceAccount: <string>
                  annotations: {}
                  state: STATE_UNSPECIFIED
                  status:
                    code: OK
                    message: <string>
                  nodePoolStats:
                    nodeCount: 123
                    ranksPerNode: 123
                    environmentCount: 123
                    environmentRanks: 123
                    batchJobCount: {}
                    batchJobRanks: {}
                  updateTime: '2023-11-07T05:31:56Z'
              nextPageToken: <string>
              totalSize: 123
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
    gatewayEksNodePool:
      type: object
      properties:
        nodeRole:
          type: string
          description: |-
            If not specified, the parent cluster's system_node_group_role
            will be used.
          title: |-
            The IAM role ARN to associate with nodes. The role must have the
            following IAM policies attached:
            - AmazonEKSWorkerNodePolicy
            - AmazonEC2ContainerRegistryReadOnly
            - AmazonEKS_CNI_Policy
        instanceType:
          type: string
          description: >-
            The type of instance used in this node pool. See
            https://aws.amazon.com/ec2/instance-types/

            for a list of valid instance types.
        spot:
          type: boolean
          title: >-
            If true, nodes are created as preemptible VM instances.

            See
            https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html#managed-node-group-capacity-types
        nodeGroupName:
          type: string
          description: |-
            The name of the node group.
            If not specified, the default is the node pool ID.
        subnetIds:
          type: array
          items:
            type: string
          description: >-
            A list of subnet IDs for nodes in this node pool.

            If not specified, the parent cluster's default subnet IDs that
            matches the zone

            will be used. Note that all the subnets will need to be in the same
            zone.
        zone:
          type: string
          description: >-
            Zone for the node pool.

            If not specified, a random zone in the cluster's region will be
            selected.
        placementGroup:
          type: string
          description: Cluster placement group to colocate hosts in this pool.
        launchTemplate:
          type: string
          description: Launch template to create for this node group.
      title: |-
        An Amazon Elastic Kubernetes Service node pool.
        Next ID: 10
      required:
        - instanceType
    gatewayFakeNodePool:
      type: object
      properties:
        machineType:
          type: string
        numNodes:
          type: integer
          format: int32
        serviceAccount:
          type: string
      description: A fake node pool to be used with FakeCluster.
    gatewayNodePool:
      type: object
      properties:
        name:
          type: string
          title: >-
            The resource name of the node pool. e.g.
            accounts/my-account/clusters/my-cluster/nodePools/my-pool
          readOnly: true
        displayName:
          type: string
          description: |-
            Human-readable display name of the node pool. e.g. "My Node Pool"
            Must be fewer than 64 characters long.
        createTime:
          type: string
          format: date-time
          description: The creation time of the node pool.
          readOnly: true
        minNodeCount:
          type: integer
          format: int32
          description: >-
            https://cloud.google.com/kubernetes-engine/quotas

            Minimum number of nodes in this node pool. Must be a non-negative
            integer

            less than or equal to max_node_count.

            If not specified, the default is 0.
        maxNodeCount:
          type: integer
          format: int32
          description: >-
            https://cloud.google.com/kubernetes-engine/quotas

            Maximum number of nodes in this node pool. Must be a positive
            integer

            greater than or equal to min_node_count.

            If not specified, the default is 1.
        overprovisionNodeCount:
          type: integer
          format: int32
          description: |-
            The number of nodes to overprovision by the autoscaler. Must be a
            non-negative integer and less than or equal to min_node_count and
            max_node_count-min_node_count.
            If not specified, the default is 0.
        eksNodePool:
          $ref: '#/components/schemas/gatewayEksNodePool'
        fakeNodePool:
          $ref: '#/components/schemas/gatewayFakeNodePool'
        annotations:
          type: object
          additionalProperties:
            type: string
          description: >-
            Arbitrary, user-specified metadata.

            Keys and values must adhere to Kubernetes constraints:
            https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set

            Additionally, the "fireworks.ai/" prefix is reserved.
        state:
          $ref: '#/components/schemas/gatewayNodePoolState'
          description: The current state of the node pool.
          readOnly: true
        status:
          $ref: '#/components/schemas/gatewayStatus'
          description: >-
            Contains detailed message when the last node pool operation fails,
            e.g.

            when node pool is in FAILED state or when last node pool update
            fails.
          readOnly: true
        nodePoolStats:
          $ref: '#/components/schemas/gatewayNodePoolStats'
          description: Live statistics of the node pool.
          readOnly: true
        updateTime:
          type: string
          format: date-time
          description: The update time for the node pool.
          readOnly: true
      title: 'Next ID: 16'
    gatewayNodePoolState:
      type: string
      enum:
        - STATE_UNSPECIFIED
        - CREATING
        - READY
        - DELETING
        - FAILED
      default: STATE_UNSPECIFIED
      description: |2-
         - CREATING: The cluster is still being created.
         - READY: The node pool is ready to be used.
         - DELETING: The node pool is being deleted.
         - FAILED: Node pool is not operational.
        Consult 'status' for detailed messaging.
        Node pool needs to be deleted and re-created.
    gatewayNodePoolStats:
      type: object
      properties:
        nodeCount:
          type: integer
          format: int32
          description: The number of nodes currently available in this pool.
        ranksPerNode:
          type: integer
          format: int32
          description: >-
            The number of ranks available per node. This is determined by the
            machine

            type of the nodes in this node pool.
        environmentCount:
          type: integer
          format: int32
          description: The number of environments connected to this node pool.
        environmentRanks:
          type: integer
          format: int32
          description: |-
            The number of ranks in this node pool that are currently allocated
            to environment connections.
        batchJobCount:
          type: object
          additionalProperties:
            type: integer
            format: int32
          description: >-
            The key is the string representation of BatchJob.State (e.g.
            "RUNNING").

            The value is the number of batch jobs in that state allocated to
            this

            node pool.
        batchJobRanks:
          type: object
          additionalProperties:
            type: integer
            format: int32
          description: >-
            The key is the string representation of BatchJob.State (e.g.
            "RUNNING").

            The value is the number of ranks allocated to batch jobs in that
            state in

            this node pool.
      title: 'Next ID: 7'
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