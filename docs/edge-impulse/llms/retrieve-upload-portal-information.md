# Source: https://docs.edgeimpulse.com/apis/studio/organizationportals/retrieve-upload-portal-information.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve upload portal information

> Retrieve a single upload portals identified by ID.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/portals/{portalId}
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
  /api/organizations/{organizationId}/portals/{portalId}:
    get:
      tags:
        - OrganizationPortals
      summary: Retrieve upload portal information
      description: Retrieve a single upload portals identified by ID.
      operationId: getOrganizationPortal
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/PortalIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetOrganizationPortalResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
    PortalIdParameter:
      name: portalId
      in: path
      required: true
      description: Portal ID
      schema:
        type: integer
  schemas:
    GetOrganizationPortalResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - id
            - name
            - url
            - token
            - bucketName
            - bucketPath
          properties:
            id:
              type: integer
              description: Portal ID for the new upload portal
            name:
              type: string
              example: EdgeImpulse Inc.
              description: The name of the upload portal.
            description:
              type: string
              example: EdgeImpulse Inc. Portal description
              description: The purpose and description of the upload portal.
            url:
              type: string
              example: edgeImpulse
              description: The url postfix of the upload portal.
            token:
              type: string
              example: SECRET_TOKEN
              description: The token used to validate access to the upload portal.
            bucketName:
              type: string
              example: my-s3-bucket
              description: The S3 bucket name to store the uploaded data.
            bucketId:
              type: integer
              example: 1
              description: >-
                S3 bucket ID. If missing, then this is using the Edge Impulse
                hosted bucket.
            bucketPath:
              type: string
              example: /path/to/bucket
              description: The S3 bucket path where uploaded data is stored.
            bucketUrl:
              type: string
              example: s3://bucketname/path/to/bucket
              description: The full S3 bucket path where uploaded data is stored.
            storageProvider:
              type: string
              example: s3
              description: The storage provider type (s3, azure, google, other).
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