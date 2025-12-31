# Source: https://docs.tavus.io/api-reference/conversations/end-conversation.md

# End Conversation

> This endpoint ends a single conversation by its unique identifier.


## OpenAPI

````yaml post /v2/conversations/{conversation_id}/end
paths:
  path: /v2/conversations/{conversation_id}/end
  method: post
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
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: OK
        examples: {}
        description: OK
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