# Source: https://docs.statsig.com/api-reference/holdouts/create-holdout.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create holdout



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/holdouts
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
  /console/v1/holdouts:
    post:
      tags:
        - Holdouts
      summary: Create holdout
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/HoldoutCreateContractDto'
      responses:
        '200':
          description: Create holdout response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/HoldoutDto'
                example:
                  message: Holdout created successfully.
                  data:
                    id: a_holdout
                    name: a holdout
                    description: helpful summary of what this holdout does
                    idType: userID
                    lastModifierID: 1vaQaBoLlkauH9iiuOSBP2
                    lastModifiedTime: 1707768016211
                    lastModifierName: CONSOLE API
                    lastModifierEmail: null
                    creatorID: 1vaQaBoLlkauH9iiuOSBP2
                    createdTime: 1707768015729
                    creatorName: CONSOLE API
                    creatorEmail: null
                    targetApps: []
                    tags: []
                    team: Console Team
                    isEnabled: true
                    isGlobal: false
                    passPercentage: 0
                    gateIDs: []
                    experimentIDs: []
                    layerIDs: []
                    targetingGateID: null
              example:
                message: Holdout created successfully.
                data:
                  id: a_holdout
                  name: a holdout
                  description: helpful summary of what this holdout does
                  idType: userID
                  lastModifierID: 1vaQaBoLlkauH9iiuOSBP2
                  lastModifiedTime: 1707768016211
                  lastModifierName: CONSOLE API
                  lastModifierEmail: null
                  creatorID: 1vaQaBoLlkauH9iiuOSBP2
                  createdTime: 1707768015729
                  creatorName: CONSOLE API
                  creatorEmail: null
                  targetApps: []
                  tags: []
                  team: Console Team
                  isEnabled: true
                  isGlobal: false
                  passPercentage: 0
                  gateIDs: []
                  experimentIDs: []
                  layerIDs: []
                  targetingGateID: null
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
        '404':
          description: Not Found Exception
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
    HoldoutCreateContractDto:
      type: object
      properties:
        name:
          type: string
          maxLength: 100
          minLength: 3
          pattern: ^[a-zA-Z0-9_\- ]*$
          example: team holdout
          description: name of the holdout
        description:
          type: string
          maxLength: 1000
          example: holdout for this team
          description: description of the holdout
        idType:
          type: string
          example: userID
          description: type of id
        teamID:
          type: string
          nullable: true
          example: 4pjeXYDjC2WinSgOiII7wh
          description: id of the team
      required:
        - name
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