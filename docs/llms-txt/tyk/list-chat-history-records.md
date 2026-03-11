# Source: https://tyk.io/docs/api-reference/chat-history/list-chat-history-records.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List chat history records

> List chat history records for a given user



## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml get /chat-history-records
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
    get:
      tags:
        - chat-history
      summary: List chat history records
      description: List chat history records for a given user
      parameters:
        - name: user_id
          in: query
          description: User ID
          required: true
          schema:
            type: integer
        - name: page
          in: query
          description: Page number
          schema:
            type: integer
        - name: page_size
          in: query
          description: Page size
          schema:
            type: integer
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/api.ChatHistoryRecordListResponse'
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
    api.ChatHistoryRecordListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/api.ChatHistoryRecordResponse'
      description: Chat History Record list response model
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
  securitySchemes:
    BearerAuth:
      type: apiKey
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).