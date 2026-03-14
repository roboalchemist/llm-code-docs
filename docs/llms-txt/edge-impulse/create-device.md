# Source: https://docs.edgeimpulse.com/apis/studio/devices/create-device.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create device

> Create a new device. If you set `ifNotExists` to `false` and the device already exists, the `deviceType` will be overwritten.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/devices/create
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
  /api/{projectId}/devices/create:
    post:
      tags:
        - Devices
      summary: Create device
      description: >-
        Create a new device. If you set `ifNotExists` to `false` and the device
        already exists, the `deviceType` will be overwritten.
      operationId: createDevice
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateDeviceRequest'
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
  schemas:
    CreateDeviceRequest:
      type: object
      required:
        - deviceId
        - deviceType
        - ifNotExists
      properties:
        deviceId:
          type: string
          description: Globally unique device identifier (e.g. MAC address)
          example: ac:87:a3:0a:2d:1b
        deviceType:
          type: string
          description: >-
            Device type, for example the exact model of the device. Should be
            the same for all similar devices
          example: DISCO_L475VG_IOT01A
        ifNotExists:
          type: boolean
          description: Whether to throw an error when this device already exists.
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