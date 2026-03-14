# Source: https://docs.statsig.com/api-reference/dynamic-configs/unarchive-dynamic-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Unarchive Dynamic Config



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json put /console/v1/dynamic_configs/{id}/unarchive
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
  /console/v1/dynamic_configs/{id}/unarchive:
    put:
      tags:
        - Dynamic Configs
      summary: Unarchive Dynamic Config
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
              $ref: '#/components/schemas/UnarchiveSchemaDto'
      responses:
        '200':
          description: Unarchive Dynamic Config Response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/DynamicConfigDto'
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    UnarchiveSchemaDto:
      type: object
      properties:
        unarchiveReason:
          type: string
          description: The reason for unarchiving the gate
          example: The gate is needed again
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
    DynamicConfigDto:
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
          description: Optional name for the configuration.
          example: my_config
        idType:
          type: string
          description: The type of ID which the dynamic config is based on.
          example: userID
        description:
          type: string
          maxLength: 1000
          description: A brief summary of what the dynamic config is being used for
          example: helpful summary of what this dynamic config does
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
          description: The list of tag names attached to the dynamic config
          example:
            - a tag
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
          description: The team name associated with the dynamic config, Enterprise only.
        teamID:
          type: string
          nullable: true
          description: The team ID associated with the dynamic config, Enterprise only.
        version:
          type: number
          description: Version number
          format: double
        isEnabled:
          type: boolean
          description: Is the dynamic config enabled
          default: true
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
              returnValueJson5:
                type: string
              variants:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                    name:
                      type: string
                    passPercentage:
                      type: number
                      minimum: 0
                      maximum: 100
                      multipleOf: 0.01
                    returnValue:
                      type: object
                      additionalProperties: {}
                    returnValueJson5:
                      type: string
                  required:
                    - name
                    - passPercentage
            required:
              - name
              - passPercentage
              - conditions
          description: An array of Rule objects
        defaultValue:
          type: object
          additionalProperties: {}
          description: The fallback JSON object when no rules are triggered
        defaultValueJson5:
          type: string
          description: >-
            Can include comments. If provided with defaultValue, must parse to
            the same JSON
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
        schema:
          type: string
          nullable: true
          description: >-
            A schema using JSON Schema Draft 2020-12 to enforce return values of
            this dynamic config's rules.
        schemaJson5:
          type: string
          nullable: true
          description: >-
            `schema` except with Json5 comments. Optional and should parse to
            same json as `schema`.
        releasePipelineID:
          type: string
          nullable: true
          description: The release pipeline ID associated with the dynamic config
        isTemplate:
          type: boolean
        status:
          type: string
          enum:
            - Enabled
            - Disabled
            - Archived
        checksPerHour:
          type: number
          nullable: true
          format: double
      required:
        - id
        - description
        - lastModifierID
        - lastModifiedTime
        - lastModifierEmail
        - lastModifierName
        - createdTime
        - creatorName
        - isEnabled
        - rules
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).