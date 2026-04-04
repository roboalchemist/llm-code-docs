# Source: https://docs.edgeimpulse.com/apis/studio/organizationdata/verify-bucket-connectivity.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Verify bucket connectivity

> Verify connectivity to a storage bucket and optionally list its contents. This endpoint allows you to:
1. Check if the provided bucket credentials are valid and the bucket is accessible.
2. Optionally list files in the bucket up to a specified limit.
3. Validate the bucket configuration before adding it to the organization.

The request can include details such as the bucket name, region, credentials, and listing options.
The response provides information about the bucket's accessibility and, if requested, a list of files in the bucket.

Important note on verification process:
- For S3-compatible storage backends: Verification is expected to be immediate.
- For Azure buckets: Verification takes longer. Users are required to poll this endpoint
until the connectionStatus changes from 'connecting' to 'connected'.

When dealing with Azure buckets, implement a polling mechanism to check the status
periodically until it's confirmed as connected.




## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/buckets/verify
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
  /api/organizations/{organizationId}/buckets/verify:
    post:
      tags:
        - OrganizationData
      summary: Verify bucket connectivity
      description: >
        Verify connectivity to a storage bucket and optionally list its
        contents. This endpoint allows you to:

        1. Check if the provided bucket credentials are valid and the bucket is
        accessible.

        2. Optionally list files in the bucket up to a specified limit.

        3. Validate the bucket configuration before adding it to the
        organization.


        The request can include details such as the bucket name, region,
        credentials, and listing options.

        The response provides information about the bucket's accessibility and,
        if requested, a list of files in the bucket.


        Important note on verification process:

        - For S3-compatible storage backends: Verification is expected to be
        immediate.

        - For Azure buckets: Verification takes longer. Users are required to
        poll this endpoint

        until the connectionStatus changes from 'connecting' to 'connected'.


        When dealing with Azure buckets, implement a polling mechanism to check
        the status

        periodically until it's confirmed as connected.
      operationId: verifyOrganizationBucket
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/VerifyOrganizationBucketRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VerifyOrganizationBucketResponse'
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
    VerifyOrganizationBucketRequest:
      type: object
      required:
        - accessKey
        - endpoint
        - bucket
      properties:
        storageProvider:
          $ref: '#/components/schemas/StorageProvider'
          description: |
            The type of storage backend to use. Supported options are:
            - 's3': Amazon S3
            - 'google': Google Cloud Storage
            - 'azure': Azure Blob Storage
            - 'other': Other S3-compatible storage
            If not specified, defaults to 's3'
        accessKey:
          type: string
          description: |
            Access key for the storage service:
            - For S3 and GCS: Use the access key.
            - For Azure: Use the Storage Account Name.
        secretKey:
          type: string
          description: >
            Secret key for the storage service:

            - For S3 and GCS: Use the secret key.

            - For Azure: Use the Storage Account Access Key.

            Note: You should either pass a `secretKey` value or a `bucketId`
            value.
        bucketId:
          type: integer
          description: >
            ID of an existing bucket. If provided, the credentials from this
            bucket

            will be used unless overridden by the `secretKey` property.
        bucket:
          type: string
          description: Name of the storage bucket or container.
        endpoint:
          type: string
          description: |
            Endpoint URL for the storage service.
            For S3-compatible services, Azure, or custom endpoints.
        region:
          type: string
          description: Optional region of the storage service (if applicable).
        prefix:
          type: string
          description: >
            Optional prefix within the bucket.

            Set this if you don't have access to the full bucket or want to
            limit the scope.
    VerifyOrganizationBucketResponse:
      description: >
        Response object for verifying an organization's bucket connectivity.


        Workflow:

        1. The client initiates verification by sending a GET request to
        /api/organizations/{organizationId}/buckets/verify with bucket and
        credential details.

        2. The server responds with this VerifyOrganizationBucketResponse
        object.

        3. The client checks the connectionStatus:
           - If "connected": Verification is complete. Other properties (files, hasInfoLabelsFile, signedUrl) are available.
           - If "connecting": Verification is in progress. The client should continue polling. Other properties are not yet available.
           - If "error": Verification failed. Check connectionError for details. Other properties are not available.
        4. If connectionStatus is "connecting", the client should periodically
        poll the endpoint until the status changes to "connected" or "error".
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - connectionStatus
          properties:
            connectionStatus:
              type: string
              description: >
                Indicates the current state of the connectivity verification
                process.

                - "connected": Verification successful, other properties are
                available.

                - "connecting": Verification in progress, continue polling.

                - "error": Verification failed, check connectionError for
                details.
              enum:
                - connected
                - connecting
                - error
            connectionError:
              type: string
              nullable: true
              description: >
                Provides additional details if connectionStatus is "error".
                Helps diagnose verification failures.
            connectionStatusSince:
              type: string
              format: date-time
              nullable: true
              description: |
                Timestamp of when the connectionStatus last changed.
            files:
              type: array
              description: >-
                Random files from the bucket. Only available when
                connectionStatus is "connected".
              items:
                type: object
                required:
                  - name
                  - size
                  - folderName
                properties:
                  name:
                    type: string
                    description: The name of the file.
                  size:
                    type: integer
                    description: The size of the file in bytes.
                  folderName:
                    type: string
                    description: The name of the folder containing the file.
            hasInfoLabelsFile:
              type: boolean
              description: >
                Indicates whether there are any info.labels files in this
                bucket.

                If so, those are used for category/labels.

                Only available when connectionStatus is "connected".
            signedUrl:
              type: string
              description: >
                A signed URL that allows you to PUT an item, to check whether
                CORS headers are set up correctly for this bucket.

                Only available when connectionStatus is "connected".
            endpoint:
              type: string
              description: >
                An alternative endpoint URL. Only returned and required for
                Azure storage accounts,

                where the endpoint must be reformatted. This field will be
                undefined for other storage providers.
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