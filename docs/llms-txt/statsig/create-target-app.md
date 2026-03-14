# Source: https://docs.statsig.com/api-reference/target-app/create-target-app.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Target App



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/target_app
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
    post:
      tags:
        - Target App
      summary: Create Target App
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TargetAppCreateDto'
      responses:
        '200':
          description: Create Target App Success
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/TargetAppDto'
                example:
                  name: Target app 1
                  description: Example description
                  gates:
                    - Example gate
                  dynamicConfigs:
                    - Example dynamic config
                  experiments:
                    - Example experiment
              example:
                name: Target app 1
                description: Example description
                gates:
                  - Example gate
                dynamicConfigs:
                  - Example dynamic config
                experiments:
                  - Example experiment
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    TargetAppCreateDto:
      type: object
      properties:
        name:
          type: string
          example: string
          description: name of the target app
        description:
          type: string
          example: a description
          description: a description of the target app
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
        - name
        - description
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
    TargetAppDto:
      type: object
      properties:
        id:
          type: string
          example: string
          description: id of target app
        name:
          type: string
          example: a tag
          description: name of the target app
      required:
        - name
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).