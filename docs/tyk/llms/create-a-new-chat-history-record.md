# Source: https://tyk.io/docs/api-reference/chat-history/create-a-new-chat-history-record.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new chat history record

> Create a new chat history record with the given input



## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml post /chat-history-records
openapi: 3.0.1
info:
  title: AI Studio API
  description: This is the API for the AI Studio user and group management system.
  termsOfService: http://swagger.io/terms/
  contact:
    name: API Support
    url: http://www.swagger.io/support
    email: support@tyk.io
  license:
    name: Apache 2.0
    url: http://www.apache.org/licenses/LICENSE-2.0.html
  version: '1.0'
servers:
  - url: //localhost:8080/api/v1
security:
  - BearerAuth: []
paths:
  /chat-history-records:
    post:
      tags:
        - chat-history
      summary: Create a new chat history record
      description: Create a new chat history record with the given input
      requestBody:
        description: Chat History Record Input
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/api.ChatHistoryRecordInput'
        required: true
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/api.ChatHistoryRecordResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/api.ErrorResponse'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/api.ErrorResponse'
components:
  schemas:
    api.ChatHistoryRecordInput:
      type: object
      properties:
        data:
          type: object
          properties:
            attributes:
              type: object
              properties:
                chat_id:
                  type: integer
                name:
                  type: string
                session_id:
                  type: string
                user_id:
                  type: integer
            type:
              type: string
      description: Chat History Record input model
    api.ChatHistoryRecordResponse:
      type: object
      properties:
        attributes:
          type: object
          properties:
            chat_id:
              type: integer
            name:
              type: string
            session_id:
              type: string
            user_id:
              type: integer
        id:
          type: string
        type:
          type: string
      description: Chat History Record response model
    api.ErrorResponse:
      type: object
      properties:
        errors:
          type: array
          items:
            type: object
            properties:
              detail:
                type: string
              title:
                type: string
      description: Error response model
  securitySchemes:
    BearerAuth:
      type: apiKey
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).