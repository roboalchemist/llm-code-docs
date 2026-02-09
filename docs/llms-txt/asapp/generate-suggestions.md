# Source: https://docs.asapp.com/apis/autocompose/generate-suggestions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate suggestions

> Get suggestions for the next agent message in the conversation. 

There are several times when this should be called:
- when an agent joins the conversation,
- after a message is sent by either the customer or the agent,
- and as the agent is typing in the composer (to enable completing the agent's in-progress message).

Optionally, add a message to the conversation.




## OpenAPI

````yaml api-specs/autocompose.yaml post /autocompose/v1/conversations/{conversationId}/suggestions
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
  /autocompose/v1/conversations/{conversationId}/suggestions:
    parameters:
      - name: conversationId
        description: The identifier for a conversation.
        in: path
        required: true
        schema:
          type: string
          pattern: ^[A-Z0-9]+$
    post:
      tags:
        - AutoCompose
      summary: Generate suggestions
      description: >
        Get suggestions for the next agent message in the conversation. 


        There are several times when this should be called:

        - when an agent joins the conversation,

        - after a message is sent by either the customer or the agent,

        - and as the agent is typing in the composer (to enable completing the
        agent's in-progress message).


        Optionally, add a message to the conversation.
      operationId: getSuggestions
      requestBody:
        description: The parameters for getting suggestions for the next agent message.
        content:
          application/json:
            schema:
              description: >-
                A suggestions request with an optional message to add to the
                conversation
              type: object
              properties:
                query:
                  description: text the agent has already entered into the composer
                  type: string
                message:
                  description: Represents a single message within a conversation.
                  type: object
                  properties:
                    text:
                      type: string
                      minLength: 1
                      description: The content of the message.
                    sender:
                      description: Information about the participant who sent the message.
                      type: object
                      properties:
                        role:
                          description: The role of the participant in the conversation.
                          type: string
                          enum:
                            - agent
                            - customer
                            - system
                        externalId:
                          type: string
                          description: >-
                            The unique identifier for the participant in your
                            external system. This should be consistent across
                            all interactions for the same individual.
                      required:
                        - role
                        - externalId
                    timestamp:
                      type: string
                      format: date-time
                      description: >-
                        The time when the message was sent. Include the
                        timezone, otherwise UTC will be assumed.
                  required:
                    - text
                    - sender
                    - timestamp
                  example:
                    text: Hello, I would like to upgrade my internet plan to GOLD.
                    sender:
                      role: agent
                      externalId: 123
                    timestamp: '2021-11-23T12:13:14.555Z'
              example:
                query: Hello, how can
                message:
                  text: Hello, I would like to upgrade my internet plan to GOLD.
                  sender:
                    role: customer
                    externalId: customer-x
                  timestamp: '2023-06-01T19:16:55.706Z'
      responses:
        '200':
          description: Successfully fetched suggestions for the conversation
          content:
            application/json:
              schema:
                description: Suggestions for next agent message
                type: object
                properties:
                  id:
                    description: >-
                      ID for the suggestions that were returned (to be used in
                      analytics events)
                    type: string
                  message:
                    description: Response for messages
                    type: object
                    properties:
                      id:
                        type: string
                        description: Message ID to be used for analytics
                    example:
                      id: 01BX5ZZKBKACTAV9WEVGEMMVS1
                  suggestions:
                    type: array
                    items:
                      description: Suggestion
                      type: object
                      properties:
                        text:
                          type: string
                          description: Suggestion text for the agent
                          example: Hello John, how can I help you?
                        templateText:
                          type: string
                          description: >-
                            Suggestion text with placeholders for metadata
                            instead of the values filled in
                          example: Hello {NAME}, how can I help you?
                        title:
                          type: string
                          description: The title of the response
                          example: Greeting
                  phraseCompletion:
                    description: >-
                      Completion of the phrase the agent is currently typing, to
                      be displayed inline in the composer
                    type: object
                    properties:
                      text:
                        type: string
                        description: >-
                          Phrase completion text for the agent (this may be
                          empty if the model does not have a confident
                          prediction for how to complete the message)
                        example: Hello, how can I help you?
                  autopilotMessage:
                    description: Recommended message for the agent to autopilot send.
                    type: object
                    properties:
                      text:
                        type: string
                        description: Text of the message
                        example: Hello John, how can I help you?
                      templateText:
                        type: string
                        description: >-
                          Text of the message with placeholders for metadata
                          instead of the values filled in
                        example: Hello {NAME}, how can I help you?
                      title:
                        type: string
                        description: The title of the message
                        example: Greeting
                      delaySeconds:
                        type: integer
                        description: >-
                          Delay before the message is sent to the customer,
                          during which a preview of the message is shown to the
                          agent and they can choose to cancel it
                        example: 5
                      triggerAfterSeconds:
                        type: integer
                        description: >-
                          Delay before showing the preview and starting the
                          countdown to send the message
                        example: 0
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