# Source: https://docs.edgeimpulse.com/apis/studio/organizationdata/preview-files-in-a-default-dataset.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Preview files in a default dataset

> Preview files and directories in a default dataset for the given prefix, with support for wildcards. This is an internal API used when starting a transformation job.



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/dataset/{dataset}/files/preview
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
  /api/organizations/{organizationId}/dataset/{dataset}/files/preview:
    post:
      tags:
        - OrganizationData
      summary: Preview files in a default dataset
      description: >-
        Preview files and directories in a default dataset for the given prefix,
        with support for wildcards. This is an internal API used when starting a
        transformation job.
      operationId: previewDefaultFilesInFolder
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/OrganizationDatasetPathParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PreviewDefaultFilesInFolderRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PreviewDefaultFilesInFolderResponse'
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
    PreviewDefaultFilesInFolderRequest:
      type: object
      required:
        - prefix
        - itemsToList
      properties:
        prefix:
          type: string
          description: S3 prefix
        itemsToList:
          description: Return either files or folders matching the specified prefix
          type: string
          enum:
            - files
            - folders
    PreviewDefaultFilesInFolderResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - files
          properties:
            files:
              type: array
              items:
                $ref: '#/components/schemas/PortalFile'
            isTruncated:
              type: boolean
              description: True if results are truncated.
            truncationReason:
              type: string
              description: >
                Explains why results are truncated; only present in the response
                if isTruncated is true. Results can be truncated if there are
                too many results (more than 500 matches), or if searching for
                more results is too expensive (for example, the dataset contains
                many items but very few match the given wildcard).
              enum:
                - too-many-results
                - too-expensive-search
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
    PortalFile:
      type: object
      required:
        - name
        - path
        - type
      properties:
        name:
          type: string
        addedDate:
          type: string
          format: date-time
          example: '2019-07-21T17:32:28Z'
        size:
          type: integer
        ETag:
          type: string
        path:
          type: string
        type:
          type: string
          enum:
            - folder
            - file
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