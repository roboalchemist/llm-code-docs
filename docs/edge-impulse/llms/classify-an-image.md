# Source: https://docs.edgeimpulse.com/apis/studio/classify/classify-an-image.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Classify an image

> Test out a trained impulse (using a posted image).



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/classify/image
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
  /api/{projectId}/classify/image:
    post:
      tags:
        - Classify
      summary: Classify an image
      description: Test out a trained impulse (using a posted image).
      operationId: classifyImage
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/UploadImageRequest'
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
    UploadImageRequest:
      type: object
      required:
        - image
      properties:
        image:
          type: string
          format: binary
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