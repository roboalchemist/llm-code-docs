# Source: https://docs.edgeimpulse.com/apis/studio/user/list-emails.md

# Source: https://docs.edgeimpulse.com/apis/studio/projects/list-emails.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List emails

> Get a list of all emails sent by Edge Impulse regarding this project.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/emails
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
  /api/{projectId}/emails:
    get:
      tags:
        - Projects
      summary: List emails
      description: Get a list of all emails sent by Edge Impulse regarding this project.
      operationId: listEmails
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListEmailResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
  schemas:
    ListEmailResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - emails
          properties:
            emails:
              type: array
              description: List of emails
              items:
                type: object
                required:
                  - from
                  - to
                  - created
                  - subject
                  - bodyText
                  - bodyHTML
                  - sent
                  - providerResponse
                properties:
                  userId:
                    type: integer
                  projectId:
                    type: integer
                  from:
                    type: string
                  to:
                    type: string
                  created:
                    type: string
                    format: date-time
                  subject:
                    type: string
                  bodyText:
                    type: string
                  bodyHTML:
                    type: string
                  sent:
                    type: boolean
                  providerResponse:
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