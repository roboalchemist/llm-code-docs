# Source: https://docs.edgeimpulse.com/apis/studio/optimization/get-all-available-learn-blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all available learn blocks

> Get all available learn blocks



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/optimize/all-learn-blocks
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
  /api/{projectId}/optimize/all-learn-blocks:
    get:
      tags:
        - Optimization
      summary: Get all available learn blocks
      description: Get all available learn blocks
      operationId: getAllLearnBlocks
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AllLearnBlocksResponse'
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
    AllLearnBlocksResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - learnBlocks
          properties:
            learnBlocks:
              type: array
              items:
                type: object
                required:
                  - type
                  - title
                  - author
                  - description
                  - name
                properties:
                  type:
                    $ref: '#/components/schemas/LearnBlockType'
                  title:
                    type: string
                  author:
                    type: string
                  description:
                    type: string
                  name:
                    type: string
                  organizationModelId:
                    type: number
                  experiment:
                    type: string
                  displayCategory:
                    $ref: '#/components/schemas/BlockDisplayCategory'
                  publicProjectTierAvailability:
                    $ref: '#/components/schemas/PublicProjectTierAvailability'
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
    LearnBlockType:
      type: string
      description: >-
        The type of learning block (anomaly, keras, keras-transfer-image,
        keras-transfer-kws, keras-object-detection, keras-regression,
        keras-freeform). Each behaves differently.
      enum:
        - anomaly
        - anomaly-gmm
        - keras
        - keras-transfer-image
        - keras-transfer-kws
        - keras-object-detection
        - keras-regression
        - keras-akida
        - keras-akida-transfer-image
        - keras-akida-object-detection
        - keras-visual-anomaly
        - keras-freeform
        - keras-anomaly
        - vlm
    BlockDisplayCategory:
      description: Category to display this block in the UI.
      type: string
      enum:
        - classical
        - tao
        - developer-preview
    PublicProjectTierAvailability:
      description: >-
        For public blocks, this indicates the project tiers for which this block
        is available.
      type: string
      enum:
        - enterprise-only
        - all-projects
        - all-projects-including-whitelabels
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