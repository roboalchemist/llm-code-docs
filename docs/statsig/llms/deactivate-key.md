# Source: https://docs.statsig.com/api-reference/keys/deactivate-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deactivate Key



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json patch /console/v1/keys/{id}/deactivate
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
  /console/v1/keys/{id}/deactivate:
    patch:
      tags:
        - Keys
      summary: Deactivate Key
      parameters:
        - name: id
          required: true
          in: path
          schema:
            type: string
      responses:
        '200':
          description: Key deactivated successfully
          content:
            application/json:
              schema:
                properties:
                  message:
                    type: string
                example:
                  message: Key deactivated successfully.
                  data:
                    key: secret-123
                    type: SERVER
                    description: Server secret key
                    scopes: []
                    environments:
                      - production
                    primaryTargetApp: primaryApp
                    secondaryTargetApps:
                      - secondaryApp
                    status: active
              example:
                message: Key deactivated successfully.
                data:
                  key: secret-123
                  type: SERVER
                  description: Server secret key
                  scopes: []
                  environments:
                    - production
                  primaryTargetApp: primaryApp
                  secondaryTargetApps:
                    - secondaryApp
                  status: active
        '403':
          description: Insufficient permissions.
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: integer
                    enum:
                      - 403
                  message:
                    type: string
                required:
                  - status
                  - message
              examples:
                Forbidden resource:
                  value:
                    status: 403
                    message: >-
                      Forbidden. The request was valid, but the server is
                      refusing action. You might not have the necessary
                      permissions to access the resource.
        '404':
          description: Key not found.
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
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).