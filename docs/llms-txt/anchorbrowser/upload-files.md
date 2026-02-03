# Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/upload-files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload Files

> Upload files directly to a browser session for use with web forms and file inputs.

Files are saved to the session's uploads directory and can be referenced in CDP commands.




## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/uploads
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
  /v1/sessions/{sessionId}/uploads:
    post:
      tags:
        - Browser Sessions
      summary: Upload Files
      description: >
        Upload files directly to a browser session for use with web forms and
        file inputs.


        Files are saved to the session's uploads directory and can be referenced
        in CDP commands.
      parameters:
        - name: sessionId
          in: path
          required: true
          description: The browser session ID
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              required:
                - file
              properties:
                file:
                  type: string
                  format: binary
                  description: File to upload to the browser session
      responses:
        '200':
          description: File uploaded successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      status:
                        type: string
                      message:
                        type: string
        '400':
          description: Invalid request (no file uploaded or file too large)
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: object
                    properties:
                      code:
                        type: integer
                      message:
                        type: string
        '404':
          description: Session not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to upload file
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