# Source: https://docs.edgeimpulse.com/apis/studio/jobs/sets-eon-tuner-primary-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sets EON tuner primary model

> Sets EON tuner primary model



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/jobs/set-tuner-primary-job
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
  /api/{projectId}/jobs/set-tuner-primary-job:
    post:
      tags:
        - Jobs
      summary: Sets EON tuner primary model
      description: Sets EON tuner primary model
      operationId: setTunerPrimaryJob
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/TrialIdQueryParameter'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SetTunerPrimaryJobRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StartJobResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    TrialIdQueryParameter:
      name: trialId
      in: query
      required: true
      description: trial ID
      schema:
        type: string
  schemas:
    SetTunerPrimaryJobRequest:
      type: object
      properties:
        name:
          type: string
          description: Optional name. If no name is provided, the trial name is used.
    StartJobResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - id
          properties:
            id:
              type: integer
              description: Job identifier. Status updates will include this identifier.
              example: 12873488112
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