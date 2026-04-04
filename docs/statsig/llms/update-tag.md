# Source: https://docs.statsig.com/api-reference/tags/update-tag.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Tag



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json patch /console/v1/tags/{id}
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
  /console/v1/tags/{id}:
    patch:
      tags:
        - Tags
      summary: Update Tag
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
              $ref: '#/components/schemas/TagUpdateDto'
      responses:
        '200':
          description: Update Tag Response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/TagDto'
                example:
                  message: Tag updated successfully
                  data:
                    id: string
                    name: a tag
                    description: a description
                    isCore: false
              example:
                message: Tag updated successfully
                data:
                  id: string
                  name: a tag
                  description: a description
                  isCore: false
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    TagUpdateDto:
      type: object
      properties:
        name:
          type: string
          maxLength: 100
          minLength: 1
        description:
          type: string
          maxLength: 1000
        isCore:
          default: false
          type: boolean
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
    TagDto:
      type: object
      properties:
        id:
          type: string
          example: string
          description: id of the tag
        name:
          type: string
          example: a tag
          description: name of the tag
        description:
          type: string
          example: a description
          description: description of the tag
        isCore:
          type: boolean
          example: false
          description: is this a core tag
      required:
        - id
        - name
        - description
        - isCore
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).