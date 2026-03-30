# Source: https://docs.edgeimpulse.com/apis/studio/raw-data/get-project-sample-metadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get project sample metadata

> Get metadata for all samples in a project.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/raw-data/metadata
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
  /api/{projectId}/raw-data/metadata:
    get:
      tags:
        - Raw data
      summary: Get project sample metadata
      description: Get metadata for all samples in a project.
      operationId: getSampleMetadata
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/RawDataCategoryQueryParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetSampleMetadataResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    RawDataCategoryQueryParameter:
      name: category
      in: query
      required: true
      description: Which of the three acquisition categories to retrieve data from
      schema:
        $ref: '#/components/schemas/RawDataFilterCategory'
  schemas:
    GetSampleMetadataResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - $ref: '#/components/schemas/ProjectSampleMetadata'
    RawDataFilterCategory:
      type: string
      enum:
        - training
        - testing
        - post-processing
        - all
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
    ProjectSampleMetadata:
      type: object
      description: Project sample metadata
      required:
        - metadata
      properties:
        metadata:
          type: array
          description: Array with all available sample metadata.
          items:
            $ref: '#/components/schemas/SampleMetadata'
    SampleMetadata:
      type: object
      required:
        - id
        - metadata
      properties:
        id:
          type: integer
          description: Sample ID
        metadata:
          type: object
          description: Sample free form associated metadata
          additionalProperties:
            type: string
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