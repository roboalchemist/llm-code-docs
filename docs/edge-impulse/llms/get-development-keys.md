# Source: https://docs.edgeimpulse.com/apis/studio/projects/get-development-keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get development keys

> Retrieve the development API and HMAC keys for a project. These keys are specifically marked to be used during development. These keys can be `undefined` if no development keys are set. Only available through JWT token authentication, if you authenticate with an API key then all keys will return undefined (this is changed behavior since 28 January 2026).



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/devkeys
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
  /api/{projectId}/devkeys:
    get:
      tags:
        - Projects
      summary: Get development keys
      description: >-
        Retrieve the development API and HMAC keys for a project. These keys are
        specifically marked to be used during development. These keys can be
        `undefined` if no development keys are set. Only available through JWT
        token authentication, if you authenticate with an API key then all keys
        will return undefined (this is changed behavior since 28 January 2026).
      operationId: listDevkeys
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DevelopmentKeysResponse'
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
    DevelopmentKeysResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - $ref: '#/components/schemas/DevelopmentKeys'
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
    DevelopmentKeys:
      type: object
      properties:
        apiKey:
          type: string
          description: API Key
        hmacKey:
          type: string
          description: HMAC Key
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