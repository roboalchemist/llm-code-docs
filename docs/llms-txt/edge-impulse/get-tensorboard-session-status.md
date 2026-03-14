# Source: https://docs.edgeimpulse.com/apis/studio/integrations/get-tensorboard-session-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get TensorBoard session status

> Get the status of a TensorBoard session



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/integrations/tensorboard/{resourceId}
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
  /api/{projectId}/integrations/tensorboard/{resourceId}:
    get:
      tags:
        - Integrations
      summary: Get TensorBoard session status
      description: Get the status of a TensorBoard session
      operationId: getTensorBoardSessionStatus
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/IntegrationResourceIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetIntegrationSessionStatusResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    IntegrationResourceIdParameter:
      name: resourceId
      in: path
      required: true
      description: |
        Unique resource ID for an integration session.
        When an integration is launched we create a new session for it.
        Each session is uniquely identifiable by the project ID and resource ID.
      example: learn-3-2-1
      schema:
        type: string
  schemas:
    GetIntegrationSessionStatusResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - sessionStatus
          properties:
            sessionStatus:
              $ref: '#/components/schemas/IntegrationSessionStatus'
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
    IntegrationSessionStatus:
      type: object
      required:
        - status
      properties:
        status:
          description: Integration session status
          type: string
          enum:
            - pending
            - active
            - error
            - stopped
        additionalInfo:
          description: >-
            Any relevant additional information, e.g. the reason the session has
            stopped or any error messages.
          type: string
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