# Source: https://docs.dify.ai/api-reference/conversations/get-conversation-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Conversation Variables

> Retrieve variables from a specific conversation.



## OpenAPI

````yaml en/api-reference/openapi_chatflow.json get /conversations/{conversation_id}/variables
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
  /conversations/{conversation_id}/variables:
    get:
      tags:
        - Conversations
      summary: Get Conversation Variables
      description: Retrieve variables from a specific conversation.
      operationId: getAdvancedConversationVariables
      parameters:
        - $ref: '#/components/parameters/ConversationIdPathParam'
        - $ref: '#/components/parameters/UserQueryParam'
        - $ref: '#/components/parameters/LastIdQueryParam'
        - $ref: '#/components/parameters/LimitQueryParamDefault20Max100'
      responses:
        '200':
          description: Successfully retrieved conversation variables.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ConversationVariablesResponse'
        '404':
          $ref: '#/components/responses/ConversationNotFound'
components:
  parameters:
    ConversationIdPathParam:
      name: conversation_id
      in: path
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
    LastIdQueryParam:
      name: last_id
      in: query
      description: ID of the last record for pagination.
      schema:
        type: string
    LimitQueryParamDefault20Max100:
      name: limit
      in: query
      description: Number of items per page (Default 20, Max 100).
      schema:
        type: integer
        default: 20
        minimum: 1
        maximum: 100
  schemas:
    ConversationVariablesResponse:
      type: object
      properties:
        limit:
          type: integer
        has_more:
          type: boolean
        data:
          type: array
          items:
            $ref: '#/components/schemas/ConversationVariableItem'
    ConversationVariableItem:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        value_type:
          type: string
        value:
          type: string
        description:
          type: string
          nullable: true
        created_at:
          type: integer
          format: int64
        updated_at:
          type: integer
          format: int64
    ErrorResponse:
      type: object
      properties:
        status:
          type: integer
          nullable: true
        code:
          type: string
          nullable: true
        message:
          type: string
  responses:
    ConversationNotFound:
      description: Conversation not found.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: API Key authentication.

````

Built with [Mintlify](https://mintlify.com).