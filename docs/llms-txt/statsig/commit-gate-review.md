# Source: https://docs.statsig.com/api-reference/gates/commit-gate-review.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Commit Gate Review



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json put /console/v1/gates/{id}/reviews/{reviewID}/commit
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
  /console/v1/gates/{id}/reviews/{reviewID}/commit:
    put:
      tags:
        - Gates
      summary: Commit Gate Review
      parameters:
        - name: id
          required: true
          in: path
          schema:
            type: string
        - name: reviewID
          required: true
          in: path
          schema:
            type: string
      responses:
        '200':
          description: Commit an approved gate review
          content:
            application/json:
              schema:
                properties:
                  message:
                    type: string
                example:
                  message: Gate review committed successfully
              example:
                message: Gate review committed successfully
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