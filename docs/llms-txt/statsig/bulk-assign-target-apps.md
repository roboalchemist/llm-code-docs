# Source: https://docs.statsig.com/api-reference/target-app/bulk-assign-target-apps.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Assign Target Apps



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json patch /console/v1/target_app
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
  /console/v1/target_app:
    patch:
      tags:
        - Target App
      summary: Bulk Assign Target Apps
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BulkAssignConfigTargetAppDto'
      responses:
        '200':
          description: Bulk Assign Target Apps Success
          content:
            application/json:
              schema:
                properties:
                  message:
                    type: string
                example:
                  message: Target apps updated successfully.
              example:
                message: Target apps updated successfully.
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
          description: Gates with IDs [not a gate] do not exist
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
    BulkAssignConfigTargetAppDto:
      type: object
      properties:
        targetApps:
          type: array
          items:
            type: string
          minItems: 1
          description: target app ids
        gates:
          type: array
          items:
            type: string
          description: Gate IDs to assign to target app(s)
        dynamicConfigs:
          type: array
          items:
            type: string
          description: Dynamic Config IDs to assign to target app(s)
        experiments:
          type: array
          items:
            type: string
          description: Experiment IDs to assign to target app(s)
      required:
        - targetApps
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).