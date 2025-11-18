# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/copy-selected-text.md

# Copy Selected Text

> Copies the currently selected text to the clipboard

## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/copy
paths:
  path: /v1/sessions/{sessionId}/copy
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
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              text:
                allOf:
                  - type: string
                    description: The text that was copied
            refIdentifier: '#/components/schemas/CopyResponseSchema'
        examples:
          example:
            value:
              text: <string>
        description: Text copied successfully
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
            description: Failed to copy text
        examples: {}
        description: Failed to copy text
  deprecated: false
  type: path
components:
  schemas: {}

````