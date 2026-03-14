# Source: https://docs.edgeimpulse.com/apis/studio/learn/trained-features.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Trained features

> Get a sample of trained features, this extracts a number of samples and their features.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/training/anomaly/{learnId}/features/get-graph
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
  /api/{projectId}/training/anomaly/{learnId}/features/get-graph:
    get:
      tags:
        - Learn
      summary: Trained features
      description: >-
        Get a sample of trained features, this extracts a number of samples and
        their features.
      operationId: anomalyTrainedFeatures
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/LearnIdParameter'
        - $ref: '#/components/parameters/FeatureAx1Parameter'
        - $ref: '#/components/parameters/FeatureAx2Parameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AnomalyTrainedFeaturesResponse'
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
    FeatureAx1Parameter:
      name: featureAx1
      in: query
      required: true
      description: Feature axis 1
      schema:
        type: integer
    FeatureAx2Parameter:
      name: featureAx2
      in: query
      required: true
      description: Feature axis 2
      schema:
        type: integer
  schemas:
    AnomalyTrainedFeaturesResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - totalSampleCount
            - data
          properties:
            totalSampleCount:
              type: integer
              description: Total number of windows in the data set
            data:
              type: array
              items:
                type: object
                required:
                  - X
                properties:
                  X:
                    type: object
                    description: >-
                      Data by feature index for this window. Note that this data
                      was scaled by the StandardScaler, use the anomaly metadata
                      to unscale if needed.
                    example:
                      '0': -2.17
                      '11': 1.21
                      '22': 0.79
                    additionalProperties:
                      type: number
                  label:
                    type: number
                    description: >-
                      Label used for datapoint colorscale in anomaly explorer
                      (for gmm only). Is currently the result of the scoring
                      function.
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