# Source: https://docs.statsig.com/api-reference/experiments-warehouse-native/create-qualifying-event.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Qualifying Event



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/experiments/qualifying_events
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
  /console/v1/experiments/qualifying_events:
    post:
      tags:
        - Experiments (Warehouse Native)
        - Experiments (Warehouse Native)
      summary: Create Qualifying Event
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MetricSourceCreationContractDto'
      responses:
        '201':
          description: Create qualifying event response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/MetricSourceContractDto'
                example:
                  message: Qualifying event created successfully.
                  data:
                    name: test_qualifying_event
                    description: Test description for qualifying event
                    tags:
                      - non_production
                    sql: SELECT * FROM `shoppy-sales.logging.events`
                    timestampColumn: ts
                    timestampAsDay: true
                    idTypeMapping:
                      - statsigUnitID: userID
                        column: user_id
                    sourceType: table
                    tableName: shoppy-sales.logging.events
              example:
                message: Qualifying event created successfully.
                data:
                  name: test_qualifying_event
                  description: Test description for qualifying event
                  tags:
                    - non_production
                  sql: SELECT * FROM `shoppy-sales.logging.events`
                  timestampColumn: ts
                  timestampAsDay: true
                  idTypeMapping:
                    - statsigUnitID: userID
                      column: user_id
                  sourceType: table
                  tableName: shoppy-sales.logging.events
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
    MetricSourceCreationContractDto:
      type: object
      properties:
        name:
          type: string
          description: The name of the source, serving as its primary identifier.
        description:
          type: string
          description: >-
            An optional description for the source, providing context and
            details about its purpose and usage.
        tags:
          type: array
          items:
            type: string
          description: >-
            Optional array of tags to categorize the source, facilitating easier
            organization and retrieval.
        sql:
          type: string
          description: The SQL query or statement used to extract data from the source.
        timestampColumn:
          type: string
          description: The name of the column containing timestamp data for the source.
        timestampAsDay:
          type: boolean
          description: >-
            Indicates whether the timestamp should be treated as a day-level
            granularity.
        idTypeMapping:
          type: array
          items:
            type: object
            properties:
              statsigUnitID:
                type: string
                description: The identifier mapping for Statsig units.
              column:
                type: string
                description: >-
                  The corresponding column name in the source that relates to
                  the Statsig unit ID.
            required:
              - statsigUnitID
              - column
          description: >-
            Array defining the mapping between Statsig unit IDs and their
            respective source columns.
        sourceType:
          type: string
          enum:
            - table
            - query
          description: >-
            The type of source, indicating whether it is a database table or a
            custom query.
        tableName:
          type: string
          description: The name of the database table if the source type is "table".
        datePartitionColumn:
          type: string
          description: >-
            The name of the date partition column if the source type is "table".
            Can be undefined.
        customFieldMapping:
          type: array
          items:
            type: object
            properties:
              key:
                type: string
                description: The identifier for the custom field mapping.
              formula:
                type: string
                description: >-
                  The formula or expression used to compute the custom field
                  value.
            required:
              - key
              - formula
          description: >-
            Optional array defining mappings for custom fields using specific
            formulas.
        isReadOnly:
          type: boolean
          description: Specifies if the source can only be edited via the Console API.
        isVerified:
          type: boolean
          description: >-
            Marks the metric source as verified, indicating trustworthiness
            within the organization.
          example: false
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
        dryRun:
          type: boolean
          description: >-
            Skips persisting the source (used to validate that inputs are
            correct)
      required:
        - name
        - sql
        - timestampColumn
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
    MetricSourceContractDto:
      type: object
      properties:
        name:
          type: string
          description: The name of the source, serving as its primary identifier.
        description:
          type: string
          description: >-
            A detailed description of the source, providing context and usage
            information.
        tags:
          type: array
          items:
            type: string
          description: >-
            Optional tags for categorizing the source and improving
            searchability.
        sql:
          type: string
          description: The SQL query or statement used to extract data from the source.
        timestampColumn:
          type: string
          description: The name of the column containing timestamp data for the source.
        timestampAsDay:
          type: boolean
          description: >-
            Indicates whether the timestamp should be treated as a day-level
            granularity.
        idTypeMapping:
          type: array
          items:
            type: object
            properties:
              statsigUnitID:
                type: string
                description: The identifier mapping for Statsig units.
              column:
                type: string
                description: >-
                  The corresponding column name in the source that relates to
                  the Statsig unit ID.
            required:
              - statsigUnitID
              - column
          description: >-
            Array defining the mapping between Statsig unit IDs and their
            respective source columns.
        sourceType:
          type: string
          enum:
            - table
            - query
          description: >-
            The type of source, indicating whether it is a database table or a
            custom query.
        tableName:
          type: string
          description: The name of the database table if the source type is "table".
        datePartitionColumn:
          type: string
          description: >-
            The name of the date partition column if the source type is "table".
            Can be undefined.
        customFieldMapping:
          type: array
          items:
            type: object
            properties:
              key:
                type: string
                description: The identifier for the custom field mapping.
              formula:
                type: string
                description: >-
                  The formula or expression used to compute the custom field
                  value.
            required:
              - key
              - formula
          description: >-
            Optional array defining mappings for custom fields using specific
            formulas.
        isReadOnly:
          type: boolean
          description: Specifies if the source can only be edited via the Console API.
        isVerified:
          type: boolean
          description: >-
            Marks the metric source as verified, indicating trustworthiness
            within the organization.
          example: false
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
        - sql
        - timestampColumn
        - idTypeMapping
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).