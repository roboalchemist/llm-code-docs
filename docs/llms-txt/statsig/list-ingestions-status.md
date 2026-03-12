# Source: https://docs.statsig.com/api-reference/ingestions/list-ingestions-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Ingestions Status



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/ingestion/status
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
  /console/v1/ingestion/status:
    get:
      tags:
        - Ingestions
      summary: List Ingestions Status
      parameters:
        - name: startDate
          required: true
          in: query
          description: Expected valid date in the form of YYYY-MM-DD
          schema:
            example: '2024-01-01'
            type: string
        - name: endDate
          required: true
          in: query
          description: Expected valid date in the form of YYYY-MM-DD
          schema:
            example: '2024-01-01'
            type: string
        - name: source
          required: false
          in: query
          schema:
            type: string
        - name: dataset
          required: false
          in: query
          schema:
            type: string
            enum:
              - Events
              - Metrics
              - entity_properties
              - export_exposures
              - export_events
        - name: status
          required: false
          in: query
          schema:
            type: string
            enum:
              - IMPORT_SUCCESSFUL
              - ROWS_INSERTED
              - LOADED_EMPTY_DATA
              - IMPORT_SCHEDULED
              - IMPORT_RESCHEDULED
              - IMPORT_STARTED
              - FILE_CREATED
              - DOWNLOAD_COMPLETED
              - BACKFILL_REQUESTED
              - ERROR
              - CONNECTION_CONFIG_ERROR
              - SSH_ERROR
              - QUERY_CONSTRUCTION_ERROR
              - INTERNAL_WRITE_ERROR_METRICS
              - INTERNAL_WRITE_ERROR_EVENTS
              - INTERNAL_WRITE_ERROR_EXPOSURES
              - QUERY_ERROR
              - SETUP_ERROR
              - AUTHENTICATION_ERROR
              - CONNECTION_ERROR
              - INTERNAL_SERVER_ERROR
              - BULK_LOAD_ERROR
              - BULK_LOAD_SUCCESSFUL
              - '%Other'
        - name: statuses
          required: false
          in: query
          schema:
            type: array
            items:
              type: string
              enum:
                - IMPORT_SUCCESSFUL
                - ROWS_INSERTED
                - LOADED_EMPTY_DATA
                - IMPORT_SCHEDULED
                - IMPORT_RESCHEDULED
                - IMPORT_STARTED
                - FILE_CREATED
                - DOWNLOAD_COMPLETED
                - BACKFILL_REQUESTED
                - ERROR
                - CONNECTION_CONFIG_ERROR
                - SSH_ERROR
                - QUERY_CONSTRUCTION_ERROR
                - INTERNAL_WRITE_ERROR_METRICS
                - INTERNAL_WRITE_ERROR_EVENTS
                - INTERNAL_WRITE_ERROR_EXPOSURES
                - QUERY_ERROR
                - SETUP_ERROR
                - AUTHENTICATION_ERROR
                - CONNECTION_ERROR
                - INTERNAL_SERVER_ERROR
                - BULK_LOAD_ERROR
                - BULK_LOAD_SUCCESSFUL
                - '%Other'
      responses:
        '200':
          description: List Ingestions Status Success
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/IngestionStatusDto'
                example:
                  - message: Your job for events ingestion completed successfully
                    timestamp: '2023-09-07T00:50:07.941Z'
                    ingestion_dataset: events
                    ingestion_source: null
                    status: BACKFILL_STARTED
              example:
                - message: Your job for events ingestion completed successfully
                  timestamp: '2023-09-07T00:50:07.941Z'
                  ingestion_dataset: events
                  ingestion_source: null
                  status: BACKFILL_STARTED
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
    IngestionStatusDto:
      type: object
      properties:
        ds:
          type: string
          format: date-time
        ingestion_dataset:
          type: string
          nullable: true
        ingestion_source:
          type: string
          nullable: true
        source_name:
          type: string
          nullable: true
        message:
          type: string
          nullable: true
        error_message:
          type: string
        status:
          type: string
          nullable: true
        rowCount:
          type: number
          format: double
        metricCount:
          type: number
          format: double
        timestamp:
          type: string
          format: date-time
          nullable: true
      required:
        - ingestion_dataset
        - ingestion_source
        - source_name
        - message
        - status
        - timestamp
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