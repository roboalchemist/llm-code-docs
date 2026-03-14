# Source: https://docs.edgeimpulse.com/apis/studio/raw-data/get-data-explorer-predictions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get data explorer predictions

> Predictions for every data explorer point (only available when using current impulse to populate data explorer)



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/raw-data/data-explorer/predictions
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
  /api/{projectId}/raw-data/data-explorer/predictions:
    get:
      tags:
        - Raw data
      summary: Get data explorer predictions
      description: >-
        Predictions for every data explorer point (only available when using
        current impulse to populate data explorer)
      operationId: getDataExplorerPredictions
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DataExplorerPredictionsResponse'
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
    DataExplorerPredictionsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - predictions
            - labels
            - classificationType
          properties:
            predictions:
              type: array
              items:
                $ref: '#/components/schemas/ModelPrediction'
            labels:
              type: array
              items:
                type: string
            classificationType:
              type: string
              enum:
                - classification
                - regression
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