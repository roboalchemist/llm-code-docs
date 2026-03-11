# Source: https://docs.edgeimpulse.com/apis/studio/user/update-current-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update current user

> Update user properties such as name. This function is only available through a JWT token.



## OpenAPI

````yaml .assets/openapi.yaml post /api/user
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
  /api/user:
    post:
      tags:
        - User
      summary: Update current user
      description: >-
        Update user properties such as name. This function is only available
        through a JWT token.
      operationId: updateCurrentUser
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateUserRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenericApiResponse'
components:
  schemas:
    UpdateUserRequest:
      type: object
      description: Only fields set in this object will be updated.
      properties:
        name:
          type: string
          description: New full name
          example: Jan Jongboom
        jobTitle:
          type: string
          description: New job title
          example: Embedded Software Engineer
        companyName:
          type: string
          description: New company name
          example: Edge Impulse Inc.
        experiments:
          type: array
          items:
            type: string
          description: List of user experiments
        projectsSortOrder:
          $ref: '#/components/schemas/UserProjectsSortOrder'
          description: Default sort order on the projects list
        timezone:
          description: User timezone.
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
    UserProjectsSortOrder:
      type: string
      enum:
        - created-asc
        - created-desc
        - added-asc
        - added-desc
        - name-asc
        - name-desc
        - last-accessed-desc
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