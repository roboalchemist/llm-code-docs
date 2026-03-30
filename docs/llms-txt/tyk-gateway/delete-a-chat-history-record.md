# Source: https://tyk.io/docs/api-reference/chat-history/delete-a-chat-history-record.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a chat history record

> Delete a chat history record by its ID

## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml delete /chat-history-records/{id}
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
  /chat-history-records/{id}:
    delete:
      tags:
        - chat-history
      summary: Delete a chat history record
      description: Delete a chat history record by its ID
      parameters:
        - name: id
          in: path
          description: Chat History Record ID
          required: true
          schema:
            type: integer
      responses:
        '204':
          description: No Content
          content: {}
        '404':
          description: Not Found
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
