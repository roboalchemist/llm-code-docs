# Source: https://docs.statsig.com/api-reference/experiments/delete-assignment-source.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Assignment Source



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json delete /console/v1/experiments/assignment_source/{name}
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
  /console/v1/experiments/assignment_source/{name}:
    delete:
      tags:
        - Experiments
        - Experiments (Warehouse Native)
      summary: Delete Assignment Source
      parameters:
        - name: name
          required: true
          in: path
          description: Name of the assignment source
          schema:
            type: string
      responses:
        '200':
          description: Delete Assignment Source response
          content:
            application/json:
              schema:
                properties:
                  message:
                    type: string
                example:
                  message: Assignment source deleted successfully.
              example:
                message: Assignment source deleted successfully.
      security:
        - STATSIG-API-KEY: []
components:
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).