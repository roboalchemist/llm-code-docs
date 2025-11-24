# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/drag-and-drop.md

# Drag and Drop

> Performs a drag and drop operation from start coordinates to end coordinates

## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/drag-and-drop
paths:
  path: /v1/sessions/{sessionId}/drag-and-drop
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
              startX:
                allOf:
                  - type: integer
                    description: Starting X coordinate
              startY:
                allOf:
                  - type: integer
                    description: Starting Y coordinate
              endX:
                allOf:
                  - type: integer
                    description: Ending X coordinate
              endY:
                allOf:
                  - type: integer
                    description: Ending Y coordinate
              button:
                allOf:
                  - type: string
                    description: Mouse button to use
                    enum:
                      - left
                      - middle
                      - right
            required: true
            refIdentifier: '#/components/schemas/DragDropRequestSchema'
            requiredProperties:
              - startX
              - startY
              - endX
              - endY
        examples:
          example:
            value:
              startX: 123
              startY: 123
              endX: 123
              endY: 123
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
        description: Drag and drop performed successfully
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
            description: Failed to perform drag and drop
        examples: {}
        description: Failed to perform drag and drop
  deprecated: false
  type: path
components:
  schemas: {}

````