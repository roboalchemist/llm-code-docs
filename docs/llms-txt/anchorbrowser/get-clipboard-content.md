# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/get-clipboard-content.md

# Get Clipboard Content

> Retrieves the current content of the clipboard

## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/{sessionId}/clipboard
paths:
  path: /v1/sessions/{sessionId}/clipboard
  method: get
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
              data:
                allOf:
                  - type: object
                    properties:
                      text:
                        type: string
                        description: Text content of the clipboard
            refIdentifier: '#/components/schemas/ClipboardResponseSchema'
        examples:
          example:
            value:
              data:
                text: <string>
        description: Clipboard content retrieved successfully
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
            description: Failed to get clipboard content
        examples: {}
        description: Failed to get clipboard content
  deprecated: false
  type: path
components:
  schemas: {}

````