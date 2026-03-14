# Source: https://docs.edgeimpulse.com/apis/studio/jobs/deploy-pretrained-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy pretrained model

> Takes in a TFLite file and builds the model and SDK. Updates are streamed over the websocket API (or can be retrieved through the /stdout endpoint). Use getProfileTfliteJobResult to get the results when the job is completed.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/jobs/deploy-pretrained-model
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
  /api/{projectId}/jobs/deploy-pretrained-model:
    post:
      tags:
        - Jobs
      summary: Deploy pretrained model
      description: >-
        Takes in a TFLite file and builds the model and SDK. Updates are
        streamed over the websocket API (or can be retrieved through the /stdout
        endpoint). Use getProfileTfliteJobResult to get the results when the job
        is completed.
      operationId: startDeployPretrainedModelJob
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DeployPretrainedModelRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StartJobResponse'
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
    DeployPretrainedModelRequest:
      type: object
      required:
        - modelFileBase64
        - modelFileType
        - deploymentType
        - modelInfo
      properties:
        modelFileBase64:
          description: A base64 encoded pretrained model
          type: string
        modelFileType:
          type: string
          enum:
            - tflite
            - onnx
            - saved_model
            - lgbm
            - xgboost
            - pickle
            - ngboost
        deploymentType:
          type: string
          description: >-
            The name of the built target. You can find this by listing all
            deployment targets through `listDeploymentTargetsForProject` (via
            `GET /v1/api/{projectId}/deployment/targets`) and see the `format`
            type.
        engine:
          $ref: '#/components/schemas/DeploymentTargetEngine'
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
                    $ref: '#/components/schemas/DeployPretrainedModelInputTimeSeries'
                  audio:
                    $ref: '#/components/schemas/DeployPretrainedModelInputAudio'
                  image:
                    $ref: '#/components/schemas/DeployPretrainedModelInputImage'
                  other:
                    $ref: '#/components/schemas/DeployPretrainedModelInputOther'
              oneOf:
                - $ref: '#/components/schemas/DeployPretrainedModelInputTimeSeries'
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
                    $ref: '#/components/schemas/DeployPretrainedModelModelRegression'
                  object-detection:
                    $ref: >-
                      #/components/schemas/DeployPretrainedModelModelObjectDetection
                  freeform:
                    $ref: '#/components/schemas/DeployPretrainedModelModelFreeform'
                  anomaly:
                    $ref: '#/components/schemas/DeployPretrainedModelModelAnomaly'
                  visual-anomaly:
                    $ref: >-
                      #/components/schemas/DeployPretrainedModelModelVisualAnomaly
              oneOf:
                - $ref: >-
                    #/components/schemas/DeployPretrainedModelModelClassification
                - $ref: '#/components/schemas/DeployPretrainedModelModelRegression'
                - $ref: >-
                    #/components/schemas/DeployPretrainedModelModelObjectDetection
                - $ref: '#/components/schemas/DeployPretrainedModelModelFreeform'
                - $ref: '#/components/schemas/DeployPretrainedModelModelAnomaly'
                - $ref: '#/components/schemas/DeployPretrainedModelModelVisualAnomaly'
        representativeFeaturesBase64:
          description: >-
            A base64 encoded .npy file containing the features from your
            validation set (optional for onnx and saved_model) - used to
            quantize your model.
          type: string
        deployModelType:
          type: string
          enum:
            - int8
            - float32
        useConverter:
          description: Optional, use a specific converter (only for ONNX models).
          type: string
          enum:
            - onnx-tf
            - onnx2tf
        overrideInputShape:
          description: >-
            Optional for ONNX files: overrides the input shape of the model.
            This is highly suggested if the model has dynamic dimensions. If
            this field is not set, then all dynamic dimensions will be set to
            '1'.
          type: array
          items:
            type: integer
    StartJobResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - id
          properties:
            id:
              type: integer
              description: Job identifier. Status updates will include this identifier.
              example: 12873488112
    DeploymentTargetEngine:
      type: string
      enum:
        - tflite
        - tflite-eon
        - tflite-eon-ram-optimized
        - tensorrt
        - tensaiflow
        - drp-ai
        - tidl
        - akida
        - syntiant
        - memryx
        - neox
        - ethos-linux
        - st-aton
        - ceva-npn
        - nordic-axon
        - vlm-connector
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