# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/paste-text.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Paste Text

> Pastes text at the current cursor position



## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/paste
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
  /v1/sessions/{sessionId}/paste:
    post:
      tags:
        - OS Level Control
      summary: Paste Text
      description: Pastes text at the current cursor position
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
              $ref: '#/components/schemas/PasteRequestSchema'
      responses:
        '200':
          description: Text pasted successfully
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
          description: Failed to paste text
      security:
        - api_key_header: []
components:
  schemas:
    PasteRequestSchema:
      type: object
      required:
        - text
      properties:
        text:
          type: string
          description: Text to paste
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````