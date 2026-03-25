# Source: https://docs.edgeimpulse.com/apis/studio/optimization/list-all-tuner-runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List all tuner runs

> List all the tuner runs for a project.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/optimize/runs
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
  /api/{projectId}/optimize/runs:
    get:
      tags:
        - Optimization
      summary: List all tuner runs
      description: List all the tuner runs for a project.
      operationId: listTunerRuns
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListTunerRunsResponse'
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
    ListTunerRunsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - runs
          properties:
            runs:
              type: array
              items:
                $ref: '#/components/schemas/TunerRun'
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
    TunerRun:
      type: object
      required:
        - tunerJobId
        - tunerCoordinatorJobId
        - index
        - created
        - jobStatus
        - visible
      properties:
        tunerJobId:
          type: integer
        tunerCoordinatorJobId:
          type: integer
        index:
          type: integer
        name:
          type: string
        created:
          type: string
          format: date-time
        jobStatus:
          $ref: '#/components/schemas/JobStatus'
        continuationJobId:
          type: integer
        space:
          type: array
          description: List of impulses specifying the EON Tuner search space
          items:
            $ref: '#/components/schemas/TunerSpaceImpulse'
        visible:
          type: boolean
          description: Whether the run is visible in the UI
    JobStatus:
      type: string
      enum:
        - cancelled
        - creating
        - failed
        - pending
        - running
        - success
    TunerSpaceImpulse:
      type: object
      required:
        - inputBlocks
        - dspBlocks
        - learnBlocks
      properties:
        parameters:
          type: object
          description: >-
            Hyperparameters with potential values that can be used in any block
            in this impulse
        inputBlocks:
          type: array
          description: Input Blocks that are part of this impulse
          items:
            $ref: '#/components/schemas/TunerSpaceInputBlock'
        dspBlocks:
          type: array
          description: DSP Blocks that are part of this impulse
          items:
            $ref: '#/components/schemas/TunerSpaceDSPBlock'
        learnBlocks:
          type: array
          description: Learning Blocks that are part of this impulse
          items:
            type: array
            items:
              $ref: '#/components/schemas/TunerSpaceLearnBlock'
    TunerSpaceInputBlock:
      type: object
      additionalProperties: true
    TunerSpaceDSPBlock:
      type: object
      additionalProperties: true
    TunerSpaceLearnBlock:
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