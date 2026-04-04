# Source: https://docs.statsig.com/api-reference/dashboards/read-dashboard.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Dashboard



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/dashboards/{id}
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
  /console/v1/dashboards/{id}:
    get:
      tags:
        - Dashboards
      summary: Read Dashboard
      parameters:
        - name: id
          required: true
          in: path
          description: id
          schema:
            type: string
      responses:
        '200':
          description: Read dashboard response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/DashboardReadResponseDto'
                example:
                  message: Dashboard Read Successfully
                  data:
                    id: dashboard_id
                    name: My Dashboard
                    description: desc
                    defaults:
                      date:
                        value: 14
                        unit: day
                      granularity: daily
                    widgets:
                      - type: header
                        title: Overview
                        width: 12
                        height: 1
              example:
                message: Dashboard Read Successfully
                data:
                  id: dashboard_id
                  name: My Dashboard
                  description: desc
                  defaults:
                    date:
                      value: 14
                      unit: day
                    granularity: daily
                  widgets:
                    - type: header
                      title: Overview
                      width: 12
                      height: 1
        '400':
          description: Invalid request. Please check the request input and try again.
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: integer
                    enum:
                      - 400
                  message:
                    type: string
                required:
                  - status
                  - message
              examples:
                Invalid Request:
                  value:
                    status: 400
                    message: >-
                      Invalid request. Please check the request input and try
                      again.
        '404':
          description: Not Found. The requested resource could not be found.
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
  schemas:
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
    DashboardReadResponseDto:
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
        id:
          type: string
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
              - type: object
                properties:
                  type:
                    type: string
                    enum:
                      - unsupported
                  title:
                    type: string
                  description:
                    type: string
                  color:
                    type: string
                  reason:
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
                  - reason
                additionalProperties: false
      required:
        - name
        - id
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).