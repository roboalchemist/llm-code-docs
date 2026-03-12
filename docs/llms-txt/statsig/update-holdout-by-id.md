# Source: https://docs.statsig.com/api-reference/holdouts/update-holdout-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update holdout by id



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/holdouts/{id}
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
  /console/v1/holdouts/{id}:
    post:
      tags:
        - Holdouts
      summary: Update holdout by id
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
              $ref: '#/components/schemas/HoldoutFullUpdateContractDto'
      responses:
        '200':
          description: Update holdout response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/HoldoutDto'
                example:
                  message: Holdout updated successfully.
                  data:
                    id: testing_holdout
                    name: testing holdout
                    description: UPDATED summary of what this holdout does
                    idType: userID
                    lastModifierID: 4dcQUIpS8PHObBGD7HJwOx
                    lastModifiedTime: 1719941188286
                    lastModifierName: CONSOLE API
                    lastModifierEmail: null
                    creatorID: 4dcQUIpS8PHObBGD7HJwOx
                    createdTime: 1719873870785
                    creatorName: CONSOLE API
                    creatorEmail: null
                    targetApps: []
                    tags: []
                    team: Console Team
                    isEnabled: true
                    isGlobal: true
                    passPercentage: 5
                    gateIDs: []
                    experimentIDs:
                      - testing123
                    layerIDs: []
                    targetingGateID: ''
              example:
                message: Holdout updated successfully.
                data:
                  id: testing_holdout
                  name: testing holdout
                  description: UPDATED summary of what this holdout does
                  idType: userID
                  lastModifierID: 4dcQUIpS8PHObBGD7HJwOx
                  lastModifiedTime: 1719941188286
                  lastModifierName: CONSOLE API
                  lastModifierEmail: null
                  creatorID: 4dcQUIpS8PHObBGD7HJwOx
                  createdTime: 1719873870785
                  creatorName: CONSOLE API
                  creatorEmail: null
                  targetApps: []
                  tags: []
                  team: Console Team
                  isEnabled: true
                  isGlobal: true
                  passPercentage: 5
                  gateIDs: []
                  experimentIDs:
                    - testing123
                  layerIDs: []
                  targetingGateID: ''
        '400':
          description: Name is already in use
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
                    message: Name is already in use
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
        '404':
          description: Not Found. The requested resource could not be found.
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
    HoldoutFullUpdateContractDto:
      type: object
      properties:
        isEnabled:
          type: boolean
          example: true
          description: enable or disable the holdout
        description:
          type: string
          maxLength: 1000
          example: example holdout description
          description: brief summary of what the holdout is being used for
        passPercentage:
          type: number
          minimum: 0
          maximum: 10
          example: 5
          description: percentage of users between 0-10% to pass through the holdout
          format: double
        gateIDs:
          type: array
          items:
            type: string
          example:
            - 4pjeXYDjC2WinSgOiII7wh
          description: an array of gateIDs which this holdout is applied to
        experimentIDs:
          type: array
          items:
            type: string
          example:
            - 70fCNphHGesdLwHdHau99q
          description: an array of experimentIDs which this holdout is applied to
        layerIDs:
          type: array
          items:
            type: string
          example:
            - 5O908pyGoCqw6QH1nt8v82
          description: an array of layerIDs which this holdout is applied to
        isGlobal:
          type: boolean
          example: false
          description: whether the holdout is being applied to all new gates
        targetingGateID:
          type: string
          nullable: true
          example: 4pjeXYDjC2WinSgOiII7wh
          description: the gateID that the holdout is targeting
        monitoringMetrics:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
              type:
                type: string
            required:
              - name
              - type
      required:
        - isEnabled
        - description
        - passPercentage
        - gateIDs
        - experimentIDs
        - layerIDs
        - isGlobal
        - targetingGateID
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
    HoldoutDto:
      type: object
      properties:
        id:
          type: string
          description: ID
        name:
          type: string
          description: Optional name for the configuration.
        idType:
          type: string
          description: type of id
        description:
          type: string
          maxLength: 1000
          example: example holdout description
          description: brief summary of what the holdout is being used for
        lastModifierID:
          type: string
          nullable: true
          description: ID of the last modifier.
        lastModifiedTime:
          type: number
          nullable: true
          description: Time of the last modification.
          format: double
        lastModifierEmail:
          type: string
          nullable: true
          description: Email of the last modifier.
        lastModifierName:
          type: string
          nullable: true
          description: Name of the last modifier.
        creatorID:
          type: string
          nullable: true
          description: ID of the user who created the entity.
        createdTime:
          type: number
          description: Timestamp when the entity was created.
          format: double
        creatorName:
          type: string
          nullable: true
          description: Name of the creator.
        creatorEmail:
          type: string
          nullable: true
          description: Email of the creator.
        tags:
          type: array
          items:
            type: string
          description: Optional tags for categorization.
        targetApps:
          type: array
          items:
            type: string
          description: List of target applications associated with this configuration.
        holdoutIDs:
          type: array
          items:
            type: string
          description: Holdouts applied to this configuration.
        team:
          type: string
          nullable: true
          description: Optional name for the responsible team.
        teamID:
          type: string
          nullable: true
          description: Optional ID of the responsible team.
        version:
          type: number
          description: Version number
          format: double
        isEnabled:
          type: boolean
          example: true
          description: enable or disable the holdout
        passPercentage:
          type: number
          minimum: 0
          maximum: 10
          example: 5
          description: percentage of users between 0-10% to pass through the holdout
          format: double
        gateIDs:
          type: array
          items:
            type: string
          example:
            - 4pjeXYDjC2WinSgOiII7wh
          description: an array of gateIDs which this holdout is applied to
        experimentIDs:
          type: array
          items:
            type: string
          example:
            - 70fCNphHGesdLwHdHau99q
          description: an array of experimentIDs which this holdout is applied to
        layerIDs:
          type: array
          items:
            type: string
          example:
            - 5O908pyGoCqw6QH1nt8v82
          description: an array of layerIDs which this holdout is applied to
        isGlobal:
          type: boolean
          example: false
          description: whether the holdout is being applied to all new gates
        targetingGateID:
          type: string
          nullable: true
          example: 4pjeXYDjC2WinSgOiII7wh
          description: the gateID that the holdout is targeting
        monitoringMetrics:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
              type:
                type: string
            required:
              - name
              - type
      required:
        - id
        - idType
        - description
        - lastModifierID
        - lastModifiedTime
        - lastModifierEmail
        - lastModifierName
        - creatorID
        - createdTime
        - creatorName
        - creatorEmail
        - isEnabled
        - passPercentage
        - gateIDs
        - experimentIDs
        - layerIDs
        - isGlobal
        - targetingGateID
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).