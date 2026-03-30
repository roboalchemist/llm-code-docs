# Source: https://io.net/docs/reference/rag/conversations/update-conversation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update conversation

> Update an existing conversation. This endpoint updates the name of an existing conversation identified by its UUID.



## OpenAPI

````yaml openapi/rag-conversations/update-conversation.json post /api/r2r/v3/conversations/{id}
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/conversations/{id}:
    post:
      summary: Update conversation
      description: >-
        Update an existing conversation. This endpoint updates the name of an
        existing conversation identified by its UUID.
      operationId: update-conversation
      parameters:
        - name: id
          in: path
          description: The unique identifier of the conversation to delete
          schema:
            type: string
          required: true
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - name
              properties:
                name:
                  type: string
                  description: The updated name for the conversation
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