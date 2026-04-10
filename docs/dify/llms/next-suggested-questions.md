# Source: https://docs.dify.ai/api-reference/chatflow/next-suggested-questions.md

# Source: https://docs.dify.ai/api-reference/chat/next-suggested-questions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Next Suggested Questions

> Get next questions suggestions for the current message.



## OpenAPI

````yaml en/api-reference/openapi_chat.json get /messages/{message_id}/suggested
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
  /messages/{message_id}/suggested:
    get:
      tags:
        - Chat
      summary: Next Suggested Questions
      description: Get next questions suggestions for the current message.
      operationId: getSuggestedQuestions
      parameters:
        - name: message_id
          in: path
          required: true
          description: Message ID.
          schema:
            type: string
        - name: user
          in: query
          required: true
          description: >-
            User identifier. **Note**: The Service API does not share
            conversations created by the WebApp. Conversations created through
            the API are isolated from those created in the WebApp interface.
          schema:
            type: string
      responses:
        '200':
          description: Successfully retrieved suggested questions.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuggestedQuestionsResponse'
components:
  schemas:
    SuggestedQuestionsResponse:
      type: object
      properties:
        result:
          type: string
          example: success
        data:
          type: array
          items:
            type: string
          example:
            - a
            - b
            - c
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