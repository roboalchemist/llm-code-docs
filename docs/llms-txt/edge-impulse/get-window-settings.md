# Source: https://docs.edgeimpulse.com/apis/studio/optimization/get-window-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get window settings

> Get window settings



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/optimize/window-settings
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
  /api/{projectId}/optimize/window-settings:
    get:
      tags:
        - Optimization
      summary: Get window settings
      description: Get window settings
      operationId: getWindowSettings
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WindowSettingsResponse'
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
    WindowSettingsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - windowSettingsEvent
            - windowSettingsContinuous
          properties:
            windowSettingsEvent:
              type: array
              items:
                $ref: '#/components/schemas/WindowSettings'
            windowSettingsContinuous:
              type: array
              items:
                $ref: '#/components/schemas/WindowSettings'
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
    WindowSettings:
      type: object
      required:
        - windowSizeMs
        - windowIncreaseMs
        - windowIncreasePct
        - zeroPadPercentage
        - windowCount
        - balanceScore
        - valid
      properties:
        windowSizeMs:
          type: number
        windowIncreaseMs:
          type: number
        windowIncreasePct:
          type: number
        zeroPadPercentage:
          type: number
        windowCount:
          type: integer
        balanceScore:
          type: number
        valid:
          type: boolean
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