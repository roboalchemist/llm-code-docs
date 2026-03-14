# Source: https://docs.edgeimpulse.com/apis/studio/performancecalibration/save-performance-calibration-parameters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Save performance calibration parameters

> Set the current performance calibration parameters



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/performance-calibration/parameters
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
  /api/{projectId}/performance-calibration/parameters:
    post:
      tags:
        - PerformanceCalibration
      summary: Save performance calibration parameters
      description: Set the current performance calibration parameters
      operationId: setPerformanceCalibrationSavedParameters
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/PerformanceCalibrationSaveParameterSetRequest
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
    PerformanceCalibrationSaveParameterSetRequest:
      type: object
      required:
        - params
      properties:
        params:
          $ref: '#/components/schemas/PerformanceCalibrationParameters'
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
    PerformanceCalibrationParameters:
      type: object
      required:
        - type
        - version
      properties:
        type:
          type: string
          description: The post-processing algorithm type.
          enum:
            - standard
        version:
          type: integer
          description: The version number of the post-processing algorithm.
          example: 1
        parametersStandard:
          $ref: '#/components/schemas/PerformanceCalibrationParametersStandard'
    PerformanceCalibrationParametersStandard:
      type: object
      required:
        - averageWindowDurationMs
        - detectionThreshold
        - suppressionMs
      properties:
        averageWindowDurationMs:
          type: number
          description: The length of the averaging window in milliseconds.
          example: 1000
        detectionThreshold:
          type: number
          description: The minimum threshold for detection, from 0-1.
          example: 0.8
        suppressionMs:
          type: number
          description: >-
            The amount of time new matches will be ignored after a positive
            result.
          example: 500
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