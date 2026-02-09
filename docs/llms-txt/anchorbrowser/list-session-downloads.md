# Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/list-session-downloads.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List Session Downloads

> Retrieves metadata of files downloaded during a browser session. Requires a valid API key for authentication.



## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/{session_id}/downloads
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
  /v1/sessions/{session_id}/downloads:
    get:
      tags:
        - Browser Sessions
      summary: List Session Downloads
      description: >-
        Retrieves metadata of files downloaded during a browser session.
        Requires a valid API key for authentication.
      parameters:
        - in: path
          name: session_id
          required: true
          description: >-
            The unique identifier of the browser session to retrieve downloads
            for.
          schema:
            type: string
      responses:
        '200':
          description: A list of download metadata associated with the browser session.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DownloadListResponse'
        '401':
          description: Invalid or missing API key.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: The browser session or its downloads metadata could not be found.
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
    DownloadListResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            count:
              type: integer
              description: Total number of downloads
            items:
              type: array
              items:
                $ref: '#/components/schemas/DownloadItem'
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
    DownloadItem:
      type: object
      properties:
        id:
          type: string
          description: The unique ID of the download record.
        file_link:
          type: string
          format: uri
          description: >-
            The URL to download the file from anchorbrowser servers. Requires
            api key authentication.
        original_download_url:
          type: string
          format: uri
          description: The URL used to download the file.
        origin_url:
          type: string
          format: uri
          description: The original URL where the file was found.
        suggested_file_name:
          type: string
          description: The suggested file name for saving the file.
        original_file_name:
          type: string
          description: The original file name before any modification.
        duration:
          type: integer
          description: The time it took to process or download the file, in milliseconds.
        size:
          type: integer
          description: The size of the file in bytes.
        created_at:
          type: string
          format: date-time
          description: The timestamp when the file record was created.
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````