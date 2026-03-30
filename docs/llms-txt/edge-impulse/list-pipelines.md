# Source: https://docs.edgeimpulse.com/apis/studio/organizationpipelines/list-pipelines.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List pipelines

> Retrieve all organizational pipelines



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/pipelines
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
  /api/organizations/{organizationId}/pipelines:
    get:
      tags:
        - OrganizationPipelines
      summary: List pipelines
      description: Retrieve all organizational pipelines
      operationId: listOrganizationPipelines
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/ListPipelinesProjectIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListOrganizationPipelinesResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
    ListPipelinesProjectIdParameter:
      name: projectId
      in: query
      required: false
      description: If set, filters on pipelines which are attached to this project.
      schema:
        type: integer
  schemas:
    ListOrganizationPipelinesResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - pipelines
          properties:
            pipelines:
              type: array
              items:
                $ref: '#/components/schemas/OrganizationPipeline'
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
    OrganizationPipeline:
      type: object
      required:
        - id
        - name
        - description
        - steps
        - created
        - emailRecipientUids
        - whenToEmail
      properties:
        id:
          type: integer
        name:
          type: string
        description:
          type: string
        intervalStr:
          type: string
          description: 15m for every 15 minutes, 2h for every 2 hours, 1d for every 1 day
        steps:
          type: array
          items:
            $ref: '#/components/schemas/OrganizationPipelineStep'
        nextRun:
          type: string
          format: date-time
        created:
          type: string
          format: date-time
        currentRun:
          $ref: '#/components/schemas/OrganizationPipelineRun'
        lastRun:
          $ref: '#/components/schemas/OrganizationPipelineRun'
        feedingIntoDataset:
          type: object
          required:
            - dataset
            - datasetLink
            - itemCount
            - itemCountChecklistOK
            - itemCountChecklistError
          properties:
            dataset:
              type: string
            datasetLink:
              type: string
            itemCount:
              type: integer
            itemCountChecklistOK:
              type: integer
            itemCountChecklistError:
              type: integer
            datasetType:
              $ref: '#/components/schemas/OrganizationDatasetTypeEnum'
        feedingIntoProject:
          type: object
          required:
            - id
            - name
            - projectLink
            - itemCount
          properties:
            id:
              type: integer
            name:
              type: string
            projectLink:
              type: string
            itemCount:
              type: integer
        emailRecipientUids:
          type: array
          items:
            type: integer
        lastRunStartError:
          type: string
        notificationWebhook:
          type: string
        whenToEmail:
          type: string
          enum:
            - always
            - on_new_data
            - never
    OrganizationPipelineStep:
      type: object
      required:
        - name
      properties:
        name:
          type: string
        filter:
          type: string
        pathFilters:
          type: array
          description: >-
            Set of paths to apply the transformation to, used for creating
            transformation jobs on default datasets. This option is experimental
            and may change in the future.
          items:
            $ref: '#/components/schemas/OrganizationCreateProjectPathFilter'
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
        outputPathInDataset:
          description: >-
            Path within the selected dataset to upload transformed files into.
            Used only when uploading into a default (non-clinical) dataset.
          type: string
        outputDatasetPathRule:
          $ref: '#/components/schemas/OrganizationCreateProjectOutputDatasetPathRule'
        label:
          type: string
        transformationParallel:
          type: integer
        extraCliArguments:
          type: string
        parameters:
          type: object
          additionalProperties:
            type: string
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
    OrganizationDatasetTypeEnum:
      type: string
      enum:
        - clinical
        - files
    OrganizationCreateProjectPathFilter:
      type: object
      description: >-
        Filter, given as a dataset and path containing wildcards, used for
        creating transformation jobs
      required:
        - dataset
        - filter
      properties:
        dataset:
          type: string
          description: Dataset name of files to transform
        filter:
          type: string
          description: >-
            Path filter with wildcards, relative to the root of the dataset. For
            example, /folder/*.json will transform all JSON files in /folder
            (when operating on files)
    OrganizationCreateProjectOutputDatasetPathRule:
      description: >-
        Defines the folder structure for writing to the output dataset. Used
        only when uploading into a default (non-clinical) dataset.
      type: string
      enum:
        - no-subfolders
        - subfolder-per-item
        - use-full-path
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