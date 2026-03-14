# Source: https://docs.edgeimpulse.com/apis/studio/organizationdata/delete-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete data

> Delete all data for selected data items. This removes all data in the underlying data bucket.



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/data/delete
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
  /api/organizations/{organizationId}/data/delete:
    post:
      tags:
        - OrganizationData
      summary: Delete data
      description: >-
        Delete all data for selected data items. This removes all data in the
        underlying data bucket.
      operationId: deleteOrganizationDataItems
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/OrganizationDatasetParameter'
        - $ref: '#/components/parameters/OrganizationDataIdsParameter'
        - $ref: '#/components/parameters/OrganizationDataFilterParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StartJobResponse'
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
    OrganizationDataIdsParameter:
      name: dataIds
      in: query
      required: true
      description: Data IDs as an Array
      example:
        - 3
        - 7
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
  schemas:
    StartJobResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - id
          properties:
            id:
              type: integer
              description: Job identifier. Status updates will include this identifier.
              example: 12873488112
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