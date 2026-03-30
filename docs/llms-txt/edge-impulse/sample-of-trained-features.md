# Source: https://docs.edgeimpulse.com/apis/studio/dsp/sample-of-trained-features.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sample of trained features

> Get a sample of trained features, this extracts a number of samples and their labels. Used to visualize the current training set.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/dsp/{dspId}/features/get-graph/{category}
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
  /api/{projectId}/dsp/{dspId}/features/get-graph/{category}:
    get:
      tags:
        - DSP
      summary: Sample of trained features
      description: >-
        Get a sample of trained features, this extracts a number of samples and
        their labels. Used to visualize the current training set.
      operationId: dspSampleTrainedFeatures
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/DspIdParameter'
        - $ref: '#/components/parameters/FeatureAx1Parameter'
        - $ref: '#/components/parameters/FeatureAx2Parameter'
        - $ref: '#/components/parameters/FeatureAx3Parameter'
        - $ref: '#/components/parameters/RawDataCategoryParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DspTrainedFeaturesResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    DspIdParameter:
      name: dspId
      in: path
      required: true
      description: DSP Block ID, use the impulse functions to retrieve the ID
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
    FeatureAx3Parameter:
      name: featureAx3
      in: query
      required: true
      description: Feature axis 3
      schema:
        type: integer
    RawDataCategoryParameter:
      name: category
      in: path
      required: true
      description: Which of the three acquisition categories to download data from
      schema:
        $ref: '#/components/schemas/RawDataCategory'
  schemas:
    DspTrainedFeaturesResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - totalSampleCount
            - data
            - skipFirstFeatures
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
                  - 'y'
                  - yLabel
                properties:
                  X:
                    type: object
                    description: Data by feature index for this window
                    example: '`{ 0: 9.81, 11: 0.32, 22: 0.79 }`'
                    additionalProperties:
                      type: number
                  'y':
                    type: integer
                    description: Training label index
                  yLabel:
                    type: string
                    description: Training label string
                  structuredYLabel:
                    type: object
                    additionalProperties:
                      type: string
                    description: >-
                      All key/value label pairs for samples with multiple labels
                      (i.e. label map datasets).
                  sample:
                    type: object
                    required:
                      - id
                      - name
                      - startMs
                      - endMs
                    properties:
                      id:
                        type: number
                      name:
                        type: string
                      startMs:
                        type: number
                      endMs:
                        type: number
            skipFirstFeatures:
              type: integer
              description: >-
                When showing the processed features, skip the first X features.
                This is used in dimensionality reduction where artificial
                features are introduced in the response (on the first few
                positions).
    RawDataCategory:
      type: string
      enum:
        - training
        - testing
        - post-processing
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