# Source: https://docs.edgeimpulse.com/apis/studio/organizationdata/download-data-1.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Download data

> Download all data for this data item.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/data/{dataId}/download
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
  /api/organizations/{organizationId}/data/{dataId}/download:
    get:
      tags:
        - OrganizationData
      summary: Download data
      description: Download all data for this data item.
      operationId: downloadOrganizationSingleDataItem
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/OrganizationDataIdParameter'
        - $ref: '#/components/parameters/OrganizationDataFilterParameter'
      responses:
        '200':
          description: ZIP file
          content:
            application/zip:
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
    OrganizationDataFilterParameter:
      name: filter
      in: query
      required: false
      description: >-
        Data filter in SQL WHERE format, where you can reference 'dataset',
        'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and
        any metadata label through 'metadata->' (dots are replaced by
        underscore).
      example: >-
        dataset = 'activity data' AND (label = 'running' OR metadata->user =
        'Jan Jongboom')
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