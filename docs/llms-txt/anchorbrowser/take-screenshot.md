# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/take-screenshot.md

# Take Screenshot

> Takes a screenshot of the current browser session and returns it as an image.

## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/{sessionId}/screenshot
paths:
  path: /v1/sessions/{sessionId}/screenshot
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
      image/png:
        schemaArray:
          - type: file
            contentEncoding: binary
        examples:
          example: {}
        description: Screenshot taken successfully
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
        examples:
          example:
            value:
              error: <string>
        description: Session not found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
        examples:
          example:
            value:
              error: <string>
        description: Failed to take screenshot
  deprecated: false
  type: path
components:
  schemas: {}

````