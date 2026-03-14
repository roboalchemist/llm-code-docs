# Source: https://docs.statsig.com/api-reference/segments/list-segments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Segments



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/segments
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
  /console/v1/segments:
    get:
      tags:
        - Segments
      summary: List Segments
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
          description: List Segments Success
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/SegmentDto'
                example:
                  message: Segments listed successfully.
                  data:
                    - id: an_id_list
                      isEnabled: true
                      description: helpful summary of what this segment is
                      lastModifierName: CONSOLE API
                      lastModifierID: ahKwUoaNauHu9AmJPc2
                      type: id_list
                      count: 0
                      tags:
                        - a tag
                    - id: a_rule_based_segment
                      isEnabled: true
                      description: helpful summary of what this segment is
                      lastModifierName: CONSOLE API
                      lastModifierID: ahKwUoaNauHu9AmJPc2
                      type: rule_based
                      count: 0
                      rules:
                        name: All Conditions
                        passPercentage: 10
                        conditions:
                          - type: public
                            operator: string
                            targetValue: 0
                            field: string
                            customID: string
                        returnValue:
                          key: true
                      tags:
                        - a tag
              example:
                message: Segments listed successfully.
                data:
                  - id: an_id_list
                    isEnabled: true
                    description: helpful summary of what this segment is
                    lastModifierName: CONSOLE API
                    lastModifierID: ahKwUoaNauHu9AmJPc2
                    type: id_list
                    count: 0
                    tags:
                      - a tag
                  - id: a_rule_based_segment
                    isEnabled: true
                    description: helpful summary of what this segment is
                    lastModifierName: CONSOLE API
                    lastModifierID: ahKwUoaNauHu9AmJPc2
                    type: rule_based
                    count: 0
                    rules:
                      name: All Conditions
                      passPercentage: 10
                      conditions:
                        - type: public
                          operator: string
                          targetValue: 0
                          field: string
                          customID: string
                      returnValue:
                        key: true
                    tags:
                      - a tag
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