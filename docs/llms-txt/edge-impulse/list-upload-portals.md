# Source: https://docs.edgeimpulse.com/apis/studio/organizationportals/list-upload-portals.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List upload portals

> Retrieve all configured upload portals.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/portals
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
  /api/organizations/{organizationId}/portals:
    get:
      tags:
        - OrganizationPortals
      summary: List upload portals
      description: Retrieve all configured upload portals.
      operationId: listOrganizationPortals
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListOrganizationPortalsResponse'
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
    ListOrganizationPortalsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - portals
          properties:
            portals:
              type: array
              items:
                type: object
                required:
                  - id
                  - name
                  - url
                  - token
                  - bucketId
                  - bucketName
                  - bucketPath
                  - bucketUrl
                  - created
                properties:
                  id:
                    type: integer
                  name:
                    type: string
                  description:
                    type: string
                  url:
                    type: string
                  bucketId:
                    type: integer
                  bucketName:
                    type: string
                  bucketPath:
                    type: string
                  bucketUrl:
                    type: string
                  storageProvider:
                    type: string
                  created:
                    type: string
                    format: date-time
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