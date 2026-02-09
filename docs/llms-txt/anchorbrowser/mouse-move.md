# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/mouse-move.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Mouse Move

> Moves the mouse cursor to the specified coordinates



## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/mouse/move
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
  /v1/sessions/{sessionId}/mouse/move:
    post:
      tags:
        - OS Level Control
      summary: Mouse Move
      description: Moves the mouse cursor to the specified coordinates
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
              $ref: '#/components/schemas/CoordinatesRequestSchema'
      responses:
        '200':
          description: Mouse move performed successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
        '400':
          description: Invalid coordinates
        '404':
          description: Session not found
        '500':
          description: Failed to perform mouse move
      security:
        - api_key_header: []
components:
  schemas:
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