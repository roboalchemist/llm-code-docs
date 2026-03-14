# Source: https://docs.edgeimpulse.com/apis/studio/organizationdata/get-data-metadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get data metadata

> Get a data item. This will HEAD the underlying bucket to retrieve the last file information.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/data/{dataId}
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
  /api/organizations/{organizationId}/data/{dataId}:
    get:
      tags:
        - OrganizationData
      summary: Get data metadata
      description: >-
        Get a data item. This will HEAD the underlying bucket to retrieve the
        last file information.
      operationId: getOrganizationDataItem
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/OrganizationDataIdParameter'
        - $ref: '#/components/parameters/OrganizationDataFilterParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetOrganizationDataItemResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
    OrganizationDataIdParameter:
      name: dataId
      in: path
      required: true
      description: Data ID
      schema:
        type: integer
    OrganizationDataFilterParameter:
      name: filter
      in: query
      required: false
      description: >-
        Data filter in SQL WHERE format, where you can reference 'dataset',
        'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and
        any metadata label through 'metadata->' (dots are replaced by
        underscore).
      example: >-
        dataset = 'activity data' AND (label = 'running' OR metadata->user =
        'Jan Jongboom')
      schema:
        type: string
  schemas:
    GetOrganizationDataItemResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - data
          properties:
            data:
              $ref: '#/components/schemas/OrganizationDataItem'
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
    OrganizationDataItem:
      type: object
      required:
        - id
        - name
        - bucketId
        - bucketName
        - bucketPath
        - dataset
        - totalFileCount
        - totalFileSize
        - created
        - metadata
        - files
      properties:
        id:
          type: integer
        name:
          type: string
        bucketId:
          type: integer
        bucketName:
          type: string
        bucketPath:
          type: string
        dataset:
          type: string
        totalFileCount:
          type: integer
        totalFileSize:
          type: integer
        created:
          type: string
          format: date-time
        metadata:
          type: object
          additionalProperties:
            type: string
        files:
          type: array
          items:
            type: object
            required:
              - name
              - bucketPath
              - size
            properties:
              name:
                type: string
              bucketPath:
                type: string
              size:
                type: integer
              lastModified:
                type: string
                format: date-time
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