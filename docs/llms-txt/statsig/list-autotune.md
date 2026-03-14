# Source: https://docs.statsig.com/api-reference/autotunes/list-autotune.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Autotune



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/autotunes
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
  /console/v1/autotunes:
    get:
      tags:
        - Autotunes
      summary: List Autotune
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
          description: Autotune Experiments listed successfully.
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/AutotuneExperimentDto'
                example:
                  message: Autotune Experiments listed successfully.
                  data:
                    - id: test_autotune_exp
                      name: test_autotune_exp
                      description: dsdsdsd test
                      idType: userID
                      lastModifierID: 24hiIXz1maFaDwtYEetv2i
                      lastModifiedTime: 1716324033128
                      lastModifierName: jairo Garciga
                      lastModifierEmail: jairo@statsig.com
                      creatorID: 5sgBiiuoBX4fscrWdCXVma
                      createdTime: 1688072516890
                      creatorName: Samuel Kitono
                      creatorEmail: samuel@statsig.com
                      targetApps: []
                      holdoutIDs: []
                      tags: []
                      team: null
                      isStarted: false
                      inlineTargetingRulesJSON: '{}'
                      inlineTargetingRules: []
                      variants:
                        - name: test_12
                          id: 7eOW6aXU7F07KxrggOrAdy
                          json:
                            user:
                              id: 12345
                              name: Jane Doe
                              email: jane.doe@example.com
                              isActive: true
                              roles:
                                - admin
                                - editor
                                - subscriber
                            posts:
                              - id: 1
                                title: Introduction to JSON5
                                content: >-
                                  JSON5 is a superset of JSON that aims to be
                                  easier for humans to write and maintain.
                                tags:
                                  - json5
                                  - json
                                  - javascript
                                comments:
                                  - id: 101
                                    author: John Smith
                                    content: Great post! Very informative.
                                    likes: 5
                                  - id: 102
                                    author: Alice Johnson
                                    content: I found this very helpful. Thanks!
                                    likes: 3
                              - id: 2
                                title: Advanced JSON5 Features
                                content: >-
                                  Explore the advanced features of JSON5,
                                  including comments, trailing commas, and more.
                                tags:
                                  - json5
                                  - advanced
                                  - features
                                comments:
                                  - id: 201
                                    author: Bob Brown
                                    content: >-
                                      I didn't know JSON5 could do this.
                                      Amazing!
                                    likes: 8
                            settings:
                              theme: dark
                              notificationsEnabled: true
                              language: en-US
                              layout:
                                header: true
                                footer: true
                                sidebar: collapsed
                            metadata:
                              version: 1.0.0
                              author: Jane Doe
                              lastUpdated: '2024-05-21T10:00:00Z'
                        - name: var1
                          id: 7eOW6cCWzX9C3WZbRWndwA
                          json: {}
                        - name: control
                          id: 7GVLLJOBETDYXLn00FXFuQ
                          json: {}
                      successEvent: add_to_cart
                      successEventValue: ''
                      explorationWindow: 24hrs
                      attributionWindow: 2hrs
                      winnerThreshold: 95%
                      winner: null
                  pagination:
                    itemsPerPage: 100
                    pageNumber: 1
                    totalItems: 1
                    nextPage: null
                    previousPage: null
                    all: /console/v1/autotunes
              example:
                message: Autotune Experiments listed successfully.
                data:
                  - id: test_autotune_exp
                    name: test_autotune_exp
                    description: dsdsdsd test
                    idType: userID
                    lastModifierID: 24hiIXz1maFaDwtYEetv2i
                    lastModifiedTime: 1716324033128
                    lastModifierName: jairo Garciga
                    lastModifierEmail: jairo@statsig.com
                    creatorID: 5sgBiiuoBX4fscrWdCXVma
                    createdTime: 1688072516890
                    creatorName: Samuel Kitono
                    creatorEmail: samuel@statsig.com
                    targetApps: []
                    holdoutIDs: []
                    tags: []
                    team: null
                    isStarted: false
                    inlineTargetingRulesJSON: '{}'
                    inlineTargetingRules: []
                    variants:
                      - name: test_12
                        id: 7eOW6aXU7F07KxrggOrAdy
                        json:
                          user:
                            id: 12345
                            name: Jane Doe
                            email: jane.doe@example.com
                            isActive: true
                            roles:
                              - admin
                              - editor
                              - subscriber
                          posts:
                            - id: 1
                              title: Introduction to JSON5
                              content: >-
                                JSON5 is a superset of JSON that aims to be
                                easier for humans to write and maintain.
                              tags:
                                - json5
                                - json
                                - javascript
                              comments:
                                - id: 101
                                  author: John Smith
                                  content: Great post! Very informative.
                                  likes: 5
                                - id: 102
                                  author: Alice Johnson
                                  content: I found this very helpful. Thanks!
                                  likes: 3
                            - id: 2
                              title: Advanced JSON5 Features
                              content: >-
                                Explore the advanced features of JSON5,
                                including comments, trailing commas, and more.
                              tags:
                                - json5
                                - advanced
                                - features
                              comments:
                                - id: 201
                                  author: Bob Brown
                                  content: I didn't know JSON5 could do this. Amazing!
                                  likes: 8
                          settings:
                            theme: dark
                            notificationsEnabled: true
                            language: en-US
                            layout:
                              header: true
                              footer: true
                              sidebar: collapsed
                          metadata:
                            version: 1.0.0
                            author: Jane Doe
                            lastUpdated: '2024-05-21T10:00:00Z'
                      - name: var1
                        id: 7eOW6cCWzX9C3WZbRWndwA
                        json: {}
                      - name: control
                        id: 7GVLLJOBETDYXLn00FXFuQ
                        json: {}
                    successEvent: add_to_cart
                    successEventValue: ''
                    explorationWindow: 24hrs
                    attributionWindow: 2hrs
                    winnerThreshold: 95%
                    winner: null
                pagination:
                  itemsPerPage: 100
                  pageNumber: 1
                  totalItems: 1
                  nextPage: null
                  previousPage: null
                  all: /console/v1/autotunes
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
    AutotuneExperimentDto:
      type: object
      properties:
        description:
          type: string
          description: Detailed description of the configuration’s purpose.
        variants:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                description: Variant name
              json:
                description: Variant JSON data
              size:
                type: number
                description: Variant size
              id:
                type: string
                description: >-
                  The name that was originally given to the autotune on creation
                  but formatted as an ID ("A Autotune" -> "a_autotune").
            required:
              - name
              - json
              - id
        successEvent:
          type: string
          description: The event you are trying to optimize for.
        successEventValue:
          type: string
          description: >-
            The value that should come with the event for it to be considered
            successful.
        explorationWindow:
          type: string
          enum:
            - 1hr
            - 24hr
            - 48hr
            - 168hr
            - 336hr
            - '1'
            - '24'
            - '48'
            - '168'
            - '336'
            - 1hrs
            - 24hrs
            - 48hrs
            - 168hrs
            - 336hrs
          description: >-
            The initial time period where Autotune will equally split the
            traffic.
        attributionWindow:
          type: string
          enum:
            - 1hr
            - 2hr
            - 4hr
            - 24hr
            - 1hrs
            - 2hrs
            - 4hrs
            - 24hrs
            - '1'
            - '2'
            - '4'
            - '24'
          description: >-
            The maximum duration between the exposure and success event that
            counts as a success.
        attributionWindowUnit:
          type: string
          enum:
            - min
            - hour
            - day
          description: Time unit of attribution window
        explorationWindowRate:
          type: number
          minimum: 0.001
          maximum: 1
          description: Exploration window rate
          format: double
        longtermExplorationAllocation:
          type: number
          minimum: 0.001
          maximum: 1
          description: Long term exploration allocation
          format: double
        winnerThreshold:
          type: string
          enum:
            - 80%
            - 90%
            - 95%
            - 98%
            - 99%
          description: >-
            The "probability of best" threshold a variant needs to achieve for
            Autotune to declare it the winner, stop collecting data, and direct
            all traffic.
        metadataField:
          type: string
          description: >-
            Metadata field containing the numeric value to optimize for. If this
            field is null, autotune optimizes for the existence of a follow-up
            event. This is only used for contextual autotunes.
        higherIsBetter:
          type: boolean
          description: >-
            Whether to optimize for an increase or decrease in the metadata
            field value. Default is true. This is only used for contextual
            autotunes.
        isContextual:
          type: boolean
          description: Whether this is a contextual autotune
        metricSourceID:
          type: string
          description: Metric source to pull success event data from
        linkedExperimentName:
          type: string
          description: Linked experiment to measure the success of the Autotune
        goalRichText:
          type: string
          description: Autotune goal
        optimizationParameter:
          type: string
          enum:
            - occurrence
            - value
          description: Optimize for event occurrence vs value
        valueColumn:
          type: string
          description: Metric source column to optimize for
        featureList:
          type: array
          items:
            type: string
          description: List of features that should be included in the analysis
        inlineTargetingRulesJSON:
          type: string
          nullable: true
          description: A raw JSON string of the inline targeting rules
        inlineTargetingRules:
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
          description: A formatted array of the inline targeting rules
        id:
          type: string
          description: ID
        name:
          type: string
          description: Optional name for the configuration.
        idType:
          type: string
          description: Type of ID
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
        tags:
          type: array
          items:
            type: string
          description: Optional tags for categorization.
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
        isStarted:
          type: boolean
          description: Is the autotune experiment currently running.
        winner:
          type: object
          properties:
            id:
              type: string
              description: The Statsig UserID of the last modifier of this autotune.
            name:
              type: string
              description: The Statsig Username of the last modifier of this autotune.
          required:
            - id
            - name
          nullable: true
      required:
        - description
        - variants
        - successEvent
        - successEventValue
        - explorationWindow
        - attributionWindow
        - winnerThreshold
        - id
        - idType
        - lastModifierID
        - lastModifiedTime
        - lastModifierEmail
        - lastModifierName
        - creatorID
        - createdTime
        - creatorName
        - creatorEmail
        - isStarted
        - winner
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