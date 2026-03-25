# Source: https://docs.edgeimpulse.com/apis/studio/organizationblocks/list-public-transformation-blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List public transformation blocks

> Retrieve all transformation blocks published by other organizations, available for all organizations.



## OpenAPI

````yaml .assets/openapi.yaml get /api/organizations/{organizationId}/transformation/public
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
  /api/organizations/{organizationId}/transformation/public:
    get:
      tags:
        - OrganizationBlocks
      summary: List public transformation blocks
      description: >-
        Retrieve all transformation blocks published by other organizations,
        available for all organizations.
      operationId: listPublicOrganizationTransformationBlocks
      parameters:
        - $ref: '#/components/parameters/OrganizationIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/ListPublicOrganizationTransformationBlocksResponse
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
    ListPublicOrganizationTransformationBlocksResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - transformationBlocks
          properties:
            transformationBlocks:
              type: array
              items:
                $ref: '#/components/schemas/PublicOrganizationTransformationBlock'
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
    PublicOrganizationTransformationBlock:
      type: object
      required:
        - id
        - ownerOrganizationId
        - ownerOrganizationName
        - name
        - created
        - description
        - operatesOn
        - allowExtraCliArguments
        - showInDataSources
        - showInCreateTransformationJob
        - showInSyntheticData
        - showInAIActions
      properties:
        id:
          type: integer
        ownerOrganizationId:
          type: integer
        ownerOrganizationName:
          type: string
        name:
          type: string
        created:
          type: string
          format: date-time
        lastUpdated:
          type: string
          format: date-time
        description:
          type: string
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
        parametersUI:
          description: List of parameters to be rendered in the UI
          type: array
          items:
            $ref: '#/components/schemas/DSPGroupItem'
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
        aiActionsOperatesOn:
          type: array
          description: >-
            For AI labeling blocks, this lists the data types that the block
            supports. If this field is empty then there's no information about
            supported data types.
          items:
            $ref: '#/components/schemas/AIActionsOperatesOn'
    TransformationJobOperatesOnEnum:
      type: string
      enum:
        - file
        - directory
        - standalone
    DSPGroupItem:
      type: object
      required:
        - name
        - type
        - param
        - defaultValue
        - readonly
        - shouldShow
        - required
        - showClickToSet
      properties:
        name:
          type: string
          example: Scale axes
        value:
          type: string
        defaultValue:
          type: string
        type:
          type: string
          example: text
        help:
          type: string
          example: Divide axes by this number
        param:
          type: string
          example: scale-axes
        selectOptions:
          type: array
          items:
            type: object
            properties:
              value:
                type: string
                description: >-
                  What is the string that will be set if this option is
                  selected?
              selected:
                type: boolean
              optionLabel:
                type: string
                description: >-
                  What is the label that will be shown to the user for this
                  option?
              priority:
                type: number
                description: >-
                  The following options are optional.  See Learn Block Auto
                  Config in Notion. Higher priority will get chosen based on
                  limits below.
              romEstimate:
                type: number
                description: >-
                  Estimated ROM footprint for this choice.  Will be tested
                  against ROM budget in Studio.
              needsOps:
                type: array
                items:
                  type: string
                  description: ML operator needed by this choice.
              needsFeatures:
                type: array
                items:
                  type: string
                  description: Feature needed by this choice. (non op related)
        readonly:
          type: boolean
        shouldShow:
          type: boolean
        showIf:
          type: object
          required:
            - parameter
            - operator
            - value
          properties:
            parameter:
              type: string
            operator:
              type: string
              enum:
                - eq
                - neq
            value:
              type: string
        invalidText:
          type: string
        section:
          type: string
          description: Interface section to render parameter in.
          enum:
            - advanced
            - augmentation
            - modelProfiling
        multiline:
          type: boolean
          description: Only valid for type "string". Will render a multiline text area.
        required:
          type: boolean
        hint:
          type: string
          description: If set, shows a hint below the input.
        placeholder:
          type: string
          description: >-
            Sets the placeholder text on the input element (for types "string",
            "int", "float" and "secret")
        showClickToSet:
          type: boolean
          description: If enabled, render a disabled input element with 'Click to set'
        valid:
          type: array
          items:
            type: object
          description: Valid values for parameter.
        items:
          type: object
          description: Recursive definition for items of a parameter with type 'array'.
        properties:
          type: object
          description: Recursive definition for a parameter with type 'object'.
        minVal:
          type: number
          description: Minimum value for parameters of type 'int' or 'float'.
        maxVal:
          type: number
          description: Maximum value for parameters of type 'int' or 'float'.
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