# Source: https://docs.statsig.com/api-reference/layers/create-a-layer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a Layer



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/layers
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
  /console/v1/layers:
    post:
      tags:
        - Layers
      summary: Create a Layer
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LayerCreateContractDto'
      responses:
        '201':
          description: Create Layer Response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/LayerContractDto'
                example:
                  message: Layer created successfully.
                  data:
                    id: the_best_layer
                    description: helpful summary of what this layer does
                    idType: userID
                    lastModifierID: 4dcQUIpS8PHObBGD7HJwOx
                    lastModifiedTime: 1720733945538
                    lastModifierName: CONSOLE API
                    lastModifierEmail: null
                    creatorID: 4dcQUIpS8PHObBGD7HJwOx
                    createdTime: 1720733942515
                    creatorName: CONSOLE API
                    creatorEmail: null
                    targetApps:
                      - Android
                    holdoutIDs:
                      - global_holdout
                      - test_holdout
                    tags: []
                    team: Console Team
                    isImplicitLayer: false
                    parameters: []
              example:
                message: Layer created successfully.
                data:
                  id: the_best_layer
                  description: helpful summary of what this layer does
                  idType: userID
                  lastModifierID: 4dcQUIpS8PHObBGD7HJwOx
                  lastModifiedTime: 1720733945538
                  lastModifierName: CONSOLE API
                  lastModifierEmail: null
                  creatorID: 4dcQUIpS8PHObBGD7HJwOx
                  createdTime: 1720733942515
                  creatorName: CONSOLE API
                  creatorEmail: null
                  targetApps:
                    - Android
                  holdoutIDs:
                    - global_holdout
                    - test_holdout
                  tags: []
                  team: Console Team
                  isImplicitLayer: false
                  parameters: []
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
    LayerCreateContractDto:
      type: object
      properties:
        name:
          type: string
          maxLength: 100
          minLength: 3
          pattern: ^[A-Za-z0-9_ -]*$
          description: >-
            The unique name of the layer, formatted as an ID (e.g., "A Layer"
            becomes "a_layer").
        description:
          type: string
          maxLength: 1000
          description: >-
            A helpful description of what this layer does, providing context for
            its purpose.
        idType:
          type: string
          description: >-
            The type of ID used for this layer, essential for validation in
            services.
        targetApps:
          oneOf:
            - type: string
            - type: array
              items:
                type: string
          description: List of target applications that this layer is associated with.
        team:
          type: string
          description: Optional identifier for the team responsible for this layer.
      required:
        - name
        - idType
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
    LayerContractDto:
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
          description: The ID type used for this layer, important for validation.
        description:
          type: string
          maxLength: 1000
          description: >-
            A detailed description of the layer, explaining its purpose and
            functionality.
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
          oneOf:
            - type: string
            - type: array
              items:
                type: string
          description: List of target applications that this layer is intended for.
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
        isImplicitLayer:
          type: boolean
          description: >-
            Indicates if the layer was automatically created by Statsig during
            experiment creation.
        parameters:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                description: >-
                  The name of this parameter, used for identification within the
                  layer.
              type:
                type: string
                enum:
                  - string
                  - number
                  - boolean
                  - object
                  - array
                description: >-
                  The data type that this parameter returns. Allowed types
                  include: string, boolean, number, object, and array.
              defaultValue:
                oneOf:
                  - type: string
                  - type: number
                  - type: boolean
                  - type: object
                    additionalProperties: {}
                  - type: array
                    items:
                      oneOf:
                        - type: string
                        - type: number
                        - type: boolean
                        - type: object
                          additionalProperties: {}
                description: >-
                  The default value for this parameter, which must match the
                  specified type.
              description:
                type: string
                description: >-
                  An optional helpful description of what this layer parameter
                  does, providing context for its purpose.
            required:
              - name
              - type
              - defaultValue
          description: >-
            An array of parameters associated with the layer, each defining
            specific attributes.
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
        - isImplicitLayer
        - parameters
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).