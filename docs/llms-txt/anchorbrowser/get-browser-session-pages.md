# Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/get-browser-session-pages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Browser Session Pages

> Retrieves a list of pages associated with a specific browser session.



## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/{session_id}/pages
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
  /v1/sessions/{session_id}/pages:
    get:
      tags:
        - Browser Sessions
      summary: Get Browser Session Pages
      description: Retrieves a list of pages associated with a specific browser session.
      parameters:
        - in: path
          name: session_id
          required: true
          description: The ID of the session to retrieve pages for.
          schema:
            type: string
      responses:
        '200':
          description: Session pages retrieved successfully.
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      description: The unique identifier of the page.
                    title:
                      type: string
                      description: The title of the page.
                    url:
                      type: string
                      description: The URL of the page.
                    frontend_url:
                      type: string
                      description: The frontend URL for accessing the page.
                  required:
                    - id
                    - title
                    - url
                    - frontend_url
        '401':
          description: Invalid API Key or unauthorized access.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Session not found.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Internal server error.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
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