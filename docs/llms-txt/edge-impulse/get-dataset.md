# Source: https://docs.edgeimpulse.com/apis/studio/organizationdata/get-dataset.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get dataset

> Get information about a dataset



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/dataset/{dataset}
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
  /api/organizations/{organizationId}/dataset/{dataset}:
    get:
      tags:
        - OrganizationData
      summary: Get dataset
      description: Get information about a dataset
      operationId: getOrganizationDataset
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/OrganizationDatasetPathParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetOrganizationDatasetResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
    OrganizationDatasetPathParameter:
      name: dataset
      in: path
      required: true
      description: Dataset name
      schema:
        type: string
  schemas:
    GetOrganizationDatasetResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - dataset
          properties:
            dataset:
              $ref: '#/components/schemas/OrganizationDataset'
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
    OrganizationDataset:
      type: object
      required:
        - dataset
        - lastFileCreated
        - totalFileSize
        - totalFileCount
        - totalItemCount
        - totalItemCountChecklistOK
        - totalItemCountChecklistFailed
        - tags
        - type
      properties:
        dataset:
          type: string
        lastFileCreated:
          type: string
          format: date-time
        totalFileSize:
          type: integer
        totalFileCount:
          type: integer
        totalItemCount:
          type: integer
        totalItemCountChecklistOK:
          type: integer
        totalItemCountChecklistFailed:
          type: integer
        tags:
          type: array
          items:
            type: string
        category:
          type: string
        bucket:
          $ref: '#/components/schemas/OrganizationDatasetBucket'
        type:
          $ref: '#/components/schemas/OrganizationDatasetTypeEnum'
        bucketPath:
          type: string
          description: Location of the dataset within the bucket
    OrganizationDatasetBucket:
      type: object
      required:
        - id
        - bucket
        - path
        - fullBucketPathDescription
        - dataItemNamingLevelsDeep
      properties:
        id:
          description: Bucket ID
          type: integer
        bucket:
          type: string
        path:
          description: Path in the bucket
          type: string
        fullBucketPathDescription:
          description: >-
            Full bucket path, incl. protocol (e.g. s3://bucket/path) - to be
            used in the UI
          type: string
        dataItemNamingLevelsDeep:
          description: >-
            Number of levels deep for data items, e.g. if you have folder
            "test/abc", with value 1 "test" will be a data item, with value 2
            "test/abc" will be a data item. Only used for "clinical" type.
          type: integer
    OrganizationDatasetTypeEnum:
      type: string
      enum:
        - clinical
        - files
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