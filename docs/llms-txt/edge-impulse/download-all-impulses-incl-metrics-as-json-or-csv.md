# Source: https://docs.edgeimpulse.com/apis/studio/impulse/download-all-impulses-incl-metrics-as-json-or-csv.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Download all impulses (incl. metrics), as JSON or CSV.

> Download all impulse for a project, including accuracy and performance metrics, as JSON or CSV.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/download-impulses-detailed
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
  /api/{projectId}/download-impulses-detailed:
    get:
      tags:
        - Impulse
      summary: Download all impulses (incl. metrics), as JSON or CSV.
      description: >-
        Download all impulse for a project, including accuracy and performance
        metrics, as JSON or CSV.
      operationId: downloadDetailedImpulses
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/DetailedImpulsesFormatParameter'
      responses:
        '200':
          description: File
          content:
            application/octet-stream:
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
    DetailedImpulsesFormatParameter:
      name: format
      in: query
      required: false
      description: >-
        Format of the detailed impulses response, either 'json' or 'csv'. If not
        set, defaults to 'json'.
      schema:
        type: string
        enum:
          - json
          - csv
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