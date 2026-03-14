# Source: https://docs.statsig.com/api-reference/events/get-specific-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get specific events



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/events/{eventName}
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
  /console/v1/events/{eventName}:
    get:
      tags:
        - Events
      summary: Get specific events
      parameters:
        - name: eventName
          required: true
          in: path
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
          description: Get specific events response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/LoggedEventDto'
                example:
                  message: Event values listed successfully.
                  data:
                    - timestamp: '1720567904601'
                      name: add_to_cart
                      source: statsig-node
                      value: appliances
                      userID: '3411'
                      metadata: {}
                    - timestamp: '1720567904594'
                      name: add_to_cart
                      source: statsig-node
                      value: sports
                      userID: '1037'
                      metadata: {}
                    - timestamp: '1720567904307'
                      name: add_to_cart
                      source: statsig-node
                      value: ''
                      userID: '5056'
                      metadata: {}
                    - timestamp: '1720567904299'
                      name: add_to_cart
                      source: statsig-node
                      value: books
                      userID: '7326'
                      metadata: {}
                    - timestamp: '1720567904288'
                      name: add_to_cart
                      source: statsig-node
                      value: books
                      userID: '166'
                      metadata: {}
                    - timestamp: '1720567904310'
                      name: add_to_cart
                      source: statsig-node
                      value: office products
                      userID: '3255'
                      metadata: {}
                    - timestamp: '1720567904299'
                      name: add_to_cart
                      source: statsig-node
                      value: sports
                      userID: '8598'
                      metadata: {}
                  pagination:
                    itemsPerPage: 7
                    pageNumber: 1
                    totalItems: 100
                    nextPage: /console/v1/events/add_to_cart?page=2&limit=7
                    previousPage: null
                    all: /console/v1/events/add_to_cart
              example:
                message: Event values listed successfully.
                data:
                  - timestamp: '1720567904601'
                    name: add_to_cart
                    source: statsig-node
                    value: appliances
                    userID: '3411'
                    metadata: {}
                  - timestamp: '1720567904594'
                    name: add_to_cart
                    source: statsig-node
                    value: sports
                    userID: '1037'
                    metadata: {}
                  - timestamp: '1720567904307'
                    name: add_to_cart
                    source: statsig-node
                    value: ''
                    userID: '5056'
                    metadata: {}
                  - timestamp: '1720567904299'
                    name: add_to_cart
                    source: statsig-node
                    value: books
                    userID: '7326'
                    metadata: {}
                  - timestamp: '1720567904288'
                    name: add_to_cart
                    source: statsig-node
                    value: books
                    userID: '166'
                    metadata: {}
                  - timestamp: '1720567904310'
                    name: add_to_cart
                    source: statsig-node
                    value: office products
                    userID: '3255'
                    metadata: {}
                  - timestamp: '1720567904299'
                    name: add_to_cart
                    source: statsig-node
                    value: sports
                    userID: '8598'
                    metadata: {}
                pagination:
                  itemsPerPage: 7
                  pageNumber: 1
                  totalItems: 100
                  nextPage: /console/v1/events/add_to_cart?page=2&limit=7
                  previousPage: null
                  all: /console/v1/events/add_to_cart
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
    LoggedEventDto:
      type: object
      properties:
        timestamp:
          type: string
          description: The timestamp when the event occurred, represented as a string.
        name:
          type: string
          description: The name of the event (e.g., "add_to_cart").
        source:
          type: string
          description: The source of the event, indicating where it was triggered from.
        value:
          type: string
          description: The value associated with the event, providing additional context.
        userID:
          type: string
          description: The ID of the user who triggered the event.
      required:
        - timestamp
        - name
        - source
        - value
        - userID
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