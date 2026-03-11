# Source: https://docs.edgeimpulse.com/apis/studio/organizations/white-label-admin--get-all-white-label-users.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# White Label Admin - Get all white label users

> White label admin only API to get the list of all registered users.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/whitelabel/users
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
  /api/organizations/{organizationId}/whitelabel/users:
    get:
      tags:
        - Organizations
      summary: White Label Admin - Get all white label users
      description: White label admin only API to get the list of all registered users.
      operationId: whitelabelAdminGetUsers
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/FiltersActiveParameter'
        - $ref: '#/components/parameters/FiltersTierParameter'
        - $ref: '#/components/parameters/FieldsParameter'
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
                $ref: '#/components/schemas/AdminGetUsersResponse'
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
    FiltersTierParameter:
      name: tier
      in: query
      required: false
      description: >-
        Whether to search for free, community plus, professional, or enterprise
        entities (users, projects)
      schema:
        $ref: '#/components/schemas/UserTierEnum'
    FieldsParameter:
      name: fields
      in: query
      required: false
      description: Comma separated list of fields to fetch in a query
      schema:
        type: string
        example: id,name
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
    AdminGetUsersResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - users
            - total
          properties:
            total:
              type: integer
            users:
              type: array
              items:
                type: object
                required:
                  - id
                  - username
                  - email
                  - name
                  - created
                properties:
                  id:
                    type: integer
                    example: 1
                  username:
                    type: string
                    example: janjongboom
                  email:
                    type: string
                    example: jan@edgeimpulse.com
                  name:
                    type: string
                    example: Jan Jongboom
                  photo:
                    type: string
                    example: https://usercdn.edgeimpulse.com/photos/1.jpg
                  created:
                    type: string
                    format: date-time
                    example: '2019-08-31T17:32:28Z'
                  lastSeen:
                    type: string
                    format: date-time
                    example: '2019-08-31T17:32:28Z'
                  activated:
                    type: boolean
                  from_evaluation:
                    type: boolean
                  tier:
                    $ref: '#/components/schemas/UserTierEnum'
                  deletedDate:
                    type: string
                    format: date-time
                    example: '2024-01-01T00:00:00Z'
    UserTierEnum:
      type: string
      description: The user account tier.
      enum:
        - free
        - community-plus
        - professional
        - enterprise
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