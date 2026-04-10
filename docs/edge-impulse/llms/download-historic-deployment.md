# Source: https://docs.edgeimpulse.com/apis/studio/deployment/download-historic-deployment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Download historic deployment

> Download a previously built deployment (use listDeploymentHistory to see all deployments).



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/deployment/history/{deploymentVersion}/download
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
  /api/{projectId}/deployment/history/{deploymentVersion}/download:
    get:
      tags:
        - Deployment
      summary: Download historic deployment
      description: >-
        Download a previously built deployment (use listDeploymentHistory to see
        all deployments).
      operationId: downloadHistoricDeployment
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/DeploymentVersionParameter'
      responses:
        '200':
          description: ZIP or BIN file
          content:
            application/zip:
              schema:
                type: string
                format: binary
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    DeploymentVersionParameter:
      name: deploymentVersion
      in: path
      required: true
      description: Deployment version ID
      schema:
        type: integer
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