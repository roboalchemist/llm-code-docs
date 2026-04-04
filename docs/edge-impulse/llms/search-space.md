# Source: https://docs.edgeimpulse.com/studio/projects/eon-tuner/search-space.md

# Source: https://docs.edgeimpulse.com/apis/studio/optimization/search-space.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Search space

> Search space



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/optimize/space
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
  /api/{projectId}/optimize/space:
    get:
      tags:
        - Optimization
      summary: Search space
      description: Search space
      operationId: getSpace
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OptimizeSpaceResponse'
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
    OptimizeSpaceResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - impulse
          properties:
            impulse:
              type: array
              description: List of impulses specifying the EON Tuner search space
              items:
                $ref: '#/components/schemas/TunerSpaceImpulse'
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