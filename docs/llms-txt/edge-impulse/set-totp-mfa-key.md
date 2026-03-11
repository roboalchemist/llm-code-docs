# Source: https://docs.edgeimpulse.com/apis/studio/user/set-totp-mfa-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set TOTP MFA key

> Enable MFA on this account using an TOTP token. First create a new key via `userGenerateNewTotpMfaKey`.



## OpenAPI

````yaml .assets/openapi.yaml post /api/user/mfa/totp/set-key
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
  /api/user/mfa/totp/set-key:
    post:
      tags:
        - User
      summary: Set TOTP MFA key
      description: >-
        Enable MFA on this account using an TOTP token. First create a new key
        via `userGenerateNewTotpMfaKey`.
      operationId: userSetTotpMfaKey
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserSetTotpMfaKeyRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserSetTotpMfaKeyResponse'
components:
  schemas:
    UserSetTotpMfaKeyRequest:
      type: object
      required:
        - key
        - totpToken
      properties:
        key:
          type: string
          description: Secret key obtained through `userGenerateNewMfaKey`.
        totpToken:
          type: string
          description: >-
            TOTP token that is valid for the key (to ensure the device is
            configured correctly)
    UserSetTotpMfaKeyResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - recoveryCodes
          properties:
            recoveryCodes:
              type: array
              description: >-
                10 recovery codes, which can be used in case you've lost access
                to your MFA TOTP app. Recovery codes are single use. Once you've
                used a recovery code once, it can not be used again.
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