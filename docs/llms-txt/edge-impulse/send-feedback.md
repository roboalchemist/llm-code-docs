# Source: https://docs.edgeimpulse.com/apis/studio/user/send-feedback.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Send feedback

> Send feedback to Edge Impulse or get in touch with sales.



## OpenAPI

````yaml .assets/openapi.yaml post /api/users/{userId}/feedback
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
  /api/users/{userId}/feedback:
    post:
      tags:
        - User
      summary: Send feedback
      description: Send feedback to Edge Impulse or get in touch with sales.
      operationId: sendUserFeedback
      parameters:
        - $ref: '#/components/parameters/UserIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SendUserFeedbackRequest'
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
    SendUserFeedbackRequest:
      type: object
      required:
        - type
        - subject
        - body
      properties:
        type:
          type: string
          enum:
            - feedback
        subject:
          type: string
          description: The reason the user is contacting Edge Impulse Support.
        body:
          type: string
          description: The body of the message.
        workEmail:
          type: string
          description: >-
            The user's work email address. This is optional, if it's not
            provided, the registered email will be used.
        company:
          type: string
          description: The user's company. This is optional.
        jobTitle:
          type: string
          description: The user's job title. This is optional.
        companySize:
          type: string
          description: The user's company size. This is optional.
        organizationId:
          type: number
          description: The user's organization ID. This is optional.
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