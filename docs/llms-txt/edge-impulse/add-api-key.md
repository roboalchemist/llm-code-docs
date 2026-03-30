# Source: https://docs.edgeimpulse.com/apis/studio/projects/add-api-key.md

# Source: https://docs.edgeimpulse.com/apis/studio/organizations/add-api-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add API key

> Add an API key.



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/apikeys
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
  /api/organizations/{organizationId}/apikeys:
    post:
      tags:
        - Organizations
      summary: Add API key
      description: Add an API key.
      operationId: addOrganizationApiKey
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AddOrganizationApiKeyRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AddApiKeyResponse'
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
    AddOrganizationApiKeyRequest:
      allOf:
        - $ref: '#/components/schemas/AddApiKeyRequest'
        - type: object
          required:
            - role
          properties:
            role:
              type: string
              enum:
                - admin
                - member
    AddApiKeyResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - id
            - apiKey
          properties:
            id:
              type: integer
              description: ID of the new API key
            apiKey:
              type: string
              description: >-
                New API Key (starts with "ei_...") - this'll be shared only
                once.
    AddApiKeyRequest:
      type: object
      required:
        - name
      properties:
        name:
          type: string
          description: Description of the key
        apiKey:
          type: string
          description: >-
            Optional: API key. This needs to start with `ei_` and will need to
            be at least 32 characters long. If this field is not passed in, a
            new API key is generated for you.
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