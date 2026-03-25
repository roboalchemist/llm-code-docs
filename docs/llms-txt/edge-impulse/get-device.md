# Source: https://docs.edgeimpulse.com/apis/studio/devices/get-device.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get device

> Retrieves a single device



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/device/{deviceId}
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
  /api/{projectId}/device/{deviceId}:
    get:
      tags:
        - Devices
      summary: Get device
      description: Retrieves a single device
      operationId: getDevice
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/DeviceIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetDeviceResponse'
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
    GetDeviceResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          properties:
            device:
              $ref: '#/components/schemas/Device'
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
    Device:
      type: object
      required:
        - id
        - deviceId
        - created
        - lastSeen
        - name
        - deviceType
        - sensors
        - remote_mgmt_connected
        - supportsSnapshotStreaming
        - remoteMgmtMode
      properties:
        id:
          type: integer
          example: 1
        deviceId:
          type: string
          description: Unique identifier (such as MAC address) for a device
          example: 38:f9:d3:d7:62:03
        created:
          type: string
          format: date-time
          example: '2019-07-21T17:32:28Z'
        lastSeen:
          type: string
          format: date-time
          example: '2019-08-31T17:32:28Z'
          description: Last message that was received from the device (ignoring keep-alive)
        name:
          type: string
          example: m6d.1 desk sensor
        deviceType:
          type: string
          example: DISCO-L475VG
        sensors:
          type: array
          items:
            type: object
            required:
              - name
              - maxSampleLengthS
              - frequencies
            properties:
              name:
                type: string
                example: Built-in accelerometer
              maxSampleLengthS:
                type: integer
                description: Maximum supported sample length in seconds
              frequencies:
                type: array
                description: Supported frequencies for this sensor in Hz.
                example:
                  - 62.5
                  - 100
                items:
                  type: number
        remote_mgmt_connected:
          type: boolean
          description: >-
            Whether the device is connected to the remote management interface.
            This property is deprecated, use `remoteMgmtMode` instead.
        remote_mgmt_host:
          type: string
          description: The remote management host that the device is connected to
        supportsSnapshotStreaming:
          type: boolean
        remoteMgmtMode:
          description: >-
            Replaces `remote_mgmt_connected`. Shows whether the device is
            connected to the remote management interface, and in which mode.
          type: string
          enum:
            - disconnected
            - ingestion
            - inference
        inferenceInfo:
          type: object
          description: >-
            If `remoteMgmtMode` is set to `inference` this object shows
            information about the model that's ran on device.
          required:
            - projectId
            - projectOwner
            - projectName
            - deployedVersion
          properties:
            projectId:
              type: integer
            projectOwner:
              type: string
            projectName:
              type: string
            deployedVersion:
              type: integer
            modelType:
              type: string
              enum:
                - classification
                - objectDetection
                - constrainedObjectDetection
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