# Source: https://docs.edgeimpulse.com/apis/studio/jobs/post-processing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Post-processing

> Begins post processing job



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/jobs/post-processing
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
  /api/{projectId}/jobs/post-processing:
    post:
      tags:
        - Jobs
      summary: Post-processing
      description: Begins post processing job
      operationId: startPostProcessingJob
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/StartPostProcessingRequest'
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
    OptionalImpulseIdParameter:
      name: impulseId
      in: query
      required: false
      description: Impulse ID. If this is unset then the default impulse is used.
      schema:
        type: integer
  schemas:
    StartPostProcessingRequest:
      type: object
      required:
        - variant
        - dataset
        - algorithm
        - evaluation
      properties:
        variant:
          $ref: '#/components/schemas/KerasModelVariantEnum'
          description: Which model variant to use (int8, float32, etc.)
        dataset:
          description: Which dataset to use
          type: string
          enum:
            - training
            - validation
            - testing
        algorithm:
          description: Which algorithm container to use
          type: string
        evaluation:
          description: Which evaluation container to use
          type: string
        population:
          description: The population size for the genetic algorithm
          type: integer
          default: 100
        maxGenerations:
          description: The maximum number of generations for the genetic algorithm
          type: integer
          default: 100
        designSpaceTolerance:
          description: The tolerance for the design space
          type: number
          default: 0.01
        objectiveSpaceTolerance:
          description: The tolerance for the objective space
          type: number
          default: 0.0025
        terminationPeriod:
          description: >-
            The number of generations the termination criteria are averaged
            across
          type: integer
          default: 5
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
    KerasModelVariantEnum:
      type: string
      enum:
        - int8
        - float32
        - akida
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