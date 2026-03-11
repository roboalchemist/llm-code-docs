# Source: https://docs.edgeimpulse.com/apis/studio/performancecalibration/get-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get status

> Get performance calibration status



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/performance-calibration/status
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
  /api/{projectId}/performance-calibration/status:
    get:
      tags:
        - PerformanceCalibration
      summary: Get status
      description: Get performance calibration status
      operationId: getPerformanceCalibrationStatus
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetPerformanceCalibrationStatusResponse'
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
    GetPerformanceCalibrationStatusResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - available
          properties:
            available:
              type: boolean
            unsupportedProjectError:
              type: string
              description: >-
                If the current project is unsupported by performance
                calibration, this field explains the reason why. Otherwise, it
                is undefined.
            options:
              $ref: '#/components/schemas/StartPerformanceCalibrationRequest'
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
    StartPerformanceCalibrationRequest:
      type: object
      required:
        - backgroundNoiseLabel
      properties:
        backgroundNoiseLabel:
          type: string
          description: The label used to signify background noise in the impulse
        otherNoiseLabels:
          type: array
          items:
            type: string
          description: >-
            Any other labels that should be considered equivalent to background
            noise
        uploadKey:
          type: string
          description: >-
            The key of an uploaded sample. If not present, a synthetic sample
            will be created.
        sampleLengthMinutes:
          type: number
          description: The length of sample to create (required for synthetic samples)
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