# Source: https://docs.tavus.io/api-reference/guardrails/create-guardrails.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Guardrails

> This endpoint creates a new set of guardrails for a persona. Guardrails provide strict behavioral boundaries and guidelines that will be rigorously followed throughout conversations.




## OpenAPI

````yaml post /v2/guardrails
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
    post:
      tags:
        - Guardrails
      summary: Create Guardrails
      description: >
        This endpoint creates a new set of guardrails for a persona. Guardrails
        provide strict behavioral boundaries and guidelines that will be
        rigorously followed throughout conversations.
      operationId: createGuardrails
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: >-
                    A descriptive name for the collection of individual
                    guardrails
                data:
                  type: array
                  description: A list of individual guardrails
                  items:
                    type: object
                    properties:
                      guardrail_name:
                        type: string
                        description: >-
                          A descriptive name for the guardrail. Only
                          alphanumeric characters and underscores are allowed.
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
                          The communication modality for the guardrail. If set
                          to `verbal`, the guardrail will be enforced by the
                          user's responses. If set `visual`, the guardrail can
                          only be enforced by visual / perception cues observed
                          by Raven
                        enum:
                          - verbal
                          - visual
                        default: verbal
                        example: verbal
                      callback_url:
                        type: string
                        description: >-
                          Optional URL that will receive notifications when the
                          guardrail is triggered
                        example: https://your-server.com/guardrails-webhook
                    required:
                      - guardrail_name
                      - guardrail_prompt
      responses:
        '200':
          description: Guardrails created successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  guardrails_id:
                    type: string
                    description: Unique identifier for the created guardrails
                    example: g12345
                  guardrails_name:
                    type: string
                    description: Name of the guardrails
                    example: Healthcare Compliance Guardrails
                  status:
                    type: string
                    description: Current status of the guardrails
                    example: active
                  created_at:
                    type: string
                    description: ISO 8601 timestamp of when the guardrails were created
                    example: '2024-01-15T10:30:00Z'
        '400':
          description: Bad Request - Invalid input parameters
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: Error message describing the validation failure
                    example: guardrail_name is required
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