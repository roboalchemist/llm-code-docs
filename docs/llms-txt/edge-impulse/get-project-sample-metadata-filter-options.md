# Source: https://docs.edgeimpulse.com/apis/studio/raw-data/get-project-sample-metadata-filter-options.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get project sample metadata filter options

> Get a list of unique key value pairs across all samples in a project that can be applied as filters to the /api/{projectId}/raw-data endpoint



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/raw-data/metadata-filter-options
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
  /api/{projectId}/raw-data/metadata-filter-options:
    get:
      tags:
        - Raw data
      summary: Get project sample metadata filter options
      description: >-
        Get a list of unique key value pairs across all samples in a project
        that can be applied as filters to the /api/{projectId}/raw-data endpoint
      operationId: getSampleMetadataFilterOptions
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/RawDataCategoryQueryParameter'
        - $ref: '#/components/parameters/LimitResultsParameter'
        - $ref: '#/components/parameters/OffsetResultsParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetSampleMetadataFilterOptionsResponse'
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
    LimitResultsParameter:
      name: limit
      in: query
      required: false
      description: Maximum number of results
      schema:
        type: integer
    OffsetResultsParameter:
      name: offset
      in: query
      required: false
      description: >-
        Offset in results, can be used in conjunction with LimitResultsParameter
        to implement paging.
      schema:
        type: integer
  schemas:
    GetSampleMetadataFilterOptionsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - $ref: '#/components/schemas/MetadataFilterOptions'
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
    MetadataFilterOptions:
      type: object
      required:
        - totalCount
        - count
        - optionsList
      properties:
        totalCount:
          type: integer
        count:
          type: integer
        optionsList:
          type: array
          description: >-
            Available metadata filter options that can be supplied to the
            /raw-data/ endpoint to filter samples
          items:
            type: object
            required:
              - key
              - options
            properties:
              key:
                example: locationId
                type: string
              options:
                type: array
                example:
                  - buildingA
                  - buildingB
                items:
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