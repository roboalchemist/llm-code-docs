# Source: https://docs.edgeimpulse.com/apis/studio/organizations/white-label-admin--get-all-white-label-projects.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# White Label Admin - Get all white label projects

> White label admin only API to get the list of all projects.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/whitelabel/projects
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
  /api/organizations/{organizationId}/whitelabel/projects:
    get:
      tags:
        - Organizations
      summary: White Label Admin - Get all white label projects
      description: White label admin only API to get the list of all projects.
      operationId: whitelabelAdminGetProjects
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/FiltersActiveParameter'
        - $ref: '#/components/parameters/SortQueryParameter'
        - $ref: '#/components/parameters/FiltersQueryParameter'
        - $ref: '#/components/parameters/LimitResultsParameter'
        - $ref: '#/components/parameters/OffsetResultsParameter'
        - $ref: '#/components/parameters/SearchQueryParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AdminListProjectsResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
    FiltersActiveParameter:
      name: active
      in: query
      required: false
      description: Whether to search for entities (users, orgs) active in the last X days
      schema:
        type: integer
    SortQueryParameter:
      name: sort
      in: query
      required: false
      description: Fields and order to sort query by
      schema:
        type: string
        description: >-
          Comma separated list of fields to sort query by. Prefix with a minus
          (-) sign to indicate descending order. Default order is ascending
        example: id,-name
    FiltersQueryParameter:
      name: filters
      in: query
      required: false
      schema:
        type: string
        description: |
          Comma separated list of filters to apply to the query.
          Filters should be in the format 'field:value'.
        example: billable:true
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
    SearchQueryParameter:
      name: search
      in: query
      required: false
      description: Search query
      schema:
        example: <id> <name>
        type: string
  schemas:
    AdminListProjectsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - $ref: '#/components/schemas/AdminListProjects'
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
    AdminListProjects:
      type: object
      required:
        - projects
        - total
      properties:
        total:
          type: integer
        projects:
          type: array
          description: Array with projects
          items:
            $ref: '#/components/schemas/AdminApiProject'
    AdminApiProject:
      type: object
      required:
        - id
        - name
        - owner
      properties:
        id:
          type: integer
          example: 1
        name:
          type: string
          example: Water hammer detection
        description:
          type: string
        created:
          type: string
          format: date-time
          example: '2019-07-21T17:32:28Z'
        owner:
          type: string
          description: User or organization that owns the project
        ownerUserId:
          type: integer
        ownerOrganizationId:
          type: integer
        lastAccessed:
          type: string
          format: date-time
          example: '2019-07-21T17:32:28Z'
        whitelabelId:
          type: integer
          nullable: true
          description: >-
            Unique identifier of the white label this project belongs to, if
            any.
        tier:
          $ref: '#/components/schemas/ProjectTierEnum'
        category:
          $ref: '#/components/schemas/ProjectType'
        deletedDate:
          type: string
          format: date-time
    ProjectTierEnum:
      type: string
      description: >-
        The project tier. This is "enterprise" for all organization projects, or
        the user tier for all user projects.
      enum:
        - free
        - community-plus
        - professional
        - enterprise
    ProjectType:
      type: string
      enum:
        - kws
        - audio
        - object-detection
        - image
        - accelerometer
        - other
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