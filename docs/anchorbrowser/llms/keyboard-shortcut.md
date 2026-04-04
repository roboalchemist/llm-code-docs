# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/keyboard-shortcut.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Keyboard Shortcut

> Performs a keyboard shortcut using the specified keys



## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/keyboard/shortcut
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
  /v1/sessions/{sessionId}/keyboard/shortcut:
    post:
      tags:
        - OS Level Control
      summary: Keyboard Shortcut
      description: Performs a keyboard shortcut using the specified keys
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
              $ref: '#/components/schemas/KeyboardShortcutRequestSchema'
      responses:
        '200':
          description: Shortcut performed successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
        '400':
          description: Invalid parameters
        '404':
          description: Session not found
        '500':
          description: Failed to perform shortcut
      security:
        - api_key_header: []
components:
  schemas:
    KeyboardShortcutRequestSchema:
      type: object
      required:
        - keys
      properties:
        keys:
          type: array
          description: Array of keys to press simultaneously
          items:
            type: string
        holdTime:
          type: integer
          description: Time to hold the keys down in milliseconds
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````