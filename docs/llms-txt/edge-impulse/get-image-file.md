# Source: https://docs.edgeimpulse.com/apis/studio/raw-data/get-image-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get image file

> Get a sample as an image file. This only applies to samples with RGBA data.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/raw-data/{sampleId}/image
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
  /api/{projectId}/raw-data/{sampleId}/image:
    get:
      tags:
        - Raw data
      summary: Get image file
      description: >-
        Get a sample as an image file. This only applies to samples with RGBA
        data.
      operationId: getSampleAsImage
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/SampleIdParameter'
        - $ref: '#/components/parameters/AfterInputBlockParameter'
        - $ref: '#/components/parameters/CacheKeyParameter'
        - $ref: '#/components/parameters/OptionalImpulseIdParameter'
      responses:
        '200':
          description: Image file (either JPEG or PNG format)
          content:
            image/jpeg:
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
    SampleIdParameter:
      name: sampleId
      in: path
      required: true
      description: Sample ID
      schema:
        type: integer
    AfterInputBlockParameter:
      name: afterInputBlock
      in: query
      required: false
      description: Whether to process the image through the input block first
      schema:
        type: boolean
    CacheKeyParameter:
      name: cacheKey
      in: query
      required: false
      description: >-
        If set, then a long cache header is sent. If this is omitted then a
        no-cache header is sent. You can use this if you f.e. know the last
        modified date of a sample. Stick the last modified date in the cache
        key, so the sample can be stored in browser cache (and will
        automatically be invalidated if the modified date changes).
      schema:
        type: string
    OptionalImpulseIdParameter:
      name: impulseId
      in: query
      required: false
      description: Impulse ID. If this is unset then the default impulse is used.
      schema:
        type: integer
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