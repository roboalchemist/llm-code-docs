# Source: https://docs.statsig.com/api-reference/dynamic-configs/get-dynamic-config-rules.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Dynamic Config Rules



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/dynamic_configs/{id}/rules
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
  /console/v1/dynamic_configs/{id}/rules:
    get:
      tags:
        - Dynamic Configs
      summary: Get Dynamic Config Rules
      parameters:
        - name: id
          required: true
          in: path
          description: id
          schema:
            type: string
      responses:
        '200':
          description: Get Dynamic Config Rules Response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/DynamicConfigRulesDto'
                example:
                  message: Dynamic Config rules read successfully.
                  data:
                    - rules:
                        - id: 5pjzfmF8KLFsh81kBPyxvR
                          baseID: 5pjzfmF8KLFsh81kBPyxvR
                          name: rule name
                          passPercentage: 1
                          conditions:
                            - type: browser_name
                              targetValue: []
                              operator: any
                          environments: null
                          completedAutomatedRollouts: []
                          pendingAutomatedRollouts: []
                        - id: 6jQEnu1fCnXqjXhm1qGEnt
                          baseID: 6jQEnu1fCnXqjXhm1qGEnt
                          name: Other2
                          passPercentage: 80
                          conditions: []
                          environments: null
                          completedAutomatedRollouts: []
                          pendingAutomatedRollouts: []
                        - id: 4DonExIcOjSV8kG3WSQ5Zm
                          baseID: 4DonExIcOjSV8kG3WSQ5Zm
                          name: Austin's fav rule
                          passPercentage: 8
                          conditions: []
                          environments: null
                          completedAutomatedRollouts: []
                          pendingAutomatedRollouts: []
                  pagination:
                    itemsPerPage: 20000
                    pageNumber: 1
                    totalItems: 1
                    nextPage: null
                    previousPage: null
                    all: ''
              example:
                message: Dynamic Config rules read successfully.
                data:
                  - rules:
                      - id: 5pjzfmF8KLFsh81kBPyxvR
                        baseID: 5pjzfmF8KLFsh81kBPyxvR
                        name: rule name
                        passPercentage: 1
                        conditions:
                          - type: browser_name
                            targetValue: []
                            operator: any
                        environments: null
                        completedAutomatedRollouts: []
                        pendingAutomatedRollouts: []
                      - id: 6jQEnu1fCnXqjXhm1qGEnt
                        baseID: 6jQEnu1fCnXqjXhm1qGEnt
                        name: Other2
                        passPercentage: 80
                        conditions: []
                        environments: null
                        completedAutomatedRollouts: []
                        pendingAutomatedRollouts: []
                      - id: 4DonExIcOjSV8kG3WSQ5Zm
                        baseID: 4DonExIcOjSV8kG3WSQ5Zm
                        name: Austin's fav rule
                        passPercentage: 8
                        conditions: []
                        environments: null
                        completedAutomatedRollouts: []
                        pendingAutomatedRollouts: []
                pagination:
                  itemsPerPage: 20000
                  pageNumber: 1
                  totalItems: 1
                  nextPage: null
                  previousPage: null
                  all: ''
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    PaginationResponseWithMessage:
      type: object
      properties:
        message:
          type: string
          description: A simple string explaining the result of the operation.
        data:
          description: Array of results returned by pagination limit.
          type: array
          items:
            type: object
        pagination:
          description: Pagination metadata for checking if there is next page for example.
          allOf:
            - $ref: '#/components/schemas/PaginationResponseMetadataDto'
      required:
        - message
        - data
        - pagination
    DynamicConfigRulesDto:
      type: object
      properties:
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
      required:
        - rules
    PaginationResponseMetadataDto:
      type: object
      properties:
        itemsPerPage:
          type: number
          format: double
        pageNumber:
          type: number
          format: double
        nextPage:
          type: string
          nullable: true
        previousPage:
          type: string
          nullable: true
        totalItems:
          type: number
          format: double
        all:
          type: string
      required:
        - itemsPerPage
        - pageNumber
        - nextPage
        - previousPage
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).