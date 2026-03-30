# Source: https://docs.edgeimpulse.com/apis/studio/learn/test-pretrained-model-using-image-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Test pretrained model using image data

> Test out a pretrained model (using image data) - upload first via  `uploadPretrainedModel`.
If you want to deploy a pretrained model from the API, see `startDeployPretrainedModelJob`.
This will transform raw image data (e.g. RGB to grayscale, resize) before classifying.
To classify raw features, see `testPretrainedModel`.




## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/pretrained-model/test-image
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
  /api/{projectId}/pretrained-model/test-image:
    post:
      tags:
        - Learn
      summary: Test pretrained model using image data
      description: >
        Test out a pretrained model (using image data) - upload first via 
        `uploadPretrainedModel`.

        If you want to deploy a pretrained model from the API, see
        `startDeployPretrainedModelJob`.

        This will transform raw image data (e.g. RGB to grayscale, resize)
        before classifying.

        To classify raw features, see `testPretrainedModel`.
      operationId: testPretrainedModelImages
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TestPretrainedModelImagesRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TestPretrainedModelResponse'
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
    TestPretrainedModelImagesRequest:
      type: object
      required:
        - imageFileBase64
        - input
        - model
      properties:
        imageFileBase64:
          description: A base64 encoded input image file
          type: string
        input:
          type: object
          required:
            - resizeMode
            - inputScaling
          properties:
            resizeMode:
              $ref: '#/components/schemas/ImageInputResizeMode'
            inputScaling:
              $ref: '#/components/schemas/ImageInputScaling'
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
    TestPretrainedModelResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          properties:
            result:
              type: object
              description: >-
                Classification value per label. For a neural network this will
                be the confidence, for anomalies the anomaly score.
              additionalProperties:
                type: number
            boundingBoxes:
              type: array
              items:
                $ref: '#/components/schemas/BoundingBoxWithScore'
            freeformResult:
              type: object
              required:
                - outputTensors
              properties:
                outputTensors:
                  type: array
                  items:
                    type: object
                    required:
                      - shape
                      - dataType
                      - data
                    properties:
                      shape:
                        type: array
                        items:
                          type: integer
                      dataType:
                        type: string
                        enum:
                          - int8
                          - uint8
                          - float32
                      data:
                        type: array
                        items:
                          type: number
            anomalyResult:
              type: array
              description: >-
                Anomaly scores and computed metrics for visual anomaly
                detection, one item per window.
              items:
                $ref: '#/components/schemas/AnomalyResult'
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