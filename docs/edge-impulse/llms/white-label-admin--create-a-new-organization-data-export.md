# Source: https://docs.edgeimpulse.com/apis/studio/organizations/white-label-admin--create-a-new-organization-data-export.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# White Label Admin - Create a new organization data export

> Create a new data export for an organization.
A job is created to process the export request and the job details are returned in the response.
This is an API only available to white label admins.




## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/whitelabel/organizations/{innerOrganizationId}/exports
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
  /api/organizations/{organizationId}/whitelabel/organizations/{innerOrganizationId}/exports:
    post:
      tags:
        - Organizations
      summary: White Label Admin - Create a new organization data export
      description: >
        Create a new data export for an organization.

        A job is created to process the export request and the job details are
        returned in the response.

        This is an API only available to white label admins.
      operationId: whitelabelAdminCreateOrganizationExport
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/InnerOrganizationIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AdminCreateOrganizationDataExportRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StartJobResponse'
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
  schemas:
    AdminCreateOrganizationDataExportRequest:
      type: object
      required:
        - description
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
    StartJobResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - id
          properties:
            id:
              type: integer
              description: Job identifier. Status updates will include this identifier.
              example: 12873488112
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