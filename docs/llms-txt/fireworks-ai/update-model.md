# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/update-model.md

# Source: https://docs.fireworks.ai/api-reference/update-model.md

# Update Model

## OpenAPI

````yaml patch /v1/accounts/{account_id}/models/{model_id}
paths:
  path: /v1/accounts/{account_id}/models/{model_id}
  method: patch
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
        model_id:
          schema:
            - type: string
              required: true
              description: The Model Id
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              displayName:
                allOf:
                  - type: string
                    description: |-
                      Human-readable display name of the model. e.g. "My Model"
                      Must be fewer than 64 characters long.
              description:
                allOf:
                  - type: string
                    description: >-
                      The description of the model. Must be fewer than 1000
                      characters long.
              state:
                allOf:
                  - $ref: '#/components/schemas/gatewayModelState'
                    description: The state of the model.
                    readOnly: true
              status:
                allOf:
                  - $ref: '#/components/schemas/gatewayStatus'
                    description: >-
                      Contains detailed message when the last model operation
                      fails.
                    readOnly: true
              kind:
                allOf:
                  - $ref: '#/components/schemas/gatewayModelKind'
                    description: |-
                      The kind of model.
                      If not specified, the default is HF_PEFT_ADDON.
              githubUrl:
                allOf:
                  - type: string
                    description: The URL to GitHub repository of the model.
              huggingFaceUrl:
                allOf:
                  - type: string
                    description: The URL to the Hugging Face model.
              baseModelDetails:
                allOf:
                  - $ref: '#/components/schemas/gatewayBaseModelDetails'
                    description: >-
                      Base model details.

                      Required if kind is HF_BASE_MODEL. Must not be set
                      otherwise.
              peftDetails:
                allOf:
                  - $ref: '#/components/schemas/gatewayPEFTDetails'
                    description: |-
                      PEFT addon details.
                      Required if kind is HF_PEFT_ADDON or HF_TEFT_ADDON.
              teftDetails:
                allOf:
                  - $ref: '#/components/schemas/gatewayTEFTDetails'
                    description: >-
                      TEFT addon details.

                      Required if kind is HF_TEFT_ADDON. Must not be set
                      otherwise.
              public:
                allOf:
                  - type: boolean
                    description: If true, the model will be publicly readable.
              conversationConfig:
                allOf:
                  - $ref: '#/components/schemas/gatewayConversationConfig'
                    description: >-
                      If set, the Chat Completions API will be enabled for this
                      model.
              contextLength:
                allOf:
                  - type: integer
                    format: int32
                    description: The maximum context length supported by the model.
              supportsImageInput:
                allOf:
                  - type: boolean
                    description: If set, images can be provided as input to the model.
              supportsTools:
                allOf:
                  - type: boolean
                    description: >-
                      If set, tools (i.e. functions) can be provided as input to
                      the model,

                      and the model may respond with one or more tool calls.
              defaultDraftModel:
                allOf:
                  - type: string
                    description: >-
                      The default draft model to use when creating a deployment.
                      If empty,

                      speculative decoding is disabled by default.
              defaultDraftTokenCount:
                allOf:
                  - type: integer
                    format: int32
                    description: >-
                      The default draft token count to use when creating a
                      deployment.

                      Must be specified if default_draft_model is specified.
              deprecationDate:
                allOf:
                  - $ref: '#/components/schemas/typeDate'
                    description: >-
                      If specified, this is the date when the serverless
                      deployment of the model will be taken down.
              supportsLora:
                allOf:
                  - type: boolean
                    description: Whether this model supports LoRA.
              useHfApplyChatTemplate:
                allOf:
                  - type: boolean
                    description: >-
                      If true, the model will use the Hugging Face
                      apply_chat_template API to apply the chat template.
              trainingContextLength:
                allOf:
                  - type: integer
                    format: int32
                    description: The maximum context length supported by the model.
              snapshotType:
                allOf:
                  - $ref: '#/components/schemas/ModelSnapshotType'
            required: true
            title: |-
              The properties of the model being updated. `model.name` must
              be populated with the updated resource's name.
        examples:
          example:
            value:
              displayName: <string>
              description: <string>
              kind: KIND_UNSPECIFIED
              githubUrl: <string>
              huggingFaceUrl: <string>
              baseModelDetails:
                worldSize: 123
                checkpointFormat: CHECKPOINT_FORMAT_UNSPECIFIED
                parameterCount: <string>
                moe: true
                tunable: true
                modelType: <string>
                supportsFireattention: true
                supportsMtp: true
              peftDetails:
                baseModel: <string>
                r: 123
                targetModules:
                  - <string>
                mergeAddonModelName: <string>
              teftDetails: {}
              public: true
              conversationConfig:
                style: <string>
                system: <string>
                template: <string>
              contextLength: 123
              supportsImageInput: true
              supportsTools: true
              defaultDraftModel: <string>
              defaultDraftTokenCount: 123
              deprecationDate:
                year: 123
                month: 123
                day: 123
              supportsLora: true
              useHfApplyChatTemplate: true
              trainingContextLength: 123
              snapshotType: FULL_SNAPSHOT
        description: |-
          The properties of the model being updated. `model.name` must
          be populated with the updated resource's name.
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
                      The resource name of the model. e.g.
                      accounts/my-account/models/my-model
                    readOnly: true
              displayName:
                allOf:
                  - type: string
                    description: |-
                      Human-readable display name of the model. e.g. "My Model"
                      Must be fewer than 64 characters long.
              description:
                allOf:
                  - type: string
                    description: >-
                      The description of the model. Must be fewer than 1000
                      characters long.
              createTime:
                allOf:
                  - type: string
                    format: date-time
                    description: The creation time of the model.
                    readOnly: true
              state:
                allOf:
                  - $ref: '#/components/schemas/gatewayModelState'
                    description: The state of the model.
                    readOnly: true
              status:
                allOf:
                  - $ref: '#/components/schemas/gatewayStatus'
                    description: >-
                      Contains detailed message when the last model operation
                      fails.
                    readOnly: true
              kind:
                allOf:
                  - $ref: '#/components/schemas/gatewayModelKind'
                    description: |-
                      The kind of model.
                      If not specified, the default is HF_PEFT_ADDON.
              githubUrl:
                allOf:
                  - type: string
                    description: The URL to GitHub repository of the model.
              huggingFaceUrl:
                allOf:
                  - type: string
                    description: The URL to the Hugging Face model.
              baseModelDetails:
                allOf:
                  - $ref: '#/components/schemas/gatewayBaseModelDetails'
                    description: >-
                      Base model details.

                      Required if kind is HF_BASE_MODEL. Must not be set
                      otherwise.
              peftDetails:
                allOf:
                  - $ref: '#/components/schemas/gatewayPEFTDetails'
                    description: |-
                      PEFT addon details.
                      Required if kind is HF_PEFT_ADDON or HF_TEFT_ADDON.
              teftDetails:
                allOf:
                  - $ref: '#/components/schemas/gatewayTEFTDetails'
                    description: >-
                      TEFT addon details.

                      Required if kind is HF_TEFT_ADDON. Must not be set
                      otherwise.
              public:
                allOf:
                  - type: boolean
                    description: If true, the model will be publicly readable.
              conversationConfig:
                allOf:
                  - $ref: '#/components/schemas/gatewayConversationConfig'
                    description: >-
                      If set, the Chat Completions API will be enabled for this
                      model.
              contextLength:
                allOf:
                  - type: integer
                    format: int32
                    description: The maximum context length supported by the model.
              supportsImageInput:
                allOf:
                  - type: boolean
                    description: If set, images can be provided as input to the model.
              supportsTools:
                allOf:
                  - type: boolean
                    description: >-
                      If set, tools (i.e. functions) can be provided as input to
                      the model,

                      and the model may respond with one or more tool calls.
              importedFrom:
                allOf:
                  - type: string
                    description: >-
                      The name of the the model from which this was imported.
                      This field is empty

                      if the model was not imported.
                    readOnly: true
              fineTuningJob:
                allOf:
                  - type: string
                    description: >-
                      If the model was created from a fine-tuning job, this is
                      the fine-tuning

                      job name.
                    readOnly: true
              defaultDraftModel:
                allOf:
                  - type: string
                    description: >-
                      The default draft model to use when creating a deployment.
                      If empty,

                      speculative decoding is disabled by default.
              defaultDraftTokenCount:
                allOf:
                  - type: integer
                    format: int32
                    description: >-
                      The default draft token count to use when creating a
                      deployment.

                      Must be specified if default_draft_model is specified.
              deployedModelRefs:
                allOf:
                  - type: array
                    items:
                      type: object
                      $ref: '#/components/schemas/gatewayDeployedModelRef'
                    description: Populated from GetModel API call only.
                    readOnly: true
              cluster:
                allOf:
                  - type: string
                    description: >-
                      The resource name of the BYOC cluster to which this model
                      belongs.

                      e.g. accounts/my-account/clusters/my-cluster. Empty if it
                      belongs to

                      a Fireworks cluster.
                    readOnly: true
              deprecationDate:
                allOf:
                  - $ref: '#/components/schemas/typeDate'
                    description: >-
                      If specified, this is the date when the serverless
                      deployment of the model will be taken down.
              calibrated:
                allOf:
                  - type: boolean
                    description: >-
                      If true, the model is calibrated and can be deployed to
                      non-FP16 precisions.
                    readOnly: true
              tunable:
                allOf:
                  - type: boolean
                    description: >-
                      If true, the model can be fine-tuned. The value will be
                      true if the tunable field is true, and

                      the model is validated against the model_type field.
                    readOnly: true
              supportsLora:
                allOf:
                  - type: boolean
                    description: Whether this model supports LoRA.
              useHfApplyChatTemplate:
                allOf:
                  - type: boolean
                    description: >-
                      If true, the model will use the Hugging Face
                      apply_chat_template API to apply the chat template.
              updateTime:
                allOf:
                  - type: string
                    format: date-time
                    description: The update time for the model.
                    readOnly: true
              defaultSamplingParams:
                allOf:
                  - type: object
                    additionalProperties:
                      type: number
                      format: float
                    description: >-
                      A json object that contains the default sampling
                      parameters for the model.
                    readOnly: true
              rlTunable:
                allOf:
                  - type: boolean
                    description: If true, the model is RL tunable.
                    readOnly: true
              supportedPrecisions:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/DeploymentPrecision'
                    title: Supported precisions
                    readOnly: true
              supportedPrecisionsWithCalibration:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/DeploymentPrecision'
                    title: Supported precisions if calibrated
                    readOnly: true
              trainingContextLength:
                allOf:
                  - type: integer
                    format: int32
                    description: The maximum context length supported by the model.
              snapshotType:
                allOf:
                  - $ref: '#/components/schemas/ModelSnapshotType'
            title: 'Next ID: 56'
            refIdentifier: '#/components/schemas/gatewayModel'
        examples:
          example:
            value:
              name: <string>
              displayName: <string>
              description: <string>
              createTime: '2023-11-07T05:31:56Z'
              state: STATE_UNSPECIFIED
              status:
                code: OK
                message: <string>
              kind: KIND_UNSPECIFIED
              githubUrl: <string>
              huggingFaceUrl: <string>
              baseModelDetails:
                worldSize: 123
                checkpointFormat: CHECKPOINT_FORMAT_UNSPECIFIED
                parameterCount: <string>
                moe: true
                tunable: true
                modelType: <string>
                supportsFireattention: true
                defaultPrecision: PRECISION_UNSPECIFIED
                supportsMtp: true
              peftDetails:
                baseModel: <string>
                r: 123
                targetModules:
                  - <string>
                baseModelType: <string>
                mergeAddonModelName: <string>
              teftDetails: {}
              public: true
              conversationConfig:
                style: <string>
                system: <string>
                template: <string>
              contextLength: 123
              supportsImageInput: true
              supportsTools: true
              importedFrom: <string>
              fineTuningJob: <string>
              defaultDraftModel: <string>
              defaultDraftTokenCount: 123
              deployedModelRefs:
                - name: <string>
                  deployment: <string>
                  state: STATE_UNSPECIFIED
                  default: true
                  public: true
              cluster: <string>
              deprecationDate:
                year: 123
                month: 123
                day: 123
              calibrated: true
              tunable: true
              supportsLora: true
              useHfApplyChatTemplate: true
              updateTime: '2023-11-07T05:31:56Z'
              defaultSamplingParams: {}
              rlTunable: true
              supportedPrecisions:
                - PRECISION_UNSPECIFIED
              supportedPrecisionsWithCalibration:
                - PRECISION_UNSPECIFIED
              trainingContextLength: 123
              snapshotType: FULL_SNAPSHOT
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas:
    BaseModelDetailsCheckpointFormat:
      type: string
      enum:
        - CHECKPOINT_FORMAT_UNSPECIFIED
        - NATIVE
        - HUGGINGFACE
      default: CHECKPOINT_FORMAT_UNSPECIFIED
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
    ModelSnapshotType:
      type: string
      enum:
        - FULL_SNAPSHOT
        - INCREMENTAL_SNAPSHOT
      default: FULL_SNAPSHOT
    gatewayBaseModelDetails:
      type: object
      properties:
        worldSize:
          type: integer
          format: int32
          description: |-
            The default number of GPUs the model is served with.
            If not specified, the default is 1.
        checkpointFormat:
          $ref: '#/components/schemas/BaseModelDetailsCheckpointFormat'
        parameterCount:
          type: string
          format: int64
          description: >-
            The number of model parameters. For serverless models, this
            determines the

            price per token.
        moe:
          type: boolean
          description: >-
            If true, this is a Mixture of Experts (MoE) model. For serverless
            models,

            this affects the price per token.
        tunable:
          type: boolean
          description: If true, this model is available for fine-tuning.
        modelType:
          type: string
          description: The type of the model.
        supportsFireattention:
          type: boolean
          description: Whether this model supports fireattention.
        defaultPrecision:
          $ref: '#/components/schemas/DeploymentPrecision'
          description: Default precision of the model.
          readOnly: true
        supportsMtp:
          type: boolean
          description: If true, this model supports MTP.
      title: 'Next ID: 11'
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
    gatewayConversationConfig:
      type: object
      properties:
        style:
          type: string
          description: The chat template to use.
        system:
          type: string
          description: The system prompt (if the chat style supports it).
        template:
          type: string
          description: The Jinja template (if style is "jinja").
      required:
        - style
    gatewayDeployedModelRef:
      type: object
      properties:
        name:
          type: string
          title: >-
            The resource name. e.g.
            accounts/my-account/deployedModels/my-deployed-model
          readOnly: true
        deployment:
          type: string
          description: The resource name of the base deployment the model is deployed to.
          readOnly: true
        state:
          $ref: '#/components/schemas/gatewayDeployedModelState'
          description: The state of the deployed model.
          readOnly: true
        default:
          type: boolean
          description: >-
            If true, this is the default target when querying this model without

            the `#<deployment>` suffix.

            The first deployment a model is deployed to will have this field set
            to

            true automatically.
          readOnly: true
        public:
          type: boolean
          description: If true, the deployed model will be publicly reachable.
          readOnly: true
      title: 'Next ID: 6'
    gatewayDeployedModelState:
      type: string
      enum:
        - STATE_UNSPECIFIED
        - UNDEPLOYING
        - DEPLOYING
        - DEPLOYED
        - UPDATING
      default: STATE_UNSPECIFIED
      description: |-
        - UNDEPLOYING: The model is being undeployed.
         - DEPLOYING: The model is being deployed.
         - DEPLOYED: The model is deployed and ready for inference.
         - UPDATING: there are updates happening with the deployed model
      title: 'Next ID: 6'
    gatewayModelKind:
      type: string
      enum:
        - KIND_UNSPECIFIED
        - HF_BASE_MODEL
        - HF_PEFT_ADDON
        - HF_TEFT_ADDON
        - FLUMINA_BASE_MODEL
        - FLUMINA_ADDON
        - DRAFT_ADDON
        - FIRE_AGENT
        - LIVE_MERGE
        - CUSTOM_MODEL
        - EMBEDDING_MODEL
        - SNAPSHOT_MODEL
      default: KIND_UNSPECIFIED
      description: |2-
         - HF_BASE_MODEL: An LLM base model.
         - HF_PEFT_ADDON: A parameter-efficent fine-tuned addon.
         - HF_TEFT_ADDON: A token-eficient fine-tuned addon.
         - FLUMINA_BASE_MODEL: A Flumina base model.
         - FLUMINA_ADDON: A Flumina addon.
         - DRAFT_ADDON: A draft model used for speculative decoding in a deployment.
         - FIRE_AGENT: A FireAgent model.
         - LIVE_MERGE: A live-merge model.
         - CUSTOM_MODEL: A customized model
         - EMBEDDING_MODEL: An Embedding model.
         - SNAPSHOT_MODEL: A snapshot model.
    gatewayModelState:
      type: string
      enum:
        - STATE_UNSPECIFIED
        - UPLOADING
        - READY
      default: STATE_UNSPECIFIED
      description: |-
        - UPLOADING: The model is still being uploaded (upload is asynchronous).
         - READY: The model is ready to be used.
      title: 'Next ID: 7'
    gatewayPEFTDetails:
      type: object
      properties:
        baseModel:
          type: string
          title: The base model name. e.g. accounts/fireworks/models/falcon-7b
        r:
          type: integer
          format: int32
          description: |-
            The rank of the update matrices.
            Must be between 4 and 64, inclusive.
        targetModules:
          type: array
          items:
            type: string
          title: >-
            This is the target modules for an adapter that we extract from

            for more information what target module means, check out

            https://huggingface.co/docs/peft/conceptual_guides/lora#common-lora-parameters-in-peft
        baseModelType:
          type: string
          description: The type of the model.
          readOnly: true
        mergeAddonModelName:
          type: string
          title: >-
            The resource name of the model to merge with base model, e.g
            accounts/fireworks/models/falcon-7b-lora
      title: |-
        PEFT addon details.
        Next ID: 6
      required:
        - baseModel
        - r
        - targetModules
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
    gatewayTEFTDetails:
      type: object
    typeDate:
      type: object
      properties:
        year:
          type: integer
          format: int32
          description: >-
            Year of the date. Must be from 1 to 9999, or 0 to specify a date
            without

            a year.
        month:
          type: integer
          format: int32
          description: >-
            Month of a year. Must be from 1 to 12, or 0 to specify a year
            without a

            month and day.
        day:
          type: integer
          format: int32
          description: >-
            Day of a month. Must be from 1 to 31 and valid for the year and
            month, or 0

            to specify a year by itself or a year and month where the day isn't

            significant.
      description: >-
        * A full date, with non-zero year, month, and day values

        * A month and day value, with a zero year, such as an anniversary

        * A year on its own, with zero month and day values

        * A year and month value, with a zero day, such as a credit card
        expiration

        date


        Related types are [google.type.TimeOfDay][google.type.TimeOfDay] and

        `google.protobuf.Timestamp`.
      title: >-
        Represents a whole or partial calendar date, such as a birthday. The
        time of

        day and time zone are either specified elsewhere or are insignificant.
        The

        date is relative to the Gregorian Calendar. This can represent one of
        the

        following:

````