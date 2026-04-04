# Source: https://docs.fireworks.ai/api-reference/get-deployment-shape.md

# Get Deployment Shape



## OpenAPI

````yaml get /v1/accounts/{account_id}/deploymentShapes/{deployment_shape_id}
openapi: 3.1.0
info:
  title: Gateway REST API
  version: 4.15.25
servers:
  - url: https://api.fireworks.ai
security:
  - BearerAuth: []
tags:
  - name: Gateway
paths:
  /v1/accounts/{account_id}/deploymentShapes/{deployment_shape_id}:
    get:
      tags:
        - Gateway
      summary: Get Deployment Shape
      operationId: Gateway_GetDeploymentShape
      parameters:
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
        - name: deployment_shape_id
          in: path
          required: true
          description: The Deployment Shape Id
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/gatewayDeploymentShape'
components:
  schemas:
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
        disableDeploymentSizeValidation:
          type: boolean
          description: If true, the deployment size validation is disabled.
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
        presetType:
          $ref: '#/components/schemas/DeploymentShapePresetType'
          description: Type of deployment shape for different deployment configurations.
      title: >-
        A deployment shape is a set of parameters that define the shape of a
        deployment.

        Deployments are created from a deployment shape.

        Next ID: 34
      required:
        - baseModel
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
        - AMD_MI350X_288GB
      default: ACCELERATOR_TYPE_UNSPECIFIED
      title: 'Next ID: 11'
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
        - FULL_PRECISION
      default: PRESET_TYPE_UNSPECIFIED
      title: |-
        - MINIMAL: Preset for cheapest & most minimal type of deployment
         - FAST: Preset for fastest generation & TTFT deployment
         - THROUGHPUT: Preset for best throughput deployment
         - FULL_PRECISION: Preset for deployment with full precision for training & most accurate numerics
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.fireworks.ai/llms.txt