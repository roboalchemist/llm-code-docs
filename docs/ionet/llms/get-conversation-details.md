# Source: https://io.net/docs/reference/rag/conversations/get-conversation-details.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get conversation details

> Get details of a specific conversation. This endpoint retrieves detailed information about a single conversation identified by its UUID.



## OpenAPI

````yaml openapi/rag-conversations/get-conversation-details.json get /api/r2r/v3/conversations/{id}
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
    get:
      summary: Get conversation details
      description: >-
        Get details of a specific conversation. This endpoint retrieves detailed
        information about a single conversation identified by its UUID.
      operationId: get-conversation-details
      parameters:
        - name: id
          in: path
          description: The unique identifier of the conversation
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
                      - id: id
                        message:
                          role: user
                          content: This is a test message.
                        metadata:
                          key: value
              schema:
                type: object
                properties:
                  results:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          example: id
                        message:
                          type: object
                          properties:
                            role:
                              type: string
                              example: user
                            content:
                              type: string
                              example: This is a test message.
                        metadata:
                          type: object
                          properties:
                            key:
                              type: string
                              example: value
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