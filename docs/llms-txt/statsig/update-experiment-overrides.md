# Source: https://docs.statsig.com/api-reference/experiments/update-experiment-overrides.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Experiment Overrides



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/experiments/{id}/overrides
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
  /console/v1/experiments/{id}/overrides:
    post:
      tags:
        - Experiments
      summary: Update Experiment Overrides
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
              $ref: '#/components/schemas/ExperimentOverridesDto'
      responses:
        '200':
          description: Update Experiment Overrides Success
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/ExperimentOverridesDto'
                example:
                  overrides:
                    - type: segment
                      id: a_segment
                      groupID: Control
                    - type: gate
                      id: a_gate
                      groupID: Test
                  userIDOverrides:
                    - groupID: Control
                      ids:
                        - updated_control_id_list
                    - groupID: Test
                      ids:
                        - updated_test_id_list
              example:
                overrides:
                  - type: segment
                    id: a_segment
                    groupID: Control
                  - type: gate
                    id: a_gate
                    groupID: Test
                userIDOverrides:
                  - groupID: Control
                    ids:
                      - updated_control_id_list
                  - groupID: Test
                    ids:
                      - updated_test_id_list
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
          description: Experiment not found.
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
    ExperimentOverridesDto:
      type: object
      properties:
        overrides:
          type: array
          items:
            type: object
            properties:
              type:
                type: string
                enum:
                  - gate
                  - segment
              id:
                type: string
                description: The id of the segment or gate
              groupID:
                type: string
                description: The experiment group which user will be forced into
              environment:
                type: string
                nullable: true
                description: >-
                  Optional environment designation (e.g., production, staging)
                  for the experiment.
            required:
              - type
              - id
              - groupID
          maxItems: 1000
          description: >-
            Array of experiment overrides, each specifying type, ID, and group
            ID.
        userIDOverrides:
          type: array
          items:
            type: object
            properties:
              groupID:
                type: string
                description: The experiment group the user will be forced into.
              ids:
                type: array
                items:
                  type: string
                maxItems: 1000
                description: >-
                  Array of user IDs to be assigned to the specified experiment
                  group.
              environment:
                type: string
                nullable: true
                description: >-
                  Optional environment designation (e.g., production, staging)
                  for the experiment.
              unitType:
                type: string
                nullable: true
                description: >-
                  Optional type of unit for the experiment, defining the scope
                  of the override.
            required:
              - groupID
              - ids
          description: >-
            Array of user ID overrides, specifying which users to force into
            experiment groups.
      required:
        - overrides
        - userIDOverrides
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
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).