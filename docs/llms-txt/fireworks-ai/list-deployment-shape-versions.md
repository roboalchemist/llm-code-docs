# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-deployment-shape-versions.md

# Source: https://docs.fireworks.ai/api-reference/list-deployment-shape-versions.md

# List Deployment Shapes Versions

## OpenAPI

````yaml get /v1/accounts/{account_id}/deploymentShapes/{deployment_shape_id}/versions
paths:
  path: /v1/accounts/{account_id}/deploymentShapes/{deployment_shape_id}/versions
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
        deployment_shape_id:
          schema:
            - type: string
              required: true
              description: The Deployment Shape Id
      query:
        pageSize:
          schema:
            - type: integer
              required: false
              description: >-
                The maximum number of deployment shape versions to return. The
                maximum page_size is 200,

                values above 200 will be coerced to 200.

                If unspecified, the default is 50.
        pageToken:
          schema:
            - type: string
              required: false
              description: >-
                A page token, received from a previous
                ListDeploymentShapeVersions call. Provide this

                to retrieve the subsequent page. When paginating, all other
                parameters

                provided to ListDeploymentShapeVersions must match the call that
                provided the page

                token.
        filter:
          schema:
            - type: string
              required: false
              description: >-
                Only deployment shape versions satisfying the provided filter
                (if specified) will be

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

                If not specified, the default order is by "create_time".
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
              deploymentShapeVersions:
                allOf:
                  - type: array
                    items:
                      type: object
                      $ref: '#/components/schemas/gatewayDeploymentShapeVersion'
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
                    description: The total number of deployment shape versions.
            refIdentifier: '#/components/schemas/gatewayListDeploymentShapeVersionsResponse'
        examples:
          example:
            value:
              deploymentShapeVersions:
                - name: <string>
                  createTime: '2023-11-07T05:31:56Z'
                  snapshot:
                    name: <string>
                    displayName: <string>
                    description: <string>
                    createTime: '2023-11-07T05:31:56Z'
                    updateTime: '2023-11-07T05:31:56Z'
                    baseModel: <string>
                    modelType: <string>
                    parameterCount: <string>
                    acceleratorCount: 123
                    acceleratorType: ACCELERATOR_TYPE_UNSPECIFIED
                    precision: PRECISION_UNSPECIFIED
                    enableAddons: true
                    draftTokenCount: 123
                    draftModel: <string>
                    ngramSpeculationLength: 123
                    enableSessionAffinity: true
                    numLoraDeviceCached: 123
                    presetType: PRESET_TYPE_UNSPECIFIED
                  validated: true
                  public: true
                  latestValidated: true
              nextPageToken: <string>
              totalSize: 123
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
    DeploymentShapePresetType:
      type: string
      enum:
        - PRESET_TYPE_UNSPECIFIED
        - MINIMAL
        - FAST
        - THROUGHPUT
        - REINFORCEMENT_FINE_TUNING
      default: PRESET_TYPE_UNSPECIFIED
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
    gatewayDeploymentShape:
      type: object
      properties:
        name:
          type: string
          title: >-
            The resource name of the deployment shape. e.g.
            accounts/my-account/deploymentShapes/my-deployment-shape
          readOnly: true
        displayName:
          type: string
          description: >-
            Human-readable display name of the deployment shape. e.g. "My
            Deployment Shape"

            Must be fewer than 64 characters long.
        description:
          type: string
          description: >-
            The description of the deployment shape. Must be fewer than 1000
            characters long.
        createTime:
          type: string
          format: date-time
          description: The creation time of the deployment shape.
          readOnly: true
        updateTime:
          type: string
          format: date-time
          description: The update time for the deployment shape.
          readOnly: true
        baseModel:
          type: string
          title: The base model name. e.g. accounts/fireworks/models/falcon-7b
        modelType:
          type: string
          description: The model type of the base model.
          readOnly: true
        parameterCount:
          type: string
          format: int64
          description: The parameter count of the base model .
          readOnly: true
        acceleratorCount:
          type: integer
          format: int32
          description: >-
            The number of accelerators used per replica.

            If not specified, the default is the estimated minimum required by
            the base model.
        acceleratorType:
          $ref: '#/components/schemas/gatewayAcceleratorType'
          description: |-
            The type of accelerator to use.
            If not specified, the default is NVIDIA_A100_80GB.
        precision:
          $ref: '#/components/schemas/DeploymentPrecision'
          description: The precision with which the model should be served.
        enableAddons:
          type: boolean
          description: >-
            If true, LORA addons are enabled for deployments created from this
            shape.
        draftTokenCount:
          type: integer
          format: int32
          description: |-
            The number of candidate tokens to generate per step for speculative
            decoding.
            Default is the base model's draft_token_count.
        draftModel:
          type: string
          description: >-
            The draft model name for speculative decoding. e.g.
            accounts/fireworks/models/my-draft-model

            If empty, speculative decoding using a draft model is disabled.

            Default is the base model's default_draft_model.

            this behavior.
        ngramSpeculationLength:
          type: integer
          format: int32
          description: >-
            The length of previous input sequence to be considered for N-gram
            speculation.
        enableSessionAffinity:
          type: boolean
          description: Whether to apply sticky routing based on `user` field.
        numLoraDeviceCached:
          type: integer
          format: int32
          title: How many LORA adapters to keep on GPU side for caching
          readOnly: true
        presetType:
          $ref: '#/components/schemas/DeploymentShapePresetType'
          description: Type of deployment shape for different deployment configurations.
      title: >-
        A deployment shape is a set of parameters that define the shape of a
        deployment.

        Deployments are created from a deployment shape.

        Next ID: 33
      required:
        - baseModel
    gatewayDeploymentShapeVersion:
      type: object
      properties:
        name:
          type: string
          title: >-
            The resource name of the deployment shape version. e.g.
            accounts/my-account/deploymentShapes/my-deployment-shape/versions/{version_id}
          readOnly: true
        createTime:
          type: string
          format: date-time
          description: >-
            The creation time of the deployment shape version. Lists will be
            ordered by this field.
          readOnly: true
        snapshot:
          $ref: '#/components/schemas/gatewayDeploymentShape'
          description: Full snapshot of the Deployment Shape at this version.
          readOnly: true
        validated:
          type: boolean
          description: If true, this version has been validated.
        public:
          type: boolean
          description: If true, this version will be publicly readable.
        latestValidated:
          type: boolean
          description: |-
            If true, this version is the latest validated version.
            Only one version of the shape can be the latest validated version.
          readOnly: true
      title: >-
        A deployment shape version is a specific version of a deployment shape.

        Versions are immutable, only created on updates and deleted when the
        deployment shape is deleted.

        Next ID: 9

````