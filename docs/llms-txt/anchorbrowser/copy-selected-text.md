# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/copy-selected-text.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Copy Selected Text

> Copies the currently selected text to the clipboard



## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/copy
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
  /v1/sessions/{sessionId}/copy:
    post:
      tags:
        - OS Level Control
      summary: Copy Selected Text
      description: Copies the currently selected text to the clipboard
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
          description: Text copied successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CopyResponseSchema'
        '404':
          description: Session not found
        '500':
          description: Failed to copy text
      security:
        - api_key_header: []
components:
  schemas:
    CopyResponseSchema:
      type: object
      properties:
        text:
          type: string
          description: The text that was copied
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````