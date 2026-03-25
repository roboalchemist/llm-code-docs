# Source: https://docs.edgeimpulse.com/apis/studio/user/get-enterprise-trials.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get enterprise trials

> Get a list of all enterprise trials for a user. This function is only available through a JWT token.



## OpenAPI

````yaml .assets/openapi.yaml get /api/users/{userId}/trials
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
  /api/users/{userId}/trials:
    get:
      tags:
        - User
      summary: Get enterprise trials
      description: >-
        Get a list of all enterprise trials for a user. This function is only
        available through a JWT token.
      operationId: listEnterpriseTrialsUser
      parameters:
        - $ref: '#/components/parameters/UserIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListEnterpriseTrialsResponse'
components:
  parameters:
    UserIdParameter:
      name: userId
      in: path
      required: true
      description: User ID
      schema:
        type: integer
  schemas:
    ListEnterpriseTrialsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - trials
          properties:
            trials:
              type: array
              description: Current or past enterprise trials.
              items:
                $ref: '#/components/schemas/EnterpriseTrial'
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