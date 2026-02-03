# Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/list-all-sessions-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List All Sessions Status

> Retrieves status information for all browser sessions associated with the API key.



## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/all/status
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
  /v1/sessions/all/status:
    get:
      tags:
        - Browser Sessions
      summary: List All Sessions Status
      description: >-
        Retrieves status information for all browser sessions associated with
        the API key.
      responses:
        '200':
          description: Successfully retrieved status for all browser sessions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SessionListResponse'
        '401':
          description: Invalid API Key
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
    SessionListResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            count:
              type: integer
              description: Total number of browser sessions
            items:
              type: array
              items:
                $ref: '#/components/schemas/SessionStatus'
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
    SessionStatus:
      type: object
      properties:
        session_id:
          type: string
          description: Unique identifier for the browser session
        status:
          type: string
          description: Current status of the browser session
        tags:
          type: array
          items:
            type: string
          description: Custom labels assigned to this browser session
        created_at:
          type: string
          format: date-time
          description: Timestamp when the browser session was created
      required:
        - session_id
        - status
        - created_at
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````