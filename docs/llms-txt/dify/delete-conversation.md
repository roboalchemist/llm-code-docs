# Source: https://docs.dify.ai/api-reference/conversations/delete-conversation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Conversation

> Delete a conversation.



## OpenAPI

````yaml en/api-reference/openapi_chatflow.json delete /conversations/{conversation_id}
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
  /conversations/{conversation_id}:
    delete:
      tags:
        - Conversations
      summary: Delete Conversation
      description: Delete a conversation.
      operationId: deleteAdvancedConversation
      parameters:
        - $ref: '#/components/parameters/ConversationIdPathParam'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - user
              properties:
                user:
                  type: string
                  description: >-
                    The user identifier. **Note**: The Service API does not
                    share conversations created by the WebApp. Conversations
                    created through the API are isolated from those created in
                    the WebApp interface.
      responses:
        '204':
          description: Conversation deleted successfully. No Content.
components:
  parameters:
    ConversationIdPathParam:
      name: conversation_id
      in: path
      required: true
      description: Conversation ID.
      schema:
        type: string
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: API Key authentication.

````

Built with [Mintlify](https://mintlify.com).