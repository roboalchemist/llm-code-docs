# Source: https://docs.statsig.com/api-reference/experiments/get-pulse-load-history-details-warehouse-native.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Pulse Load History Details (Warehouse Native)



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/experiments/{id}/pulse_load_history/{dagID}
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
  /console/v1/experiments/{id}/pulse_load_history/{dagID}:
    get:
      tags:
        - Experiments
        - Experiments (Warehouse Native)
      summary: Get Pulse Load History Details (Warehouse Native)
      parameters:
        - name: dagID
          required: true
          in: path
          description: dagID
          schema:
            type: string
      responses:
        '200':
          description: Get Pulse Load History Details
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/PulseLoadHistoryDetailsDto'
                example:
                  message: Pulse load history read successfully.
                  data:
                    dagID: dag_123
                    jobs:
                      - jobType: user_metrics
                        startTime: 1718042400000
                        endTime: 1718046000000
                        sql: select * from metric_source_table
                        metricSourceName: Warehouse Metrics
                      - jobType: pulse
                        startTime: 1718046000000
                        endTime: 1718047200000
                        sql: select * from pulse_rollup_table
                        rollup: daily
              example:
                message: Pulse load history read successfully.
                data:
                  dagID: dag_123
                  jobs:
                    - jobType: user_metrics
                      startTime: 1718042400000
                      endTime: 1718046000000
                      sql: select * from metric_source_table
                      metricSourceName: Warehouse Metrics
                    - jobType: pulse
                      startTime: 1718046000000
                      endTime: 1718047200000
                      sql: select * from pulse_rollup_table
                      rollup: daily
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
          description: Pulse load history not found.
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
    PulseLoadHistoryDetailsDto:
      type: object
      properties:
        dagID:
          type: string
        jobs:
          type: array
          items:
            type: object
            properties:
              jobType:
                type: string
                description: The Echidna job type.
              startTime:
                type: number
                nullable: true
                description: Unix timestamp in milliseconds when this job started.
              endTime:
                type: number
                nullable: true
                description: >-
                  Unix timestamp in milliseconds when this job ended, when
                  available.
              sql:
                type: string
                nullable: true
                description: The SQL executed for this job.
              metricSourceName:
                type: string
                nullable: true
                description: >-
                  Present for user-metrics style jobs and names the metric
                  source used by the job.
              rollup:
                type: string
                enum:
                  - 7
                  - 14
                  - 28
                  - cumulative
                  - dx
                  - daily
                  - pre_exposure
                nullable: true
                description: >-
                  Present for pulse-style jobs and indicates the rollup used for
                  the calculation.
            required:
              - jobType
              - startTime
              - endTime
              - sql
      required:
        - dagID
        - jobs
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).