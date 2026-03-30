# Source: https://tyk.io/docs/api-reference/chats/create-a-new-chat.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new chat

> Create a new chat with the provided information

## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml post /chats
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
  /chats:
    post:
      tags:
        - chats
      summary: Create a new chat
      description: Create a new chat with the provided information
      requestBody:
        description: Chat information
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/api.ChatInput'
        required: true
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/api.ChatResponse'
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
      security:
        - BearerAuth: []
components:
  schemas:
    api.ChatInput:
      type: object
      properties:
        data:
          type: object
          properties:
            attributes:
              type: object
              properties:
                group_ids:
                  type: array
                  items:
                    type: integer
                llm_id:
                  type: integer
                llm_settings_id:
                  type: integer
                name:
                  type: string
            type:
              type: string
      description: Chat input model
    api.ChatResponse:
      type: object
      properties:
        attributes:
          type: object
          properties:
            groups:
              type: array
              items:
                $ref: '#/components/schemas/api.GroupResponse'
            llm_id:
              type: integer
            llm_settings_id:
              type: integer
            name:
              type: string
        id:
          type: string
        type:
          type: string
      description: Chat response model
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
    api.GroupResponse:
      type: object
      properties:
        attributes:
          type: object
          properties:
            name:
              type: string
        id:
          type: string
        type:
          type: string
      description: Group response model
  securitySchemes:
    BearerAuth:
      type: apiKey
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).
