# Source: https://docs.edgeimpulse.com/apis/studio/optimization/retrieves-dsp-block-parameters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieves DSP block parameters

> Retrieves DSP block parameters



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/optimize/dsp-parameters
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
  /api/{projectId}/optimize/dsp-parameters:
    get:
      tags:
        - Optimization
      summary: Retrieves DSP block parameters
      description: Retrieves DSP block parameters
      operationId: getDspParameters
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/OptimizeOrganizationIdParameter'
        - $ref: '#/components/parameters/OptimizeOrganizationDspIdParameter'
      responses:
        '200':
          description: DSP parameters
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OptimizeDSPParametersResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    OptimizeOrganizationIdParameter:
      name: organizationId
      in: query
      required: true
      description: Organization ID
      schema:
        type: integer
    OptimizeOrganizationDspIdParameter:
      name: organizationDspId
      in: query
      required: true
      description: Organization DSP ID
      schema:
        type: integer
  schemas:
    OptimizeDSPParametersResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - parameters
          properties:
            parameters:
              type: object
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