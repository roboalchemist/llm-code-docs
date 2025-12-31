# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/scroll.md

# Scroll

> Performs a scroll action at the specified coordinates

## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/scroll
paths:
  path: /v1/sessions/{sessionId}/scroll
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
              deltaX:
                allOf:
                  - type: integer
                    description: >-
                      Horizontal scroll amount (positive is right, negative is
                      left)
              deltaY:
                allOf:
                  - type: integer
                    description: Vertical scroll amount (positive is down, negative is up)
              steps:
                allOf:
                  - type: integer
                    description: >-
                      Number of steps to break the scroll into for smoother
                      scrolling
              useOs:
                allOf:
                  - type: boolean
                    description: Whether to use the OS scroll or the Playwright scroll
            required: true
            refIdentifier: '#/components/schemas/CoordinatesRequestSchema'
            requiredProperties:
              - x
              - 'y'
              - deltaY
        examples:
          example:
            value:
              x: 123
              'y': 123
              deltaX: 123
              deltaY: 123
              steps: 123
              useOs: true
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
        description: Scroll performed successfully
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
            description: Failed to perform scroll
        examples: {}
        description: Failed to perform scroll
  deprecated: false
  type: path
components:
  schemas: {}

````