# Source: https://docs.statsig.com/api-reference/configs/read-exposure-event-count.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Exposure Event Count

> Get the count of exposure events recently received by Statsig.



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/exposure_count
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
  /console/v1/exposure_count:
    get:
      tags:
        - Configs
      summary: Read Exposure Event Count
      description: Get the count of exposure events recently received by Statsig.
      parameters:
        - name: experiments
          required: false
          in: query
          schema:
            oneOf:
              - type: string
              - type: array
                items:
                  type: string
                maxItems: 25
        - name: gates
          required: false
          in: query
          schema:
            oneOf:
              - type: string
              - type: array
                items:
                  type: string
                maxItems: 25
        - name: dynamicConfigs
          required: false
          in: query
          schema:
            oneOf:
              - type: string
              - type: array
                items:
                  type: string
                maxItems: 25
      responses:
        '200':
          description: Get Experiment Success
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/ExposureCountDto'
                example:
                  message: Exposure count fetched successfully.
                  data:
                    gates:
                      - id: a_gate
                        pastDay: 0
                        past7Days: 98
                    experiments:
                      - id: my_experiment
                        pastDay: 102
                        past7Days: 558
                      - id: another_experiment
                        pastDay: 5904
                        past7Days: 2078
                    dynamicConfigs:
                      - id: dc_limit
                        pastDay: 240830
                        past7Days: 1329945
              example:
                message: Exposure count fetched successfully.
                data:
                  gates:
                    - id: a_gate
                      pastDay: 0
                      past7Days: 98
                  experiments:
                    - id: my_experiment
                      pastDay: 102
                      past7Days: 558
                    - id: another_experiment
                      pastDay: 5904
                      past7Days: 2078
                  dynamicConfigs:
                    - id: dc_limit
                      pastDay: 240830
                      past7Days: 1329945
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
                    message: Data is not available
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
    ExposureCountDto:
      type: object
      properties:
        gates:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              pastDay:
                type: number
              past7Days:
                type: number
            required:
              - id
              - pastDay
              - past7Days
          maxItems: 25
          description: ids of gates to query (max 25)
        experiments:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              pastDay:
                type: number
              past7Days:
                type: number
            required:
              - id
              - pastDay
              - past7Days
          maxItems: 25
          description: ids of experiments to query (max 25)
        dynamicConfigs:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              pastDay:
                type: number
              past7Days:
                type: number
            required:
              - id
              - pastDay
              - past7Days
          maxItems: 25
          description: ids of dynamic configs to query (max 25)
      required:
        - gates
        - experiments
        - dynamicConfigs
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).