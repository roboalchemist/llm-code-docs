# Source: https://docs.edgeimpulse.com/apis/studio/organizations/set-member-datasets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set member datasets

> Set the datasets a guest member has access to in an organization.



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/members/{memberId}/datasets
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
  /api/organizations/{organizationId}/members/{memberId}/datasets:
    post:
      tags:
        - Organizations
      summary: Set member datasets
      description: Set the datasets a guest member has access to in an organization.
      operationId: setOrganizationMemberDatasets
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/MemberIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SetMemberDatasetsRequest'
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
    MemberIdParameter:
      name: memberId
      in: path
      required: true
      description: Member ID
      schema:
        type: integer
  schemas:
    SetMemberDatasetsRequest:
      type: object
      required:
        - datasets
      properties:
        datasets:
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