# Source: https://docs.statsig.com/api-reference/gates/update-gate-rules.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Gate Rules

> Update all given rules. It does NOT create or delete if you add more rules and remove rules in the rules object.



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json patch /console/v1/gates/{id}/rules/{ruleID}
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
  /console/v1/gates/{id}/rules/{ruleID}:
    patch:
      tags:
        - Gates
      summary: Update Gate Rules
      description: >-
        Update all given rules. It does NOT create or delete if you add more
        rules and remove rules in the rules object.
      parameters:
        - name: id
          required: true
          in: path
          description: Gate ID
          schema:
            type: string
        - name: ruleID
          required: true
          in: path
          description: Rule ID
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RuleUpdateDto'
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
                  message: Gate updated successfully.
                  data:
                    id: a_gate
                    isEnabled: true
                    description: helpful summary of what this gate does
                    status: In Progress
                    lastModifierName: CONSOLE API
                    lastModifierID: 1vaasdfLlkaujjajiuOSBP2
                    rules:
                      - name: All Conditions
                        id: 38ttpCpzrQFTMKcqFKk02l:10.00:1
                        baseID: 38ttpCpzrQFTMKcqFKk02l
                        passPercentage: 10
                        conditions:
                          - type: user_id
                            targetValue:
                              - 35sClJFs8l0y5uRQhDwUDo
                            operator: any
                        environments:
                          - staging
                    tags:
                      - '* Core'
              example:
                message: Gate updated successfully.
                data:
                  id: a_gate
                  isEnabled: true
                  description: helpful summary of what this gate does
                  status: In Progress
                  lastModifierName: CONSOLE API
                  lastModifierID: 1vaasdfLlkaujjajiuOSBP2
                  rules:
                    - name: All Conditions
                      id: 38ttpCpzrQFTMKcqFKk02l:10.00:1
                      baseID: 38ttpCpzrQFTMKcqFKk02l
                      passPercentage: 10
                      conditions:
                        - type: user_id
                          targetValue:
                            - 35sClJFs8l0y5uRQhDwUDo
                          operator: any
                      environments:
                        - staging
                  tags:
                    - '* Core'
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    RuleUpdateDto:
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
            Of the users that meet the conditions of this rule, what percent
            should return true.
          format: double
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
            The base ID of this rule, i.e. without any added metadata. Will
            remain the exact same throughout
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
          description: 'Read-only: Automated rollout phases that have already completed.'
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
            Read-only: Automated rollout phases that are scheduled but not yet
            complete.
      example:
        name: All Conditions
        id: 38ttpCpzrQFTMKcqFKk02l:10.00:1
        baseID: 38ttpCpzrQFTMKcqFKk02l
        passPercentage: 10
        conditions:
          - type: user_id
            targetValue:
              - 35sClJFs8l0y5uRQhDwUDo
            operator: any
        environments:
          - staging
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