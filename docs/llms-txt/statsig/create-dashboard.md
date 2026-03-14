# Source: https://docs.statsig.com/api-reference/dashboards/create-dashboard.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Dashboard



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/dashboards
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
  /console/v1/dashboards:
    post:
      tags:
        - Dashboards
      summary: Create Dashboard
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateDashboardDto'
      responses:
        '200':
          description: Create dashboard response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/DashboardCreateResponseDto'
                example:
                  message: Dashboard Created Successfully
                  data:
                    id: dashboard_id
              example:
                message: Dashboard Created Successfully
                data:
                  id: dashboard_id
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    CreateDashboardDto:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          maxLength: 200
        description:
          type: string
          maxLength: 10000
        defaults:
          type: object
          properties:
            date:
              type: object
              properties:
                value:
                  type: integer
                  minimum: 0
                  exclusiveMinimum: true
                  format: int64
                unit:
                  type: string
                  enum:
                    - day
                    - week
                    - month
              required:
                - value
                - unit
            granularity:
              type: string
              enum:
                - auto
                - daily
                - weekly
                - monthly
          additionalProperties: false
        widgets:
          type: array
          items:
            discriminator:
              propertyName: type
            oneOf:
              - type: object
                properties:
                  type:
                    type: string
                    enum:
                      - text
                  title:
                    type: string
                  content:
                    type: string
                  width:
                    type: integer
                    minimum: 0
                    exclusiveMinimum: true
                    maximum: 12
                  height:
                    type: integer
                    minimum: 0
                    exclusiveMinimum: true
                required:
                  - type
                  - title
                  - content
                additionalProperties: false
              - type: object
                properties:
                  type:
                    type: string
                    enum:
                      - header
                  title:
                    type: string
                  color:
                    type: string
                  width:
                    type: integer
                    minimum: 0
                    exclusiveMinimum: true
                    maximum: 12
                  height:
                    type: integer
                    minimum: 0
                    exclusiveMinimum: true
                required:
                  - type
                  - title
                additionalProperties: false
              - type: object
                properties:
                  type:
                    type: string
                    enum:
                      - timeseries
                  title:
                    type: string
                  description:
                    type: string
                  color:
                    type: string
                  query:
                    type: object
                    properties:
                      source:
                        type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - event
                          event_name:
                            type: string
                          filters:
                            type: array
                            items:
                              type: object
                              properties:
                                property:
                                  type: object
                                  properties:
                                    key:
                                      type: string
                                    column: {}
                                  required:
                                    - key
                                    - column
                                  additionalProperties: false
                                operator: {}
                                values:
                                  default: []
                                  type: array
                                  items:
                                    type: string
                              required:
                                - property
                                - operator
                              additionalProperties: false
                        required:
                          - type
                          - event_name
                        additionalProperties: false
                      sources:
                        type: array
                        items:
                          type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - event
                            event_name:
                              type: string
                            filters:
                              type: array
                              items:
                                type: object
                                properties:
                                  property:
                                    type: object
                                    properties:
                                      key:
                                        type: string
                                      column: {}
                                    required:
                                      - key
                                      - column
                                    additionalProperties: false
                                  operator: {}
                                  values:
                                    default: []
                                    type: array
                                    items:
                                      type: string
                                required:
                                  - property
                                  - operator
                                additionalProperties: false
                          required:
                            - type
                            - event_name
                          additionalProperties: false
                      aggregation:
                        type: object
                        properties:
                          type: {}
                          property:
                            type: object
                            properties:
                              key:
                                type: string
                              column: {}
                            required:
                              - key
                              - column
                            additionalProperties: false
                        required:
                          - type
                        additionalProperties: false
                      unit_type:
                        type: string
                      group_bys:
                        type: array
                        items:
                          type: object
                          properties:
                            key:
                              type: string
                            column: {}
                          required:
                            - key
                            - column
                          additionalProperties: false
                      viz:
                        type: object
                        properties:
                          chart_type: {}
                        required:
                          - chart_type
                        additionalProperties: false
                    required:
                      - aggregation
                    additionalProperties: false
                  width:
                    type: integer
                    minimum: 0
                    exclusiveMinimum: true
                    maximum: 12
                  height:
                    type: integer
                    minimum: 0
                    exclusiveMinimum: true
                required:
                  - type
                  - title
                  - query
                additionalProperties: false
              - type: object
                properties:
                  type:
                    type: string
                    enum:
                      - funnel
                  title:
                    type: string
                  description:
                    type: string
                  color:
                    type: string
                  query:
                    type: object
                    properties:
                      steps:
                        type: array
                        items:
                          type: object
                          properties:
                            event_name:
                              type: string
                            filters:
                              type: array
                              items:
                                type: object
                                properties:
                                  property:
                                    type: object
                                    properties:
                                      key:
                                        type: string
                                      column: {}
                                    required:
                                      - key
                                      - column
                                    additionalProperties: false
                                  operator: {}
                                  values:
                                    default: []
                                    type: array
                                    items:
                                      type: string
                                required:
                                  - property
                                  - operator
                                additionalProperties: false
                          required:
                            - event_name
                          additionalProperties: false
                        minItems: 2
                      unit_type:
                        type: string
                      conversion_window:
                        type: object
                        properties:
                          value:
                            type: integer
                            minimum: 0
                            exclusiveMinimum: true
                          unit:
                            type: string
                            enum:
                              - second
                              - minute
                              - hour
                              - day
                        required:
                          - value
                          - unit
                        additionalProperties: false
                      chart_type:
                        type: string
                        enum:
                          - conversion-rate
                          - conversions
                    required:
                      - steps
                    additionalProperties: false
                  width:
                    type: integer
                    minimum: 0
                    exclusiveMinimum: true
                    maximum: 12
                  height:
                    type: integer
                    minimum: 0
                    exclusiveMinimum: true
                required:
                  - type
                  - title
                  - query
                additionalProperties: false
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
    DashboardCreateResponseDto:
      type: object
      properties:
        id:
          type: string
      required:
        - id
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).