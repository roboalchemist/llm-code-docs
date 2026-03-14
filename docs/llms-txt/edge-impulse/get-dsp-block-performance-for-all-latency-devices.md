# Source: https://docs.edgeimpulse.com/apis/studio/dsp/get-dsp-block-performance-for-all-latency-devices.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get DSP block performance for all latency devices

> Get estimated performance (latency and RAM) for the DSP block, for all supported project latency devices.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/dsp/{dspId}/performance
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
  /api/{projectId}/dsp/{dspId}/performance:
    get:
      tags:
        - DSP
      summary: Get DSP block performance for all latency devices
      description: >-
        Get estimated performance (latency and RAM) for the DSP block, for all
        supported project latency devices.
      operationId: getPerformanceAllVariants
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/DspIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DspPerformanceAllVariantsResponse'
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
  schemas:
    DspPerformanceAllVariantsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          properties:
            performance:
              type: array
              description: List of performance estimates for each supported MCU.
              items:
                type: object
                required:
                  - mcu
                  - latency
                  - ram
                properties:
                  mcu:
                    type: string
                  latency:
                    type: integer
                    description: Latency estimate, in ms
                  ram:
                    type: integer
                    description: RAM estimate, in bytes
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