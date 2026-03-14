# Source: https://docs.edgeimpulse.com/apis/studio/performancecalibration/get-ground-truth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get ground truth

> Get performance calibration ground truth data



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/performance-calibration/ground-truth
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
  /api/{projectId}/performance-calibration/ground-truth:
    get:
      tags:
        - PerformanceCalibration
      summary: Get ground truth
      description: Get performance calibration ground truth data
      operationId: getPerformanceCalibrationGroundTruth
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/GetPerformanceCalibrationGroundTruthResponse
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
    GetPerformanceCalibrationGroundTruthResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - samples
          properties:
            samples:
              type: array
              items:
                $ref: '#/components/schemas/PerformanceCalibrationGroundTruth'
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
    PerformanceCalibrationGroundTruth:
      type: object
      required:
        - type
        - labelIdx
        - labelString
        - start
        - length
      properties:
        type:
          type: string
          description: >-
            Whether this region is a single sample, a region of background
            noise, or a region of background noise that contains samples.
          enum:
            - sample
            - noise
            - combined_noise
        labelIdx:
          type: integer
          description: Index of the label in the array of all labels
        labelString:
          type: string
          description: String label of the sample
        start:
          type: integer
          description: The start time of the region in milliseconds
        length:
          type: integer
          description: The length of the region in milliseconds
        samples:
          type: array
          description: If the region contains samples, all the samples within this region
          items:
            type: object
            required:
              - id
              - start
              - length
              - idx
            properties:
              id:
                type: integer
                description: The ID of the samples in Studio
              start:
                type: number
                description: The start time of the sample in milliseconds
              length:
                type: number
                description: The length of the sample in milliseconds
              idx:
                type: integer
                description: >-
                  For debugging. The index of the sample in the original Y
                  array.
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