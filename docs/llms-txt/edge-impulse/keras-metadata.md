# Source: https://docs.edgeimpulse.com/apis/studio/learn/keras-metadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Keras metadata

> Get metadata about a trained Keras block. Use the impulse blocks to find the learnId.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/training/keras/{learnId}/metadata
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
  /api/{projectId}/training/keras/{learnId}/metadata:
    get:
      tags:
        - Learn
      summary: Keras metadata
      description: >-
        Get metadata about a trained Keras block. Use the impulse blocks to find
        the learnId.
      operationId: getKerasMetadata
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/LearnIdParameter'
        - $ref: '#/components/parameters/ExcludeLabelsParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/KerasModelMetadataResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    LearnIdParameter:
      name: learnId
      in: path
      required: true
      description: Learn Block ID, use the impulse functions to retrieve the ID
      schema:
        type: integer
    ExcludeLabelsParameter:
      name: excludeLabels
      in: query
      required: false
      description: >-
        If set to "true", the "labels" field is left empty (which can be big on
        e.g. regression projects).
      schema:
        type: boolean
  schemas:
    KerasModelMetadataResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - $ref: '#/components/schemas/KerasModelMetadata'
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
    KerasModelTypeEnum:
      type: string
      enum:
        - int8
        - float32
        - akida
        - requiresRetrain
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
    TensorboardGraphs:
      type: array
      items:
        $ref: '#/components/schemas/KerasModelMetadataGraph'
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