# Source: https://docs.tavus.io/api-reference/conversations/delete-conversation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Conversation

> This endpoint deletes a single conversation by its unique identifier.




## OpenAPI

````yaml delete /v2/conversations/{conversation_id}
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
    delete:
      tags:
        - Conversations
      summary: Delete Conversation
      description: |
        This endpoint deletes a single conversation by its unique identifier.
      operationId: deleteConversation
      parameters:
        - name: hard
          in: query
          schema:
            type: boolean
            example: true
          description: >-
            If set to true, the conversation and associated assets will be hard
            deleted. CAUTION: This action is irrevocable.
      responses:
        '204':
          description: NO CONTENT
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