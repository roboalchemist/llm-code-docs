# Source: https://docs.edgeimpulse.com/apis/studio/organizations/white-label-admin--update-organization-data-export.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# White Label Admin - Update organization data export

> Update a data export for an organization. This is an API only available to white label admins.



## OpenAPI

````yaml .assets/openapi.yaml put /api/organizations/{organizationId}/whitelabel/organizations/{innerOrganizationId}/exports/{exportId}
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
  /api/organizations/{organizationId}/whitelabel/organizations/{innerOrganizationId}/exports/{exportId}:
    put:
      tags:
        - Organizations
      summary: White Label Admin - Update organization data export
      description: >-
        Update a data export for an organization. This is an API only available
        to white label admins.
      operationId: whitelabelAdminUpdateOrganizationExport
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/InnerOrganizationIdParameter'
        - $ref: '#/components/parameters/ExportIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AdminUpdateOrganizationDataExportRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenericApiResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
    InnerOrganizationIdParameter:
      name: innerOrganizationId
      in: path
      required: true
      description: Organization ID within the context of a white label
      schema:
        type: integer
    ExportIdParameter:
      name: exportId
      in: path
      required: true
      description: Export ID
      schema:
        type: integer
  schemas:
    AdminUpdateOrganizationDataExportRequest:
      type: object
      properties:
        description:
          type: string
          description: Description of the data export
        expirationDate:
          type: string
          format: date-time
          description: >-
            Date when the export will expire. Default is 30 days. Maximum
            expiration date is 60 days from the creation date.
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