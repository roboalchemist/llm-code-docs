# Source: https://docs.edgeimpulse.com/apis/studio/raw-data/rebalance-dataset.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rebalance dataset

> This API is deprecated, use rebalanceDatasetV2 instead (`/v1/api/{projectId}/v2/rebalance`). Rebalances the dataset over training / testing categories. This resets the category for all data and splits it 80%/20% between training and testing. This is a deterministic process based on the hash of the name of the data.



## OpenAPI

````yaml .assets/openapi.yaml post /api/{projectId}/rebalance
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
  /api/{projectId}/rebalance:
    post:
      tags:
        - Raw data
      summary: Rebalance dataset
      description: >-
        This API is deprecated, use rebalanceDatasetV2 instead
        (`/v1/api/{projectId}/v2/rebalance`). Rebalances the dataset over
        training / testing categories. This resets the category for all data and
        splits it 80%/20% between training and testing. This is a deterministic
        process based on the hash of the name of the data.
      operationId: rebalanceDataset
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RebalanceDatasetResponse'
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
    RebalanceDatasetResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - $ref: '#/components/schemas/DatasetRatioData'
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
    DatasetRatioData:
      type: object
      required:
        - ratio
      properties:
        ratio:
          type: object
          properties:
            training:
              type: integer
              description: number of training samples after rebalance
            testing:
              type: integer
              description: >-
                number of testing samples after rebalance. This ignores test
                data with a label that's not in the training dataset.
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