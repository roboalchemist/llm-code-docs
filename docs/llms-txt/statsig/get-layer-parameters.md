# Source: https://docs.statsig.com/api-reference/layers/get-layer-parameters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Layer Parameters

> Fetches parameter values from a layer. Layers allow you to share parameters across multiple experiments. Automatically logs exposure events.



## OpenAPI

````yaml http-api/httpopenapi.json post /v1/get_layer
openapi: 3.0.0
info:
  title: Statsig SDK HTTP API
  version: 1.0.0
  description: >-
    HTTP API for Statsig SDK operations including feature gates, dynamic
    configs, experiments, layers, and event logging.


    **⚠️ Important:** We strongly recommend using official SDKs instead of
    direct HTTP calls when possible. SDKs provide better performance, automatic
    error handling, and type safety.


    ## Authentication


    All requests require the `statsig-api-key` header with either:

    - **Server Secret Key** - for server-side use only, never expose in client
    code

    - **Client SDK Key** - safe for use in client-side applications


    ## Rate Limiting


    Requests are rate limited. The rate limit increments vary by endpoint
    (typically 2 per request).


    ## Base URLs


    - SDK API operations: `https://api.statsig.com`

    - Event logging: `https://events.statsigapi.net`
  contact:
    name: Statsig Support
    url: https://www.statsig.com/slack
servers:
  - url: https://api.statsig.com
    description: SDK API Server
  - url: https://events.statsigapi.net
    description: Events API Server
security:
  - ApiKeyAuth: []
tags:
  - name: Feature Gates
    description: Check feature gate evaluations
  - name: Dynamic Configs
    description: Fetch dynamic configuration values
  - name: Experiments
    description: Get experiment assignments and configurations
  - name: Layers
    description: Retrieve layer parameter values
  - name: Autotune
    description: Get ranked lists for contextual multi-armed bandits
  - name: Events
    description: Log custom events and exposures
paths:
  /v1/get_layer:
    post:
      tags:
        - Layers
      summary: Get Layer Parameters
      description: >-
        Fetches parameter values from a layer. Layers allow you to share
        parameters across multiple experiments. Automatically logs exposure
        events.
      operationId: getLayer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GetLayerRequest'
            example:
              layerName: product_page_layer
              user:
                userID: user-123
      responses:
        '200':
          description: Layer parameter values
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetLayerResponse'
              examples:
                layer_with_experiment:
                  summary: Layer allocated to experiment
                  value:
                    name: product_page_layer
                    value:
                      add_to_cart_color: blue
                      price_format: compact
                      show_reviews: true
                    ruleID: rule_abc123
                    allocatedExperimentName: add_to_cart_experiment
                layer_no_experiment:
                  summary: Layer without experiment allocation
                  value:
                    name: product_page_layer
                    value:
                      add_to_cart_color: green
                      price_format: detailed
                    ruleID: default
                    allocatedExperimentName: null
        '404':
          description: Layer not found
components:
  schemas:
    GetLayerRequest:
      type: object
      required:
        - layerName
      properties:
        layerName:
          type: string
          description: Name of the layer
        user:
          $ref: '#/components/schemas/StatsigUser'
        statsigMetadata:
          $ref: '#/components/schemas/StatsigMetadata'
    GetLayerResponse:
      type: object
      required:
        - name
        - value
      properties:
        name:
          type: string
          description: Layer name
        value:
          type: object
          additionalProperties: true
          description: Layer parameter values
        ruleID:
          type: string
          description: ID of the rule that was evaluated
        allocatedExperimentName:
          type: string
          description: Name of the experiment this layer is allocated to (if any)
    StatsigUser:
      type: object
      description: >-
        User object containing identification and attributes for evaluation. At
        minimum, provide at least one identifier.
      properties:
        userID:
          type: string
          description: Primary user identifier
          example: user-123
        email:
          type: string
          format: email
          description: User email address
          example: user@example.com
        ip:
          type: string
          description: User IP address for geo-targeting
          example: 192.168.1.1
        userAgent:
          type: string
          description: User agent string for device/browser targeting
          example: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
        country:
          type: string
          description: 2-letter country code (ISO 3166-1 alpha-2)
          example: US
        locale:
          type: string
          description: Locale/language code
          example: en_US
        appVersion:
          type: string
          description: Application version
          example: 1.2.3
        custom:
          type: object
          additionalProperties: true
          description: >-
            Custom user attributes for targeting (string, number, boolean, or
            array of strings)
          example:
            subscription_plan: premium
            account_age_days: 45
            is_beta_tester: true
        privateAttributes:
          type: object
          additionalProperties: true
          description: Private attributes used for evaluation but not logged to analytics
          example:
            internal_user_id: '12345'
        customIDs:
          type: object
          additionalProperties:
            type: string
          description: Additional custom identifier mappings
          example:
            companyID: company-456
            deviceID: device-789
        statsigEnvironment:
          type: object
          description: Environment tier for targeting
          properties:
            tier:
              type: string
              enum:
                - production
                - staging
                - development
              description: Environment tier
    StatsigMetadata:
      type: object
      additionalProperties: true
      description: >-
        SDK metadata for tracking SDK type, version, and other diagnostic
        information
      properties:
        sdkType:
          type: string
          description: SDK type sending the request (e.g., js-client)
        sdkVersion:
          type: string
          description: SDK version
        exposureLoggingDisabled:
          type: boolean
          description: >-
            When true, prevents the HTTP API from automatically logging
            exposures. Use this only if you will handle exposure logging
            yourself.
      example:
        sdkType: js-client
        sdkVersion: 4.20.0
        exposureLoggingDisabled: false
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: statsig-api-key
      description: SDK API key (Server Secret or Client SDK Key)

````

Built with [Mintlify](https://mintlify.com).