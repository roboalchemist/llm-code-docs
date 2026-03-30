# Source: https://docs.edgeimpulse.com/apis/studio/organizationblocks/update-transformation-block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update transformation block

> Updates a transformation block. Only values in the body will be updated.



## OpenAPI

````yaml .assets/openapi.yaml post /api/organizations/{organizationId}/transformation/{transformationId}
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
  /api/organizations/{organizationId}/transformation/{transformationId}:
    post:
      tags:
        - OrganizationBlocks
      summary: Update transformation block
      description: Updates a transformation block. Only values in the body will be updated.
      operationId: updateOrganizationTransformationBlock
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
        - $ref: '#/components/parameters/TransformationIdParameter'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/UpdateOrganizationTransformationBlockRequest
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
    TransformationIdParameter:
      name: transformationId
      in: path
      required: true
      description: Transformation block ID.
      schema:
        type: integer
  schemas:
    UpdateOrganizationTransformationBlockRequest:
      type: object
      properties:
        name:
          type: string
        dockerContainer:
          type: string
        indMetadata:
          description: Whether to pass the `--metadata` parameter to the container.
          type: boolean
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
        additionalMountPoints:
          type: array
          items:
            $ref: '#/components/schemas/TransformationBlockAdditionalMountPoint'
        operatesOn:
          $ref: '#/components/schemas/TransformationJobOperatesOnEnum'
        allowExtraCliArguments:
          type: boolean
        parameters:
          description: >-
            List of parameters, spec'ed according to
            https://docs.edgeimpulse.com/docs/tips-and-tricks/adding-parameters-to-custom-blocks
          type: array
          items:
            type: object
        maxRunningTimeStr:
          type: string
          description: >-
            15m for 15 minutes, 2h for 2 hours, 1d for 1 day. If not set, the
            default is 8 hours.
        isPublic:
          type: boolean
        publicProjectTierAvailability:
          $ref: '#/components/schemas/PublicProjectTierAvailability'
        repositoryUrl:
          type: string
          description: URL to the source code of this custom learn block.
        showInDataSources:
          type: boolean
          description: >-
            Whether to show this block in 'Data sources'. Only applies for
            standalone blocks.
        showInCreateTransformationJob:
          type: boolean
          description: >-
            Whether to show this block in 'Create transformation job'. Only
            applies for standalone blocks.
        showInSyntheticData:
          type: boolean
          description: >-
            Whether to show this block in 'Synthetic data'. Only applies for
            standalone blocks.
        showInAIActions:
          type: boolean
          description: >-
            Whether to show this block in 'AI Labeling'. Only applies for
            standalone blocks.
        environmentVariables:
          type: array
          items:
            $ref: '#/components/schemas/EnvironmentVariable'
        aiActionsOperatesOn:
          type: array
          description: >-
            For AI labeling blocks, this lists the data types that the block
            supports. If this field is empty then there's no information about
            supported data types.
          items:
            $ref: '#/components/schemas/AIActionsOperatesOn'
        sourceCodeDownloadStaffOnly:
          type: boolean
          description: Whether the source code is only available for staff users.
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
    TransformationBlockAdditionalMountPoint:
      type: object
      required:
        - type
        - mountPoint
      properties:
        type:
          type: string
          enum:
            - bucket
            - portal
        bucketId:
          type: integer
        portalId:
          type: integer
        mountPoint:
          type: string
    TransformationJobOperatesOnEnum:
      type: string
      enum:
        - file
        - directory
        - standalone
    PublicProjectTierAvailability:
      description: >-
        For public blocks, this indicates the project tiers for which this block
        is available.
      type: string
      enum:
        - enterprise-only
        - all-projects
        - all-projects-including-whitelabels
    EnvironmentVariable:
      type: object
      required:
        - key
      properties:
        key:
          type: string
          description: >-
            Environmental variable key. Needs to adhere to regex
            "^[a-zA-Z_]+[a-zA-Z0-9_]*$".
        value:
          description: >-
            If value is left undefined, only the key is passed in as an
            environmental variable.
          type: string
    AIActionsOperatesOn:
      type: string
      enum:
        - images_object_detection
        - images_single_label
        - audio
        - other
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