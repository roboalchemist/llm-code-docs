# Source: https://docs.edgeimpulse.com/apis/studio/organizationdata/add-a-storage-bucket.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a storage bucket

> Add a storage bucket.



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/buckets
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
  /api/organizations/{organizationId}/buckets:
    post:
      tags:
        - OrganizationData
      summary: Add a storage bucket
      description: Add a storage bucket.
      operationId: addOrganizationBucket
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AddOrganizationBucketRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EntityCreatedResponse'
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
    AddOrganizationBucketRequest:
      type: object
      required:
        - accessKey
        - secretKey
        - endpoint
        - bucket
        - region
      properties:
        accessKey:
          type: string
          description: >-
            Access key for the storage service (e.g., S3 access key, GCS access
            key)
        secretKey:
          type: string
          description: >-
            Secret key for the storage service (e.g., S3 secret key, GCS secret
            key)
        endpoint:
          type: string
          description: >
            Endpoint URL for the storage service (e.g., S3 endpoint, custom
            endpoint for other services)
        bucket:
          type: string
          description: Name of the storage bucket
        region:
          type: string
          description: Region of the storage service (if applicable)
        checkConnectivityPrefix:
          type: string
          description: |
            Set this if you don't have access to the root of this bucket.
            Only used to verify connectivity to this bucket.
        storageProvider:
          $ref: '#/components/schemas/StorageProvider'
          description: The type of storage provider. Defaults to 's3' if not specified.
    EntityCreatedResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - id
          properties:
            id:
              type: integer
              description: Unique identifier of the created entity.
    StorageProvider:
      type: string
      enum:
        - s3
        - google
        - azure
        - other
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