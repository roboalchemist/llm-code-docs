# Source: https://docs.statsig.com/api-reference/metrics/list-all-metric-values.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List All Metric Values

> List all metric values



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/metrics/values
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
  /console/v1/metrics/values:
    get:
      tags:
        - Metrics
      summary: List All Metric Values
      description: List all metric values
      parameters:
        - name: date
          required: true
          in: query
          description: Expected valid date in the form of YYYY-MM-DD
          schema:
            example: '2024-01-01'
            type: string
        - name: metricName
          required: false
          in: query
          schema:
            type: string
        - name: metricType
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
          description: List All Metric Values Response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/MetricValueDto'
                example:
                  message: Metric values listed successfully.
                  data:
                    - value: 21377
                      unitType: overall
                      numerator: null
                      denominator: null
                      metricName: Page Loads
                      metricType: event_count_custom
                    - value: 21377
                      unitType: stableID
                      numerator: null
                      denominator: null
                      metricName: Page Loads
                      metricType: event_count_custom
                    - value: 21355
                      unitType: userID
                      numerator: null
                      denominator: null
                      metricName: Page Loads
                      metricType: event_count_custom
                    - value: 646524
                      unitType: stableID
                      numerator: null
                      denominator: null
                      metricName: Average Time Spent on Page
                      metricType: event_user
                    - value: 5676
                      unitType: stableID
                      numerator: null
                      denominator: null
                      metricName: Page Latency
                      metricType: mean
                  pagination:
                    itemsPerPage: 5
                    pageNumber: 1
                    totalItems: 5767
                    nextPage: /console/v1/metrics/values?date=2024-02-04&page=2&limit=5
                    previousPage: null
              example:
                message: Metric values listed successfully.
                data:
                  - value: 21377
                    unitType: overall
                    numerator: null
                    denominator: null
                    metricName: Page Loads
                    metricType: event_count_custom
                  - value: 21377
                    unitType: stableID
                    numerator: null
                    denominator: null
                    metricName: Page Loads
                    metricType: event_count_custom
                  - value: 21355
                    unitType: userID
                    numerator: null
                    denominator: null
                    metricName: Page Loads
                    metricType: event_count_custom
                  - value: 646524
                    unitType: stableID
                    numerator: null
                    denominator: null
                    metricName: Average Time Spent on Page
                    metricType: event_user
                  - value: 5676
                    unitType: stableID
                    numerator: null
                    denominator: null
                    metricName: Page Latency
                    metricType: mean
                pagination:
                  itemsPerPage: 5
                  pageNumber: 1
                  totalItems: 5767
                  nextPage: /console/v1/metrics/values?date=2024-02-04&page=2&limit=5
                  previousPage: null
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
    MetricValueDto:
      type: object
      properties:
        value:
          type: number
          format: double
        unitType:
          type: string
        numerator:
          type: number
          format: double
        denominator:
          type: number
          format: double
        inputRows:
          type: number
          format: double
        metricName:
          type: string
        metricType:
          type: string
        displayName:
          type: string
      required:
        - value
        - unitType
        - metricName
        - metricType
        - displayName
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