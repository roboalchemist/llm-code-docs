# Source: https://io.net/docs/reference/rag/conversations/create-a-new-conversation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new conversation

> Create a new conversation. This endpoint initializes a new conversation for the authenticated user.



## OpenAPI

````yaml openapi/rag-conversations/create-a-new-conversation.json post /api/r2r/v3/conversations
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/conversations:
    post:
      summary: Create a new conversation
      description: >-
        Create a new conversation. This endpoint initializes a new conversation
        for the authenticated user.
      operationId: create-a-new-conversation
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: The name of the conversation
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    results:
                      id: id
                      created_at: '2024-01-15T09:30:00Z'
                      user_id: user_id
                      name: name
              schema:
                type: object
                properties:
                  results:
                    type: object
                    properties:
                      id:
                        type: string
                        example: id
                      created_at:
                        type: string
                        example: '2024-01-15T09:30:00Z'
                      user_id:
                        type: string
                        example: user_id
                      name:
                        type: string
                        example: name
        '404':
          description: '404'
          content:
            application/json:
              examples:
                Result:
                  value: {}
              schema:
                type: object
                properties: {}
        '422':
          description: '422'
          content:
            text/plain:
              examples:
                Result:
                  value: ''
      deprecated: false
components:
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````