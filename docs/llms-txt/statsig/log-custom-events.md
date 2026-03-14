# Source: https://docs.statsig.com/api-reference/events/log-custom-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Log Custom Events

> Logs one or more custom events for analytics and metric calculation. Events are used to measure experiment outcomes and user behavior.



## OpenAPI

````yaml http-api/httpopenapi.json post /v1/log_event
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
  /v1/log_event:
    post:
      tags:
        - Events
      summary: Log Custom Events
      description: >-
        Logs one or more custom events for analytics and metric calculation.
        Events are used to measure experiment outcomes and user behavior.
      operationId: logEvent
      parameters:
        - name: STATSIG-CLIENT-TIME
          in: header
          required: false
          description: >-
            Client timestamp in milliseconds. Used to normalize event timestamps
            against server time and account for client clock drift.
          schema:
            type: integer
            format: int64
          example: 1616826986211
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LogEventRequest'
            examples:
              single_event:
                summary: Log single event
                value:
                  events:
                    - eventName: add_to_cart
                      value: 29.99
                      time: 1616826986211
                      user:
                        userID: user-123
                      metadata:
                        product_id: prod_456
                        category: electronics
              multiple_events:
                summary: Log multiple events
                value:
                  events:
                    - eventName: page_view
                      time: 1616826986211
                      user:
                        userID: user-123
                      metadata:
                        page: /product/123
                    - eventName: button_click
                      value: add_to_cart
                      time: 1616826987211
                      user:
                        userID: user-123
      responses:
        '202':
          description: Events accepted for processing
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LogEventResponse'
              example:
                success: true
        '503':
          description: Service unavailable
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LogEventResponse'
              example:
                success: false
      servers:
        - url: https://events.statsigapi.net
          description: Events API Server
components:
  schemas:
    LogEventRequest:
      type: object
      required:
        - events
      properties:
        events:
          type: array
          items:
            $ref: '#/components/schemas/StatsigEvent'
          minItems: 1
          description: Array of events to log
        user:
          $ref: '#/components/schemas/StatsigUser'
          description: Shared user object for all events (can be overridden per event)
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
    StatsigEvent:
      type: object
      required:
        - eventName
      properties:
        eventName:
          type: string
          minLength: 1
          description: Name of the event
        value:
          oneOf:
            - type: string
            - type: number
          description: Optional event value (string or number)
        time:
          description: Event timestamp (unix timestamp in milliseconds or ISO date string)
          oneOf:
            - type: integer
              format: int64
            - type: string
              format: date-time
        user:
          $ref: '#/components/schemas/StatsigUser'
          description: User object for this specific event (overrides request-level user)
        metadata:
          type: object
          additionalProperties:
            type: string
          description: Additional event metadata as key-value pairs
        secondaryExposures:
          type: array
          items:
            $ref: '#/components/schemas/ExposureEventMetadata'
          description: Secondary exposures for this event
        statsigMetadata:
          $ref: '#/components/schemas/StatsigMetadata'
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