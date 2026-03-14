# Source: https://docs.statsig.com/api-reference/experiments/load-pulse-warehouse-native.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Load Pulse (Warehouse Native)



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/experiments/{id}/load_pulse
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
  /console/v1/experiments/{id}/load_pulse:
    post:
      tags:
        - Experiments
        - Experiments (Warehouse Native)
      summary: Load Pulse (Warehouse Native)
      parameters:
        - name: id
          required: true
          in: path
          description: id
          schema:
            type: string
        - name: refresh
          required: false
          in: query
          schema:
            default: full
            type: string
            enum:
              - full
              - incremental
              - metric
        - name: metricIDs
          required: false
          in: query
          schema:
            type: array
            items:
              type: string
        - name: turboMode
          required: false
          in: query
          schema:
            type: boolean
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EchidnaLoadPulseQueryDto'
      responses:
        '200':
          description: Load Pulse Success
          content:
            application/json:
              schema:
                properties:
                  message:
                    type: string
                example:
                  message: Experiment is loading.
              example:
                message: Experiment is loading.
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
    EchidnaLoadPulseQueryDto:
      type: object
      properties:
        refresh:
          default: full
          type: string
          enum:
            - full
            - incremental
            - metric
        metricIDs:
          type: array
          items:
            type: string
        turboMode:
          type: boolean
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).