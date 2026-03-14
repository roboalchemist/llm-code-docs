# Source: https://docs.statsig.com/api-reference/autotune/get-ranked-list-for-contextual-bandit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Ranked List for Contextual Bandit

> Returns a ranked list of variants for a contextual multi-armed bandit (autotune) experiment. The ranking is based on predicted performance.



## OpenAPI

````yaml http-api/httpopenapi.json post /v1/get_ranked_list
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
  /v1/get_ranked_list:
    post:
      tags:
        - Autotune
      summary: Get Ranked List for Contextual Bandit
      description: >-
        Returns a ranked list of variants for a contextual multi-armed bandit
        (autotune) experiment. The ranking is based on predicted performance.
      operationId: getRankedList
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GetRankedListRequest'
            example:
              configName: product_recommendation_bandit
              user:
                userID: user-123
      responses:
        '200':
          description: Ranked list of variants
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetRankedListResponse'
              example:
                - name: variant_a
                  value:
                    recommendation_algorithm: collaborative_filtering
                  rule_id: rule_123
                  score: 0.85
                - name: variant_b
                  value:
                    recommendation_algorithm: content_based
                  rule_id: rule_124
                  score: 0.72
        '404':
          description: Config not found or not a contextual bandit
components:
  schemas:
    GetRankedListRequest:
      type: object
      required:
        - configName
      properties:
        configName:
          type: string
          minLength: 2
          maxLength: 100
          pattern: ^[a-zA-Z0-9_\- ]+$
          description: Name of the contextual bandit (autotune) experiment
        user:
          $ref: '#/components/schemas/StatsigUser'
        statsigMetadata:
          $ref: '#/components/schemas/StatsigMetadata'
    GetRankedListResponse:
      type: array
      items:
        $ref: '#/components/schemas/CMABVariant'
      description: Array of variants ranked by predicted performance
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
    CMABVariant:
      type: object
      required:
        - name
        - value
        - rule_id
        - score
      properties:
        name:
          type: string
          description: Variant name
        value:
          type: object
          additionalProperties: true
          description: Variant parameter values
        rule_id:
          type: string
          nullable: true
          description: Rule ID for this variant
        score:
          type: number
          format: double
          description: Predicted performance score for this variant
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: statsig-api-key
      description: SDK API key (Server Secret or Client SDK Key)

````

Built with [Mintlify](https://mintlify.com).