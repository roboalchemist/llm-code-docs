# Source: https://docs.statsig.com/api-reference/ingestions/list-ingestion-runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Ingestion Runs



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/ingestion/runs
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
  /console/v1/ingestion/runs:
    get:
      tags:
        - Ingestions
      summary: List Ingestion Runs
      parameters:
        - name: page
          required: false
          in: query
          schema:
            oneOf:
              - type: string
              - type: number
      responses:
        '200':
          description: List Ingestion Runs Success
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/IngestionRunDataContractDto'
                example:
                  message: Ingestion Runs Listed Successfully.
                  data:
                    - runID: 5a09550b-75a1-4f98-908a-cd79ca729689
                      latestStatus: download_error
                      lastUpdatedAt: '2023-12-14T02:47:00.321Z'
                      createdAt: '2023-12-14T02:31:46.896Z'
                      trigger: scheduled
                      sources:
                        - Events 1
                        - Events 2
                      dateStamps:
                        - '2023-12-12'
                      runHistory:
                        - statusTimestamp: '2023-12-14T02:47:01.422Z'
                          status: download_error
                        - statusTimestamp: '2023-12-14T02:46:46.800Z'
                          status: download_started
                        - statusTimestamp: '2023-12-14T02:44:32.597Z'
                          status: download_error
                        - statusTimestamp: '2023-12-14T02:43:34.056Z'
                          status: download_started
                        - statusTimestamp: '2023-12-14T02:34:27.056Z'
                          status: started
                        - statusTimestamp: '2023-12-14T02:31:46.896Z'
                          status: enqueued
                      granularHistory:
                        - source: Events 1
                          latestSourceStatus: download_error
                          statusByDate:
                            - dateStamp: '2023-12-12'
                              statuses:
                                - statusTimestamp: '2023-12-14T02:44:30.666Z'
                                  status: download_error
                                - statusTimestamp: '2023-12-14T02:43:22.724Z'
                                  status: download_started
                                - statusTimestamp: '2023-12-14T02:34:25.325Z'
                                  status: started
                                - statusTimestamp: '2023-12-14T02:31:46.896Z'
                                  status: enqueued
                        - source: Events 2
                          latestSourceStatus: download_error
                          statusByDate:
                            - dateStamp: '2023-12-12'
                              statuses:
                                - statusTimestamp: '2023-12-14T02:44:30.666Z'
                                  status: download_error
                                - statusTimestamp: '2023-12-14T02:43:22.724Z'
                                  status: download_started
                                - statusTimestamp: '2023-12-14T02:34:25.325Z'
                                  status: started
                                - statusTimestamp: '2023-12-14T02:31:46.896Z'
                                  status: enqueued
                    - runID: 21b97020-e61a-49bf-a9f3-ce46cec50489
                      latestStatus: pulse_complete
                      lastUpdatedAt: '2023-12-14T04:18:54.603Z'
                      createdAt: '2023-12-14T02:30:27.217Z'
                      trigger: scheduled
                      sources:
                        - Metrics 1
                      dateStamps:
                        - '2023-12-12'
                      runHistory:
                        - statusTimestamp: '2023-12-14T04:18:55.556Z'
                          status: pulse_complete
                        - statusTimestamp: '2023-12-14T03:32:49.429Z'
                          status: metrics_complete
                        - statusTimestamp: '2023-12-14T03:21:40.015Z'
                          status: metrics_started
                        - statusTimestamp: '2023-12-14T03:21:33.322Z'
                          status: metrics_started
                        - statusTimestamp: '2023-12-14T03:21:27.046Z'
                          status: metrics_started
                        - statusTimestamp: '2023-12-14T03:21:15.449Z'
                          status: metrics_started
                        - statusTimestamp: '2023-12-14T02:45:17.161Z'
                          status: download_complete
                        - statusTimestamp: '2023-12-14T02:43:33.661Z'
                          status: download_started
                        - statusTimestamp: '2023-12-14T02:35:09.734Z'
                          status: started
                        - statusTimestamp: '2023-12-14T02:30:27.217Z'
                          status: enqueued
                      granularHistory:
                        - source: Metrics 1
                          latestSourceStatus: pulse_complete
                          statusByDate:
                            - dateStamp: '2023-12-12'
                              statuses:
                                - statusTimestamp: '2023-12-14T04:18:53.975Z'
                                  status: pulse_complete
                                - statusTimestamp: '2023-12-14T04:04:48.761Z'
                                  status: pulse_started
                                - statusTimestamp: '2023-12-14T03:32:48.019Z'
                                  status: metrics_complete
                                - statusTimestamp: '2023-12-14T03:21:38.667Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-14T03:21:32.039Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-14T03:21:25.385Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-14T03:21:14.383Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-14T02:45:05.125Z'
                                  status: download_complete
                                - statusTimestamp: '2023-12-14T02:43:27.013Z'
                                  status: download_started
                                - statusTimestamp: '2023-12-14T02:35:07.577Z'
                                  status: started
                                - statusTimestamp: '2023-12-14T02:30:27.217Z'
                                  status: enqueued
                    - runID: de941fa2-3e0f-44ec-a44c-5c51eed07e0d
                      latestStatus: download_error
                      lastUpdatedAt: '2023-12-13T02:44:23.790Z'
                      createdAt: '2023-12-13T02:30:55.992Z'
                      trigger: scheduled
                      sources:
                        - Events 1
                        - Events 2
                      dateStamps:
                        - '2023-12-11'
                      runHistory:
                        - statusTimestamp: '2023-12-13T02:44:24.865Z'
                          status: download_error
                        - statusTimestamp: '2023-12-13T02:44:12.421Z'
                          status: download_started
                        - statusTimestamp: '2023-12-13T02:41:48.458Z'
                          status: download_error
                        - statusTimestamp: '2023-12-13T02:40:56.694Z'
                          status: download_started
                        - statusTimestamp: '2023-12-13T02:32:35.607Z'
                          status: started
                        - statusTimestamp: '2023-12-13T02:30:55.992Z'
                          status: enqueued
                      granularHistory:
                        - source: Events 1
                          latestSourceStatus: download_error
                          statusByDate:
                            - dateStamp: '2023-12-11'
                              statuses:
                                - statusTimestamp: '2023-12-13T02:41:47.374Z'
                                  status: download_error
                                - statusTimestamp: '2023-12-13T02:40:50.210Z'
                                  status: download_started
                                - statusTimestamp: '2023-12-13T02:32:33.118Z'
                                  status: started
                                - statusTimestamp: '2023-12-13T02:30:55.992Z'
                                  status: enqueued
                        - source: Events 2
                          latestSourceStatus: download_error
                          statusByDate:
                            - dateStamp: '2023-12-11'
                              statuses:
                                - statusTimestamp: '2023-12-13T02:41:47.374Z'
                                  status: download_error
                                - statusTimestamp: '2023-12-13T02:40:50.210Z'
                                  status: download_started
                                - statusTimestamp: '2023-12-13T02:32:33.118Z'
                                  status: started
                                - statusTimestamp: '2023-12-13T02:30:55.992Z'
                                  status: enqueued
                    - runID: 93b0150f-d53a-416e-876f-bac00634a872
                      latestStatus: pulse_complete
                      lastUpdatedAt: '2023-12-13T03:47:23.504Z'
                      createdAt: '2023-12-13T02:29:32.793Z'
                      trigger: scheduled
                      sources:
                        - Metrics 1
                      dateStamps:
                        - '2023-12-11'
                      runHistory:
                        - statusTimestamp: '2023-12-13T03:47:24.548Z'
                          status: pulse_complete
                        - statusTimestamp: '2023-12-13T03:41:19.158Z'
                          status: pulse_started
                        - statusTimestamp: '2023-12-13T03:35:05.780Z'
                          status: pulse_started
                        - statusTimestamp: '2023-12-13T03:28:52.123Z'
                          status: pulse_started
                        - statusTimestamp: '2023-12-13T03:22:38.140Z'
                          status: pulse_started
                        - statusTimestamp: '2023-12-13T03:20:48.982Z'
                          status: metrics_complete
                        - statusTimestamp: '2023-12-13T03:16:40.079Z'
                          status: metrics_started
                        - statusTimestamp: '2023-12-13T03:16:31.359Z'
                          status: metrics_started
                        - statusTimestamp: '2023-12-13T03:16:23.553Z'
                          status: metrics_started
                        - statusTimestamp: '2023-12-13T03:16:08.026Z'
                          status: metrics_started
                        - statusTimestamp: '2023-12-13T02:42:52.210Z'
                          status: download_complete
                        - statusTimestamp: '2023-12-13T02:41:01.394Z'
                          status: download_started
                        - statusTimestamp: '2023-12-13T02:33:26.492Z'
                          status: started
                        - statusTimestamp: '2023-12-13T02:29:32.793Z'
                          status: enqueued
                      granularHistory:
                        - source: Metrics 1
                          latestSourceStatus: pulse_complete
                          statusByDate:
                            - dateStamp: '2023-12-11'
                              statuses:
                                - statusTimestamp: '2023-12-13T03:47:22.812Z'
                                  status: pulse_complete
                                - statusTimestamp: '2023-12-13T03:41:17.582Z'
                                  status: pulse_started
                                - statusTimestamp: '2023-12-13T03:20:47.294Z'
                                  status: metrics_complete
                                - statusTimestamp: '2023-12-13T03:16:38.421Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-13T03:16:29.827Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-13T03:16:21.847Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-13T03:16:05.864Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-13T02:42:36.220Z'
                                  status: download_complete
                                - statusTimestamp: '2023-12-13T02:40:47.890Z'
                                  status: download_started
                                - statusTimestamp: '2023-12-13T02:33:24.219Z'
                                  status: started
                                - statusTimestamp: '2023-12-13T02:29:32.793Z'
                                  status: enqueued
                    - runID: a4df397e-c816-4e39-9b1a-ab6b2e5f3811
                      latestStatus: download_error
                      lastUpdatedAt: '2023-12-12T02:43:29.739Z'
                      createdAt: '2023-12-12T02:30:41.989Z'
                      trigger: scheduled
                      sources:
                        - Events 1
                        - Events 2
                      dateStamps:
                        - '2023-12-10'
                      runHistory:
                        - statusTimestamp: '2023-12-12T02:43:30.735Z'
                          status: download_error
                        - statusTimestamp: '2023-12-12T02:43:16.318Z'
                          status: download_started
                        - statusTimestamp: '2023-12-12T02:40:56.030Z'
                          status: download_error
                        - statusTimestamp: '2023-12-12T02:39:58.147Z'
                          status: download_started
                        - statusTimestamp: '2023-12-12T02:32:18.156Z'
                          status: started
                        - statusTimestamp: '2023-12-12T02:30:41.989Z'
                          status: enqueued
                      granularHistory:
                        - source: Events 1
                          latestSourceStatus: download_error
                          statusByDate:
                            - dateStamp: '2023-12-10'
                              statuses:
                                - statusTimestamp: '2023-12-12T02:40:54.406Z'
                                  status: download_error
                                - statusTimestamp: '2023-12-12T02:39:51.150Z'
                                  status: download_started
                                - statusTimestamp: '2023-12-12T02:32:16.419Z'
                                  status: started
                                - statusTimestamp: '2023-12-12T02:30:41.989Z'
                                  status: enqueued
                        - source: Events 2
                          latestSourceStatus: download_error
                          statusByDate:
                            - dateStamp: '2023-12-10'
                              statuses:
                                - statusTimestamp: '2023-12-12T02:40:54.406Z'
                                  status: download_error
                                - statusTimestamp: '2023-12-12T02:39:51.150Z'
                                  status: download_started
                                - statusTimestamp: '2023-12-12T02:32:16.419Z'
                                  status: started
                                - statusTimestamp: '2023-12-12T02:30:41.989Z'
                                  status: enqueued
                    - runID: eedeb4c0-07dd-43d0-8014-5ac41ef7dab8
                      latestStatus: pulse_complete
                      lastUpdatedAt: '2023-12-12T03:50:41.473Z'
                      createdAt: '2023-12-12T02:29:22.966Z'
                      trigger: scheduled
                      sources:
                        - Metrics 1
                      dateStamps:
                        - '2023-12-10'
                      runHistory:
                        - statusTimestamp: '2023-12-12T03:50:42.631Z'
                          status: pulse_complete
                        - statusTimestamp: '2023-12-12T03:43:37.286Z'
                          status: pulse_started
                        - statusTimestamp: '2023-12-12T03:36:24.884Z'
                          status: pulse_started
                        - statusTimestamp: '2023-12-12T03:29:10.652Z'
                          status: pulse_started
                        - statusTimestamp: '2023-12-12T03:21:58.355Z'
                          status: pulse_started
                        - statusTimestamp: '2023-12-12T03:20:04.085Z'
                          status: metrics_complete
                        - statusTimestamp: '2023-12-12T03:15:24.760Z'
                          status: metrics_started
                        - statusTimestamp: '2023-12-12T03:15:18.051Z'
                          status: metrics_started
                        - statusTimestamp: '2023-12-12T03:15:10.427Z'
                          status: metrics_started
                        - statusTimestamp: '2023-12-12T03:14:55.187Z'
                          status: metrics_started
                        - statusTimestamp: '2023-12-12T02:42:29.345Z'
                          status: download_complete
                        - statusTimestamp: '2023-12-12T02:40:52.701Z'
                          status: download_started
                        - statusTimestamp: '2023-12-12T02:32:50.650Z'
                          status: started
                        - statusTimestamp: '2023-12-12T02:29:22.966Z'
                          status: enqueued
                      granularHistory:
                        - source: Metrics 1
                          latestSourceStatus: pulse_complete
                          statusByDate:
                            - dateStamp: '2023-12-07'
                              statuses:
                                - statusTimestamp: '2023-12-12T03:29:02.000Z'
                                  status: pulse_complete
                                - statusTimestamp: '2023-12-12T03:21:56.433Z'
                                  status: pulse_started
                                - statusTimestamp: '2023-12-12T03:20:02.276Z'
                                  status: metrics_complete
                                - statusTimestamp: '2023-12-12T03:15:23.367Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-12T03:15:16.599Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-12T03:15:09.146Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-12T03:14:52.858Z'
                                  status: metrics_started
                            - dateStamp: '2023-12-08'
                              statuses:
                                - statusTimestamp: '2023-12-12T03:36:14.414Z'
                                  status: pulse_complete
                                - statusTimestamp: '2023-12-12T03:29:09.220Z'
                                  status: pulse_started
                                - statusTimestamp: '2023-12-12T03:20:02.276Z'
                                  status: metrics_complete
                                - statusTimestamp: '2023-12-12T03:15:23.367Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-12T03:15:16.599Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-12T03:15:09.146Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-12T03:14:52.858Z'
                                  status: metrics_started
                            - dateStamp: '2023-12-09'
                              statuses:
                                - statusTimestamp: '2023-12-12T03:43:28.767Z'
                                  status: pulse_complete
                                - statusTimestamp: '2023-12-12T03:36:23.369Z'
                                  status: pulse_started
                                - statusTimestamp: '2023-12-12T03:20:02.276Z'
                                  status: metrics_complete
                                - statusTimestamp: '2023-12-12T03:15:23.367Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-12T03:15:16.599Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-12T03:15:09.146Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-12T03:14:52.858Z'
                                  status: metrics_started
                            - dateStamp: '2023-12-10'
                              statuses:
                                - statusTimestamp: '2023-12-12T03:50:40.851Z'
                                  status: pulse_complete
                                - statusTimestamp: '2023-12-12T03:43:35.832Z'
                                  status: pulse_started
                                - statusTimestamp: '2023-12-12T03:20:02.276Z'
                                  status: metrics_complete
                                - statusTimestamp: '2023-12-12T03:15:23.367Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-12T03:15:16.599Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-12T03:15:09.146Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-12T03:14:52.858Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-12T02:42:12.290Z'
                                  status: download_complete
                                - statusTimestamp: '2023-12-12T02:40:45.773Z'
                                  status: download_started
                                - statusTimestamp: '2023-12-12T02:32:48.580Z'
                                  status: started
                                - statusTimestamp: '2023-12-12T02:29:22.966Z'
                                  status: enqueued
                    - runID: 93b8b43c-8d52-4c77-bf8b-26426031a937
                      latestStatus: download_error
                      lastUpdatedAt: '2023-12-12T05:23:34.419Z'
                      createdAt: '2023-12-11T02:30:09.748Z'
                      trigger: scheduled
                      sources:
                        - Events 1
                        - Events 2
                      dateStamps:
                        - '2023-12-09'
                      runHistory:
                        - statusTimestamp: '2023-12-11T02:43:14.831Z'
                          status: download_error
                        - statusTimestamp: '2023-12-11T02:42:59.726Z'
                          status: download_started
                        - statusTimestamp: '2023-12-11T02:40:35.456Z'
                          status: download_error
                        - statusTimestamp: '2023-12-11T02:39:41.755Z'
                          status: download_started
                        - statusTimestamp: '2023-12-11T02:31:30.223Z'
                          status: started
                        - statusTimestamp: '2023-12-11T02:30:09.748Z'
                          status: enqueued
                      granularHistory:
                        - source: Events 1
                          latestSourceStatus: download_complete
                          statusByDate:
                            - dateStamp: '2023-12-09'
                              statuses:
                                - statusTimestamp: '2023-12-12T05:23:36.192Z'
                                  status: download_complete
                                - statusTimestamp: '2023-12-11T02:40:33.565Z'
                                  status: download_error
                                - statusTimestamp: '2023-12-11T02:39:34.990Z'
                                  status: download_started
                                - statusTimestamp: '2023-12-11T02:31:28.492Z'
                                  status: started
                                - statusTimestamp: '2023-12-11T02:30:09.748Z'
                                  status: enqueued
                        - source: Events 2
                          latestSourceStatus: download_complete
                          statusByDate:
                            - dateStamp: '2023-12-09'
                              statuses:
                                - statusTimestamp: '2023-12-12T05:23:36.193Z'
                                  status: download_complete
                                - statusTimestamp: '2023-12-11T02:40:33.565Z'
                                  status: download_error
                                - statusTimestamp: '2023-12-11T02:39:34.990Z'
                                  status: download_started
                                - statusTimestamp: '2023-12-11T02:31:28.492Z'
                                  status: started
                                - statusTimestamp: '2023-12-11T02:30:09.748Z'
                                  status: enqueued
                    - runID: 97bbdee6-d77b-42c9-b4f0-d970eee9f983
                      latestStatus: pulse_complete
                      lastUpdatedAt: '2023-12-11T10:00:43.391Z'
                      createdAt: '2023-12-11T02:29:04.866Z'
                      trigger: scheduled
                      sources:
                        - Metrics 1
                      dateStamps:
                        - '2023-12-09'
                      runHistory:
                        - statusTimestamp: '2023-12-11T10:00:44.621Z'
                          status: pulse_complete
                        - statusTimestamp: '2023-12-11T09:54:39.521Z'
                          status: pulse_started
                        - statusTimestamp: '2023-12-11T09:47:27.810Z'
                          status: pulse_started
                        - statusTimestamp: '2023-12-11T09:40:15.586Z'
                          status: pulse_started
                        - statusTimestamp: '2023-12-11T09:33:02.761Z'
                          status: pulse_started
                        - statusTimestamp: '2023-12-11T09:31:14.238Z'
                          status: metrics_complete
                        - statusTimestamp: '2023-12-11T09:26:37.129Z'
                          status: metrics_started
                        - statusTimestamp: '2023-12-11T09:26:30.339Z'
                          status: metrics_started
                        - statusTimestamp: '2023-12-11T09:26:23.246Z'
                          status: metrics_started
                        - statusTimestamp: '2023-12-11T09:26:13.395Z'
                          status: metrics_started
                        - statusTimestamp: '2023-12-11T02:51:38.296Z'
                          status: download_complete
                        - statusTimestamp: '2023-12-11T02:49:59.185Z'
                          status: download_started
                        - statusTimestamp: '2023-12-11T02:42:14.545Z'
                          status: started
                        - statusTimestamp: '2023-12-11T02:29:04.866Z'
                          status: enqueued
                      granularHistory:
                        - source: Metrics 1
                          latestSourceStatus: pulse_complete
                          statusByDate:
                            - dateStamp: '2023-12-06'
                              statuses:
                                - statusTimestamp: '2023-12-11T09:40:06.488Z'
                                  status: pulse_complete
                                - statusTimestamp: '2023-12-11T09:33:00.819Z'
                                  status: pulse_started
                                - statusTimestamp: '2023-12-11T09:31:12.660Z'
                                  status: metrics_complete
                                - statusTimestamp: '2023-12-11T09:26:35.749Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-11T09:26:28.818Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-11T09:26:22.624Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-11T09:26:11.934Z'
                                  status: metrics_started
                            - dateStamp: '2023-12-07'
                              statuses:
                                - statusTimestamp: '2023-12-11T09:47:19.007Z'
                                  status: pulse_complete
                                - statusTimestamp: '2023-12-11T09:40:14.371Z'
                                  status: pulse_started
                                - statusTimestamp: '2023-12-11T09:31:12.660Z'
                                  status: metrics_complete
                                - statusTimestamp: '2023-12-11T09:26:35.749Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-11T09:26:28.818Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-11T09:26:22.625Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-11T09:26:11.934Z'
                                  status: metrics_started
                            - dateStamp: '2023-12-08'
                              statuses:
                                - statusTimestamp: '2023-12-11T09:54:31.386Z'
                                  status: pulse_complete
                                - statusTimestamp: '2023-12-11T09:47:26.424Z'
                                  status: pulse_started
                                - statusTimestamp: '2023-12-11T09:31:12.660Z'
                                  status: metrics_complete
                                - statusTimestamp: '2023-12-11T09:26:35.749Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-11T09:26:28.818Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-11T09:26:22.625Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-11T09:26:11.934Z'
                                  status: metrics_started
                            - dateStamp: '2023-12-09'
                              statuses:
                                - statusTimestamp: '2023-12-11T10:00:42.867Z'
                                  status: pulse_complete
                                - statusTimestamp: '2023-12-11T09:54:38.280Z'
                                  status: pulse_started
                                - statusTimestamp: '2023-12-11T09:31:12.660Z'
                                  status: metrics_complete
                                - statusTimestamp: '2023-12-11T09:26:35.749Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-11T09:26:28.818Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-11T09:26:22.625Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-11T09:26:11.934Z'
                                  status: metrics_started
                                - statusTimestamp: '2023-12-11T02:51:26.328Z'
                                  status: download_complete
                                - statusTimestamp: '2023-12-11T02:49:52.797Z'
                                  status: download_started
                                - statusTimestamp: '2023-12-11T02:42:12.424Z'
                                  status: started
                                - statusTimestamp: '2023-12-11T02:29:04.866Z'
                                  status: enqueued
                  pagination:
                    itemsPerPage: 10
                    pageNumber: 1
                    nextPage: /console/v1/ingestion/runs?page=2
                    previousPage: null
              example:
                message: Ingestion Runs Listed Successfully.
                data:
                  - runID: 5a09550b-75a1-4f98-908a-cd79ca729689
                    latestStatus: download_error
                    lastUpdatedAt: '2023-12-14T02:47:00.321Z'
                    createdAt: '2023-12-14T02:31:46.896Z'
                    trigger: scheduled
                    sources:
                      - Events 1
                      - Events 2
                    dateStamps:
                      - '2023-12-12'
                    runHistory:
                      - statusTimestamp: '2023-12-14T02:47:01.422Z'
                        status: download_error
                      - statusTimestamp: '2023-12-14T02:46:46.800Z'
                        status: download_started
                      - statusTimestamp: '2023-12-14T02:44:32.597Z'
                        status: download_error
                      - statusTimestamp: '2023-12-14T02:43:34.056Z'
                        status: download_started
                      - statusTimestamp: '2023-12-14T02:34:27.056Z'
                        status: started
                      - statusTimestamp: '2023-12-14T02:31:46.896Z'
                        status: enqueued
                    granularHistory:
                      - source: Events 1
                        latestSourceStatus: download_error
                        statusByDate:
                          - dateStamp: '2023-12-12'
                            statuses:
                              - statusTimestamp: '2023-12-14T02:44:30.666Z'
                                status: download_error
                              - statusTimestamp: '2023-12-14T02:43:22.724Z'
                                status: download_started
                              - statusTimestamp: '2023-12-14T02:34:25.325Z'
                                status: started
                              - statusTimestamp: '2023-12-14T02:31:46.896Z'
                                status: enqueued
                      - source: Events 2
                        latestSourceStatus: download_error
                        statusByDate:
                          - dateStamp: '2023-12-12'
                            statuses:
                              - statusTimestamp: '2023-12-14T02:44:30.666Z'
                                status: download_error
                              - statusTimestamp: '2023-12-14T02:43:22.724Z'
                                status: download_started
                              - statusTimestamp: '2023-12-14T02:34:25.325Z'
                                status: started
                              - statusTimestamp: '2023-12-14T02:31:46.896Z'
                                status: enqueued
                  - runID: 21b97020-e61a-49bf-a9f3-ce46cec50489
                    latestStatus: pulse_complete
                    lastUpdatedAt: '2023-12-14T04:18:54.603Z'
                    createdAt: '2023-12-14T02:30:27.217Z'
                    trigger: scheduled
                    sources:
                      - Metrics 1
                    dateStamps:
                      - '2023-12-12'
                    runHistory:
                      - statusTimestamp: '2023-12-14T04:18:55.556Z'
                        status: pulse_complete
                      - statusTimestamp: '2023-12-14T03:32:49.429Z'
                        status: metrics_complete
                      - statusTimestamp: '2023-12-14T03:21:40.015Z'
                        status: metrics_started
                      - statusTimestamp: '2023-12-14T03:21:33.322Z'
                        status: metrics_started
                      - statusTimestamp: '2023-12-14T03:21:27.046Z'
                        status: metrics_started
                      - statusTimestamp: '2023-12-14T03:21:15.449Z'
                        status: metrics_started
                      - statusTimestamp: '2023-12-14T02:45:17.161Z'
                        status: download_complete
                      - statusTimestamp: '2023-12-14T02:43:33.661Z'
                        status: download_started
                      - statusTimestamp: '2023-12-14T02:35:09.734Z'
                        status: started
                      - statusTimestamp: '2023-12-14T02:30:27.217Z'
                        status: enqueued
                    granularHistory:
                      - source: Metrics 1
                        latestSourceStatus: pulse_complete
                        statusByDate:
                          - dateStamp: '2023-12-12'
                            statuses:
                              - statusTimestamp: '2023-12-14T04:18:53.975Z'
                                status: pulse_complete
                              - statusTimestamp: '2023-12-14T04:04:48.761Z'
                                status: pulse_started
                              - statusTimestamp: '2023-12-14T03:32:48.019Z'
                                status: metrics_complete
                              - statusTimestamp: '2023-12-14T03:21:38.667Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-14T03:21:32.039Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-14T03:21:25.385Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-14T03:21:14.383Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-14T02:45:05.125Z'
                                status: download_complete
                              - statusTimestamp: '2023-12-14T02:43:27.013Z'
                                status: download_started
                              - statusTimestamp: '2023-12-14T02:35:07.577Z'
                                status: started
                              - statusTimestamp: '2023-12-14T02:30:27.217Z'
                                status: enqueued
                  - runID: de941fa2-3e0f-44ec-a44c-5c51eed07e0d
                    latestStatus: download_error
                    lastUpdatedAt: '2023-12-13T02:44:23.790Z'
                    createdAt: '2023-12-13T02:30:55.992Z'
                    trigger: scheduled
                    sources:
                      - Events 1
                      - Events 2
                    dateStamps:
                      - '2023-12-11'
                    runHistory:
                      - statusTimestamp: '2023-12-13T02:44:24.865Z'
                        status: download_error
                      - statusTimestamp: '2023-12-13T02:44:12.421Z'
                        status: download_started
                      - statusTimestamp: '2023-12-13T02:41:48.458Z'
                        status: download_error
                      - statusTimestamp: '2023-12-13T02:40:56.694Z'
                        status: download_started
                      - statusTimestamp: '2023-12-13T02:32:35.607Z'
                        status: started
                      - statusTimestamp: '2023-12-13T02:30:55.992Z'
                        status: enqueued
                    granularHistory:
                      - source: Events 1
                        latestSourceStatus: download_error
                        statusByDate:
                          - dateStamp: '2023-12-11'
                            statuses:
                              - statusTimestamp: '2023-12-13T02:41:47.374Z'
                                status: download_error
                              - statusTimestamp: '2023-12-13T02:40:50.210Z'
                                status: download_started
                              - statusTimestamp: '2023-12-13T02:32:33.118Z'
                                status: started
                              - statusTimestamp: '2023-12-13T02:30:55.992Z'
                                status: enqueued
                      - source: Events 2
                        latestSourceStatus: download_error
                        statusByDate:
                          - dateStamp: '2023-12-11'
                            statuses:
                              - statusTimestamp: '2023-12-13T02:41:47.374Z'
                                status: download_error
                              - statusTimestamp: '2023-12-13T02:40:50.210Z'
                                status: download_started
                              - statusTimestamp: '2023-12-13T02:32:33.118Z'
                                status: started
                              - statusTimestamp: '2023-12-13T02:30:55.992Z'
                                status: enqueued
                  - runID: 93b0150f-d53a-416e-876f-bac00634a872
                    latestStatus: pulse_complete
                    lastUpdatedAt: '2023-12-13T03:47:23.504Z'
                    createdAt: '2023-12-13T02:29:32.793Z'
                    trigger: scheduled
                    sources:
                      - Metrics 1
                    dateStamps:
                      - '2023-12-11'
                    runHistory:
                      - statusTimestamp: '2023-12-13T03:47:24.548Z'
                        status: pulse_complete
                      - statusTimestamp: '2023-12-13T03:41:19.158Z'
                        status: pulse_started
                      - statusTimestamp: '2023-12-13T03:35:05.780Z'
                        status: pulse_started
                      - statusTimestamp: '2023-12-13T03:28:52.123Z'
                        status: pulse_started
                      - statusTimestamp: '2023-12-13T03:22:38.140Z'
                        status: pulse_started
                      - statusTimestamp: '2023-12-13T03:20:48.982Z'
                        status: metrics_complete
                      - statusTimestamp: '2023-12-13T03:16:40.079Z'
                        status: metrics_started
                      - statusTimestamp: '2023-12-13T03:16:31.359Z'
                        status: metrics_started
                      - statusTimestamp: '2023-12-13T03:16:23.553Z'
                        status: metrics_started
                      - statusTimestamp: '2023-12-13T03:16:08.026Z'
                        status: metrics_started
                      - statusTimestamp: '2023-12-13T02:42:52.210Z'
                        status: download_complete
                      - statusTimestamp: '2023-12-13T02:41:01.394Z'
                        status: download_started
                      - statusTimestamp: '2023-12-13T02:33:26.492Z'
                        status: started
                      - statusTimestamp: '2023-12-13T02:29:32.793Z'
                        status: enqueued
                    granularHistory:
                      - source: Metrics 1
                        latestSourceStatus: pulse_complete
                        statusByDate:
                          - dateStamp: '2023-12-11'
                            statuses:
                              - statusTimestamp: '2023-12-13T03:47:22.812Z'
                                status: pulse_complete
                              - statusTimestamp: '2023-12-13T03:41:17.582Z'
                                status: pulse_started
                              - statusTimestamp: '2023-12-13T03:20:47.294Z'
                                status: metrics_complete
                              - statusTimestamp: '2023-12-13T03:16:38.421Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-13T03:16:29.827Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-13T03:16:21.847Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-13T03:16:05.864Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-13T02:42:36.220Z'
                                status: download_complete
                              - statusTimestamp: '2023-12-13T02:40:47.890Z'
                                status: download_started
                              - statusTimestamp: '2023-12-13T02:33:24.219Z'
                                status: started
                              - statusTimestamp: '2023-12-13T02:29:32.793Z'
                                status: enqueued
                  - runID: a4df397e-c816-4e39-9b1a-ab6b2e5f3811
                    latestStatus: download_error
                    lastUpdatedAt: '2023-12-12T02:43:29.739Z'
                    createdAt: '2023-12-12T02:30:41.989Z'
                    trigger: scheduled
                    sources:
                      - Events 1
                      - Events 2
                    dateStamps:
                      - '2023-12-10'
                    runHistory:
                      - statusTimestamp: '2023-12-12T02:43:30.735Z'
                        status: download_error
                      - statusTimestamp: '2023-12-12T02:43:16.318Z'
                        status: download_started
                      - statusTimestamp: '2023-12-12T02:40:56.030Z'
                        status: download_error
                      - statusTimestamp: '2023-12-12T02:39:58.147Z'
                        status: download_started
                      - statusTimestamp: '2023-12-12T02:32:18.156Z'
                        status: started
                      - statusTimestamp: '2023-12-12T02:30:41.989Z'
                        status: enqueued
                    granularHistory:
                      - source: Events 1
                        latestSourceStatus: download_error
                        statusByDate:
                          - dateStamp: '2023-12-10'
                            statuses:
                              - statusTimestamp: '2023-12-12T02:40:54.406Z'
                                status: download_error
                              - statusTimestamp: '2023-12-12T02:39:51.150Z'
                                status: download_started
                              - statusTimestamp: '2023-12-12T02:32:16.419Z'
                                status: started
                              - statusTimestamp: '2023-12-12T02:30:41.989Z'
                                status: enqueued
                      - source: Events 2
                        latestSourceStatus: download_error
                        statusByDate:
                          - dateStamp: '2023-12-10'
                            statuses:
                              - statusTimestamp: '2023-12-12T02:40:54.406Z'
                                status: download_error
                              - statusTimestamp: '2023-12-12T02:39:51.150Z'
                                status: download_started
                              - statusTimestamp: '2023-12-12T02:32:16.419Z'
                                status: started
                              - statusTimestamp: '2023-12-12T02:30:41.989Z'
                                status: enqueued
                  - runID: eedeb4c0-07dd-43d0-8014-5ac41ef7dab8
                    latestStatus: pulse_complete
                    lastUpdatedAt: '2023-12-12T03:50:41.473Z'
                    createdAt: '2023-12-12T02:29:22.966Z'
                    trigger: scheduled
                    sources:
                      - Metrics 1
                    dateStamps:
                      - '2023-12-10'
                    runHistory:
                      - statusTimestamp: '2023-12-12T03:50:42.631Z'
                        status: pulse_complete
                      - statusTimestamp: '2023-12-12T03:43:37.286Z'
                        status: pulse_started
                      - statusTimestamp: '2023-12-12T03:36:24.884Z'
                        status: pulse_started
                      - statusTimestamp: '2023-12-12T03:29:10.652Z'
                        status: pulse_started
                      - statusTimestamp: '2023-12-12T03:21:58.355Z'
                        status: pulse_started
                      - statusTimestamp: '2023-12-12T03:20:04.085Z'
                        status: metrics_complete
                      - statusTimestamp: '2023-12-12T03:15:24.760Z'
                        status: metrics_started
                      - statusTimestamp: '2023-12-12T03:15:18.051Z'
                        status: metrics_started
                      - statusTimestamp: '2023-12-12T03:15:10.427Z'
                        status: metrics_started
                      - statusTimestamp: '2023-12-12T03:14:55.187Z'
                        status: metrics_started
                      - statusTimestamp: '2023-12-12T02:42:29.345Z'
                        status: download_complete
                      - statusTimestamp: '2023-12-12T02:40:52.701Z'
                        status: download_started
                      - statusTimestamp: '2023-12-12T02:32:50.650Z'
                        status: started
                      - statusTimestamp: '2023-12-12T02:29:22.966Z'
                        status: enqueued
                    granularHistory:
                      - source: Metrics 1
                        latestSourceStatus: pulse_complete
                        statusByDate:
                          - dateStamp: '2023-12-07'
                            statuses:
                              - statusTimestamp: '2023-12-12T03:29:02.000Z'
                                status: pulse_complete
                              - statusTimestamp: '2023-12-12T03:21:56.433Z'
                                status: pulse_started
                              - statusTimestamp: '2023-12-12T03:20:02.276Z'
                                status: metrics_complete
                              - statusTimestamp: '2023-12-12T03:15:23.367Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-12T03:15:16.599Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-12T03:15:09.146Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-12T03:14:52.858Z'
                                status: metrics_started
                          - dateStamp: '2023-12-08'
                            statuses:
                              - statusTimestamp: '2023-12-12T03:36:14.414Z'
                                status: pulse_complete
                              - statusTimestamp: '2023-12-12T03:29:09.220Z'
                                status: pulse_started
                              - statusTimestamp: '2023-12-12T03:20:02.276Z'
                                status: metrics_complete
                              - statusTimestamp: '2023-12-12T03:15:23.367Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-12T03:15:16.599Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-12T03:15:09.146Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-12T03:14:52.858Z'
                                status: metrics_started
                          - dateStamp: '2023-12-09'
                            statuses:
                              - statusTimestamp: '2023-12-12T03:43:28.767Z'
                                status: pulse_complete
                              - statusTimestamp: '2023-12-12T03:36:23.369Z'
                                status: pulse_started
                              - statusTimestamp: '2023-12-12T03:20:02.276Z'
                                status: metrics_complete
                              - statusTimestamp: '2023-12-12T03:15:23.367Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-12T03:15:16.599Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-12T03:15:09.146Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-12T03:14:52.858Z'
                                status: metrics_started
                          - dateStamp: '2023-12-10'
                            statuses:
                              - statusTimestamp: '2023-12-12T03:50:40.851Z'
                                status: pulse_complete
                              - statusTimestamp: '2023-12-12T03:43:35.832Z'
                                status: pulse_started
                              - statusTimestamp: '2023-12-12T03:20:02.276Z'
                                status: metrics_complete
                              - statusTimestamp: '2023-12-12T03:15:23.367Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-12T03:15:16.599Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-12T03:15:09.146Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-12T03:14:52.858Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-12T02:42:12.290Z'
                                status: download_complete
                              - statusTimestamp: '2023-12-12T02:40:45.773Z'
                                status: download_started
                              - statusTimestamp: '2023-12-12T02:32:48.580Z'
                                status: started
                              - statusTimestamp: '2023-12-12T02:29:22.966Z'
                                status: enqueued
                  - runID: 93b8b43c-8d52-4c77-bf8b-26426031a937
                    latestStatus: download_error
                    lastUpdatedAt: '2023-12-12T05:23:34.419Z'
                    createdAt: '2023-12-11T02:30:09.748Z'
                    trigger: scheduled
                    sources:
                      - Events 1
                      - Events 2
                    dateStamps:
                      - '2023-12-09'
                    runHistory:
                      - statusTimestamp: '2023-12-11T02:43:14.831Z'
                        status: download_error
                      - statusTimestamp: '2023-12-11T02:42:59.726Z'
                        status: download_started
                      - statusTimestamp: '2023-12-11T02:40:35.456Z'
                        status: download_error
                      - statusTimestamp: '2023-12-11T02:39:41.755Z'
                        status: download_started
                      - statusTimestamp: '2023-12-11T02:31:30.223Z'
                        status: started
                      - statusTimestamp: '2023-12-11T02:30:09.748Z'
                        status: enqueued
                    granularHistory:
                      - source: Events 1
                        latestSourceStatus: download_complete
                        statusByDate:
                          - dateStamp: '2023-12-09'
                            statuses:
                              - statusTimestamp: '2023-12-12T05:23:36.192Z'
                                status: download_complete
                              - statusTimestamp: '2023-12-11T02:40:33.565Z'
                                status: download_error
                              - statusTimestamp: '2023-12-11T02:39:34.990Z'
                                status: download_started
                              - statusTimestamp: '2023-12-11T02:31:28.492Z'
                                status: started
                              - statusTimestamp: '2023-12-11T02:30:09.748Z'
                                status: enqueued
                      - source: Events 2
                        latestSourceStatus: download_complete
                        statusByDate:
                          - dateStamp: '2023-12-09'
                            statuses:
                              - statusTimestamp: '2023-12-12T05:23:36.193Z'
                                status: download_complete
                              - statusTimestamp: '2023-12-11T02:40:33.565Z'
                                status: download_error
                              - statusTimestamp: '2023-12-11T02:39:34.990Z'
                                status: download_started
                              - statusTimestamp: '2023-12-11T02:31:28.492Z'
                                status: started
                              - statusTimestamp: '2023-12-11T02:30:09.748Z'
                                status: enqueued
                  - runID: 97bbdee6-d77b-42c9-b4f0-d970eee9f983
                    latestStatus: pulse_complete
                    lastUpdatedAt: '2023-12-11T10:00:43.391Z'
                    createdAt: '2023-12-11T02:29:04.866Z'
                    trigger: scheduled
                    sources:
                      - Metrics 1
                    dateStamps:
                      - '2023-12-09'
                    runHistory:
                      - statusTimestamp: '2023-12-11T10:00:44.621Z'
                        status: pulse_complete
                      - statusTimestamp: '2023-12-11T09:54:39.521Z'
                        status: pulse_started
                      - statusTimestamp: '2023-12-11T09:47:27.810Z'
                        status: pulse_started
                      - statusTimestamp: '2023-12-11T09:40:15.586Z'
                        status: pulse_started
                      - statusTimestamp: '2023-12-11T09:33:02.761Z'
                        status: pulse_started
                      - statusTimestamp: '2023-12-11T09:31:14.238Z'
                        status: metrics_complete
                      - statusTimestamp: '2023-12-11T09:26:37.129Z'
                        status: metrics_started
                      - statusTimestamp: '2023-12-11T09:26:30.339Z'
                        status: metrics_started
                      - statusTimestamp: '2023-12-11T09:26:23.246Z'
                        status: metrics_started
                      - statusTimestamp: '2023-12-11T09:26:13.395Z'
                        status: metrics_started
                      - statusTimestamp: '2023-12-11T02:51:38.296Z'
                        status: download_complete
                      - statusTimestamp: '2023-12-11T02:49:59.185Z'
                        status: download_started
                      - statusTimestamp: '2023-12-11T02:42:14.545Z'
                        status: started
                      - statusTimestamp: '2023-12-11T02:29:04.866Z'
                        status: enqueued
                    granularHistory:
                      - source: Metrics 1
                        latestSourceStatus: pulse_complete
                        statusByDate:
                          - dateStamp: '2023-12-06'
                            statuses:
                              - statusTimestamp: '2023-12-11T09:40:06.488Z'
                                status: pulse_complete
                              - statusTimestamp: '2023-12-11T09:33:00.819Z'
                                status: pulse_started
                              - statusTimestamp: '2023-12-11T09:31:12.660Z'
                                status: metrics_complete
                              - statusTimestamp: '2023-12-11T09:26:35.749Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-11T09:26:28.818Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-11T09:26:22.624Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-11T09:26:11.934Z'
                                status: metrics_started
                          - dateStamp: '2023-12-07'
                            statuses:
                              - statusTimestamp: '2023-12-11T09:47:19.007Z'
                                status: pulse_complete
                              - statusTimestamp: '2023-12-11T09:40:14.371Z'
                                status: pulse_started
                              - statusTimestamp: '2023-12-11T09:31:12.660Z'
                                status: metrics_complete
                              - statusTimestamp: '2023-12-11T09:26:35.749Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-11T09:26:28.818Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-11T09:26:22.625Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-11T09:26:11.934Z'
                                status: metrics_started
                          - dateStamp: '2023-12-08'
                            statuses:
                              - statusTimestamp: '2023-12-11T09:54:31.386Z'
                                status: pulse_complete
                              - statusTimestamp: '2023-12-11T09:47:26.424Z'
                                status: pulse_started
                              - statusTimestamp: '2023-12-11T09:31:12.660Z'
                                status: metrics_complete
                              - statusTimestamp: '2023-12-11T09:26:35.749Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-11T09:26:28.818Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-11T09:26:22.625Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-11T09:26:11.934Z'
                                status: metrics_started
                          - dateStamp: '2023-12-09'
                            statuses:
                              - statusTimestamp: '2023-12-11T10:00:42.867Z'
                                status: pulse_complete
                              - statusTimestamp: '2023-12-11T09:54:38.280Z'
                                status: pulse_started
                              - statusTimestamp: '2023-12-11T09:31:12.660Z'
                                status: metrics_complete
                              - statusTimestamp: '2023-12-11T09:26:35.749Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-11T09:26:28.818Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-11T09:26:22.625Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-11T09:26:11.934Z'
                                status: metrics_started
                              - statusTimestamp: '2023-12-11T02:51:26.328Z'
                                status: download_complete
                              - statusTimestamp: '2023-12-11T02:49:52.797Z'
                                status: download_started
                              - statusTimestamp: '2023-12-11T02:42:12.424Z'
                                status: started
                              - statusTimestamp: '2023-12-11T02:29:04.866Z'
                                status: enqueued
                pagination:
                  itemsPerPage: 10
                  pageNumber: 1
                  nextPage: /console/v1/ingestion/runs?page=2
                  previousPage: null
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
    IngestionRunDataContractDto:
      type: object
      properties:
        runID:
          type: string
        latestStatus:
          type: string
        lastUpdatedAt:
          type: string
          format: date-time
        createdAt:
          type: string
          format: date-time
        trigger:
          type: string
        sources:
          type: array
          items:
            type: string
        dateStamps:
          type: array
          items:
            type: string
        runHistory:
          type: array
          items:
            type: object
            properties:
              statusTimestamp:
                type: string
                format: date-time
              status:
                type: string
            required:
              - statusTimestamp
              - status
        granularHistory:
          type: array
          items:
            type: object
            properties:
              source:
                type: string
              latestSourceStatus:
                type: string
              statusByDate:
                type: array
                items:
                  type: object
                  properties:
                    dateStamp:
                      type: string
                    statuses:
                      type: array
                      items:
                        type: object
                        properties:
                          statusTimestamp:
                            type: string
                            format: date-time
                          status:
                            type: string
                        required:
                          - statusTimestamp
                          - status
                  required:
                    - dateStamp
                    - statuses
            required:
              - source
              - latestSourceStatus
              - statusByDate
      required:
        - runID
        - latestStatus
        - lastUpdatedAt
        - createdAt
        - trigger
        - sources
        - dateStamps
        - runHistory
        - granularHistory
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