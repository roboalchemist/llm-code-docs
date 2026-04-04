# Source: https://docs.statsig.com/api-reference/experiments-warehouse-native/list-qualifying-event.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List qualifying event



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/experiments/qualifying_events
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
    get:
      tags:
        - Experiments (Warehouse Native)
        - Experiments (Warehouse Native)
      summary: List qualifying event
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
          description: List metric source response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/MetricSourceContractDto'
                example:
                  message: Qualifying events listed successfully.
                  data:
                    - name: Log Events
                      description: >-
                        all app events including add to cart, purchase, page
                        view, checkout
                      tags: []
                      sql: >
                        SELECT *

                        FROM shoppy-sales.logging.events

                        where DATE(ts) between {statsig_start_date} and
                        {statsig_end_date}
                      timestampColumn: ts
                      timestampAsDay: false
                      idTypeMapping:
                        - statsigUnitID: userID
                          column: user_id
                        - statsigUnitID: deviceID
                          column: device_id
                      tableName: ''
                      customFieldMapping:
                        - key: ''
                          formula: ''
                  pagination:
                    itemsPerPage: 1
                    pageNumber: 1
                    totalItems: 14
                    nextPage: /console/v1/metrics/qualifying_event/list?page=2&limit=1
                    previousPage: null
                    all: /console/v1/metrics/qualifying_event/list
              example:
                message: Qualifying events listed successfully.
                data:
                  - name: Log Events
                    description: >-
                      all app events including add to cart, purchase, page view,
                      checkout
                    tags: []
                    sql: >
                      SELECT *

                      FROM shoppy-sales.logging.events

                      where DATE(ts) between {statsig_start_date} and
                      {statsig_end_date}
                    timestampColumn: ts
                    timestampAsDay: false
                    idTypeMapping:
                      - statsigUnitID: userID
                        column: user_id
                      - statsigUnitID: deviceID
                        column: device_id
                    tableName: ''
                    customFieldMapping:
                      - key: ''
                        formula: ''
                pagination:
                  itemsPerPage: 1
                  pageNumber: 1
                  totalItems: 14
                  nextPage: /console/v1/metrics/qualifying_event/list?page=2&limit=1
                  previousPage: null
                  all: /console/v1/metrics/qualifying_event/list
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