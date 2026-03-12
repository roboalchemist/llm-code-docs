# Source: https://docs.statsig.com/api-reference/segments/update-segment-rules.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Segment Rules



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/segments/{id}/conditional
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
  /console/v1/segments/{id}/conditional:
    post:
      tags:
        - Segments
      summary: Update Segment Rules
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
              $ref: '#/components/schemas/SegmentRulesDto'
      responses:
        '200':
          description: Rules Successfully Updated
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/SegmentDto'
                example:
                  message: Rules successfully updated
              example:
                message: Rules successfully updated
        '400':
          description: Segment must be of type 'rule_based' to be modified on this endpoint
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: integer
                    enum:
                      - 400
                  message:
                    type: string
                required:
                  - status
                  - message
              examples:
                Invalid Request:
                  value:
                    status: 400
                    message: >-
                      Invalid request. Please check the request input and try
                      again.
        '401':
          description: >-
            This endpoint only accepts an active CONSOLE key, but an invalid key
            was sent. Key: console-xxxXXXxxxXXXxxx
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: integer
                    enum:
                      - 401
                  message:
                    type: string
                required:
                  - status
                  - message
              examples:
                Invalid Endpoint:
                  value:
                    status: 401
                    message: >-
                      This endpoint only accepts an active CONSOLE key, but an
                      invalid key was sent. Key: console-xxxXXXxxxXXXxxx
        '404':
          description: Segment not found.
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: integer
                    enum:
                      - 404
                  message:
                    type: string
                required:
                  - status
                  - message
              examples:
                Not Found:
                  value:
                    status: 404
                    message: Not Found. The requested resource could not be found.
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    SegmentRulesDto:
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
              Of the users that meet the conditions of this rule, what percent
              should return true.
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
                    - fails_segment
                    - ip_address
                    - os_name
                    - os_version
                    - passes_segment
                    - unit_id
                    - user_id
              required:
                - type
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
    SegmentDto:
      type: object
      properties:
        isEnabled:
          type: boolean
          description: Is the segment enabled.
        type:
          type: string
          enum:
            - id_list
            - rule_based
            - analysis_list
            - user_store_id_list
        count:
          type: number
          description: 'For id_list segments: the length of the ID list'
          format: double
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
            required:
              - name
              - passPercentage
              - conditions
          description: Rule Object
        tags:
          type: array
          items:
            type: string
          description: Optional tags for categorization.
        id:
          type: string
          description: ID
        name:
          type: string
          description: Optional name for the configuration.
        idType:
          type: string
          description: Type of ID
        description:
          type: string
          description: Detailed description of the configuration’s purpose.
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
          description: ID of the user who created the entity.
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
          description: Email of the creator.
        targetApps:
          type: array
          items:
            type: string
          description: List of target applications associated with this configuration.
        holdoutIDs:
          type: array
          items:
            type: string
          description: Holdouts applied to this configuration.
        team:
          type: string
          nullable: true
          description: Optional name for the responsible team.
        teamID:
          type: string
          nullable: true
          description: Optional ID of the responsible team.
        version:
          type: number
          description: Version number
          format: double
      required:
        - isEnabled
        - type
        - id
        - idType
        - description
        - lastModifierID
        - lastModifiedTime
        - lastModifierEmail
        - lastModifierName
        - creatorID
        - createdTime
        - creatorName
        - creatorEmail
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).