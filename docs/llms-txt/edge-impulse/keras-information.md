# Source: https://docs.edgeimpulse.com/apis/studio/learn/keras-information.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Keras information

> Get information about a Keras block, such as its dependencies. Use the impulse blocks to find the learnId.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/training/keras/{learnId}
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
  /api/{projectId}/training/keras/{learnId}:
    get:
      tags:
        - Learn
      summary: Keras information
      description: >-
        Get information about a Keras block, such as its dependencies. Use the
        impulse blocks to find the learnId.
      operationId: getKeras
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/LearnIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/KerasResponse'
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
    KerasResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - $ref: '#/components/schemas/KerasConfig'
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
    KerasConfig:
      type: object
      required:
        - dependencies
        - trained
        - name
        - script
        - minimumConfidenceRating
        - selectedModelType
        - mode
        - trainingCycles
        - learningRate
        - defaultBatchSize
        - visualLayers
        - augmentationPolicyImage
        - transferLearningModels
        - shape
        - profileInt8
        - skipEmbeddingsAndMemory
        - showAdvancedTrainingSettings
        - showAugmentationTrainingSettings
        - thresholds
      properties:
        dependencies:
          $ref: '#/components/schemas/DependencyData'
        trained:
          type: boolean
          description: Whether the block is trained
        name:
          type: string
        type:
          $ref: '#/components/schemas/LearnBlockType'
        script:
          type: string
          description: The Keras script. This script might be empty if the mode is visual.
        minimumConfidenceRating:
          type: number
          description: >-
            DEPRECATED, see "thresholds" instead. Minimum confidence rating
            required for the neural network. Scores below this confidence are
            tagged as uncertain.
        selectedModelType:
          $ref: '#/components/schemas/KerasModelTypeEnum'
          description: The model type that is currently selected.
        mode:
          type: string
          description: The mode (visual or expert) to use for editing this network.
          enum:
            - visual
            - expert
        visualLayers:
          type: array
          description: >-
            The visual layers (if in visual mode) for the neural network. This
            will be an empty array when in expert mode.
          items:
            $ref: '#/components/schemas/KerasVisualLayer'
        trainingCycles:
          type: integer
          description: Number of training cycles. If in expert mode this will be 0.
        learningRate:
          type: number
          description: Learning rate (between 0 and 1). If in expert mode this will be 0.
        batchSize:
          type: integer
          description: The batch size used during training.
        defaultBatchSize:
          type: integer
          description: The default batch size if a value is not configured.
        shape:
          type: string
          description: Python-formatted tuple of input axes
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
        transferLearningModels:
          type: array
          items:
            $ref: '#/components/schemas/TransferLearningModel'
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
            This metadata key is used to prevent group data leakage between
            train and validation datasets.
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
            Capacity level for visual anomaly detection (GMM). Determines which
            set of default configurations to use. The higher capacity, the
            higher number of (Gaussian) components, and the more adapted the
            model becomes to the original distribution
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
        thresholds:
          type: array
          description: List of configurable thresholds for this block.
          items:
            $ref: '#/components/schemas/BlockThreshold'
    DependencyData:
      type: object
      required:
        - classes
        - blockNames
        - featureCount
        - sampleCount
        - outputClasses
      properties:
        classes:
          type: array
          description: Set of all labels present in data feeding into this model
          items:
            type: string
        blockNames:
          type: array
          items:
            type: string
        featureCount:
          type: integer
        sampleCount:
          type: integer
        outputClasses:
          type: array
          description: Set of output classes for this model
          items:
            type: string
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
    BlockThreshold:
      type: object
      description: >-
        Configurable threshold for this block (e.g. minimum score before tagging
        as an anomaly, or the min. score to save bounding boxes)
      required:
        - key
        - description
        - helpText
        - value
      properties:
        key:
          type: string
          description: >-
            Identifier to reference the threshold. You'll need to refer to the
            threshold by this key when you set the threshold).
          example: min_score
        description:
          type: string
          description: User-friendly description of the threshold.
          example: Score threshold
        helpText:
          type: string
          description: Additional help text (shown in the UI under a "?" icon)
          example: >-
            Threshold score for bounding boxes. If the score for a bounding box
            is below this the box will be discarded.
        suggestedValue:
          type: number
          description: >-
            If the threshold has a suggested value, e.g. a max. absolute error
            for regression projects; or the min. anomaly score for visual
            anomaly detection, then this is the numeric value of that threshold.
        suggestedValueText:
          type: string
          description: >-
            If the threshold has a suggested value, e.g. a max. absolute error
            for regression projects; or the min. anomaly score for visual
            anomaly detection, then this is the stringified value of that
            threshold.
        value:
          description: Current value of the threshold
          example: 0.5
          oneOf:
            - type: number
            - type: string
        dropdownOptions:
          description: Optional list of options, will be shown in a dropdown.
          type: array
          items:
            type: object
            required:
              - description
              - value
            properties:
              description:
                type: string
                description: Full description of the value
              value:
                type: string
                description: Value, maps back to "BlockThreshold#value"
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