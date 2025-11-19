# Source: https://docs.tavus.io/api-reference/guardrails/create-guardrails.md

# Create Guardrails

> This endpoint creates a new set of guardrails for a persona. Guardrails provide strict behavioral boundaries and guidelines that will be rigorously followed throughout conversations.


## OpenAPI

````yaml post /v2/guardrails
paths:
  path: /v2/guardrails
  method: post
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    description: >-
                      A descriptive name for the collection of individual
                      guardrails
              data:
                allOf:
                  - type: array
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
                            medical information, or provide medical advice
                            outside approved guidelines
                        modality:
                          type: string
                          description: >-
                            The communication modality for the guardrail. If set
                            to `verbal`, the guardrail will be enforced by the
                            user's responses. If set `visual`, the guardrail can
                            only be enforced by visual / perception cues
                            observed by Raven
                          enum:
                            - verbal
                            - visual
                          default: verbal
                          example: verbal
                        callback_url:
                          type: string
                          description: >-
                            Optional URL that will receive notifications when
                            the guardrail is triggered
                          example: https://your-server.com/guardrails-webhook
                      required:
                        - guardrail_name
                        - guardrail_prompt
        examples:
          example:
            value:
              name: <string>
              data:
                - guardrail_name: healthcare_compliance_guardrail
                  guardrail_prompt: >-
                    Never discuss competitor products, share sensitive medical
                    information, or provide medical advice outside approved
                    guidelines
                  modality: verbal
                  callback_url: https://your-server.com/guardrails-webhook
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              guardrails_id:
                allOf:
                  - type: string
                    description: Unique identifier for the created guardrails
                    example: g12345
              guardrails_name:
                allOf:
                  - type: string
                    description: Name of the guardrails
                    example: Healthcare Compliance Guardrails
              status:
                allOf:
                  - type: string
                    description: Current status of the guardrails
                    example: active
              created_at:
                allOf:
                  - type: string
                    description: ISO 8601 timestamp of when the guardrails were created
                    example: '2024-01-15T10:30:00Z'
        examples:
          example:
            value:
              guardrails_id: g12345
              guardrails_name: Healthcare Compliance Guardrails
              status: active
              created_at: '2024-01-15T10:30:00Z'
        description: Guardrails created successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    description: Error message describing the validation failure
                    example: guardrail_name is required
        examples:
          example:
            value:
              message: guardrail_name is required
        description: Bad Request - Invalid input parameters
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