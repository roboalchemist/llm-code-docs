# Source: https://docs.edgeimpulse.com/apis/studio/organizationdata/list-storage-buckets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List storage buckets

> Retrieve all configured storage buckets. This does not list the secret key.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/buckets
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
    get:
      tags:
        - OrganizationData
      summary: List storage buckets
      description: >-
        Retrieve all configured storage buckets. This does not list the secret
        key.
      operationId: listOrganizationBuckets
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListOrganizationBucketsResponse'
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
    ListOrganizationBucketsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - buckets
          properties:
            buckets:
              type: array
              items:
                $ref: '#/components/schemas/OrganizationBucket'
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
    OrganizationBucket:
      type: object
      required:
        - id
        - accessKey
        - endpoint
        - bucket
        - region
        - connected
        - storageProvider
      properties:
        id:
          type: integer
          example: 1
        accessKey:
          type: string
          description: Access key for the storage service
          example: AKIAIOSFODNN7EXAMPLE
        endpoint:
          type: string
          description: Endpoint URL for the storage service
          example: https://s3.amazonaws.com
        bucket:
          type: string
          description: Name of the storage bucket
          example: my-organization-bucket
        region:
          type: string
          description: Region of the storage service (if applicable)
          example: us-west-2
        connected:
          type: boolean
          description: Whether we can reach the bucket
          example: true
        checkConnectivityPrefix:
          type: string
          description: >
            Optional prefix used for connectivity verification when root bucket
            access is restricted.
          example: data/
        storageProvider:
          $ref: '#/components/schemas/StorageProvider'
          description: The type of storage provider for this bucket
          example: s3
        storageAccountName:
          type: string
          description: The name of the storage account for Azure Blob Storage
          example: my-storage-account
    StorageProvider:
      type: string
      enum:
        - s3
        - google
        - azure
        - other
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