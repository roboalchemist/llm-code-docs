# Source: https://docs.edgeimpulse.com/apis/studio/learn/anomaly-gmm-metadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Anomaly GMM metadata

> Get raw model metadata of the Gaussian mixture model (GMM) for a trained anomaly block. Use the impulse blocks to find the learnId.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/training/anomaly/{learnId}/gmm/metadata
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
  /api/{projectId}/training/anomaly/{learnId}/gmm/metadata:
    get:
      tags:
        - Learn
      summary: Anomaly GMM metadata
      description: >-
        Get raw model metadata of the Gaussian mixture model (GMM) for a trained
        anomaly block. Use the impulse blocks to find the learnId.
      operationId: getGmmMetadata
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/LearnIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AnomalyGmmMetadataResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    LearnIdParameter:
      name: learnId
      in: path
      required: true
      description: Learn Block ID, use the impulse functions to retrieve the ID
      schema:
        type: integer
  schemas:
    AnomalyGmmMetadataResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - $ref: '#/components/schemas/AnomalyGmmMetadata'
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
    AnomalyGmmMetadata:
      type: object
      required:
        - means
        - covariances
        - weights
      properties:
        means:
          type: array
          items:
            type: array
            items:
              type: number
          description: 2D array of shape (n, m)
        covariances:
          type: array
          items:
            type: array
            items:
              type: array
              items:
                type: number
          description: 3D array of shape (n, m, m)
        weights:
          type: array
          items:
            type: number
          description: 1D array of shape (n,)
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