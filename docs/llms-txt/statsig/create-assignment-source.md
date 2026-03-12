# Source: https://docs.statsig.com/api-reference/experiments/create-assignment-source.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Assignment Source



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/experiments/assignment_sources
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
  /console/v1/experiments/assignment_sources:
    post:
      tags:
        - Experiments
        - Experiments (Warehouse Native)
      summary: Create Assignment Source
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AssignmentSourceCreationDto'
      responses:
        '201':
          description: Create Assignment Source response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/AssignmentSourceContractDto'
                example:
                  message: Assignment Source created successfully
                  data:
                    name: exposures4
                    description: ''
                    tags: []
                    sql: SELECT * FROM shoppy-sales.experiment_data.exposures
                    timestampColumn: ts
                    groupIDColumn: group_id
                    experimentIDColumn: experiment_name
                    idTypeMapping:
                      - statsigUnitID: stableID
                        column: user_id
              example:
                message: Assignment Source created successfully
                data:
                  name: exposures4
                  description: ''
                  tags: []
                  sql: SELECT * FROM shoppy-sales.experiment_data.exposures
                  timestampColumn: ts
                  groupIDColumn: group_id
                  experimentIDColumn: experiment_name
                  idTypeMapping:
                    - statsigUnitID: stableID
                      column: user_id
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
    AssignmentSourceCreationDto:
      type: object
      properties:
        name:
          type: string
          description: Unique identifier for the assignment source.
        description:
          type: string
          description: Optional detailed context for the assignment source.
        isVerified:
          type: boolean
          description: >-
            Marks the assignment source as verified for internal
            trustworthiness.
        tags:
          type: array
          items:
            type: string
          description: Optional tags for categorization.
        sql:
          type: string
          description: SQL query defining the data source for assignments.
        timestampColumn:
          type: string
          description: Column name representing the timestamp of assignments.
        experimentIDColumn:
          type: string
          description: Column name for the experiment ID associated with the assignments.
        groupIDColumn:
          type: string
          description: Column name for the group ID linked to the assignments.
        groupNameColumn:
          type: string
          description: Optional column name for the group name linked to the assignments.
        idTypeMapping:
          type: array
          items:
            type: object
            properties:
              statsigUnitID:
                type: string
                description: ID for the Statsig unit.
              column:
                type: string
                description: Column name associated with the ID type mapping.
            required:
              - statsigUnitID
              - column
          description: Mappings of Statsig units to their respective columns.
        isReadOnly:
          type: boolean
          description: Specifies if the source can only be edited via the Console API.
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
        team:
          type: string
          nullable: true
          description: >-
            Optional field indicating the team name responsible for the metric,
            aiding in accountability and management.
        teamID:
          type: string
          nullable: true
          description: >-
            Optional field indicating the team ID responsible for the metric,
            aiding in accountability and management.
        scheduledReloadHour:
          type: integer
          minimum: 0
          maximum: 23
          nullable: true
          description: >-
            Optional field indicating what UTC hour to run a scheduled scan for
            the assignment source.
          format: int64
        dryRun:
          type: boolean
          description: >-
            Skips persisting the assignment source (used to validate that inputs
            are correct)
      required:
        - name
        - sql
        - timestampColumn
        - experimentIDColumn
        - groupIDColumn
        - idTypeMapping
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
    AssignmentSourceContractDto:
      type: object
      properties:
        name:
          type: string
          description: Unique identifier for the assignment source.
        description:
          type: string
          description: Detailed context and purpose of the assignment source.
        isVerified:
          type: boolean
          description: >-
            Marks the assignment source as verified for internal
            trustworthiness.
        tags:
          type: array
          items:
            type: string
          description: Tags for categorization and search.
        sql:
          type: string
          description: SQL query defining the data source for assignments.
        timestampColumn:
          type: string
          description: Column name representing the timestamp of assignments.
        experimentIDColumn:
          type: string
          description: Column name for the experiment ID associated with the assignments.
        groupIDColumn:
          type: string
          description: Column name for the group ID linked to the assignments.
        groupNameColumn:
          type: string
          description: Optional column name for the group name linked to the assignments.
        idTypeMapping:
          type: array
          items:
            type: object
            properties:
              statsigUnitID:
                type: string
                description: ID for the Statsig unit.
              column:
                type: string
                description: Column name associated with the ID type mapping.
            required:
              - statsigUnitID
              - column
          description: Mappings of Statsig units to their respective columns.
        isReadOnly:
          type: boolean
          description: Specifies if the source can only be edited via the Console API.
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
        team:
          type: string
          nullable: true
          description: >-
            Optional field indicating the team name responsible for the metric,
            aiding in accountability and management.
        teamID:
          type: string
          nullable: true
          description: >-
            Optional field indicating the team ID responsible for the metric,
            aiding in accountability and management.
        scheduledReloadHour:
          type: integer
          minimum: 0
          maximum: 23
          nullable: true
          description: >-
            Optional field indicating what UTC hour to run a scheduled scan for
            the assignment source.
          format: int64
      required:
        - name
        - description
        - tags
        - sql
        - timestampColumn
        - experimentIDColumn
        - groupIDColumn
        - idTypeMapping
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).