# Source: https://docs.edgeimpulse.com/apis/studio/organizationportals/update-upload-portal.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update upload portal

> Updates an upload portal for the organization.



## OpenAPI

````yaml .assets/openapi.yaml put /api/organizations/{organizationId}/portals/{portalId}/update
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
  /api/organizations/{organizationId}/portals/{portalId}/update:
    put:
      tags:
        - OrganizationPortals
      summary: Update upload portal
      description: Updates an upload portal for the organization.
      operationId: updateOrganizationPortal
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/PortalIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateOrganizationPortalRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateOrganizationPortalResponse'
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
    CreateOrganizationPortalRequest:
      type: object
      required:
        - name
        - bucketId
        - bucketPath
      properties:
        name:
          type: string
          example: EdgeImpulse Inc.
          description: The name of the upload portal.
        description:
          type: string
          example: EdgeImpulse Inc. Portal description
          description: The purpose and description of the upload portal.
        bucketId:
          type: integer
          example: 1
          description: >-
            The S3 bucket id to store the uploaded data. Set to '0' to select a
            bucket hosted by Edge Impulse.
        bucketPath:
          type: string
          example: /path/in/bucket
          description: The path in the bucket the upload portal will write to.
    UpdateOrganizationPortalResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - url
          properties:
            url:
              type: string
              description: URL to the portal
            signedUrl:
              type: string
              description: >-
                pre-signed upload URL, only set if not using the Edge Impulse
                hosted bucket.
            bucketBucket:
              type: string
              description: Only set if not using the Edge Impulse hosted bucket.
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