# Source: https://docs.edgeimpulse.com/apis/studio/jobs/train-model-keras.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Train model (Keras)

> Take the output from a DSP block and train a neural network using Keras. Updates are streamed over the websocket API.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/jobs/train/keras/{learnId}
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
  /api/{projectId}/jobs/train/keras/{learnId}:
    post:
      tags:
        - Jobs
      summary: Train model (Keras)
      description: >-
        Take the output from a DSP block and train a neural network using Keras.
        Updates are streamed over the websocket API.
      operationId: trainKerasJob
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/LearnIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SetKerasParameterRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StartJobResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    LearnIdParameter:
      name: learnId
      in: path
      required: true
      description: Learn Block ID, use the impulse functions to retrieve the ID
      schema:
        type: integer
  schemas:
    SetKerasParameterRequest:
      type: object
      description: Only fields defined in this object are set
      properties:
        mode:
          type: string
          description: Whether to use visual or expert mode.
          enum:
            - expert
            - visual
        minimumConfidenceRating:
          type: number
          description: >-
            DEPRECATED, use "setImpulseThresholds" instead. Minimum confidence
            score, if the neural network scores a sample below this threshold it
            will be flagged as uncertain.
        selectedModelType:
          $ref: '#/components/schemas/KerasModelTypeEnum'
          description: The model type to select, as described in the model metadata call.
        script:
          type: string
          description: Raw Keras script (only used in expert mode)
        visualLayers:
          type: array
          description: The visual layers for the neural network (only in visual mode).
          items:
            $ref: '#/components/schemas/KerasVisualLayer'
        trainingCycles:
          type: integer
          description: Number of training cycles (only in visual mode).
        learningRate:
          type: number
          description: Learning rate (between 0 and 1) (only in visual mode).
        batchSize:
          type: number
          description: Batch size used during training (only in visual mode).
        trainTestSplit:
          type: number
          description: Train/test split (between 0 and 1)
        autoClassWeights:
          type: boolean
          description: >-
            Whether to automatically balance class weights, use this for skewed
            datasets.
        useLearnedOptimizer:
          type: boolean
          description: Use learned optimizer and ignore learning rate.
        augmentationPolicyImage:
          $ref: '#/components/schemas/AugmentationPolicyImageEnum'
        augmentationPolicySpectrogram:
          $ref: '#/components/schemas/AugmentationPolicySpectrogram'
        profileInt8:
          type: boolean
          description: Whether to profile the i8 model (might take a very long time)
        skipEmbeddingsAndMemory:
          type: boolean
          description: >-
            If set, skips creating embeddings and measuring memory (used in
            tests)
        akidaEdgeLearningConfig:
          $ref: '#/components/schemas/AkidaEdgeLearningConfig'
        customValidationMetadataKey:
          type: string
          description: >-
            If the 'custom validation split' experiment is enabled, this
            metadata key is used to prevent group data leakage between train and
            validation datasets.
        showAdvancedTrainingSettings:
          type: boolean
          description: >-
            Whether the 'Advanced training settings' UI element should be
            expanded.
        showAugmentationTrainingSettings:
          type: boolean
          description: >-
            Whether the 'Augmentation training settings' UI element should be
            expanded.
        customParameters:
          type: object
          description: >-
            Training parameters, this list depends on the list of parameters
            that the model exposes.
          additionalProperties:
            type: string
            nullable: true
        anomalyCapacity:
          $ref: '#/components/schemas/AnomalyCapacity'
          description: >-
            Capacity level for visual anomaly detection. Determines which set of
            default configurations to use. The higher capacity, the higher
            number of (Gaussian) components, and the more adapted the model
            becomes to the original distribution
        lastShownModelVariant:
          $ref: '#/components/schemas/KerasModelVariantEnum'
          description: >-
            Last shown variant on the Keras screen. Used to keep the same view
            after refreshing.
        blockParameters:
          $ref: '#/components/schemas/BlockParameters'
          description: >-
            Training parameters specific to the type of the learn block.
            Parameters may be adjusted depending on the model defined in the
            visual layers. Used for our built-in blocks.
    StartJobResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - id
          properties:
            id:
              type: integer
              description: Job identifier. Status updates will include this identifier.
              example: 12873488112
    KerasModelTypeEnum:
      type: string
      enum:
        - int8
        - float32
        - akida
        - requiresRetrain
    KerasVisualLayer:
      type: object
      required:
        - type
      properties:
        type:
          $ref: '#/components/schemas/KerasVisualLayerType'
        neurons:
          type: integer
          description: >-
            Number of neurons or filters in this layer (only for dense, conv1d,
            conv2d) or in the final conv2d layer (only for transfer layers)
        kernelSize:
          type: integer
          description: Kernel size for the convolutional layers (only for conv1d, conv2d)
        dropoutRate:
          type: number
          description: >-
            Fraction of input units to drop (only for dropout) or in the final
            layer dropout (only for transfer layers)
        columns:
          type: integer
          description: Number of columns for the reshape operation (only for reshape)
        stack:
          type: integer
          description: >-
            Number of convolutional layers before the pooling layer (only for
            conv1d, conv2d)
        enabled:
          type: boolean
        organizationModelId:
          type: integer
          description: >-
            Custom transfer learning model ID (when type is set to
            transfer_organization)
    AugmentationPolicyImageEnum:
      type: string
      description: The data augmentation policy to use with image input
      enum:
        - none
        - all
    AugmentationPolicySpectrogram:
      type: object
      required:
        - enabled
      properties:
        enabled:
          type: boolean
          description: >-
            True if spectrogram augmentation is enabled. Other properties will
            be ignored if this is false.
        warping:
          type: boolean
          description: True if warping along the time axis is enabled.
        freqMasking:
          type: string
          enum:
            - none
            - low
            - high
          description: The amount of frequency masking to apply.
        timeMasking:
          type: string
          enum:
            - none
            - low
            - high
          description: The amount of time masking to apply.
        gaussianNoise:
          type: string
          enum:
            - none
            - low
            - high
          description: The amount of Gaussian noise to add.
    AkidaEdgeLearningConfig:
      type: object
      required:
        - enabled
      properties:
        enabled:
          type: boolean
          description: >-
            True if Akida Edge Learning model creation is enabled. Other
            properties will be ignored if this is false.
        additionalClasses:
          type: number
          description: >-
            Number of additional classes that will be added to the Edge Learning
            model.
        neuronsPerClass:
          type: number
          description: >-
            Number of neurons in each class on the last layer in the Edge
            Learning model.
    AnomalyCapacity:
      type: string
      description: >-
        Capacity level for visual anomaly detection. Determines which set of
        default configurations to use. The higher capacity, the higher number of
        (Gaussian) components, and the more adapted the model becomes to the
        original distribution
      enum:
        - low
        - medium
        - high
    KerasModelVariantEnum:
      type: string
      enum:
        - int8
        - float32
        - akida
    BlockParameters:
      description: >-
        Training parameters specific to the type of the learn block. Parameters
        may be adjusted depending on the model defined in the visual layers.
        Used for our built-in blocks.
      oneOf:
        - $ref: '#/components/schemas/BlockParamsVisualAnomalyPatchcore'
        - $ref: '#/components/schemas/BlockParamsVisualAnomalyGmm'
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
    BlockParamsVisualAnomalyPatchcore:
      type: object
      properties:
        backbone:
          type: string
          description: The backbone to use for feature extraction
        numLayers:
          type: integer
          description: The number of layers in the feature extractor (1-3)
        poolSize:
          type: integer
          description: The pool size for the feature extractor
        samplingRatio:
          type: number
          description: The sampling ratio for the coreset, used for anomaly scoring
        numNearestNeighbors:
          type: integer
          description: >-
            The number of nearest neighbors to consider, used for anomaly
            scoring
    BlockParamsVisualAnomalyGmm:
      type: object
      properties:
        backbone:
          type: string
          description: The backbone to use for feature extraction
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