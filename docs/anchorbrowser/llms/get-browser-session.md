# Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/get-browser-session.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Browser Session

> Retrieves detailed information about a specific browser session.



## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/{session_id}
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
    get:
      tags:
        - Browser Sessions
      summary: Get Browser Session
      description: Retrieves detailed information about a specific browser session.
      parameters:
        - in: path
          name: session_id
          required: true
          description: The ID of the session to retrieve.
          schema:
            type: string
      responses:
        '200':
          description: Session retrieved successfully.
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    description: The session data.
                    properties:
                      session_id:
                        type: string
                        description: The unique identifier of the session.
                      team_id:
                        type: string
                        description: The team ID associated with the session.
                      duration:
                        type: integer
                        description: The duration of the session in seconds.
                      status:
                        type: string
                        description: The current status of the session.
                      credits_used:
                        type: number
                        description: The number of credits consumed by the session.
                      configuration:
                        type: object
                        description: The configuration settings for the session.
                      playground:
                        type: boolean
                        description: Whether this is a playground session.
                      proxy_bytes:
                        type: integer
                        description: The number of bytes transferred through the proxy.
                      tokens:
                        type: object
                        description: Token usage information.
                      steps:
                        type: array
                        items:
                          type: object
                        description: Array of steps executed in the session.
                      tags:
                        type: object
                        description: Tags associated with the session.
                      created_at:
                        type: string
                        format: date-time
                        description: The timestamp when the session was created.
        '404':
          description: Session not found.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to fetch session.
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