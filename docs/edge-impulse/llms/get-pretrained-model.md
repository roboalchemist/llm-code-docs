# Source: https://docs.edgeimpulse.com/apis/studio/learn/get-pretrained-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get pretrained model

> Receive info back about the earlier uploaded pretrained model (via `uploadPretrainedModel`) input/output tensors. If you want to deploy a pretrained model from the API, see `startDeployPretrainedModelJob`.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/pretrained-model
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
  /api/{projectId}/pretrained-model:
    get:
      tags:
        - Learn
      summary: Get pretrained model
      description: >-
        Receive info back about the earlier uploaded pretrained model (via
        `uploadPretrainedModel`) input/output tensors. If you want to deploy a
        pretrained model from the API, see `startDeployPretrainedModelJob`.
      operationId: getPretrainedModelInfo
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetPretrainedModelResponse'
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
    GetPretrainedModelResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - specificDeviceSelected
            - availableModelTypes
          properties:
            specificDeviceSelected:
              type: boolean
              description: Whether a specific device was selected for performance profiling
            availableModelTypes:
              type: array
              description: The types of model that are available
              items:
                $ref: '#/components/schemas/KerasModelTypeEnum'
            model:
              type: object
              required:
                - fileName
                - inputs
                - outputs
              properties:
                fileName:
                  type: string
                profileInfo:
                  type: object
                  required:
                    - table
                  properties:
                    float32:
                      $ref: '#/components/schemas/ProfileModelInfo'
                    int8:
                      $ref: '#/components/schemas/ProfileModelInfo'
                    table:
                      $ref: '#/components/schemas/ProfileModelTable'
                inputs:
                  type: array
                  items:
                    $ref: '#/components/schemas/PretrainedModelTensor'
                outputs:
                  type: array
                  items:
                    $ref: '#/components/schemas/PretrainedModelTensor'
                profileJobId:
                  description: >-
                    If this is set, then we're still profiling this model.
                    Subscribe to job updates to see when it's done (afterward
                    the metadata will be updated).
                  type: integer
                profileJobFailed:
                  description: >-
                    If this is set, then the profiling job failed (get the
                    status by getting the job logs for 'profilingJobId').
                  type: boolean
                supportsTFLite:
                  type: boolean
            modelInfo:
              type: object
              required:
                - input
                - model
              properties:
                input:
                  discriminator:
                    propertyName: inputType
                    mapping:
                      time-series:
                        $ref: >-
                          #/components/schemas/DeployPretrainedModelInputTimeSeries
                      audio:
                        $ref: '#/components/schemas/DeployPretrainedModelInputAudio'
                      image:
                        $ref: '#/components/schemas/DeployPretrainedModelInputImage'
                      other:
                        $ref: '#/components/schemas/DeployPretrainedModelInputOther'
                  oneOf:
                    - $ref: >-
                        #/components/schemas/DeployPretrainedModelInputTimeSeries
                    - $ref: '#/components/schemas/DeployPretrainedModelInputAudio'
                    - $ref: '#/components/schemas/DeployPretrainedModelInputImage'
                    - $ref: '#/components/schemas/DeployPretrainedModelInputOther'
                model:
                  discriminator:
                    propertyName: modelType
                    mapping:
                      classification:
                        $ref: >-
                          #/components/schemas/DeployPretrainedModelModelClassification
                      regression:
                        $ref: >-
                          #/components/schemas/DeployPretrainedModelModelRegression
                      object-detection:
                        $ref: >-
                          #/components/schemas/DeployPretrainedModelModelObjectDetection
                      freeform:
                        $ref: >-
                          #/components/schemas/DeployPretrainedModelModelFreeform
                      anomaly:
                        $ref: '#/components/schemas/DeployPretrainedModelModelAnomaly'
                      visual-anomaly:
                        $ref: >-
                          #/components/schemas/DeployPretrainedModelModelVisualAnomaly
                  oneOf:
                    - $ref: >-
                        #/components/schemas/DeployPretrainedModelModelClassification
                    - $ref: >-
                        #/components/schemas/DeployPretrainedModelModelRegression
                    - $ref: >-
                        #/components/schemas/DeployPretrainedModelModelObjectDetection
                    - $ref: '#/components/schemas/DeployPretrainedModelModelFreeform'
                    - $ref: '#/components/schemas/DeployPretrainedModelModelAnomaly'
                    - $ref: >-
                        #/components/schemas/DeployPretrainedModelModelVisualAnomaly
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
    KerasModelTypeEnum:
      type: string
      enum:
        - int8
        - float32
        - akida
        - requiresRetrain
    ProfileModelInfo:
      type: object
      required:
        - variant
        - device
        - tfliteFileSizeBytes
        - isSupportedOnMcu
        - customMetrics
        - hasPerformance
      properties:
        variant:
          $ref: '#/components/schemas/KerasModelVariantEnum'
        device:
          type: string
        tfliteFileSizeBytes:
          type: integer
        isSupportedOnMcu:
          type: boolean
        memory:
          type: object
          properties:
            tflite:
              $ref: '#/components/schemas/ProfileModelInfoMemoryDetails'
            eon:
              $ref: '#/components/schemas/ProfileModelInfoMemoryDetails'
            eonRamOptimized:
              $ref: '#/components/schemas/ProfileModelInfoMemoryDetails'
        timePerInferenceMs:
          type: integer
        mcuSupportError:
          type: string
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
    ProfileModelTable:
      type: object
      required:
        - variant
        - lowEndMcu
        - highEndMcu
        - highEndMcuPlusAccelerator
        - mpu
        - gpuOrMpuAccelerator
      description: >-
        Performance for a range of device types. Note that MPU is referred to as
        CPU in Studio, as MPU and CPU are treated equivalent for performance
        estimation.
      properties:
        variant:
          type: string
          enum:
            - int8
            - float32
        lowEndMcu:
          $ref: '#/components/schemas/ProfileModelTableMcu'
        highEndMcu:
          $ref: '#/components/schemas/ProfileModelTableMcu'
        highEndMcuPlusAccelerator:
          $ref: '#/components/schemas/ProfileModelTableMcu'
        mpu:
          $ref: '#/components/schemas/ProfileModelTableMpu'
        gpuOrMpuAccelerator:
          $ref: '#/components/schemas/ProfileModelTableMpu'
    PretrainedModelTensor:
      type: object
      required:
        - dataType
        - name
        - shape
      properties:
        dataType:
          type: string
          enum:
            - int8
            - uint8
            - float32
        name:
          type: string
        shape:
          type: array
          items:
            type: integer
        quantizationScale:
          type: number
        quantizationZeroPoint:
          type: number
    DeployPretrainedModelInputTimeSeries:
      type: object
      required:
        - inputType
        - frequencyHz
        - windowLengthMs
      properties:
        inputType:
          type: string
          enum:
            - time-series
        frequencyHz:
          type: number
        windowLengthMs:
          type: integer
    DeployPretrainedModelInputAudio:
      type: object
      required:
        - inputType
        - frequencyHz
      properties:
        inputType:
          type: string
          enum:
            - audio
        frequencyHz:
          type: number
    DeployPretrainedModelInputImage:
      type: object
      required:
        - inputType
      properties:
        inputType:
          type: string
          enum:
            - image
        inputScaling:
          $ref: '#/components/schemas/ImageInputScaling'
        resizeMode:
          $ref: '#/components/schemas/ImageInputResizeMode'
    DeployPretrainedModelInputOther:
      type: object
      required:
        - inputType
      properties:
        inputType:
          type: string
          enum:
            - other
    DeployPretrainedModelModelClassification:
      type: object
      required:
        - modelType
        - labels
      properties:
        modelType:
          type: string
          enum:
            - classification
        labels:
          type: array
          items:
            type: string
    DeployPretrainedModelModelRegression:
      type: object
      required:
        - modelType
      properties:
        modelType:
          type: string
          enum:
            - regression
    DeployPretrainedModelModelObjectDetection:
      type: object
      required:
        - modelType
        - labels
        - lastLayer
        - minimumConfidence
      properties:
        modelType:
          type: string
          enum:
            - object-detection
        labels:
          type: array
          items:
            type: string
        lastLayer:
          $ref: '#/components/schemas/ObjectDetectionLastLayer'
        minimumConfidence:
          description: >-
            Deprecated: use thresholdValues instead. Threshold for objects (f.e.
            0.3).
          type: number
        thresholdValues:
          type: object
          description: >-
            All configured thresholds for the current model. Valid keys are
            'min_score' (object detection models, all but paddleocr-detector);
            'min_score_pixel', 'min_score_box', 'unclip_ratio'
            (paddleocr-detector).
          additionalProperties:
            type: number
    DeployPretrainedModelModelFreeform:
      type: object
      required:
        - modelType
      properties:
        modelType:
          type: string
          enum:
            - freeform
    DeployPretrainedModelModelAnomaly:
      type: object
      required:
        - modelType
      properties:
        modelType:
          type: string
          enum:
            - anomaly
    DeployPretrainedModelModelVisualAnomaly:
      type: object
      required:
        - modelType
      properties:
        modelType:
          type: string
          enum:
            - visual-anomaly
        thresholdValues:
          type: object
          description: >-
            All configured thresholds for the current model. Valid keys are
            'min_anomaly_score' and 'anomaly_scoring_aggregation_method'.
          additionalProperties:
            $ref: '#/components/schemas/ThresholdValue'
    KerasModelVariantEnum:
      type: string
      enum:
        - int8
        - float32
        - akida
    ProfileModelInfoMemoryDetails:
      type: object
      required:
        - ram
        - rom
        - arenaSize
      properties:
        ram:
          type: integer
          description: Estimated amount of RAM required by the model, measured in bytes
        rom:
          type: integer
          description: Estimated amount of ROM required by the model, measured in bytes
        arenaSize:
          type: integer
          description: Estimated arena size required for model inference, measured in bytes
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
    ProfileModelTableMcu:
      type: object
      required:
        - description
        - supported
      properties:
        description:
          type: string
        timePerInferenceMs:
          type: integer
        memory:
          type: object
          properties:
            tflite:
              type: object
              required:
                - ram
                - rom
              properties:
                ram:
                  type: integer
                rom:
                  type: integer
            eon:
              type: object
              required:
                - ram
                - rom
              properties:
                ram:
                  type: integer
                rom:
                  type: integer
            eonRamOptimized:
              type: object
              required:
                - ram
                - rom
              properties:
                ram:
                  type: integer
                rom:
                  type: integer
        supported:
          type: boolean
        mcuSupportError:
          type: string
    ProfileModelTableMpu:
      type: object
      required:
        - description
        - supported
      properties:
        description:
          type: string
        timePerInferenceMs:
          type: integer
        rom:
          type: number
        supported:
          type: boolean
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
    ImageInputResizeMode:
      type: string
      description: >
        Input images are resized automatically before training and testing, to
        match the impulse input shape.

        This determines the resize mode used when the aspect ratio of the input
        data is different to the aspect ratio of the impulse.
      example: squash
      enum:
        - squash
        - fit-short
        - fit-long
        - crop
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
    ThresholdValue:
      description: Current value of the threshold
      oneOf:
        - type: number
        - type: string
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