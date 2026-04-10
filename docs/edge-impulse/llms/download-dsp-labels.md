# Source: https://docs.edgeimpulse.com/apis/studio/dsp/download-dsp-labels.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Download DSP labels

> Download labels for a DSP block over all data in the training set, already sliced in windows.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/dsp-data/{dspId}/y/{category}
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
  /api/{projectId}/dsp-data/{dspId}/y/{category}:
    get:
      tags:
        - DSP
      summary: Download DSP labels
      description: >-
        Download labels for a DSP block over all data in the training set,
        already sliced in windows.
      operationId: downloadDspLabels
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/DspIdParameter'
        - $ref: '#/components/parameters/RawDataCategoryParameter'
      responses:
        '200':
          description: Numpy binary file
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
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
    RawDataCategoryParameter:
      name: category
      in: path
      required: true
      description: Which of the three acquisition categories to download data from
      schema:
        $ref: '#/components/schemas/RawDataCategory'
  schemas:
    RawDataCategory:
      type: string
      enum:
        - training
        - testing
        - post-processing
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