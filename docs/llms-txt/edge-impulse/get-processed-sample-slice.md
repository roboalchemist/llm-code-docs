# Source: https://docs.edgeimpulse.com/apis/studio/dsp/get-processed-sample-slice.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get processed sample (slice)

> Get slice of sample data, and run it through the DSP block. This only the axes selected by the DSP block. E.g. if you have selected only accX and accY as inputs for the DSP block, but the raw sample also contains accZ, accZ is filtered out.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/dsp/{dspId}/raw-data/{sampleId}/slice/run
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
  /api/{projectId}/dsp/{dspId}/raw-data/{sampleId}/slice/run:
    post:
      tags:
        - DSP
      summary: Get processed sample (slice)
      description: >-
        Get slice of sample data, and run it through the DSP block. This only
        the axes selected by the DSP block. E.g. if you have selected only accX
        and accY as inputs for the DSP block, but the raw sample also contains
        accZ, accZ is filtered out.
      operationId: runDspSampleSlice
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/DspIdParameter'
        - $ref: '#/components/parameters/SampleIdParameter'
        - $ref: '#/components/parameters/SliceStartParameter'
        - $ref: >-
            #/components/parameters/OptionalSliceEndDefaultToWindowLengthParameter
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DspRunRequestWithoutFeatures'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DspRunResponseWithSample'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    DspIdParameter:
      name: dspId
      in: path
      required: true
      description: DSP Block ID, use the impulse functions to retrieve the ID
      schema:
        type: integer
    SampleIdParameter:
      name: sampleId
      in: path
      required: true
      description: Sample ID
      schema:
        type: integer
    SliceStartParameter:
      name: sliceStart
      in: query
      required: true
      description: Begin index of the slice
      schema:
        type: integer
    OptionalSliceEndDefaultToWindowLengthParameter:
      name: sliceEnd
      in: query
      required: false
      description: >-
        End index of the slice. If not given, the sample will be sliced to the
        same length as the impulse input block window length.
      schema:
        type: integer
  schemas:
    DspRunRequestWithoutFeatures:
      type: object
      required:
        - params
        - store
      properties:
        params:
          type: object
          description: DSP parameters with values
          example:
            scale-axes: '10'
          additionalProperties:
            type: string
            nullable: true
        store:
          type: boolean
          description: Whether to store the DSP parameters as the new default parameters.
    DspRunResponseWithSample:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - features
            - graphs
            - sample
            - canProfilePerformance
          properties:
            features:
              type: array
              description: >-
                Array of processed features. Laid out according to the names in
                'labels'
              items:
                type: number
            graphs:
              type: array
              description: Graphs to plot to give an insight in how the DSP process ran
              items:
                $ref: '#/components/schemas/DspRunGraph'
            labels:
              type: array
              description: Labels of the feature axes
              items:
                type: string
            state_string:
              type: string
              description: String representation of the DSP state returned
            labelAtEndOfWindow:
              description: >-
                DEPRECATED. Label at the end of the window (only present for
                time-series data)
              type: string
            labelForWindow:
              description: >-
                Label for the window. How the label is chosen is dependent on
                the value of "labelingMethodMultiLabel" in the input block.
              type: string
            sample:
              $ref: '#/components/schemas/RawSampleData'
            performance:
              $ref: '#/components/schemas/DspPerformance'
            canProfilePerformance:
              type: boolean
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
    DspRunGraph:
      type: object
      required:
        - name
        - type
      properties:
        name:
          type: string
          description: Name of the graph
          example: Frequency domain
        image:
          type: string
          description: Base64 encoded image, only present if type is 'image'
        imageMimeType:
          type: string
          description: >-
            Mime type of the Base64 encoded image, only present if type is
            'image'
        X:
          type: object
          description: >-
            Values on the x-axis per plot. Key is the name of the raw feature.
            Present if type is 'logarithmic' or 'linear'.
          example:
            accX:
              - 3
              - 5
              - 7
            accY:
              - 2
              - 1
              - 5
          additionalProperties:
            type: array
            items:
              type: number
        'y':
          type: array
          description: Values of the y-axis. Present if type is 'logarithmic' or 'linear'.
          example:
            - 0
            - 0.5
            - 1
          items:
            type: number
        suggestedXMin:
          type: number
          description: Suggested minimum value of x-axis
        suggestedXMax:
          type: number
          description: Suggested maxium value of x-axis
        suggestedYMin:
          type: number
          description: Suggested minimum value of y-axis
        suggestedYMax:
          type: number
          description: Suggested maximum value of y-axis
        type:
          type: string
          description: Type of graph (either `logarithmic`, `linear` or `image`)
        lineWidth:
          type: number
          description: >-
            Width of the graph line (if type is `logarithmic` or `linear`).
            Default 3.
        smoothing:
          type: boolean
          description: Whether to apply smoothing to the graph.
        axisLabels:
          type: object
          description: Labels for the graph x and y axes.
          required:
            - X
            - 'y'
          properties:
            X:
              type: string
            'y':
              type: string
        highlights:
          type: object
          description: Indices of points to highlight, per axis.
          additionalProperties:
            type: array
            items:
              type: number
    RawSampleData:
      type: object
      required:
        - sample
        - payload
        - totalPayloadLength
      properties:
        sample:
          $ref: '#/components/schemas/Sample'
        payload:
          $ref: '#/components/schemas/RawSamplePayload'
        totalPayloadLength:
          type: integer
          description: Total number of payload values
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
    RawSamplePayload:
      type: object
      description: Sensor readings and metadata
      required:
        - device_type
        - sensors
        - values
      properties:
        device_name:
          type: string
          description: >-
            Unique identifier for this device. **Only** set this when the device
            has a globally unique identifier (e.g. MAC address).
          example: ac:87:a3:0a:2d:1b
        device_type:
          type: string
          description: >-
            Device type, for example the exact model of the device. Should be
            the same for all similar devices.
          example: DISCO-L475VG-IOT01A
        sensors:
          type: array
          description: Array with sensor axes
          items:
            $ref: '#/components/schemas/Sensor'
        values:
          type: array
          description: >
            Array of sensor values. One array item per interval, and as many
            items in this array as there are sensor axes. This type is returned
            if there are multiple axes.
          items:
            type: array
            items:
              type: number
        cropStart:
          type: integer
          description: New start index of the cropped sample
          example: 0
        cropEnd:
          type: integer
          description: New end index of the cropped sample
          example: 128
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