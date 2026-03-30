# Source: https://docs.edgeimpulse.com/apis/studio/organizations/white-label-admin--create-a-new-organization-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# White Label Admin - Create a new organization project

> White label admin only API to create a new project for an organization.



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/whitelabel/organizations/{innerOrganizationId}/projects
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
  /api/organizations/{organizationId}/whitelabel/organizations/{innerOrganizationId}/projects:
    post:
      tags:
        - Organizations
      summary: White Label Admin - Create a new organization project
      description: White label admin only API to create a new project for an organization.
      operationId: whitelabelAdminCreateOrganizationProject
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/InnerOrganizationIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AdminCreateProjectRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateProjectResponse'
components:
  parameters:
    OrganizationIdParameter:
      name: organizationId
      in: path
      required: true
      description: Organization ID
      schema:
        type: integer
    InnerOrganizationIdParameter:
      name: innerOrganizationId
      in: path
      required: true
      description: Organization ID within the context of a white label
      schema:
        type: integer
  schemas:
    AdminCreateProjectRequest:
      type: object
      required:
        - projectName
      properties:
        projectName:
          type: string
          example: My project
          description: The name of the project.
        projectVisibility:
          $ref: '#/components/schemas/ProjectVisibility'
        ownerId:
          type: integer
          example: 1
          description: >-
            Unique identifier of the owner of the new project. Either this
            parameter or ownerEmail must be set.
        ownerEmail:
          type: string
          example: groucho@marxbros.com
          description: >-
            Email of the owner of the new project. Either this parameter or
            ownerId must be set.
    CreateProjectResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - id
            - apiKey
          properties:
            id:
              type: integer
              description: Project ID for the new project
            apiKey:
              type: string
              description: API key for the new project
    ProjectVisibility:
      type: string
      enum:
        - public
        - private
      description: >-
        The visibility of the project, either public or private. Public projects
        can be viewed by anyone on the internet and edited by collaborators.
        Private projects can only be viewed and edited by collaborators.
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