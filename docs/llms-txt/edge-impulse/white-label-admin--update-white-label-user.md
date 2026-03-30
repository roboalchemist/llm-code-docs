# Source: https://docs.edgeimpulse.com/apis/studio/organizations/white-label-admin--update-white-label-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# White Label Admin - Update white label user

> White label admin only API to update user properties.



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/whitelabel/users/{userId}
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
  /api/organizations/{organizationId}/whitelabel/users/{userId}:
    post:
      tags:
        - Organizations
      summary: White Label Admin - Update white label user
      description: White label admin only API to update user properties.
      operationId: whitelabelAdminUpdateUser
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/UserIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AdminUpdateUserRequest'
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
    UserIdParameter:
      name: userId
      in: path
      required: true
      description: User ID
      schema:
        type: integer
  schemas:
    AdminUpdateUserRequest:
      type: object
      description: Only fields set in this object will be updated.
      properties:
        email:
          type: string
          description: >-
            New email. This will also update the forum's email address but the
            user may need to logout/login back
          example: quijote@lamancha.es
        name:
          type: string
          description: New user full name
          example: Don Quijote de la Mancha
        activated:
          type: boolean
          description: >-
            Whether the user is active or not. Can only go from inactive to
            active.
          example: true
        suspended:
          type: boolean
          description: Whether the user is suspended or not.
          example: false
        suspensionReason:
          type: string
          description: Reason for suspension
          example: Spamming the forum
        jobTitle:
          type: string
          description: New user job title
          example: Knight
        experiments:
          type: array
          items:
            type: string
          description: List of user experiments
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