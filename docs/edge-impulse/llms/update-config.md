# Source: https://docs.edgeimpulse.com/apis/studio/optimization/update-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update config

> Update config



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/optimize/config
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
  /api/{projectId}/optimize/config:
    post:
      tags:
        - Optimization
      summary: Update config
      description: Update config
      operationId: updateConfig
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OptimizeConfig'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenericApiResponse'
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
    TunerSpaceInputBlock:
      type: object
      additionalProperties: true
    TunerSpaceDSPBlock:
      type: object
      additionalProperties: true
    TunerSpaceLearnBlock:
      type: object
      additionalProperties: true
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