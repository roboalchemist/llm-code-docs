# Source: https://docs.edgeimpulse.com/apis/studio/dsp/features-for-sample.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Features for sample

> Runs the DSP block against a sample. This will move the sliding window (dependent on the sliding window length and the sliding window increase parameters in the impulse) over the complete file, and run the DSP function for every window that is extracted.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/dsp/{dspId}/features/get-graph/classification/{sampleId}
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
  /api/{projectId}/dsp/{dspId}/features/get-graph/classification/{sampleId}:
    get:
      tags:
        - DSP
      summary: Features for sample
      description: >-
        Runs the DSP block against a sample. This will move the sliding window
        (dependent on the sliding window length and the sliding window increase
        parameters in the impulse) over the complete file, and run the DSP
        function for every window that is extracted.
      operationId: dspGetFeaturesForSample
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/DspIdParameter'
        - $ref: '#/components/parameters/SampleIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DspSampleFeaturesResponse'
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
    SampleIdParameter:
      name: sampleId
      in: path
      required: true
      description: Sample ID
      schema:
        type: integer
  schemas:
    DspSampleFeaturesResponse:
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
                    type: array
                    description: Feature data for this window
                    example: '`{ 9.81, 0.32, 0.79 }`'
                    items:
                      type: number
                  'y':
                    type: integer
                    description: Training label index
                  yLabel:
                    type: string
                    description: Training label string
                  sample:
                    type: object
                    required:
                      - id
                      - name
                      - startMs
                      - endMs
                    properties:
                      id:
                        type: integer
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