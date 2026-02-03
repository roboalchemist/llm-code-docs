# Source: https://docs.tavus.io/api-reference/conversations/get-conversation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Conversation

> This endpoint returns a single conversation by its unique identifier.


<Accordion title="Verbose Response Data" icon="lightbulb">
  You can append `?verbose=true` to the URL to receive additional event data in the response, including:

  * `shutdown_reason`: The reason why the conversation ended (e.g., "participant\_left\_timeout")
  * `transcript`: A complete transcript of the conversation with role-based messages (via `application.transcription_ready`)
  * `system.replica_joined`: When the replica joined the conversation
  * `system.shutdown`: When and why the conversation ended
  * `application.perception_analysis`: The final visual analysis of the user that includes their appearance, behavior, emotional states, and screen activities

  This is particularly useful as an alternative to using the `callback_url` parameter on the <a href="/api-reference/conversations/create-conversation" target="_blank" rel="noopener noreferrer">create conversation</a> endpoint for retrieving detailed conversation data.
</Accordion>


## OpenAPI

````yaml get /v2/conversations/{conversation_id}
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
  /v2/conversations/{conversation_id}:
    parameters:
      - name: conversation_id
        in: path
        required: true
        description: The unique identifier of the conversation.
        schema:
          type: string
          example: c123456
    get:
      tags:
        - Conversations
      summary: Get Conversation
      description: |
        This endpoint returns a single conversation by its unique identifier.
      operationId: getConversation
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  conversation_id:
                    type: string
                    description: A unique identifier for the conversation.
                    example: c123456
                  conversation_name:
                    type: string
                    description: The name of the conversation.
                    example: A Meeting with Hassaan
                  conversation_url:
                    type: string
                    description: A direct link to join the conversation.
                    example: https://tavus.daily.co/c123456
                  callback_url:
                    type: string
                    description: >-
                      The url that will receive webhooks with updates of the
                      conversation state.
                    example: https://yourwebsite.com/webhook
                  status:
                    type: string
                    description: The status of the conversation.
                    example: active
                  replica_id:
                    type: string
                    description: >-
                      A unique identifier for the replica used to create this
                      conversation
                    example: r79e1c033f
                  persona_id:
                    type: string
                    description: >-
                      A unique identifier for the persona used to create this
                      conversation
                    example: p5317866
                  created_at:
                    type: string
                    description: The date and time the conversation was created.
                    example: ''
                  updated_at:
                    type: string
                    example: ''
                    description: >-
                      The date and time of when the conversation was last
                      updated.
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message.
                    example: Invalid conversation_id
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