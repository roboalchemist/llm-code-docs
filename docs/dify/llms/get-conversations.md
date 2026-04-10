# Source: https://docs.dify.ai/api-reference/conversations/get-conversations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Conversations

> Retrieve the conversation list for the current user.



## OpenAPI

````yaml en/api-reference/openapi_chatflow.json get /conversations
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
  /conversations:
    get:
      tags:
        - Conversations
      summary: Get Conversations
      description: Retrieve the conversation list for the current user.
      operationId: getAdvancedConversationsList
      parameters:
        - $ref: '#/components/parameters/UserQueryParam'
        - $ref: '#/components/parameters/LastIdQueryParam'
        - $ref: '#/components/parameters/LimitQueryParamDefault20Max100'
        - $ref: '#/components/parameters/SortByQueryParam'
      responses:
        '200':
          description: Successfully retrieved conversations list.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ConversationsListResponse'
components:
  parameters:
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
    SortByQueryParam:
      name: sort_by
      in: query
      description: Sorting field (e.g., -updated_at).
      schema:
        type: string
        enum:
          - created_at
          - '-created_at'
          - updated_at
          - '-updated_at'
        default: '-updated_at'
  schemas:
    ConversationsListResponse:
      type: object
      properties:
        limit:
          type: integer
        has_more:
          type: boolean
        data:
          type: array
          items:
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