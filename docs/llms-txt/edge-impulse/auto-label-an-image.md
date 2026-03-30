# Source: https://docs.edgeimpulse.com/apis/studio/raw-data/auto-label-an-image.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Auto-label an image

> Classify an image using another neural network.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/raw-data/{sampleId}/autolabel
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
  /api/{projectId}/raw-data/{sampleId}/autolabel:
    post:
      tags:
        - Raw data
      summary: Auto-label an image
      description: Classify an image using another neural network.
      operationId: classifyUsingAutolabel
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/SampleIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ObjectDetectionAutoLabelRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ObjectDetectionAutoLabelResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    SampleIdParameter:
      name: sampleId
      in: path
      required: true
      description: Sample ID
      schema:
        type: integer
  schemas:
    ObjectDetectionAutoLabelRequest:
      type: object
      required:
        - neuralNetwork
      properties:
        neuralNetwork:
          type: string
          enum:
            - yolov5
            - yolo-pro
            - currentProject
    ObjectDetectionAutoLabelResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - results
            - allLabels
          properties:
            results:
              type: array
              items:
                type: object
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
            allLabels:
              type: array
              items:
                type: string
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