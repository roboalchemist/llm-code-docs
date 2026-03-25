# Source: https://docs.dify.ai/api-reference/chat/stop-chat-message-generation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Stop Chat Message Generation

> Stops a chat message generation task. Only supported in streaming mode.



## OpenAPI

````yaml en/api-reference/openapi_chat.json post /chat-messages/{task_id}/stop
openapi: 3.0.1
info:
  title: Chat App API
  description: >-
    Chat applications support session persistence, allowing previous chat
    history to be used as context for responses. This can be applicable for
    chatbot, customer service AI, etc.
  version: 1.0.0
servers:
  - url: '{api_base_url}'
    description: >-
      The base URL for the Chat App API. Replace {api_base_url} with the actual
      API base URL provided for your application (e.g., from
      props.appDetail.api_base_url).
    variables:
      api_base_url:
        default: https://api.dify.ai/v1
        description: Actual base URL of the API
security:
  - ApiKeyAuth: []
tags:
  - name: Chat
    description: Operations related to chat messages and interactions.
  - name: Files
    description: File upload and preview operations.
  - name: End Users
    description: Operations related to end user information.
  - name: Feedback
    description: User feedback operations.
  - name: Conversations
    description: Operations related to managing conversations.
  - name: TTS
    description: Text-to-Speech and Speech-to-Text operations.
  - name: Application
    description: Operations to retrieve application settings and information.
  - name: Annotations
    description: Operations related to managing annotations for direct replies.
paths:
  /chat-messages/{task_id}/stop:
    post:
      tags:
        - Chat
      summary: Stop Chat Message Generation
      description: Stops a chat message generation task. Only supported in streaming mode.
      operationId: stopChatMessageGeneration
      parameters:
        - name: task_id
          in: path
          required: true
          description: >-
            Task ID, can be obtained from the streaming chunk return of a
            `/chat-messages` request.
          schema:
            type: string
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
                    User identifier, must be consistent with the user passed in
                    the send message interface. **Note**: The Service API does
                    not share conversations created by the WebApp. Conversations
                    created through the API are isolated from those created in
                    the WebApp interface.
            examples:
              example:
                value:
                  user: abc-123
      responses:
        '200':
          $ref: '#/components/responses/SuccessResult'
components:
  responses:
    SuccessResult:
      description: Operation successful.
      content:
        application/json:
          schema:
            type: object
            properties:
              result:
                type: string
                example: success
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: >-
        API Key authentication. For all API requests, include your API Key in
        the `Authorization` HTTP Header, prefixed with 'Bearer '. Example:
        `Authorization: Bearer {API_KEY}`. **Strongly recommend storing your API
        Key on the server-side, not shared or stored on the client-side, to
        avoid possible API-Key leakage that can lead to serious consequences.**

````

Built with [Mintlify](https://mintlify.com).