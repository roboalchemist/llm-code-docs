# Source: https://docs.statsig.com/api-reference/ingestions/read-ingestion-run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Ingestion Run



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/ingestion/runs/{id}
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
  /console/v1/ingestion/runs/{id}:
    get:
      tags:
        - Ingestions
      summary: Read Ingestion Run
      parameters:
        - name: id
          required: true
          in: path
          description: id
          schema:
            type: string
      responses:
        '200':
          description: Read Ingestion Run Success
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/IngestionRunDataContractDto'
                example:
                  message: Ingestion Run Read Successfully
                  data:
                    runID: de941fa2-3e0f-44ec-a44c-5c51eed07e0d
                    latestStatus: download_error
                    lastUpdatedAt: '2023-12-13T02:44:23.790Z'
                    createdAt: '2023-12-13T02:30:55.992Z'
                    trigger: scheduled
                    sources:
                      - Events 1
                      - Events 2
                    dateStamps:
                      - '2023-12-11'
                    runHistory:
                      - statusTimestamp: '2023-12-13T02:44:24.865Z'
                        status: download_error
                      - statusTimestamp: '2023-12-13T02:44:12.421Z'
                        status: download_started
                      - statusTimestamp: '2023-12-13T02:41:48.458Z'
                        status: download_error
                      - statusTimestamp: '2023-12-13T02:40:56.694Z'
                        status: download_started
                      - statusTimestamp: '2023-12-13T02:32:35.607Z'
                        status: started
                      - statusTimestamp: '2023-12-13T02:30:55.992Z'
                        status: enqueued
                    granularHistory:
                      - source: Events 1
                        latestSourceStatus: download_error
                        statusByDate:
                          - dateStamp: '2023-12-11'
                            statuses:
                              - statusTimestamp: '2023-12-13T02:41:47.374Z'
                                status: download_error
                              - statusTimestamp: '2023-12-13T02:40:50.210Z'
                                status: download_started
                              - statusTimestamp: '2023-12-13T02:32:33.118Z'
                                status: started
                              - statusTimestamp: '2023-12-13T02:30:55.992Z'
                                status: enqueued
                      - source: Events 2
                        latestSourceStatus: download_error
                        statusByDate:
                          - dateStamp: '2023-12-11'
                            statuses:
                              - statusTimestamp: '2023-12-13T02:41:47.374Z'
                                status: download_error
                              - statusTimestamp: '2023-12-13T02:40:50.210Z'
                                status: download_started
                              - statusTimestamp: '2023-12-13T02:32:33.118Z'
                                status: started
                              - statusTimestamp: '2023-12-13T02:30:55.992Z'
                                status: enqueued
              example:
                message: Ingestion Run Read Successfully
                data:
                  runID: de941fa2-3e0f-44ec-a44c-5c51eed07e0d
                  latestStatus: download_error
                  lastUpdatedAt: '2023-12-13T02:44:23.790Z'
                  createdAt: '2023-12-13T02:30:55.992Z'
                  trigger: scheduled
                  sources:
                    - Events 1
                    - Events 2
                  dateStamps:
                    - '2023-12-11'
                  runHistory:
                    - statusTimestamp: '2023-12-13T02:44:24.865Z'
                      status: download_error
                    - statusTimestamp: '2023-12-13T02:44:12.421Z'
                      status: download_started
                    - statusTimestamp: '2023-12-13T02:41:48.458Z'
                      status: download_error
                    - statusTimestamp: '2023-12-13T02:40:56.694Z'
                      status: download_started
                    - statusTimestamp: '2023-12-13T02:32:35.607Z'
                      status: started
                    - statusTimestamp: '2023-12-13T02:30:55.992Z'
                      status: enqueued
                  granularHistory:
                    - source: Events 1
                      latestSourceStatus: download_error
                      statusByDate:
                        - dateStamp: '2023-12-11'
                          statuses:
                            - statusTimestamp: '2023-12-13T02:41:47.374Z'
                              status: download_error
                            - statusTimestamp: '2023-12-13T02:40:50.210Z'
                              status: download_started
                            - statusTimestamp: '2023-12-13T02:32:33.118Z'
                              status: started
                            - statusTimestamp: '2023-12-13T02:30:55.992Z'
                              status: enqueued
                    - source: Events 2
                      latestSourceStatus: download_error
                      statusByDate:
                        - dateStamp: '2023-12-11'
                          statuses:
                            - statusTimestamp: '2023-12-13T02:41:47.374Z'
                              status: download_error
                            - statusTimestamp: '2023-12-13T02:40:50.210Z'
                              status: download_started
                            - statusTimestamp: '2023-12-13T02:32:33.118Z'
                              status: started
                            - statusTimestamp: '2023-12-13T02:30:55.992Z'
                              status: enqueued
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
                    message: runID de941fa2-3e0f-44ec-a44c-5c51eed07e0z not found
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
    IngestionRunDataContractDto:
      type: object
      properties:
        runID:
          type: string
        latestStatus:
          type: string
        lastUpdatedAt:
          type: string
          format: date-time
        createdAt:
          type: string
          format: date-time
        trigger:
          type: string
        sources:
          type: array
          items:
            type: string
        dateStamps:
          type: array
          items:
            type: string
        runHistory:
          type: array
          items:
            type: object
            properties:
              statusTimestamp:
                type: string
                format: date-time
              status:
                type: string
            required:
              - statusTimestamp
              - status
        granularHistory:
          type: array
          items:
            type: object
            properties:
              source:
                type: string
              latestSourceStatus:
                type: string
              statusByDate:
                type: array
                items:
                  type: object
                  properties:
                    dateStamp:
                      type: string
                    statuses:
                      type: array
                      items:
                        type: object
                        properties:
                          statusTimestamp:
                            type: string
                            format: date-time
                          status:
                            type: string
                        required:
                          - statusTimestamp
                          - status
                  required:
                    - dateStamp
                    - statuses
            required:
              - source
              - latestSourceStatus
              - statusByDate
      required:
        - runID
        - latestStatus
        - lastUpdatedAt
        - createdAt
        - trigger
        - sources
        - dateStamps
        - runHistory
        - granularHistory
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).