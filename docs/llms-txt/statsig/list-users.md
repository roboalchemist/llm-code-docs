# Source: https://docs.statsig.com/api-reference/users/list-users.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Users



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/users
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
  /console/v1/users:
    get:
      tags:
        - Users
      summary: List Users
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
        - name: include_stale_members
          required: false
          in: query
          description: >-
            Whether to include stale company-user membership edges. Defaults to
            false, which returns only effective current members (matching the
            Settings UI).
          schema:
            example: false
            type: boolean
      responses:
        '200':
          description: List users response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/UserContractDto'
                example:
                  message: User listed successfully.
                  data:
                    - email: test@statsig.com
                      firstName: a
                      lastName: b
                      role: admin
                    - email: test@statsig.com
                      firstName: a
                      lastName: b
                      role: member
                    - email: test@statsig.com
                      firstName: test
                      lastName: ''
                      role: admin
                    - email: test@statsig.com
                      firstName: test
                      lastName: ''
                      role: member
                    - email: test@statsig.com
                      firstName: test
                      lastName: user
                      role: member
                    - email: test@statsig.com
                      firstName: test
                      lastName: user
                      role: admin
                    - email: test@statsig.com
                      firstName: test
                      lastName: user
                      role: admin
                    - email: test@statsig.com
                      firstName: test
                      lastName: user
                      role: member
                  pagination:
                    itemsPerPage: 10
                    pageNumber: 4
                    totalItems: 38
                    nextPage: null
                    previousPage: /console/v1/users?page=3&limit=10
                    all: /console/v1/users
              example:
                message: User listed successfully.
                data:
                  - email: test@statsig.com
                    firstName: a
                    lastName: b
                    role: admin
                  - email: test@statsig.com
                    firstName: a
                    lastName: b
                    role: member
                  - email: test@statsig.com
                    firstName: test
                    lastName: ''
                    role: admin
                  - email: test@statsig.com
                    firstName: test
                    lastName: ''
                    role: member
                  - email: test@statsig.com
                    firstName: test
                    lastName: user
                    role: member
                  - email: test@statsig.com
                    firstName: test
                    lastName: user
                    role: admin
                  - email: test@statsig.com
                    firstName: test
                    lastName: user
                    role: admin
                  - email: test@statsig.com
                    firstName: test
                    lastName: user
                    role: member
                pagination:
                  itemsPerPage: 10
                  pageNumber: 4
                  totalItems: 38
                  nextPage: null
                  previousPage: /console/v1/users?page=3&limit=10
                  all: /console/v1/users
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
    UserContractDto:
      type: object
      properties:
        email:
          type: string
          format: email
          description: The email address of the user.
        firstName:
          type: string
          description: The user's first name.
        lastName:
          type: string
          description: The user's last name.
        role:
          type: string
          description: >-
            The user's role, which can be 'Admin', 'Read Only', 'Member', or any
            custom role name.
      required:
        - email
        - firstName
        - lastName
        - role
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