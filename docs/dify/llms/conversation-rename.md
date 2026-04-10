# Source: https://docs.dify.ai/api-reference/conversations/conversation-rename.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Conversation Rename

> Rename the session.



## OpenAPI

````yaml en/api-reference/openapi_chatflow.json post /conversations/{conversation_id}/name
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
  /conversations/{conversation_id}/name:
    post:
      tags:
        - Conversations
      summary: Conversation Rename
      description: Rename the session.
      operationId: renameAdvancedConversation
      parameters:
        - $ref: '#/components/parameters/ConversationIdPathParam'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ConversationRenameRequest'
      responses:
        '200':
          description: Conversation renamed successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ConversationRenameResponse'
components:
  parameters:
    ConversationIdPathParam:
      name: conversation_id
      in: path
      required: true
      description: Conversation ID.
      schema:
        type: string
  schemas:
    ConversationRenameRequest:
      type: object
      required:
        - user
      properties:
        name:
          type: string
          nullable: true
        auto_generate:
          type: boolean
          default: false
        user:
          type: string
    ConversationRenameResponse:
      $ref: '#/components/schemas/ConversationListItem'
    ConversationListItem:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        inputs:
          type: object
          additionalProperties: true
        status:
          type: string
        introduction:
          type: string
          nullable: true
        created_at:
          type: integer
          format: int64
        updated_at:
          type: integer
          format: int64
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: API Key authentication.

````

Built with [Mintlify](https://mintlify.com).