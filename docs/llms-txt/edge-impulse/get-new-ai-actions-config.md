# Source: https://docs.edgeimpulse.com/apis/studio/projects/get-new-ai-actions-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get new AI Actions config

> Get the AI Actions config for a new action



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/ai-actions/new
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
  /api/{projectId}/ai-actions/new:
    get:
      tags:
        - Projects
      summary: Get new AI Actions config
      description: Get the AI Actions config for a new action
      operationId: getNewAIAction
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetAIActionResponse'
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
    GetAIActionResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - action
          properties:
            action:
              $ref: '#/components/schemas/AIAction'
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
    AIAction:
      type: object
      required:
        - id
        - displayName
        - config
        - previewConfig
        - maxDataPreviewCount
        - gridColumnCount
        - setMetadataAfterRunning
        - cacheUnchangedSteps
      properties:
        id:
          type: integer
        name:
          type: string
          description: Manually set name (optional)
        displayName:
          type: string
          description: >-
            Name to show to the user when interacting with this action (e.g. in
            a table, or when running the action). Will return either "name" (if
            present), or a name derived from the transformation block.
        config:
          $ref: '#/components/schemas/AIActionsConfig'
        previewConfig:
          $ref: '#/components/schemas/AIActionsConfig'
        maxDataPreviewCount:
          description: >-
            When rendering preview items, the max amount of items to show (pass
            this into the previewAIActionsSamples)
          type: integer
        gridColumnCount:
          description: Number of grid columns to use during preview.
          type: integer
        lastPreviewState:
          type: object
          description: >-
            Contains the last preview state, this is filled with whatever was
            ran last, so when you refresh an AI Action it'll always have the
            exact same state as before refresh.
          required:
            - samples
            - proposedChanges
          properties:
            samples:
              type: array
              items:
                $ref: '#/components/schemas/Sample'
            proposedChanges:
              type: array
              items:
                type: object
                required:
                  - sampleId
                  - step
                  - proposedChanges
                properties:
                  sampleId:
                    type: integer
                  step:
                    type: integer
                  proposedChanges:
                    $ref: '#/components/schemas/SampleProposedChanges'
        setMetadataAfterRunning:
          type: array
          description: >-
            After the action runs, add this key/value pair as metadata on the
            affected samples.
          items:
            type: object
            required:
              - key
              - value
            properties:
              key:
                type: string
              value:
                type: string
        cacheUnchangedSteps:
          description: >-
            If enabled, will load cached results from the previous preview job
            for unchanged jobs. Disable this if you're developing your own
            custom AI Labeling job, and want to always re-run all steps.
          type: boolean
    AIActionsConfig:
      type: object
      required:
        - dataCategory
        - steps
      properties:
        dataCategory:
          $ref: '#/components/schemas/AIActionsDataCategory'
          description: Type of data to run this AI action on.
        dataMetadataKey:
          description: >-
            Metadata key to filter on. Required if dataCategory is equal to
            "dataWithoutMetadataKey" or "dataWithMetadata".
          type: string
        dataMetadataValue:
          description: >-
            Metadata value to filter on. Required if dataCategory is equal to
            "dataWithMetadata".
          type: string
        steps:
          type: array
          items:
            $ref: '#/components/schemas/AIActionsConfigStep'
    Sample:
      type: object
      required:
        - id
        - filename
        - signatureValidate
        - created
        - lastModified
        - category
        - coldstorageFilename
        - label
        - intervalMs
        - frequency
        - originalIntervalMs
        - originalFrequency
        - deviceType
        - sensors
        - valuesCount
        - added
        - boundingBoxes
        - boundingBoxesType
        - chartType
        - isDisabled
        - isProcessing
        - processingError
        - isCropped
        - projectId
        - sha256Hash
      properties:
        id:
          type: integer
          example: 2
        filename:
          type: string
          example: idle01.d8Ae
        signatureValidate:
          type: boolean
          description: Whether signature validation passed
          example: true
        signatureMethod:
          type: string
          example: HS256
        signatureKey:
          type: string
          description: >-
            Either the shared key or the public key that was used to validate
            the sample
        created:
          type: string
          format: date-time
          description: >-
            Timestamp when the sample was created on device, or if no accurate
            time was known on device, the time that the file was processed by
            the ingestion service.
        lastModified:
          type: string
          format: date-time
          description: Timestamp when the sample was last modified.
        category:
          $ref: '#/components/schemas/RawDataCategory'
          example: training
        coldstorageFilename:
          type: string
        label:
          type: string
          example: healthy-machine
        intervalMs:
          type: number
          description: >-
            Interval between two windows (1000 / frequency). If the data was
            resampled, then this lists the resampled interval.
          example: 16
        frequency:
          type: number
          description: >-
            Frequency of the sample. If the data was resampled, then this lists
            the resampled frequency.
          example: 62.5
        originalIntervalMs:
          type: number
          description: >-
            Interval between two windows (1000 / frequency) in the source data
            (before resampling).
          example: 16
        originalFrequency:
          type: number
          description: Frequency of the sample in the source data (before resampling).
          example: 62.5
        deviceName:
          type: string
        deviceType:
          type: string
        sensors:
          type: array
          items:
            $ref: '#/components/schemas/Sensor'
        valuesCount:
          type: integer
          description: Number of readings in this file
        totalLengthMs:
          type: number
          description: Total length (in ms.) of this file
        added:
          type: string
          format: date-time
          description: >-
            Timestamp when the sample was added to the current acquisition
            bucket.
        boundingBoxes:
          type: array
          items:
            $ref: '#/components/schemas/BoundingBox'
        boundingBoxesType:
          type: string
          enum:
            - object_detection
            - constrained_object_detection
        chartType:
          type: string
          enum:
            - chart
            - image
            - video
            - table
        thumbnailVideo:
          type: string
        thumbnailVideoFull:
          type: string
        isDisabled:
          type: boolean
          description: True if the current sample is excluded from use
        isProcessing:
          type: boolean
          description: True if the current sample is still processing (e.g. for video)
        processingJobId:
          type: integer
          description: Set when sample is processing and a job has picked up the request
        processingError:
          type: boolean
          description: Set when processing this sample failed
        processingErrorString:
          type: string
          description: Error (only set when processing this sample failed)
        isCropped:
          type: boolean
          description: >-
            Whether the sample is cropped from another sample (and has crop
            start / end info)
        metadata:
          type: object
          description: Sample free form associated metadata
          additionalProperties:
            type: string
        projectId:
          type: integer
          description: Unique identifier of the project this sample belongs to
        projectOwnerName:
          type: string
          description: Name of the owner of the project this sample belongs to
        projectName:
          type: string
          description: Name of the project this sample belongs to
        projectLabelingMethod:
          $ref: '#/components/schemas/ProjectLabelingMethod'
          description: What labeling flow the project this sample belongs to uses
        sha256Hash:
          type: string
          description: Data sample SHA 256 hash (including CBOR envelope if applicable)
        structuredLabels:
          type: array
          items:
            $ref: '#/components/schemas/StructuredLabel'
        structuredLabelsList:
          type: array
          items:
            type: string
        createdBySyntheticDataJobId:
          type: integer
          description: >-
            If this sample was created by a synthetic data job, it's referenced
            here.
        imageDimensions:
          type: object
          required:
            - width
            - height
          properties:
            width:
              type: integer
            height:
              type: integer
        videoUrl:
          type: string
          description: Video link, cropped and in original resolution.
        videoUrlFull:
          type: string
          description: Video link in original resolution.
        labelMap:
          $ref: '#/components/schemas/SampleLabelMapLabels'
    SampleProposedChanges:
      type: object
      properties:
        label:
          type: string
          description: New label (single-label)
        isDisabled:
          type: boolean
          description: >-
            True if the current sample should be disabled; or false if it should
            not be disabled.
        boundingBoxes:
          type: array
          description: >-
            List of bounding boxes. The existing bounding boxes on the sample
            will be replaced (so if you want to add new bounding boxes, use the
            existing list as a basis).
          items:
            $ref: '#/components/schemas/BoundingBox'
        metadata:
          type: object
          description: >-
            Free form associated metadata. The existing metadata on the sample
            will be replaced (so if you want to add new metadata, use the
            existing list as a basis).
          additionalProperties:
            type: string
        structuredLabels:
          type: array
          description: New label (multi-label)
          items:
            $ref: '#/components/schemas/StructuredLabel'
    AIActionsDataCategory:
      type: string
      enum:
        - allData
        - unlabeledData
        - enabledData
        - dataWithoutMetadataKey
        - dataWithMetadata
    AIActionsConfigStep:
      type: object
      required:
        - transformationBlockId
        - parameters
      properties:
        transformationBlockId:
          description: The selected transformation block ID.
          type: integer
        parameters:
          description: >-
            Parameters for the transformation block. These map back to the
            parameters in OrganizationTransformationBlock 'parameters' property.
          type: object
          additionalProperties:
            type: string
    RawDataCategory:
      type: string
      enum:
        - training
        - testing
        - post-processing
    Sensor:
      type: object
      required:
        - name
        - units
      properties:
        name:
          type: string
          description: Name of the axis
          example: accX
        units:
          type: string
          description: >-
            Type of data on this axis. Needs to comply to SenML units (see
            https://www.iana.org/assignments/senml/senml.xhtml).
    BoundingBox:
      type: object
      description: >-
        This has the _absolute values_ for x/y/w/h (so 0..x (where x is the w/h
        of the image))
      required:
        - label
        - x
        - 'y'
        - width
        - height
      properties:
        label:
          type: string
        x:
          type: integer
        'y':
          type: integer
        width:
          type: integer
        height:
          type: integer
    ProjectLabelingMethod:
      type: string
      enum:
        - single_label
        - object_detection
        - label_map
    StructuredLabel:
      type: object
      description: >-
        A structured label contains a label, and the range for which this label
        is valid. `endIndex` is inclusive. E.g. `{ startIndex: 10, endIndex: 13,
        label: 'running' }` means that the values at index 10, 11, 12, 13 are
        labeled 'running'. To get time codes you can multiple by the sample's
        `intervalMs` property.
      required:
        - startIndex
        - endIndex
        - label
      properties:
        startIndex:
          type: integer
          description: Start index of the label (e.g. 0)
        endIndex:
          type: integer
          description: >-
            End index of the label (e.g. 3). This value is inclusive, so {
            startIndex: 0, endIndex: 3 } covers 0, 1, 2, 3.
        label:
          type: string
          description: The label for this section.
        labelMap:
          $ref: '#/components/schemas/SampleLabelMapLabels'
    SampleLabelMapLabels:
      description: >
        Structured sample labels in the form of a key-value map.

        This property is optional and only defined for samples with key-value
        labels.
      discriminator:
        propertyName: type
        mapping:
          key-values:
            $ref: '#/components/schemas/SampleKeyValueLabels'
      oneOf:
        - $ref: '#/components/schemas/SampleKeyValueLabels'
    SampleKeyValueLabels:
      type: object
      required:
        - type
        - labels
      properties:
        type:
          type: string
          enum:
            - key-values
        labels:
          type: object
          additionalProperties:
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