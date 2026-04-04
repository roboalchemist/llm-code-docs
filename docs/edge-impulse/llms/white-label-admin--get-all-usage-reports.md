# Source: https://docs.edgeimpulse.com/apis/studio/organizations/white-label-admin--get-all-usage-reports.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# White Label Admin - Get all usage reports

> Get all usage reports for an organization. This is an API only available to white label admins.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/whitelabel/organizations/{innerOrganizationId}/usage/reports
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
  /api/organizations/{organizationId}/whitelabel/organizations/{innerOrganizationId}/usage/reports:
    get:
      tags:
        - Organizations
      summary: White Label Admin - Get all usage reports
      description: >-
        Get all usage reports for an organization. This is an API only available
        to white label admins.
      operationId: whitelabelAdminGetOrganizationUsageReports
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/InnerOrganizationIdParameter'
        - $ref: '#/components/parameters/LimitResultsParameter'
        - $ref: '#/components/parameters/OffsetResultsParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AdminGetReportsResponse'
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
    LimitResultsParameter:
      name: limit
      in: query
      required: false
      description: Maximum number of results
      schema:
        type: integer
    OffsetResultsParameter:
      name: offset
      in: query
      required: false
      description: >-
        Offset in results, can be used in conjunction with LimitResultsParameter
        to implement paging.
      schema:
        type: integer
  schemas:
    AdminGetReportsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - reports
            - totalCount
          properties:
            reports:
              type: array
              description: List of organization usage reports.
              items:
                $ref: '#/components/schemas/Report'
            totalCount:
              type: integer
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
    Report:
      type: object
      required:
        - id
        - created
        - jobId
        - jobFinished
        - jobFinishedSuccessful
        - reportStartDate
        - reportEndDate
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
        downloadLink:
          type: string
        reportStartDate:
          type: string
          format: date-time
        reportEndDate:
          type: string
          format: date-time
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