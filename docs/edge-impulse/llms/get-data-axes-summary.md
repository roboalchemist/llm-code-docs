# Source: https://docs.edgeimpulse.com/apis/studio/projects/get-data-axes-summary.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get data axes summary

> Get a list of axes that are present in the training data.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/data-axes
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
  /api/{projectId}/data-axes:
    get:
      tags:
        - Projects
      summary: Get data axes summary
      description: Get a list of axes that are present in the training data.
      operationId: getProjectDataAxesSummary
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/IncludeDisabledParameter'
        - $ref: '#/components/parameters/IncludeNotProcessedParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProjectDataAxesSummaryResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    IncludeDisabledParameter:
      name: includeDisabled
      in: query
      required: false
      description: Whether to include disabled samples. Defaults to true
      schema:
        type: boolean
    IncludeNotProcessedParameter:
      name: includeNotProcessed
      in: query
      required: false
      description: Whether to include non-processed samples. Defaults to true
      schema:
        type: boolean
  schemas:
    ProjectDataAxesSummaryResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - dataAxisSummary
          properties:
            dataAxisSummary:
              type: object
              description: Summary of the amount of data (in ms.) per sensor axis
              additionalProperties:
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