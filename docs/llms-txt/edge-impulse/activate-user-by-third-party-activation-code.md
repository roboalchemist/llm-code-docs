# Source: https://docs.edgeimpulse.com/apis/studio/user/activate-user-by-third-party-activation-code.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Activate user by third party activation code

> Activate a user that was created by a third party. This function is only available through a JWT token.



## OpenAPI

````yaml .assets/openapi.yaml post /api/user/activate-by-third-party-activation-code
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
  /api/user/activate-by-third-party-activation-code:
    post:
      tags:
        - User
      summary: Activate user by third party activation code
      description: >-
        Activate a user that was created by a third party. This function is only
        available through a JWT token.
      operationId: activateUserByThirdPartyActivationCode
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/ActivateUserByThirdPartyActivationCodeRequest
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetJWTResponse'
components:
  schemas:
    ActivateUserByThirdPartyActivationCodeRequest:
      type: object
      required:
        - activationCode
        - password
        - username
      properties:
        activationCode:
          type: string
        password:
          type: string
          description: Password, minimum length 8 characters.
        name:
          type: string
          description: Your name
          example: Jan Jongboom
        username:
          type: string
          description: >-
            Username, minimum 4 and maximum 30 characters. May contain
            alphanumeric characters, hyphens, underscores and dots. Validated
            according to
            `^(?=.{4,30}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._-]+(?<![_.])$`.
          example: janjongboom
        privacyPolicy:
          type: boolean
          description: Whether the user accepted the privacy policy
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