# Source: https://docs.dify.ai/api-reference/conversations/get-conversation-history-messages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Conversation History Messages

> Returns historical chat records in a scrolling load format.



## OpenAPI

````yaml en/api-reference/openapi_chatflow.json get /messages
openapi: 3.0.1
info:
  title: Advanced Chat App API
  description: >-
    Chat applications support session persistence, allowing previous chat
    history to be used as context for responses. This can be applicable for
    chatbot, customer service AI, etc. This version includes advanced features
    like workflow events and more detailed file type support.
  version: 1.0.0
servers:
  - url: '{api_base_url}'
    description: >-
      The base URL for the Advanced Chat App API. Replace {api_base_url} with
      the actual API base URL provided for your application (e.g., from
      props.appDetail.api_base_url).
    variables:
      api_base_url:
        default: https://api.dify.ai/v1
        description: Actual base URL of the API
security:
  - ApiKeyAuth: []
tags:
  - name: Chatflow
    description: Advanced chat operations with workflow events.
  - name: Files
    description: File upload and preview operations for advanced chat.
  - name: End Users
    description: Operations related to end user information.
  - name: Feedback
    description: User feedback operations for advanced chat.
  - name: Conversations
    description: Conversation management for advanced chat.
  - name: TTS
    description: Speech and Text conversion for advanced chat.
  - name: Application
    description: Application settings and info for advanced chat.
  - name: Annotations
    description: Annotation management for advanced chat.
paths:
  /messages:
    get:
      tags:
        - Conversations
      summary: Get Conversation History Messages
      description: Returns historical chat records in a scrolling load format.
      operationId: getAdvancedConversationHistory
      parameters:
        - $ref: '#/components/parameters/ConversationIdQueryParam'
        - $ref: '#/components/parameters/UserQueryParam'
        - name: first_id
          in: query
          description: ID of the first chat record on the current page (for pagination).
          schema:
            type: string
        - $ref: '#/components/parameters/LimitQueryParamDefault20'
      responses:
        '200':
          description: Successfully retrieved conversation history.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ConversationHistoryResponse'
components:
  parameters:
    ConversationIdQueryParam:
      name: conversation_id
      in: query
      required: true
      description: Conversation ID.
      schema:
        type: string
    UserQueryParam:
      name: user
      in: query
      required: true
      description: >-
        User identifier. **Note**: The Service API does not share conversations
        created by the WebApp. Conversations created through the API are
        isolated from those created in the WebApp interface.
      schema:
        type: string
    LimitQueryParamDefault20:
      name: limit
      in: query
      description: Number of items per page.
      schema:
        type: integer
        default: 20
  schemas:
    ConversationHistoryResponse:
      type: object
      properties:
        limit:
          type: integer
        has_more:
          type: boolean
        data:
          type: array
          items:
            $ref: '#/components/schemas/ConversationMessageItem'
    ConversationMessageItem:
      type: object
      properties:
        id:
          type: string
          format: uuid
        conversation_id:
          type: string
          format: uuid
        inputs:
          type: object
          additionalProperties: true
        query:
          type: string
        answer:
          type: string
        message_files:
          type: array
          items:
            $ref: '#/components/schemas/MessageFileItem'
        feedback:
          type: object
          nullable: true
          properties:
            rating:
              type: string
              enum:
                - like
                - dislike
        retriever_resources:
          type: array
          items:
            $ref: '#/components/schemas/RetrieverResource'
        created_at:
          type: integer
          format: int64
    MessageFileItem:
      type: object
      properties:
        id:
          type: string
          format: uuid
        type:
          type: string
        url:
          type: string
          format: url
        belongs_to:
          type: string
          enum:
            - user
            - assistant
    RetrieverResource:
      type: object
      properties:
        position:
          type: integer
        dataset_id:
          type: string
          format: uuid
        dataset_name:
          type: string
        document_id:
          type: string
          format: uuid
        document_name:
          type: string
        segment_id:
          type: string
          format: uuid
        score:
          type: number
          format: float
        content:
          type: string
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: API Key authentication.

````

Built with [Mintlify](https://mintlify.com).