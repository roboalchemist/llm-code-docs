# Source: https://docs.statsig.com/api-reference/feature-gates/check-feature-gates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Check Feature Gate(s)

> Evaluates one or more feature gates for a user and returns pass/fail results. Automatically logs exposure events for analytics.



## OpenAPI

````yaml http-api/httpopenapi.json post /v1/check_gate
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
  /v1/check_gate:
    post:
      tags:
        - Feature Gates
      summary: Check Feature Gate(s)
      description: >-
        Evaluates one or more feature gates for a user and returns pass/fail
        results. Automatically logs exposure events for analytics.
      operationId: checkGate
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CheckGateRequest'
            examples:
              single_gate:
                summary: Check single gate
                value:
                  gateName: new_user_onboarding
                  user:
                    userID: user-123
                    email: user@example.com
              multiple_gates:
                summary: Check multiple gates
                value:
                  gateNames:
                    - feature_a
                    - feature_b
                    - feature_c
                  user:
                    userID: user-123
                    custom:
                      tier: premium
      responses:
        '200':
          description: Gate evaluation result(s)
          content:
            application/json:
              schema:
                oneOf:
                  - $ref: '#/components/schemas/CheckGateResponse'
                  - type: object
                    additionalProperties:
                      $ref: '#/components/schemas/CheckGateResponse'
                    description: >-
                      Map of gate names to their evaluation results (when
                      checking multiple gates)
              examples:
                single_gate_pass:
                  summary: Single gate passing
                  value:
                    name: new_user_onboarding
                    value: true
                    rule_id: 2RamGsERWbWMIMnSfOlQuX
                    group_name: Test Group
                single_gate_fail:
                  summary: Single gate failing
                  value:
                    name: new_user_onboarding
                    value: false
                    rule_id: null
                    group_name: null
                multiple_gates:
                  summary: Multiple gates response
                  value:
                    feature_a:
                      name: feature_a
                      value: true
                      rule_id: rule_123
                      group_name: Enabled
                    feature_b:
                      name: feature_b
                      value: false
                      rule_id: null
                      group_name: null
                    feature_c:
                      name: feature_c
                      value: true
                      rule_id: rule_456
                      group_name: Control
components:
  schemas:
    CheckGateRequest:
      type: object
      properties:
        gateName:
          type: string
          minLength: 2
          maxLength: 100
          pattern: ^[a-zA-Z0-9_\-. ]+$
          description: Single gate name to check (use this OR gateNames, not both)
        gateNames:
          type: array
          items:
            type: string
            minLength: 2
            maxLength: 100
            pattern: ^[a-zA-Z0-9_\-. ]+$
          minItems: 1
          maxItems: 100
          description: Array of gate names to check (use this OR gateName, not both)
        user:
          $ref: '#/components/schemas/StatsigUser'
        statsigMetadata:
          $ref: '#/components/schemas/StatsigMetadata'
      oneOf:
        - required:
            - gateName
        - required:
            - gateNames
    CheckGateResponse:
      type: object
      required:
        - name
        - value
        - rule_id
        - group_name
      properties:
        name:
          type: string
          description: Gate name
        value:
          type: boolean
          description: Whether the gate passes for this user
        rule_id:
          type: string
          nullable: true
          description: ID of the rule that matched (null if gate failed)
        group_name:
          type: string
          nullable: true
          description: Name of the matching group (null if gate failed)
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