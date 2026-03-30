# Source: https://docs.edgeimpulse.com/apis/studio/organizationdata/update-storage-bucket.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update storage bucket

> Updates storage bucket details. This only updates fields that were set in the request body.
Before updating the bucket details, it is required to verify the connection using the
POST /api/organizations/{organizationId}/buckets/verify endpoint.

The verification process:
1. Call the verify endpoint with the new bucket details.
2. Poll the verify endpoint until it responds with `connectionStatus: connected`.
3. If the endpoint responds with `connectionStatus: error`, the verification has failed.

Only proceed with updating the bucket details after receiving a `connected` status.
The polling interval and timeout should be determined based on your application's requirements.




## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/buckets/{bucketId}
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
  /api/organizations/{organizationId}/buckets/{bucketId}:
    post:
      tags:
        - OrganizationData
      summary: Update storage bucket
      description: >
        Updates storage bucket details. This only updates fields that were set
        in the request body.

        Before updating the bucket details, it is required to verify the
        connection using the

        POST /api/organizations/{organizationId}/buckets/verify endpoint.


        The verification process:

        1. Call the verify endpoint with the new bucket details.

        2. Poll the verify endpoint until it responds with `connectionStatus:
        connected`.

        3. If the endpoint responds with `connectionStatus: error`, the
        verification has failed.


        Only proceed with updating the bucket details after receiving a
        `connected` status.

        The polling interval and timeout should be determined based on your
        application's requirements.
      operationId: updateOrganizationBucket
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/BucketIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateOrganizationBucketRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenericApiResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
    BucketIdParameter:
      name: bucketId
      in: path
      required: true
      description: Bucket ID
      schema:
        type: integer
  schemas:
    UpdateOrganizationBucketRequest:
      type: object
      properties:
        accessKey:
          type: string
          description: S3 access key
        secretKey:
          type: string
          description: S3 secret key
        endpoint:
          type: string
          description: S3 endpoint
        bucket:
          type: string
          description: S3 bucket
        region:
          type: string
          description: S3 region
        checkConnectivityPrefix:
          type: string
          description: |
            Set this if you don't have access to the root of this bucket.
            Only used to verify connectivity to this bucket.
        storageAccountName:
          type: string
          description: The name of the storage account for Azure Blob Storage
          example: my-storage-account
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