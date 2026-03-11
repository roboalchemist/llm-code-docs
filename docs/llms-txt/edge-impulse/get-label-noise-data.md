# Source: https://docs.edgeimpulse.com/apis/studio/raw-data/get-label-noise-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get label noise data

> Obtain metrics that describe potential label noise issues in the dataset. To calculate these metrics, use the `calculateDataQualityMetrics` endpoint.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/raw-data/data-quality/label-noise
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
  /api/{projectId}/raw-data/data-quality/label-noise:
    get:
      tags:
        - Raw data
      summary: Get label noise data
      description: >-
        Obtain metrics that describe potential label noise issues in the
        dataset. To calculate these metrics, use the
        `calculateDataQualityMetrics` endpoint.
      operationId: getLabelNoiseData
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetLabelNoiseDataResponse'
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
    GetLabelNoiseDataResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - data
          properties:
            data:
              type: object
              properties:
                cosineSimilarity:
                  $ref: '#/components/schemas/CosineSimilarityData'
                neighbors:
                  $ref: '#/components/schemas/NeighborsData'
                crossValidation:
                  $ref: '#/components/schemas/CrossValidationData'
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
    CosineSimilarityData:
      type: object
      description: >-
        Describes the results of running the cosine similarity label noise
        detection method.
      required:
        - similarButDifferentLabel
        - differentButSameLabel
      properties:
        similarButDifferentLabel:
          type: array
          description: >-
            A list of samples that have windows that are similar to windows of
            other samples that have a different label.
          items:
            $ref: '#/components/schemas/CosineSimilarityIssue'
        differentButSameLabel:
          type: array
          description: >-
            A list of samples that have windows that are dissimilar to windows
            of other samples that have the same label.
          items:
            $ref: '#/components/schemas/CosineSimilarityIssue'
    NeighborsData:
      type: object
      description: >-
        Describes the results of running the nearest neighbors label noise
        detection method.
      required:
        - scoresAndNeighbors
        - numNeighbors
      properties:
        scoresAndNeighbors:
          type: array
          items:
            $ref: '#/components/schemas/NeighborsScore'
          description: >-
            The label noise score and nearest neighbors for each window of data
            in the project that shows a potential label noise issue.
        numNeighbors:
          type: integer
          description: The number of neighbors used in the nearest neighbors algorithm.
    CrossValidationData:
      type: object
      description: >-
        Describes the results of running the cross validation label noise
        detection method.
      required:
        - scores
      properties:
        scores:
          type: array
          items:
            type: object
            required:
              - id
              - windowStart
              - windowEnd
              - label
              - probability
              - score
            properties:
              id:
                type: integer
                description: The ID of the sample this window belongs to
              sample:
                $ref: '#/components/schemas/Sample'
                description: Detailed information about the sample this window belongs to
              windowStart:
                type: integer
                description: The start time of this window in milliseconds
              windowEnd:
                type: integer
                description: The end time of this window in milliseconds
              label:
                type: integer
                description: The label of this window, in index form
              probability:
                type: number
                description: >-
                  The probability of this window being the label it was
                  assigned, as estimated by a classifier trained on the whole
                  dataset.
              score:
                type: number
                description: >-
                  The z-score of the probability with respect to other class
                  members, so that outliers (i.e. windows whose probability is
                  low) can be easily spotted. This assumes that most correctly
                  labelled class members will have a high probability.
    CosineSimilarityIssue:
      type: object
      description: >-
        Describes a sample that has potential issues as identified by the cosine
        similarity label noise detection method.
      required:
        - id
        - label
        - issues
      properties:
        id:
          type: integer
          description: The ID of this sample
        sample:
          $ref: '#/components/schemas/Sample'
          description: Detailed information about the sample
        label:
          type: integer
          description: The label of this sample, in index form
        issues:
          type: array
          description: >-
            A list of samples that have windows that are symptomatic of this
            issue.
          items:
            type: object
            required:
              - id
              - label
              - windows
            properties:
              id:
                type: integer
                description: The ID of this sample
              sample:
                $ref: '#/components/schemas/Sample'
                description: Detailed information about the sample
              label:
                type: integer
                description: The label of this sample, in index form
              windows:
                type: array
                description: The windows in this sample that are symptomatic of this issue.
                items:
                  type: object
                  required:
                    - windowStart
                    - windowEnd
                    - score
                  properties:
                    windowStart:
                      type: integer
                      description: The start time of this window in milliseconds
                    windowEnd:
                      type: integer
                      description: The end time of this window in milliseconds
                    score:
                      type: number
                      description: >-
                        The cosine similarity score between this window and a
                        window from the sample in the parent object.
    NeighborsScore:
      type: object
      description: >-
        Describes the label noise score and nearest neighbors for a single
        window of data in the project that shows a potential label noise issue.
      required:
        - id
        - windowStart
        - windowEnd
        - score
        - neighborWindows
      properties:
        id:
          type: integer
          description: The ID of the sample this window belongs to
        sample:
          $ref: '#/components/schemas/Sample'
          description: Detailed information about the sample this window belongs to
        windowStart:
          type: integer
          description: The start time of this window in milliseconds
        windowEnd:
          type: integer
          description: The end time of this window in milliseconds
        score:
          type: number
          description: >-
            The label noise score for this window, from 0 to the total number of
            windows.
        neighborWindows:
          type: array
          description: Details of the nearest neighbors to this window
          items:
            type: object
            required:
              - id
              - windowStart
              - windowEnd
            properties:
              id:
                type: integer
                description: The ID of the sample this window belongs to
              sample:
                $ref: '#/components/schemas/Sample'
                description: Detailed information about the sample this window belongs to
              windowStart:
                type: integer
                description: The start time of this window in milliseconds
              windowEnd:
                type: integer
                description: The end time of this window in milliseconds
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