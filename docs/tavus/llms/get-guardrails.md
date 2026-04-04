# Source: https://docs.tavus.io/api-reference/guardrails/get-guardrails.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Guardrails (One Set)

> This endpoint returns a single set of guardrails by its unique identifier.




## OpenAPI

````yaml get /v2/guardrails/{guardrails_id}
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
    get:
      tags:
        - Guardrails
      summary: Get Guardrails (One Set)
      description: >
        This endpoint returns a single set of guardrails by its unique
        identifier.
      operationId: getGuardrail
      responses:
        '200':
          description: Successfully retrieved guardrails
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      guardrail_name:
                        type: string
                        description: >-
                          Name of the individual guardrail. Only alphanumeric
                          characters and underscores are allowed.
                        example: healthcare_compliance_guardrail
                      guardrail_prompt:
                        type: string
                        description: >-
                          The detailed prompt that defines the behavioral
                          boundaries and restrictions
                        example: >-
                          Never discuss competitor products, share sensitive
                          medical information, or provide medical advice outside
                          approved guidelines
                      modality:
                        type: string
                        description: >-
                          The communication modality for an individual
                          guardrail. If set to `verbal`, the guardrail will be
                          enforced by the user's responses. If set `visual`, the
                          guardrail can only be enforced by visual / perception
                          cues observed by Raven
                        enum:
                          - verbal
                          - visual
                        default: verbal
                        example: verbal
                      callback_url:
                        type: string
                        description: >-
                          URL that will receive notifications when the guardrail
                          is triggered
                        example: https://your-server.com/guardrails-webhook
                      created_at:
                        type: string
                        description: ISO 8601 timestamp of when the guardrails were created
                        example: '2024-01-15T10:30:00Z'
                      updated_at:
                        type: string
                        description: >-
                          ISO 8601 timestamp of when the guardrails were last
                          updated
                        example: '2024-01-15T10:30:00Z'
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