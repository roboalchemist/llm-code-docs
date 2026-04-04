# Source: https://docs.anchorbrowser.io/api-reference/os-level-control/take-screenshot.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Take Screenshot

> Takes a screenshot of the current browser session and returns it as an image.



## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/{sessionId}/screenshot
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
  /v1/sessions/{sessionId}/screenshot:
    get:
      tags:
        - OS Level Control
      summary: Take Screenshot
      description: >-
        Takes a screenshot of the current browser session and returns it as an
        image.
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
          description: Screenshot taken successfully
          content:
            image/png:
              schema:
                type: string
                format: binary
        '404':
          description: Session not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
        '500':
          description: Failed to take screenshot
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
      security:
        - api_key_header: []
components:
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````