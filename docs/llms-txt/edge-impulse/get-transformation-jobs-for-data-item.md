# Source: https://docs.edgeimpulse.com/apis/studio/organizationdata/get-transformation-jobs-for-data-item.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get transformation jobs for data item

> Get all transformation jobs that ran for a data item. If limit / offset is not provided then max. 20 results are returned.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/data/{dataId}/transformation-jobs
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
  /api/organizations/{organizationId}/data/{dataId}/transformation-jobs:
    get:
      tags:
        - OrganizationData
      summary: Get transformation jobs for data item
      description: >-
        Get all transformation jobs that ran for a data item. If limit / offset
        is not provided then max. 20 results are returned.
      operationId: getOrganizationDataItemTransformJobs
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/OrganizationDataIdParameter'
        - $ref: '#/components/parameters/LimitResultsParameter'
        - $ref: '#/components/parameters/OffsetResultsParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/GetOrganizationDataItemTransformJobsResponse
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
    OrganizationDataIdParameter:
      name: dataId
      in: path
      required: true
      description: Data ID
      schema:
        type: integer
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
    GetOrganizationDataItemTransformJobsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - transformationJobs
            - totalTransformationJobCount
          properties:
            transformationJobs:
              type: array
              items:
                type: object
                required:
                  - id
                  - transformationJobId
                  - createProjectId
                  - created
                  - jobId
                  - transformationBlockName
                properties:
                  id:
                    type: integer
                  transformationJobId:
                    type: integer
                  createProjectId:
                    type: integer
                  created:
                    type: string
                    format: date-time
                  jobId:
                    type: integer
                  jobStarted:
                    type: string
                    format: date-time
                  jobFinished:
                    type: string
                    format: date-time
                  jobFinishedSuccessful:
                    type: boolean
                  transformationBlockName:
                    type: string
                  pipelineName:
                    type: string
            totalTransformationJobCount:
              type: integer
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