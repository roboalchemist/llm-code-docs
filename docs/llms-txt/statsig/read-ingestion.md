# Source: https://docs.statsig.com/api-reference/ingestions/read-ingestion.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Ingestion



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/ingestion
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
  /console/v1/ingestion:
    get:
      tags:
        - Ingestions
      summary: Read Ingestion
      parameters:
        - name: type
          required: true
          in: query
          schema:
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
        - name: dataset
          required: true
          in: query
          schema:
            type: string
            enum:
              - Events
              - Metrics
              - entity_properties
              - export_exposures
              - export_events
        - name: source_name
          required: false
          in: query
          schema:
            type: string
      responses:
        '200':
          description: Read Ingestion Success
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/IngestionDto'
                example:
                  message: Ingestion schedule updated successfully.
                  data:
                    dataset: Metrics
                    scheduled_hour_pst: 10
              example:
                message: Ingestion schedule updated successfully.
                data:
                  dataset: Metrics
                  scheduled_hour_pst: 10
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
    IngestionDto:
      type: object
      properties:
        id:
          type: string
        type:
          type: string
        enabled:
          type: boolean
        data:
          type: object
      required:
        - id
        - type
        - enabled
        - data
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).