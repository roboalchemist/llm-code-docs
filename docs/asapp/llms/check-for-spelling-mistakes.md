# Source: https://docs.asapp.com/apis/autocompose/check-for-spelling-mistakes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Check for spelling mistakes

> Get spelling correction for a message as it is being typed, if there is a misspelling. Only the current word
will be corrected, once it's fully typed (so it is recommended to call this endpoint after space characters).




## OpenAPI

````yaml api-specs/autocompose.yaml post /autocompose/v1/spellcheck/correction
openapi: 3.0.1
info:
  title: AutoCompose API
  description: >
    Autocompose API to suggest the next agent message.

    Suggestions are based on the conversation history, conversation metadata,
    and

    the in-progress message text the agent has already typed into the composer.
  version: 0.0.3
servers:
  - url: https://api.sandbox.asapp.com
security:
  - API-ID: []
    API-Secret: []
tags:
  - name: AutoCompose
    description: Improve agent productivity with AutoCompose API
paths:
  /autocompose/v1/spellcheck/correction:
    post:
      tags:
        - AutoCompose
      summary: Check for spelling mistakes
      description: >
        Get spelling correction for a message as it is being typed, if there is
        a misspelling. Only the current word

        will be corrected, once it's fully typed (so it is recommended to call
        this endpoint after space characters).
      operationId: getSpellingCorrection
      requestBody:
        description: >-
          The parameters for getting a spelling correction as a message is being
          typed.
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                text:
                  description: >-
                    text being typed by the agent, already entered into the
                    composer
                  type: string
                typingEvent:
                  type: object
                  properties:
                    cursorStart:
                      description: >-
                        position of the cursor before the typing event, to
                        identify if a word is being typed
                      type: integer
                    cursorEnd:
                      description: >-
                        position of the cursor after the typing event, to
                        identify if a word is being typed
                      type: integer
                  required:
                    - cursorStart
                    - cursorEnd
                userDictionary:
                  description: >-
                    Words that should not be corrected if they are present on
                    the text
                  type: array
                  items:
                    type: string
              required:
                - text
                - typingEvent
              example:
                text: 'How is tihs '
                typingEvent:
                  cursorStart: 11
                  cursorEnd: 12
                userDictionary:
                  - Hellooo
      responses:
        '200':
          description: Successfully checked for a spelling mistake.
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    description: >-
                      ID for the spelling correction that was returned (to be
                      used in analytics events)
                    type: string
                    example: 01BX5ZZKBKACTAV9WEVGEMMVS1
                  misspelledText:
                    description: >-
                      misspelling that needs to be replaced with the corrected
                      text
                    type: string
                    example: tihs
                  correctedText:
                    type: string
                    description: correction for the misspelling
                    example: this
                  position:
                    type: integer
                    description: position where the misspelling starts
                    example: 7
        '400':
          description: 400 - Bad request
          content:
            application/json:
              schema:
                description: Bad request response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 400-01
                      message: Bad request
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        '401':
          description: 401 - Unauthorized
          content:
            application/json:
              schema:
                description: Unauthorized response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 401-01
                      message: Unauthorized
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        '403':
          description: 403 - Forbidden
          content:
            application/json:
              schema:
                description: Forbidden response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 403-01
                      message: Forbidden Response
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        '404':
          description: 404 - Not Found
          content:
            application/json:
              schema:
                description: Not Found response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 404-01
                      message: Not Found
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        '409':
          description: 409 - Conflict
          content:
            application/json:
              schema:
                description: Conflict response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 409-01
                      message: Conflict
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        '413':
          description: 413 - Request Entity Too Large
          content:
            application/json:
              schema:
                description: Request Entity Too Large response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 413-01
                      message: Request Entity Too Large
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        '422':
          description: 422 - Unprocessable Entity
          content:
            application/json:
              schema:
                description: Unprocessable Entity response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 422-01
                      message: Unprocessable Entity
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        '429':
          description: 429 - Too Many Requests
          content:
            application/json:
              schema:
                description: Too Many Requests response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 429-01
                      message: Too Many Requests
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        '503':
          description: 503 - Service Unavailable
          content:
            application/json:
              schema:
                description: Service Unavailable response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 503-01
                      message: Service Unavailable
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        default:
          description: 500 - Internal Server Error
          content:
            application/json:
              schema:
                description: Default error response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 500-01
                      message: Internal server error
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
components:
  securitySchemes:
    API-ID:
      type: apiKey
      in: header
      name: asapp-api-id
    API-Secret:
      type: apiKey
      in: header
      name: asapp-api-secret

````