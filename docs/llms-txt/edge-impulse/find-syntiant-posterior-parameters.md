# Source: https://docs.edgeimpulse.com/apis/studio/deployment/find-syntiant-posterior-parameters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Find Syntiant posterior parameters

> Automatically find the current posterior parameters for the Syntiant deployment target



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/jobs/find-syntiant-posterior
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
  /api/{projectId}/jobs/find-syntiant-posterior:
    post:
      tags:
        - Deployment
      summary: Find Syntiant posterior parameters
      description: >-
        Automatically find the current posterior parameters for the Syntiant
        deployment target
      operationId: findSyntiantPosterior
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/FindSyntiantPosteriorRequest'
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
    FindSyntiantPosteriorRequest:
      type: object
      required:
        - targetWords
        - referenceSet
      properties:
        targetWords:
          type: array
          items:
            type: string
        referenceSet:
          type: string
          enum:
            - 600_seconds
            - full
            - custom
            - no_calibration
        wavFile:
          type: string
          format: binary
        metaCsvFile:
          type: string
          format: binary
        deploymentTarget:
          type: string
          enum:
            - syntiant-ndp101
            - syntiant-ndp101-lib
            - syntiant-ndp120-lib
            - syntiant-ndp120-lib-tdk-v14
            - syntiant-nicla-ndp120
            - syntiant-avnet-rasyn
            - syntiant-ndp120-lib-ndp-v1-15-0
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