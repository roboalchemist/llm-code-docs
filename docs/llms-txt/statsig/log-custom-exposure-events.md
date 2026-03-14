# Source: https://docs.statsig.com/api-reference/events/log-custom-exposure-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Log Custom Exposure Events

> Manually logs exposure events for experiments or feature gates. Useful for analytics-only experiments, delayed exposure logging, or when automatic exposure logging is disabled.



## OpenAPI

````yaml http-api/httpopenapi.json post /v1/log_custom_exposure
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
  /v1/log_custom_exposure:
    post:
      tags:
        - Events
      summary: Log Custom Exposure Events
      description: >-
        Manually logs exposure events for experiments or feature gates. Useful
        for analytics-only experiments, delayed exposure logging, or when
        automatic exposure logging is disabled.
      operationId: logCustomExposure
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LogCustomExposureRequest'
            examples:
              experiment_exposure:
                summary: Log experiment exposure
                value:
                  exposures:
                    - user:
                        userID: user-123
                      experimentName: checkout_flow_v2
                      group: Test Group
                      ruleID: rule_abc123
                      secondaryExposures:
                        - gate: is_employee
                          gateValue: 'false'
                          ruleID: default
              gate_exposure:
                summary: Log gate exposure
                value:
                  exposures:
                    - user:
                        userID: user-123
                      gateName: premium_features
                      passes: true
                      ruleID: premium_rule
      responses:
        '202':
          description: Exposures accepted for processing
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LogEventResponse'
              example:
                success: true
      servers:
        - url: https://events.statsigapi.net
          description: Events API Server
components:
  schemas:
    LogCustomExposureRequest:
      type: object
      required:
        - exposures
      properties:
        exposures:
          type: array
          items:
            $ref: '#/components/schemas/ExposureEvent'
          minItems: 1
          description: Array of exposure events to log
        user:
          $ref: '#/components/schemas/StatsigUser'
          description: Shared user object for all exposures
        statsigMetadata:
          $ref: '#/components/schemas/StatsigMetadata'
    LogEventResponse:
      type: object
      required:
        - success
      properties:
        success:
          type: boolean
          description: Whether the request was successful
    ExposureEvent:
      type: object
      oneOf:
        - $ref: '#/components/schemas/ExperimentExposure'
        - $ref: '#/components/schemas/GateExposure'
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
    ExperimentExposure:
      type: object
      required:
        - experimentName
      properties:
        experimentName:
          type: string
          minLength: 1
          description: Name of the experiment or dynamic config
        user:
          $ref: '#/components/schemas/StatsigUser'
        group:
          type: string
          minLength: 1
          description: Group name (use this OR ruleID)
        ruleID:
          type: string
          description: Rule ID (use this OR group)
        time:
          description: Exposure timestamp
          oneOf:
            - type: integer
              format: int64
            - type: string
        secondaryExposures:
          type: array
          items:
            $ref: '#/components/schemas/ExposureEventMetadata'
      oneOf:
        - required:
            - experimentName
            - group
        - required:
            - experimentName
            - ruleID
    GateExposure:
      type: object
      required:
        - gateName
        - passes
      properties:
        gateName:
          type: string
          minLength: 1
          description: Name of the feature gate
        passes:
          type: boolean
          description: Whether the gate passed
        user:
          $ref: '#/components/schemas/StatsigUser'
        group:
          type: string
          minLength: 1
          description: Group name (use this OR ruleID)
        ruleID:
          type: string
          description: Rule ID (use this OR group)
        time:
          description: Exposure timestamp
          oneOf:
            - type: integer
              format: int64
            - type: string
        secondaryExposures:
          type: array
          items:
            $ref: '#/components/schemas/ExposureEventMetadata'
      oneOf:
        - required:
            - gateName
            - passes
            - group
        - required:
            - gateName
            - passes
            - ruleID
    ExposureEventMetadata:
      type: object
      required:
        - gate
        - gateValue
        - ruleID
      properties:
        gate:
          type: string
          description: Name of the gate
        gateValue:
          type: string
          description: Gate value as string ('true' or 'false')
        ruleID:
          type: string
          description: Rule ID that was evaluated
      description: Secondary exposure tracking for gates checked during evaluation
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: statsig-api-key
      description: SDK API key (Server Secret or Client SDK Key)

````

Built with [Mintlify](https://mintlify.com).