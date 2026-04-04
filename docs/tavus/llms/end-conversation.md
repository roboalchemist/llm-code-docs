# Source: https://docs.tavus.io/api-reference/conversations/end-conversation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# End Conversation

> This endpoint ends a single conversation by its unique identifier.




## OpenAPI

````yaml post /v2/conversations/{conversation_id}/end
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
  /v2/conversations/{conversation_id}/end:
    parameters:
      - name: conversation_id
        in: path
        required: true
        description: The unique identifier of the conversation.
        schema:
          type: string
          example: c123456
    post:
      tags:
        - Conversations
      summary: End Conversation
      description: |
        This endpoint ends a single conversation by its unique identifier.
      operationId: endConversation
      responses:
        '200':
          description: OK
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