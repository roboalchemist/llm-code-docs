# Source: https://docs.tavus.io/api-reference/personas/delete-persona.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Persona

> This endpoint deletes a single persona by its unique identifier.




## OpenAPI

````yaml delete /v2/personas/{persona_id}
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
  /v2/personas/{persona_id}:
    parameters:
      - name: persona_id
        in: path
        required: true
        description: The unique identifier of the persona.
        schema:
          type: string
          example: pf3073f2dcc1
    delete:
      tags:
        - Personas
      summary: Delete Persona
      description: |
        This endpoint deletes a single persona by its unique identifier.
      operationId: deletePersona
      parameters:
        - name: persona_id
          in: path
          required: true
          description: The unique identifier of the persona.
          schema:
            type: string
            example: pf3073f2dcc1
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
                    example: Invalid persona_id
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