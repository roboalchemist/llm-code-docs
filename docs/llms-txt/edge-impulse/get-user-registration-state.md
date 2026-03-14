# Source: https://docs.edgeimpulse.com/apis/studio/user/get-user-registration-state.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get user registration state

> Tells whether a user is registered and whether it needs to set its password.



## OpenAPI

````yaml .assets/openapi.yaml get /api-user-need-to-set-password/{usernameOrEmail}
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
  /api-user-need-to-set-password/{usernameOrEmail}:
    get:
      tags:
        - User
      summary: Get user registration state
      description: >-
        Tells whether a user is registered and whether it needs to set its
        password.
      operationId: getUserNeedToSetPassword
      parameters:
        - $ref: '#/components/parameters/UsernameOrEmailParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetUserNeedToSetPasswordResponse'
      security: []
components:
  parameters:
    UsernameOrEmailParameter:
      name: usernameOrEmail
      in: path
      required: true
      description: Username or email
      schema:
        type: string
  schemas:
    GetUserNeedToSetPasswordResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          properties:
            email:
              type: string
              description: User email
            needPassword:
              type: boolean
              description: Whether the user needs to set its password or not
            whitelabels:
              type: array
              items:
                type: string
              description: White label domains the user belongs to, if any
            trials:
              type: array
              description: Current or past enterprise trials.
              items:
                $ref: '#/components/schemas/EnterpriseTrial'
            emailVerified:
              type: boolean
              description: Whether the user has verified its email address or not
            idps:
              type: array
              description: >-
                List of unique identifiers for identity providers associated
                with the user.
              example:
                - okta
                - google
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
    EnterpriseTrial:
      type: object
      required:
        - id
        - userId
        - created
        - organizationId
        - expirationDate
        - expiredDate
        - deletedDate
        - upgradedDate
      properties:
        id:
          type: integer
          description: Unique identifier of the trial.
        userId:
          type: integer
          description: ID of the user who created the trial.
        organizationId:
          type: integer
          description: ID of the organization created for the trial.
        created:
          type: string
          format: date-time
          description: >-
            Date when the trial was created. Trials start immediately on
            creation.
        expirationDate:
          $ref: '#/components/schemas/TrialExpirationDate'
        notes:
          $ref: '#/components/schemas/TrialNotes'
        expiredDate:
          type: string
          format: date-time
          nullable: true
          description: >-
            Date when the trial actually expired. This is set when the trial is
            expired by the system.
        deletedDate:
          type: string
          format: date-time
          nullable: true
          description: >-
            Date when the trial was deleted. This is set when the trial is
            fully  deleted by the system.
        upgradedDate:
          type: string
          format: date-time
          nullable: true
          description: Date when the trial was upgraded to a full enterprise account.
    TrialExpirationDate:
      type: string
      format: date-time
      description: >-
        Expiration date of the trial. The trial will be set as expired after
        this date. There will be a grace period of 30 days after a trial expires
        before fully deleting the trial organization. This field is ignored if
        the trial is requested by a non-admin user, defaulting to 14 days trial.
      example: '2020-01-01T00:00:00Z'
    TrialNotes:
      type: string
      description: >-
        Notes about the trial. Free form text. This field is ignored if the
        trial is requested by a non-admin user.
      example: This is a trial for the company's new project.
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