# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/set-clipboard-content.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Set Clipboard Content

> Sets the content of the clipboard



## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/clipboard
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
  /v1/sessions/{sessionId}/clipboard:
    post:
      tags:
        - OS Level Control
      summary: Set Clipboard Content
      description: Sets the content of the clipboard
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
              $ref: '#/components/schemas/ClipboardRequestSchema'
      responses:
        '200':
          description: Clipboard content set successfully
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
          description: Failed to set clipboard content
      security:
        - api_key_header: []
components:
  schemas:
    ClipboardRequestSchema:
      type: object
      required:
        - text
      properties:
        text:
          type: string
          description: Text to set in the clipboard
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````