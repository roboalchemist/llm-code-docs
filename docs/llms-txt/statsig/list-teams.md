# Source: https://docs.statsig.com/api-reference/users/list-teams.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Teams



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/users/teams
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
  /console/v1/users/teams:
    get:
      tags:
        - Users
      summary: List Teams
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
          description: Get teams response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/TeamDtoWithoutMembersDto'
                example:
                  message: Teams listed successfully.
                  data:
                    - name: test
                      defaultGateMetrics: []
                      defaultExperimentPrimaryMetrics: []
                      defaultExperimentSecondaryMetrics: []
                      defaultHoldoutMetrics: []
                      changeTeamConfigs: anyone
                      reviewApproval: anyone
                      defaultTargetApplications: []
                    - name: Console Team
                      defaultGateMetrics: []
                      defaultExperimentPrimaryMetrics: []
                      defaultExperimentSecondaryMetrics: []
                      defaultHoldoutMetrics: []
                      changeTeamConfigs: anyone
                      reviewApproval: anyone
                      defaultTargetApplications: []
                    - name: WHN-ish Team
                      defaultGateMetrics:
                        - name: MA Custom Metric 2
                          type: event_user
                        - name: MA Custom Metric 9
                          type: event_count_custom
                        - name: MA Custom Metric 3
                          type: event_count_custom
                      defaultExperimentPrimaryMetrics: []
                      defaultExperimentSecondaryMetrics:
                        - name: MA Custom Metric 2
                          type: event_user
                        - name: MA Custom Metric 9
                          type: event_count_custom
                        - name: MA Custom Metric 3
                          type: event_count_custom
                      defaultHoldoutMetrics: []
                      changeTeamConfigs: team_only
                      reviewApproval: team_only
                      defaultTargetApplications: []
                  pagination:
                    itemsPerPage: 3
                    pageNumber: 1
                    totalItems: 8
                    nextPage: /console/v1/users/teams?page=2&limit=3
                    previousPage: null
                    all: /console/v1/users/teams
              example:
                message: Teams listed successfully.
                data:
                  - name: test
                    defaultGateMetrics: []
                    defaultExperimentPrimaryMetrics: []
                    defaultExperimentSecondaryMetrics: []
                    defaultHoldoutMetrics: []
                    changeTeamConfigs: anyone
                    reviewApproval: anyone
                    defaultTargetApplications: []
                  - name: Console Team
                    defaultGateMetrics: []
                    defaultExperimentPrimaryMetrics: []
                    defaultExperimentSecondaryMetrics: []
                    defaultHoldoutMetrics: []
                    changeTeamConfigs: anyone
                    reviewApproval: anyone
                    defaultTargetApplications: []
                  - name: WHN-ish Team
                    defaultGateMetrics:
                      - name: MA Custom Metric 2
                        type: event_user
                      - name: MA Custom Metric 9
                        type: event_count_custom
                      - name: MA Custom Metric 3
                        type: event_count_custom
                    defaultExperimentPrimaryMetrics: []
                    defaultExperimentSecondaryMetrics:
                      - name: MA Custom Metric 2
                        type: event_user
                      - name: MA Custom Metric 9
                        type: event_count_custom
                      - name: MA Custom Metric 3
                        type: event_count_custom
                    defaultHoldoutMetrics: []
                    changeTeamConfigs: team_only
                    reviewApproval: team_only
                    defaultTargetApplications: []
                pagination:
                  itemsPerPage: 3
                  pageNumber: 1
                  totalItems: 8
                  nextPage: /console/v1/users/teams?page=2&limit=3
                  previousPage: null
                  all: /console/v1/users/teams
        '400':
          description: Invalid request. Please check the request input and try again.
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
    TeamDtoWithoutMembersDto:
      type: object
      properties:
        name:
          type: string
          description: The name of the team.
        description:
          type: string
          description: Description of the team.
        id:
          type: string
          description: The ID of the team.
        defaultGateMetrics:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                description: The name of the metric.
              type:
                type: string
                description: The type of the metric.
            required:
              - name
              - type
          description: Default gate metrics for the team.
        defaultExperimentPrimaryMetrics:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                description: The name of the metric.
              type:
                type: string
                description: The type of the metric.
            required:
              - name
              - type
          description: Default primary metrics for experiments in the team.
        defaultExperimentSecondaryMetrics:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                description: The name of the metric.
              type:
                type: string
                description: The type of the metric.
            required:
              - name
              - type
          description: Default secondary metrics for experiments in the team.
        defaultHoldoutMetrics:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                description: The name of the metric.
              type:
                type: string
                description: The type of the metric.
            required:
              - name
              - type
          description: Default holdout metrics for the team.
        changeTeamConfigs:
          type: string
          enum:
            - anyone
            - team_only
          description: 'Who can change team configurations: "anyone" or "team_only".'
        reviewApproval:
          type: string
          enum:
            - anyone
            - team_only
            - admin_only
          description: >-
            Who can review and approve changes: "anyone", "team_only", or
            "admin_only".
        defaultTargetApplications:
          type: array
          items:
            type: string
          description: Default target applications for the team.
        defaultHoldoutID:
          type: string
          nullable: true
          description: Default holdout ID for the team, if applicable.
        requireReviews:
          type: boolean
          nullable: true
          description: Whether reviews are required for changes, if applicable.
        requireGateTemplates:
          type: boolean
          nullable: true
          description: Whether gate templates are required for the team, if applicable.
        requireExperimentTemplates:
          type: boolean
          nullable: true
          description: >-
            Whether experiment templates are required for the team, if
            applicable.
        requireDynamicConfigTemplates:
          type: boolean
          nullable: true
          description: >-
            Whether dynamic config templates are required for the team, if
            applicable.
      required:
        - name
        - id
        - defaultGateMetrics
        - defaultExperimentPrimaryMetrics
        - defaultExperimentSecondaryMetrics
        - defaultHoldoutMetrics
        - changeTeamConfigs
        - reviewApproval
        - defaultTargetApplications
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