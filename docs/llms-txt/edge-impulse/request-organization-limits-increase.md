# Source: https://docs.edgeimpulse.com/apis/studio/organizations/request-organization-limits-increase.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Request organization limits increase

> Request an increase in the limits for this organization. Available limits are: users, projects, compute, storage.



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/limits-request
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
  /api/organizations/{organizationId}/limits-request:
    post:
      tags:
        - Organizations
      summary: Request organization limits increase
      description: >-
        Request an increase in the limits for this organization. Available
        limits are: users, projects, compute, storage.
      operationId: requestEnterpriseLimitsIncrease
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EnterpriseLimitsIncreaseRequest'
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
  schemas:
    EnterpriseLimitsIncreaseRequest:
      type: object
      required:
        - limits
      properties:
        limits:
          type: array
          items:
            $ref: '#/components/schemas/EnterpriseLimit'
        reason:
          type: string
          description: Additional notes for the request. This is optional.
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
    EnterpriseLimit:
      type: string
      enum:
        - users
        - projects
        - compute
        - storage
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