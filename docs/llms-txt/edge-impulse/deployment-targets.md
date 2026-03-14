# Source: https://docs.edgeimpulse.com/apis/studio/deployment/deployment-targets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deployment targets

> List all deployment targets



## OpenAPI

````yaml .assets/openapi.yaml get /api/deployment/targets
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
  /api/deployment/targets:
    get:
      tags:
        - Deployment
      summary: Deployment targets
      description: List all deployment targets
      operationId: listAllDeploymentTargets
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeploymentTargetsResponse'
components:
  schemas:
    DeploymentTargetsResponse:
      allOf:
        - $ref: '#/components/schemas/GenericApiResponse'
        - type: object
          required:
            - targets
          properties:
            targets:
              type: array
              items:
                $ref: '#/components/schemas/DeploymentTarget'
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
    DeploymentTarget:
      type: object
      required:
        - name
        - description
        - image
        - imageClasses
        - format
        - hasEonCompiler
        - hasTensorRT
        - hasTensaiFlow
        - hasDRPAI
        - hasTIDL
        - hasAkida
        - hasMemryx
        - hasStAton
        - hasCevaNpn
        - hasNordicAxon
        - hideOptimizations
        - uiSection
        - supportedEngines
        - preferredEngine
        - modelVariants
        - docsUrl
        - parameters
      properties:
        name:
          type: string
        description:
          type: string
        image:
          type: string
        imageClasses:
          type: string
        format:
          type: string
        latencyDevice:
          type: string
        hasEonCompiler:
          type: boolean
          description: Preferably use supportedEngines / preferredEngine
        hasTensorRT:
          type: boolean
          description: Preferably use supportedEngines / preferredEngine
        hasTensaiFlow:
          type: boolean
          description: Preferably use supportedEngines / preferredEngine
        hasDRPAI:
          type: boolean
          description: Preferably use supportedEngines / preferredEngine
        hasTIDL:
          type: boolean
          description: Preferably use supportedEngines / preferredEngine
        hasAkida:
          type: boolean
          description: Preferably use supportedEngines / preferredEngine
        hasMemryx:
          type: boolean
          description: Preferably use supportedEngines / preferredEngine
        hasStAton:
          type: boolean
          description: Preferably use supportedEngines / preferredEngine
        hasCevaNpn:
          type: boolean
          description: Preferably use supportedEngines / preferredEngine
        hasNordicAxon:
          type: boolean
          description: Preferably use supportedEngines / preferredEngine
        hideOptimizations:
          type: boolean
        badge:
          type: object
          required:
            - name
            - description
          properties:
            name:
              type: string
            description:
              type: string
        uiSection:
          type: string
          enum:
            - library
            - firmware
            - mobile
            - hidden
        customDeployId:
          type: integer
        customDeployOrganizationId:
          type: integer
        integrateUrl:
          type: string
        ownerOrganizationName:
          type: string
        supportedEngines:
          type: array
          items:
            $ref: '#/components/schemas/DeploymentTargetEngine'
        preferredEngine:
          $ref: '#/components/schemas/DeploymentTargetEngine'
        url:
          type: string
        docsUrl:
          type: string
        firmwareRepoUrl:
          type: string
        modelVariants:
          type: array
          items:
            $ref: '#/components/schemas/DeploymentTargetVariant'
        parameters:
          type: array
          items:
            $ref: '#/components/schemas/DSPGroupItem'
        redirect:
          type: object
          description: >-
            An optional redirect field for integration partners to be shown in
            addition to the docs link, i.e. for directing users to a partner's
            website or application once deployment completes. This is
            experimental and may change in the future.
          properties:
            url:
              type: string
            text:
              type: string
    DeploymentTargetEngine:
      type: string
      enum:
        - tflite
        - tflite-eon
        - tflite-eon-ram-optimized
        - tensorrt
        - tensaiflow
        - drp-ai
        - tidl
        - akida
        - syntiant
        - memryx
        - neox
        - ethos-linux
        - st-aton
        - ceva-npn
        - nordic-axon
        - vlm-connector
    DeploymentTargetVariant:
      type: object
      required:
        - variant
        - supported
      properties:
        variant:
          $ref: '#/components/schemas/KerasModelVariantEnum'
        supported:
          type: boolean
        hint:
          type: string
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
    KerasModelVariantEnum:
      type: string
      enum:
        - int8
        - float32
        - akida
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