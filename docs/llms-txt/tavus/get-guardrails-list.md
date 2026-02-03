# Source: https://docs.tavus.io/api-reference/guardrails/get-guardrails-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Guardrails (All Sets)

> This endpoint returns a list of all sets of guardrails.




## OpenAPI

````yaml get /v2/guardrails
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
  /v2/guardrails:
    get:
      tags:
        - Guardrails
      summary: Get Guardrails (All Sets)
      description: |
        This endpoint returns a list of all sets of guardrails.
      operationId: getGuardrails
      parameters:
        - in: query
          name: limit
          schema:
            type: integer
          description: The number of guardrails to return per page. Default is 10.
        - in: query
          name: page
          schema:
            type: integer
          description: The page number to return. Default is 1.
      responses:
        '200':
          description: Successfully retrieved guardrails
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
                        guardrails_id:
                          type: string
                          description: Unique identifier for the guardrails
                          example: g12345
                        created_at:
                          type: string
                          description: >-
                            ISO 8601 timestamp of when the guardrails were
                            created
                          example: '2024-01-15T10:30:00Z'
                        updated_at:
                          type: string
                          description: >-
                            ISO 8601 timestamp of when the guardrails were last
                            updated
                          example: '2024-01-15T10:30:00Z'
                  total_count:
                    type: integer
                    description: The total number of guardrails
                    example: 15
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