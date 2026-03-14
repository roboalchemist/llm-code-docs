# Source: https://docs.edgeimpulse.com/apis/studio/optimization/retrieves-the-eon-tuner-state.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieves the EON tuner state

> Retrieves the EON tuner state



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/optimize/state
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
  /api/{projectId}/optimize/state:
    get:
      tags:
        - Optimization
      summary: Retrieves the EON tuner state
      description: Retrieves the EON tuner state
      operationId: getState
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      responses:
        '200':
          description: Current EON tuner state
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OptimizeStateResponse'
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
    OptimizeStateResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - config
            - status
            - trials
            - workers
            - projectDataType
            - tunerJobIsRunning
            - nextRunIndex
            - canExtendSearch
            - isWhitelabel
            - totalTrainingTimeExceeded
          properties:
            config:
              $ref: '#/components/schemas/OptimizeConfig'
            status:
              type: object
              required:
                - numPendingTrials
                - numRunningTrials
                - numCompletedTrials
                - numFailedTrials
                - numReadyWorkers
                - numBusyWorkers
                - numPendingWorkers
                - status
              properties:
                numPendingTrials:
                  type: integer
                numRunningTrials:
                  type: integer
                numCompletedTrials:
                  type: integer
                numFailedTrials:
                  type: integer
                numReadyWorkers:
                  type: integer
                numBusyWorkers:
                  type: integer
                numPendingWorkers:
                  type: integer
                status:
                  type: string
                  enum:
                    - creating
                    - ready
                    - running
                    - completed
            tunerJobId:
              description: >-
                Actual tuner process, job message events will be tagged with
                this ID
              type: integer
            tunerCoordinatorJobId:
              description: >-
                The coordinator pod, attach the job runner to this process for
                finished events
              type: integer
            continuationJobId:
              description: >-
                Job ID for the initial job this job continuous the
                hyperparameter search process for.
              type: integer
            tuningAlgorithm:
              type: string
              description: Tuning algorithm to use to search hyperparameter space
              enum:
                - random
                - hyperband
                - bayesian
                - custom
            tunerJobIsRunning:
              description: Whether the job is active (if false => finished)
              type: boolean
            trials:
              type: array
              items:
                $ref: '#/components/schemas/TunerTrial'
            projectDataType:
              type: string
              enum:
                - audio
                - image
                - motion
                - other
            jobError:
              type: string
            workers:
              type: array
              items:
                type: object
                required:
                  - workerId
                  - status
                properties:
                  workerId:
                    type: string
                  status:
                    type: string
                    enum:
                      - pending
                      - ready
                      - busy
            nextRunIndex:
              type: integer
              description: >-
                Index of the next run to be created. Used to pre-populate the
                name of the next run.
            canExtendSearch:
              type: boolean
              description: >-
                Whether the search can be extended to evaluate more candidate
                models. Extending is possible if the search space contains
                candidate models that are expected to perform better than the
                current best candidate. And extending is also possible if the
                previous run was paused due to the total runtime limit being
                exceeded.
            isWhitelabel:
              type: boolean
            totalTrainingTimeExceeded:
              type: boolean
              description: >-
                Whether the total training time has exceeded the defined limit
                for the current run.
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
    OptimizeConfig:
      type: object
      required:
        - targetDevice
        - targetLatency
      properties:
        name:
          type: string
        targetLatency:
          type: integer
          description: Target latency in MS
          example: 0
        targetDevice:
          type: object
          required:
            - name
          description: Target device
          properties:
            name:
              type: string
              example: cortex-m4f-80mhz
            ram:
              type: integer
              example: 1024
            rom:
              type: integer
              example: 1024
        compiler:
          type: array
          items:
            type: string
        precision:
          type: array
          items:
            type: string
        trainingCycles:
          type: integer
          description: Maximum number of training cycles
          example: 5
        tuningMaxTrials:
          type: integer
          description: Maximum number of trials
          example: 2
        tuningWorkers:
          type: integer
          description: Maximum number of parallel workers/jobs
          example: 1
        initialTrials:
          type: integer
          description: Number of initial trials
          example: 5
        optimizationRounds:
          type: integer
          description: Number of optimization rounds
          example: 3
        trialsPerOptimizationRound:
          type: integer
          description: Number of trials per optimization round
          example: 3
        minMACCS:
          type: number
        maxMACCS:
          type: number
        tuningAlgorithm:
          type: string
          description: Tuning algorithm to use to search hyperparameter space
          enum:
            - random
            - hyperband
            - bayesian
            - custom
        notificationOnCompletion:
          type: boolean
        importProjectMetrics:
          type: boolean
          description: >-
            Whether to import metrics for previous EON tuner runs in the same
            project to accelerate the hyperparameter search process
        importResourceMetrics:
          type: boolean
          description: >-
            Whether to import resource usage (RAM/ROM/latency) metrics to
            accelerate the hyperparameter search process
        numImportProjectMetrics:
          type: number
          description: Number of project trials to import
        numImportResourceMetrics:
          type: number
          description: Number of resource usage trials to import
        enableSEM:
          type: boolean
          description: Enable standard error of the mean (SEM)
        accuracySEM:
          type: number
          description: Standard error of the trial accuracy mean
        latencySEM:
          type: number
          description: Standard error of the trial latency mean
        optimizationObjectives:
          type: array
          description: Hyperparameter optimization objectives and corresponding weights
          items:
            type: object
            required:
              - objective
              - label
              - weight
            properties:
              objective:
                type: string
                description: Objective to optimize
              label:
                type: string
                description: Label of the objective
              weight:
                type: number
                description: Weight of the objective
        rawObjectives:
          type: string
          description: Hyperparameter optimization objectives + weights in string format
        optimizationPrecision:
          type: string
          description: Model variant to optimize for
          enum:
            - float32
            - int8
        earlyStopping:
          type: boolean
          description: >-
            Enable trial level early stopping based on loss metrics during
            training
        earlyStoppingWindowSize:
          type: number
          description: >-
            Stops the EON tuner if the feasible (mean) objective has not
            improved over the past “window_size” iterations
        earlyStoppingImprovementBar:
          type: number
          description: >-
            Threshold (in [0,1]) for considering relative improvement over the
            best point.
        MOMF:
          type: boolean
          description: Enable Multi-fidelity Multi-Objective optimization
        verboseLogging:
          type: boolean
          description: Enable verbose logging
        disableConstraints:
          type: boolean
          description: Disable search constraints
        disableDeduplicate:
          type: boolean
          description: Disable trial deduplication
        maxTotalTrainingTime:
          type: number
          description: Maximum total training time in seconds
        tunerSpaceOptions:
          type: object
          additionalProperties:
            type: array
            items:
              type: string
        space:
          type: array
          description: List of impulses specifying the EON Tuner search space
          items:
            $ref: '#/components/schemas/TunerSpaceImpulse'
        searchSpaceTemplate:
          type: object
          description: Search space template
          required:
            - identifier
          properties:
            identifier:
              type: string
              description: Search space template identifier
              enum:
                - speech_keyword
                - speech_continuous
                - audio_event
                - audio_continuous
                - visual
                - motion_event
                - motion_continuous
                - audio_syntiant
                - object_detection_bounding_boxes
                - object_detection_centroids
                - visual_ad
                - object_detection_yolo_pro
            classification:
              type: boolean
              description: >-
                Whether a classification block should be added to the search
                space
            anomaly:
              type: boolean
              description: Whether an anomaly block should be added to the search space
            regression:
              type: boolean
              description: Whether a regression block should be added to the search space
        searchSpaceSource:
          type: object
          description: Search space source
          required:
            - type
          properties:
            type:
              type: string
              description: Search space source type
              enum:
                - template
                - run
                - impulse
                - custom
            templateTitle:
              type: string
              description: Search space source template title
            runTitle:
              type: string
              description: Search space source run title
            impulseTitle:
              type: string
              description: Search space source impulse title
    TunerTrial:
      type: object
      required:
        - id
        - name
        - status
        - blocks
        - impulse
      properties:
        id:
          type: string
        name:
          type: string
        status:
          type: string
          enum:
            - pending
            - running
            - completed
            - failed
        lastCompletedEpoch:
          type: string
          format: date-time
        lastCompletedTraining:
          type: string
          format: date-time
        retries:
          type: integer
        currentEpoch:
          type: integer
        workerId:
          type: string
        blocks:
          type: array
          items:
            type: object
            required:
              - id
              - type
              - retries
              - status
              - blockId
            properties:
              id:
                type: integer
              lastActive:
                type: string
                format: date-time
              retries:
                type: integer
              status:
                type: string
                enum:
                  - pending
                  - running
                  - completed
                  - failed
              type:
                type: string
                enum:
                  - input
                  - dsp
                  - learn
              modelBlockIndex:
                type: integer
                description: >-
                  Index of corresponding DSP/learn block in the impulse model
                  passed to createTrial()
        impulse:
          $ref: '#/components/schemas/TunerTrialImpulse'
        experiment:
          type: string
        original_trial_id:
          type: string
        model:
          type: object
          additionalProperties: true
        dspJobId:
          type: object
          properties:
            training:
              type: number
            testing:
              type: number
        learnJobId:
          type: number
        devicePerformance:
          type: object
          additionalProperties: true
        optimizationRound:
          type: number
        progress:
          type: object
          required:
            - epoch
            - loss
            - val_loss
            - accuracy
            - val_accuracy
          properties:
            epoch:
              type: number
            loss:
              type: number
            val_loss:
              type: number
            accuracy:
              type: number
            val_accuracy:
              type: number
        metrics:
          type: object
          properties:
            test:
              type: object
              properties:
                float32:
                  $ref: '#/components/schemas/KerasModelMetadataMetrics'
                int8:
                  $ref: '#/components/schemas/KerasModelMetadataMetrics'
            train:
              type: object
              properties:
                float32:
                  $ref: '#/components/schemas/KerasModelMetadataMetrics'
                int8:
                  $ref: '#/components/schemas/KerasModelMetadataMetrics'
            validation:
              type: object
              properties:
                float32:
                  $ref: '#/components/schemas/KerasModelMetadataMetrics'
                int8:
                  $ref: '#/components/schemas/KerasModelMetadataMetrics'
        impulseAddedToProject:
          type: object
          required:
            - impulseId
            - link
          properties:
            impulseId:
              type: integer
            link:
              type: string
        createdInPostProcessing:
          type: boolean
    TunerSpaceImpulse:
      type: object
      required:
        - inputBlocks
        - dspBlocks
        - learnBlocks
      properties:
        parameters:
          type: object
          description: >-
            Hyperparameters with potential values that can be used in any block
            in this impulse
        inputBlocks:
          type: array
          description: Input Blocks that are part of this impulse
          items:
            $ref: '#/components/schemas/TunerSpaceInputBlock'
        dspBlocks:
          type: array
          description: DSP Blocks that are part of this impulse
          items:
            $ref: '#/components/schemas/TunerSpaceDSPBlock'
        learnBlocks:
          type: array
          description: Learning Blocks that are part of this impulse
          items:
            type: array
            items:
              $ref: '#/components/schemas/TunerSpaceLearnBlock'
    TunerTrialImpulse:
      type: object
      required:
        - inputBlock
        - dspBlock
        - learnBlock
      properties:
        inputBlocks:
          type: array
          items:
            $ref: '#/components/schemas/TunerCreateTrialInputBlock'
        dspBlocks:
          type: array
          items:
            $ref: '#/components/schemas/TunerCreateTrialDSPBlock'
        learnBlocks:
          type: array
          items:
            $ref: '#/components/schemas/TunerCreateTrialLearnBlock'
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
    TunerSpaceInputBlock:
      type: object
      additionalProperties: true
    TunerSpaceDSPBlock:
      type: object
      additionalProperties: true
    TunerSpaceLearnBlock:
      type: object
      additionalProperties: true
    TunerCreateTrialInputBlock:
      type: object
      additionalProperties: true
    TunerCreateTrialDSPBlock:
      type: object
      additionalProperties: true
    TunerCreateTrialLearnBlock:
      type: object
      additionalProperties: true
    KerasModelTypeEnum:
      type: string
      enum:
        - int8
        - float32
        - akida
        - requiresRetrain
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