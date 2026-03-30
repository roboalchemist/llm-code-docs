# Source: https://docs.edgeimpulse.com/apis/studio/organizationcreateproject/start-transformation-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Start transformation job

> Start a transformation job to fetch data from the organization and put it in a project, or transform into new data.



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/create-project
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
    post:
      tags:
        - OrganizationCreateProject
      summary: Start transformation job
      description: >-
        Start a transformation job to fetch data from the organization and put
        it in a project, or transform into new data.
      operationId: organizationCreateProject
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OrganizationCreateProjectRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrganizationCreateProjectResponse'
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
    OrganizationCreateProjectRequest:
      type: object
      description: >-
        If uploadType is set to 'project', either projectId, newProjectName or
        projectApiKey is required. projectId and newProjectName are only
        available through JWT tokens. If uploadType is set to 'dataset' then
        outputDatasetName can be set to '' to output in the same dataset, or set
        to a string to create (or append to) a new dataset.
      required:
        - name
      properties:
        name:
          type: string
        filter:
          type: string
          description: >-
            Filter in SQL format, used for creating transformation jobs on
            clinical datasets
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
        projectVisibility:
          $ref: '#/components/schemas/ProjectVisibility'
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
          description: >-
            Path of new dataset within the bucket; used only when creating a new
            dataset.
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
        emailRecipientUids:
          type: array
          items:
            type: integer
        transformationParallel:
          description: Number of parallel jobs to start
          type: integer
        extraCliArguments:
          description: Optional extra arguments for this transformation block
          type: string
        parameters:
          type: object
          description: >-
            List of custom parameters for this transformation job (see the list
            of parameters that the block exposes).
          additionalProperties:
            type: string
    OrganizationCreateProjectResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - createProjectId
            - apiKey
          properties:
            createProjectId:
              type: integer
              description: Project ID for the new project
            apiKey:
              type: string
              description: >-
                DEPRECATED. API key for the new project. This field will always
                be empty.
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
    ProjectVisibility:
      type: string
      enum:
        - public
        - private
      description: >-
        The visibility of the project, either public or private. Public projects
        can be viewed by anyone on the internet and edited by collaborators.
        Private projects can only be viewed and edited by collaborators.
    OrganizationCreateProjectOutputDatasetPathRule:
      description: >-
        Defines the folder structure for writing to the output dataset. Used
        only when uploading into a default (non-clinical) dataset.
      type: string
      enum:
        - no-subfolders
        - subfolder-per-item
        - use-full-path
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