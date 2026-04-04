# Source: https://docs.edgeimpulse.com/apis/studio/user/generate-a-new-totp-mfa-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate a new TOTP MFA key

> Creates a new MFA key, only allowed if the user has no MFA configured. TOTP tokens use SHA-1 algorithm.



## OpenAPI

````yaml .assets/openapi.yaml post /api/user/mfa/totp/create-key
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
  /api/user/mfa/totp/create-key:
    post:
      tags:
        - User
      summary: Generate a new TOTP MFA key
      description: >-
        Creates a new MFA key, only allowed if the user has no MFA configured.
        TOTP tokens use SHA-1 algorithm.
      operationId: userGenerateNewTotpMfaKey
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserGenerateNewMfaKeyResponse'
components:
  schemas:
    UserGenerateNewMfaKeyResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - key
            - url
          properties:
            key:
              type: string
              description: Secret key (use SHA-1).
            url:
              type: string
              description: URL that will be converted into a QR code that can be scanned.
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