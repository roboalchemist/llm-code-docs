# Source: https://docs.edgeimpulse.com/apis/studio/organizationpipelines/run-pipeline.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run pipeline

> Run an organizational pipeline



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/pipelines/{pipelineId}/run
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
  /api/organizations/{organizationId}/pipelines/{pipelineId}/run:
    post:
      tags:
        - OrganizationPipelines
      summary: Run pipeline
      description: Run an organizational pipeline
      operationId: runOrganizationPipeline
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/OrganizationPipelineIdParameter'
        - $ref: '#/components/parameters/IgnoreLastSuccessfulRunQueryParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RunOrganizationPipelineResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
    OrganizationPipelineIdParameter:
      name: pipelineId
      in: path
      required: true
      description: Pipeline ID
      schema:
        type: integer
    IgnoreLastSuccessfulRunQueryParameter:
      name: ignoreLastSuccessfulRun
      in: query
      required: false
      description: >-
        If set then `EI_LAST_SUCCESSFUL_RUN` is not set. You can use this to
        re-run a pipeline from scratch.
      schema:
        type: boolean
  schemas:
    RunOrganizationPipelineResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - pipelineRun
          properties:
            pipelineRun:
              $ref: '#/components/schemas/OrganizationPipelineRun'
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
    OrganizationPipelineRun:
      type: object
      required:
        - id
        - steps
        - created
      properties:
        id:
          type: integer
        steps:
          type: array
          items:
            $ref: '#/components/schemas/OrganizationPipelineRunStep'
        created:
          type: string
          format: date-time
        finished:
          type: string
          format: date-time
        itemCountBefore:
          $ref: '#/components/schemas/OrganizationPipelineItemCount'
          description: >-
            Item count before the pipeline ran, only set when the pipeline has a
            dataset attached.
        itemCountAfter:
          $ref: '#/components/schemas/OrganizationPipelineItemCount'
          description: >-
            Item count after the pipeline ran, only set when the pipeline has a
            dataset attached.
        itemCountImportIntoProjectFailed:
          description: >-
            Number of data items that failed to import into a project (through
            the s3-to-project, portal-to-project or dataset-to-project)
            transform blocks
          type: integer
    OrganizationPipelineRunStep:
      type: object
      required:
        - name
        - status
      properties:
        name:
          type: string
        transformationJob:
          $ref: '#/components/schemas/OrganizationCreateProject'
        filter:
          type: string
        uploadType:
          type: string
          enum:
            - project
            - dataset
        projectId:
          type: integer
        newProjectName:
          type: string
        projectApiKey:
          type: string
        projectHmacKey:
          type: string
        transformationBlockId:
          type: integer
        builtinTransformationBlock:
          type: object
        category:
          type: string
          enum:
            - training
            - testing
            - split
        outputDatasetName:
          type: string
        outputDatasetBucketId:
          type: integer
        outputDatasetBucketPath:
          type: string
        label:
          type: string
        extraCliArguments:
          type: string
        parameters:
          type: object
          additionalProperties:
            type: string
    OrganizationPipelineItemCount:
      type: object
      required:
        - itemCount
        - itemCountChecklistOK
        - itemCountChecklistFailed
      properties:
        itemCount:
          type: integer
        itemCountChecklistOK:
          type: integer
        itemCountChecklistFailed:
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