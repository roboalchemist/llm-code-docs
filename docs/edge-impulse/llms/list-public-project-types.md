# Source: https://docs.edgeimpulse.com/apis/studio/projects/list-public-project-types.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List public project types

> Retrieve the list of available public project types. You don't need any authentication for this method.



## OpenAPI

````yaml .assets/openapi.yaml get /api/projects/types
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
  /api/projects/types:
    get:
      tags:
        - Projects
      summary: List public project types
      description: >-
        Retrieve the list of available public project types. You don't need any
        authentication for this method.
      operationId: listPublicProjectTypes
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListPublicProjectTypesResponse'
      security: []
components:
  schemas:
    ListPublicProjectTypesResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - $ref: '#/components/schemas/ListPublicProjectTypes'
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
    ListPublicProjectTypes:
      type: object
      required:
        - projectTypes
      properties:
        projectTypes:
          type: array
          description: Array with project types
          items:
            type: object
            required:
              - value
              - label
            properties:
              value:
                $ref: '#/components/schemas/ProjectType'
              label:
                type: string
    ProjectType:
      type: string
      enum:
        - kws
        - audio
        - object-detection
        - image
        - accelerometer
        - other
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