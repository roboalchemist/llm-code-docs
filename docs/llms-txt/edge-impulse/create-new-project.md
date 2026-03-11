# Source: https://docs.edgeimpulse.com/apis/studio/projects/create-new-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create new project

> Create a new project. This API can only be called using a JWT token.



## OpenAPI

````yaml .assets/openapi.yaml post /api/projects/create
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
  /api/projects/create:
    post:
      tags:
        - Projects
      summary: Create new project
      description: Create a new project. This API can only be called using a JWT token.
      operationId: createProject
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateProjectRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateProjectResponse'
components:
  schemas:
    CreateProjectRequest:
      type: object
      required:
        - projectName
      properties:
        projectName:
          type: string
          example: EEG trials
          description: The name of the first project.
        projectVisibility:
          $ref: '#/components/schemas/ProjectVisibility'
        originalProjectVersionId:
          type: integer
          description: The ID of the version that was used to restore this project.
        showGettingStartedWizard:
          type: boolean
          description: >-
            Whether to show the getting started wizard use-case chooser screen
            after the project is created
        tutorialKey:
          $ref: '#/components/schemas/TutorialType'
          description: Optional in-product tutorial to launch after the project is created
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
    TutorialType:
      type: string
      description: >-
        The type of in-product guided tutorial to show in the getting started
        wizard
      enum:
        - kws
        - cv
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