# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/type-text.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Type Text

> Types the specified text with optional delay between keystrokes



## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/keyboard/type
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
  /v1/sessions/{sessionId}/keyboard/type:
    post:
      tags:
        - OS Level Control
      summary: Type Text
      description: Types the specified text with optional delay between keystrokes
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
              $ref: '#/components/schemas/TypeTextRequestSchema'
      responses:
        '200':
          description: Text typed successfully
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
          description: Failed to type text
      security:
        - api_key_header: []
components:
  schemas:
    TypeTextRequestSchema:
      type: object
      required:
        - text
      properties:
        text:
          type: string
          description: Text to type
        delay:
          type: integer
          description: Delay between keystrokes in milliseconds
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````