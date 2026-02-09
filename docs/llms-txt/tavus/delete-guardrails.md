# Source: https://docs.tavus.io/api-reference/guardrails/delete-guardrails.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Guardrails

> This endpoint deletes a single set of guardrails by its unique identifier.




## OpenAPI

````yaml delete /v2/guardrails/{guardrails_id}
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
  /v2/guardrails/{guardrails_id}:
    parameters:
      - name: guardrails_id
        in: path
        required: true
        description: The unique identifier of the guardrails.
        schema:
          type: string
          example: g12345
    delete:
      tags:
        - Guardrails
      summary: Delete Guardrails
      description: >
        This endpoint deletes a single set of guardrails by its unique
        identifier.
      operationId: deleteGuardrails
      responses:
        '204':
          description: NO CONTENT - Guardrails deleted successfully
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
                    example: Invalid guardrails_id
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
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message.
                    example: Guardrails not found
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````