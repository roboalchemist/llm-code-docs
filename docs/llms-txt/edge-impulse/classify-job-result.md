# Source: https://docs.edgeimpulse.com/apis/studio/classify/classify-job-result.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Classify job result

> Get classify job result, containing the result for the complete testing dataset.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/classify/all/result
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
  /api/{projectId}/classify/all/result:
    get:
      tags:
        - Classify
      summary: Classify job result
      description: >-
        Get classify job result, containing the result for the complete testing
        dataset.
      operationId: getClassifyJobResult
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/FeatureExplorerOnlyParameter'
        - $ref: '#/components/parameters/ModelVariantParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
        - $ref: '#/components/parameters/TruncateStructuredLabelsParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ClassifyJobResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    FeatureExplorerOnlyParameter:
      name: featureExplorerOnly
      in: query
      required: false
      description: >-
        Whether to get only the classification results relevant to the feature
        explorer.
      schema:
        type: boolean
    ModelVariantParameter:
      name: variant
      in: query
      required: false
      description: Keras model variant
      schema:
        $ref: '#/components/schemas/KerasModelVariantEnum'
    OptionalImpulseIdParameter:
      name: impulseId
      in: query
      required: false
      description: Impulse ID. If this is unset then the default impulse is used.
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
  schemas:
    ClassifyJobResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - result
            - predictions
            - accuracy
            - additionalMetricsByLearnBlock
            - availableVariants
          properties:
            result:
              type: array
              items:
                $ref: '#/components/schemas/ModelResult'
            predictions:
              type: array
              items:
                $ref: '#/components/schemas/ModelPrediction'
            accuracy:
              type: object
              required:
                - totalSummary
                - summaryPerClass
                - confusionMatrixValues
                - rows
                - allLabels
              properties:
                totalSummary:
                  type: object
                  required:
                    - good
                    - bad
                  properties:
                    good:
                      type: integer
                    bad:
                      type: integer
                summaryPerClass:
                  type: object
                  additionalProperties:
                    type: object
                    required:
                      - good
                      - bad
                    properties:
                      good:
                        type: integer
                      bad:
                        type: integer
                confusionMatrixValues:
                  type: object
                  additionalProperties:
                    type: object
                    additionalProperties:
                      type: number
                allLabels:
                  type: array
                  items:
                    type: string
                accuracyScore:
                  type: number
                balancedAccuracyScore:
                  type: number
                anomalyAccuracyScore:
                  type: number
                noAnomalyAccuracyScore:
                  type: number
                mseScore:
                  type: number
            additionalMetricsByLearnBlock:
              type: array
              items:
                type: object
                required:
                  - learnBlockId
                  - learnBlockName
                  - additionalMetrics
                properties:
                  learnBlockId:
                    type: integer
                  learnBlockName:
                    type: string
                  additionalMetrics:
                    type: array
                    items:
                      $ref: '#/components/schemas/AdditionalMetric'
            availableVariants:
              type: array
              description: >-
                List of all model variants for which classification results
                exist
              items:
                $ref: '#/components/schemas/KerasModelVariantEnum'
            noResultsBecauseThresholdsChanged:
              type: string
              description: >
                If set to true, there are currently no results because
                thresholds were changed (e.g. on live classification);

                and what action you can run to get new results the quickest.

                If the value is "can_regenerate_model_summary" you can run
                'regenerateModelTestingSummary'.

                If the value is "should_rerun_full_job", you need to run
                'startClassifyJob' or 'startEvaluateJob'.
              enum:
                - can_regenerate_model_summary
                - should_rerun_full_job
    KerasModelVariantEnum:
      type: string
      enum:
        - int8
        - float32
        - akida
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
    ModelResult:
      type: object
      required:
        - sampleId
        - sample
        - classifications
      properties:
        sampleId:
          type: integer
        sample:
          $ref: '#/components/schemas/Sample'
        classifications:
          type: array
          items:
            $ref: '#/components/schemas/ClassifySampleResponseClassification'
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
    ClassifySampleResponseClassification:
      type: object
      required:
        - learnBlock
        - result
        - expectedLabels
        - minimumConfidenceRating
        - thresholds
      properties:
        learnBlock:
          $ref: '#/components/schemas/ImpulseLearnBlock'
        result:
          type: array
          description: Classification result, one item per window.
          example:
            - idle: 0.0002
              wave: 0.9998
              anomaly: -0.42
          items:
            type: object
            description: >-
              Classification value per label. For a neural network this will be
              the confidence, for anomalies the anomaly score.
            additionalProperties:
              type: number
        anomalyResult:
          type: array
          description: >-
            Anomaly scores and computed metrics for visual anomaly detection,
            one item per window.
          items:
            $ref: '#/components/schemas/AnomalyResult'
        structuredResult:
          type: array
          description: >-
            Results of inferencing that returns structured data, such as object
            detection
          items:
            $ref: '#/components/schemas/StructuredClassifyResult'
        minimumConfidenceRating:
          type: number
          description: >-
            DEPRECATED, see "thresholds" instead. The minimum confidence rating
            for this block. For regression, this is the absolute error (which
            can be larger than 1).
        details:
          type: array
          description: >-
            Structured outputs and computed metrics for some model types (e.g.
            object detection), one item per window.
          items:
            $ref: '#/components/schemas/ClassifySampleResponseClassificationDetails'
        objectDetectionLastLayer:
          $ref: '#/components/schemas/ObjectDetectionLastLayer'
        expectedLabels:
          type: array
          description: An array with an expected label per window.
          items:
            $ref: '#/components/schemas/StructuredLabel'
        expectedAnomalyOutcome:
          type: array
          description: >
            An array with the expected anomaly outcome for each window — either
            “anomaly” or “no anomaly”. The outcome is determined by which labels
            are marked as anomalous in the project setup, or by the sample label
            if no such configuration is defined.
          items:
            $ref: '#/components/schemas/StructuredLabel'
        thresholds:
          type: array
          description: List of configurable thresholds for this block.
          items:
            $ref: '#/components/schemas/BlockThreshold'
        isMultiLabel:
          type: boolean
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
    AnomalyResult:
      type: object
      properties:
        boxes:
          type: array
          description: >-
            For visual anomaly detection. An array of bounding box objects, (x,
            y, width, height, score, label), one per detection in the image.
            Filtered by the minimum confidence rating of the learn block.
          items:
            $ref: '#/components/schemas/BoundingBoxWithScore'
        scores:
          type: array
          description: >-
            2D array of shape (n, n) with raw anomaly scores for visual anomaly
            detection, where n can be calculated as ((1/8 of image input size)/2
            - 1). The scores corresponds to each grid cell in the image's
            spatial matrix.
          items:
            type: array
            items:
              type: number
        meanScore:
          type: number
          description: Mean value of the scores.
        maxScore:
          type: number
          description: Maximum value of the scores.
    StructuredClassifyResult:
      type: object
      required:
        - boxes
        - scores
        - mAP
        - f1
        - precision
        - recall
      properties:
        boxes:
          type: array
          description: >-
            For object detection. An array of bounding box arrays, (x, y, width,
            height), one per detection in the image.
          items:
            type: array
            items:
              type: number
        labels:
          type: array
          description: >-
            For object detection. An array of labels, one per detection in the
            image.
          items:
            type: string
        scores:
          type: array
          description: >-
            For object detection. An array of probability scores, one per
            detection in the image.
          items:
            type: number
        mAP:
          type: number
          description: >-
            For object detection. A score that indicates accuracy compared to
            the ground truth, if available.
        f1:
          type: number
          description: >-
            For FOMO. A score that combines the precision and recall of a
            classifier into a single metric, if available.
        precision:
          type: number
          description: >-
            A measure of how many of the positive predictions made are correct
            (true positives).
        recall:
          type: number
          description: >-
            A measure of how many of the positive cases the classifier correctly
            predicted, over all the positive cases.
        debugInfoJson:
          type: string
          description: Debug info in JSON format
          example: |
            {
                "y_trues": [
                    {"x": 0.854, "y": 0.453125, "label": 1},
                    {"x": 0.197, "y": 0.53125, "label": 2}
                ],
                "y_preds": [
                    {"x": 0.916, "y": 0.875, "label": 1},
                    {"x": 0.25, "y": 0.541, "label": 2}
                ],
                "assignments": [
                    {"yp": 1, "yt": 1, "label": 2, "distance": 0.053}
                ],
                "normalised_min_distance": 0.2,
                "all_pairwise_distances": [
                    [0, 0, 0.426],
                    [1, 1, 0.053]
                ],
                "unassigned_y_true_idxs": [0],
                "unassigned_y_pred_idxs": [0]
            }
    ClassifySampleResponseClassificationDetails:
      type: object
      properties:
        boxes:
          type: array
          description: Bounding boxes predicted by localization model
          items:
            type: array
            items:
              type: number
        labels:
          type: array
          description: Labels predicted by localization model
          items:
            type: number
        scores:
          type: array
          description: Scores predicted by localization model
          items:
            type: number
        mAP:
          type: number
          description: >-
            For object detection, the COCO mAP computed for the predictions on
            this image
        f1:
          type: number
          description: For FOMO, the F1 score computed for the predictions on this image
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