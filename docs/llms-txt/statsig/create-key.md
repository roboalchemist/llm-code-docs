# Source: https://docs.statsig.com/api-reference/keys/create-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Key



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/keys
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
  /console/v1/keys:
    post:
      tags:
        - Keys
      summary: Create Key
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/KeyCreateContractDto'
      responses:
        '200':
          description: Key created successfully
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/KeyDto'
                example:
                  message: Key created successfully.
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
                message: Key created successfully.
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
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    KeyCreateContractDto:
      type: object
      properties:
        description:
          type: string
          maxLength: 1000
        type:
          type: string
          enum:
            - SERVER
            - CLIENT
            - CONSOLE
            - SCIM
            - ORG
        scopes:
          type: array
          items:
            type: string
            enum:
              - omni_read_only
              - omni_read_write
              - client_download_config_specs
              - none_hash_enabled
              - can_access_keys
              - client_can_write_user_store
              - personal_read_only
              - personal_read_write
        environments:
          type: array
          items:
            type: string
        targetAppID:
          type: string
        secondaryTargetAppIDs:
          type: array
          items:
            type: string
      required:
        - description
        - type
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
    KeyDto:
      type: object
      properties:
        key:
          type: string
          nullable: true
        type:
          type: string
          enum:
            - SERVER
            - CLIENT
            - CONSOLE
            - SCIM
            - ORG
        description:
          type: string
        scopes:
          type: array
          items:
            type: string
            enum:
              - omni_read_only
              - omni_read_write
              - client_download_config_specs
              - none_hash_enabled
              - can_access_keys
              - client_can_write_user_store
              - personal_read_only
              - personal_read_write
        environments:
          type: array
          items:
            type: string
        primaryTargetApp:
          type: string
          nullable: true
        secondaryTargetApps:
          type: array
          items:
            type: string
          nullable: true
        status:
          type: string
          enum:
            - active
            - deactivated
        lastUsed:
          type: string
          nullable: true
      required:
        - key
        - type
        - description
        - scopes
        - status
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).