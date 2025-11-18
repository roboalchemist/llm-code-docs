# Source: https://docs.asapp.com/apis/generativeagent/analyze-conversation.md

# Analyze conversation

> Call this API to trigger GenerativeAgent to analyze and respond to a conversation.

This API should be called after a customer sends a message while not speaking with a live agent. The Bot replies will not be returned on this request; they will be delivered asynchronously via the webhook callback.

This API also adds an optional **message** field to create a message for a given conversation before triggering the bot replies. The message object is the exact same message used in the conversations API /message endpoint


## OpenAPI

````yaml api-specs/generativeagent.yaml post /generativeagent/v1/analyze
paths:
  path: /generativeagent/v1/analyze
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              streamId:
                allOf:
                  - type: string
                    description: >-
                      The id associated with the connection where the responses
                      should be sent to.
                    example: 97555020-0276-435f-8104-c378221ba292
              conversationId:
                allOf:
                  - type: string
                    description: Internal conversation identifier from ASAPP
                    example: 01BX5ZZKBKACTAV9WEVGEMMVS0
              taskName:
                allOf:
                  - type: string
                    description: Name of the task to be used in the analysis
                    example: UpgradePlan
              inputVariables:
                allOf:
                  - type: object
                    description: Input variables to be used as context in the analysis.
                    example:
                      call_context: Customer called to upgrade their current plan to GOLD
                      customer_info:
                        current_plan: SILVER
                        customer_since: '2020-01-01'
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
              channelType:
                allOf:
                  - description: >-
                      Channel type used by the current request (digital or
                      voice)
                    type: string
                    enum:
                      - digital
                      - voice
                    example: digital
            required: true
            description: >-
              The parameters for triggering the analysis and response to a
              conversation
            requiredProperties:
              - conversationId
            example:
              conversationId: 01BX5ZZKBKACTAV9WEVGEMMVS0
              message:
                text: Hello, I would like to upgrade my internet plan to GOLD.
                sender:
                  role: agent
                  externalId: 123
                timestamp: '2021-11-23T12:13:14.555Z'
              taskName: UpgradePlan
              inputVariables:
                context: Customer called to upgrade their current plan to GOLD
                customer_info:
                  current_plan: SILVER
                  customer_since: '2020-01-01'
              channelType: digital
        examples:
          example:
            value:
              conversationId: 01BX5ZZKBKACTAV9WEVGEMMVS0
              message:
                text: Hello, I would like to upgrade my internet plan to GOLD.
                sender:
                  role: agent
                  externalId: 123
                timestamp: '2021-11-23T12:13:14.555Z'
              taskName: UpgradePlan
              inputVariables:
                context: Customer called to upgrade their current plan to GOLD
                customer_info:
                  current_plan: SILVER
                  customer_since: '2020-01-01'
              channelType: digital
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              conversationId:
                allOf:
                  - type: string
                    description: Internal conversation identifier from ASAPP
                    example: 01BX5ZZKBKACTAV9WEVGEMMVS0
              messageId:
                allOf:
                  - type: string
                    description: Internal message identifier from ASAPP
                    example: 01BX5ZZKBKACTAV9WEVGEMMVS1
            description: >-
              Conversation identifier and message identifier if passed in the
              request
        examples:
          example:
            value:
              conversationId: 01BX5ZZKBKACTAV9WEVGEMMVS0
              messageId: 01BX5ZZKBKACTAV9WEVGEMMVS1
        description: >-
          Successfully triggered the bot to analyze and respond to a
          conversation
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