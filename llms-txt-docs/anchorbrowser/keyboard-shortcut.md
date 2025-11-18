# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/keyboard-shortcut.md

# Keyboard Shortcut

> Performs a keyboard shortcut using the specified keys

## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/keyboard/shortcut
paths:
  path: /v1/sessions/{sessionId}/keyboard/shortcut
  method: post
  servers:
    - url: https://api.anchorbrowser.io
      description: API server
  request:
    security:
      - title: api key header
        parameters:
          query: {}
          header:
            anchor-api-key:
              type: apiKey
              description: API key passed in the header
          cookie: {}
    parameters:
      path:
        sessionId:
          schema:
            - type: string
              required: true
              description: The ID of the browser session
              format: uuid
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              keys:
                allOf:
                  - type: array
                    description: Array of keys to press simultaneously
                    items:
                      type: string
              holdTime:
                allOf:
                  - type: integer
                    description: Time to hold the keys down in milliseconds
            required: true
            refIdentifier: '#/components/schemas/KeyboardShortcutRequestSchema'
            requiredProperties:
              - keys
        examples:
          example:
            value:
              keys:
                - <string>
              holdTime: 123
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: string
        examples:
          example:
            value:
              status: <string>
        description: Shortcut performed successfully
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Invalid parameters
        examples: {}
        description: Invalid parameters
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Session not found
        examples: {}
        description: Session not found
    '500':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Failed to perform shortcut
        examples: {}
        description: Failed to perform shortcut
  deprecated: false
  type: path
components:
  schemas: {}

````