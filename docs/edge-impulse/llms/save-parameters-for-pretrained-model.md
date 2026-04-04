# Source: https://docs.edgeimpulse.com/apis/studio/learn/save-parameters-for-pretrained-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Save parameters for pretrained model

> Save input / model configuration for a pretrained model. This overrides the current impulse. If you want to deploy a pretrained model from the API, see `startDeployPretrainedModelJob`.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/pretrained-model/save
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
  /api/{projectId}/pretrained-model/save:
    post:
      tags:
        - Learn
      summary: Save parameters for pretrained model
      description: >-
        Save input / model configuration for a pretrained model. This overrides
        the current impulse. If you want to deploy a pretrained model from the
        API, see `startDeployPretrainedModelJob`.
      operationId: savePretrainedModelParameters
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SavePretrainedModelRequest'
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
    OptionalImpulseIdParameter:
      name: impulseId
      in: query
      required: false
      description: Impulse ID. If this is unset then the default impulse is used.
      schema:
        type: integer
  schemas:
    SavePretrainedModelRequest:
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
                $ref: '#/components/schemas/DeployPretrainedModelModelClassification'
              regression:
                $ref: '#/components/schemas/DeployPretrainedModelModelRegression'
              object-detection:
                $ref: '#/components/schemas/DeployPretrainedModelModelObjectDetection'
              freeform:
                $ref: '#/components/schemas/DeployPretrainedModelModelFreeform'
              anomaly:
                $ref: '#/components/schemas/DeployPretrainedModelModelAnomaly'
              visual-anomaly:
                $ref: '#/components/schemas/DeployPretrainedModelModelVisualAnomaly'
          oneOf:
            - $ref: '#/components/schemas/DeployPretrainedModelModelClassification'
            - $ref: '#/components/schemas/DeployPretrainedModelModelRegression'
            - $ref: '#/components/schemas/DeployPretrainedModelModelObjectDetection'
            - $ref: '#/components/schemas/DeployPretrainedModelModelFreeform'
            - $ref: '#/components/schemas/DeployPretrainedModelModelAnomaly'
            - $ref: '#/components/schemas/DeployPretrainedModelModelVisualAnomaly'
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