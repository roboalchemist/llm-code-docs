# Source: https://docs.asapp.com/apis/conversations/create-or-update-a-conversation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create or update a conversation

> Creates a new conversation or updates an existing one based on the provided `externalId`.

Use this endpoint when:
- Starting a new conversation
- Updating conversation details (e.g., reassigning to a different agent)

If the `externalId` is not found, a new conversation will be created. Otherwise, the existing conversation will be updated.




## OpenAPI

````yaml api-specs/conversations.yaml post /conversation/v1/conversations
openapi: 3.0.1
info:
  title: Conversations API
  description: Operations to manage ASAPP conversations
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
  - name: Conversations
    description: Operations to send conversational inputs to ASAPP AI services
paths:
  /conversation/v1/conversations:
    post:
      tags:
        - Conversations
      summary: Create or update a conversation
      description: >
        Creates a new conversation or updates an existing one based on the
        provided `externalId`.


        Use this endpoint when:

        - Starting a new conversation

        - Updating conversation details (e.g., reassigning to a different agent)


        If the `externalId` is not found, a new conversation will be created.
        Otherwise, the existing conversation will be updated.
      operationId: createOrUpdateConversation
      requestBody:
        required: true
        content:
          application/json:
            schema:
              description: >-
                Conversation between an agent and a customer that requires a
                timestamp of creation
              type: object
              properties:
                id:
                  type: string
                  description: The identifier of the conversation.
                externalId:
                  type: string
                  description: Your unique identifier for a conversation.
                agent:
                  type: object
                  description: >-
                    Information about the agent participating in the
                    conversation.
                  properties:
                    externalId:
                      type: string
                      description: >-
                        The unique identifier for the agent in your external
                        system.
                    name:
                      type: string
                      description: The display name of the agent.
                  required:
                    - externalId
                customer:
                  type: object
                  description: >-
                    Information about the customer participating in the
                    conversation.
                  properties:
                    externalId:
                      type: string
                      description: >-
                        The unique identifier for the customer in your external
                        system.
                    name:
                      type: string
                      description: The display name of the customer.
                  required:
                    - externalId
                metadata:
                  type: object
                  additionalProperties:
                    type: string
                  description: >-
                    Additional key-value pairs to store custom metadata about
                    the conversation. Use this for filtering or categorization
                    purposes.
                timestamp:
                  type: string
                  format: date-time
                  description: >-
                    The time when the conversation was created. Include the
                    timezone, otherwise UTC will be assumed.
              required:
                - externalId
                - customer
                - timestamp
              example:
                externalId: id-111
                agent:
                  externalId: agent-111
                  name: agent-x
                customer:
                  externalId: customer-x
                  name: customer-name-x
                metadata:
                  organizationalGroup: some-group
                  subdivision: some-division
                  queue: some-queue
                timestamp: '2021-11-23T12:13:14.555Z'
      responses:
        '200':
          description: Successfully created or updated conversation
          content:
            application/json:
              schema:
                description: Response for conversation
                type: object
                properties:
                  id:
                    type: string
                    description: The identifier of the conversation.
                example:
                  id: 01BX5ZZKBKACTAV9WEVGEMMVRZ
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