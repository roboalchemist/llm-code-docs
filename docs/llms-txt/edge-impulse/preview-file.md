# Source: https://docs.edgeimpulse.com/apis/studio/organizationdata/preview-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Preview file

> Preview a single file from a data item (same as downloadOrganizationDataFile but w/ content-disposition inline and could be truncated).



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/data/{dataId}/files/preview
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
  /api/organizations/{organizationId}/data/{dataId}/files/preview:
    get:
      tags:
        - OrganizationData
      summary: Preview file
      description: >-
        Preview a single file from a data item (same as
        downloadOrganizationDataFile but w/ content-disposition inline and could
        be truncated).
      operationId: previewOrganizationDataFile
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/OrganizationDataIdParameter'
        - $ref: '#/components/parameters/OrganizationFileNameParameter'
      responses:
        '200':
          description: File
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
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
    OrganizationFileNameParameter:
      name: fileName
      in: query
      required: true
      description: File name
      schema:
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