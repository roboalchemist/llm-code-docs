# Source: https://docs.edgeimpulse.com/apis/studio/user/create-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create user

> Create a new user and project. This API is no longer publicly available. Sign up at https://studio.edgeimpulse.com/signup instead.



## OpenAPI

````yaml .assets/openapi.yaml post /api-user-create
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
  /api-user-create:
    post:
      tags:
        - User
      summary: Create user
      description: >-
        Create a new user and project. This API is no longer publicly available.
        Sign up at https://studio.edgeimpulse.com/signup instead.
      operationId: createUser
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateUserResponse'
      security: []
components:
  schemas:
    CreateUserRequest:
      type: object
      required:
        - name
        - username
        - email
        - privacyPolicy
        - turnstileResponse
      properties:
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
        email:
          type: string
          description: >-
            E-mail address. Will need to be validated before the account will
            become active.
          example: jan@edgeimpulse.com
        password:
          type: string
          description: Password, minimum length 8 characters.
        projectName:
          type: string
          description: >-
            A project will automatically be created. Sets the name of the first
            project. If not set, this will be derived from the username.
        privacyPolicy:
          type: boolean
          description: Whether the user accepted the privacy policy
        activationToken:
          type: string
          description: Activation token for users created via SSO
        identityProvider:
          type: string
          description: >-
            Unique identifier of the identity provider asserting the identity of
            this user
        jobTitle:
          type: string
          description: Job title of the user. Optional field
        sessionId:
          type: string
          description: Session ID. Optional field
        companyName:
          type: string
          description: ACME Inc.
        utmParams:
          type: array
          description: List of UTM parameters.
          items:
            $ref: '#/components/schemas/UtmParameter'
        ignoreEmailValidation:
          type: boolean
          description: >-
            If true, allows signup to proceed despite a potentially invalid
            email. Note that this will enforce email verification post-signup
        turnstileResponse:
          type: string
          description: CloudFlare Turnstile response token
        dateOfBirth:
          type: string
          format: date
          description: Date of birth of the user in YYYY-MM-DD format. Optional field.
        approverEmail:
          type: string
          description: Email address to be used for signup approval. Optional field.
    CreateUserResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          properties:
            redirectUrl:
              type: string
              description: URL to redirect user to.
            id:
              type: integer
              description: User unique identifier
    UtmParameter:
      type: object
      additionalProperties: true
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