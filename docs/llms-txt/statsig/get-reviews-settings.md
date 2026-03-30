# Source: https://docs.statsig.com/api-reference/settings/get-reviews-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Reviews Settings



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/settings/reviews
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
  /console/v1/settings/reviews:
    get:
      tags:
        - Settings
      summary: Get Reviews Settings
      parameters: []
      responses:
        '200':
          description: Get Reviews Settings Response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/SettingsReviewsContractDto'
                example:
                  message: Settings read successfully.
                  data:
                    is_config_review_required: true
                    is_metric_review_required: true
                    is_metric_review_required_on_verified_only: false
              example:
                message: Settings read successfully.
                data:
                  is_config_review_required: true
                  is_metric_review_required: true
                  is_metric_review_required_on_verified_only: false
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
    SettingsReviewsContractDto:
      type: object
      properties:
        is_config_review_required:
          type: boolean
          description: Whether config reviews are required.
        is_metric_review_required:
          type: boolean
          description: Whether metric reviews are required.
        is_metric_review_required_on_verified_only:
          type: boolean
          description: Whether metric reviews are only required for verified metrics.
        is_whn_analysis_only_review_required:
          type: boolean
          description: >-
            Whether analysis-only experiment reviews are required. Only
            applicable to WHN projects.
        is_whn_source_review_required:
          type: boolean
          description: >-
            Whether metric/assignment/entity property source reviews are
            required. Only applicable to WHN projects.
      required:
        - is_config_review_required
        - is_metric_review_required
        - is_metric_review_required_on_verified_only
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).