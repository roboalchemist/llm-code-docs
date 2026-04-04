# Source: https://io.net/docs/reference/rag/conversations/delete-a-conversation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a conversation

> Delete an existing conversation. This endpoint deletes a conversation identified by its UUID.



## OpenAPI

````yaml openapi/rag-conversations/delete-a-conversation.json delete /api/r2r/v3/conversations/{id}
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
    delete:
      summary: Delete a conversation
      description: >-
        Delete an existing conversation. This endpoint deletes a conversation
        identified by its UUID.
      operationId: delete-a-conversation
      parameters:
        - name: id
          in: path
          description: The unique identifier of the conversation to delete
          schema:
            type: string
          required: true
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    results:
                      success: true
              schema:
                type: object
                properties:
                  results:
                    type: object
                    properties:
                      success:
                        type: boolean
                        example: true
                        default: true
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