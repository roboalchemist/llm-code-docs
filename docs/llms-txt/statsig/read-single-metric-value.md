# Source: https://docs.statsig.com/api-reference/metrics/read-single-metric-value.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Single Metric Value



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/metrics
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
  /console/v1/metrics:
    get:
      tags:
        - Metrics
        - Metrics
      summary: Read Single Metric Value
      parameters:
        - name: id
          required: true
          in: query
          description: The unique identifier of the metric with format <metric_id>::<type>
          schema:
            type: string
        - name: date
          required: true
          in: query
          description: Expected valid date in the form of YYYY-MM-DD
          schema:
            example: '2024-01-01'
            type: string
      responses:
        '200':
          description: Get metric data on given date response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/MetricValuesDto'
                example:
                  message: Metric read successfully.
                  data:
                    - value: 0
                      unit_type: overall
                      numerator: null
                      denominator: null
                      metric_name: TestMetricCapi
                      metric_type: sum
                    - value: 0
                      unit_type: userID
                      numerator: null
                      denominator: null
                      metric_name: TestMetricCapi
                      metric_type: sum
              example:
                message: Metric read successfully.
                data:
                  - value: 0
                    unit_type: overall
                    numerator: null
                    denominator: null
                    metric_name: TestMetricCapi
                    metric_type: sum
                  - value: 0
                    unit_type: userID
                    numerator: null
                    denominator: null
                    metric_name: TestMetricCapi
                    metric_type: sum
        '401':
          description: >-
            This endpoint only accepts an active CONSOLE key, but an invalid key
            was sent. Key: console-xxxXXXxxxXXXxxx
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: integer
                    enum:
                      - 401
                  message:
                    type: string
                required:
                  - status
                  - message
              examples:
                Invalid Endpoint:
                  value:
                    status: 401
                    message: >-
                      This endpoint only accepts an active CONSOLE key, but an
                      invalid key was sent. Key: console-xxxXXXxxxXXXxxx
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
    MetricValuesDto:
      type: object
      properties:
        value:
          type: number
          description: Metric value for the given unit_type
          format: double
        unit_type:
          type: string
          description: 'Unit of the metric: stableID, userID, and other custom ids'
        row_count:
          type: number
          description: Row count for imported metric, optional
          format: double
        numerator:
          type: number
          description: Numerator of a ratio metric, optional
          format: double
        denominator:
          type: number
          description: Denominator of a ratio metric, optional
          format: double
      required:
        - value
        - unit_type
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