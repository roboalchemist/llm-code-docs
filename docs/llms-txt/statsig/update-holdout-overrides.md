# Source: https://docs.statsig.com/api-reference/holdouts/update-holdout-overrides.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Holdout Overrides



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/holdouts/{id}/overrides
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
  /console/v1/holdouts/{id}/overrides:
    post:
      tags:
        - Holdouts
      summary: Update Holdout Overrides
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
              $ref: '#/components/schemas/UpdateOverridesContractDto'
      responses:
        '200':
          description: Update Holdout Overrides Success
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/OverrideDto'
                example:
                  message: Holdout Overrides updated successfully.
                  data:
                    passingUserIDs:
                      - passing-user
                    failingUserIDs:
                      - failing-user
                    passingCustomIDs:
                      - passing-custom-id
                    failingCustomIDs:
                      - failing-custom-id
              example:
                message: Holdout Overrides updated successfully.
                data:
                  passingUserIDs:
                    - passing-user
                  failingUserIDs:
                    - failing-user
                  passingCustomIDs:
                    - passing-custom-id
                  failingCustomIDs:
                    - failing-custom-id
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
    UpdateOverridesContractDto:
      oneOf:
        - type: object
          properties:
            environmentOverrides:
              type: array
              items:
                type: object
                properties:
                  environment:
                    type: string
                    nullable: true
                    description: Environment
                    example: staging
                  unitID:
                    type: string
                    nullable: true
                    description: Unit ID
                    example: unit123
                  passingIDs:
                    type: array
                    items:
                      type: string
                    description: List of passing IDs
                    example:
                      - id1
                      - id2
                  failingIDs:
                    type: array
                    items:
                      type: string
                    description: List of failing IDs
                    example:
                      - id3
                      - id4
                required:
                  - unitID
                  - passingIDs
                  - failingIDs
                description: Contract for environment override
                example:
                  environment: staging
                  unitID: unit123
                  passingIDs:
                    - id1
                    - id2
                  failingIDs:
                    - id3
                    - id4
          required:
            - environmentOverrides
          description: Contract for updating environment overrides
          example:
            environmentOverrides:
              - environment: staging
                unitID: unit123
                passingIDs:
                  - id1
                  - id2
                failingIDs:
                  - id3
                  - id4
        - type: object
          properties:
            passingUserIDs:
              type: array
              items:
                type: string
                minLength: 1
                description: User ID
                example: user123
              maxItems: 2000
              description: List of user IDs
              example:
                - user123
                - user456
                - user789
            failingUserIDs:
              type: array
              items:
                type: string
                minLength: 1
                description: User ID
                example: user123
              maxItems: 2000
              description: List of user IDs
              example:
                - user123
                - user456
                - user789
            passingCustomIDs:
              type: array
              items:
                type: string
                minLength: 1
                description: Custom ID
                example: custom123
              maxItems: 2000
              description: Optional list of custom IDs
              example:
                - custom123
                - custom456
            failingCustomIDs:
              type: array
              items:
                type: string
                minLength: 1
                description: Custom ID
                example: custom123
              maxItems: 2000
              description: Optional list of custom IDs
              example:
                - custom123
                - custom456
          required:
            - passingUserIDs
            - failingUserIDs
          description: Contract for updating ID overrides
          example:
            passingUserIDs:
              - user123
              - user456
            failingUserIDs:
              - user789
              - user012
            passingCustomIDs:
              - custom123
            failingCustomIDs:
              - custom456
      description: Contract for updating overrides
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
    OverrideDto:
      type: object
      properties:
        passingUserIDs:
          type: array
          items:
            type: string
            minLength: 1
            description: User ID
            example: user123
          maxItems: 2000
          description: List of user IDs
          example:
            - user123
            - user456
            - user789
        failingUserIDs:
          type: array
          items:
            type: string
            minLength: 1
            description: User ID
            example: user123
          maxItems: 2000
          description: List of user IDs
          example:
            - user123
            - user456
            - user789
        passingCustomIDs:
          type: array
          items:
            type: string
            minLength: 1
            description: Custom ID
            example: custom123
          maxItems: 2000
          description: Optional list of custom IDs
          example:
            - custom123
            - custom456
        failingCustomIDs:
          type: array
          items:
            type: string
            minLength: 1
            description: Custom ID
            example: custom123
          maxItems: 2000
          description: Optional list of custom IDs
          example:
            - custom123
            - custom456
        environmentOverrides:
          type: array
          items:
            type: object
            properties:
              environment:
                type: string
                nullable: true
                description: Environment
                example: staging
              unitID:
                type: string
                nullable: true
                description: Unit ID
                example: unit123
              passingIDs:
                type: array
                items:
                  type: string
                description: List of passing IDs
                example:
                  - id1
                  - id2
              failingIDs:
                type: array
                items:
                  type: string
                description: List of failing IDs
                example:
                  - id3
                  - id4
            required:
              - unitID
              - passingIDs
              - failingIDs
            description: Contract for environment override
            example:
              environment: staging
              unitID: unit123
              passingIDs:
                - id1
                - id2
              failingIDs:
                - id3
                - id4
      required:
        - passingUserIDs
        - failingUserIDs
        - environmentOverrides
      description: Contract for overrides
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).