# Source: https://docs.statsig.com/api-reference/dynamic-configs/get-dynamic-config-or-experiment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Dynamic Config or Experiment

> Fetches configuration values for a dynamic config or experiment. Works for both types - the system automatically determines which type based on the name. Automatically logs exposure events.



## OpenAPI

````yaml http-api/httpopenapi.json post /v1/get_config
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
  /v1/get_config:
    post:
      tags:
        - Dynamic Configs
        - Experiments
      summary: Get Dynamic Config or Experiment
      description: >-
        Fetches configuration values for a dynamic config or experiment. Works
        for both types - the system automatically determines which type based on
        the name. Automatically logs exposure events.
      operationId: getConfig
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GetConfigRequest'
            examples:
              dynamic_config:
                summary: Get dynamic config
                value:
                  configName: homepage_config
                  user:
                    userID: user-123
              experiment:
                summary: Get experiment config
                value:
                  configName: checkout_flow_test
                  user:
                    userID: user-123
                    country: US
                    custom:
                      subscription_plan: pro
      responses:
        '200':
          description: Configuration values
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetConfigResponse'
              examples:
                config_found:
                  summary: Config with values
                  value:
                    name: homepage_config
                    value:
                      header_text: Welcome!
                      show_banner: true
                      button_color: '#FF5733'
                    group: 2RamGsERWbWMIMnSfOlQuX
                    rule_id: 2RamGsERWbWMIMnSfOlQuX
                    group_name: Power Users
                config_not_found:
                  summary: Config not found
                  value:
                    name: unknown_config
                    value: {}
                    group: ''
                    rule_id: null
                    group_name: null
components:
  schemas:
    GetConfigRequest:
      type: object
      required:
        - configName
      properties:
        configName:
          type: string
          minLength: 2
          maxLength: 100
          pattern: ^[a-zA-Z0-9_\-. ]+$
          description: Name of the dynamic config or experiment
        user:
          $ref: '#/components/schemas/StatsigUser'
        statsigMetadata:
          $ref: '#/components/schemas/StatsigMetadata'
    GetConfigResponse:
      type: object
      required:
        - name
        - value
        - rule_id
        - group_name
      properties:
        name:
          type: string
          description: Config name
        value:
          type: object
          additionalProperties: true
          description: Configuration parameter values as key-value pairs
        group:
          type: string
          description: Rule ID (deprecated, use rule_id instead)
        rule_id:
          type: string
          nullable: true
          description: ID of the rule that matched
        group_name:
          type: string
          nullable: true
          description: Name of the matching group
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