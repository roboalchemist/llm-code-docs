# Source: https://docs.edgeimpulse.com/apis/studio/login/get-jwt-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get JWT token

> Get a JWT token to authenticate with the API.



## OpenAPI

````yaml .assets/openapi.yaml post /api-login
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
  /api-login:
    post:
      tags:
        - Login
      summary: Get JWT token
      description: Get a JWT token to authenticate with the API.
      operationId: login
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GetJWTRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetJWTResponse'
      security: []
components:
  schemas:
    GetJWTRequest:
      type: object
      required:
        - username
        - password
      properties:
        username:
          type: string
          description: Username or e-mail address
          example: edge-user-01
        password:
          type: string
          description: Password
        uuid:
          type: string
          description: Evaluation user UUID
        ssoType:
          type: string
          enum:
            - browser
            - cli
        sessionId:
          type: string
          description: Session ID
        totpToken:
          type: string
          description: >-
            TOTP Token. Required if a user has multi-factor authentication with
            a TOTP token enabled. If a user has MFA enabled, but no totpToken is
            submitted; then an error starting with "ERR_TOTP_TOKEN IS REQUIRED"
            is returned. Use this to then prompt for an MFA token and re-login.
    GetJWTResponse:
      example: '`{ "success": true, "token": "A372jdhe.ad3r4gfrg" }`'
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          properties:
            token:
              type: string
              description: >-
                JWT token, to be used to log in in the future through
                JWTAuthentication
            redirectUrl:
              type: string
              description: Redirect URL to follow to complete login
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