# Source: https://docs.edgeimpulse.com/apis/studio/organizationcreateproject/list-transformation-jobs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List transformation jobs

> Get list of transformation jobs.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/create-project
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
  /api/organizations/{organizationId}/create-project:
    get:
      tags:
        - OrganizationCreateProject
      summary: List transformation jobs
      description: Get list of transformation jobs.
      operationId: getOrganizationCreateProjects
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/LimitResultsParameter'
        - $ref: '#/components/parameters/OffsetResultsParameter'
        - $ref: '#/components/parameters/IncludePipelineJobsParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrganizationGetCreateProjectsResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
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
    IncludePipelineJobsParameter:
      name: includePipelineJobs
      in: query
      required: false
      description: If enabled, also includes jobs that are part of a pipeline
      schema:
        type: boolean
  schemas:
    OrganizationGetCreateProjectsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - jobs
            - totalJobCount
          properties:
            totalJobCount:
              type: integer
            jobs:
              type: array
              items:
                type: object
                required:
                  - id
                  - name
                  - transformJobStatus
                  - uploadJobStatus
                  - uploadType
                  - category
                  - created
                  - totalDownloadFileCount
                  - totalDownloadFileSize
                  - totalDownloadFileSizeString
                  - totalTimeSpentString
                properties:
                  id:
                    type: integer
                  organizationId:
                    type: integer
                  name:
                    type: string
                  uploadType:
                    type: string
                    enum:
                      - dataset
                      - project
                  transformJobStatus:
                    $ref: '#/components/schemas/TransformationJobStatusEnum'
                  uploadJobId:
                    type: integer
                  uploadJobStatus:
                    $ref: '#/components/schemas/TransformationJobStatusEnum'
                  projectOwner:
                    type: string
                  projectId:
                    type: integer
                  projectName:
                    type: string
                  transformationBlockId:
                    type: integer
                  builtinTransformationBlock:
                    type: object
                  transformationBlockName:
                    type: string
                  transformationOperatesOn:
                    $ref: '#/components/schemas/TransformationJobOperatesOnEnum'
                  created:
                    type: string
                    format: date-time
                  outputDatasetName:
                    type: string
                  outputDatasetBucketId:
                    type: integer
                  outputDatasetBucketPath:
                    type: string
                  totalDownloadFileCount:
                    type: integer
                  totalDownloadFileSize:
                    type: integer
                  totalDownloadFileSizeString:
                    type: string
                  totalUploadFileCount:
                    type: integer
                  totalTimeSpentSeconds:
                    type: integer
                    description: Total amount of compute used for this job (in seconds)
                  totalTimeSpentString:
                    type: string
                    description: Total amount of compute used (friendly string)
                  createdByUser:
                    $ref: '#/components/schemas/CreatedUpdatedByUser'
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
    TransformationJobStatusEnum:
      type: string
      enum:
        - waiting
        - created
        - started
        - finished
        - failed
    TransformationJobOperatesOnEnum:
      type: string
      enum:
        - file
        - directory
        - standalone
    CreatedUpdatedByUser:
      type: object
      required:
        - id
        - name
        - username
      properties:
        id:
          type: integer
        name:
          type: string
        username:
          type: string
        photo:
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