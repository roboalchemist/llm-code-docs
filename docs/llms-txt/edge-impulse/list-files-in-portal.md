# Source: https://docs.edgeimpulse.com/apis/studio/uploadportal/list-files-in-portal.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List files in portal

> List all files and directories in specified prefix.



## OpenAPI

````yaml .assets/openapi.yaml post /api/portals/{portalId}/files
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
  /api/portals/{portalId}/files:
    post:
      tags:
        - UploadPortal
      summary: List files in portal
      description: List all files and directories in specified prefix.
      operationId: listPortalFilesInFolder
      parameters:
        - $ref: '#/components/parameters/PortalIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ListPortalFilesInFolderRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListPortalFilesInFolderResponse'
components:
  parameters:
    PortalIdParameter:
      name: portalId
      in: path
      required: true
      description: Portal ID
      schema:
        type: integer
  schemas:
    ListPortalFilesInFolderRequest:
      type: object
      required:
        - prefix
      properties:
        prefix:
          type: string
          description: S3 prefix
        continuationToken:
          type: string
          description: >-
            Only one S3 page (1000 items typically) is returned. Pass in the
            continuationToken on the next request to receive the next page.
        onlyFetchFolders:
          type: boolean
          description: If set, then no files will be returned
    ListPortalFilesInFolderResponse:
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
            continuationToken:
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