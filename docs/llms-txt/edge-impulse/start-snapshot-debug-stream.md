# Source: https://docs.edgeimpulse.com/apis/studio/devices/start-snapshot-debug-stream.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Start snapshot debug stream

> Start a snapshot debug stream for this device with a current camera view. Updates are streamed through the websocket API. A keep-alive token is returned, you'll need to ping the API (with keepDeviceDebugStreamAlive) every 10 seconds (so we know when the client is disconnected).



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/device/{deviceId}/debug-stream/snapshot/start
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
  /api/{projectId}/device/{deviceId}/debug-stream/snapshot/start:
    post:
      tags:
        - Devices
      summary: Start snapshot debug stream
      description: >-
        Start a snapshot debug stream for this device with a current camera
        view. Updates are streamed through the websocket API. A keep-alive token
        is returned, you'll need to ping the API (with
        keepDeviceDebugStreamAlive) every 10 seconds (so we know when the client
        is disconnected).
      operationId: startDeviceSnapshotDebugStream
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/DeviceIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/StartDeviceSnapshotDebugStreamRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StartDeviceDebugStreamResponse'
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
    StartDeviceSnapshotDebugStreamRequest:
      type: object
      required:
        - resolution
      properties:
        resolution:
          type: string
          enum:
            - high
            - low
    StartDeviceDebugStreamResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - streamId
          properties:
            streamId:
              type: integer
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