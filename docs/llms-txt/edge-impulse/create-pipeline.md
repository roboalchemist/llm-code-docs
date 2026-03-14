# Source: https://docs.edgeimpulse.com/apis/studio/organizationpipelines/create-pipeline.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create pipeline

> Create an organizational pipelines



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/pipelines
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
    post:
      tags:
        - OrganizationPipelines
      summary: Create pipeline
      description: Create an organizational pipelines
      operationId: createOrganizationPipeline
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OrganizationUpdatePipelineBody'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EntityCreatedResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
  schemas:
    OrganizationUpdatePipelineBody:
      type: object
      required:
        - name
        - description
        - steps
        - emailRecipientUids
        - whenToEmail
      properties:
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
        dataset:
          type: string
        projectId:
          type: integer
        emailRecipientUids:
          type: array
          items:
            type: integer
        notificationWebhook:
          type: string
        whenToEmail:
          type: string
          enum:
            - always
            - on_new_data
            - never
        archived:
          type: boolean
    EntityCreatedResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - id
          properties:
            id:
              type: integer
              description: Unique identifier of the created entity.
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