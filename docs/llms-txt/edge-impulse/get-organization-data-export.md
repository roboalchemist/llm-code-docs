# Source: https://docs.edgeimpulse.com/apis/studio/organizations/get-organization-data-export.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get organization data export

> Get a data export for an organization.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/exports/{exportId}
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
  /api/organizations/{organizationId}/exports/{exportId}:
    get:
      tags:
        - Organizations
      summary: Get organization data export
      description: Get a data export for an organization.
      operationId: getOrganizationDataExport
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/ExportIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetOrganizationDataExportResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
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
    GetOrganizationDataExportResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - export
          properties:
            export:
              $ref: '#/components/schemas/OrganizationDataExport'
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
    OrganizationDataExport:
      type: object
      required:
        - id
        - created
        - expirationDate
        - jobId
        - jobFinished
        - jobFinishedSuccessful
      properties:
        id:
          type: integer
        created:
          type: string
          format: date-time
        createdByUser:
          $ref: '#/components/schemas/CreatedUpdatedByUser'
        jobId:
          type: integer
        jobFinished:
          type: boolean
        jobFinishedSuccessful:
          type: boolean
        description:
          type: string
          description: Description of the data export
        expirationDate:
          type: string
          format: date-time
          description: >-
            Date when the export will expire. Default is 30 days. Maximum
            expiration date is 60 days from the creation date.
        downloadUrl:
          type: string
    CreatedUpdatedByUser:
      type: object
      required:
        - id
        - name
        - username
      properties:
        id:
          type: integer
        name:
          type: string
        username:
          type: string
        photo:
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