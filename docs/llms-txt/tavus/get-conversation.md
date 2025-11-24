# Source: https://docs.tavus.io/api-reference/conversations/get-conversation.md

# Get Conversation

> This endpoint returns a single conversation by its unique identifier.


## OpenAPI

````yaml get /v2/conversations/{conversation_id}
paths:
  path: /v2/conversations/{conversation_id}
  method: get
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
      application/json:
        schemaArray:
          - type: object
            properties:
              conversation_id:
                allOf:
                  - type: string
                    example: c123456
                    description: A unique identifier for the conversation.
              conversation_name:
                allOf:
                  - type: string
                    example: A Meeting with Hassaan
                    description: The name of the conversation.
              conversation_url:
                allOf:
                  - type: string
                    example: https://tavus.daily.co/c123456
                    description: A direct link to join the conversation.
              callback_url:
                allOf:
                  - type: string
                    description: >-
                      The url that will receive webhooks with updates of the
                      conversation state.
                    example: https://yourwebsite.com/webhook
              status:
                allOf:
                  - type: string
                    description: The status of the conversation.
                    example: active
              replica_id:
                allOf:
                  - type: string
                    description: >-
                      A unique identifier for the replica used to create this
                      conversation
                    example: r79e1c033f
              persona_id:
                allOf:
                  - type: string
                    description: >-
                      A unique identifier for the persona used to create this
                      conversation
                    example: p5317866
              created_at:
                allOf:
                  - type: string
                    example: ''
                    description: The date and time the conversation was created.
              updated_at:
                allOf:
                  - type: string
                    example: ''
                    description: >-
                      The date and time of when the conversation was last
                      updated.
        examples:
          example:
            value:
              conversation_id: c123456
              conversation_name: A Meeting with Hassaan
              conversation_url: https://tavus.daily.co/c123456
              callback_url: https://yourwebsite.com/webhook
              status: active
              replica_id: r79e1c033f
              persona_id: p5317866
              created_at: ''
              updated_at: ''
        description: ''
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