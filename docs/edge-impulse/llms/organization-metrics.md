# Source: https://docs.edgeimpulse.com/apis/studio/organizations/organization-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Organization metrics

> Get general metrics for this organization.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/metrics
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
  /api/organizations/{organizationId}/metrics:
    get:
      tags:
        - Organizations
      summary: Organization metrics
      description: Get general metrics for this organization.
      operationId: getOrganizationMetrics
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/ExcludeEdgeImpulseUsersParameter'
        - $ref: '#/components/parameters/ProjectVisibilityParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrganizationMetricsResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
    ExcludeEdgeImpulseUsersParameter:
      name: excludeEdgeImpulseUsers
      in: query
      required: false
      description: >-
        Whether to exclude Edge Impulse users when counting enterprise
        entitlements usage
      schema:
        type: boolean
    ProjectVisibilityParameter:
      name: projectVisibility
      in: query
      required: false
      description: >-
        What project visibility type to include when counting enterprise
        entitlements usage
      schema:
        $ref: '#/components/schemas/ProjectVisibility'
  schemas:
    OrganizationMetricsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - metrics
          properties:
            metrics:
              type: object
              required:
                - totalJobsComputeTime
                - jobsComputeTimeCurrentYear
                - jobsComputeTimeCurrentYearSince
                - cpuComputeTimeCurrentContract
                - gpuComputeTimeCurrentContract
                - totalStorage
                - projectCount
                - userCount
              properties:
                totalJobsComputeTime:
                  type: number
                  description: >-
                    Total compute time of all organizational jobs since the
                    creation of the organization (including organizational
                    project jobs). Compute time is the amount of computation
                    time spent in jobs, in minutes used by an organization over
                    a 12 month period, calculated as CPU + GPU minutes.
                jobsComputeTimeCurrentYear:
                  type: number
                  description: >-
                    Total compute time of all organizational jobs in the current
                    contract (including organizational project jobs). Compute
                    time is the amount of computation time spent in jobs, in
                    minutes used by an organization over a 12 month period,
                    calculated as CPU + GPU minutes.
                jobsComputeTimeCurrentYearSince:
                  type: string
                  format: date-time
                  description: >-
                    The date from which the compute time for the running
                    contract is calculated.
                cpuComputeTimeCurrentContract:
                  type: number
                  description: >-
                    CPU compute time of all jobs in the organization in the
                    current contract (including organizational project jobs).
                gpuComputeTimeCurrentContract:
                  type: number
                  description: >-
                    GPU compute time of all jobs in the organization in the
                    current contract (including organizational project jobs).
                totalStorage:
                  type: number
                  description: Total storage used by the organization.
                projectCount:
                  type: integer
                  description: Total number of projects owned by the organization.
                userCount:
                  type: integer
                  description: Total number of users in the organization.
    ProjectVisibility:
      type: string
      enum:
        - public
        - private
      description: >-
        The visibility of the project, either public or private. Public projects
        can be viewed by anyone on the internet and edited by collaborators.
        Private projects can only be viewed and edited by collaborators.
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