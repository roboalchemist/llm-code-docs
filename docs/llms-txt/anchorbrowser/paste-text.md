# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/paste-text.md

# Paste Text

> Pastes text at the current cursor position

## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/paste
paths:
  path: /v1/sessions/{sessionId}/paste
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
              text:
                allOf:
                  - type: string
                    description: Text to paste
            required: true
            refIdentifier: '#/components/schemas/PasteRequestSchema'
            requiredProperties:
              - text
        examples:
          example:
            value:
              text: <string>
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
        description: Text pasted successfully
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
            description: Failed to paste text
        examples: {}
        description: Failed to paste text
  deprecated: false
  type: path
components:
  schemas: {}

````