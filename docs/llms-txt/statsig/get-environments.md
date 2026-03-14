# Source: https://docs.statsig.com/api-reference/environments/get-environments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Environments



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/environments
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
  /console/v1/environments:
    get:
      tags:
        - Environments
      summary: Get Environments
      parameters: []
      responses:
        '200':
          description: Get Environments Response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/EnvironmentsContractDto'
                example:
                  message: Environments read successfully.
                  data:
                    environments:
                      - name: development
                        id: '0.35629335902367476'
                        isProduction: false
                        requiresReview: false
                        requiresReleasePipeline: true
                      - name: staging
                        id: '0.015089163460661137'
                        isProduction: false
                        requiresReview: false
                        requiresReleasePipeline: true
                      - name: production
                        id: '0.4067426155658289'
                        isProduction: true
                        requiresReview: true
                        requiresReleasePipeline: true
              example:
                message: Environments read successfully.
                data:
                  environments:
                    - name: development
                      id: '0.35629335902367476'
                      isProduction: false
                      requiresReview: false
                      requiresReleasePipeline: true
                    - name: staging
                      id: '0.015089163460661137'
                      isProduction: false
                      requiresReview: false
                      requiresReleasePipeline: true
                    - name: production
                      id: '0.4067426155658289'
                      isProduction: true
                      requiresReview: true
                      requiresReleasePipeline: true
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
    EnvironmentsContractDto:
      type: object
      properties:
        environments:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                description: The name of the environment.
              id:
                type: string
                description: A unique identifier for the environment.
              isProduction:
                type: boolean
                description: Whether the environment is production.
              requiresReview:
                type: boolean
                description: Whether the environment requires review.
              requiredReviewGroupID:
                type: string
                description: >-
                  The ID of the review group that the environment requires
                  review from.
              requiresReleasePipeline:
                type: boolean
                description: Whether the environment requires a release pipeline.
            required:
              - name
              - id
              - isProduction
              - requiresReview
              - requiresReleasePipeline
      required:
        - environments
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).