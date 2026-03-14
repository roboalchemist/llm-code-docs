# Source: https://docs.statsig.com/api-reference/segments/add-ids-to-user-store-id-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add IDs to User Store ID List

> This endpoint has a limit of 1000 ids per request



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json patch /console/v1/segments/{id}/add_ids
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
  /console/v1/segments/{id}/add_ids:
    patch:
      tags:
        - Segments
      summary: Add IDs to User Store ID List
      description: This endpoint has a limit of 1000 ids per request
      parameters:
        - name: id
          required: true
          in: path
          description: id
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SegmentIDListUserStoreContractDto'
      responses:
        '200':
          description: User Store ID List updated successfully.
          content:
            application/json:
              schema:
                properties:
                  message:
                    type: string
                example:
                  message: IDs successfully added to Segment ID List
              example:
                message: IDs successfully added to Segment ID List
        '400':
          description: >-
            Segment must be of type 'user_store_id_list' to be modified on this
            endpoint
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
          description: Segment not found.
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
    SegmentIDListUserStoreContractDto:
      type: object
      properties:
        ids:
          type: array
          items:
            type: string
          maxItems: 1000
        version:
          type: number
          format: double
      required:
        - ids
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).