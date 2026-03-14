# Source: https://docs.statsig.com/api-reference/holdouts/list-holdouts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Holdouts



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/holdouts
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
  /console/v1/holdouts:
    get:
      tags:
        - Holdouts
      summary: List Holdouts
      parameters:
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
          description: List holdouts response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/HoldoutDto'
                example:
                  message: Holdouts listed successfully.
                  data:
                    - id: testing_holdout
                      name: testing holdout
                      description: helpful summary of what this holdout does
                      idType: userID
                      lastModifierID: 4dcQUIpS8PHObBGD7HJwOx
                      lastModifiedTime: 1719873874212
                      lastModifierName: CONSOLE API
                      lastModifierEmail: null
                      creatorID: 4dcQUIpS8PHObBGD7HJwOx
                      createdTime: 1719873870785
                      creatorName: CONSOLE API
                      creatorEmail: null
                      targetApps: []
                      tags: []
                      team: Console Team
                      isEnabled: true
                      isGlobal: false
                      passPercentage: 0
                      gateIDs: []
                      experimentIDs: []
                      layerIDs: []
                      targetingGateID: null
                    - id: test123
                      name: test123
                      description: ''
                      idType: userID
                      lastModifierID: 5O908pyGoCqw6QH1nt8v82
                      lastModifiedTime: 1719872028057
                      lastModifierName: test
                      lastModifierEmail: user@statsig.com
                      creatorID: 5O908pyGoCqw6QH1nt8v82
                      createdTime: 1719872027567
                      creatorName: Test User
                      creatorEmail: test@statsig.com
                      targetApps: []
                      tags: []
                      team: Console Team
                      isEnabled: true
                      isGlobal: false
                      passPercentage: 0
                      gateIDs: []
                      experimentIDs: []
                      layerIDs: []
                      targetingGateID: null
                    - id: test_target_gate
                      name: test_target_gate
                      description: test holdout
                      idType: userID
                      lastModifierID: 4dcQUIpS8PHObBGD7HJwOx
                      lastModifiedTime: 1710521134863
                      lastModifierName: CONSOLE API
                      lastModifierEmail: null
                      creatorID: 5sgBiiuoBX4fscrWdCXVma
                      createdTime: 1702237002465
                      creatorName: Test User
                      creatorEmail: test@statsig.com
                      targetApps: []
                      tags: []
                      team: null
                      isEnabled: true
                      isGlobal: false
                      passPercentage: 1
                      gateIDs:
                        - product_larger_image
                        - product_larger_image_lower
                        - test_new_gate
                        - ma_test_rollout
                        - empty_gate
                        - new_gate_to_point_experiment_at
                        - new_gate_with_monitoring_metrics
                        - andy_test_gate
                      experimentIDs:
                        - mostly_test_experiment
                        - test_123
                        - new_test_exp
                        - test_exp_start
                        - andy_test_experiment
                      layerIDs:
                        - Homepage Feed Improvements
                        - statsig_is_awesome
                        - testing_tool
                        - test_statsig_2
                        - layer_holdout_parameters
                      targetingGateID: ''
                  pagination:
                    itemsPerPage: 20000
                    pageNumber: 1
                    totalItems: 3
                    nextPage: null
                    previousPage: null
                    all: /console/v1/holdouts
              example:
                message: Holdouts listed successfully.
                data:
                  - id: testing_holdout
                    name: testing holdout
                    description: helpful summary of what this holdout does
                    idType: userID
                    lastModifierID: 4dcQUIpS8PHObBGD7HJwOx
                    lastModifiedTime: 1719873874212
                    lastModifierName: CONSOLE API
                    lastModifierEmail: null
                    creatorID: 4dcQUIpS8PHObBGD7HJwOx
                    createdTime: 1719873870785
                    creatorName: CONSOLE API
                    creatorEmail: null
                    targetApps: []
                    tags: []
                    team: Console Team
                    isEnabled: true
                    isGlobal: false
                    passPercentage: 0
                    gateIDs: []
                    experimentIDs: []
                    layerIDs: []
                    targetingGateID: null
                  - id: test123
                    name: test123
                    description: ''
                    idType: userID
                    lastModifierID: 5O908pyGoCqw6QH1nt8v82
                    lastModifiedTime: 1719872028057
                    lastModifierName: test
                    lastModifierEmail: user@statsig.com
                    creatorID: 5O908pyGoCqw6QH1nt8v82
                    createdTime: 1719872027567
                    creatorName: Test User
                    creatorEmail: test@statsig.com
                    targetApps: []
                    tags: []
                    team: Console Team
                    isEnabled: true
                    isGlobal: false
                    passPercentage: 0
                    gateIDs: []
                    experimentIDs: []
                    layerIDs: []
                    targetingGateID: null
                  - id: test_target_gate
                    name: test_target_gate
                    description: test holdout
                    idType: userID
                    lastModifierID: 4dcQUIpS8PHObBGD7HJwOx
                    lastModifiedTime: 1710521134863
                    lastModifierName: CONSOLE API
                    lastModifierEmail: null
                    creatorID: 5sgBiiuoBX4fscrWdCXVma
                    createdTime: 1702237002465
                    creatorName: Test User
                    creatorEmail: test@statsig.com
                    targetApps: []
                    tags: []
                    team: null
                    isEnabled: true
                    isGlobal: false
                    passPercentage: 1
                    gateIDs:
                      - product_larger_image
                      - product_larger_image_lower
                      - test_new_gate
                      - ma_test_rollout
                      - empty_gate
                      - new_gate_to_point_experiment_at
                      - new_gate_with_monitoring_metrics
                      - andy_test_gate
                    experimentIDs:
                      - mostly_test_experiment
                      - test_123
                      - new_test_exp
                      - test_exp_start
                      - andy_test_experiment
                    layerIDs:
                      - Homepage Feed Improvements
                      - statsig_is_awesome
                      - testing_tool
                      - test_statsig_2
                      - layer_holdout_parameters
                    targetingGateID: ''
                pagination:
                  itemsPerPage: 20000
                  pageNumber: 1
                  totalItems: 3
                  nextPage: null
                  previousPage: null
                  all: /console/v1/holdouts
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
    HoldoutDto:
      type: object
      properties:
        id:
          type: string
          description: ID
        name:
          type: string
          description: Optional name for the configuration.
        idType:
          type: string
          description: type of id
        description:
          type: string
          maxLength: 1000
          example: example holdout description
          description: brief summary of what the holdout is being used for
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
        isEnabled:
          type: boolean
          example: true
          description: enable or disable the holdout
        passPercentage:
          type: number
          minimum: 0
          maximum: 10
          example: 5
          description: percentage of users between 0-10% to pass through the holdout
          format: double
        gateIDs:
          type: array
          items:
            type: string
          example:
            - 4pjeXYDjC2WinSgOiII7wh
          description: an array of gateIDs which this holdout is applied to
        experimentIDs:
          type: array
          items:
            type: string
          example:
            - 70fCNphHGesdLwHdHau99q
          description: an array of experimentIDs which this holdout is applied to
        layerIDs:
          type: array
          items:
            type: string
          example:
            - 5O908pyGoCqw6QH1nt8v82
          description: an array of layerIDs which this holdout is applied to
        isGlobal:
          type: boolean
          example: false
          description: whether the holdout is being applied to all new gates
        targetingGateID:
          type: string
          nullable: true
          example: 4pjeXYDjC2WinSgOiII7wh
          description: the gateID that the holdout is targeting
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
      required:
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
        - isEnabled
        - passPercentage
        - gateIDs
        - experimentIDs
        - layerIDs
        - isGlobal
        - targetingGateID
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