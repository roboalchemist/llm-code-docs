# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-deployment.md

# Source: https://docs.fireworks.ai/api-reference/get-deployment.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-deployment.md

# Source: https://docs.fireworks.ai/api-reference/get-deployment.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-deployment.md

# Source: https://docs.fireworks.ai/api-reference/get-deployment.md

# Get Deployment

## OpenAPI

````yaml get /v1/accounts/{account_id}/deployments/{deployment_id}
paths:
  path: /v1/accounts/{account_id}/deployments/{deployment_id}
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
        deployment_id:
          schema:
            - type: string
              required: true
              description: The Deployment Id
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
                      The resource name of the deployment. e.g.
                      accounts/my-account/deployments/my-deployment
                    readOnly: true
              displayName:
                allOf:
                  - type: string
                    description: >-
                      Human-readable display name of the deployment. e.g. "My
                      Deployment"

                      Must be fewer than 64 characters long.
              description:
                allOf:
                  - type: string
                    description: Description of the deployment.
              createTime:
                allOf:
                  - type: string
                    format: date-time
                    description: The creation time of the deployment.
                    readOnly: true
              expireTime:
                allOf:
                  - type: string
                    format: date-time
                    description: >-
                      The time at which this deployment will automatically be
                      deleted.
              purgeTime:
                allOf:
                  - type: string
                    format: date-time
                    description: The time at which the resource will be hard deleted.
                    readOnly: true
              deleteTime:
                allOf:
                  - type: string
                    format: date-time
                    description: The time at which the resource will be soft deleted.
                    readOnly: true
              state:
                allOf:
                  - $ref: '#/components/schemas/gatewayDeploymentState'
                    description: The state of the deployment.
                    readOnly: true
              status:
                allOf:
                  - $ref: '#/components/schemas/gatewayStatus'
                    description: >-
                      Detailed status information regarding the most recent
                      operation.
                    readOnly: true
              minReplicaCount:
                allOf:
                  - type: integer
                    format: int32
                    description: |-
                      The minimum number of replicas.
                      If not specified, the default is 0.
              maxReplicaCount:
                allOf:
                  - type: integer
                    format: int32
                    description: >-
                      The maximum number of replicas.

                      If not specified, the default is max(min_replica_count,
                      1).

                      May be set to 0 to downscale the deployment to 0.
              desiredReplicaCount:
                allOf:
                  - type: integer
                    format: int32
                    description: >-
                      The desired number of replicas for this deployment. This
                      represents the target

                      replica count that the system is trying to achieve.
                    readOnly: true
              replicaCount:
                allOf:
                  - type: integer
                    format: int32
                    readOnly: true
              autoscalingPolicy:
                allOf:
                  - $ref: '#/components/schemas/gatewayAutoscalingPolicy'
              baseModel:
                allOf:
                  - type: string
                    title: >-
                      The base model name. e.g.
                      accounts/fireworks/models/falcon-7b
              acceleratorCount:
                allOf:
                  - type: integer
                    format: int32
                    description: >-
                      The number of accelerators used per replica.

                      If not specified, the default is the estimated minimum
                      required by the

                      base model.
              acceleratorType:
                allOf:
                  - $ref: '#/components/schemas/gatewayAcceleratorType'
                    description: |-
                      The type of accelerator to use.
                      If not specified, the default is NVIDIA_A100_80GB.
              precision:
                allOf:
                  - $ref: '#/components/schemas/DeploymentPrecision'
                    description: The precision with which the model should be served.
              cluster:
                allOf:
                  - type: string
                    description: >-
                      If set, this deployment is deployed to a cloud-premise
                      cluster.
                    readOnly: true
              enableAddons:
                allOf:
                  - type: boolean
                    description: If true, PEFT addons are enabled for this deployment.
              draftTokenCount:
                allOf:
                  - type: integer
                    format: int32
                    description: >-
                      The number of candidate tokens to generate per step for
                      speculative

                      decoding.

                      Default is the base model's draft_token_count. Set

                      CreateDeploymentRequest.disable_speculative_decoding to
                      false to disable

                      this behavior.
              draftModel:
                allOf:
                  - type: string
                    description: >-
                      The draft model name for speculative decoding. e.g.
                      accounts/fireworks/models/my-draft-model

                      If empty, speculative decoding using a draft model is
                      disabled.

                      Default is the base model's default_draft_model. Set

                      CreateDeploymentRequest.disable_speculative_decoding to
                      false to disable

                      this behavior.
              ngramSpeculationLength:
                allOf:
                  - type: integer
                    format: int32
                    description: >-
                      The length of previous input sequence to be considered for
                      N-gram speculation.
              enableSessionAffinity:
                allOf:
                  - type: boolean
                    description: Whether to apply sticky routing based on `user` field.
              directRouteApiKeys:
                allOf:
                  - type: array
                    items:
                      type: string
                    description: >-
                      The set of API keys used to access the direct route
                      deployment. If direct routing is not enabled, this field
                      is unused.
              numPeftDeviceCached:
                allOf:
                  - type: integer
                    format: int32
                    title: How many peft adapters to keep on gpu side for caching
                    readOnly: true
              directRouteType:
                allOf:
                  - $ref: '#/components/schemas/gatewayDirectRouteType'
                    description: >-
                      If set, this deployment will expose an endpoint that
                      bypasses the Fireworks API gateway.
              directRouteHandle:
                allOf:
                  - type: string
                    description: >-
                      The handle for calling a direct route. The meaning of the
                      handle depends on the

                      direct route type of the deployment:
                         INTERNET                    -> The host name for accessing the deployment
                         GCP_PRIVATE_SERVICE_CONNECT -> The service attachment name used to create the PSC endpoint.
                         AWS_PRIVATELINK             -> The service name used to create the VPC endpoint.
                    readOnly: true
              deploymentTemplate:
                allOf:
                  - type: string
                    description: >-
                      The name of the deployment template to use for this
                      deployment. Only

                      available to enterprise accounts.
              autoTune:
                allOf:
                  - $ref: '#/components/schemas/gatewayAutoTune'
                    description: The performance profile to use for this deployment.
              placement:
                allOf:
                  - $ref: '#/components/schemas/gatewayPlacement'
                    description: >-
                      The desired geographic region where the deployment must be
                      placed.

                      If unspecified, the default is the GLOBAL multi-region.
              region:
                allOf:
                  - $ref: '#/components/schemas/gatewayRegion'
                    description: >-
                      The geographic region where the deployment is presently
                      located. This region may change

                      over time, but within the `placement` constraint.
                    readOnly: true
              updateTime:
                allOf:
                  - type: string
                    format: date-time
                    description: The update time for the deployment.
                    readOnly: true
              disableDeploymentSizeValidation:
                allOf:
                  - type: boolean
                    description: Whether the deployment size validation is disabled.
              enableMtp:
                allOf:
                  - type: boolean
                    description: If true, MTP is enabled for this deployment.
              enableHotReloadLatestAddon:
                allOf:
                  - type: boolean
                    description: >-
                      Allows up to 1 addon at a time to be loaded, and will
                      merge it into the base model.
              deploymentShape:
                allOf:
                  - type: string
                    description: >-
                      The name of the deployment shape that this deployment is
                      using.

                      On the server side, this will be replaced with the
                      deployment shape version name.
              activeModelVersion:
                allOf:
                  - type: string
                    description: >-
                      The model version that is currently active and applied to
                      running replicas of a deployment.
              targetModelVersion:
                allOf:
                  - type: string
                    description: >-
                      The target model version that is being rolled out to the
                      deployment.

                      In a ready steady state, the target model version is the
                      same as the active model version.
            title: 'Next ID: 82'
            refIdentifier: '#/components/schemas/gatewayDeployment'
            requiredProperties:
              - baseModel
        examples:
          example:
            value:
              name: <string>
              displayName: <string>
              description: <string>
              createTime: '2023-11-07T05:31:56Z'
              expireTime: '2023-11-07T05:31:56Z'
              purgeTime: '2023-11-07T05:31:56Z'
              deleteTime: '2023-11-07T05:31:56Z'
              state: STATE_UNSPECIFIED
              status:
                code: OK
                message: <string>
              minReplicaCount: 123
              maxReplicaCount: 123
              desiredReplicaCount: 123
              replicaCount: 123
              autoscalingPolicy:
                scaleUpWindow: <string>
                scaleDownWindow: <string>
                scaleToZeroWindow: <string>
                loadTargets: {}
              baseModel: <string>
              acceleratorCount: 123
              acceleratorType: ACCELERATOR_TYPE_UNSPECIFIED
              precision: PRECISION_UNSPECIFIED
              cluster: <string>
              enableAddons: true
              draftTokenCount: 123
              draftModel: <string>
              ngramSpeculationLength: 123
              enableSessionAffinity: true
              directRouteApiKeys:
                - <string>
              numPeftDeviceCached: 123
              directRouteType: DIRECT_ROUTE_TYPE_UNSPECIFIED
              directRouteHandle: <string>
              deploymentTemplate: <string>
              autoTune:
                longPrompt: true
              placement:
                region: REGION_UNSPECIFIED
                multiRegion: MULTI_REGION_UNSPECIFIED
                regions:
                  - REGION_UNSPECIFIED
              region: REGION_UNSPECIFIED
              updateTime: '2023-11-07T05:31:56Z'
              disableDeploymentSizeValidation: true
              enableMtp: true
              enableHotReloadLatestAddon: true
              deploymentShape: <string>
              activeModelVersion: <string>
              targetModelVersion: <string>
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
    gatewayAcceleratorType:
      type: string
      enum:
        - ACCELERATOR_TYPE_UNSPECIFIED
        - NVIDIA_A100_80GB
        - NVIDIA_H100_80GB
        - AMD_MI300X_192GB
        - NVIDIA_A10G_24GB
        - NVIDIA_A100_40GB
        - NVIDIA_L4_24GB
        - NVIDIA_H200_141GB
        - NVIDIA_B200_180GB
        - AMD_MI325X_256GB
      default: ACCELERATOR_TYPE_UNSPECIFIED
    gatewayAutoTune:
      type: object
      properties:
        longPrompt:
          type: boolean
          description: If true, this deployment is optimized for long prompt lengths.
    gatewayAutoscalingPolicy:
      type: object
      properties:
        scaleUpWindow:
          type: string
          description: >-
            The duration the autoscaler will wait before scaling up a deployment
            after observing

            increased load. Default is 30s.
        scaleDownWindow:
          type: string
          description: >-
            The duration the autoscaler will wait before scaling down a
            deployment after observing

            decreased load. Default is 10m.
        scaleToZeroWindow:
          type: string
          description: >-
            The duration after which there are no requests that the deployment
            will be scaled down

            to zero replicas, if min_replica_count==0. Default is 1h.

            This must be at least 5 minutes.
        loadTargets:
          type: object
          additionalProperties:
            type: number
            format: float
          title: >-
            Map of load metric names to their target utilization factors.

            Currently only the "default" key is supported, which specifies the
            default target for all metrics.

            If not specified, the default target is 0.8
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
    gatewayDeploymentState:
      type: string
      enum:
        - STATE_UNSPECIFIED
        - CREATING
        - READY
        - DELETING
        - FAILED
        - UPDATING
        - DELETED
      default: STATE_UNSPECIFIED
      description: |2-
         - CREATING: The deployment is still being created.
         - READY: The deployment is ready to be used.
         - DELETING: The deployment is being deleted.
         - FAILED: The deployment failed to be created. See the `status` field for
        additional details on why it failed.
         - UPDATING: There are in-progress updates happening with the deployment.
         - DELETED: The deployment is soft-deleted.
    gatewayDirectRouteType:
      type: string
      enum:
        - DIRECT_ROUTE_TYPE_UNSPECIFIED
        - INTERNET
        - GCP_PRIVATE_SERVICE_CONNECT
        - AWS_PRIVATELINK
      default: DIRECT_ROUTE_TYPE_UNSPECIFIED
      title: |-
        - DIRECT_ROUTE_TYPE_UNSPECIFIED: No direct routing
         - INTERNET: The direct route is exposed via the public internet
         - GCP_PRIVATE_SERVICE_CONNECT: The direct route is exposed via GCP Private Service Connect
         - AWS_PRIVATELINK: The direct route is exposed via AWS PrivateLink
    gatewayMultiRegion:
      type: string
      enum:
        - MULTI_REGION_UNSPECIFIED
        - GLOBAL
        - US
      default: MULTI_REGION_UNSPECIFIED
    gatewayPlacement:
      type: object
      properties:
        region:
          $ref: '#/components/schemas/gatewayRegion'
          description: The region where the deployment must be placed.
        multiRegion:
          $ref: '#/components/schemas/gatewayMultiRegion'
          description: The multi-region where the deployment must be placed.
        regions:
          type: array
          items:
            $ref: '#/components/schemas/gatewayRegion'
          title: The list of regions where the deployment must be placed
      description: >-
        The desired geographic region where the deployment must be placed.
        Exactly one field will be

        specified.
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

````