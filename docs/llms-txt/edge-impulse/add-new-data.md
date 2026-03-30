# Source: https://docs.edgeimpulse.com/apis/studio/organizationdata/add-new-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add new data

> Add a new data item. You can add a maximum of 10000 files directly through this API. Use `addOrganizationDataFile` to add additional files.



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/data/add
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
  /api/organizations/{organizationId}/data/add:
    post:
      tags:
        - OrganizationData
      summary: Add new data
      description: >-
        Add a new data item. You can add a maximum of 10000 files directly
        through this API. Use `addOrganizationDataFile` to add additional files.
      operationId: addOrganizationDataItem
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/OrganizationAddDataItemRequest'
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
    OrganizationAddDataItemRequest:
      type: object
      required:
        - name
        - dataset
        - metadata
        - files[]
      properties:
        name:
          type: string
        bucketId:
          type: integer
        bucketName:
          type: string
          description: Name of the bucket name (as an Edge Impulse name)
        dataset:
          type: string
        bucketPath:
          type: string
          description: >-
            Optional path in the bucket to create this data item (files are
            created under this path).
        metadata:
          type: string
          description: Key-value pair of metadata (in JSON format)
        files[]:
          type: array
          items:
            type: string
            format: binary
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