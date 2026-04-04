# Source: https://docs.edgeimpulse.com/apis/studio/optimization/get-config.md

# Source: https://docs.edgeimpulse.com/apis/studio/dsp/get-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get config

> Retrieve the configuration parameters for the DSP block. Use the impulse functions to retrieve all DSP blocks.



## OpenAPI

````yaml .assets/openapi.yaml get /api/{projectId}/dsp/{dspId}
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
  /api/{projectId}/dsp/{dspId}:
    get:
      tags:
        - DSP
      summary: Get config
      description: >-
        Retrieve the configuration parameters for the DSP block. Use the impulse
        functions to retrieve all DSP blocks.
      operationId: getDspConfig
      parameters:
        - $ref: '#/components/parameters/ProjectIdParameter'
        - $ref: '#/components/parameters/DspIdParameter'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DSPConfigResponse'
components:
  parameters:
    ProjectIdParameter:
      name: projectId
      in: path
      required: true
      description: Project ID
      schema:
        type: integer
    DspIdParameter:
      name: dspId
      in: path
      required: true
      description: DSP Block ID, use the impulse functions to retrieve the ID
      schema:
        type: integer
  schemas:
    DSPConfigResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - $ref: '#/components/schemas/DSPConfig'
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
    DSPConfig:
      type: object
      required:
        - dsp
      properties:
        dsp:
          $ref: '#/components/schemas/DSPInfo'
        config:
          type: array
          items:
            $ref: '#/components/schemas/DSPGroup'
        configError:
          type: string
    DSPInfo:
      type: object
      required:
        - id
        - name
        - windowLength
        - type
        - classes
        - features
        - expectedWindowCount
        - inputAxes
        - canCalculateFeatureImportance
        - calculateFeatureImportance
        - canNormalizeData
        - normalizeData
      properties:
        id:
          type: integer
          example: 1
        name:
          type: string
          example: Spectral features
        windowLength:
          type: integer
          example: 3000
        type:
          type: string
          example: spectral-analysis
        classes:
          type: array
          items:
            type: string
        features:
          type: object
          required:
            - generated
          properties:
            generated:
              type: boolean
              description: Whether this block has generated features
            count:
              type: integer
              description: Number of generated features
            labels:
              type: array
              description: Names of the features
              items:
                type: string
            classes:
              type: array
              description: Classes that the features were generated on
              items:
                type: string
        expectedWindowCount:
          type: integer
          description: Expected number of windows that would be generated
        inputAxes:
          type: array
          description: Axes that this block depends on.
          items:
            type: string
        performance:
          $ref: '#/components/schemas/DspPerformance'
        canCalculateFeatureImportance:
          type: boolean
        calculateFeatureImportance:
          type: boolean
        canNormalizeData:
          type: boolean
          description: >-
            Whether this DSP block supports data normalization after features
            were generated. This is true unless "dontAllowDataNormalization" is
            set to true in the DSP block's parameters.json.
        normalizeData:
          $ref: '#/components/schemas/DSPNormalizeData'
          description: Data normalization that was last selected for this block.
        hasAutoTune:
          description: Whether this type of DSP block supports autotuning.
          type: boolean
        minimumVersionForAutotune:
          description: >-
            For DSP blocks that support autotuning, this value specifies the
            minimum block implementation version for which autotuning is
            supported.
          type: number
        hasAutotunerResults:
          description: Whether autotune results exist for this DSP block.
          type: boolean
        usesState:
          description: Whether this DSP block uses state.
          type: boolean
    DSPGroup:
      type: object
      required:
        - group
        - items
      properties:
        group:
          type: string
          example: Scaling
        items:
          type: array
          items:
            $ref: '#/components/schemas/DSPGroupItem'
    DspPerformance:
      type: object
      required:
        - latency
        - ram
      properties:
        latency:
          type: integer
        ram:
          type: integer
        customDspString:
          type: string
          description: >-
            If the project latencyDevice has custom DSP hardware, this value
            contains a device specific latency metric (eg. cycles)
    DSPNormalizeData:
      type: string
      enum:
        - none
        - normalize-channel-standard-scaler
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