# Source: https://docs.anchorbrowser.io/api-reference/session-recordings/get-session-recording.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Session Recording

> Downloads the primary recording file for the specified browser session. Returns the recording as an MP4 file.



## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/{session_id}/recordings/primary/fetch
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
  /v1/sessions/{session_id}/recordings/primary/fetch:
    get:
      tags:
        - Session Recordings
      summary: Get Session Recording
      description: >-
        Downloads the primary recording file for the specified browser session.
        Returns the recording as an MP4 file.
      parameters:
        - in: path
          name: session_id
          required: true
          description: The ID of the browser session to download the recording for.
          schema:
            type: string
      responses:
        '200':
          description: The browser session recording file
          content:
            video/mp4:
              schema:
                type: string
                format: binary
        '401':
          description: Invalid API Key - Authentication failed or API key is missing.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Recording not found
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