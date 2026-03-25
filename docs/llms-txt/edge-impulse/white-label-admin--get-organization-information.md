# Source: https://docs.edgeimpulse.com/apis/studio/organizations/white-label-admin--get-organization-information.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# White Label Admin - Get organization information

> White label admin only API to list all information about an organization.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/whitelabel/organizations/{innerOrganizationId}
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
    get:
      tags:
        - Organizations
      summary: White Label Admin - Get organization information
      description: >-
        White label admin only API to list all information about an
        organization.
      operationId: whitelabelAdminGetOrganizationInfo
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/InnerOrganizationIdParameter'
        - $ref: '#/components/parameters/FiltersIncludeDeletedParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AdminOrganizationInfoResponse'
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
    FiltersIncludeDeletedParameter:
      name: includeDeleted
      in: query
      required: false
      description: Whether to include deleted entities (users, projects, orgs)
      schema:
        type: boolean
  schemas:
    AdminOrganizationInfoResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - $ref: '#/components/schemas/OrganizationComputeTimeUsage'
        - type: object
          properties:
            billable:
              type: boolean
            entitlementLimits:
              $ref: '#/components/schemas/EntitlementLimits'
            computeTimeCurrentContractSince:
              type: string
              format: date-time
              description: >-
                The date from which the compute time for the running contract is
                calculated.
            totalStorage:
              type: number
              description: Total storage used by the organization.
            dailyMetrics:
              type: array
              description: Metrics for the last 365 days
              nullable: true
              items:
                $ref: '#/components/schemas/DailyMetricsRecord'
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
    DailyMetricsRecord:
      type: object
      required:
        - date
        - totalUsers
        - totalStaffUsers
        - totalProjects
        - totalCurrentContractCpuComputeTimeSeconds
        - totalCurrentContractGpuComputeTimeSeconds
        - totalCurrentContractComputeTimeSeconds
        - computeTimeCalculatedSince
        - totalStorageSizeBytes
        - usersAdded
        - usersDeleted
        - projectsAdded
        - projectsDeleted
        - cpuComputeTimeSeconds
        - gpuComputeTimeSeconds
        - computeTimeSeconds
        - storageBytesAdded
        - storageBytesDeleted
      properties:
        date:
          type: string
          format: date-time
          description: Date of the metrics record.
          example: '2021-01-01T00:00:00Z'
        totalUsers:
          type: integer
          description: >
            Total number of users, if the metrics record applies to a
            non-developer profile organization.

            For developer profile organizations, we default to 0.
          example: 100
        totalStaffUsers:
          type: integer
          description: >
            Total number of staff users, if the metrics record applies to a
            non-developer profile organization.

            For developer profile organizations, we default to 0.
          example: 10
        totalProjects:
          type: integer
          description: |
            Total number of projects at the end of the metrics record date.
          example: 50
        totalCurrentContractCpuComputeTimeSeconds:
          type: integer
          description: >
            Total CPU compute time since contract start date, or organization /
            user creation date, at

            the end of the metrics record date.
          example: 100000
        totalCurrentContractGpuComputeTimeSeconds:
          type: integer
          description: >
            Total GPU compute time since contract start date, or organization /
            user creation date, at

            the end of the metrics record date.
          example: 100000
        totalCurrentContractComputeTimeSeconds:
          type: integer
          description: >
            Total compute time since contract start date, or organization / user
            creation date, at

            the end of the metrics record date.

            Compute time is calculated as CPU + 3*GPU compute time.
          example: 100000
        computeTimeCalculatedSince:
          type: string
          format: date-time
          description: >
            Date from which the total compute time is calculated. This is the
            contract start date for billing

            organizations, or organization / user creation date.
          example: '2021-01-01T00:00:00Z'
        totalStorageSizeBytes:
          type: integer
          description: |
            Total storage size in bytes at the end of the metrics record date.
          example: 1000000000
        usersAdded:
          type: integer
          description: |
            Number of users added during the metrics record date.
          example: 10
        staffUsersAdded:
          type: integer
          description: |
            Number of staff users added during the metrics record date.
          example: 1
        usersDeleted:
          type: integer
          description: |
            Number of users deleted during the metrics record date.
          example: 5
        staffUsersDeleted:
          type: integer
          description: |
            Number of staff users deleted during the metrics record date.
          example: 1
        projectsAdded:
          type: integer
          description: |
            Number of projects added during the metrics record date.
          example: 10
        projectsDeleted:
          type: integer
          description: |
            Number of projects deleted during the metrics record date.
          example: 5
        cpuComputeTimeSeconds:
          type: integer
          description: |
            Total CPU compute time during the metrics record date.
          example: 10000
        gpuComputeTimeSeconds:
          type: integer
          description: |
            Total GPU compute time during the metrics record date.
          example: 10000
        computeTimeSeconds:
          type: integer
          description: |
            Total compute time during the metrics record date.
            Compute time is calculated as CPU + 3*GPU compute time.
          example: 10000
        storageBytesAdded:
          type: integer
          description: |
            Total storage size in bytes added during the metrics record date.
          example: 1000000000
        storageBytesDeleted:
          type: integer
          description: |
            Total storage size in bytes deleted during the metrics record date.
          example: 500000000
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