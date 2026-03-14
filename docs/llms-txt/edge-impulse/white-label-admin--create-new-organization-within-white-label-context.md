# Source: https://docs.edgeimpulse.com/apis/studio/organizations/white-label-admin--create-new-organization-within-white-label-context.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# White Label Admin - Create new organization within white label context

> Create a new organization. This is an API only available to white label admins



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/whitelabel/organizations
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
  /api/organizations/{organizationId}/whitelabel/organizations:
    post:
      tags:
        - Organizations
      summary: White Label Admin - Create new organization within white label context
      description: >-
        Create a new organization. This is an API only available to white label
        admins
      operationId: whitelabelAdminCreateOrganization
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/WhitelabelAdminCreateOrganizationRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateOrganizationResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
  schemas:
    WhitelabelAdminCreateOrganizationRequest:
      type: object
      required:
        - organizationName
      properties:
        organizationName:
          type: string
          example: EdgeImpulse Inc.
          description: The name of the organization.
        adminId:
          type: integer
          example: 1
          description: Unique identifier of the administrator of the new organization.
        adminEmail:
          type: string
          example: jan@edgeimpulse.com
          description: Email of the administrator of the new organization.
    CreateOrganizationResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - id
            - apiKey
          properties:
            id:
              type: integer
              description: Organization ID for the new organization
            apiKey:
              type: string
              description: API key for the new organization (this is shown only once)
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