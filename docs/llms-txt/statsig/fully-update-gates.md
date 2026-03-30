# Source: https://docs.statsig.com/api-reference/gates/fully-update-gates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Fully Update Gates



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/gates/{id}
openapi: 3.0.0
info:
  title: Console API
  description: >-
    The "Console API" is the CRUD API for performing the actions offered on
    console.statsig.com without needing to go through the web UI.

    If you have any feature requests, drop on in to our [slack
    channel](https://www.statsig.com/slack) and let us know.

    <br /><br />

    <b>Authorization</b>

    <br />

    All requests must include the **STATSIG-API-KEY** field in the header. The
    value should be a **Console API Key** which can be created in the Project
    Settings on
    [console.statsig.com/api_keys](https://console.statsig.com/api_keys)

    <br /><br />

    <b>Rate Limiting</b>

    <br />

    Requests to the Console API are limited to <code>~ 100reqs / 10secs and ~
    900reqs / 15 mins</code>.

    <br /><br />

    <b>Keyboard Search</b>

    <br />

    Use <code>Ctrl/Cmd + K</code> to search for specific endpoints.
  version: 20240601.0.0
  contact: {}
servers:
  - url: https://statsigapi.net
security: []
tags: []
paths:
  /console/v1/gates/{id}:
    post:
      tags:
        - Gates
      summary: Fully Update Gates
      parameters:
        - name: id
          required: true
          in: path
          description: id
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GateFullUpdateDto'
      responses:
        '200':
          description: Update gate response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/ExternalGateDto'
                example:
                  data:
                    checksPerHour: 0
                    createdTime: 1705439406615
                    creatorEmail: null
                    creatorID: 4R5PV7mvYdW6NLCwK8ocoz
                    creatorName: CONSOLE API
                    description: Updated Gate Description
                    holdoutIDs: []
                    id: a_gate
                    idType: stableID
                    isEnabled: false
                    lastModifiedTime: 1705439409750
                    lastModifierEmail: null
                    lastModifierID: 4R5PV7mvYdW6NLCwK8ocoz
                    lastModifierName: CONSOLE API
                    name: A Gate
                    rules:
                      - conditions:
                          - operator: any
                            targetValue:
                              - '111'
                              - '222'
                            type: user_id
                          - operator: str_contains_any
                            targetValue:
                              - '@outlook.com'
                              - '@gmail.com'
                            type: email
                          - field: age
                            operator: gt
                            targetValue: 31
                            type: custom_field
                          - operator: version_gt
                            targetValue: 1.1.1
                            type: app_version
                          - operator: any
                            targetValue:
                              - Android
                              - Chrome
                            type: browser_name
                          - operator: any
                            targetValue:
                              - 94.0.4606.81
                              - 94.0.4606.92
                            type: browser_version
                          - operator: none
                            targetValue:
                              - Android
                              - Windows
                            type: os_name
                          - operator: version_lte
                            targetValue: 11.0.0
                            type: os_version
                          - operator: any
                            targetValue:
                              - NZ
                              - US
                            type: country
                          - operator: any
                            targetValue:
                              - production
                            type: environment_tier
                          - targetValue: growth_org
                            type: passes_segment
                          - targetValue: growth_org
                            type: fails_segment
                          - operator: any
                            targetValue:
                              - 1.1.1.1
                              - 8.8.8.8
                            type: ip_address
                          - customID: userID
                            operator: any
                            targetValue:
                              - '31'
                            type: unit_id
                        environments: null
                        name: All Conditions
                        passPercentage: 10
                    status: Disabled
                    tags:
                      - ★ Core
                    targetApps: []
                    type: PERMANENT
                    typeReason: NONE
                    team: null
                    reviewSettings:
                      requiredReview: false
                      allowedReviewers: []
                    measureMetricLifts: true
                    store0100Exposures: false
                    owner:
                      ownerID: user123
                      ownerName: CONSOLE API
                      ownerType: SDK_KEY
                      ownerEmail: ''
                    monitoringMetrics: []
                    version: 2
                  message: Gate updated successfully.
              example:
                data:
                  checksPerHour: 0
                  createdTime: 1705439406615
                  creatorEmail: null
                  creatorID: 4R5PV7mvYdW6NLCwK8ocoz
                  creatorName: CONSOLE API
                  description: Updated Gate Description
                  holdoutIDs: []
                  id: a_gate
                  idType: stableID
                  isEnabled: false
                  lastModifiedTime: 1705439409750
                  lastModifierEmail: null
                  lastModifierID: 4R5PV7mvYdW6NLCwK8ocoz
                  lastModifierName: CONSOLE API
                  name: A Gate
                  rules:
                    - conditions:
                        - operator: any
                          targetValue:
                            - '111'
                            - '222'
                          type: user_id
                        - operator: str_contains_any
                          targetValue:
                            - '@outlook.com'
                            - '@gmail.com'
                          type: email
                        - field: age
                          operator: gt
                          targetValue: 31
                          type: custom_field
                        - operator: version_gt
                          targetValue: 1.1.1
                          type: app_version
                        - operator: any
                          targetValue:
                            - Android
                            - Chrome
                          type: browser_name
                        - operator: any
                          targetValue:
                            - 94.0.4606.81
                            - 94.0.4606.92
                          type: browser_version
                        - operator: none
                          targetValue:
                            - Android
                            - Windows
                          type: os_name
                        - operator: version_lte
                          targetValue: 11.0.0
                          type: os_version
                        - operator: any
                          targetValue:
                            - NZ
                            - US
                          type: country
                        - operator: any
                          targetValue:
                            - production
                          type: environment_tier
                        - targetValue: growth_org
                          type: passes_segment
                        - targetValue: growth_org
                          type: fails_segment
                        - operator: any
                          targetValue:
                            - 1.1.1.1
                            - 8.8.8.8
                          type: ip_address
                        - customID: userID
                          operator: any
                          targetValue:
                            - '31'
                          type: unit_id
                      environments: null
                      name: All Conditions
                      passPercentage: 10
                  status: Disabled
                  tags:
                    - ★ Core
                  targetApps: []
                  type: PERMANENT
                  typeReason: NONE
                  team: null
                  reviewSettings:
                    requiredReview: false
                    allowedReviewers: []
                  measureMetricLifts: true
                  store0100Exposures: false
                  owner:
                    ownerID: user123
                    ownerName: CONSOLE API
                    ownerType: SDK_KEY
                    ownerEmail: ''
                  monitoringMetrics: []
                  version: 2
                message: Gate updated successfully.
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    GateFullUpdateDto:
      type: object
      properties:
        name:
          type: string
          maxLength: 100
          minLength: 3
          pattern: ^[a-zA-Z0-9_\-. ]*$
          description: The gate display name
        isEnabled:
          type: boolean
        description:
          type: string
          maxLength: 1000
        rules:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                description: The name of this rule.
              passPercentage:
                type: number
                minimum: 0
                maximum: 100
                multipleOf: 0.01
                description: >-
                  Of the users that meet the conditions of this rule, what
                  percent should return true.
              conditions:
                type: array
                items:
                  type: object
                  properties:
                    targetValue:
                      oneOf:
                        - type: array
                          items:
                            type: string
                        - type: array
                          items:
                            type: number
                        - type: string
                        - type: number
                      nullable: true
                    operator:
                      type: string
                    field:
                      type: string
                      nullable: true
                    customID:
                      type: string
                      nullable: true
                    type:
                      type: string
                      enum:
                        - app_version
                        - browser_name
                        - browser_version
                        - country
                        - custom_field
                        - email
                        - environment_tier
                        - fails_gate
                        - fails_segment
                        - ip_address
                        - locale
                        - os_name
                        - os_version
                        - passes_gate
                        - passes_segment
                        - public
                        - time
                        - unit_id
                        - user_id
                        - user_agent
                        - url
                        - javascript
                        - device_model
                        - target_app
                        - experiment_group
                  required:
                    - type
                description: An array of Condition objects.
              environments:
                type: array
                items:
                  type: string
                nullable: true
                description: The environments this rule is enabled for.
              id:
                type: string
                description: The Statsig ID of this rule.
              baseID:
                type: string
                description: >-
                  The base ID of this rule, i.e. without any added metadata.
                  Will remain the exact same throughout
              returnValue:
                type: object
                additionalProperties: {}
                description: The return value of the rule.
              completedAutomatedRollouts:
                type: array
                items:
                  type: object
                  properties:
                    time:
                      type: number
                    passPercent:
                      type: number
                  required:
                    - passPercent
                readOnly: true
                description: >-
                  Read-only: Automated rollout phases that have already
                  completed.
              pendingAutomatedRollouts:
                type: array
                items:
                  type: object
                  properties:
                    time:
                      type: number
                    passPercent:
                      type: number
                  required:
                    - passPercent
                readOnly: true
                description: >-
                  Read-only: Automated rollout phases that are scheduled but not
                  yet complete.
            required:
              - name
              - passPercentage
              - conditions
        tags:
          type: array
          items:
            type: string
        type:
          type: string
          enum:
            - PERMANENT
            - TEMPORARY
        idType:
          type: string
        targetApps:
          oneOf:
            - type: string
            - type: array
              items:
                type: string
        creatorID:
          type: string
          nullable: true
        creatorEmail:
          type: string
          nullable: true
        team:
          type: string
          nullable: true
        teamID:
          type: string
          nullable: true
        measureMetricLifts:
          type: boolean
        monitoringMetrics:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
              type:
                type: string
            required:
              - name
              - type
        reviewSettings:
          type: object
          properties:
            requiredReview:
              type: boolean
          required:
            - requiredReview
          description: >-
            Whether reviews are required for this gate. If a gate has reviews
            required due to a project-level or team-level setting, setting this
            will have no effect.
        releasePipelineID:
          type: string
          nullable: true
      required:
        - isEnabled
        - description
        - rules
      example:
        isEnabled: false
        description: Updated Gate Description
        rules:
          - name: All Conditions
            passPercentage: 10
            conditions:
              - type: user_id
                targetValue:
                  - '111'
                  - '222'
                operator: any
              - type: email
                targetValue:
                  - '@outlook.com'
                  - '@gmail.com'
                operator: str_contains_any
              - type: custom_field
                targetValue: 31
                operator: gt
                field: age
              - type: app_version
                targetValue: 1.1.1
                operator: version_gt
              - type: browser_name
                targetValue:
                  - Android
                  - Chrome
                operator: any
              - type: browser_version
                targetValue:
                  - 94.0.4606.81
                  - 94.0.4606.92
                operator: any
              - type: os_name
                targetValue:
                  - Android
                  - Windows
                operator: none
              - type: os_version
                targetValue: 11.0.0
                operator: version_lte
              - type: country
                targetValue:
                  - NZ
                  - US
                operator: any
              - type: environment_tier
                targetValue:
                  - production
                operator: any
              - type: passes_segment
                targetValue: growth_org
              - type: fails_segment
                targetValue: growth_org
              - type: ip_address
                targetValue:
                  - 1.1.1.1
                  - 8.8.8.8
                operator: any
              - type: unit_id
                operator: any
                targetValue:
                  - '31'
                customID: userID
        tags:
          - ★ Core
        type: TEMPORARY
        idType: stableID
        targetApps: []
    SingleDataResponse:
      type: object
      properties:
        message:
          type: string
          description: A simple string explaining the result of the operation.
        data:
          type: object
          description: A single result.
      required:
        - message
        - data
    ExternalGateDto:
      type: object
      properties:
        id:
          type: string
          description: ID
        name:
          type: string
          maxLength: 100
          minLength: 3
          pattern: ^[a-zA-Z0-9_\-. ]*$
          description: The gate display name
        idType:
          type: string
        description:
          type: string
          maxLength: 1000
        lastModifierID:
          type: string
          nullable: true
          description: ID of the last modifier.
        lastModifiedTime:
          type: number
          nullable: true
          description: Time of the last modification.
          format: double
        lastModifierEmail:
          type: string
          nullable: true
          description: Email of the last modifier.
        lastModifierName:
          type: string
          nullable: true
          description: Name of the last modifier.
        creatorID:
          type: string
          nullable: true
        createdTime:
          type: number
          description: Timestamp when the entity was created.
          format: double
        creatorName:
          type: string
          nullable: true
          description: Name of the creator.
        creatorEmail:
          type: string
          nullable: true
        tags:
          type: array
          items:
            type: string
        targetApps:
          oneOf:
            - type: string
            - type: array
              items:
                type: string
        holdoutIDs:
          type: array
          items:
            type: string
          description: Holdouts applied to this configuration.
        team:
          type: string
          nullable: true
        teamID:
          type: string
          nullable: true
        version:
          type: number
          description: Version number
          format: double
        checksPerHour:
          type: number
          nullable: true
          format: double
        status:
          type: string
          enum:
            - In Progress
            - Launched
            - Disabled
            - Archived
        type:
          type: string
          enum:
            - TEMPORARY
            - PERMANENT
            - STALE
            - TEMPLATE
        typeReason:
          type: string
          enum:
            - NONE
            - STALE_PROBABLY_LAUNCHED
            - STALE_PROBABLY_UNLAUNCHED
            - STALE_PROBABLY_FORGOTTEN
            - STALE_NO_RULES
            - STALE_PROBABLY_DEAD_CHECK
            - STALE_EMPTY_CHECKS
            - STALE_ALL_TRUE
            - STALE_ALL_FALSE
        owner:
          type: object
          properties:
            ownerID:
              type: string
              description: ID of the owner
              example: abc123
            ownerType:
              type: string
              description: Type of the owner (e.g., SDK_KEY or USER)
              example: USER
            ownerName:
              type: string
              description: The name of the owner. This field is optional.
              example: John Doe
            ownerEmail:
              type: string
              description: The email of the owner. This field is optional.
          description: >-
            Schema for owner data including ID, type, name. Note that if Entity
            is created by CONSOLE API, owner will be undefined.
          example:
            ownerID: user123
            ownerType: USER
            ownerName: John Doe
            ownerEmail: owner123@test.com
          nullable: true
        isTemplate:
          type: boolean
        store0100Exposures:
          type: boolean
          description: Whether this gate stores 0/100 exposures for monitoring/analysis.
        isEnabled:
          type: boolean
        rules:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                description: The name of this rule.
              passPercentage:
                type: number
                minimum: 0
                maximum: 100
                multipleOf: 0.01
                description: >-
                  Of the users that meet the conditions of this rule, what
                  percent should return true.
              conditions:
                type: array
                items:
                  type: object
                  properties:
                    targetValue:
                      oneOf:
                        - type: array
                          items:
                            type: string
                        - type: array
                          items:
                            type: number
                        - type: string
                        - type: number
                      nullable: true
                    operator:
                      type: string
                    field:
                      type: string
                      nullable: true
                    customID:
                      type: string
                      nullable: true
                    type:
                      type: string
                      enum:
                        - app_version
                        - browser_name
                        - browser_version
                        - country
                        - custom_field
                        - email
                        - environment_tier
                        - fails_gate
                        - fails_segment
                        - ip_address
                        - locale
                        - os_name
                        - os_version
                        - passes_gate
                        - passes_segment
                        - public
                        - time
                        - unit_id
                        - user_id
                        - user_agent
                        - url
                        - javascript
                        - device_model
                        - target_app
                        - experiment_group
                  required:
                    - type
                description: An array of Condition objects.
              environments:
                type: array
                items:
                  type: string
                nullable: true
                description: The environments this rule is enabled for.
              id:
                type: string
                description: The Statsig ID of this rule.
              baseID:
                type: string
                description: >-
                  The base ID of this rule, i.e. without any added metadata.
                  Will remain the exact same throughout
              returnValue:
                type: object
                additionalProperties: {}
                description: The return value of the rule.
              completedAutomatedRollouts:
                type: array
                items:
                  type: object
                  properties:
                    time:
                      type: number
                    passPercent:
                      type: number
                  required:
                    - passPercent
                readOnly: true
                description: >-
                  Read-only: Automated rollout phases that have already
                  completed.
              pendingAutomatedRollouts:
                type: array
                items:
                  type: object
                  properties:
                    time:
                      type: number
                    passPercent:
                      type: number
                  required:
                    - passPercent
                readOnly: true
                description: >-
                  Read-only: Automated rollout phases that are scheduled but not
                  yet complete.
            required:
              - name
              - passPercentage
              - conditions
        measureMetricLifts:
          type: boolean
        monitoringMetrics:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
              type:
                type: string
            required:
              - name
              - type
        reviewSettings:
          type: object
          properties:
            requiredReview:
              type: boolean
            allowedReviewers:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: string
                  name:
                    type: string
                  email:
                    type: string
                required:
                  - id
                  - name
                  - email
              nullable: true
          required:
            - requiredReview
        releasePipelineID:
          type: string
          nullable: true
        activeReview:
          type: object
          properties:
            reviewID:
              type: string
            reviewStatus:
              type: string
            description:
              type: string
          required:
            - reviewID
            - reviewStatus
            - description
      required:
        - id
        - description
        - lastModifierID
        - lastModifiedTime
        - lastModifierEmail
        - lastModifierName
        - createdTime
        - creatorName
        - checksPerHour
        - status
        - type
        - typeReason
        - isEnabled
        - rules
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).