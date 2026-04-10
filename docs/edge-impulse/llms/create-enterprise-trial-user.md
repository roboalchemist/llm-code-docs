# Source: https://docs.edgeimpulse.com/apis/studio/user/create-enterprise-trial-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create enterprise trial user

> Creates an enterprise trial user and a new trial organization, and redirects the user to the new organization. This API is internal (it requires some signed fields), sign up at https://studio.edgeimpulse.com/signup instead.



## OpenAPI

````yaml .assets/openapi.yaml post /api-user-create-enterprise-trial
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
  /api-user-create-enterprise-trial:
    post:
      tags:
        - User
      summary: Create enterprise trial user
      description: >-
        Creates an enterprise trial user and a new trial organization, and
        redirects the user to the new organization. This API is internal (it
        requires some signed fields), sign up at
        https://studio.edgeimpulse.com/signup instead.
      operationId: createEnterpriseTrialUser
      requestBody:
        description: Trial request
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateEnterpriseTrialUserRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateEnterpriseTrialResponse'
      security: []
components:
  schemas:
    CreateEnterpriseTrialUserRequest:
      allOf:
        - $ref: '#/components/schemas/StartEnterpriseTrialRequest'
        - type: object
          required:
            - name
            - username
            - email
            - privacyPolicy
            - turnstileResponse
          properties:
            name:
              type: string
              description: Name of the user.
              example: John Doe
            username:
              type: string
              description: >-
                Username, minimum 4 and maximum 30 characters. May contain
                alphanumeric characters, hyphens, underscores and dots.
                Validated according to
                `^(?=.{4,30}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._-]+(?<![_.])$`.
              example: johndoe
            email:
              type: string
              description: >-
                Email of the user. Only business email addresses are allowed.
                Emails with free domains like gmail.com or yahoo.com are not
                allowed.
              example: jan@edgeimpulse.com
            privacyPolicy:
              type: boolean
              description: >-
                Whether the user has accepted the terms of service and privacy
                policy.
            password:
              type: string
              description: Password of the user. Minimum length 8 characters.
            jobTitle:
              type: string
              description: Job title of the user.
              example: TinyML engineer
            companyName:
              type: string
              description: Name of the company requesting the trial.
              example: ACME Inc.
            redirectUrlOrigin:
              type: string
              description: >-
                Origin of the redirect URL returned as result of creating the
                trial user.
              example: https://studio.edgeimpulse.com
            redirectUrlQueryParams:
              type: string
              description: >-
                Query parameters to be appended to the redirect URL returned as
                result of creating the trial user.
              example: utm_source=google&utm_medium=cpc&utm_campaign=trial
            utmParams:
              type: array
              description: List of UTM parameters.
              items:
                $ref: '#/components/schemas/UtmParameter'
            turnstileResponse:
              type: string
              description: CloudFlare Turnstile response token
    CreateEnterpriseTrialResponse:
      allOf:
        - $ref: '#/components/schemas/EntityCreatedResponse'
        - type: object
          properties:
            userId:
              type: integer
              description: >-
                ID of the user created for the trial, if the user did not
                already exist.
            redirectUrl:
              type: string
              description: >-
                URL to redirect the user to in order to access the enterprise
                trial.
    StartEnterpriseTrialRequest:
      type: object
      properties:
        email:
          type: string
          description: >-
            Email of the user requesting the trial. If this email is different
            to the one stored for the user requesting the trial, it will be used
            to replace the existing one.
          example: fred@flintstones.org
        name:
          type: string
          description: >-
            Name of the user requesting the trial. If this name is different to
            the one stored for the user requesting the trial, it will be used to
            replace the existing one.
          example: Fred Flintstone
        organizationName:
          type: string
          description: >-
            Name of the trial organization. All enterprise features are tied to
            an organization. This organization will be deleted after the trial
            ends. If no organization name is provided, the user's name will be
            used.
          example: My Company
        expirationDate:
          $ref: '#/components/schemas/TrialExpirationDate'
        notes:
          $ref: '#/components/schemas/TrialNotes'
        useCase:
          type: string
          description: Use case of the trial.
          example: Industrial
        userHasMLModelsInProduction:
          type: string
          enum:
            - 'yes'
            - 'no'
            - no, but we will soon
          description: Whether the user has ML models in production.
          example: 'no'
        companyName:
          type: string
          description: Name of the company requesting the trial.
          example: ACME Inc.
        companySize:
          type: string
          description: >-
            Size of the company requesting the trial. This is a range of number
            of employees.
          example: 1-10
        country:
          type: string
          description: Country of the company requesting the trial.
          example: United States
        stateOrProvince:
          type: string
          description: State or province of the company requesting the trial.
          example: California
        redirectUrlOrigin:
          type: string
          description: >-
            Origin of the redirect URL returned as result of creating the trial
            user.
          example: https://studio.edgeimpulse.com
        redirectUrlQueryParams:
          type: string
          description: >-
            Query parameters to be appended to the redirect URL returned as
            result of creating the trial user.
          example: utm_source=google&utm_medium=cpc&utm_campaign=trial
    UtmParameter:
      type: object
      additionalProperties: true
    EntityCreatedResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - id
          properties:
            id:
              type: integer
              description: Unique identifier of the created entity.
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