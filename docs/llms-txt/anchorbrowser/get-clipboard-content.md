# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/get-clipboard-content.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Clipboard Content

> Retrieves the current content of the clipboard



## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/{sessionId}/clipboard
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
    get:
      tags:
        - OS Level Control
      summary: Get Clipboard Content
      description: Retrieves the current content of the clipboard
      parameters:
        - name: sessionId
          in: path
          required: true
          description: The ID of the browser session
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Clipboard content retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ClipboardResponseSchema'
        '404':
          description: Session not found
        '500':
          description: Failed to get clipboard content
      security:
        - api_key_header: []
components:
  schemas:
    ClipboardResponseSchema:
      type: object
      properties:
        data:
          type: object
          properties:
            text:
              type: string
              description: Text content of the clipboard
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````