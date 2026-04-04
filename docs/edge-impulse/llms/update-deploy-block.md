# Source: https://docs.edgeimpulse.com/apis/studio/organizationblocks/update-deploy-block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update deploy block

> Updates a deploy block. Only values in the body will be updated.



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/deploy/{deployId}
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
  /api/organizations/{organizationId}/deploy/{deployId}:
    post:
      tags:
        - OrganizationBlocks
      summary: Update deploy block
      description: Updates a deploy block. Only values in the body will be updated.
      operationId: updateOrganizationDeployBlock
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/DeployIdParameter'
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/UpdateOrganizationDeployBlockRequest'
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
    DeployIdParameter:
      name: deployId
      in: path
      required: true
      description: Deploy block ID.
      schema:
        type: integer
  schemas:
    UpdateOrganizationDeployBlockRequest:
      type: object
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