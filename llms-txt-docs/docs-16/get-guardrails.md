# Source: https://docs.tavus.io/api-reference/guardrails/get-guardrails.md

# Get Guardrails (One Set)

> This endpoint returns a single set of guardrails by its unique identifier.


## OpenAPI

````yaml get /v2/guardrails/{guardrails_id}
paths:
  path: /v2/guardrails/{guardrails_id}
  method: get
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
      path:
        guardrails_id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the guardrails.
              example: g12345
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
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
        examples:
          example:
            value:
              data:
                guardrail_name: healthcare_compliance_guardrail
                guardrail_prompt: >-
                  Never discuss competitor products, share sensitive medical
                  information, or provide medical advice outside approved
                  guidelines
                modality: verbal
                callback_url: https://your-server.com/guardrails-webhook
                created_at: '2024-01-15T10:30:00Z'
                updated_at: '2024-01-15T10:30:00Z'
        description: Successfully retrieved guardrails
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid guardrails_id
        examples:
          example:
            value:
              error: Invalid guardrails_id
        description: Bad Request
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
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message.
                    example: Guardrails not found
        examples:
          example:
            value:
              error: Guardrails not found
        description: Not Found
  deprecated: false
  type: path
components:
  schemas: {}

````