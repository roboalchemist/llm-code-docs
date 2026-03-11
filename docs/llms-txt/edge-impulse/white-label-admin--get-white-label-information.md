# Source: https://docs.edgeimpulse.com/apis/studio/organizations/white-label-admin--get-white-label-information.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# White Label Admin - Get white label information

> White label admin only API to get the white label information.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/whitelabel
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
  /api/organizations/{organizationId}/whitelabel:
    get:
      tags:
        - Organizations
      summary: White Label Admin - Get white label information
      description: White label admin only API to get the white label information.
      operationId: whitelabelAdminGetInfo
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetWhitelabelResponse'
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
    GetWhitelabelResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          properties:
            whitelabel:
              $ref: '#/components/schemas/Whitelabel'
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
    Whitelabel:
      type: object
      required:
        - id
        - name
        - domain
        - themeId
        - identityProviders
        - allowPasswordAuth
        - deploymentTargets
        - allDeploymentTargets
        - allowSignup
        - allowFreeProjects
        - supportedProjectTypes
        - allowNewProjectUi
        - learningBlocks
        - allLearningBlocks
        - developmentBoards
        - allDevelopmentBoards
      properties:
        id:
          type: integer
        name:
          type: string
        domain:
          type: string
        ownerOrganizationId:
          type: integer
        themeId:
          type: integer
        theme:
          $ref: '#/components/schemas/Theme'
        identityProviders:
          type: array
          items:
            type: string
        allowPasswordAuth:
          type: boolean
        deploymentTargets:
          description: List of deployment targets enabled for this white label
          type: array
          items:
            type: string
        allDeploymentTargets:
          description: List of all supported deployment targets
          type: array
          items:
            type: string
        customDeploymentBlocks:
          description: List of custom deployment blocks available to this white label
          type: array
          items:
            type: object
            required:
              - name
              - id
            properties:
              name:
                type: string
                description: The name of the custom deployment block
              id:
                type: number
                description: The custom deployment block ID
        deploymentOptionsOrder:
          $ref: '#/components/schemas/DeploymentOptionsOrder'
        allowSignup:
          type: boolean
        allowFreeProjects:
          type: boolean
        exposePublicProjects:
          type: boolean
        defaultDeploymentTarget:
          type: string
          description: The name of the default deployment target for this white label
          nullable: true
          example: C++ Library
        supportedProjectTypes:
          type: array
          items:
            $ref: '#/components/schemas/ProjectType'
        allowNewProjectUi:
          type: boolean
          description: >-
            Whether the new project UI should be enabled for this white label or
            not.
        learningBlocks:
          description: List of learning blocks enabled for this white label
          type: array
          items:
            type: string
        allLearningBlocks:
          description: List of all supported learning blocks
          type: array
          items:
            type: object
            required:
              - title
              - type
            properties:
              title:
                type: string
                description: The name of the learning block
              type:
                type: string
                description: The learning block type
        developmentBoards:
          type: array
          items:
            $ref: '#/components/schemas/DevelopmentBoardResponse'
        allDevelopmentBoards:
          type: array
          items:
            $ref: '#/components/schemas/DevelopmentBoardResponse'
        organizationsLimit:
          type: integer
          description: >-
            The maximum number of organizations that can be created under this
            white label.
        disablePublicEntities:
          type: boolean
          description: >-
            Whether public entities (like projects, user profiles, etc.) are
            disabled for this whitelabel instance.
        disableMarketingFeatures:
          type: boolean
          description: >-
            Whether marketing features (marketing cookies, HubSpot tracking,
            etc.) are disabled for this whitelabel instance.
        disableForumAccess:
          type: boolean
          description: Whether forum access is disabled for this whitelabel instance.
        customLimits:
          type: object
          description: Custom limits for this whitelabel instance.
    Theme:
      type: object
      required:
        - id
        - name
        - favicon
        - logos
        - colors
      properties:
        id:
          type: integer
        ownerUserId:
          type: integer
        ownerOrganizationId:
          type: integer
        name:
          type: string
        favicon:
          type: object
          properties:
            favicon32:
              type: string
            favicon57:
              type: string
            favicon76:
              type: string
            favicon96:
              type: string
            favicon120:
              type: string
            favicon128:
              type: string
            favicon144:
              type: string
            favicon152:
              type: string
            favicon180:
              type: string
            favicon228:
              type: string
        logos:
          type: object
          properties:
            primary:
              type: string
            primaryPng:
              type: string
            primaryWhite:
              type: string
            loginLogo:
              type: string
            loginLogoWhite:
              type: string
            mark:
              type: string
            markWhite:
              type: string
            deviceLogo:
              type: string
        colors:
          type: object
          properties:
            primaryColor:
              type: string
            primaryColorRgb:
              type: array
              items:
                type: number
            primaryColorGradientEnd:
              type: string
    DeploymentOptionsOrder:
      type: array
      description: >-
        Optional attribute allowing a whitelabel to customize the order of
        deployment options in the deployment view, given as an in-order list of
        deployment options.
      items:
        type: string
        description: Deployment option name
        example: org-1
    ProjectType:
      type: string
      enum:
        - kws
        - audio
        - object-detection
        - image
        - accelerometer
        - other
    DevelopmentBoardResponse:
      type: object
      required:
        - id
        - name
        - image
        - docsUrl
      properties:
        id:
          type: integer
        name:
          type: string
        image:
          type: string
        docsUrl:
          type: string
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