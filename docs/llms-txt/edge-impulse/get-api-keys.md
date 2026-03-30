# Source: https://docs.edgeimpulse.com/apis/studio/projects/get-api-keys.md

# Source: https://docs.edgeimpulse.com/apis/studio/organizations/get-api-keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get API keys

> Retrieve all API keys. This does **not** return the full API key, but only a portion (for security purposes).



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/apikeys
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
    get:
      tags:
        - Organizations
      summary: Get API keys
      description: >-
        Retrieve all API keys. This does **not** return the full API key, but
        only a portion (for security purposes).
      operationId: listOrganizationApiKeys
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListOrganizationApiKeysResponse'
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
    ListOrganizationApiKeysResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - apiKeys
          properties:
            apiKeys:
              type: array
              description: List of API keys.
              items:
                $ref: '#/components/schemas/OrganizationApiKey'
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
    OrganizationApiKey:
      type: object
      required:
        - id
        - name
        - apiKey
        - created
        - role
        - isTransformationJobKey
      properties:
        id:
          type: integer
        apiKey:
          type: string
        name:
          type: string
        created:
          type: string
          format: date-time
        role:
          type: string
          enum:
            - admin
            - member
        isTransformationJobKey:
          type: boolean
        createdByUser:
          $ref: '#/components/schemas/CreatedUpdatedByUser'
        lastUsed:
          description: When this API key was last used.
          type: object
          required:
            - date
          properties:
            date:
              type: string
              format: date-time
            country:
              type: string
              example: United States
              description: If available, the country from which the API key was last used.
            ipAddress:
              type: string
              description: >-
                If available, the IP address from which the API key was last
                used.
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