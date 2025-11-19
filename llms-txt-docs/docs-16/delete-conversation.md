# Source: https://docs.tavus.io/api-reference/conversations/delete-conversation.md

# Delete Conversation

> This endpoint deletes a single conversation by its unique identifier.


## OpenAPI

````yaml delete /v2/conversations/{conversation_id}
paths:
  path: /v2/conversations/{conversation_id}
  method: delete
  servers:
    - url: https://tavusapi.com
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
          cookie: {}
    parameters:
      path:
        conversation_id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the conversation.
              example: c123456
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: NO CONTENT
        examples: {}
        description: NO CONTENT
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid conversation_id
        examples:
          example:
            value:
              error: Invalid conversation_id
        description: Bad Request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid access token
        examples:
          example:
            value:
              message: Invalid access token
        description: UNAUTHORIZED
  deprecated: false
  type: path
components:
  schemas: {}

````