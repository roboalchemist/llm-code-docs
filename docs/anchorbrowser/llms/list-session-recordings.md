# Source: https://docs.anchorbrowser.io/api-reference/session-recordings/list-session-recordings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List Session Recordings

> Retrieves the URLs of the browser session's video recordings. Requires a valid API key for authentication.



## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/{session_id}/recordings
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
  /v1/sessions/{session_id}/recordings:
    get:
      tags:
        - Session Recordings
      summary: List Session Recordings
      description: >-
        Retrieves the URLs of the browser session's video recordings. Requires a
        valid API key for authentication.
      parameters:
        - in: path
          name: session_id
          required: true
          description: The ID of the browser session to retrieve recordings for.
          schema:
            type: string
      responses:
        '200':
          description: A set of recording URLs associated with the browser session.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RecordingListResponse'
        '401':
          description: Invalid API Key.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Session recordings not found.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '429':
          description: Too many requests, please try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    RecordingListResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            count:
              type: integer
              description: Total number of video recordings
            items:
              type: array
              items:
                $ref: '#/components/schemas/RecordingItem'
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
    RecordingItem:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the recording
        is_primary:
          type: boolean
          description: Indicates if this is the primary recording
        file_link:
          type: string
          description: URL to access the recording file
        suggested_file_name:
          type: string
          description: Suggested filename for the recording
        duration:
          type: string
          description: Duration of the recording
        size:
          type: number
          description: Size of the recording file in bytes
        created_at:
          type: string
          format: date-time
          description: Timestamp when the recording was created
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````