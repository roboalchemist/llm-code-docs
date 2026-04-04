# Source: https://docs.statsig.com/api-reference/ingestions/get-ingestion-event-delta-ledger.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Ingestion Event Delta Ledger



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/ingestion/events/delta
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
  /console/v1/ingestion/events/delta:
    get:
      tags:
        - Ingestions
      summary: Get Ingestion Event Delta Ledger
      parameters:
        - name: source_name
          required: false
          in: query
          schema:
            type: string
        - name: event_name
          required: false
          in: query
          schema:
            type: string
        - name: start_date
          required: true
          in: query
          description: Expected valid date in the form of YYYY-MM-DD
          schema:
            example: '2024-01-01'
            type: string
        - name: end_date
          required: true
          in: query
          description: Expected valid date in the form of YYYY-MM-DD
          schema:
            example: '2024-01-01'
            type: string
      responses:
        '200':
          description: Get Ingestion Event Delta Ledger Success
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/IngestionEventDeltaResponseDto'
                example:
                  type: databricks
                  dataset: Metrics
                  source_name: ingestion-1
                  query: SELECT * FROM TABLE
                  column_mapping:
                    unit_id: string
                    id_type: string
                    dateid: string
                    metric_name: string
                    metric_value: string
                    numerator: string
                    denominator: string
                  use_delta_sharing: false
                  share: string
                  schema: string
                  table: string
                  enabled: false
              example:
                type: databricks
                dataset: Metrics
                source_name: ingestion-1
                query: SELECT * FROM TABLE
                column_mapping:
                  unit_id: string
                  id_type: string
                  dateid: string
                  metric_name: string
                  metric_value: string
                  numerator: string
                  denominator: string
                use_delta_sharing: false
                share: string
                schema: string
                table: string
                enabled: false
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
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
    IngestionEventDeltaResponseDto:
      oneOf:
        - type: array
          items:
            type: object
            properties:
              date:
                type: string
              source:
                type: string
              event:
                type: string
              internal_count:
                type: number
              external_count:
                type: number
              has_diff:
                type: boolean
              threshold:
                type: number
              last_updated_time:
                type: string
                format: date-time
            required:
              - date
              - source
              - event
              - internal_count
              - external_count
              - has_diff
              - threshold
              - last_updated_time
        - type: array
          items:
            type: object
            properties:
              date:
                type: string
              events:
                type: array
                items:
                  type: object
                  properties:
                    source:
                      type: string
                    event:
                      type: string
                    internal_count:
                      type: number
                    external_count:
                      type: number
                    has_diff:
                      type: boolean
                    threshold:
                      type: number
                    last_updated_time:
                      type: string
                      format: date-time
                  required:
                    - source
                    - event
                    - internal_count
                    - external_count
                    - has_diff
                    - threshold
                    - last_updated_time
            required:
              - date
              - events
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).