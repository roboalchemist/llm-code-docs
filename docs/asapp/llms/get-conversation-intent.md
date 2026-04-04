# Source: https://docs.asapp.com/apis/autosummary/get-conversation-intent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get conversation intent

> Retrieves the primary intent of a conversation, represented by both an intent code and a human-readable intent name. If no intent is detected, "NO_INTENT" is returned.

This endpoint requires:
1. Intent support to be explicitly enabled for your account.
2. A valid conversationId, which is an ASAPP-generated identifier created when using the ASAPP /conversations endpoint.

Use this endpoint to gain insights into the main purpose or topic of a conversation.




## OpenAPI

````yaml api-specs/autosummary.yaml get /autosummary/v1/intent/{conversationId}
openapi: 3.0.0
info:
  title: AutoSummary API
  description: >
    This is the AutoSummary API which can be used for summarizing conversations.
    It offers two kind of summaries, structured UMR tags or generated free text.
    In addition, it allows structured data about the conversation to be
    retrieved. The usual usage flow consist on first publishing the content of
    the conversation on Conversations API and, once it has finished, invoking
    the corresponding summarization endpoint of this API. A single request
    containing a reference to the conversation is received and a response
    including the corresponding summary or structured data is returned.


    By automating this activity, organizations decrease after-call work,
    reducing agent time and effort, and produce consistent, structured summaries
    and data well-suited for analytics.
  version: 1.0.0
servers:
  - url: https://api.sandbox.asapp.com
security:
  - API-ID: []
    API-Secret: []
tags:
  - name: AutoSummary
    description: Endpoints for summarizing conversations and retrieving structured data
paths:
  /autosummary/v1/intent/{conversationId}:
    parameters:
      - name: conversationId
        description: The identifier for a conversation.
        in: path
        required: true
        schema:
          type: string
          pattern: ^[A-Z0-9]+$
    get:
      tags:
        - AutoSummary
      summary: Get conversation intent
      description: >
        Retrieves the primary intent of a conversation, represented by both an
        intent code and a human-readable intent name. If no intent is detected,
        "NO_INTENT" is returned.


        This endpoint requires:

        1. Intent support to be explicitly enabled for your account.

        2. A valid conversationId, which is an ASAPP-generated identifier
        created when using the ASAPP /conversations endpoint.


        Use this endpoint to gain insights into the main purpose or topic of a
        conversation.
      operationId: getIntent
      responses:
        '200':
          description: Successfully generated intent.
          content:
            application/json:
              schema:
                type: object
                properties:
                  conversationId:
                    type: string
                    description: The id of the conversation.
                  intent:
                    description: >
                      An object containing the determined intent for the
                      conversation.
                    type: object
                    properties:
                      code:
                        type: string
                        description: >-
                          The machine-readable code for the given conversation.
                          If no intent was found, then "NO_INTENT" is returned.
                      name:
                        type: string
                        description: >-
                          The human-readable name of the intent for the given
                          conversation.
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