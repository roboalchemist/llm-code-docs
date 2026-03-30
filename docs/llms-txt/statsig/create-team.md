# Source: https://docs.statsig.com/api-reference/users/create-team.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Team



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/users/teams
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
    post:
      tags:
        - Users
      summary: Create Team
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TeamCreationDto'
      responses:
        '200':
          description: Create team response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/TeamDto'
                example:
                  message: Team created successfully.
                  data:
                    name: The Avengers
                    members:
                      - email: test@statsig.com
                        firstName: test
                        lastName: user
                        role: admin
                    admins: []
                    defaultGateMetrics: []
                    defaultExperimentPrimaryMetrics: []
                    defaultExperimentSecondaryMetrics: []
                    defaultHoldoutMetrics: []
                    changeTeamConfigs: anyone
                    reviewApproval: anyone
                    defaultTargetApplications: []
              example:
                message: Team created successfully.
                data:
                  name: The Avengers
                  members:
                    - email: test@statsig.com
                      firstName: test
                      lastName: user
                      role: admin
                  admins: []
                  defaultGateMetrics: []
                  defaultExperimentPrimaryMetrics: []
                  defaultExperimentSecondaryMetrics: []
                  defaultHoldoutMetrics: []
                  changeTeamConfigs: anyone
                  reviewApproval: anyone
                  defaultTargetApplications: []
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
    TeamCreationDto:
      type: object
      properties:
        name:
          type: string
          description: The name of the team.
        description:
          type: string
          description: Description of the team.
        members:
          type: array
          items:
            type: string
          description: Array of member email addresses in the team.
        admins:
          type: array
          items:
            type: string
          description: Array of admin email addresses in the team.
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
        - members
        - admins
        - defaultGateMetrics
        - defaultExperimentPrimaryMetrics
        - defaultExperimentSecondaryMetrics
        - defaultHoldoutMetrics
        - changeTeamConfigs
        - reviewApproval
        - defaultTargetApplications
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
    TeamDto:
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
        members:
          type: array
          items:
            type: object
            properties:
              email:
                type: string
                format: email
                description: The email address of the user.
              firstName:
                type: string
                description: The user's first name.
              lastName:
                type: string
                description: The user's last name.
              role:
                type: string
                description: >-
                  The user's role, which can be 'Admin', 'Read Only', 'Member',
                  or any custom role name.
            required:
              - email
              - firstName
              - lastName
              - role
        admins:
          type: array
          items:
            type: object
            properties:
              email:
                type: string
                format: email
                description: The email address of the user.
              firstName:
                type: string
                description: The user's first name.
              lastName:
                type: string
                description: The user's last name.
              role:
                type: string
                description: >-
                  The user's role, which can be 'Admin', 'Read Only', 'Member',
                  or any custom role name.
            required:
              - email
              - firstName
              - lastName
              - role
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
        - members
        - admins
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).