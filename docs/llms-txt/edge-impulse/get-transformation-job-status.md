# Source: https://docs.edgeimpulse.com/apis/studio/organizationcreateproject/get-transformation-job-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get transformation job status

> Get the current status of a transformation job job.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/create-project/{createProjectId}
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
  /api/organizations/{organizationId}/create-project/{createProjectId}:
    get:
      tags:
        - OrganizationCreateProject
      summary: Get transformation job status
      description: Get the current status of a transformation job job.
      operationId: getOrganizationCreateProjectStatus
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/OrganizationCreateProjectIdParameter'
        - $ref: '#/components/parameters/TransformLimitResultsParameter'
        - $ref: '#/components/parameters/TransformOffsetResultsParameter'
        - $ref: '#/components/parameters/TransformSelectionParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrganizationCreateProjectStatusResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
    OrganizationCreateProjectIdParameter:
      name: createProjectId
      in: path
      required: true
      description: Create project job ID.
      schema:
        type: integer
    TransformLimitResultsParameter:
      name: transformLimit
      in: query
      required: true
      description: Maximum number of results of transformation jobs
      schema:
        type: integer
    TransformOffsetResultsParameter:
      name: transformOffset
      in: query
      required: true
      description: >-
        Offset in results of transformation jobs, can be used in conjunction
        with TransformLimitResultsParameter to implement paging.
      schema:
        type: integer
    TransformSelectionParameter:
      name: selection
      in: query
      required: false
      description: >-
        Type of selected rows, either 'all', 'created', 'in-progress' or
        'failed' (defaults to 'all')
      schema:
        type: string
  schemas:
    OrganizationCreateProjectStatusResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          properties:
            status:
              $ref: '#/components/schemas/OrganizationCreateProjectWithFiles'
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
    OrganizationCreateProjectWithFiles:
      allOf:
        - $ref: '#/components/schemas/OrganizationCreateProject'
        - type: object
          required:
            - files
            - fileCountForFilter
          properties:
            files:
              type: array
              items:
                type: object
                required:
                  - id
                  - fileName
                  - bucketPath
                  - transformationJobStatus
                  - linkToDataItem
                  - lengthString
                  - sourceDatasetType
                properties:
                  id:
                    type: integer
                  fileName:
                    type: string
                  bucketPath:
                    type: string
                  transformationJobId:
                    type: integer
                  transformationJobStatus:
                    $ref: '#/components/schemas/TransformationJobStatusEnum'
                  linkToDataItem:
                    type: string
                  lengthString:
                    type: string
                    description: Only set after job was finished
                  sourceDatasetType:
                    $ref: '#/components/schemas/OrganizationDatasetTypeEnum'
            fileCountForFilter:
              type: integer
    OrganizationCreateProject:
      type: object
      required:
        - id
        - organizationId
        - name
        - status
        - transformJobStatus
        - uploadJobStatus
        - uploadType
        - category
        - created
        - totalDownloadFileCount
        - totalDownloadFileSize
        - totalDownloadFileSizeString
        - totalUploadFileCount
        - transformationParallel
        - transformationSummary
        - inProgress
        - operatesOn
        - totalTimeSpentSeconds
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
        status:
          $ref: '#/components/schemas/TransformationJobStatusEnum'
        transformJobStatus:
          $ref: '#/components/schemas/TransformationJobStatusEnum'
        uploadJobId:
          type: integer
        uploadJobStatus:
          $ref: '#/components/schemas/TransformationJobStatusEnum'
        uploadJobFilesUploaded:
          type: integer
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
        category:
          type: string
          enum:
            - training
            - testing
            - split
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
        transformationParallel:
          type: integer
          description: Number of transformation jobs that can be ran in parallel
        transformationSummary:
          type: object
          required:
            - startedCount
            - succeededCount
            - finishedCount
            - totalFileCount
            - totalTimeSpentSeconds
          properties:
            startedCount:
              type: integer
            succeededCount:
              type: integer
            finishedCount:
              type: integer
            totalFileCount:
              type: integer
            totalTimeSpentSeconds:
              type: integer
              description: Total amount of compute used for this job (in seconds)
        inProgress:
          type: boolean
        label:
          type: string
        filterQuery:
          type: string
        emailRecipientUids:
          type: array
          items:
            type: integer
        pipelineId:
          type: integer
        pipelineName:
          type: string
        pipelineRunId:
          type: integer
        pipelineStep:
          type: integer
        operatesOn:
          $ref: '#/components/schemas/TransformationJobOperatesOnEnum'
        totalTimeSpentSeconds:
          type: integer
          description: Total amount of compute used for this job (in seconds)
        totalTimeSpentString:
          type: string
          description: Total amount of compute used (friendly string)
        createdByUser:
          $ref: '#/components/schemas/CreatedUpdatedByUser'
    TransformationJobStatusEnum:
      type: string
      enum:
        - waiting
        - created
        - started
        - finished
        - failed
    OrganizationDatasetTypeEnum:
      type: string
      enum:
        - clinical
        - files
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