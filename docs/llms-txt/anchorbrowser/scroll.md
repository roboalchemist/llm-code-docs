# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/scroll.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Scroll

> Performs a scroll action at the specified coordinates



## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/scroll
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
  /v1/sessions/{sessionId}/scroll:
    post:
      tags:
        - OS Level Control
      summary: Scroll
      description: Performs a scroll action at the specified coordinates
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
              $ref: '#/components/schemas/ScrollRequestSchema'
      responses:
        '200':
          description: Scroll performed successfully
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
          description: Failed to perform scroll
      security:
        - api_key_header: []
components:
  schemas:
    ScrollRequestSchema:
      allOf:
        - $ref: '#/components/schemas/CoordinatesRequestSchema'
        - type: object
          required:
            - deltaY
          properties:
            deltaX:
              type: integer
              description: Horizontal scroll amount (positive is right, negative is left)
            deltaY:
              type: integer
              description: Vertical scroll amount (positive is down, negative is up)
            steps:
              type: integer
              description: Number of steps to break the scroll into for smoother scrolling
            useOs:
              type: boolean
              description: Whether to use the OS scroll or the Playwright scroll
    CoordinatesRequestSchema:
      type: object
      required:
        - x
        - 'y'
      properties:
        x:
          type: integer
          description: X coordinate
        'y':
          type: integer
          description: Y coordinate
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````