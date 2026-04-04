# Source: https://docs.edgeimpulse.com/apis/studio/organizationblocks/get-secrets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get secrets

> Retrieve all secrets.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/secrets
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
  /api/organizations/{organizationId}/secrets:
    get:
      tags:
        - OrganizationBlocks
      summary: Get secrets
      description: Retrieve all secrets.
      operationId: listOrganizationSecrets
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListOrganizationSecretsResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
  schemas:
    ListOrganizationSecretsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - secrets
          properties:
            secrets:
              type: array
              items:
                type: object
                required:
                  - id
                  - name
                  - description
                  - created
                properties:
                  id:
                    type: integer
                  name:
                    type: string
                  description:
                    type: string
                  created:
                    type: string
                    format: date-time
                  createdByUser:
                    $ref: '#/components/schemas/CreatedUpdatedByUser'
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
    CreatedUpdatedByUser:
      type: object
      required:
        - id
        - name
        - username
      properties:
        id:
          type: integer
        name:
          type: string
        username:
          type: string
        photo:
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