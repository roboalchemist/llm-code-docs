# Source: https://docs.statsig.com/api-reference/gates/list-gates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Gates



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/gates
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
  /console/v1/gates:
    get:
      tags:
        - Gates
      summary: List Gates
      parameters:
        - name: idType
          required: false
          in: query
          description: Filter by idType
          examples:
            single id type:
              value: userID
            multiple id types:
              value:
                - userID
                - stableID
          schema:
            oneOf:
              - type: string
              - type: array
                items:
                  type: string
        - name: type
          required: false
          in: query
          description: Filter by type
          schema:
            type: string
            enum:
              - TEMPORARY
              - PERMANENT
              - STALE
              - TEMPLATE
        - name: typeReason
          required: false
          in: query
          description: Filter by typeReason
          schema:
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
        - name: passRate
          required: false
          in: query
          description: >-
            Filter by pass rate of the gates, as determined by a sampling of
            overall true/false values returned: 0, 100, or INBETWEEN (pass rate
            greater than zero but less than 100)
          schema:
            oneOf:
              - type: string
                enum:
                  - '0'
                  - '100'
                  - INBETWEEN
              - type: array
                items:
                  type: string
                  enum:
                    - '0'
                    - '100'
                    - INBETWEEN
        - name: rolloutRate
          required: false
          in: query
          description: >-
            Filter by rollout rate of the gates: 0 (all rules are set to pass
            0%), 100 (all rules pass 100% including an "everyone" catch all
            rule), or INBETWEEN (at least one rule has a pass rate greater than
            0 but less than 100)
          schema:
            oneOf:
              - type: string
                enum:
                  - '0'
                  - '100'
                  - INBETWEEN
              - type: array
                items:
                  type: string
                  enum:
                    - '0'
                    - '100'
                    - INBETWEEN
        - name: releasePipelineID
          required: false
          in: query
          description: Filter by release pipeline ID
          schema:
            type: string
            nullable: true
        - name: includeArchived
          required: false
          in: query
          description: Include archived gates in the response
          schema:
            type: string
            enum:
              - 'true'
              - 'false'
        - name: store0100Exposures
          required: false
          in: query
          description: Filter gates by whether "Store 0/100 Exposures" is enabled.
          schema:
            type: string
            enum:
              - 'true'
              - 'false'
        - name: creatorName
          required: false
          in: query
          description: Name of the creator.
          schema:
            type: string
            nullable: true
        - name: creatorID
          required: false
          in: query
          description: ID of the user who created the entity.
          schema:
            type: string
            nullable: true
        - name: tags
          required: false
          in: query
          description: Filter by tags
          examples:
            single tag:
              value: tag1
            multiple tags:
              value:
                - tag1
                - tag2
          schema:
            oneOf:
              - type: string
              - type: array
                items:
                  type: string
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
          description: List gates success
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/ExternalGateDto'
                example:
                  message: Gates listed successfully.
                  data:
                    - id: a_gate
                      name: A Gate
                      description: description
                      idType: userID
                      lastModifierID: 4R5PV7mvYdW6NLCwK8ocoz
                      lastModifiedTime: 1705439406750
                      lastModifierName: CONSOLE API
                      lastModifierEmail: null
                      creatorID: 4R5PV7mvYdW6NLCwK8ocoz
                      createdTime: 1705439406615
                      creatorName: CONSOLE API
                      creatorEmail: null
                      targetApps: []
                      holdoutIDs: []
                      tags: []
                      isEnabled: true
                      status: In Progress
                      rules: []
                      checksPerHour: 0
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
                      version: 1
                  pagination:
                    all: ''
                    itemsPerPage: 100
                    nextPage: null
                    pageNumber: 1
                    previousPage: null
                    totalItems: 1
              example:
                message: Gates listed successfully.
                data:
                  - id: a_gate
                    name: A Gate
                    description: description
                    idType: userID
                    lastModifierID: 4R5PV7mvYdW6NLCwK8ocoz
                    lastModifiedTime: 1705439406750
                    lastModifierName: CONSOLE API
                    lastModifierEmail: null
                    creatorID: 4R5PV7mvYdW6NLCwK8ocoz
                    createdTime: 1705439406615
                    creatorName: CONSOLE API
                    creatorEmail: null
                    targetApps: []
                    holdoutIDs: []
                    tags: []
                    isEnabled: true
                    status: In Progress
                    rules: []
                    checksPerHour: 0
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
                    version: 1
                pagination:
                  all: ''
                  itemsPerPage: 100
                  nextPage: null
                  pageNumber: 1
                  previousPage: null
                  totalItems: 1
        '403':
          description: Forbidden resource
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: number
                    enum:
                      - 403
                  message:
                    type: string
                    enum:
                      - Forbidden resource
                required:
                  - status
                  - message
              examples:
                Forbidden resource:
                  value:
                    status: 403
                    message: Forbidden resource
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