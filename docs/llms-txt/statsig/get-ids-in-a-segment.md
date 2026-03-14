# Source: https://docs.statsig.com/api-reference/segments/get-ids-in-a-segment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get IDs in a Segment

> This endpoint is rate limited to 100



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/segments/{id}/id_list
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
  /console/v1/segments/{id}/id_list:
    get:
      tags:
        - Segments
      summary: Get IDs in a Segment
      description: This endpoint is rate limited to 100
      parameters:
        - name: id
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
          description: IDs read successfully
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        $ref: '#/components/schemas/IDListDto'
                example:
                  message: Segments listed successfully.
                  data:
                    name: small_id_list
                    count: 3
                    ids:
                      - 1, 2, 3
              example:
                message: Segments listed successfully.
                data:
                  name: small_id_list
                  count: 3
                  ids:
                    - 1, 2, 3
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
    IDListDto:
      type: object
      properties:
        name:
          type: string
          description: The name associated with the list of IDs
          example: Example List
        count:
          type: number
          description: The count of IDs in the list
          example: 5
          format: double
        ids:
          type: array
          items:
            type: string
          description: The array of IDs
          example:
            - id1
            - id2
            - id3
            - id4
            - id5
      required:
        - name
        - count
        - ids
      description: Schema for a list of IDs with a name and count
      example:
        name: Example List
        count: 5
        ids:
          - id1
          - id2
          - id3
          - id4
          - id5
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