# Source: https://docs.anchorbrowser.io/api-reference/session-recordings/pause-session-recording.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Pause Session Recording

> Pauses the video recording for the specified browser session.



## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{session_id}/recordings/pause
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
  /v1/sessions/{session_id}/recordings/pause:
    post:
      tags:
        - Session Recordings
      summary: Pause Session Recording
      description: Pauses the video recording for the specified browser session.
      parameters:
        - in: path
          name: session_id
          required: true
          description: The ID of the browser session for which to pause recording.
          schema:
            type: string
      responses:
        '200':
          description: Recording paused successfully.
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    $ref: '#/components/schemas/SuccessResponse'
        '401':
          description: Invalid API Key.
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Session not found.
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to pause recording.
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
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