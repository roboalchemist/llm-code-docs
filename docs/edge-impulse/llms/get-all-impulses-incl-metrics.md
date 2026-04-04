# Source: https://docs.edgeimpulse.com/apis/studio/impulse/get-all-impulses-incl-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all impulses (incl. metrics)

> Retrieve all impulse for a project, including accuracy and performance metrics.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/impulses-detailed
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
  /api/{projectId}/impulses-detailed:
    get:
      tags:
        - Impulse
      summary: Get all impulses (incl. metrics)
      description: >-
        Retrieve all impulse for a project, including accuracy and performance
        metrics.
      operationId: getAllDetailedImpulses
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetAllDetailedImpulsesResponse'
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
    GetAllDetailedImpulsesResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - impulses
            - metricKeysByCategory
            - extraTableColumns
          properties:
            impulses:
              type: array
              items:
                $ref: '#/components/schemas/DetailedImpulse'
            metricKeysByCategory:
              type: array
              items:
                type: object
                required:
                  - category
                  - metricKeys
                properties:
                  category:
                    $ref: '#/components/schemas/DetailedImpulseMetricCategory'
                  metricKeys:
                    type: array
                    items:
                      type: object
                      required:
                        - name
                        - description
                        - type
                        - showInTable
                      properties:
                        name:
                          type: string
                        description:
                          type: string
                        type:
                          type: string
                          enum:
                            - core
                            - additional
                        filteringType:
                          $ref: >-
                            #/components/schemas/DetailedImpulseMetricFilteringType
                        showInTable:
                          type: boolean
            extraTableColumns:
              type: array
              description: >-
                Which extra impulse information should be shown in the impulses
                table.
              items:
                type: string
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
    DetailedImpulse:
      type: object
      required:
        - impulse
        - metrics
        - dspBlockConfigs
        - learnBlockKerasConfigs
        - learnBlockAnomalyConfigs
        - postProcessingBlockConfigs
        - configured
        - complete
        - isStale
        - tags
      properties:
        impulse:
          $ref: '#/components/schemas/Impulse'
        metrics:
          type: array
          items:
            $ref: '#/components/schemas/DetailedImpulseMetric'
        dspBlockConfigs:
          type: array
          items:
            type: object
            required:
              - blockId
              - config
            properties:
              blockId:
                type: integer
              config:
                $ref: '#/components/schemas/DSPConfig'
                description: >-
                  This returns a DSPConfig object, but "dsp.classes" and
                  "dsp.features.classes" will be set to an empty array (use
                  getDspConfig to retrieve these).
              metadata:
                $ref: '#/components/schemas/DSPMetadata'
                description: >-
                  This returns a DSPMetadata object, but "labels" will be set to
                  an empty array (use getDspMetadata to retrieve these).
        learnBlockKerasConfigs:
          items:
            type: object
            required:
              - blockId
              - config
            properties:
              blockId:
                type: integer
              config:
                $ref: '#/components/schemas/KerasConfig'
                description: >-
                  This returns a KerasConfig object, but
                  "transferLearningModels" and "dependencies.classes" will be
                  set to an empty array (use getKeras to retrieve these).
              metadata:
                $ref: '#/components/schemas/KerasModelMetadata'
                description: >-
                  This returns a KerasModelMetadata object, but 1) non-default
                  "onDevicePerformance", 2) "predictions", 3) "labels"; are
                  omitted (use getKerasMetadata to retrieve these).
        learnBlockAnomalyConfigs:
          items:
            type: object
            required:
              - blockId
              - config
            properties:
              blockId:
                type: integer
              config:
                $ref: '#/components/schemas/AnomalyConfig'
              metadata:
                $ref: '#/components/schemas/AnomalyModelMetadata'
                description: >-
                  This returns a AnomalyModelMetadata object, but 1) non-default
                  "onDevicePerformance", 2) "predictions" are omitted (use
                  getAnomalyMetadata to retrieve these).
              gmmMetadata:
                $ref: '#/components/schemas/AnomalyGmmMetadata'
        postProcessingBlockConfigs:
          items:
            type: object
            required:
              - blockId
              - config
            properties:
              blockId:
                type: integer
              config:
                $ref: '#/components/schemas/PostProcessingConfig'
        pretrainedModelInfo:
          type: object
          required:
            - fileName
          properties:
            fileName:
              type: string
        isStale:
          type: boolean
          description: >-
            Whether this impulse contains blocks with "stale" features (i.e. the
            dataset has changed since features were generated)
        configured:
          type: boolean
          description: Whether this impulse is configured
        complete:
          type: boolean
          description: Whether this impulse is fully trained and configured
        tags:
          type: array
          items:
            type: string
          description: Tags associated with this impulse
        createdFromTunerTrialId:
          type: number
          description: >-
            The source EON Tuner trial ID for impulses created from the EON
            Tuner
        createdByUser:
          $ref: '#/components/schemas/CreatedUpdatedByUser'
          description: The user who originally created this impulse.
    DetailedImpulseMetricCategory:
      type: string
      enum:
        - impulseMetrics
        - inputBlockConfig
        - dspBlockConfig
        - learnBlockConfig
        - learnBlockMetrics
        - postProcessingBlockConfig
    DetailedImpulseMetricFilteringType:
      type: object
      required:
        - type
        - options
      properties:
        type:
          type: string
          enum:
            - numeric
            - string
            - select
            - boolean
            - list
        options:
          type: array
          items:
            type: string
    Impulse:
      type: object
      required:
        - id
        - name
        - inputBlocks
        - dspBlocks
        - learnBlocks
        - postProcessingBlocks
        - type
      properties:
        id:
          type: integer
          description: ID for this impulse.
        name:
          type: string
          description: Name for this impulse.
        inputBlocks:
          type: array
          description: Input Blocks that are part of this impulse
          items:
            $ref: '#/components/schemas/ImpulseInputBlock'
        dspBlocks:
          type: array
          description: DSP Blocks that are part of this impulse
          items:
            $ref: '#/components/schemas/ImpulseDspBlock'
        learnBlocks:
          type: array
          description: Learning Blocks that are part of this impulse
          items:
            $ref: '#/components/schemas/ImpulseLearnBlock'
        postProcessingBlocks:
          type: array
          description: Post-processing blocks that are part of this impulse
          items:
            $ref: '#/components/schemas/ImpulsePostProcessingBlock'
        type:
          $ref: '#/components/schemas/ImpulseType'
    DetailedImpulseMetric:
      type: object
      required:
        - name
        - type
        - category
        - description
        - value
      properties:
        name:
          type: string
        type:
          type: string
          enum:
            - core
            - additional
        filteringType:
          $ref: '#/components/schemas/DetailedImpulseMetricFilteringType'
        category:
          $ref: '#/components/schemas/DetailedImpulseMetricCategory'
        description:
          type: string
        value:
          oneOf:
            - type: string
            - type: boolean
        title:
          type: string
        valueForSorting:
          type: integer
        valueHint:
          type: string
          description: Additional help explaining the value for this metric
    DSPConfig:
      type: object
      required:
        - dsp
      properties:
        dsp:
          $ref: '#/components/schemas/DSPInfo'
        config:
          type: array
          items:
            $ref: '#/components/schemas/DSPGroup'
        configError:
          type: string
    DSPMetadata:
      type: object
      required:
        - created
        - generated
        - dspConfig
        - labels
        - featureCount
        - windowCount
        - includedSamples
        - windowSizeMs
        - windowIncreaseMs
        - padZeros
        - frequency
        - outputConfig
      properties:
        created:
          type: string
          format: date-time
          description: Date when the features were created
        generated:
          type: boolean
          description: Whether features were generated
        dspConfig:
          type: object
          additionalProperties:
            type: string
        labels:
          type: array
          description: Labels in the dataset when generator ran
          items:
            type: string
        featureLabels:
          type: array
          description: >-
            Names of the generated features. Only set if axes have explicit
            labels.
          items:
            type: string
        windowCount:
          type: integer
        featureCount:
          type: integer
          description: Number of features for this DSP block
        includedSamples:
          type: array
          description: >-
            The included samples in this DSP block. Note that these are sorted
            in the same way as the `npy` files are laid out. So with the
            `windowCount` parameter you can exactly search back to see which
            file contributed to which windows there.
          items:
            type: object
            required:
              - id
              - windowCount
            properties:
              id:
                type: integer
              windowCount:
                type: integer
        windowSizeMs:
          type: integer
          description: Length of the sliding window when generating features.
        windowIncreaseMs:
          type: integer
          description: Increase of the sliding window when generating features.
        padZeros:
          type: boolean
          description: Whether data was zero-padded when generating features.
        frequency:
          type: number
          description: Frequency of the original data in Hz.
        outputConfig:
          type: object
          description: Information about the output of the DSP block
          required:
            - type
            - shape
          properties:
            type:
              type: string
              description: Output type of the DSP block
              enum:
                - image
                - spectrogram
                - flat
            shape:
              type: object
              description: The shape of the block output
              required:
                - width
              properties:
                width:
                  description: >-
                    Available on all types. Denotes the width of an 'image' or
                    'spectrogram', or the number of features in a 'flat' block.
                  type: integer
                height:
                  description: Only available for type 'image' and 'spectrogram'
                  type: integer
                channels:
                  description: Only available for type 'image'
                  type: integer
                frames:
                  description: Number of frames, only available for type 'image'
                  type: integer
        fftUsed:
          type: array
          items:
            type: integer
        resamplingAlgorithmVersion:
          type: number
          description: >-
            The version number of the resampling algorithm used (for resampled
            time series data only)
        featureExplorerJobId:
          type: integer
          description: >-
            When specified, a job is running (asynchronously) to generate the
            feature explorer.
        featureExplorerJobFailed:
          description: >-
            If this is set, then the feature explorer job failed (get the status
            by getting the job logs for 'featureExplorerJobId').
          type: boolean
        featureImportanceJobId:
          type: integer
          description: >-
            When specified, a job is running (asynchronously) to generate
            feature importance.
        featureImportanceJobFailed:
          description: >-
            If this is set, then the feature importance job failed (get the
            status by getting the job logs for 'featureImportanceJobId').
          type: boolean
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
    KerasModelMetadata:
      type: object
      required:
        - created
        - layers
        - classNames
        - availableModelTypes
        - recommendedModelType
        - modelValidationMetrics
        - hasTrainedModel
        - mode
        - imageInputScaling
        - labels
        - thresholds
      properties:
        created:
          type: string
          format: date-time
          description: Date when the model was trained
        layers:
          type: array
          description: Layers of the neural network
          items:
            $ref: '#/components/schemas/KerasModelLayer'
        classNames:
          type: array
          description: Labels for the output layer
          items:
            type: string
        labels:
          type: array
          description: >-
            Original labels in the dataset when features were generated, e.g.
            used to render the feature explorer.
          items:
            type: string
        availableModelTypes:
          type: array
          description: The types of model that are available
          items:
            $ref: '#/components/schemas/KerasModelTypeEnum'
        recommendedModelType:
          $ref: '#/components/schemas/KerasModelTypeEnum'
          description: The model type that is recommended for use
        modelValidationMetrics:
          type: array
          description: Metrics for each of the available model types
          items:
            $ref: '#/components/schemas/KerasModelMetadataMetrics'
        hasTrainedModel:
          type: boolean
        mode:
          $ref: '#/components/schemas/KerasModelMode'
        objectDetectionLastLayer:
          $ref: '#/components/schemas/ObjectDetectionLastLayer'
        imageInputScaling:
          $ref: '#/components/schemas/ImageInputScaling'
        thresholds:
          type: array
          description: List of configurable thresholds for this block.
          items:
            $ref: '#/components/schemas/BlockThreshold'
        tensorboardGraphs:
          $ref: '#/components/schemas/TensorboardGraphs'
          description: List of TensorBoard graphs associated with this model
    AnomalyConfig:
      type: object
      required:
        - name
        - axes
        - trained
        - dependencies
        - selectedAxes
        - minimumConfidenceRating
        - thresholds
      properties:
        dependencies:
          $ref: '#/components/schemas/DependencyData'
        name:
          type: string
        axes:
          type: array
          description: Selectable axes for the anomaly detection block
          items:
            type: object
            required:
              - ix
              - label
              - selected
              - favourite
            properties:
              ix:
                type: integer
              label:
                type: string
              selected:
                type: boolean
              favourite:
                type: boolean
        trained:
          type: boolean
          description: Whether the block is trained
        clusterCount:
          type: integer
          description: >-
            Number of clusters for K-means, or number of components for GMM (in
            config)
        selectedAxes:
          type: array
          items:
            type: integer
          description: Selected clusters (in config)
        minimumConfidenceRating:
          type: number
          description: >-
            DEPRECATED, see "thresholds" instead. Minimum confidence rating for
            this block, scores above this number will be flagged as anomaly.
        thresholds:
          type: array
          description: List of configurable thresholds for this block.
          items:
            $ref: '#/components/schemas/BlockThreshold'
    AnomalyModelMetadata:
      type: object
      required:
        - created
        - scale
        - mean
        - clusters
        - axes
        - defaultMinimumConfidenceRating
        - thresholds
      properties:
        created:
          type: string
          format: date-time
          description: Date when the model was trained
        scale:
          type: array
          description: >-
            Scale input for StandardScaler. Values are scaled like this (where
            `ix` is axis index): `input[ix] = (input[ix] - mean[ix]) /
            scale[ix];`
          items:
            type: number
        mean:
          type: array
          description: >-
            Mean input for StandardScaler. Values are scaled like this (where
            `ix` is axis index): `input[ix] = (input[ix] - mean[ix]) /
            scale[ix];`
          items:
            type: number
        clusters:
          type: array
          description: Trained K-means clusters
          items:
            type: object
            required:
              - center
              - maxError
            properties:
              center:
                type: array
                description: Center of each cluster (one value per axis)
                items:
                  type: number
              maxError:
                type: number
                description: Size of the cluster
        axes:
          type: array
          description: Which axes were included during training (by index)
          example: '`[ 0, 11, 22 ]`'
          items:
            type: integer
        defaultMinimumConfidenceRating:
          type: number
          description: >-
            DEPRECATED, see "thresholds" instead. Default minimum confidence
            rating required before tagging as anomaly, based on scores of
            training data (GMM only).
        availableModelTypes:
          type: array
          description: The types of model that are available
          items:
            $ref: '#/components/schemas/KerasModelTypeEnum'
        recommendedModelType:
          $ref: '#/components/schemas/KerasModelTypeEnum'
          description: The model type that is recommended for use
        modelValidationMetrics:
          type: array
          description: Metrics for each of the available model types
          items:
            $ref: '#/components/schemas/KerasModelMetadataMetrics'
        hasTrainedModel:
          type: boolean
        thresholds:
          type: array
          description: List of configurable thresholds for this block.
          items:
            $ref: '#/components/schemas/BlockThreshold'
    AnomalyGmmMetadata:
      type: object
      required:
        - means
        - covariances
        - weights
      properties:
        means:
          type: array
          items:
            type: array
            items:
              type: number
          description: 2D array of shape (n, m)
        covariances:
          type: array
          items:
            type: array
            items:
              type: array
              items:
                type: number
          description: 3D array of shape (n, m, m)
        weights:
          type: array
          items:
            type: number
          description: 1D array of shape (n,)
    PostProcessingConfig:
      type: object
      required:
        - enabled
        - parameters
      properties:
        enabled:
          type: boolean
        parameters:
          type: array
          items:
            $ref: '#/components/schemas/DSPGroupItem'
    CreatedUpdatedByUser:
      type: object
      required:
        - id
        - name
        - username
      properties:
        id:
          type: integer
        name:
          type: string
        username:
          type: string
        photo:
          type: string
    ImpulseInputBlock:
      type: object
      required:
        - id
        - type
        - name
        - title
      properties:
        id:
          type: integer
          minimum: 1
          description: >-
            Identifier for this block. Make sure to up this number when creating
            a new block via `getNewBlockId`, and don't re-use identifiers. If
            the block hasn't changed, keep the ID as-is. ID must be unique
            across the project and greather than zero (>0).
        type:
          type: string
          description: Block type (either time-series, image or features)
          example: time-series
          enum:
            - time-series
            - image
            - features
        name:
          type: string
          description: Block name, will be used in menus
          example: Time series
        title:
          type: string
          description: Block title, used in the impulse UI
          example: Time series
        windowSizeMs:
          type: integer
          description: Size of the sliding window in milliseconds
          example: 2004
        windowIncreaseMs:
          type: integer
          description: >-
            We use a sliding window to go over the raw data. How many
            milliseconds to increase the sliding window with for each step.
        frequencyHz:
          type: number
          description: (Input only) Frequency of the input data in Hz
          example: 60
        classificationWindowIncreaseMs:
          type: integer
          description: >-
            We use a sliding window to go over the raw data. How many
            milliseconds to increase the sliding window with for each step in
            classification mode.
        padZeros:
          type: boolean
          description: Whether to zero pad data when a data item is too short
        labelingMethodMultiLabel:
          type: object
          description: How to pick the label for multi-label samples
          required:
            - type
          properties:
            type:
              type: string
              enum:
                - end-of-window
                - anywhere-in-window
            labels:
              description: >-
                Required when choosing "anywhere-in-window". The list of classes
                that should trigger detection (e.g. "interference").
              type: array
              items:
                type: string
        imageWidth:
          type: integer
          description: Width all images are resized to before training
          example: 28
        imageHeight:
          type: integer
          description: Width all images are resized to before training
          example: 28
        resizeMode:
          $ref: '#/components/schemas/ImageInputResizeMode'
        resizeMethod:
          type: string
          description: Resize method to use when resizing images
          example: squash
          enum:
            - lanczos3
            - nearest
        cropAnchor:
          type: string
          description: If images are resized using a crop, choose where to anchor the crop
          example: middle-center
          enum:
            - top-left
            - top-center
            - top-right
            - middle-left
            - middle-center
            - middle-right
            - bottom-left
            - bottom-center
            - bottom-right
        createdBy:
          type: string
          description: >-
            The system component that created the block version (createImpulse |
            clone | tuner). Cannot be set via API.
          example: createImpulse
        createdAt:
          type: string
          format: date-time
          description: >-
            The datetime that the block version was created. Cannot be set via
            API.
        datasetSubset:
          $ref: '#/components/schemas/ImpulseInputBlockDatasetSubset'
    ImpulseDspBlock:
      type: object
      required:
        - id
        - type
        - name
        - axes
        - title
        - implementationVersion
      properties:
        id:
          type: integer
          minimum: 1
          description: >-
            Identifier for this block. Make sure to up this number when creating
            a new block via `getNewBlockId`, and don't re-use identifiers. If
            the block hasn't changed, keep the ID as-is. ID must be unique
            across the project and greather than zero (>0).
        type:
          type: string
          description: Block type
          example: spectral-analysis
        name:
          type: string
          description: Block name, will be used in menus
          example: Spectral features
        axes:
          type: array
          description: Input axes, identified by the name in the name of the axis
          items:
            type: string
            example: accX
        title:
          type: string
          description: Block title, used in the impulse UI
          example: Spectral Analysis
        valuesPerAxis:
          type: integer
          description: >-
            Number of features this DSP block outputs per axis. This is only set
            when the DSP block is configured.
          example: 11
        input:
          type: integer
          description: The ID of the Input block a DSP block is connected to
          example: 1
        createdBy:
          type: string
          description: >-
            The system component that created the block version (createImpulse |
            clone | tuner). Cannot be set via API.
          example: createImpulse
        createdAt:
          type: string
          format: date-time
          description: >-
            The datetime that the block version was created. Cannot be set via
            API.
        implementationVersion:
          type: integer
          description: Implementation version of the block
        organization:
          type: object
          required:
            - id
            - dspId
          properties:
            id:
              type: integer
            dspId:
              type: integer
        customUrl:
          type: string
          description: Required for type 'custom'
        namedAxes:
          type: array
          description: Named axes for the block
          items:
            type: object
            required:
              - name
            properties:
              name:
                type: string
                description: Name of the axis
              description:
                type: string
                description: Description of the axis
              required:
                type: boolean
                description: Whether the axis is required
              selectedAxis:
                type: string
                description: The selected axis for the block
    ImpulseLearnBlock:
      type: object
      required:
        - id
        - type
        - name
        - dsp
        - title
      properties:
        id:
          type: integer
          minimum: 1
          description: >-
            Identifier for this block. Make sure to up this number when creating
            a new block via `getNewBlockId`, and don't re-use identifiers. If
            the block hasn't changed, keep the ID as-is. ID must be unique
            across the project and greather than zero (>0).
        type:
          $ref: '#/components/schemas/LearnBlockType'
        name:
          type: string
          description: >-
            Block name, will be used in menus. If a block has a baseBlockId,
            this field is ignored and the base block's name is used instead.
          example: NN Classifier
        dsp:
          type: array
          description: DSP dependencies, identified by DSP block ID
          items:
            type: integer
            example: 27
        title:
          type: string
          description: Block title, used in the impulse UI
          example: Classification (Keras)
        createdBy:
          type: string
          description: >-
            The system component that created the block version (createImpulse |
            clone | tuner). Cannot be set via API.
          example: createImpulse
        createdAt:
          type: string
          format: date-time
          description: >-
            The datetime that the block version was created. Cannot be set via
            API.
    ImpulsePostProcessingBlock:
      type: object
      required:
        - id
        - type
        - name
        - title
        - implementationVersion
      properties:
        id:
          type: integer
          minimum: 1
          description: >-
            Identifier for this block. Make sure to up this number when creating
            a new block via `getNewBlockId`, and don't re-use identifiers. If
            the block hasn't changed, keep the ID as-is. ID must be unique
            across the project and greather than zero (>0).
        type:
          type: string
          description: Block type
          example: object-tracking
        name:
          type: string
          description: Block name, will be used in menus
          example: Object tracking
        title:
          type: string
          description: Block title, used in the impulse UI
          example: Object tracking
        createdBy:
          type: string
          description: >-
            The system component that created the block version (createImpulse |
            clone | tuner). Cannot be set via API.
          example: createImpulse
        createdAt:
          type: string
          format: date-time
          description: >-
            The datetime that the block version was created. Cannot be set via
            API.
        implementationVersion:
          type: integer
          description: Implementation version of the block
    ImpulseType:
      type: string
      description: >
        Specifies the type of impulse. Options include: - default: Standard Edge
        Impulse pipeline. - BYOM: Impulse that includes a pretrained model. -
        VLM: Impulse created as part of a Vision Learning Model (VLM) workflow.
      enum:
        - default
        - BYOM
        - VLM
    DSPInfo:
      type: object
      required:
        - id
        - name
        - windowLength
        - type
        - classes
        - features
        - expectedWindowCount
        - inputAxes
        - canCalculateFeatureImportance
        - calculateFeatureImportance
        - canNormalizeData
        - normalizeData
      properties:
        id:
          type: integer
          example: 1
        name:
          type: string
          example: Spectral features
        windowLength:
          type: integer
          example: 3000
        type:
          type: string
          example: spectral-analysis
        classes:
          type: array
          items:
            type: string
        features:
          type: object
          required:
            - generated
          properties:
            generated:
              type: boolean
              description: Whether this block has generated features
            count:
              type: integer
              description: Number of generated features
            labels:
              type: array
              description: Names of the features
              items:
                type: string
            classes:
              type: array
              description: Classes that the features were generated on
              items:
                type: string
        expectedWindowCount:
          type: integer
          description: Expected number of windows that would be generated
        inputAxes:
          type: array
          description: Axes that this block depends on.
          items:
            type: string
        performance:
          $ref: '#/components/schemas/DspPerformance'
        canCalculateFeatureImportance:
          type: boolean
        calculateFeatureImportance:
          type: boolean
        canNormalizeData:
          type: boolean
          description: >-
            Whether this DSP block supports data normalization after features
            were generated. This is true unless "dontAllowDataNormalization" is
            set to true in the DSP block's parameters.json.
        normalizeData:
          $ref: '#/components/schemas/DSPNormalizeData'
          description: Data normalization that was last selected for this block.
        hasAutoTune:
          description: Whether this type of DSP block supports autotuning.
          type: boolean
        minimumVersionForAutotune:
          description: >-
            For DSP blocks that support autotuning, this value specifies the
            minimum block implementation version for which autotuning is
            supported.
          type: number
        hasAutotunerResults:
          description: Whether autotune results exist for this DSP block.
          type: boolean
        usesState:
          description: Whether this DSP block uses state.
          type: boolean
    DSPGroup:
      type: object
      required:
        - group
        - items
      properties:
        group:
          type: string
          example: Scaling
        items:
          type: array
          items:
            $ref: '#/components/schemas/DSPGroupItem'
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
    KerasModelLayer:
      type: object
      required:
        - input
        - output
      properties:
        input:
          type: object
          required:
            - shape
            - name
            - type
          properties:
            shape:
              type: integer
              description: Input size
              example: 33
            name:
              type: string
              description: TensorFlow name
              example: x_input:0
            type:
              type: string
              description: TensorFlow type
              example: '<dtype: ''float32''>'
        output:
          type: object
          required:
            - shape
            - name
            - type
          properties:
            shape:
              type: integer
              description: Output size
              example: 20
            name:
              type: string
              description: TensorFlow name
              example: dense_1/Relu:0
            type:
              type: string
              description: TensorFlow type
              example: '<dtype: ''float32''>'
    KerasModelMetadataMetrics:
      type: object
      required:
        - type
        - loss
        - confusionMatrix
        - report
        - onDevicePerformance
        - visualization
        - isSupportedOnMcu
        - additionalMetrics
      properties:
        type:
          $ref: '#/components/schemas/KerasModelTypeEnum'
          description: The type of model
        loss:
          type: number
          description: The model's loss on the validation set after training
        accuracy:
          type: number
          description: The model's accuracy on the validation set after training
        confusionMatrix:
          type: array
          example:
            - - 31
              - 1
              - 0
            - - 2
              - 27
              - 3
            - - 1
              - 0
              - 39
          items:
            type: array
            items:
              type: number
        report:
          type: object
          description: Precision, recall, F1 and support scores
        onDevicePerformance:
          type: array
          items:
            type: object
            required:
              - mcu
              - name
              - isDefault
              - latency
              - tflite
              - eon
              - hasPerformance
            properties:
              mcu:
                type: string
              name:
                type: string
              isDefault:
                type: boolean
              latency:
                type: number
              tflite:
                type: object
                required:
                  - ramRequired
                  - romRequired
                  - arenaSize
                  - modelSize
                properties:
                  ramRequired:
                    type: integer
                  romRequired:
                    type: integer
                  arenaSize:
                    type: integer
                  modelSize:
                    type: integer
              eon:
                type: object
                required:
                  - ramRequired
                  - romRequired
                  - arenaSize
                  - modelSize
                properties:
                  ramRequired:
                    type: integer
                  romRequired:
                    type: integer
                  arenaSize:
                    type: integer
                  modelSize:
                    type: integer
              eon_ram_optimized:
                type: object
                required:
                  - ramRequired
                  - romRequired
                  - arenaSize
                  - modelSize
                properties:
                  ramRequired:
                    type: integer
                  romRequired:
                    type: integer
                  arenaSize:
                    type: integer
                  modelSize:
                    type: integer
              customMetrics:
                description: Custom, device-specific performance metrics
                type: array
                items:
                  $ref: '#/components/schemas/KerasCustomMetric'
              hasPerformance:
                description: If false, then no metrics are available for this target
                type: boolean
              profilingError:
                description: Specific error during profiling (e.g. model not supported)
                type: string
        predictions:
          type: array
          items:
            $ref: '#/components/schemas/ModelPrediction'
        visualization:
          type: string
          enum:
            - featureExplorer
            - dataExplorer
            - none
        isSupportedOnMcu:
          type: boolean
        mcuSupportError:
          type: string
        profilingJobId:
          description: >-
            If this is set, then we're still profiling this model. Subscribe to
            job updates to see when it's done (afterward the metadata will be
            updated).
          type: integer
        profilingJobFailed:
          description: >-
            If this is set, then the profiling job failed (get the status by
            getting the job logs for 'profilingJobId').
          type: boolean
        additionalMetrics:
          type: array
          items:
            $ref: '#/components/schemas/AdditionalMetric'
    KerasModelMode:
      type: string
      enum:
        - classification
        - regression
        - object-detection
        - visual-anomaly
        - anomaly-gmm
        - freeform
        - anomaly
    ObjectDetectionLastLayer:
      type: string
      enum:
        - mobilenet-ssd
        - fomo
        - yolov2-akida
        - yolov5
        - yolov5v5-drpai
        - yolox
        - yolov7
        - yolo-pro
        - tao-retinanet
        - tao-ssd
        - tao-yolov3
        - tao-yolov4
        - yolov11
        - yolov11-abs
        - paddleocr-detector
        - qc-face-det-lite
    ImageInputScaling:
      description: >-
        Normalization that is applied to images. If this is not set then 0..1 is
        used. "0..1" gives you non-normalized pixels between 0 and 1. "-1..1"
        gives you non-normalized pixels between -1 and 1. "0..255" gives you
        non-normalized pixels between 0 and 255. "-128..127" gives you
        non-normalized pixels between -128 and 127. "torch" first scales pixels
        between 0 and 1, then applies normalization using the ImageNet dataset
        (same as `torchvision.transforms.Normalize()`).
        "bgr-subtract-imagenet-mean" scales to 0..255, reorders pixels to BGR,
        and subtracts the ImageNet mean from each channel.
      type: string
      enum:
        - 0..1
        - '-1..1'
        - '-128..127'
        - 0..255
        - torch
        - bgr-subtract-imagenet-mean
    TensorboardGraphs:
      type: array
      items:
        $ref: '#/components/schemas/KerasModelMetadataGraph'
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
    ImageInputResizeMode:
      type: string
      description: >
        Input images are resized automatically before training and testing, to
        match the impulse input shape.

        This determines the resize mode used when the aspect ratio of the input
        data is different to the aspect ratio of the impulse.
      example: squash
      enum:
        - squash
        - fit-short
        - fit-long
        - crop
    ImpulseInputBlockDatasetSubset:
      type: object
      description: >-
        Only generate features for samples where (sample_id + datasetSubsetSeed)
        % datasetSubset) == 0
      required:
        - includePercentage
      properties:
        includePercentage:
          description: >-
            Number between 0 and 100, with the % of data that should be
            _included_
          type: number
        seed:
          description: Seed number (optional). If not specified, the seed is set to 0.
          type: integer
    DspPerformance:
      type: object
      required:
        - latency
        - ram
      properties:
        latency:
          type: integer
        ram:
          type: integer
        customDspString:
          type: string
          description: >-
            If the project latencyDevice has custom DSP hardware, this value
            contains a device specific latency metric (eg. cycles)
    DSPNormalizeData:
      type: string
      enum:
        - none
        - normalize-channel-standard-scaler
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
    KerasCustomMetric:
      type: object
      required:
        - name
        - value
      properties:
        name:
          description: The name of the metric
          type: string
        value:
          description: The value of this metric for this model type
          type: string
    ModelPrediction:
      type: object
      required:
        - sampleId
        - startMs
        - endMs
        - prediction
      properties:
        sampleId:
          type: integer
        startMs:
          type: number
        endMs:
          type: number
        label:
          type: string
        prediction:
          type: string
        predictionCorrect:
          type: boolean
        f1Score:
          type: number
          description: Only set for object detection projects
        anomalyScores:
          type: array
          description: >-
            Only set for visual anomaly projects. 2D array of shape (n, n) with
            raw anomaly scores, where n varies based on the image input size and
            the specific visual anomaly algorithm used. The scores corresponds
            to each grid cell in the image's spatial matrix.
          items:
            type: array
            items:
              type: number
        boundingBoxes:
          type: array
          description: >-
            Only set for object detection projects. Coordinates are scaled 0..1,
            not absolute values.
          items:
            $ref: '#/components/schemas/BoundingBoxWithScore'
        labelMapPredictions:
          type: object
          description: >-
            For samples with structured labels (in the form of a key/value label
            map), this object will contain per-key prediction info for the
            sample.
          additionalProperties:
            type: string
    AdditionalMetric:
      type: object
      required:
        - name
        - value
        - fullPrecisionValue
      properties:
        name:
          type: string
        value:
          type: string
        fullPrecisionValue:
          type: number
        tooltipText:
          type: string
        link:
          type: string
    KerasModelMetadataGraph:
      type: object
      required:
        - title
        - data
      properties:
        title:
          description: Graph title
          type: string
        xLabel:
          description: X-axis title
          type: string
        yLabel:
          description: Y-axis title
          type: string
        description:
          description: A description for the graph
          type: string
        hideInUI:
          description: Whether this graph should be hidden by default in the Studio UI
          type: boolean
        data:
          type: array
          items:
            $ref: '#/components/schemas/KerasModelMetadataGraphSeries'
    BoundingBoxWithScore:
      type: object
      description: This has the _ratio_ for x/y/w/h (so 0..1)
      required:
        - label
        - x
        - 'y'
        - width
        - height
        - score
      properties:
        label:
          type: string
        x:
          type: number
        'y':
          type: number
        width:
          type: number
        height:
          type: number
        score:
          type: number
    KerasModelMetadataGraphSeries:
      type: object
      required:
        - title
        - values
      properties:
        title:
          type: string
        values:
          type: array
          items:
            type: number
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