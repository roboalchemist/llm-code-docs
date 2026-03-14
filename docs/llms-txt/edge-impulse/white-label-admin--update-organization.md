# Source: https://docs.edgeimpulse.com/apis/studio/organizations/white-label-admin--update-organization.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# White Label Admin - Update organization

> White label admin only API to update organization properties such as name and logo.



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/whitelabel/organizations/{innerOrganizationId}
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
  /api/organizations/{organizationId}/whitelabel/organizations/{innerOrganizationId}:
    post:
      tags:
        - Organizations
      summary: White Label Admin - Update organization
      description: >-
        White label admin only API to update organization properties such as
        name and logo.
      operationId: whitelabelAdminUpdateOrganization
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/InnerOrganizationIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AdminUpdateOrganizationRequest'
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
  schemas:
    AdminUpdateOrganizationRequest:
      type: object
      description: Only fields set in this object will be updated.
      properties:
        logo:
          type: string
          description: New logo URL, or set to `null` to remove the logo.
        headerImg:
          type: string
          description: New leader image URL, or set to `null` to remove the leader.
        name:
          type: string
          description: New organization name.
        experiments:
          type: array
          items:
            type: string
        readme:
          type: string
          description: Readme for the organization (in Markdown)
        billable:
          type: boolean
        entitlementLimits:
          $ref: '#/components/schemas/EntitlementLimits'
        contractStartDate:
          type: string
          format: date-time
          description: >-
            The date in which the organization contract started. Compute time
            will be calculated from this date.
        domain:
          type: string
          description: >-
            The domain of the organization. The organization domain is used to
            add new users to an organization. For example, new @edgeimpulse.com
            would be added to the Edge Impulse organization if this organization
            has edgeimpulse.com as the domain.
          example: edgeimpulse.com
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
    EntitlementLimits:
      type: object
      properties:
        totalStorage:
          type: number
          description: Storage entitlement, in bytes
        computeTimePerYear:
          type: number
          description: Total compute time entitlement (CPU + GPU), in seconds
        gpuComputeTimePerYear:
          type: number
          description: GPU compute time entitlement, in seconds
        numberOfProjects:
          type: integer
          description: Number of projects allowed for this organization
        numberOfUsers:
          type: integer
          description: Number of users allowed for this organization
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