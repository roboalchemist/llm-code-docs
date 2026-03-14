# Source: https://tyk.io/docs/api-reference/analytics/get-chat-interactions-for-a-specific-chat.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get chat interactions for a specific chat

> Get the number of interactions for a specific chat over time

## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml get /analytics/chat-interactions-for-chat
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
  /analytics/chat-interactions-for-chat:
    get:
      tags:
        - Analytics
      summary: Get chat interactions for a specific chat
      description: Get the number of interactions for a specific chat over time
      parameters:
        - name: start_date
          in: query
          description: Start date (YYYY-MM-DD)
          required: true
          schema:
            type: string
        - name: end_date
          in: query
          description: End date (YYYY-MM-DD)
          required: true
          schema:
            type: string
        - name: chat_id
          in: query
          description: Chat ID
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/analytics.ChartData'
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
    analytics.ChartData:
      type: object
      properties:
        data:
          type: array
          items:
            type: number
        labels:
          type: array
          items:
            type: string
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
