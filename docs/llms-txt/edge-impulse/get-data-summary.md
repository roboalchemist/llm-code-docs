# Source: https://docs.edgeimpulse.com/apis/studio/projects/get-data-summary.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get data summary

> Get summary of all data present in the training set. This returns the number of data items, the total length of all data, and the labels. This is similar to `dataSummary` in `ProjectInfoResponse` but allows you to exclude disabled items or items that are still processing.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/data-summary
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
  /api/{projectId}/data-summary:
    get:
      tags:
        - Projects
      summary: Get data summary
      description: >-
        Get summary of all data present in the training set. This returns the
        number of data items, the total length of all data, and the labels. This
        is similar to `dataSummary` in `ProjectInfoResponse` but allows you to
        exclude disabled items or items that are still processing.
      operationId: getProjectTrainingDataSummary
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/IncludeDisabledParameter'
        - $ref: '#/components/parameters/IncludeNotProcessedParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProjectTrainingDataSummaryResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    IncludeDisabledParameter:
      name: includeDisabled
      in: query
      required: false
      description: Whether to include disabled samples. Defaults to true
      schema:
        type: boolean
    IncludeNotProcessedParameter:
      name: includeNotProcessed
      in: query
      required: false
      description: Whether to include non-processed samples. Defaults to true
      schema:
        type: boolean
  schemas:
    ProjectTrainingDataSummaryResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - dataSummary
          properties:
            dataSummary:
              type: object
              required:
                - labels
                - dataCount
                - hasTimeseriesDataWithMultipleLabels
              properties:
                labels:
                  type: array
                  description: Labels in the training set
                  items:
                    type: string
                dataCount:
                  type: integer
                  example: Number of files in the training set
                hasTimeseriesDataWithMultipleLabels:
                  type: boolean
                  description: >-
                    Whether there are samples in the training dataset that are
                    both time-series data and have multiple labels
                labelsPerKey:
                  description: >-
                    For labelmap datasets, this property provides a breakdown of
                    labels per attribute or key.
                  type: object
                  additionalProperties:
                    type: array
                    items:
                      type: string
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