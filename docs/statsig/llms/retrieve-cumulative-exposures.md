# Source: https://docs.statsig.com/api-reference/experiments/retrieve-cumulative-exposures.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve cumulative exposures



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/experiments/{id}/cumulative_exposures
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
  /console/v1/experiments/{id}/cumulative_exposures:
    get:
      tags:
        - Experiments
        - Experiments
      summary: Retrieve cumulative exposures
      parameters:
        - name: id
          required: true
          in: path
          description: id
          schema:
            type: string
      responses:
        '200':
          description: Get cumulative exposures success
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/CumulativeExposureResponseDto'
                example:
                  message: Successfully loaded Cumulative Exposures
                  data:
                    - groupID: 6pY4WNHgJu1sqAyApUZuaa
                      groupName: Daily Deals
                      results:
                        - date: '2024-12-23'
                          exposures: 0
                        - date: '2024-12-24'
                          exposures: 7407
                        - date: '2024-12-25'
                          exposures: 10237
                        - date: '2024-12-26'
                          exposures: 10725
                        - date: '2024-12-27'
                          exposures: 10906
                        - date: '2024-12-28'
                          exposures: 11061
                        - date: '2024-12-29'
                          exposures: 11251
                        - date: '2024-12-30'
                          exposures: 11412
                    - groupID: 6pY4WPmjbMaWK06w12V7tc
                      groupName: Items You May Like
                      results:
                        - date: '2024-12-23'
                          exposures: 0
                        - date: '2024-12-24'
                          exposures: 7392
                        - date: '2024-12-25'
                          exposures: 10239
                        - date: '2024-12-26'
                          exposures: 10732
                        - date: '2024-12-27'
                          exposures: 10934
                        - date: '2024-12-28'
                          exposures: 11108
                        - date: '2024-12-29'
                          exposures: 11287
                        - date: '2024-12-30'
                          exposures: 11455
                    - groupID: 6pY4WR1lE4kr3pErCaQKMe
                      groupName: Buy Again
                      results:
                        - date: '2024-12-23'
                          exposures: 0
                        - date: '2024-12-24'
                          exposures: 7475
                        - date: '2024-12-25'
                          exposures: 10289
                        - date: '2024-12-26'
                          exposures: 10774
                        - date: '2024-12-27'
                          exposures: 10975
                        - date: '2024-12-28'
                          exposures: 11168
                        - date: '2024-12-29'
                          exposures: 11321
                        - date: '2024-12-30'
                          exposures: 11483
              example:
                message: Successfully loaded Cumulative Exposures
                data:
                  - groupID: 6pY4WNHgJu1sqAyApUZuaa
                    groupName: Daily Deals
                    results:
                      - date: '2024-12-23'
                        exposures: 0
                      - date: '2024-12-24'
                        exposures: 7407
                      - date: '2024-12-25'
                        exposures: 10237
                      - date: '2024-12-26'
                        exposures: 10725
                      - date: '2024-12-27'
                        exposures: 10906
                      - date: '2024-12-28'
                        exposures: 11061
                      - date: '2024-12-29'
                        exposures: 11251
                      - date: '2024-12-30'
                        exposures: 11412
                  - groupID: 6pY4WPmjbMaWK06w12V7tc
                    groupName: Items You May Like
                    results:
                      - date: '2024-12-23'
                        exposures: 0
                      - date: '2024-12-24'
                        exposures: 7392
                      - date: '2024-12-25'
                        exposures: 10239
                      - date: '2024-12-26'
                        exposures: 10732
                      - date: '2024-12-27'
                        exposures: 10934
                      - date: '2024-12-28'
                        exposures: 11108
                      - date: '2024-12-29'
                        exposures: 11287
                      - date: '2024-12-30'
                        exposures: 11455
                  - groupID: 6pY4WR1lE4kr3pErCaQKMe
                    groupName: Buy Again
                    results:
                      - date: '2024-12-23'
                        exposures: 0
                      - date: '2024-12-24'
                        exposures: 7475
                      - date: '2024-12-25'
                        exposures: 10289
                      - date: '2024-12-26'
                        exposures: 10774
                      - date: '2024-12-27'
                        exposures: 10975
                      - date: '2024-12-28'
                        exposures: 11168
                      - date: '2024-12-29'
                        exposures: 11321
                      - date: '2024-12-30'
                        exposures: 11483
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
    CumulativeExposureResponseDto:
      type: array
      items:
        type: object
        properties:
          groupID:
            type: string
          groupName:
            type: string
          results:
            type: array
            items:
              type: object
              properties:
                date:
                  type: string
                exposures:
                  type: number
              required:
                - date
                - exposures
        required:
          - groupID
          - groupName
          - results
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).