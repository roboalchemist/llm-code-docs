# Source: https://docs.edgeimpulse.com/apis/studio/raw-data/set-data-explorer-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set data explorer settings

> Set data explorer configuration, like the type of data, and the input / dsp block to use.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/raw-data/data-explorer/settings
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
  /api/{projectId}/raw-data/data-explorer/settings:
    post:
      tags:
        - Raw data
      summary: Set data explorer settings
      description: >-
        Set data explorer configuration, like the type of data, and the input /
        dsp block to use.
      operationId: setDataExplorerSettings
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DataExplorerSettings'
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
    DataExplorerSettings:
      type: object
      properties:
        preset:
          description: Preset to use for the data explorer.
          type: string
          enum:
            - keywords
            - images
            - current-impulse
            - current-impulse-embeddings
        dimensionalityReductionTechnique:
          type: string
          enum:
            - tsne
            - pca
        impulseId:
          type: integer
          description: >-
            Which impulse to use (if preset is either 'current-impulse' or
            'current-impulse-embeddings'). If this is undefined then
            'defaultImpulseId' is used.
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