# Source: https://docs.statsig.com/api-reference/experiments/finish-experiment-early.md

# Source: https://docs.statsig.com/api-reference/autotunes/finish-experiment-early.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Finish Experiment Early



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json put /console/v1/autotunes/{id}/make_decision
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
  /console/v1/autotunes/{id}/make_decision:
    put:
      tags:
        - Autotunes
      summary: Finish Experiment Early
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
              $ref: '#/components/schemas/ExperimentStatusUpdateDto'
      responses:
        '200':
          description: Finish Experiment Early Success
          content:
            application/json:
              schema:
                properties:
                  message:
                    type: string
                example:
                  message: Decision made for Autotune Experiment.
              example:
                message: Decision made for Autotune Experiment.
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
                    message: Autotune experiment has not yet started
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
                    message: Autotune Experiment not found.
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    ExperimentStatusUpdateDto:
      type: object
      properties:
        id:
          type: string
          description: The ID of the group to launch
          example: groupid123
        decisionReason:
          type: string
          description: The reason for making the decision to update the experiment status
          example: Your reason for stopping early
        removeTargeting:
          default: false
          type: boolean
          description: Indicates whether to remove targeting from the experiment
          example: false
      required:
        - id
        - decisionReason
      description: Schema for updating the status of an experiment
      example:
        id: experiment123
        decisionReason: Your reason for stopping early
        removeTargeting: false
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).