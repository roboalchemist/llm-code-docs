# Source: https://docs.statsig.com/api-reference/alerts/list-topline-alerts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Topline Alerts



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/alerts
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
  /console/v1/alerts:
    get:
      tags:
        - Alerts
      summary: List Topline Alerts
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
          description: List Alerts success response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/AlertSchemaDto'
        '403':
          description: Forbidden resource
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: number
                    enum:
                      - 403
                  message:
                    type: string
                    enum:
                      - Forbidden resource
                required:
                  - status
                  - message
              examples:
                Forbidden resource:
                  value:
                    status: 403
                    message: Forbidden resource
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
    AlertSchemaDto:
      type: object
      properties:
        id:
          type: string
          description: ID of the alert
        name:
          type: string
          description: Name of the alert
        alertType:
          type: string
          enum:
            - threshold
            - change
            - pct_change
          description: Type of alert
        metrics:
          type: object
          properties: {}
          description: List of metrics associated with this alert
        metricGroupBys:
          type: object
          properties: {}
          description: Metric groupbys
        formula:
          type: string
          description: Formula for the alert
        message:
          type: string
          description: Alert message
        creatorID:
          type: string
        companyID:
          type: string
        priority:
          type: string
          enum:
            - P0
            - P1
            - P2
            - P3
            - P4
            - P5
          description: Priority of this alert
        alertThreshold:
          type: number
          format: double
        warningThreshold:
          type: number
          format: double
        windowMs:
          type: number
          description: >-
            How far back and how frequently a metric should be checked, in
            milliseconds
          format: double
        condition:
          type: string
          enum:
            - greater
            - greater_or_equal
            - less
            - less_or_equal
            - equal
            - not_equal
          description: >-
            Condition under which a metric change triggers an alert in
            milliseconds
        renotificationConditions:
          type: array
          items:
            type: string
            enum:
              - raise
              - warn
              - no-data
          description: Condition under which a re-notification is sent
        renotificationWindowMs:
          type: number
          description: How long to wait before re-notifying in milliseconds
          format: double
        renotificationMessage:
          type: string
          description: Re-notification message
        team:
          type: string
          nullable: true
          description: Team associated with this alert
        tags:
          type: array
          items:
            type: string
          description: Tags associated with this alert
      required:
        - id
        - name
        - alertType
        - metrics
        - metricGroupBys
        - message
        - companyID
        - priority
        - alertThreshold
        - windowMs
        - condition
        - tags
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