# Source: https://docs.statsig.com/api-reference/prompts/create-prompt.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Prompt



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json post /console/v1/prompts
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
  /console/v1/prompts:
    post:
      tags:
        - Prompts
      summary: Create Prompt
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AIConfigCreateDto'
      responses:
        '200':
          description: Create Prompt
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/ExternalPromptDto'
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
        '403':
          description: >-
            Forbidden. The request was valid, but the server is refusing action.
            You might not have the necessary permissions to access the resource.
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: integer
                    enum:
                      - 403
                  message:
                    type: string
                required:
                  - status
                  - message
              examples:
                Forbidden resource:
                  value:
                    status: 403
                    message: >-
                      Forbidden. The request was valid, but the server is
                      refusing action. You might not have the necessary
                      permissions to access the resource.
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    AIConfigCreateDto:
      type: object
      properties:
        name:
          type: string
          maxLength: 100
          minLength: 3
          pattern: ^[a-zA-Z0-9_\-. ]*$
          description: Name for the AI Config.
          example: my_prompt
        displayName:
          type: string
          maxLength: 100
          minLength: 3
          pattern: ^[a-zA-Z0-9_\-. ]*$
          description: Optional display name for the AI Config.
        description:
          type: string
          maxLength: 1000
          description: Description for the AI Config.
        targetApps:
          oneOf:
            - type: string
            - type: array
              items:
                type: string
          description: List of target app names.
        team:
          type: string
          description: Team name.
        teamID:
          type: string
          description: Team ID.
        tags:
          type: array
          items:
            type: string
          description: Optional tags to associate with the AI Config.
        creatorID:
          type: string
          nullable: true
        owner:
          type: object
          properties:
            ownerID:
              type: string
              description: ID of the owner
              example: abc123
            ownerType:
              type: string
              description: Type of the owner (e.g., SDK_KEY or USER)
              example: USER
            ownerName:
              type: string
              description: The name of the owner. This field is optional.
              example: John Doe
            ownerEmail:
              type: string
              description: The email of the owner. This field is optional.
          description: >-
            Schema for owner data including ID, type, name. Note that if Entity
            is created by CONSOLE API, owner will be undefined.
          example:
            ownerID: user123
            ownerType: USER
            ownerName: John Doe
            ownerEmail: owner123@test.com
          nullable: true
        creatorEmail:
          type: string
          nullable: true
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
    ExternalPromptDto:
      type: object
      properties:
        id:
          type: string
          description: ID
        name:
          type: string
          maxLength: 100
          minLength: 3
          pattern: ^[a-zA-Z0-9_\-. ]*$
          description: The gate display name
        idType:
          type: string
        description:
          type: string
          maxLength: 1000
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
        tags:
          type: array
          items:
            type: string
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
        teamID:
          type: string
          nullable: true
        version:
          type: number
          description: Version number
          format: double
      required:
        - id
        - description
        - lastModifierID
        - lastModifiedTime
        - lastModifierEmail
        - lastModifierName
        - createdTime
        - creatorName
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).