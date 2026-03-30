# Source: https://docs.statsig.com/api-reference/change-validation/update-change-validation-message.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update change validation message



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json patch /console/v1/change_validation/message
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
  /console/v1/change_validation/message:
    patch:
      tags:
        - Change Validation
      summary: Update change validation message
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ChangeValidationUpdateMessageDto'
      responses:
        '200':
          description: Update Change Validation Message Success
          content:
            application/json:
              schema:
                properties:
                  message:
                    type: string
                example:
                  message: Validation message updated successfully
              example:
                message: Validation message updated successfully
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    ChangeValidationUpdateMessageDto:
      type: object
      properties:
        reviewID:
          type: string
        message:
          type: string
      required:
        - reviewID
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).