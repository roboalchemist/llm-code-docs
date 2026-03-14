# Source: https://docs.edgeimpulse.com/apis/studio/user/get-buckets-current-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get buckets current user

> List all organizational storage buckets that the current user has access to. This function is only available through a JWT token.



## OpenAPI

````yaml .assets/openapi.yaml get /api/users/buckets
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
  /api/users/buckets:
    get:
      tags:
        - User
      summary: Get buckets current user
      description: >-
        List all organizational storage buckets that the current user has access
        to. This function is only available through a JWT token.
      operationId: listOrganizationBucketsCurrentUser
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListOrganizationBucketsUserResponse'
components:
  schemas:
    ListOrganizationBucketsUserResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - buckets
          properties:
            buckets:
              type: array
              items:
                type: object
                required:
                  - id
                  - organizationId
                  - organizationName
                  - bucket
                  - region
                  - whitelabelId
                properties:
                  id:
                    type: integer
                  organizationId:
                    type: integer
                  organizationName:
                    type: string
                  bucket:
                    type: string
                    description: S3 bucket
                  region:
                    type: string
                    description: S3 region
                  whitelabelId:
                    type: integer
                    description: >-
                      The unique identifier of the white label this bucket
                      belongs to, if any
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