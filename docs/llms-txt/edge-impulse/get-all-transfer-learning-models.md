# Source: https://docs.edgeimpulse.com/apis/studio/impulse/get-all-transfer-learning-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all transfer learning models

> Retrieve all transfer learning models across all categories



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/transfer-learning-models
openapi: 3.0.0
info:
  title: Edge Impulse API
  version: 1.0.0
servers:
  - url: https://studio.edgeimpulse.com/v1
security:
  - ApiKeyAuthentication: []
  - JWTAuthentication: []
  - JWTHttpHeaderAuthentication: []
  - OAuth2: []
paths:
  /api/{projectId}/transfer-learning-models:
    get:
      tags:
        - Impulse
      summary: Get all transfer learning models
      description: Retrieve all transfer learning models across all categories
      operationId: getAllTransferLearningModels
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetAllTransferLearningModelsResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
  schemas:
    GetAllTransferLearningModelsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - transferLearningModels
          properties:
            transferLearningModels:
              type: array
              items:
                $ref: '#/components/schemas/TransferLearningModel'
    GenericApiResponse:
      type: object
      required:
        - success
      properties:
        success:
          type: boolean
          description: Whether the operation succeeded
        error:
          type: string
          description: Optional error description (set if 'success' was false)
    TransferLearningModel:
      type: object
      required:
        - name
        - shortName
        - description
        - hasNeurons
        - hasDropout
        - type
        - learnBlockType
        - author
        - blockType
        - hasExpertMode
      properties:
        name:
          type: string
        shortName:
          type: string
        abbreviatedName:
          type: string
        description:
          type: string
        hasNeurons:
          type: boolean
        hasDropout:
          type: boolean
        defaultNeurons:
          type: integer
        defaultDropout:
          type: number
        defaultLearningRate:
          type: number
        defaultTrainingCycles:
          type: number
        hasImageAugmentation:
          type: boolean
        type:
          $ref: '#/components/schemas/KerasVisualLayerType'
        learnBlockType:
          $ref: '#/components/schemas/LearnBlockType'
        organizationModelId:
          type: integer
        implementationVersion:
          type: integer
        repositoryUrl:
          type: string
          description: URL to the source code of this custom learn block.
        author:
          type: string
        blockType:
          $ref: '#/components/schemas/BlockType'
        customParameters:
          type: array
          items:
            $ref: '#/components/schemas/DSPGroupItem'
        displayCategory:
          $ref: '#/components/schemas/BlockDisplayCategory'
        blockNoLongerAvailable:
          type: object
          description: >-
            If this object is set, then you can no longer train this block. The
            reason (or a migration path) is in the `reasonMarkdown` and
            `reasonHtml` properties.
          required:
            - reasonMarkdown
            - reasonHtml
          properties:
            reasonMarkdown:
              description: >-
                Reason or migration path for current users of this block, in
                Markdown format.
              type: string
            reasonHtml:
              description: >-
                Reason or migration path for current users of this block, in
                HTML format.
              type: string
        hasExpertMode:
          description: Whether this block can be switched to expert mode.
          type: boolean
    KerasVisualLayerType:
      type: string
      enum:
        - dense
        - conv1d
        - conv2d
        - reshape
        - flatten
        - dropout
        - batchNormalization
        - transfer_mobilenetv2_a35
        - transfer_mobilenetv2_a1
        - transfer_mobilenetv2_a05
        - transfer_mobilenetv2_160_a1
        - transfer_mobilenetv2_160_a75
        - transfer_mobilenetv2_160_a5
        - transfer_mobilenetv2_160_a35
        - transfer_mobilenetv1_a25_d100
        - transfer_mobilenetv1_a2_d100
        - transfer_mobilenetv1_a1_d100
        - transfer_kws_mobilenetv1_a1_d100
        - transfer_kws_mobilenetv2_a35_d100
        - transfer_kws_syntiant_ndp10x
        - transfer_kws_conv2d_tiny
        - object_ssd_mobilenet_v2_fpnlite_320x320
        - fomo_mobilenet_v2_a01
        - fomo_mobilenet_v2_a35
        - transfer_organization
        - transfer_akidanet_imagenet_160_a100
        - transfer_akidanet_imagenet_160_a50
        - transfer_akidanet_imagenet_160_a25
        - transfer_akidanet_imagenet_224_a100
        - transfer_akidanet_imagenet_224_a50
        - transfer_akidanet_imagenet_224_a25
        - fomo_akidanet_a50
        - fomo_ad_gmm
        - fomo_ad_patchcore
    LearnBlockType:
      type: string
      description: >-
        The type of learning block (anomaly, keras, keras-transfer-image,
        keras-transfer-kws, keras-object-detection, keras-regression,
        keras-freeform). Each behaves differently.
      enum:
        - anomaly
        - anomaly-gmm
        - keras
        - keras-transfer-image
        - keras-transfer-kws
        - keras-object-detection
        - keras-regression
        - keras-akida
        - keras-akida-transfer-image
        - keras-akida-object-detection
        - keras-visual-anomaly
        - keras-freeform
        - keras-anomaly
        - vlm
    BlockType:
      type: string
      enum:
        - official
        - personal
        - enterprise
        - community
    DSPGroupItem:
      type: object
      required:
        - name
        - type
        - param
        - defaultValue
        - readonly
        - shouldShow
        - required
        - showClickToSet
      properties:
        name:
          type: string
          example: Scale axes
        value:
          type: string
        defaultValue:
          type: string
        type:
          type: string
          example: text
        help:
          type: string
          example: Divide axes by this number
        param:
          type: string
          example: scale-axes
        selectOptions:
          type: array
          items:
            type: object
            properties:
              value:
                type: string
                description: >-
                  What is the string that will be set if this option is
                  selected?
              selected:
                type: boolean
              optionLabel:
                type: string
                description: >-
                  What is the label that will be shown to the user for this
                  option?
              priority:
                type: number
                description: >-
                  The following options are optional.  See Learn Block Auto
                  Config in Notion. Higher priority will get chosen based on
                  limits below.
              romEstimate:
                type: number
                description: >-
                  Estimated ROM footprint for this choice.  Will be tested
                  against ROM budget in Studio.
              needsOps:
                type: array
                items:
                  type: string
                  description: ML operator needed by this choice.
              needsFeatures:
                type: array
                items:
                  type: string
                  description: Feature needed by this choice. (non op related)
        readonly:
          type: boolean
        shouldShow:
          type: boolean
        showIf:
          type: object
          required:
            - parameter
            - operator
            - value
          properties:
            parameter:
              type: string
            operator:
              type: string
              enum:
                - eq
                - neq
            value:
              type: string
        invalidText:
          type: string
        section:
          type: string
          description: Interface section to render parameter in.
          enum:
            - advanced
            - augmentation
            - modelProfiling
        multiline:
          type: boolean
          description: Only valid for type "string". Will render a multiline text area.
        required:
          type: boolean
        hint:
          type: string
          description: If set, shows a hint below the input.
        placeholder:
          type: string
          description: >-
            Sets the placeholder text on the input element (for types "string",
            "int", "float" and "secret")
        showClickToSet:
          type: boolean
          description: If enabled, render a disabled input element with 'Click to set'
        valid:
          type: array
          items:
            type: object
          description: Valid values for parameter.
        items:
          type: object
          description: Recursive definition for items of a parameter with type 'array'.
        properties:
          type: object
          description: Recursive definition for a parameter with type 'object'.
        minVal:
          type: number
          description: Minimum value for parameters of type 'int' or 'float'.
        maxVal:
          type: number
          description: Maximum value for parameters of type 'int' or 'float'.
    BlockDisplayCategory:
      description: Category to display this block in the UI.
      type: string
      enum:
        - classical
        - tao
        - developer-preview
  securitySchemes:
    ApiKeyAuthentication:
      type: apiKey
      in: header
      name: x-api-key
    JWTAuthentication:
      type: apiKey
      in: cookie
      name: jwt
    JWTHttpHeaderAuthentication:
      type: apiKey
      in: header
      name: x-jwt-token
    OAuth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: /v1/oauth/authorize
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        implicit:
          authorizationUrl: /v1/oauth/authorize
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        password:
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information
        clientCredentials:
          tokenUrl: /v1/oauth/token
          scopes:
            openid: Access to basic profile information
            email: Access to email address
            profile: Access to full profile information

````

Built with [Mintlify](https://mintlify.com).