# Source: https://docs.edgeimpulse.com/apis/studio/impulse/verify-custom-dsp-block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Verify custom DSP block

> Verify the validity of a custom DSP block



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/verify-dsp-block/url
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
  /api/{projectId}/verify-dsp-block/url:
    post:
      tags:
        - Impulse
      summary: Verify custom DSP block
      description: Verify the validity of a custom DSP block
      operationId: verifyDspBlockUrl
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/VerifyDspBlockUrlRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VerifyDspBlockUrlResponse'
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
    VerifyDspBlockUrlRequest:
      type: object
      required:
        - url
      properties:
        url:
          type: string
    VerifyDspBlockUrlResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          properties:
            block:
              type: object
              required:
                - title
                - author
                - description
                - name
                - latestImplementationVersion
              properties:
                title:
                  type: string
                author:
                  type: string
                description:
                  type: string
                name:
                  type: string
                latestImplementationVersion:
                  type: integer
                namedAxes:
                  type: array
                  items:
                    $ref: '#/components/schemas/DSPNamedAxis'
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
    DSPNamedAxis:
      type: object
      required:
        - name
        - description
        - required
      properties:
        name:
          type: string
        description:
          type: string
        required:
          type: boolean
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