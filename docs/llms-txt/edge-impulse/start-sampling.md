# Source: https://docs.edgeimpulse.com/apis/studio/devices/start-sampling.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Start sampling

> Start sampling on a device. This function returns immediately. Updates are streamed through the websocket API.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/device/{deviceId}/start-sampling
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
  /api/{projectId}/device/{deviceId}/start-sampling:
    post:
      tags:
        - Devices
      summary: Start sampling
      description: >-
        Start sampling on a device. This function returns immediately. Updates
        are streamed through the websocket API.
      operationId: startSampling
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/DeviceIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/StartSamplingRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StartSamplingResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    DeviceIdParameter:
      name: deviceId
      in: path
      required: true
      description: Device ID
      schema:
        type: string
  schemas:
    StartSamplingRequest:
      type: object
      required:
        - label
        - lengthMs
        - category
        - intervalMs
      properties:
        label:
          type: string
          description: Label to be used during sampling.
        lengthMs:
          type: integer
          description: Requested length of the sample (in ms).
        category:
          $ref: '#/components/schemas/RawDataCategory'
          description: Which acquisition category to sample data into.
        intervalMs:
          type: number
          description: Interval between samples (can be calculated like `1/hz * 1000`)
        sensor:
          type: string
          description: The sensor to sample from.
        labelColor:
          type: string
          description: >-
            Text color of label displayed on supported clients. Value can be any
            supported CSS color value
        collectedSampleCount:
          type: number
          description: >-
            A hint to supported clients to show the number of samples currently
            collected
        targetSampleCount:
          type: number
          description: >-
            A hint to supported clients to show the desired number of samples to
            be collected
    StartSamplingResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          properties:
            id:
              type: integer
    RawDataCategory:
      type: string
      enum:
        - training
        - testing
        - post-processing
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