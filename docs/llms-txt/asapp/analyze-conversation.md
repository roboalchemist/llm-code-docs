# Source: https://docs.asapp.com/apis/generativeagent/analyze-conversation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Analyze conversation

> Call this API to trigger GenerativeAgent to analyze and respond to a conversation.

This API should be called after a customer sends a message while not speaking with a live agent. The Bot replies will not be returned on this request; they will be delivered asynchronously via the webhook callback.

This API also adds an optional **message** field to create a message for a given conversation before triggering the bot replies. The message object is the exact same message used in the conversations API /message endpoint




## OpenAPI

````yaml api-specs/generativeagent.yaml post /generativeagent/v1/analyze
openapi: 3.0.1
info:
  title: GenerativeAgent API
  description: >
    GenerativeAgent API allows customers to interact with a chat / voice
    automation bot leveraging LLMs by sending messages and receiving responses
    asynchronously through webhooks
  contact:
    email: api-info@asapp.com
  license:
    name: ASAPP Software License
    url: https://api.asapp.com/LICENSE
  version: '0.1'
servers:
  - url: https://api.sandbox.asapp.com
security:
  - API-ID: []
    API-Secret: []
tags:
  - name: GenerativeAgent
    description: >-
      Operations to send messages and trigger GenerativeAgent to respond or
      query the current state
paths:
  /generativeagent/v1/analyze:
    post:
      tags:
        - GenerativeAgent
      summary: Analyze conversation
      description: >
        Call this API to trigger GenerativeAgent to analyze and respond to a
        conversation.


        This API should be called after a customer sends a message while not
        speaking with a live agent. The Bot replies will not be returned on this
        request; they will be delivered asynchronously via the webhook callback.


        This API also adds an optional **message** field to create a message for
        a given conversation before triggering the bot replies. The message
        object is the exact same message used in the conversations API /message
        endpoint
      operationId: postAnalyze
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              description: >-
                The parameters for triggering the analysis and response to a
                conversation
              properties:
                streamId:
                  type: string
                  description: >-
                    The id associated with the connection where the responses
                    should be sent to.
                  example: 97555020-0276-435f-8104-c378221ba292
                conversationId:
                  type: string
                  description: Internal conversation identifier from ASAPP
                  example: 01BX5ZZKBKACTAV9WEVGEMMVS0
                taskName:
                  type: string
                  description: Name of the task to be used in the analysis
                  example: UpgradePlan
                inputVariables:
                  type: object
                  description: Input variables to be used as context in the analysis.
                  example:
                    call_context: Customer called to upgrade their current plan to GOLD
                    customer_info:
                      current_plan: SILVER
                      customer_since: '2020-01-01'
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
                channelType:
                  description: Channel type used by the current request (digital or voice)
                  type: string
                  enum:
                    - digital
                    - voice
                  example: digital
              required:
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
      responses:
        '200':
          description: >-
            Successfully triggered the bot to analyze and respond to a
            conversation
          content:
            application/json:
              schema:
                type: object
                description: >-
                  Conversation identifier and message identifier if passed in
                  the request
                properties:
                  conversationId:
                    type: string
                    description: Internal conversation identifier from ASAPP
                    example: 01BX5ZZKBKACTAV9WEVGEMMVS0
                  messageId:
                    type: string
                    description: Internal message identifier from ASAPP
                    example: 01BX5ZZKBKACTAV9WEVGEMMVS1
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