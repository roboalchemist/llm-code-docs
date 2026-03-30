# Source: https://docs.statsig.com/api-reference/param-store/list-param-stores.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Param Stores



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/param_stores
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
  /console/v1/param_stores:
    get:
      tags:
        - Param Store
      summary: List Param Stores
      parameters:
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
          description: List param stores
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/ParamStoreDto'
                example:
                  message: List param stores success
                  data:
                    - id: 6O13wytnLL1Lss5QgUSAeu
                      name: param 1
                      displayName: param 1
                      description: ''
                      createdTime: 1734618662756
                      creatorID: 5O908pyGoCqw6QH1nt8v82
                      lastModifierID: 5O908pyGoCqw6QH1nt8v82
                      parameters:
                        - name: prm1
                          ref_type: static
                          param_type: boolean
                          value: false
                        - name: prm2
                          ref_type: static
                          param_type: boolean
                          value: false
                    - id: 24hiIXz3kbFaDwtYEetv2i
                      name: param 2
                      displayName: param 1
                      description: ''
                      createdTime: 1734618662756
                      creatorID: 5O908pyGoCqw6QH1nt8v82
                      lastModifierID: 5O908pyGoCqw6QH1nt8v82
                      parameters:
                        - name: prm1
                          ref_type: static
                          param_type: boolean
                          value: false
                        - name: prm2
                          ref_type: static
                          param_type: boolean
                          value: false
              example:
                message: List param stores success
                data:
                  - id: 6O13wytnLL1Lss5QgUSAeu
                    name: param 1
                    displayName: param 1
                    description: ''
                    createdTime: 1734618662756
                    creatorID: 5O908pyGoCqw6QH1nt8v82
                    lastModifierID: 5O908pyGoCqw6QH1nt8v82
                    parameters:
                      - name: prm1
                        ref_type: static
                        param_type: boolean
                        value: false
                      - name: prm2
                        ref_type: static
                        param_type: boolean
                        value: false
                  - id: 24hiIXz3kbFaDwtYEetv2i
                    name: param 2
                    displayName: param 1
                    description: ''
                    createdTime: 1734618662756
                    creatorID: 5O908pyGoCqw6QH1nt8v82
                    lastModifierID: 5O908pyGoCqw6QH1nt8v82
                    parameters:
                      - name: prm1
                        ref_type: static
                        param_type: boolean
                        value: false
                      - name: prm2
                        ref_type: static
                        param_type: boolean
                        value: false
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
    ParamStoreDto:
      type: object
      properties:
        id:
          type: string
          description: Param Store ID
        name:
          type: string
          description: Param Store Name
        displayName:
          type: string
          description: Param Store Display Name
        description:
          type: string
          description: Param Store Description
        createdTime:
          type: number
          description: Param Store Creation Time
          format: double
        creatorID:
          type: string
          description: Creator ID
        lastModifierID:
          type: string
          description: Last Modifier ID
        team:
          type: string
          nullable: true
          description: Team Name
        teamID:
          type: string
          description: Team ID
        parameters:
          type: array
          items:
            oneOf:
              - type: object
                properties:
                  ref_type:
                    type: string
                    enum:
                      - static
                  name:
                    type: string
                    description: Parameter Name
                  param_type:
                    type: string
                    enum:
                      - boolean
                  value:
                    type: boolean
                required:
                  - ref_type
                  - name
                  - param_type
                  - value
              - type: object
                properties:
                  ref_type:
                    type: string
                    enum:
                      - static
                  name:
                    type: string
                    description: Parameter Name
                  param_type:
                    type: string
                    enum:
                      - number
                  value:
                    type: number
                required:
                  - ref_type
                  - name
                  - param_type
                  - value
              - type: object
                properties:
                  ref_type:
                    type: string
                    enum:
                      - static
                  name:
                    type: string
                    description: Parameter Name
                  param_type:
                    type: string
                    enum:
                      - string
                  value:
                    type: string
                required:
                  - ref_type
                  - name
                  - param_type
                  - value
              - type: object
                properties:
                  ref_type:
                    type: string
                    enum:
                      - static
                  name:
                    type: string
                    description: Parameter Name
                  param_type:
                    type: string
                    enum:
                      - object
                  value:
                    type: object
                    additionalProperties: {}
                required:
                  - ref_type
                  - name
                  - param_type
                  - value
              - type: object
                properties:
                  ref_type:
                    type: string
                    enum:
                      - static
                  name:
                    type: string
                    description: Parameter Name
                  param_type:
                    type: string
                    enum:
                      - array
                  value:
                    type: array
                    items: {}
                required:
                  - ref_type
                  - name
                  - param_type
                  - value
              - type: object
                properties:
                  ref_type:
                    type: string
                    enum:
                      - gate
                  name:
                    type: string
                    description: Parameter Name
                  gate_name:
                    type: string
                    description: Gate Name
                  param_type:
                    type: string
                    enum:
                      - boolean
                  pass_value:
                    type: boolean
                  fail_value:
                    type: boolean
                required:
                  - ref_type
                  - name
                  - gate_name
                  - param_type
                  - pass_value
                  - fail_value
              - type: object
                properties:
                  ref_type:
                    type: string
                    enum:
                      - gate
                  name:
                    type: string
                    description: Parameter Name
                  gate_name:
                    type: string
                    description: Gate Name
                  param_type:
                    type: string
                    enum:
                      - number
                  pass_value:
                    type: number
                  fail_value:
                    type: number
                required:
                  - ref_type
                  - name
                  - gate_name
                  - param_type
                  - pass_value
                  - fail_value
              - type: object
                properties:
                  ref_type:
                    type: string
                    enum:
                      - gate
                  name:
                    type: string
                    description: Parameter Name
                  gate_name:
                    type: string
                    description: Gate Name
                  param_type:
                    type: string
                    enum:
                      - string
                  pass_value:
                    type: string
                  fail_value:
                    type: string
                required:
                  - ref_type
                  - name
                  - gate_name
                  - param_type
                  - pass_value
                  - fail_value
              - type: object
                properties:
                  ref_type:
                    type: string
                    enum:
                      - gate
                  name:
                    type: string
                    description: Parameter Name
                  gate_name:
                    type: string
                    description: Gate Name
                  param_type:
                    type: string
                    enum:
                      - object
                  pass_value:
                    type: object
                    additionalProperties: {}
                  fail_value:
                    type: object
                    additionalProperties: {}
                required:
                  - ref_type
                  - name
                  - gate_name
                  - param_type
                  - pass_value
                  - fail_value
              - type: object
                properties:
                  ref_type:
                    type: string
                    enum:
                      - gate
                  name:
                    type: string
                    description: Parameter Name
                  gate_name:
                    type: string
                    description: Gate Name
                  param_type:
                    type: string
                    enum:
                      - array
                  pass_value:
                    type: array
                    items: {}
                  fail_value:
                    type: array
                    items: {}
                required:
                  - ref_type
                  - name
                  - gate_name
                  - param_type
                  - pass_value
                  - fail_value
              - type: object
                properties:
                  ref_type:
                    type: string
                    enum:
                      - layer
                  name:
                    type: string
                    description: Parameter Name
                  param_type:
                    type: string
                    enum:
                      - string
                      - boolean
                      - number
                      - array
                      - object
                    description: Parameter Type
                  layer_name:
                    type: string
                    description: Layer Name
                  param_name:
                    type: string
                    description: Parameter Name in Layer
                required:
                  - ref_type
                  - name
                  - param_type
                  - layer_name
                  - param_name
              - type: object
                properties:
                  ref_type:
                    type: string
                    enum:
                      - dynamic_config
                  name:
                    type: string
                    description: Parameter Name
                  param_type:
                    type: string
                    enum:
                      - string
                      - boolean
                      - number
                      - array
                      - object
                    description: Parameter Type
                  config_name:
                    type: string
                    description: Dynamic Config Name
                  param_name:
                    type: string
                    description: Parameter Name in Config
                required:
                  - ref_type
                  - name
                  - param_type
                  - config_name
                  - param_name
              - type: object
                properties:
                  ref_type:
                    type: string
                    enum:
                      - experiment
                  name:
                    type: string
                    description: Parameter Name
                  param_type:
                    type: string
                    enum:
                      - string
                      - boolean
                      - number
                      - array
                      - object
                    description: Parameter Type
                  experiment_name:
                    type: string
                    description: Experiment Name
                  param_name:
                    type: string
                    description: Parameter Name in Experiment
                required:
                  - ref_type
                  - name
                  - param_type
                  - experiment_name
                  - param_name
            description: Parameter Definition
          description: List of Parameters
      required:
        - id
        - name
        - displayName
        - description
        - createdTime
        - creatorID
        - lastModifierID
        - parameters
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