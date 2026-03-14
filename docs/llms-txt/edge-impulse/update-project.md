# Source: https://docs.edgeimpulse.com/apis/studio/projects/update-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update project

> Update project properties such as name and logo.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}
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
    post:
      tags:
        - Projects
      summary: Update project
      description: Update project properties such as name and logo.
      operationId: updateProject
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateProjectRequest'
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
    UpdateProjectRequest:
      type: object
      description: Only fields set in this object will be updated.
      properties:
        logo:
          type: string
          description: New logo URL, or set to `null` to remove the logo.
        name:
          type: string
          description: New project name.
        description:
          type: string
        projectVisibility:
          $ref: '#/components/schemas/ProjectVisibility'
        publicProjectListed:
          type: boolean
          description: >
            If the project allows public access, whether to list it the public
            projects overview response. If not listed, the project is still
            accessible via direct link. If the project does not allow public
            access, this field has no effect.
        lastDeployEonCompiler:
          type: boolean
          description: Call this when clicking the Eon compiler setting
        lastDeployModelEngine:
          $ref: '#/components/schemas/ModelEngineShortEnum'
          type: string
          description: Model engine for last deploy
        latencyDevice:
          type: string
          description: MCU used for calculating latency
        experiments:
          type: array
          items:
            type: string
        showCreateFirstImpulse:
          type: boolean
          description: >-
            Whether to show the 'Create your first impulse' section on the
            dashboard
        labelingMethod:
          $ref: '#/components/schemas/ProjectLabelingMethod'
          description: What labeling flow to use
        selectedProjectTypeInWizard:
          type: string
          description: Which option was selected in the project type wizard
          enum:
            - accelerometer
            - audio
            - image_classification
            - object_detection
            - something_else
        gettingStartedStep:
          type: integer
          description: >-
            The next step in the getting started wizard, or set to -1 to clear
            the getting started wizard
        gettingStartedTutorial:
          $ref: '#/components/schemas/TutorialType'
          description: >-
            The type of in-product guided tutorial for the getting started
            wizard
        gettingStartedClasses:
          type: array
          description: Classes or labels used in the getting started wizard
          items:
            type: string
        useGpu:
          type: boolean
          description: Whether to use GPU for training
        computeTimeLimitM:
          type: integer
          description: Job limit in minutes
        dspFileSizeMb:
          type: integer
          description: DSP file size in MB
        enterprisePerformance:
          type: boolean
        trainJobRamMb:
          type: integer
          description: Amount of RAM allocated to training jobs
        metadata:
          type: object
          description: New metadata about the project
        readme:
          type: string
          description: Readme for the project (in Markdown)
        lastAcquisitionLabel:
          type: string
        trainJobNotificationUids:
          type: array
          description: >-
            The IDs of users who should be notified when a Keras or retrain job
            is finished.
          items:
            type: integer
        dspJobNotificationUids:
          type: array
          description: The IDs of users who should be notified when a DSP job is finished.
          items:
            type: integer
        modelTestingJobNotificationUids:
          type: array
          description: >-
            The IDs of users who should be notified when a model testing job is
            finished.
          items:
            type: integer
        exportJobNotificationUids:
          type: array
          description: >-
            The IDs of users who should be notified when an export job is
            finished.
          items:
            type: integer
        csvImportConfig:
          type: object
          description: >-
            Config file specifying how to process CSV files. (set to null to
            clear the config)
        inPretrainedModelFlow:
          type: boolean
          description: >-
            DEPRECATED. To enable the pretrained model flow, set the impulse
            type property to "BYOM" instead.
        dspPageSize:
          description: Set to '0' to disable DSP paging
          type: integer
        indPauseProcessingSamples:
          description: >-
            Used in tests, to ensure samples that need to be processed async are
            not picked up until the flag is set to FALSE again.
          type: boolean
        showSensorDataInAcquisitionGraph:
          description: >-
            Whether to show the actual sensor data in acquisition charts (only
            applies when you have structured labels)
          type: boolean
        lastDeploymentTarget:
          description: >-
            Which deployment target was last selected (used to populate this
            deployment target again the next time you visit the deployment
            page). Should match the _format_ property of the response from
            listDeploymentTargetsForProject.
          type: string
        dataAcquisitionPageSize:
          type: integer
          description: Default page size on data acquisition
        dataAcquisitionViewType:
          type: string
          description: Default view type on data acquisition
          enum:
            - list
            - grid
        dataAcquisitionGridColumnCount:
          type: integer
          description: Number of grid columns in non-detailed view on data acquisition
        dataAcquisitionGridColumnCountDetailed:
          type: integer
          description: Number of grid columns in detailed view on data acquisition
        showExactSampleLength:
          type: boolean
          description: >-
            If enabled, does not round sample length to hours/minutes/seconds,
            but always displays sample length in milliseconds. E.g. instead of
            1m 32s, this'll say 92,142ms.
        inlineEditBoundingBoxes:
          type: boolean
          description: >-
            If enabled, allows editing bounding box labels directly from the
            acquisition UI.
        defaultProfilingVariant:
          $ref: '#/components/schemas/KerasModelVariantEnum'
          description: >-
            Last shown variant on the model testing and live classification
            pages. Used to keep the same view after refreshing.
        enabledModelProfilingVariants:
          type: array
          description: >-
            Set of model variants enabled by default on the model testing and
            live classification pages.
          items:
            $ref: '#/components/schemas/KerasModelVariantEnum'
        impulseListCoreMetricsHiddenColumns:
          type: array
          description: >-
            Which core metrics should be hidden in the impulse list. See
            'GetAllDetailedImpulsesResponse' for a list of all metrics.
          items:
            type: string
        impulseListAdditionalMetricsShownColumns:
          type: array
          description: >-
            Which additional metrics should be shown in the impulse list. See
            'GetAllDetailedImpulsesResponse' for a list of all metrics.
          items:
            type: string
        impulseListExtraColumns:
          type: array
          description: Which extra columns should be shown in the impulse list.
          items:
            type: string
        aiActionsGridColumnCount:
          type: integer
          description: Number of grid columns in AI Actions
        lastShownModelEngine:
          $ref: '#/components/schemas/ModelEngineShortEnum'
          description: >-
            Last shown model engine on the Keras/DSP/BYOM/Anomaly screens. Used
            to keep the same view after refreshing.
        versioningStorageSizeMib:
          type: integer
        anomalyLabelsConfig:
          $ref: '#/components/schemas/AnomalyLabelsConfig'
          description: >
            Labels to be treated as anomalous or non-anomalous. Defaults to
            "anomaly" / "no anomaly" if not specified.

            Useful when you want to override these default labels. Only relevant
            when there is an anomaly block in your impulse.
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
    ProjectVisibility:
      type: string
      enum:
        - public
        - private
      description: >-
        The visibility of the project, either public or private. Public projects
        can be viewed by anyone on the internet and edited by collaborators.
        Private projects can only be viewed and edited by collaborators.
    ModelEngineShortEnum:
      type: string
      enum:
        - tflite-eon
        - tflite-eon-ram-optimized
        - tflite
    ProjectLabelingMethod:
      type: string
      enum:
        - single_label
        - object_detection
        - label_map
    TutorialType:
      type: string
      description: >-
        The type of in-product guided tutorial to show in the getting started
        wizard
      enum:
        - kws
        - cv
    KerasModelVariantEnum:
      type: string
      enum:
        - int8
        - float32
        - akida
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