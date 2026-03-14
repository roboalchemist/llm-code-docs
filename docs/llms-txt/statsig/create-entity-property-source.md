# Source: https://docs.statsig.com/api-reference/experiments/create-entity-property-source.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Entity Property Source



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/experiments/entity_properties
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
  /console/v1/experiments/entity_properties:
    post:
      tags:
        - Experiments
        - Experiments (Warehouse Native)
      summary: Create Entity Property Source
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EntityPropertySourceCreationDto'
      responses:
        '201':
          description: Create Entity Property Source response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/EntityPropertySourceDto'
                example:
                  message: Entity Property Source created successfully
                  data:
                    name: Location
                    description: ''
                    tags: []
                    sql: SELECT * FROM shoppy-sales.setup.user_properties
                    timestampColumn: timestamp
                    idTypeMapping:
                      - statsigUnitID: stableID
                        column: user_id
                    timestampAsDay: true
              example:
                message: Entity Property Source created successfully
                data:
                  name: Location
                  description: ''
                  tags: []
                  sql: SELECT * FROM shoppy-sales.setup.user_properties
                  timestampColumn: timestamp
                  idTypeMapping:
                    - statsigUnitID: stableID
                      column: user_id
                  timestampAsDay: true
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
        '404':
          description: Not Found. The requested resource could not be found.
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
    EntityPropertySourceCreationDto:
      type: object
      properties:
        name:
          type: string
          description: Unique identifier for the entity property source.
        description:
          type: string
          description: Optional detailed context for the entity property source.
        tags:
          type: array
          items:
            type: string
          description: Optional tags for categorization.
        sql:
          type: string
          description: SQL query defining the data source.
        timestampColumn:
          type: string
          description: Optional column name for timestamp.
        timestampAsDay:
          type: boolean
          description: Indicates if the timestamp is treated as a day.
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
                description: Column name linked to the ID.
            required:
              - statsigUnitID
              - column
          description: Mappings of Statsig units to their columns.
        isReadOnly:
          type: boolean
          description: Specifies if the source can only be edited via the Console API.
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
        dryRun:
          type: boolean
          description: >-
            Skips persisting the entity property source (used to validate that
            inputs are correct)
      required:
        - name
        - sql
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
    EntityPropertySourceDto:
      type: object
      properties:
        name:
          type: string
          description: Unique identifier for the entity property source.
        description:
          type: string
          description: Detailed context and purpose of the entity property source.
        tags:
          type: array
          items:
            type: string
          description: Tags for categorization and search.
        sql:
          type: string
          description: SQL query defining the data source.
        timestampColumn:
          type: string
          description: Optional column name for timestamp.
        timestampAsDay:
          type: boolean
          description: Indicates if the timestamp is treated as a day.
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
                description: Column name linked to the ID.
            required:
              - statsigUnitID
              - column
          description: Mappings of Statsig units to their columns.
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
      required:
        - name
        - description
        - tags
        - sql
        - idTypeMapping
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).