# Source: https://docs.statsig.com/api-reference/gates/load-pulse-gate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Load Pulse Gate



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/gates/{id}/load_pulse
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
  /console/v1/gates/{id}/load_pulse:
    post:
      tags:
        - Gates
      summary: Load Pulse Gate
      parameters:
        - name: id
          required: true
          in: path
          description: id
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EchidnaGateLoadPulseQueryDto'
      responses:
        '200':
          description: Load Pulse Gate Response
          content:
            application/json:
              schema:
                properties:
                  message:
                    type: string
                example:
                  message: Gate loaded successfully.
              example:
                message: Gate loaded successfully.
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    EchidnaGateLoadPulseQueryDto:
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
        ruleId:
          type: string
        turboMode:
          type: boolean
      required:
        - ruleId
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).