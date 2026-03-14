# Source: https://docs.statsig.com/api-reference/keys/list-keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Keys



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/keys
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
    get:
      tags:
        - Keys
      summary: List Keys
      parameters:
        - name: primaryTargetApp
          required: false
          in: query
          schema:
            type: string
        - name: environment
          required: false
          in: query
          schema:
            type: string
        - name: limit
          required: false
          in: query
          description: Results per page
          schema:
            example: 10
            oneOf:
              - type: string
              - type: number
            type: integer
        - name: page
          required: false
          in: query
          description: Page number
          schema:
            example: 1
            oneOf:
              - type: string
              - type: number
            type: integer
      responses:
        '200':
          description: Keys listed successfully
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/KeyDto'
                example:
                  message: Keys listed successfully.
                  data:
                    - key: secret-123
                      type: SERVER
                      description: Server secret key
                      scopes: []
                      environments:
                        - production
                      primaryTargetApp: primaryApp
                      secondaryTargetApps:
                        - secondaryApp
                      status: active
                    - key: console-123
                      type: CONSOLE
                      description: Console API key
                      scopes:
                        - omni_read_write
                        - can_access_keys
                      status: active
              example:
                message: Keys listed successfully.
                data:
                  - key: secret-123
                    type: SERVER
                    description: Server secret key
                    scopes: []
                    environments:
                      - production
                    primaryTargetApp: primaryApp
                    secondaryTargetApps:
                      - secondaryApp
                    status: active
                  - key: console-123
                    type: CONSOLE
                    description: Console API key
                    scopes:
                      - omni_read_write
                      - can_access_keys
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
    PaginationResponseWithMessage:
      type: object
      properties:
        message:
          type: string
          description: A simple string explaining the result of the operation.
        data:
          description: Array of results returned by pagination limit.
          type: array
          items:
            type: object
        pagination:
          description: Pagination metadata for checking if there is next page for example.
          allOf:
            - $ref: '#/components/schemas/PaginationResponseMetadataDto'
      required:
        - message
        - data
        - pagination
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
    PaginationResponseMetadataDto:
      type: object
      properties:
        itemsPerPage:
          type: number
          format: double
        pageNumber:
          type: number
          format: double
        nextPage:
          type: string
          nullable: true
        previousPage:
          type: string
          nullable: true
        totalItems:
          type: number
          format: double
        all:
          type: string
      required:
        - itemsPerPage
        - pageNumber
        - nextPage
        - previousPage
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).