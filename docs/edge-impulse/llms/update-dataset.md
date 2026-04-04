# Source: https://docs.edgeimpulse.com/apis/studio/organizationdata/update-dataset.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update dataset

> Set information about a dataset



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/dataset/{dataset}
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
  /api/organizations/{organizationId}/dataset/{dataset}:
    post:
      tags:
        - OrganizationData
      summary: Update dataset
      description: Set information about a dataset
      operationId: updateOrganizationDataset
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/OrganizationDatasetPathParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateOrganizationDatasetRequest'
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
    OrganizationDatasetPathParameter:
      name: dataset
      in: path
      required: true
      description: Dataset name
      schema:
        type: string
  schemas:
    UpdateOrganizationDatasetRequest:
      type: object
      properties:
        dataset:
          type: string
        tags:
          type: array
          items:
            type: string
        category:
          type: string
        type:
          $ref: '#/components/schemas/OrganizationDatasetTypeEnum'
        bucket:
          type: object
          required:
            - id
            - path
            - dataItemNamingLevelsDeep
          properties:
            id:
              description: Bucket ID
              type: integer
            path:
              description: Path in the bucket
              type: string
            dataItemNamingLevelsDeep:
              description: >-
                Number of levels deep for data items, e.g. if you have folder
                "test/abc", with value 1 "test" will be a data item, with value
                2 "test/abc" will be a data item. Only used for "clinical"
                datasets.
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
    OrganizationDatasetTypeEnum:
      type: string
      enum:
        - clinical
        - files
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