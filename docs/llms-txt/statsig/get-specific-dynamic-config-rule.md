# Source: https://docs.statsig.com/api-reference/dynamic-configs/get-specific-dynamic-config-rule.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Specific Dynamic Config Rule



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/dynamic_configs/{id}/rule/{ruleId}
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
  /console/v1/dynamic_configs/{id}/rule/{ruleId}:
    get:
      tags:
        - Dynamic Configs
      summary: Get Specific Dynamic Config Rule
      parameters:
        - name: id
          required: true
          in: path
          description: Dynamic Config ID
          schema:
            type: string
        - name: ruleId
          required: true
          in: path
          description: Rule ID
          schema:
            type: string
      responses:
        '200':
          description: Get Specific Dynamic Config Rule Response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/DynamicConfigRuleDto'
                example:
                  message: Dynamic Config rules read successfully.
                  data:
                    id: 6jQEnu1fCnXqjXhm1qGEnt
                    baseID: 6jQEnu1fCnXqjXhm1qGEnt
                    name: Other2
                    passPercentage: 80
                    conditions: []
                    environments: null
                    completedAutomatedRollouts: []
                    pendingAutomatedRollouts: []
              example:
                message: Dynamic Config rules read successfully.
                data:
                  id: 6jQEnu1fCnXqjXhm1qGEnt
                  baseID: 6jQEnu1fCnXqjXhm1qGEnt
                  name: Other2
                  passPercentage: 80
                  conditions: []
                  environments: null
                  completedAutomatedRollouts: []
                  pendingAutomatedRollouts: []
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
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
    DynamicConfigRuleDto:
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
      required:
        - name
        - passPercentage
        - conditions
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).