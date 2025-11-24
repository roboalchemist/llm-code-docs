# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/mouse-up.md

# Mouse Up

> Performs a mouse button up action at the specified coordinates

## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/mouse/up
paths:
  path: /v1/sessions/{sessionId}/mouse/up
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
              x:
                allOf:
                  - type: integer
                    description: X coordinate
              'y':
                allOf:
                  - type: integer
                    description: Y coordinate
              button:
                allOf:
                  - type: string
                    description: Mouse button to use
                    enum:
                      - left
                      - middle
                      - right
            required: true
            refIdentifier: '#/components/schemas/CoordinatesRequestSchema'
            requiredProperties:
              - x
              - 'y'
        examples:
          example:
            value:
              x: 123
              'y': 123
              button: left
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
        description: Mouse up performed successfully
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Invalid coordinates or parameters
        examples: {}
        description: Invalid coordinates or parameters
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
            description: Failed to perform mouse up
        examples: {}
        description: Failed to perform mouse up
  deprecated: false
  type: path
components:
  schemas: {}

````