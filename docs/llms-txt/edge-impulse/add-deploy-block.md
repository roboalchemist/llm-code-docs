# Source: https://docs.edgeimpulse.com/apis/studio/organizationblocks/add-deploy-block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add deploy block

> Adds a deploy block.



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/deploy
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
  /api/organizations/{organizationId}/deploy:
    post:
      tags:
        - OrganizationBlocks
      summary: Add deploy block
      description: Adds a deploy block.
      operationId: addOrganizationDeployBlock
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/AddOrganizationDeployBlockRequest'
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
    AddOrganizationDeployBlockRequest:
      type: object
      required:
        - name
        - dockerContainer
        - description
        - cliArguments
      properties:
        name:
          type: string
        dockerContainer:
          type: string
        description:
          type: string
        cliArguments:
          type: string
        requestsCpu:
          type: number
        requestsMemory:
          type: integer
        limitsCpu:
          type: number
        limitsMemory:
          type: integer
        photo:
          type: string
          format: binary
        integrateUrl:
          type: string
        privileged:
          type: boolean
        mountLearnBlock:
          type: boolean
        supportsEonCompiler:
          type: boolean
        showOptimizations:
          type: boolean
        category:
          type: string
          enum:
            - library
            - firmware
        sourceCodeDownloadStaffOnly:
          type: boolean
          description: Whether the source code is only available for staff users.
        parameters:
          description: >-
            List of parameters, spec'ed according to
            https://docs.edgeimpulse.com/docs/tips-and-tricks/adding-parameters-to-custom-blocks
          type: array
          items:
            type: object
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