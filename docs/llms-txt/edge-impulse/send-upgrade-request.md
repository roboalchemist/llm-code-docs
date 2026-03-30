# Source: https://docs.edgeimpulse.com/apis/studio/user/send-upgrade-request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Send upgrade request

> Send an upgrade to Enterprise request to Edge Impulse.



## OpenAPI

````yaml .assets/openapi.yaml post /api/users/{userId}/upgrade
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
  /api/users/{userId}/upgrade:
    post:
      tags:
        - User
      summary: Send upgrade request
      description: Send an upgrade to Enterprise request to Edge Impulse.
      operationId: sendUserUpgradeRequest
      parameters:
        - $ref: '#/components/parameters/UserIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EnterpriseUpgradeOrTrialExtensionRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenericApiResponse'
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
    EnterpriseUpgradeOrTrialExtensionRequest:
      type: object
      properties:
        reason:
          type: string
          description: >-
            Answer to the question: 'Why is this the right time for your team to
            invest in edge AI?'. This is optional.
        useCase:
          type: string
          description: >-
            Answer to the question: 'What best describes your use case?'. This
            is optional.
        timeline:
          type: string
          description: >-
            Answer to the question: 'What is your timeline for solving your
            problem?'. This is optional.
        objective:
          type: string
          description: >-
            Answer to the question: 'What are you hoping to achieve with an
            extension?'. This is optional.
        trialId:
          type: number
          description: The user's trial ID. This is optional.
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