# Source: https://docs.edgeimpulse.com/apis/studio/optimization/create-trial.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create trial

> Create trial



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/optimize/{jobId}/create-trial
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
  /api/{projectId}/optimize/{jobId}/create-trial:
    post:
      tags:
        - Optimization
      summary: Create trial
      description: Create trial
      operationId: createTrial
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/JobIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TunerCreateTrialImpulse'
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
    JobIdParameter:
      name: jobId
      in: path
      required: true
      description: Job ID
      schema:
        type: integer
  schemas:
    TunerCreateTrialImpulse:
      type: object
      required:
        - inputBlock
        - dspBlock
        - learnBlock
      properties:
        id:
          type: string
        experiment:
          type: string
        original_trial_id:
          type: string
        optimizationRound:
          type: number
        inputBlocks:
          type: array
          items:
            $ref: '#/components/schemas/TunerCreateTrialInputBlock'
        dspBlocks:
          type: array
          items:
            $ref: '#/components/schemas/TunerCreateTrialDSPBlock'
        learnBlocks:
          type: array
          items:
            $ref: '#/components/schemas/TunerCreateTrialLearnBlock'
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
    TunerCreateTrialInputBlock:
      type: object
      additionalProperties: true
    TunerCreateTrialDSPBlock:
      type: object
      additionalProperties: true
    TunerCreateTrialLearnBlock:
      type: object
      additionalProperties: true
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