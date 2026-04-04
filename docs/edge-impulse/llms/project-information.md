# Source: https://docs.edgeimpulse.com/apis/studio/projects/project-information.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Project information

> List all information about this project.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}
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
  /api/{projectId}:
    get:
      tags:
        - Projects
      summary: Project information
      description: List all information about this project.
      operationId: getProjectInfo
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProjectInfoResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    OptionalImpulseIdParameter:
      name: impulseId
      in: query
      required: false
      description: Impulse ID. If this is unset then the default impulse is used.
      schema:
        type: integer
  schemas:
    ProjectInfoResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - project
            - downloads
            - developmentKeys
            - impulse
            - devices
            - dataSummary
            - dataSummaryPerCategory
            - computeTime
            - acquisitionSettings
            - collaborators
            - deploySettings
            - experiments
            - latencyDevices
            - urls
            - showCreateFirstImpulse
            - showGettingStartedWizard
            - performance
            - trainJobNotificationUids
            - dspJobNotificationUids
            - modelTestingJobNotificationUids
            - exportJobNotificationUids
            - hasNewTrainingData
            - studioUrl
            - inPretrainedModelFlow
            - showSensorDataInAcquisitionGraph
            - notifications
          properties:
            project:
              $ref: '#/components/schemas/Project'
            developmentKeys:
              $ref: '#/components/schemas/DevelopmentKeys'
              description: >-
                Only available through JWT token authentication, if you
                authenticate with an API key then all keys will return undefined
                (this is changed behavior since 28 January 2026).
            impulse:
              type: object
              required:
                - created
                - configured
                - complete
              properties:
                created:
                  type: boolean
                  description: Whether an impulse was created
                configured:
                  type: boolean
                  description: Whether an impulse was configured
                complete:
                  type: boolean
                  description: Whether an impulse was fully trained and configured
            devices:
              type: array
              items:
                $ref: '#/components/schemas/Device'
            dataSummary:
              $ref: '#/components/schemas/ProjectDataSummary'
            dataSummaryPerCategory:
              type: object
              required:
                - training
                - testing
                - postProcessing
              properties:
                training:
                  $ref: '#/components/schemas/ProjectDataSummary'
                testing:
                  $ref: '#/components/schemas/ProjectDataSummary'
                postProcessing:
                  $ref: '#/components/schemas/ProjectDataSummary'
            computeTime:
              type: object
              required:
                - periodStartDate
                - periodEndDate
                - timeUsedMs
                - timeLeftMs
              properties:
                periodStartDate:
                  type: string
                  format: date-time
                  description: Start of the current time period.
                periodEndDate:
                  type: string
                  format: date-time
                  description: >-
                    End of the current time period. This is the date when the
                    compute time resets again.
                timeUsedMs:
                  type: integer
                  description: The amount of compute used for the current time period.
                timeLeftMs:
                  type: integer
                  description: The amount of compute left for the current time period.
            acquisitionSettings:
              type: object
              required:
                - intervalMs
                - lengthMs
                - segmentShift
                - defaultPageSize
                - viewType
                - gridColumnCount
                - gridColumnCountDetailed
                - showExactSampleLength
                - inlineEditBoundingBoxes
              properties:
                intervalMs:
                  type: number
                  description: >-
                    Interval during the last acquisition, or the recommended
                    interval based on the data set.
                lengthMs:
                  type: integer
                  description: >-
                    Length of the last acquisition, or a recommended interval
                    based on the data set.
                sensor:
                  type: string
                  description: Sensor that was used during the last acquisition.
                label:
                  type: string
                  description: Label that was used during the last acquisition.
                segmentLength:
                  type: number
                  description: >-
                    Length of the last sample segment after segmenting a larger
                    sample.
                segmentShift:
                  type: boolean
                  description: Whether to auto-shift segments
                defaultPageSize:
                  type: integer
                  description: Default page size on data acquisition
                viewType:
                  type: string
                  description: Default view type on data acquisition
                  enum:
                    - list
                    - grid
                gridColumnCount:
                  type: integer
                  description: Number of grid columns in non-detailed view
                gridColumnCountDetailed:
                  type: integer
                  description: Number of grid columns in detailed view
                showExactSampleLength:
                  type: boolean
                  description: >-
                    If enabled, does not round sample length to
                    hours/minutes/seconds, but always displays sample length in
                    milliseconds. E.g. instead of 1m 32s, this'll say 92,142ms.
                inlineEditBoundingBoxes:
                  type: boolean
                  description: >-
                    If enabled, allows editing bounding box labels directly from
                    the acquisition UI.
            collaborators:
              type: array
              items:
                $ref: '#/components/schemas/User'
            deploySettings:
              type: object
              required:
                - eonCompiler
                - sensor
                - arduinoLibraryName
                - tinkergenLibraryName
                - particleLibraryName
              properties:
                eonCompiler:
                  type: boolean
                sensor:
                  type: string
                  enum:
                    - accelerometer
                    - microphone
                    - camera
                    - positional
                    - environmental
                    - fusion
                    - unknown
                arduinoLibraryName:
                  type: string
                tinkergenLibraryName:
                  type: string
                particleLibraryName:
                  type: string
                lastDeployModelEngine:
                  $ref: '#/components/schemas/ModelEngineShortEnum'
                  type: string
                  description: Model engine for last deploy
            experiments:
              type: array
              description: >-
                Experiments that the project has access to. Enabling experiments
                can only be done through a JWT token.
              items:
                type: object
                required:
                  - type
                  - title
                  - enabled
                  - showToUser
                properties:
                  type:
                    type: string
                  title:
                    type: string
                  help:
                    type: string
                  enabled:
                    type: boolean
                  showToUser:
                    type: boolean
            latencyDevices:
              type: array
              items:
                $ref: '#/components/schemas/LatencyDevice'
            urls:
              type: object
              properties:
                mobileClient:
                  description: >-
                    Base URL for the mobile client. If this is undefined then no
                    development API key is set.
                  type: string
                mobileClientComputer:
                  description: >-
                    Base URL for collecting data with the mobile client from a
                    computer. If this is undefined then no development API key
                    is set.
                  type: string
                mobileClientInference:
                  description: >-
                    Base URL for running inference with the mobile client. If
                    this is undefined then no development API key is set.
                  type: string
            showCreateFirstImpulse:
              type: boolean
            showGettingStartedWizard:
              type: object
              required:
                - showWizard
                - step
              properties:
                showWizard:
                  type: boolean
                step:
                  type: integer
                  description: Current step of the getting started wizard
                tutorial:
                  $ref: '#/components/schemas/TutorialType'
                  description: >-
                    The type of in-product guided tutorial used in the getting
                    started wizard
                classes:
                  type: array
                  description: Classes or labels used in the getting started wizard
                  items:
                    type: string
                  maxItems: 2
            performance:
              type: object
              required:
                - gpu
                - jobLimitM
                - dspFileSizeMb
                - enterprisePerformance
                - trainJobRamMb
              properties:
                gpu:
                  type: boolean
                jobLimitM:
                  type: integer
                  description: >-
                    Compute time limit per job in minutes (applies only to DSP
                    and learning jobs).
                dspFileSizeMb:
                  type: integer
                  description: Maximum size for DSP file output
                enterprisePerformance:
                  type: boolean
                trainJobRamMb:
                  type: integer
                  description: Amount of RAM allocated to training jobs
            readme:
              type: object
              description: Present if a readme is set for this project
              required:
                - markdown
                - html
              properties:
                markdown:
                  type: string
                html:
                  type: string
            trainJobNotificationUids:
              type: array
              description: >-
                The IDs of users who should be notified when a Keras or retrain
                job is finished.
              items:
                type: integer
            dspJobNotificationUids:
              type: array
              description: >-
                The IDs of users who should be notified when a DSP job is
                finished.
              items:
                type: integer
            modelTestingJobNotificationUids:
              type: array
              description: >-
                The IDs of users who should be notified when a model testing job
                is finished.
              items:
                type: integer
            exportJobNotificationUids:
              type: array
              description: >-
                The IDs of users who should be notified when an export job is
                finished.
              items:
                type: integer
            hasNewTrainingData:
              type: boolean
            csvImportConfig:
              type: object
              description: Config file specifying how to process CSV files.
            studioUrl:
              type: string
            inPretrainedModelFlow:
              type: boolean
              description: >-
                DEPRECATED. To enable the pretrained model flow, set the impulse
                type property to "BYOM" instead.
            dspPageSize:
              type: integer
            showSensorDataInAcquisitionGraph:
              description: >-
                Whether to show the actual sensor data in acquisition charts
                (only applies when you have structured labels)
              type: boolean
            targetConstraints:
              $ref: '#/components/schemas/TargetConstraints'
            notifications:
              type: array
              description: List of notifications to show within the project
              items:
                type: string
            defaultImpulseId:
              type: integer
              description: Default selected impulse (by ID).
            lastShownModelEngine:
              $ref: '#/components/schemas/ModelEngineShortEnum'
              description: >-
                Last shown model engine on the Keras/DSP/BYOM/Anomaly screens.
                Used to keep the same view after refreshing.
            versioningStorageSizeMib:
              type: integer
            anomalyLabelsConfig:
              $ref: '#/components/schemas/AnomalyLabelsConfig'
              description: >
                Labels to be treated as anomalous or non-anomalous. Defaults to
                "anomaly" / "no anomaly" if not specified.

                Useful when you want to override these default labels. Only
                relevant when there is an anomaly block in your impulse.
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
    Project:
      type: object
      required:
        - id
        - name
        - description
        - created
        - owner
        - collaborators
        - labelingMethod
        - metadata
        - isEnterpriseProject
        - whitelabelId
        - tier
        - hasPublicVersion
        - isPublic
        - allowsLivePublicAccess
        - ownerIsDeveloperProfile
        - indPauseProcessingSamples
        - publicProjectListed
      properties:
        id:
          type: integer
          example: 1
        name:
          type: string
          example: Water hammer detection
        description:
          type: string
        created:
          type: string
          format: date-time
          example: '2019-07-21T17:32:28Z'
        owner:
          type: string
          description: User or organization that owns the project
        lastAccessed:
          type: string
          format: date-time
          example: '2019-07-21T17:32:28Z'
        lastModified:
          type: string
          format: date-time
          example: '2019-07-21T17:32:28Z'
        lastModificationDetails:
          type: string
          description: Details about the last modification
          example: Data sample added
        logo:
          type: string
          description: Custom logo for this project (not available for all projects)
        ownerUserId:
          type: integer
        ownerOrganizationId:
          type: integer
        ownerAvatar:
          type: string
          description: URL of the project owner avatar, if any.
        ownerIsDeveloperProfile:
          type: boolean
        developerProfileUserId:
          type: integer
          description: User ID of the developer profile, if any.
        collaborators:
          type: array
          items:
            $ref: '#/components/schemas/ProjectCollaborator'
        labelingMethod:
          $ref: '#/components/schemas/ProjectLabelingMethod'
        metadata:
          type: object
          description: Metadata about the project
        dataExplorerScreenshot:
          type: string
        isEnterpriseProject:
          type: boolean
          description: Whether this is an enterprise project
        whitelabelId:
          type: integer
          nullable: true
          description: >-
            Unique identifier of the white label this project belongs to, if
            any.
        whitelabelName:
          type: string
          description: Name of the white label this project belongs to, if any.
        tags:
          type: array
          items:
            type: string
          description: List of project tags
          example:
            - FOMO
            - beers
        category:
          type: string
          description: Project category
          enum:
            - Accelerometer
            - Audio
            - Images
            - Keyword spotting
            - Object detection
            - Other
        license:
          $ref: '#/components/schemas/PublicProjectLicense'
          description: Public project license, if any.
        tier:
          $ref: '#/components/schemas/ProjectTierEnum'
        hasPublicVersion:
          type: boolean
          description: Whether this project has been published or not.
        isPublic:
          type: boolean
          description: >
            Whether this is a public version of a project. A version is a
            snapshot of a project at a certain point in time, which can be used
            to periodically save the state of a project. Versions can be private
            (just for internal use and reference) or public, available to
            everyone. A public version can be cloned by anyone, restoring the
            state of the project at the time into a new, separate project.
        allowsLivePublicAccess:
          type: boolean
          description: >
            Whether this project allows live, public access. Unlike a public
            version, a live public project is not fixed in time, and always
            includes the latest project changes. Similar to public versions, a
            live public project can be cloned by anyone, creating a new,
            separate project.
        indPauseProcessingSamples:
          type: boolean
        publicProjectListed:
          type: boolean
          description: >
            If the project allows public access, whether to list it the public
            projects overview response. If not listed, the project is still
            accessible via direct link. If the project does not allow public
            access, this field has no effect.
        deletedDate:
          type: string
          format: date-time
        fullDeletionDate:
          type: string
          format: date-time
        scheduledFullDeletionDate:
          type: string
          format: date-time
    DevelopmentKeys:
      type: object
      properties:
        apiKey:
          type: string
          description: API Key
        hmacKey:
          type: string
          description: HMAC Key
    Device:
      type: object
      required:
        - id
        - deviceId
        - created
        - lastSeen
        - name
        - deviceType
        - sensors
        - remote_mgmt_connected
        - supportsSnapshotStreaming
        - remoteMgmtMode
      properties:
        id:
          type: integer
          example: 1
        deviceId:
          type: string
          description: Unique identifier (such as MAC address) for a device
          example: 38:f9:d3:d7:62:03
        created:
          type: string
          format: date-time
          example: '2019-07-21T17:32:28Z'
        lastSeen:
          type: string
          format: date-time
          example: '2019-08-31T17:32:28Z'
          description: Last message that was received from the device (ignoring keep-alive)
        name:
          type: string
          example: m6d.1 desk sensor
        deviceType:
          type: string
          example: DISCO-L475VG
        sensors:
          type: array
          items:
            type: object
            required:
              - name
              - maxSampleLengthS
              - frequencies
            properties:
              name:
                type: string
                example: Built-in accelerometer
              maxSampleLengthS:
                type: integer
                description: Maximum supported sample length in seconds
              frequencies:
                type: array
                description: Supported frequencies for this sensor in Hz.
                example:
                  - 62.5
                  - 100
                items:
                  type: number
        remote_mgmt_connected:
          type: boolean
          description: >-
            Whether the device is connected to the remote management interface.
            This property is deprecated, use `remoteMgmtMode` instead.
        remote_mgmt_host:
          type: string
          description: The remote management host that the device is connected to
        supportsSnapshotStreaming:
          type: boolean
        remoteMgmtMode:
          description: >-
            Replaces `remote_mgmt_connected`. Shows whether the device is
            connected to the remote management interface, and in which mode.
          type: string
          enum:
            - disconnected
            - ingestion
            - inference
        inferenceInfo:
          type: object
          description: >-
            If `remoteMgmtMode` is set to `inference` this object shows
            information about the model that's ran on device.
          required:
            - projectId
            - projectOwner
            - projectName
            - deployedVersion
          properties:
            projectId:
              type: integer
            projectOwner:
              type: string
            projectName:
              type: string
            deployedVersion:
              type: integer
            modelType:
              type: string
              enum:
                - classification
                - objectDetection
                - constrainedObjectDetection
    ProjectDataSummary:
      type: object
      required:
        - totalLengthMs
        - labels
        - dataCount
      properties:
        totalLengthMs:
          type: number
          description: Total length (in ms.) of all data in the training set
          example: '726336'
        labels:
          type: array
          description: Labels in the training set
          items:
            type: string
        dataCount:
          type: integer
          example: Number of files in the training set
    User:
      type: object
      required:
        - id
        - username
        - name
        - email
        - created
        - staffInfo
        - pending
        - activated
        - mfaConfigured
      properties:
        id:
          type: integer
          example: 1
        username:
          type: string
          example: janjongboom
        name:
          type: string
          example: Jan Jongboom
        email:
          type: string
          example: quijote@edgeimpulse.com
        photo:
          type: string
          example: https://usercdn.edgeimpulse.com/photos/1.jpg
        created:
          type: string
          format: date-time
          example: '2019-08-31T17:32:28Z'
        lastSeen:
          type: string
          format: date-time
          example: '2019-08-31T17:32:28Z'
        staffInfo:
          $ref: '#/components/schemas/StaffInfo'
        pending:
          type: boolean
        jobTitle:
          type: string
          example: Software Engineer
        permissions:
          description: List of permissions the user has
          type: array
          items:
            $ref: '#/components/schemas/Permission'
        companyName:
          type: string
          example: Edge Impulse Inc.
        activated:
          type: boolean
          description: Whether the user has activated their account or not.
        mfaConfigured:
          type: boolean
          description: Whether the user has configured multi-factor authentication
        stripeCustomerId:
          type: string
          description: Stripe customer ID, if any.
        hasPendingPayments:
          type: boolean
          description: Whether the user has pending payments.
        tier:
          $ref: '#/components/schemas/UserTierEnum'
        idps:
          type: array
          description: >-
            List of identity providers (e.g. Google, GitHub) that the user has
            used to sign in with
          items:
            type: string
    ModelEngineShortEnum:
      type: string
      enum:
        - tflite-eon
        - tflite-eon-ram-optimized
        - tflite
    LatencyDevice:
      type: object
      required:
        - mcu
        - name
        - selected
        - int8Latency
        - int8ConvLatency
        - float32Latency
        - float32ConvLatency
        - helpText
      properties:
        mcu:
          type: string
        name:
          type: string
        selected:
          type: boolean
        int8Latency:
          type: number
        int8ConvLatency:
          type: number
        float32Latency:
          type: number
        float32ConvLatency:
          type: number
        helpText:
          type: string
    TutorialType:
      type: string
      description: >-
        The type of in-product guided tutorial to show in the getting started
        wizard
      enum:
        - kws
        - cv
    TargetConstraints:
      type: object
      required:
        - targetDevices
        - applicationBudgets
      properties:
        selectedTargetBasedOn:
          type: string
          description: >-
            A type explaining how the target was chosen. If updating this
            manually, use the 'user-configured' type
          enum:
            - user-configured
            - default
            - default-accepted
            - recent-project
            - connected-device
        targetDevices:
          type: array
          description: >-
            The potential targets for the project, where each entry captures
            hardware attributes that allow target guidance throughout the Studio
            workflow. The first target in the list is considered as the selected
            target for the project.
          items:
            $ref: '#/components/schemas/TargetConstraintsDevice'
        applicationBudgets:
          type: array
          description: >-
            A list of application budgets to be configured based on target
            device. An application budget enables guidance on performance and
            resource usage. The first application budget in the list is
            considered as the selected budget for the project.
          items:
            $ref: '#/components/schemas/ApplicationBudget'
    AnomalyLabelsConfig:
      type: object
      required:
        - anomalyLabels
        - noAnomalyLabels
      properties:
        anomalyLabels:
          type: array
          description: >-
            Labels to treat as anomalous during classification or model testing
            in Studio, defaults to ['anomaly']
          items:
            type: string
        noAnomalyLabels:
          type: array
          description: >-
            Labels to treat as non-anomalous during classification or model
            testing in Studio, defaults to ['no anomaly']
          items:
            type: string
    ProjectCollaborator:
      allOf:
        - $ref: '#/components/schemas/User'
        - type: object
          required:
            - isOwner
          properties:
            isOwner:
              type: boolean
    ProjectLabelingMethod:
      type: string
      enum:
        - single_label
        - object_detection
        - label_map
    PublicProjectLicense:
      type: string
      enum:
        - Apache-2.0
        - BSD-3-Clause
        - BSD-3-Clause-Clear
    ProjectTierEnum:
      type: string
      description: >-
        The project tier. This is "enterprise" for all organization projects, or
        the user tier for all user projects.
      enum:
        - free
        - community-plus
        - professional
        - enterprise
    StaffInfo:
      type: object
      required:
        - isStaff
        - hasSudoRights
      properties:
        isStaff:
          type: boolean
        hasSudoRights:
          type: boolean
        companyName:
          type: string
    Permission:
      type: string
      enum:
        - admin:infra:disallowedEmailDomains:read
        - admin:infra:disallowedEmailDomains:write
        - admin:infra:featureFlags:read
        - admin:infra:featureFlags:write
        - admin:infra:config:read
        - admin:infra:config:write
        - admin:infra:migrations:read
        - admin:infra:migrations:write
        - admin:metrics:read
        - admin:metrics:write
        - admin:oauth:read
        - admin:oauth:write
        - admin:organizations:read
        - admin:organizations:write
        - admin:organizations:members:write
        - admin:projects:members:write
        - admin:projects:read
        - admin:projects:write
        - admin:trashbin:write
        - admin:trials:read
        - admin:trials:write
        - admin:users:permissions:write
        - admin:users:read
        - admin:users:signupApprovals:read
        - admin:users:signupApprovals:write
        - admin:users:write
        - admin:jobs:read
        - admin:emails:verification:code:read
        - admin:sso:read
        - admin:sso:domainIdps:write
        - admin:vlm:model:read
        - admin:vlm:model:write
        - projects:limits:write
        - projects:training:keras:write
        - projects:data:versioning:write
        - thirdpartyauth:read
        - thirdpartyauth:write
        - users:emails:read
        - whitelabels:read
        - whitelabels:write
        - test:data:write
    UserTierEnum:
      type: string
      description: The user account tier.
      enum:
        - free
        - community-plus
        - professional
        - enterprise
    TargetConstraintsDevice:
      type: object
      properties:
        processors:
          type: array
          description: Target processors
          items:
            $ref: '#/components/schemas/TargetProcessor'
        board:
          type: string
          description: The exact dev board part number, if available
        name:
          type: string
          description: Display name in Studio
        latencyDevice:
          type: string
          description: MCU identifier, if available
          example: cortex-m4f-80mhz
    ApplicationBudget:
      type: object
      description: >-
        Specifies limits for your specific application, as available RAM and ROM
        for the model's operation and the maximum allowed latency.
      properties:
        latencyPerInferenceMs:
          $ref: '#/components/schemas/ResourceRange'
        energyPerInferenceJoules:
          $ref: '#/components/schemas/ResourceRange'
        memoryOverhead:
          $ref: '#/components/schemas/TargetMemory'
    TargetProcessor:
      type: object
      properties:
        part:
          type: string
          description: The exact part number, if available
        format:
          type: string
          description: >-
            Processor type, serving as a broad descriptor for the intended
            use-case
          example: low-end MCU
        architecture:
          type: string
          description: >-
            Processor family, informing about the processor's instruction set
            and core design
          example: Cortex-M
        specificArchitecture:
          type: string
          description: >-
            Processor architecture, informing about the specific processor, if
            known
          example: Cortex-M0+
        accelerator:
          type: string
          description: Target accelerator, if any
          example: Arm Cortex-U55
        fpu:
          type: boolean
          description: Does the target processor have a floating point unit
        clockRateMhz:
          $ref: '#/components/schemas/ResourceRange'
          description: Clock rate of the processor
        memory:
          $ref: '#/components/schemas/TargetMemory'
    ResourceRange:
      type: object
      description: Describes range of expected availability for an arbitrary resource
      properties:
        minimum:
          type: number
        maximum:
          type: number
    TargetMemory:
      type: object
      description: RAM and ROM specifications of target
      properties:
        ram:
          $ref: '#/components/schemas/MemorySpec'
        rom:
          $ref: '#/components/schemas/MemorySpec'
    MemorySpec:
      type: object
      description: Describes performance characteristics of a particular memory type
      properties:
        fastBytes:
          $ref: '#/components/schemas/ResourceRange'
        slowBytes:
          $ref: '#/components/schemas/ResourceRange'
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