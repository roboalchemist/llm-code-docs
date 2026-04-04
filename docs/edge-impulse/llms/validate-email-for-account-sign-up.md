# Source: https://docs.edgeimpulse.com/apis/studio/emailverification/validate-email-for-account-sign-up.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Validate email for account sign-up

> Validate whether an email is valid for sign up. Using an email that fails this check can result in the associated account missing communications and features that are distributed through email.



## OpenAPI

````yaml .assets/openapi.yaml post /api/emails/validate
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
  /api/emails/validate:
    post:
      tags:
        - EmailVerification
      summary: Validate email for account sign-up
      description: >-
        Validate whether an email is valid for sign up. Using an email that
        fails this check can result in the associated account missing
        communications and features that are distributed through email.
      operationId: validateEmail
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EmailValidationRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ValidateEmailResponse'
      security: []
components:
  schemas:
    EmailValidationRequest:
      type: object
      required:
        - email
      properties:
        email:
          type: string
          description: E-mail address to validate
          example: jan@edgeimpulse.com
    ValidateEmailResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - email
            - verdict
            - score
          properties:
            email:
              type: string
              description: Email address that was checked.
            verdict:
              type: string
              description: Classification of the email's validity status
              enum:
                - Valid
                - Risky
                - Invalid
            score:
              type: number
              example: 0.98015
              description: >-
                This number from 0 to 1 represents the likelihood the email
                address is valid, expressed as a percentage.
            suggestion:
              type: string
              example: gmail.com
              description: A corrected domain, if a possible typo is detected.
            local:
              type: string
              example: jan.jongboom
              description: The first part of the email address (before the @ sign)
            host:
              type: string
              example: edgeimpulse.com
              description: The second part of the email address (after the @ sign)
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