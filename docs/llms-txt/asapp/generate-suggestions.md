# Source: https://docs.asapp.com/apis/autocompose/generate-suggestions.md

# Generate suggestions

> Get suggestions for the next agent message in the conversation. 

There are several times when this should be called:
- when an agent joins the conversation,
- after a message is sent by either the customer or the agent,
- and as the agent is typing in the composer (to enable completing the agent's in-progress message).

Optionally, add a message to the conversation.


## OpenAPI

````yaml api-specs/autocompose.yaml post /autocompose/v1/conversations/{conversationId}/suggestions
paths:
  path: /autocompose/v1/conversations/{conversationId}/suggestions
  method: post
  servers:
    - url: https://api.sandbox.asapp.com
  request:
    security:
      - title: API ID & API Secret
        parameters:
          query: {}
          header:
            asapp-api-id:
              type: apiKey
            asapp-api-secret:
              type: apiKey
          cookie: {}
    parameters:
      path:
        conversationId:
          schema:
            - type: string
              required: true
              description: The identifier for a conversation.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              query:
                allOf:
                  - description: text the agent has already entered into the composer
                    type: string
              message:
                allOf:
                  - description: Represents a single message within a conversation.
                    type: object
                    properties:
                      text:
                        type: string
                        minLength: 1
                        description: The content of the message.
                      sender:
                        description: >-
                          Information about the participant who sent the
                          message.
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
            description: >-
              A suggestions request with an optional message to add to the
              conversation
            example:
              query: Hello, how can
              message:
                text: Hello, I would like to upgrade my internet plan to GOLD.
                sender:
                  role: customer
                  externalId: customer-x
                timestamp: '2023-06-01T19:16:55.706Z'
        examples:
          example:
            value:
              query: Hello, how can
              message:
                text: Hello, I would like to upgrade my internet plan to GOLD.
                sender:
                  role: customer
                  externalId: customer-x
                timestamp: '2023-06-01T19:16:55.706Z'
        description: The parameters for getting suggestions for the next agent message.
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - description: >-
                      ID for the suggestions that were returned (to be used in
                      analytics events)
                    type: string
              message:
                allOf:
                  - description: Response for messages
                    type: object
                    properties:
                      id:
                        type: string
                        description: Message ID to be used for analytics
                    example:
                      id: 01BX5ZZKBKACTAV9WEVGEMMVS1
              suggestions:
                allOf:
                  - type: array
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
                allOf:
                  - description: >-
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
                allOf:
                  - description: Recommended message for the agent to autopilot send.
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
            description: Suggestions for next agent message
        examples:
          example:
            value:
              id: <string>
              message:
                id: 01BX5ZZKBKACTAV9WEVGEMMVS1
              suggestions:
                - text: Hello John, how can I help you?
                  templateText: Hello {NAME}, how can I help you?
                  title: Greeting
              phraseCompletion:
                text: Hello, how can I help you?
              autopilotMessage:
                text: Hello John, how can I help you?
                templateText: Hello {NAME}, how can I help you?
                title: Greeting
                delaySeconds: 5
                triggerAfterSeconds: 0
        description: Successfully fetched suggestions for the conversation
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Bad request response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 400-01
                message: Bad request
        description: 400 - Bad request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Unauthorized response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 401-01
                message: Unauthorized
        description: 401 - Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Forbidden response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 403-01
                message: Forbidden Response
        description: 403 - Forbidden
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Not Found response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 404-01
                message: Not Found
        description: 404 - Not Found
    '409':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Conflict response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 409-01
                message: Conflict
        description: 409 - Conflict
    '413':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Request Entity Too Large response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 413-01
                message: Request Entity Too Large
        description: 413 - Request Entity Too Large
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Unprocessable Entity response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 422-01
                message: Unprocessable Entity
        description: 422 - Unprocessable Entity
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Too Many Requests response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 429-01
                message: Too Many Requests
        description: 429 - Too Many Requests
    '503':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Service Unavailable response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 503-01
                message: Service Unavailable
        description: 503 - Service Unavailable
    default:
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Default error response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 500-01
                message: Internal server error
        description: 500 - Internal Server Error
  deprecated: false
  type: path
components:
  schemas: {}

````