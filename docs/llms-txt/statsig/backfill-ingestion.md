# Source: https://docs.statsig.com/api-reference/ingestions/backfill-ingestion.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Backfill Ingestion



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/ingestion/backfill
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
  /console/v1/ingestion/backfill:
    post:
      tags:
        - Ingestions
      summary: Backfill Ingestion
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/IngestionBackfillContractDto'
      responses:
        '200':
          description: Backfill Ingestion Success
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/IngestionBackfillDataDto'
                example:
                  message: Ingestion backfilled successfully.
                  data:
                    runID: string
              example:
                message: Ingestion backfilled successfully.
                data:
                  runID: string
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
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    IngestionBackfillContractDto:
      type: object
      properties:
        datestamp_start:
          type: string
          description: Expected valid date in the form of YYYY-MM-DD
          example: '2024-01-01'
        datestamp_end:
          type: string
          description: Expected valid date in the form of YYYY-MM-DD
          example: '2024-01-01'
        type:
          type: string
          enum:
            - redshift
            - bigquery-v2
            - snowflake-v2
            - databricks
            - azure-synapse
            - s3
            - athena
            - adls
        source:
          oneOf:
            - type: string
            - type: array
              items:
                type: string
          nullable: true
        dataset:
          type: string
          enum:
            - Events
            - Metrics
            - entity_properties
            - export_exposures
            - export_events
      required:
        - datestamp_start
        - datestamp_end
        - type
        - dataset
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
    IngestionBackfillDataDto:
      type: object
      properties:
        runID:
          type: string
      required:
        - runID
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).