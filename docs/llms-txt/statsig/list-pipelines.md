# Source: https://docs.statsig.com/api-reference/release-pipelines/list-pipelines.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Pipelines



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/release_pipelines
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
  /console/v1/release_pipelines:
    get:
      tags:
        - Release Pipelines
      summary: List Pipelines
      parameters:
        - name: limit
          required: false
          in: query
          description: Results per page
          schema:
            example: 10
            oneOf:
              - type: string
              - type: number
            type: integer
        - name: page
          required: false
          in: query
          description: Page number
          schema:
            example: 1
            oneOf:
              - type: string
              - type: number
            type: integer
      responses:
        '200':
          description: List pipelines
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/ReleasePipelineDto'
                example:
                  message: List pipelines success
                  data:
                    - id: 45aiIXz4aaAadWtYEetjko
                      name: Pipeline 1
                      creatorID: 24hiIXz3kbFaDwtYEetv2i
                      createdTime: 1705439406615
                      lastModifierID: 24hiIXz3kbFaDwtYEetv2i
                      lastModifiedTime: 1705439406615
                      phases:
                        - id: 24hiIXz3kbFaDwtYEetv2i
                          name: Phase 1
                          timeIntervalMs: 3600000
                          requiredReview: false
                          rules:
                            - id: 24hiIXz3kbFaDwtYEetv2i
                              name: Rule
                              conditions:
                                - type: app_version
                                  targetValue:
                                    - '1'
                                    - '222'
                                  operator: any
                              environments: null
                    - id: 24hiIXz3kbFaDwtYEetv2i
                      name: Pipeline 2
                      creatorID: 24hiIXz3kbFaDwtYEetv2i
                      createdTime: 1705439406615
                      lastModifierID: 24hiIXz3kbFaDwtYEetv2i
                      lastModifiedTime: 1705439406615
                      phases:
                        - id: 24hiIXz3kbFaDwtYEetv2i
                          name: Phase 1
                          timeIntervalMs: 3600000
                          requiredReview: false
                          rules:
                            - id: 24hiIXz3kbFaDwtYEetv2i
                              name: Rule
                              conditions:
                                - type: app_version
                                  targetValue:
                                    - '1'
                                    - '222'
                                  operator: any
                              environments: null
              example:
                message: List pipelines success
                data:
                  - id: 45aiIXz4aaAadWtYEetjko
                    name: Pipeline 1
                    creatorID: 24hiIXz3kbFaDwtYEetv2i
                    createdTime: 1705439406615
                    lastModifierID: 24hiIXz3kbFaDwtYEetv2i
                    lastModifiedTime: 1705439406615
                    phases:
                      - id: 24hiIXz3kbFaDwtYEetv2i
                        name: Phase 1
                        timeIntervalMs: 3600000
                        requiredReview: false
                        rules:
                          - id: 24hiIXz3kbFaDwtYEetv2i
                            name: Rule
                            conditions:
                              - type: app_version
                                targetValue:
                                  - '1'
                                  - '222'
                                operator: any
                            environments: null
                  - id: 24hiIXz3kbFaDwtYEetv2i
                    name: Pipeline 2
                    creatorID: 24hiIXz3kbFaDwtYEetv2i
                    createdTime: 1705439406615
                    lastModifierID: 24hiIXz3kbFaDwtYEetv2i
                    lastModifiedTime: 1705439406615
                    phases:
                      - id: 24hiIXz3kbFaDwtYEetv2i
                        name: Phase 1
                        timeIntervalMs: 3600000
                        requiredReview: false
                        rules:
                          - id: 24hiIXz3kbFaDwtYEetv2i
                            name: Rule
                            conditions:
                              - type: app_version
                                targetValue:
                                  - '1'
                                  - '222'
                                operator: any
                            environments: null
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
    ReleasePipelineDto:
      type: object
      properties:
        id:
          type: string
          description: Pipeline ID
        name:
          type: string
          description: Pipeline Name
        creatorID:
          type: string
          description: Pipeline Creator ID
        createdTime:
          type: number
          description: Pipeline Creation Time
          format: double
        lastModifierID:
          type: string
          description: Last Modifier ID
        lastModifiedTime:
          type: number
          description: Last Modification Time
          format: double
        phases:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
                description: Phase ID
              name:
                type: string
                description: Phase Name
              timeIntervalMs:
                type: number
                description: Time interval in milliseconds for this phase
              requiredReview:
                type: boolean
                description: Whether this phase requires review to proceed
              rules:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      description: The Statsig ID of this rule.
                    name:
                      type: string
                      description: The name of this rule.
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
                  required:
                    - name
                    - conditions
                description: Rules to apply in this phase
            required:
              - name
              - timeIntervalMs
              - requiredReview
              - rules
          description: Phases of the release pipeline that will be executed in order.
        triggerNotice:
          type: string
          description: >-
            A notice that will be displayed to the user on the config page when
            the release pipeline is triggered
      required:
        - id
        - name
        - creatorID
        - createdTime
        - lastModifierID
        - lastModifiedTime
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