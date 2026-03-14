# Source: https://docs.edgeimpulse.com/apis/studio/organizationdata/view-file-from-dataset.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View file from dataset

> View a file that's located in a dataset (requires JWT auth). File might be converted (e.g. Parquet) or truncated (e.g. CSV).



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/dataset/{dataset}/files/view
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
  /api/organizations/{organizationId}/dataset/{dataset}/files/view:
    get:
      tags:
        - OrganizationData
      summary: View file from dataset
      description: >-
        View a file that's located in a dataset (requires JWT auth). File might
        be converted (e.g. Parquet) or truncated (e.g. CSV).
      operationId: viewDatasetFile
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/OrganizationDatasetPathParameter'
        - $ref: '#/components/parameters/PortalPathParameter'
      responses:
        '200':
          description: OK
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
    OrganizationDatasetPathParameter:
      name: dataset
      in: path
      required: true
      description: Dataset name
      schema:
        type: string
    PortalPathParameter:
      name: path
      in: query
      required: true
      description: Path to file in portal
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