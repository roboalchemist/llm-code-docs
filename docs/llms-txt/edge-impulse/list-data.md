# Source: https://docs.edgeimpulse.com/apis/studio/organizationdata/list-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List data

> Lists all data items. This can be filtered by the ?filter parameter.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/data
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
  /api/organizations/{organizationId}/data:
    get:
      tags:
        - OrganizationData
      summary: List data
      description: Lists all data items. This can be filtered by the ?filter parameter.
      operationId: listOrganizationData
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/OrganizationDatasetParameter'
        - $ref: '#/components/parameters/OrganizationDataFilterParameter'
        - $ref: '#/components/parameters/LimitResultsParameter'
        - $ref: '#/components/parameters/OffsetResultsParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListOrganizationDataResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
    OrganizationDatasetParameter:
      name: dataset
      in: query
      required: false
      description: Selected dataset
      example: activity data
      schema:
        type: string
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
    LimitResultsParameter:
      name: limit
      in: query
      required: false
      description: Maximum number of results
      schema:
        type: integer
    OffsetResultsParameter:
      name: offset
      in: query
      required: false
      description: >-
        Offset in results, can be used in conjunction with LimitResultsParameter
        to implement paging.
      schema:
        type: integer
  schemas:
    ListOrganizationDataResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          properties:
            filterParseError:
              type: string
            data:
              type: array
              items:
                type: object
                required:
                  - id
                  - name
                  - bucketId
                  - bucketName
                  - bucketPath
                  - fullBucketPath
                  - dataset
                  - totalFileCount
                  - totalFileSize
                  - created
                  - metadata
                  - metadataStringForCLI
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
                  fullBucketPath:
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
                  metadataStringForCLI:
                    type: string
                    description: >-
                      String that's passed in to a transformation block in
                      `--metadata` (the metadata + a `dataItemInfo` object)
            totalFileCount:
              type: integer
            totalDataItemCount:
              type: integer
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