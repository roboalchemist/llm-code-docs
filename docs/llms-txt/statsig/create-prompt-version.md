# Source: https://docs.statsig.com/api-reference/prompts/create-prompt-version.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Prompt Version



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/prompts/{id}/versions
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
  /console/v1/prompts/{id}/versions:
    post:
      tags:
        - Prompts
      summary: Create Prompt Version
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
              $ref: '#/components/schemas/AIConfigVersionCreateDto'
      responses:
        '201':
          description: Create Prompt Version
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/AIConfigVersionCreateDto'
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    AIConfigVersionCreateDto:
      type: object
      properties:
        prompts:
          type: array
          items:
            type: object
            properties:
              content:
                type: string
              role:
                type: string
                enum:
                  - system
                  - user
                  - assistant
            required:
              - content
              - role
        temperature:
          type: number
          format: double
        model:
          type: string
        name:
          type: string
          maxLength: 100
          minLength: 3
          pattern: ^[a-zA-Z0-9_\-. ]*$
          description: The Prompt Version display name
          example: my_config
        provider:
          type: string
        workflow_body:
          type: object
          properties:
            type:
              type: string
              enum:
                - JSON
            value:
              type: string
          required:
            - type
            - value
        workflow_headers:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
              value:
                type: string
            required:
              - name
              - value
        auth_workflow_headers:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
              value:
                type: string
            required:
              - name
              - value
        eval_model:
          type: string
        top_p:
          type: number
          format: double
        frequency_penalty:
          type: number
          format: double
        presence_penalty:
          type: number
          format: double
        max_tokens:
          type: number
          format: double
        id:
          type: string
          maxLength: 100
          minLength: 3
          pattern: ^[a-zA-Z0-9_\-.]*$
          description: The Prompt Version name ID
        description:
          type: string
          maxLength: 1000
      required:
        - name
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