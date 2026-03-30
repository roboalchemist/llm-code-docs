# Source: https://docs.edgeimpulse.com/apis/studio/whitelabels/get-impulse-blocks.md

# Source: https://docs.edgeimpulse.com/apis/studio/optimization/get-impulse-blocks.md

# Source: https://docs.edgeimpulse.com/apis/studio/impulse/get-impulse-blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get impulse blocks

> Lists all possible blocks that can be used in the impulse



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/impulse/blocks
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
  /api/{projectId}/impulse/blocks:
    get:
      tags:
        - Impulse
      summary: Get impulse blocks
      description: Lists all possible blocks that can be used in the impulse
      operationId: getImpulseBlocks
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetImpulseBlocksResponse'
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
    GetImpulseBlocksResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - inputBlocks
            - dspBlocks
            - learnBlocks
            - postProcessingBlocks
          properties:
            inputBlocks:
              type: array
              items:
                $ref: '#/components/schemas/InputBlock'
            dspBlocks:
              type: array
              items:
                $ref: '#/components/schemas/DSPBlock'
            learnBlocks:
              type: array
              items:
                $ref: '#/components/schemas/LearnBlock'
            postProcessingBlocks:
              type: array
              items:
                $ref: '#/components/schemas/PostProcessingBlock'
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
    InputBlock:
      type: object
      required:
        - type
        - title
        - author
        - description
        - name
        - blockType
      properties:
        type:
          type: string
          enum:
            - time-series
            - image
            - features
        title:
          type: string
          example: Time series
        author:
          type: string
          example: Edge Impulse Inc.
        description:
          type: string
        name:
          type: string
          example: Time series
        blockType:
          $ref: '#/components/schemas/BlockType'
    DSPBlock:
      type: object
      required:
        - type
        - title
        - author
        - description
        - name
        - recommended
        - experimental
        - latestImplementationVersion
        - blockType
        - variants
      properties:
        type:
          type: string
          example: spectral-analysis
        title:
          type: string
          example: Spectral features
        author:
          type: string
          example: Edge Impulse Inc.
        description:
          type: string
        name:
          type: string
          example: Spectral analysis
        recommended:
          type: boolean
        experimental:
          type: boolean
        latestImplementationVersion:
          type: integer
        organizationId:
          type: integer
        organizationDspId:
          type: integer
        blockType:
          $ref: '#/components/schemas/BlockType'
        namedAxes:
          type: array
          items:
            $ref: '#/components/schemas/DSPNamedAxis'
        supportedTargets:
          description: >-
            List of target devices that support this DSP block. If undefined
            this block works on all targets.
          type: array
          items:
            type: string
            example: brainchip-akd1000
    LearnBlock:
      type: object
      required:
        - type
        - title
        - author
        - description
        - name
        - recommended
        - blockType
      properties:
        type:
          type: string
          example: spectral-analysis
        title:
          type: string
          example: Spectral features
        author:
          type: string
          example: Edge Impulse Inc.
        description:
          type: string
        name:
          type: string
          example: Spectral analysis
        recommended:
          type: boolean
        organizationModelId:
          type: integer
        publicProjectTierAvailability:
          $ref: '#/components/schemas/PublicProjectTierAvailability'
        isPublicEnterpriseOnly:
          type: boolean
          description: Whether this block is publicly available to only enterprise users
        blockType:
          $ref: '#/components/schemas/BlockType'
        displayCategory:
          $ref: '#/components/schemas/BlockDisplayCategory'
        supportedTargets:
          description: >-
            List of target devices that support this learn block. If undefined
            this block works on all targets.
          type: array
          items:
            type: string
            example: brainchip-akd1000
    PostProcessingBlock:
      type: object
      required:
        - type
        - title
        - author
        - description
        - name
        - recommended
        - experimental
        - latestImplementationVersion
        - blockType
        - defaultParameters
      properties:
        type:
          type: string
          example: object-tracking
        title:
          type: string
          example: Object tracking
        author:
          type: string
          example: Edge Impulse Inc.
        description:
          type: string
        name:
          type: string
          example: Object tracking
        recommended:
          type: boolean
        experimental:
          type: boolean
        latestImplementationVersion:
          type: integer
        blockType:
          $ref: '#/components/schemas/BlockType'
        supportedTargets:
          description: >-
            List of target devices that support this DSP block. If undefined
            this block works on all targets.
          type: array
          items:
            type: string
            example: brainchip-akd1000
        defaultParameters:
          type: array
          items:
            $ref: '#/components/schemas/DSPGroupItem'
    BlockType:
      type: string
      enum:
        - official
        - personal
        - enterprise
        - community
    DSPNamedAxis:
      type: object
      required:
        - name
        - description
        - required
      properties:
        name:
          type: string
        description:
          type: string
        required:
          type: boolean
    PublicProjectTierAvailability:
      description: >-
        For public blocks, this indicates the project tiers for which this block
        is available.
      type: string
      enum:
        - enterprise-only
        - all-projects
        - all-projects-including-whitelabels
    BlockDisplayCategory:
      description: Category to display this block in the UI.
      type: string
      enum:
        - classical
        - tao
        - developer-preview
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