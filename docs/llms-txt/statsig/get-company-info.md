# Source: https://docs.statsig.com/api-reference/company/get-company-info.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Company Info



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/company
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
  /console/v1/company:
    get:
      tags:
        - Company
      summary: Get Company Info
      parameters: []
      responses:
        '200':
          description: Get company info response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/CompanyInfoResponseDto'
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
    CompanyInfoResponseDto:
      type: object
      properties:
        companyID:
          type: string
        companyName:
          type: string
        isWarehouseNative:
          type: boolean
        orgID:
          type: string
          nullable: true
        orgName:
          type: string
          nullable: true
        resultsUpTo:
          type: number
          format: double
      required:
        - companyID
        - companyName
        - isWarehouseNative
        - orgID
        - orgName
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).