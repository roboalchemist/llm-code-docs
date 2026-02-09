# Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/end-browser-session.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# End Browser Session

> Deletes the browser session associated with the provided browser session ID. Requires a valid API key for authentication.



## OpenAPI

````yaml openapi-mintlify.yaml delete /v1/sessions/{session_id}
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
  /v1/sessions/{session_id}:
    delete:
      tags:
        - Browser Sessions
      summary: End Browser Session
      description: >-
        Deletes the browser session associated with the provided browser session
        ID. Requires a valid API key for authentication.
      parameters:
        - in: path
          name: session_id
          required: true
          description: The ID of the browser session to end.
          schema:
            type: string
      responses:
        '200':
          description: Browser session ended successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '401':
          description: Invalid API Key or browser session ID
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    SuccessResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            status:
              type: string
    ErrorResponse:
      type: object
      properties:
        error:
          type: object
          properties:
            code:
              type: integer
            message:
              type: string
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````