# Source: https://docs.tavus.io/api-reference/conversations/get-conversations.md

# List Conversations

> This endpoint returns a list of all Conversations created by the account associated with the API Key in use.


## OpenAPI

````yaml get /v2/conversations
paths:
  path: /v2/conversations
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
      path: {}
      query:
        limit:
          schema:
            - type: integer
              description: The number of conversations to return per page. Default is 10.
        page:
          schema:
            - type: integer
              description: The page number to return. Default is 1.
        status:
          schema:
            - type: string
              description: >-
                Filter the conversations by status. Possible values: active,
                ended.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        conversation_id:
                          type: string
                          description: A unique identifier for the conversation.
                          example: c123456
                        conversation_name:
                          type: string
                          description: A name for the conversation.
                          example: A Meeting with Hassaan
                        status:
                          type: string
                          description: The status of the video.
                          example: active
                        conversation_url:
                          type: string
                          description: A direct link to join the conversation.
                          example: https://tavus.daily.co/c123456
                        callback_url:
                          type: string
                          description: >-
                            The url that will receive webhooks with updates of
                            the conversation state.
                          example: https://yourwebsite.com/webhook
                        replica_id:
                          type: string
                          description: >-
                            A unique identifier for the replica used to create
                            this conversation
                          example: r79e1c033f
                        persona_id:
                          type: string
                          description: >-
                            A unique identifier for the persona used to create
                            this conversation
                          example: p5317866
                        created_at:
                          type: string
                          description: The date and time the conversation was created.
                          example: ''
                        updated_at:
                          type: string
                          description: >-
                            The date and time of when the conversation was last
                            updated.
              total_count:
                allOf:
                  - type: integer
                    description: >-
                      The total number of conversations given the filters
                      provided.
        examples:
          example:
            value:
              data:
                - conversation_id: c123456
                  conversation_name: A Meeting with Hassaan
                  status: active
                  conversation_url: https://tavus.daily.co/c123456
                  callback_url: https://yourwebsite.com/webhook
                  replica_id: r79e1c033f
                  persona_id: p5317866
                  created_at: ''
                  updated_at: <string>
              total_count: 123
        description: ''
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