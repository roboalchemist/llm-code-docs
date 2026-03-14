# Source: https://docs.edgeimpulse.com/apis/studio/organizations/white-label-admin--get-organization-compute-time-usage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# White Label Admin - Get organization compute time usage

> Get compute time usage for an organization over a period of time. This is an API only available to white label admins



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/whitelabel/organizations/{innerOrganizationId}/usage/computeTime
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
  /api/organizations/{organizationId}/whitelabel/organizations/{innerOrganizationId}/usage/computeTime:
    get:
      tags:
        - Organizations
      summary: White Label Admin - Get organization compute time usage
      description: >-
        Get compute time usage for an organization over a period of time. This
        is an API only available to white label admins
      operationId: whitelabelAdminGetOrganizationComputeTimeUsage
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/InnerOrganizationIdParameter'
        - $ref: '#/components/parameters/RequiredStartDateParameter'
        - $ref: '#/components/parameters/RequiredEndDateParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/AdminGetOrganizationComputeTimeUsageResponse
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
    RequiredStartDateParameter:
      name: startDate
      in: query
      required: true
      description: Start date
      schema:
        type: string
        format: date-time
    RequiredEndDateParameter:
      name: endDate
      in: query
      required: true
      description: End date
      schema:
        type: string
        format: date-time
  schemas:
    AdminGetOrganizationComputeTimeUsageResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - $ref: '#/components/schemas/OrganizationComputeTimeUsage'
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
    OrganizationComputeTimeUsage:
      type: object
      properties:
        cpuComputeTime:
          type: number
          description: >-
            CPU compute time in seconds of all jobs in the organization
            (including organizational project jobs).
        gpuComputeTime:
          type: number
          description: >-
            GPU compute time in seconds of all jobs in the organization
            (including organizational project jobs).
        totalComputeTime:
          type: number
          description: >-
            Total compute time is the amount of computation time spent in jobs,
            in minutes used by an organization over the given period, calculated
            as CPU + GPU minutes.
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