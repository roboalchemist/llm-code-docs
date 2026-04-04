# Source: https://docs.edgeimpulse.com/apis/studio/raw-data/list-samples.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List samples

> Retrieve all raw data by category.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/raw-data
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
  /api/{projectId}/raw-data:
    get:
      tags:
        - Raw data
      summary: List samples
      description: Retrieve all raw data by category.
      operationId: listSamples
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/RawDataCategoryQueryParameter'
        - $ref: '#/components/parameters/LimitResultsParameter'
        - $ref: '#/components/parameters/OffsetResultsParameter'
        - $ref: '#/components/parameters/ExcludeSensorsParameter'
        - $ref: '#/components/parameters/FiltersLabelsParameter'
        - $ref: '#/components/parameters/FiltersFilenameParameter'
        - $ref: '#/components/parameters/FiltersMaxLengthParameter'
        - $ref: '#/components/parameters/FiltersMinLengthParameter'
        - $ref: '#/components/parameters/FiltersMinFrequencyParameter'
        - $ref: '#/components/parameters/FiltersMaxFrequencyParameter'
        - $ref: '#/components/parameters/FiltersSignatureParameter'
        - $ref: '#/components/parameters/FiltersDisabledParameter'
        - $ref: '#/components/parameters/FiltersMinLabelParameter'
        - $ref: '#/components/parameters/FiltersMaxLabelParameter'
        - $ref: '#/components/parameters/SearchQueryParameter'
        - $ref: '#/components/parameters/ProposedActionsJobIdParameter'
        - $ref: '#/components/parameters/TruncateStructuredLabelsParameter'
        - $ref: '#/components/parameters/SamplesSortByParameter'
        - $ref: '#/components/parameters/FiltersDataTypeParameter'
        - $ref: '#/components/parameters/FiltersMinIdParameter'
        - $ref: '#/components/parameters/FiltersMaxIdParameter'
        - $ref: '#/components/parameters/FiltersMetadataParameter'
        - $ref: '#/components/parameters/FiltersMinDateParameter'
        - $ref: '#/components/parameters/FiltersMaxDateParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListSamplesResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    RawDataCategoryQueryParameter:
      name: category
      in: query
      required: true
      description: Which of the three acquisition categories to retrieve data from
      schema:
        $ref: '#/components/schemas/RawDataFilterCategory'
    LimitResultsParameter:
      name: limit
      in: query
      required: false
      description: Maximum number of results
      schema:
        type: integer
    OffsetResultsParameter:
      name: offset
      in: query
      required: false
      description: >-
        Offset in results, can be used in conjunction with LimitResultsParameter
        to implement paging.
      schema:
        type: integer
    ExcludeSensorsParameter:
      name: excludeSensors
      in: query
      required: false
      description: >-
        Whether to exclude sensors in the response (as these can slow down
        requests when you have large pages).
      schema:
        type: boolean
    FiltersLabelsParameter:
      name: labels
      in: query
      required: false
      description: >-
        Only include samples with a label within the given list of labels, given
        as a JSON string
      schema:
        example: '["idle", "snake"]'
        type: string
    FiltersFilenameParameter:
      name: filename
      in: query
      required: false
      description: Only include samples whose filename includes the given filename
      schema:
        type: string
    FiltersMaxLengthParameter:
      name: maxLength
      in: query
      required: false
      description: Only include samples shorter than the given length, in milliseconds
      schema:
        type: integer
    FiltersMinLengthParameter:
      name: minLength
      in: query
      required: false
      description: Only include samples longer than the given length, in milliseconds
      schema:
        type: integer
    FiltersMinFrequencyParameter:
      name: minFrequency
      in: query
      required: false
      description: >-
        Only include samples with higher frequency than given frequency, in
        hertz
      schema:
        type: number
    FiltersMaxFrequencyParameter:
      name: maxFrequency
      in: query
      required: false
      description: Only include samples with lower frequency than given frequency, in hertz
      schema:
        type: number
    FiltersSignatureParameter:
      name: signatureValidity
      in: query
      required: false
      description: Include samples with either valid or invalid signatures
      schema:
        type: string
        enum:
          - both
          - valid
          - invalid
    FiltersDisabledParameter:
      name: includeDisabled
      in: query
      required: false
      description: Include only enabled or disabled samples (or both)
      schema:
        type: string
        enum:
          - both
          - enabled
          - disabled
    FiltersMinLabelParameter:
      name: minLabel
      in: query
      required: false
      description: Only include samples with a label >= this value
      schema:
        type: number
    FiltersMaxLabelParameter:
      name: maxLabel
      in: query
      required: false
      description: Only include samples with a label < this value
      schema:
        type: number
    SearchQueryParameter:
      name: search
      in: query
      required: false
      description: Search query
      schema:
        example: <id> <name>
        type: string
    ProposedActionsJobIdParameter:
      name: proposedActionsJobId
      in: query
      required: false
      description: >-
        Pass this parameter when querying samples from inside an AI Action job.
        If you pass this parameter in a multi-stage AI Action, previous proposed
        changes (from an earlier step) will be applied to the returned dataset.
      schema:
        type: integer
    TruncateStructuredLabelsParameter:
      name: truncateStructuredLabels
      in: query
      required: false
      description: >-
        If true, only a slice of labels will be returned for samples with
        multiple labels.
      schema:
        type: boolean
    SamplesSortByParameter:
      name: sortBy
      in: query
      required: false
      description: If not specified, "id-desc" is used.
      schema:
        type: string
        enum:
          - id-desc
          - random
    FiltersDataTypeParameter:
      name: dataType
      in: query
      required: false
      description: Include only samples with a particular data type
      schema:
        type: string
        enum:
          - audio
          - image
    FiltersMinIdParameter:
      name: minId
      in: query
      required: false
      description: Include only samples with an ID >= this value
      schema:
        type: integer
    FiltersMaxIdParameter:
      name: maxId
      in: query
      required: false
      description: Include only samples with an ID < this value
      schema:
        type: integer
    FiltersMetadataParameter:
      name: metadata
      in: query
      required: false
      description: >
        Filter samples by metadata key-value pairs, provided as a JSON string.

        Each item in the filter list is an object with the following properties:
            - "key": Metadata key to filter on.
            - "op": Operator ("eq" for positive match, "neq" for negative match).
            - "values": (optional) Array of values to match/exclude. If omitted or empty, matches/excludes all values for the key.
        In addition to filter objects, the following option objects can be
        specified:
            - { "no_metadata": boolean } - If true, include samples without any metadata
            - { "filters_combinator": ("and" | "or") } - Specifies the combinator and matching mode:
                - "and": All filter items must match (logical AND).
                - "or": Any filter item may match (logical OR); samples with metadata keys not present in the filters are included.
      schema:
        example: >
          Example 1: returns samples where metadata key "foo" is 'bar' or 'baz'
          AND

          metadata key "k" is "v".

          [
              { "no_metadata": true },
              { "filters_combinator": "and" },
              { "key": "foo", "op": "eq", "values": ["bar", "baz"] },
              { "key": "k", "op": "eq", "values": ["v"] }
          ]


          Example 2: returns samples where metadata key "foo" is not 'bar'.
          Samples

          without any metadata are filtered out.

          [
              { "no_metadata": false },
              { "filters_combinator": "or" },
              { "key": "foo", "op": "neq", "values": ["bar"] }
          ]
        type: string
    FiltersMinDateParameter:
      name: minDate
      in: query
      required: false
      description: Only include samples that where added after the date given
      schema:
        type: string
        format: date-time
        example: '2023-01-01T00:00:00.000Z'
    FiltersMaxDateParameter:
      name: maxDate
      in: query
      required: false
      description: Only include samples that were added before the date given
      schema:
        type: string
        format: date-time
        example: '2024-12-31T00:00:00.000Z'
  schemas:
    ListSamplesResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - samples
            - totalCount
          properties:
            samples:
              type: array
              items:
                $ref: '#/components/schemas/Sample'
            totalCount:
              type: integer
    RawDataFilterCategory:
      type: string
      enum:
        - training
        - testing
        - post-processing
        - all
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