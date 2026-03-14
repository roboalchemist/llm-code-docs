# Source: https://docs.edgeimpulse.com/apis/studio/organizations/white-label-admin--add-user-to-an-organization.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# White Label Admin - Add user to an organization

> DEPRECATED. White label admin only API to add a user to an organization. If no user is provided, the current user is used.



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/whitelabel/organizations/{innerOrganizationId}/members
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
  /api/organizations/{organizationId}/whitelabel/organizations/{innerOrganizationId}/members:
    post:
      tags:
        - Organizations
      summary: White Label Admin - Add user to an organization
      description: >-
        DEPRECATED. White label admin only API to add a user to an organization.
        If no user is provided, the current user is used.
      operationId: whitelabelAdminAddUserToOrganization
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/InnerOrganizationIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AdminAddOrganizationUserRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenericApiResponse'
      deprecated: true
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
    AdminAddOrganizationUserRequest:
      allOf:
        - $ref: '#/components/schemas/AdminAddUserRequest'
        - type: object
          required:
            - role
            - datasets
          properties:
            role:
              $ref: '#/components/schemas/OrganizationMemberRole'
            datasets:
              description: >-
                Only used for 'guest' users. Limits the datasets the user has
                access to.
              type: array
              items:
                type: string
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
    AdminAddUserRequest:
      type: object
      properties:
        usernameOrEmail:
          type: string
          example: janjongboom
          description: >-
            Username or email of the user to be added to the project or
            organization. If no user is provided, the user ID attached to the
            JWT will be used.
    OrganizationMemberRole:
      type: string
      enum:
        - admin
        - member
        - guest
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