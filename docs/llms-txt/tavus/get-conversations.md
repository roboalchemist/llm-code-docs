# Source: https://docs.tavus.io/api-reference/conversations/get-conversations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List Conversations

> This endpoint returns a list of all Conversations created by the account associated with the API Key in use.




## OpenAPI

````yaml get /v2/conversations
openapi: 3.0.3
info:
  title: Tavus Developer API Collection
  version: 1.0.0
  contact: {}
servers:
  - url: https://tavusapi.com
security:
  - apiKey: []
tags:
  - name: Videos
  - name: Replicas
  - name: Conversations
  - name: Personas
  - name: Replacements
  - name: Transcriptions
  - name: Documents
paths:
  /v2/conversations:
    get:
      tags:
        - Conversations
      summary: List Conversations
      description: >
        This endpoint returns a list of all Conversations created by the account
        associated with the API Key in use.
      operationId: listConversations
      parameters:
        - in: query
          name: limit
          schema:
            type: integer
          description: The number of conversations to return per page. Default is 10.
        - in: query
          name: page
          schema:
            type: integer
          description: The page number to return. Default is 1.
        - in: query
          name: status
          schema:
            type: string
          description: 'Filter the conversations by status. Possible values: active, ended.'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
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
                    type: integer
                    description: >-
                      The total number of conversations given the filters
                      provided.
        '401':
          description: UNAUTHORIZED
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: The error message.
                    example: Invalid access token
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````