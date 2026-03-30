# Source: https://docs.edgeimpulse.com/apis/studio/raw-data/rebalance-dataset-1.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rebalance dataset

> Rebalances the dataset over training / testing categories. This resets the category for all data and splits it 80%/20% between training and testing. This is a deterministic process based on the hash of the name of the data. Returns immediately on small datasets, or starts a job on larger datasets. To get the dataset ratio (as returned by the v1 endpoint), use getDatasetRatio.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/v2/rebalance
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
  /api/{projectId}/v2/rebalance:
    post:
      tags:
        - Raw data
      summary: Rebalance dataset
      description: >-
        Rebalances the dataset over training / testing categories. This resets
        the category for all data and splits it 80%/20% between training and
        testing. This is a deterministic process based on the hash of the name
        of the data. Returns immediately on small datasets, or starts a job on
        larger datasets. To get the dataset ratio (as returned by the v1
        endpoint), use getDatasetRatio.
      operationId: rebalanceDatasetV2
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                anyOf:
                  - $ref: '#/components/schemas/GenericApiResponse'
                  - $ref: '#/components/schemas/StartJobResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
  schemas:
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