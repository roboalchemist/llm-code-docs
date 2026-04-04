# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/drag-and-drop.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Drag and Drop

> Performs a drag and drop operation from start coordinates to end coordinates



## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/drag-and-drop
openapi: 3.1.0
info:
  title: AnchorBrowser API
  version: 1.0.0
  description: APIs to manage all browser-related actions and configuration.
servers:
  - url: https://api.anchorbrowser.io
    description: API server
security: []
paths:
  /v1/sessions/{sessionId}/drag-and-drop:
    post:
      tags:
        - OS Level Control
      summary: Drag and Drop
      description: >-
        Performs a drag and drop operation from start coordinates to end
        coordinates
      parameters:
        - name: sessionId
          in: path
          required: true
          description: The ID of the browser session
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DragDropRequestSchema'
      responses:
        '200':
          description: Drag and drop performed successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
        '400':
          description: Invalid coordinates or parameters
        '404':
          description: Session not found
        '500':
          description: Failed to perform drag and drop
      security:
        - api_key_header: []
components:
  schemas:
    DragDropRequestSchema:
      type: object
      required:
        - startX
        - startY
        - endX
        - endY
      properties:
        startX:
          type: integer
          description: Starting X coordinate
        startY:
          type: integer
          description: Starting Y coordinate
        endX:
          type: integer
          description: Ending X coordinate
        endY:
          type: integer
          description: Ending Y coordinate
        button:
          type: string
          description: Mouse button to use
          enum:
            - left
            - middle
            - right
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````