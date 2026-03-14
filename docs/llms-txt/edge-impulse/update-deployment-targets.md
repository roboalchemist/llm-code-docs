# Source: https://docs.edgeimpulse.com/apis/studio/whitelabels/update-deployment-targets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update deployment targets

> Update some or all of the deployment targets enabled for this white label.



## OpenAPI

````yaml .assets/openapi.yaml post /api/whitelabel/{whitelabelIdentifier}/deploymentTargets
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
  /api/whitelabel/{whitelabelIdentifier}/deploymentTargets:
    post:
      tags:
        - Whitelabels
      summary: Update deployment targets
      description: >-
        Update some or all of the deployment targets enabled for this white
        label.
      operationId: updateDeploymentTargets
      parameters:
        - $ref: '#/components/parameters/WhitelabelIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateWhitelabelDeploymentTargetsRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenericApiResponse'
components:
  parameters:
    WhitelabelIdParameter:
      name: whitelabelIdentifier
      in: path
      required: true
      description: Whitelabel ID
      schema:
        type: integer
  schemas:
    UpdateWhitelabelDeploymentTargetsRequest:
      type: object
      properties:
        targets:
          type: array
          description: >-
            The names of the deployment targets that are enabled for this
            whitelabel.
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